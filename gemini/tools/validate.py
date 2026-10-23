"""Validate the Gemini (Antigravity) skill pack.

usage: python tools/validate.py [skills_dir]   (default: skills/ next to this tools/ folder)

Checks frontmatter (Agent Skills spec + Antigravity description style), SKILL.md length, the pack's
Gemini structure (done criteria, preflight, verification steps, few-shot examples), relative links and
heading anchors, and leftovers from other harnesses. Exit 1 on any error.
"""
import pathlib
import re
import sys

import yaml

FRONTMATTER_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}
WHEN = re.compile(r"Use this skill when|Use esta skill quando")
STRUCTURE = {
    "done criteria ('Done when' / 'Pronto quando')": re.compile(r"\*\*(Done when|Pronto quando)"),
    "preflight step ('Step 0' / 'Passo 0')": re.compile(r"^## (Step|Passo) 0", re.M),
    "verification ('Verify:' / 'Verificação:')": re.compile(r"\*\*(Verify|Verificação):\*\*"),
    "examples section": re.compile(r"^## (Examples|Exemplos)", re.M),
}
FOREIGN = re.compile(r"mcp__|javascript_tool|browser_batch|get_page_text|read_page\b|form_input|WebFetch|AskUserQuestion"
                     r"|~/\.claude|CLAUDE_PLUGIN_ROOT|disable-model-invocation|EXECUTION DIRECTIVE|DIRETRIZ DE EXECUÇÃO"
                     r"|agents/openai\.yaml|allow_implicit_invocation|codex exec|tab\.playwright|nodeRepl|apply_patch"
                     r"|GPT-6|~/\.agents/skills|\$[a-z]+(-[a-z]+)+\b")
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
    return re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")


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
    text = (root / "SKILL.md").read_text(encoding="utf-8")
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
    if not WHEN.search(desc):
        errs.append("description lacks an explicit 'Use this skill when' / 'Use esta skill quando' clause")
    if any(not isinstance(v, str) for v in (fm.get("metadata") or {}).values()):
        errs.append("metadata values must be strings")
    if len(text.splitlines()) > 500:
        errs.append(f"SKILL.md has {len(text.splitlines())} lines (> 500)")
    for label, pattern in STRUCTURE.items():
        if not pattern.search(text):
            errs.append(f"SKILL.md lacks {label}")
    if (root / "agents" / "openai.yaml").exists():
        errs.append("agents/openai.yaml belongs to the Codex pack")

    for md in sorted(root.rglob("*.md")):
        rel = md.relative_to(root)
        for n, line in unfenced(md.read_text(encoding="utf-8")):
            hit = FOREIGN.search(line)
            if hit:
                errs.append(f"{rel}:{n}: other-harness term: {hit.group(0)}")
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
