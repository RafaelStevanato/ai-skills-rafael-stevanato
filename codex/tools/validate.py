"""Validate the Codex skill pack.

usage: python tools/validate.py [skills_dir]   (default: skills/ next to this tools/ folder)

Checks frontmatter (Codex skill-creator rules), SKILL.md length, agents/openai.yaml fields,
relative links and heading anchors, and leftovers from other harnesses. Exit 1 on any error.
"""
import pathlib
import re
import sys

import yaml

FRONTMATTER_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}
YAML_KEYS = {"interface": {"display_name", "short_description", "icon_small", "icon_large", "brand_color", "default_prompt"},
             "policy": {"allow_implicit_invocation"}, "dependencies": {"tools"}}
FOREIGN = re.compile(r"mcp__|javascript_tool|browser_batch|get_page_text|read_page|form_input|WebFetch|AskUserQuestion"
                     r"|~/\.claude|CLAUDE_PLUGIN_ROOT|disable-model-invocation|EXECUTION DIRECTIVE|DIRETRIZ DE EXECUÇÃO")
FENCE = re.compile(r"^\s*(```|~~~)")
LINK = re.compile(r"\]\(([^)\s]+)\)")
NAME = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")


def unfenced(text):
    fenced = False
    for n, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line):
            fenced = not fenced
        elif not fenced:
            yield n, line


def slug(heading):
    s = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return s.replace(" ", "-")


def anchors(path, cache={}):
    if path not in cache:
        seen, out = {}, set()
        for _, line in unfenced(path.read_text(encoding="utf-8")):
            m = re.match(r"#{1,6} (.+)", line)
            if m:
                base = slug(m.group(1))
                k = seen.get(base, 0)
                out.add(base if k == 0 else f"{base}-{k}")
                seen[base] = k + 1
        cache[path] = out
    return cache[path]


def check_skill(root):
    errs, warns = [], []
    skill_md = root / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return ["no frontmatter"], warns
    fm = yaml.safe_load(m.group(1)) or {}
    if set(fm) - FRONTMATTER_KEYS:
        errs.append(f"frontmatter keys not allowed: {sorted(set(fm) - FRONTMATTER_KEYS)}")
    name, desc = str(fm.get("name", "")), str(fm.get("description", ""))
    if name != root.name or not NAME.fullmatch(name) or len(name) > 64:
        errs.append(f"bad name {name!r}")
    if not desc or len(desc) > 1024 or "<" in desc or ">" in desc:
        errs.append(f"bad description ({len(desc)} chars)")
    elif len(desc) > 400:
        warns.append(f"description is {len(desc)} chars; Codex shortens long descriptions when many skills compete")
    if any(not isinstance(v, str) for v in (fm.get("metadata") or {}).values()):
        errs.append("metadata values must be strings")
    if len(text.splitlines()) > 500:
        errs.append(f"SKILL.md has {len(text.splitlines())} lines (> 500)")

    oy = root / "agents" / "openai.yaml"
    if oy.exists():
        cfg = yaml.safe_load(oy.read_text(encoding="utf-8")) or {}
        for section, keys in cfg.items():
            if section not in YAML_KEYS or set(keys) - YAML_KEYS[section]:
                errs.append(f"openai.yaml: unknown key in {section!r}")
        ui = cfg.get("interface", {})
        if not 25 <= len(ui.get("short_description", "")) <= 64:
            errs.append(f"openai.yaml: short_description must be 25-64 chars ({len(ui.get('short_description', ''))})")
        if f"${name}" not in ui.get("default_prompt", ""):
            errs.append(f"openai.yaml: default_prompt must mention ${name}")
    else:
        warns.append("no agents/openai.yaml")

    for md in sorted(root.rglob("*.md")):
        rel = md.relative_to(root)
        body = md.read_text(encoding="utf-8")
        for n, line in unfenced(body):
            if FOREIGN.search(line):
                errs.append(f"{rel}:{n}: other-harness term: {FOREIGN.search(line).group(0)}")
            if re.fullmatch(r"\s*\[TODO:.*\]\s*", line):
                errs.append(f"{rel}:{n}: TODO placeholder")
            for target in LINK.findall(line):
                if re.match(r"[a-z]+:", target):
                    continue
                file_part, _, frag = target.partition("#")
                dest = (md.parent / file_part).resolve() if file_part else md
                if not dest.exists():
                    errs.append(f"{rel}:{n}: broken link {target}")
                elif frag and dest.suffix == ".md" and frag not in anchors(dest):
                    errs.append(f"{rel}:{n}: missing anchor {target}")
    return errs, warns


def main():
    skills = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent / "skills"
    failed = False
    for root in sorted(p for p in skills.iterdir() if (p / "SKILL.md").exists()):
        errs, warns = check_skill(root)
        failed |= bool(errs)
        print(f"{'FAIL' if errs else 'ok  '} {root.name}")
        for e in errs:
            print(f"     error: {e}")
        for w in warns:
            print(f"     warn:  {w}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
