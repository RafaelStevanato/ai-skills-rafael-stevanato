#!/usr/bin/env python3
"""turnitout-ptbr: higieniza prosa e comentários de código em PT-BR, sem LLM, só stdlib."""
import functools
import io
import json
import os
import re
import sys
import tempfile
from pathlib import Path

# motivo: ast, tokenize e subprocess são importados só onde se usam; o hook roda a cada Write/Edit

MARKER_DIR = Path(tempfile.gettempdir())
RULES_PATH = Path(__file__).with_name("rules_ptbr.json")

PROSE_EXTS = {".md", ".txt", ".tex", ".rst", ".adoc"}
C_EXTS = {".js", ".ts", ".tsx", ".jsx", ".go", ".rs", ".c", ".cpp", ".h", ".hpp", ".java", ".php"}
HASH_EXTS = {".sh", ".rb"}
SQL_EXTS = {".sql"}
CODE_EXTS = {".py"} | C_EXTS | HASH_EXTS | SQL_EXTS
EXCLUDED_DIRS = {".claude", ".codex", ".gemini", ".agents"}
EXCLUDED_NAMES = {"claude.md", "agents.md", "gemini.md", "skill.md"}
MAX_BYTES = 2_000_000

ZW_RE = re.compile(r"[\u200b\u200c\u200e\u200f\u202a-\u202e\u2060-\u206f\ufeff\u00ad]")
# motivo: o ZWJ cola emojis compostos (homem programador, bandeira arco-íris); fora disso é lixo
ZWJ_RE = re.compile(
    r"(?<![\U0001F000-\U0001FFFF\u2600-\u27BF\uFE0F])\u200d"
    r"|\u200d(?![\U0001F000-\U0001FFFF\u2600-\u27BF])"
)

TABLE_RE = re.compile(r"[ \t]*\|")
# motivo: sem \s, para o regex nunca juntar linhas; travessão no início da linha (diálogo) fica
EM_RE = re.compile(r"(?<=\S)[ \t]*\u2014[ \t]*(?=\S)")
EN_RE = re.compile(r"(?<=\S)[ \t]+\u2013[ \t]+(?=\S)")

# motivo: grupos nomeados deixam um conectivo novo do JSON ter grupos próprios sem quebrar a numeração
START_HEAD = r"(?P<head>^[ \t]*(?:(?:--|//+|/\*+|#{1,6}|[-*+>])[ \t]+)?|[.!?\u2026][ \t]+)"

PROTECTED_RE = re.compile(
    r"\A---[ \t]*\r?\n[\s\S]*?\r?\n---[ \t]*(?=\r?\n|\Z)"
    r"|(?P<fence>`{3,}|~{3,})[\s\S]*?(?P=fence)"
    r"|`[^`\n]+`"
    r"|\$\$[\s\S]*?\$\$|\$[^$\n]+\$"
    r"|\\begin\{(?:equation|align|gather|lstlisting|verbatim)\*?\}[\s\S]*?"
    r"\\end\{(?:equation|align|gather|lstlisting|verbatim)\*?\}"
    r"|\\(?:cite|ref|eqref|label|includegraphics|usepackage|input|include)\{[^{}]*\}"
    r"|\]\([^)\n]+\)|https?://[^\s)\]>]*[^\s)\]>.,;:!?]"
    # motivo: menção ou citação entre aspas nunca pode ser reescrita
    r'|"[^"\n]*"|\u201c[^\u201d\n]*\u201d|\u00ab[^\u00bb\n]*\u00bb'
)
RESTORE_RE = re.compile(r"\ue000(\d+)\ue001")

DIRECTIVE_RE = re.compile(
    r"^(?://+|#|--|/\*+)\s*(?:@ts-|eslint|prettier-|nolint|noinspection|pragma|type:|noqa|pylint:"
    r"|fmt:|!|go:|\+build|<reference|biome-ignore|istanbul|c8 |jshint|shellcheck)"
)

# motivo: aspas simples não atravessam linha, por causa dos lifetimes do Rust
_STR = r'("(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\\n])*\'|`(?:\\.|[^`\\])*`)'
_C_RE = re.compile(_STR + r"|(//[^\n]*|/\*[\s\S]*?\*/)")
_HASH_RE = re.compile(_STR + r"|((?<![^\s])#[^\n]*)")
_SQL_RE = re.compile(_STR + r"|(--[^\n]*|/\*[\s\S]*?\*/)")

HUNK_RE = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@", re.MULTILINE)


@functools.lru_cache(maxsize=None)
def _rules():
    data = json.loads(RULES_PATH.read_text(encoding="utf-8"))
    alt = "|".join(f"(?:{s})" for s in data["strip_starters"])
    # o + remove conectivos empilhados ("Além disso, vale ressaltar que x" -> "X")
    starters = re.compile(START_HEAD + "(?:" + alt + ")+(?P<next>[^\\W_]|\ue000)", re.IGNORECASE | re.MULTILINE) if alt else None
    lexical = [(re.compile(r["pattern"], re.IGNORECASE), r["replacement"]) for r in data["lexical_replacements"]]
    return starters, lexical


def strip_zw(text):
    return ZWJ_RE.sub("", ZW_RE.sub("", text))


def _expand(m, repl):
    out = m.expand(repl)
    return out[:1].upper() + out[1:] if m.group(0)[:1].isupper() else out


def clean(text):
    starters, lexical = _rules()
    text = text.replace("\u00a0", " ")
    text = "\n".join(
        ln if TABLE_RE.match(ln) else EN_RE.sub(" - ", EM_RE.sub(" - ", ln)) for ln in text.split("\n")
    )
    if starters:
        text = starters.sub(lambda m: m["head"] + m["next"].upper(), text)
    for rx, repl in lexical:
        text = rx.sub(lambda m: _expand(m, repl), text)
    return text


def _prose(text):
    masks = []

    def hide(m):
        masks.append(m.group(0))
        return f"\ue000{len(masks) - 1}\ue001"

    out = clean(PROTECTED_RE.sub(hide, strip_zw(text)))
    return RESTORE_RE.sub(lambda m: masks[int(m.group(1))], out)


def _python(src):
    # motivo: splice em vez de untokenize, que no 3.12 pode alterar f-strings com {{ }}
    import ast
    import tokenize

    try:
        lines = io.StringIO(src).readlines()
        edits = []
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type != tokenize.COMMENT or DIRECTIVE_RE.match(tok.string):
                continue
            new = clean(strip_zw(tok.string))
            if new == tok.string:
                continue
            (row, c0), (_, c1) = tok.start, tok.end
            if lines[row - 1][c0:c1] != tok.string:
                return src
            edits.append((row - 1, c0, c1, new))
        if not edits:
            return src
        for row, c0, c1, new in reversed(edits):
            lines[row] = lines[row][:c0] + new + lines[row][c1:]
        out = "".join(lines)
        return out if ast.dump(ast.parse(out)) == ast.dump(ast.parse(src)) else src
    except Exception:
        return src


def _code(text, rx):
    def swap(m):
        if m.group(1) is not None:
            return m.group(1)
        comment = m.group(2)
        return comment if DIRECTIVE_RE.match(comment) else clean(strip_zw(comment))

    return rx.sub(swap, text)


def sanitize(text, ext):
    if ext in PROSE_EXTS:
        return _prose(text)
    if ext == ".py":
        return _python(text)
    rx = _C_RE if ext in C_EXTS else _HASH_RE if ext in HASH_EXTS else _SQL_RE if ext in SQL_EXTS else None
    return _code(text, rx) if rx else text


def _excluded(p):
    # motivo: skills e regras citam as frases banidas como exemplo e seriam destruídas
    if any(part.lower() in EXCLUDED_DIRS for part in p.parts) or p.name.lower() in EXCLUDED_NAMES:
        return True
    return any(os.path.isfile(os.path.join(d, "SKILL.md")) for d in p.parents)


def process_file(path, allowed=None, write=True):
    p = Path(os.path.abspath(path))
    if p.suffix.lower() not in PROSE_EXTS | CODE_EXTS or not p.is_file() or p.stat().st_size > MAX_BYTES:
        return False
    if _excluded(p):
        return False
    try:
        with open(p, encoding="utf-8", newline="") as f:
            old = f.read()
    except (OSError, UnicodeDecodeError):
        return False
    if "turnitout: off" in old:
        return False
    new = sanitize(old, p.suffix.lower())
    if allowed is not None:
        a, b = old.split("\n"), new.split("\n")
        if len(a) != len(b):
            return False
        new = "\n".join(y if i in allowed else x for i, (x, y) in enumerate(zip(a, b)))
    if new == old:
        return False
    if write:
        with open(p, "w", encoding="utf-8", newline="") as f:
            f.write(new)
    return True


def _edited_lines(path, tool_input):
    news = [tool_input.get("new_string")] + [e.get("new_string") for e in tool_input.get("edits") or []]
    news = [n.replace("\r\n", "\n") for n in news if isinstance(n, str) and n]
    try:
        with open(path, encoding="utf-8", newline="") as f:
            body = f.read().replace("\r\n", "\n")
    except (OSError, UnicodeDecodeError):
        return set()
    lines = set()
    for ns in news:
        i = body.find(ns)
        while i != -1:
            first = body.count("\n", 0, i)
            lines.update(range(first, first + ns.rstrip("\n").count("\n") + 1))
            i = body.find(ns, i + 1)
    return lines


def _git(root, *args):
    import subprocess

    r = subprocess.run(["git", "-C", root, *args], capture_output=True, timeout=5)
    return r.stdout if r.returncode == 0 else None


def _new_lines(diff):
    lines = set()
    for m in HUNK_RE.finditer(diff):
        start, count = int(m.group(1)), int(m.group(2) if m.group(2) is not None else 1)
        lines.update(range(start - 1, start - 1 + count))
    return lines


def _sweep(payload, marker):
    # sem marcador não sabemos quando o turno começou; nunca tocar em arquivos do usuário
    if not marker.exists():
        return
    import subprocess

    try:
        begin = marker.stat().st_mtime
        done = set(marker.read_text(encoding="utf-8").splitlines())
        top = _git(payload.get("cwd") or os.getcwd(), "rev-parse", "--show-toplevel")
        if not top:
            return
        root = top.decode("utf-8").strip()
        status = _git(root, "-c", "core.quotePath=false", "status", "--porcelain", "-z", "-uall")
        entries = (status or b"").decode("utf-8", "replace").split("\0")
        i = 0
        while i < len(entries):
            entry, i = entries[i], i + 1
            if len(entry) < 4:
                continue
            xy, rel = entry[:2], entry[3:]
            origin = []
            if "R" in xy or "C" in xy:
                # a próxima entrada é o caminho de origem; com ele no diff, o renome não vira arquivo novo
                origin, i = entries[i:i + 1], i + 1
            full = os.path.normcase(os.path.abspath(os.path.join(root, rel)))
            if full in done:
                continue
            try:
                if os.path.getmtime(full) < begin:
                    continue
                allowed = None
                if xy != "??":
                    diff = _git(root, "--literal-pathspecs", "diff", "-U0", "--no-color", "--no-ext-diff", "-M",
                                "HEAD", "--", rel, *origin)
                    if diff is not None:
                        allowed = _new_lines(diff.decode("utf-8", "replace"))
                        if not allowed:
                            continue
                process_file(full, allowed)
            except (subprocess.SubprocessError, OSError):
                continue
    except (subprocess.SubprocessError, OSError):
        pass
    finally:
        marker.unlink(missing_ok=True)


def handle(payload):
    sid = re.sub(r"[^\w-]", "", payload.get("session_id") or "default")
    marker = MARKER_DIR / f"turnitout-{sid}.turn"
    if payload.get("hook_event_name") == "UserPromptSubmit":
        marker.write_text("", encoding="utf-8")
        return None
    tool_input = payload.get("tool_input") or {}
    given = tool_input.get("file_path") or tool_input.get("path")
    if not given:
        _sweep(payload, marker)
        return None
    path = os.path.join(payload.get("cwd") or "", given)
    if marker.exists():
        with open(marker, "a", encoding="utf-8") as f:
            f.write(os.path.normcase(os.path.abspath(path)) + "\n")
    allowed = None
    if payload.get("tool_name") != "Write":
        # Edit só higieniza o que o Claude escreveu, nunca o texto antigo do usuário
        allowed = _edited_lines(path, tool_input)
        if not allowed:
            return None
    if process_file(path, allowed):
        return f"turnitout-ptbr higienizou {path}. Releia o arquivo antes de editá-lo de novo."
    return None


def _help():
    return (
        "Uso: turnitout_ptbr.py [--all] [--check] ARQUIVO...\n"
        "     turnitout_ptbr.py   (sem argumentos: modo hook, JSON no stdin)\n"
        "\n"
        "Higieniza texto em PT-BR: conectivos de IA no início de frase, clichês de tradução,\n"
        "travessão e caracteres invisíveis. Em código, altera só os comentários.\n"
        "\n"
        "  --all    higieniza o arquivo inteiro (padrão: em arquivo rastreado pelo git,\n"
        "           só as linhas alteradas em relação ao HEAD)\n"
        "  --check  não grava; imprime os caminhos que mudariam\n"
        "  -h       mostra esta ajuda\n"
        "\n"
        "Saída: 0 = ok. Com --check, 1 = algum arquivo mudaria. 2 = uso inválido ou arquivo inexistente.\n"
        f"Prosa: {' '.join(sorted(PROSE_EXTS))}\n"
        f"Código (só comentários): {' '.join(sorted(CODE_EXTS))}\n"
        'Ignora: trechos entre aspas ou crases, arquivos com "turnitout: off", pastas .claude .codex\n'
        ".gemini .agents, arquivos CLAUDE.md AGENTS.md GEMINI.md SKILL.md e pastas de skill."
    )


def _changed_lines(p):
    # None = arquivo inteiro (fora do git, sem rastreio ou sem HEAD); set = linhas alteradas vs HEAD
    # motivo: --literal-pathspecs, senão "a[1].md" casaria com "a1.md" como glob
    import subprocess

    try:
        if _git(str(p.parent), "--literal-pathspecs", "ls-files", "--error-unmatch", "--", p.name) is None:
            return None
        diff = _git(str(p.parent), "--literal-pathspecs", "diff", "-U0", "--no-color", "--no-ext-diff",
                    "HEAD", "--", p.name)
    except (subprocess.SubprocessError, OSError):
        return None
    return None if diff is None else _new_lines(diff.decode("utf-8", "replace"))


def cli(argv):
    import argparse

    class Parser(argparse.ArgumentParser):
        def error(self, message):
            self.exit(2, f"turnitout_ptbr.py: uso inválido ({message}). Rode com --help.\n")

    # a ajuda inteira vai na descrição: o texto automático do argparse sai em inglês
    ap = Parser(prog="turnitout_ptbr.py", usage=argparse.SUPPRESS, add_help=False,
                formatter_class=argparse.RawDescriptionHelpFormatter, description=_help())
    ap.add_argument("-h", "--help", action="help", help=argparse.SUPPRESS)
    ap.add_argument("--all", action="store_true", help=argparse.SUPPRESS)
    ap.add_argument("--check", action="store_true", help=argparse.SUPPRESS)
    ap.add_argument("files", nargs="*", help=argparse.SUPPRESS)
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    args, extra = ap.parse_known_args(argv)
    if extra:
        ap.error("opção desconhecida: " + " ".join(extra))
    if not args.files:
        ap.error("falta ARQUIVO")
    missing = would = False
    for name in args.files:
        if not os.path.isfile(name):
            print(f"turnitout_ptbr.py: arquivo não encontrado: {name}", file=sys.stderr)
            missing = True
            continue
        p = Path(os.path.abspath(name))
        if process_file(p, None if args.all else _changed_lines(p), write=not args.check):
            print(name if args.check else f"higienizado: {name}")
            would = would or args.check
    return 2 if missing else int(would)


def main():
    if len(sys.argv) > 1:
        try:
            return cli(sys.argv[1:])
        except Exception as e:
            print(f"turnitout_ptbr.py: erro: {e}", file=sys.stderr)
            return 2
    try:
        raw = sys.stdin.buffer.read()
        # motivo: o stdin do Windows chega em cp1252 no modo texto, e o caminho tem acento
        payload = json.loads(raw.decode("utf-8")) if raw.strip() else {}
        msg = handle(payload)
        if msg and payload.get("hook_event_name") == "PostToolUse":
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": msg}}))
        return 0
    except Exception as e:
        print(f"turnitout-ptbr: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
