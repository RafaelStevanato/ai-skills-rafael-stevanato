#!/usr/bin/env python3
"""Instala ou remove o hook turnitout-ptbr no settings.json do Claude Code (só biblioteca padrão)."""
import argparse
import copy
import json
import os
import shutil
import sys
import time
from pathlib import Path

ENGINE = Path(os.path.abspath(__file__)).with_name("turnitout_ptbr.py")
MARK = "turnitout_ptbr.py"
TIMEOUT = 10
# evento -> matcher (None = o grupo não tem a chave matcher)
EVENTS = {"PostToolUse": "Write|Edit|MultiEdit", "Stop": "", "UserPromptSubmit": None}

HELP = """Uso: install_hooks.py [--settings CAMINHO] [--uninstall]

Instala o hook turnitout-ptbr (PostToolUse, Stop e UserPromptSubmit) no settings.json do Claude Code.
Substitui qualquer hook que cite turnitout_ptbr.py, nunca duplica e faz backup antes de gravar.

  --settings CAMINHO  settings.json a alterar (padrão: ~/.claude/settings.json)
  --uninstall         remove as entradas do turnitout-ptbr
  -h                  mostra esta ajuda

Saída: 0 = ok (ou nada a fazer). 1 = erro (motor ausente, JSON inválido, formato inesperado)."""


def command():
    # motivo: barras normais e aspas nos dois caminhos; o hook roda em bash, inclusive no Windows
    return f'"{Path(sys.executable).as_posix()}" "{ENGINE.as_posix()}"'


def group(matcher):
    entry = {"hooks": [{"type": "command", "command": command(), "timeout": TIMEOUT}]}
    return entry if matcher is None else {"matcher": matcher, **entry}


def strip(hooks):
    """Tira todo comando que cita turnitout_ptbr.py; descarta o que ficar vazio por causa disso."""
    for event in list(hooks):
        kept = []
        for g in hooks[event]:
            inner = g.get("hooks") if isinstance(g, dict) else None
            if not isinstance(inner, list):
                kept.append(g)
                continue
            rest = [h for h in inner if not (isinstance(h, dict) and MARK in str(h.get("command") or ""))]
            if rest or not inner:  # grupo que já nascia vazio não é nosso
                kept.append({**g, "hooks": rest})
        if kept or not hooks[event]:
            hooks[event] = kept
        else:
            del hooks[event]


def apply(data, uninstall):
    hooks = data.get("hooks", {})
    if not isinstance(hooks, dict) or not all(isinstance(v, list) for v in hooks.values()):
        raise ValueError('"hooks" fora do formato esperado (objeto de listas)')
    strip(hooks)
    if not uninstall:
        for event, matcher in EVENTS.items():
            hooks.setdefault(event, []).append(group(matcher))
    if hooks:
        data["hooks"] = hooks
    else:
        data.pop("hooks", None)


def layout(raw):
    # preserva o jeito do arquivo: fim de linha, recuo e quebra de linha final
    eol = "\r\n" if "\r\n" in raw else "\n"
    indent = next((ln[: len(ln) - len(ln.lstrip())] for ln in raw.splitlines() if ln[:1] in (" ", "\t")), "  ")
    return eol, indent, (eol if raw.endswith("\n") or not raw else "")


def run(args):
    uninstall = args.uninstall
    settings = Path(args.settings) if args.settings else Path.home() / ".claude" / "settings.json"
    if not uninstall and not (ENGINE.is_file() and ENGINE.with_name("rules_ptbr.json").is_file()):
        raise ValueError(f"motor não encontrado ao lado do instalador: {ENGINE}")
    raw = settings.read_bytes().decode("utf-8-sig") if settings.is_file() else ""
    data = json.loads(raw) if raw.strip() else {}
    if not isinstance(data, dict):
        raise ValueError(f"{settings} não é um objeto JSON")
    new = copy.deepcopy(data)
    apply(new, uninstall)
    if new == data:
        print(f"nada a fazer: {settings} já está como pedido")
        return 0
    eol, indent, tail = layout(raw)
    out = json.dumps(new, indent=indent, ensure_ascii=False).replace("\n", eol) + tail
    backup = None
    if settings.is_file():
        backup = settings.with_name(f"{settings.name}.bak-turnitout-{time.strftime('%Y%m%d-%H%M%S')}")
        shutil.copy2(settings, backup)
    settings.parent.mkdir(parents=True, exist_ok=True)
    tmp = settings.with_name(settings.name + ".tmp-turnitout")
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(out)
    os.replace(tmp, settings)
    if json.loads(settings.read_bytes().decode("utf-8")) != new:
        raise ValueError(f"{settings} gravado, mas o JSON recarregado difere do esperado")
    print(f"hook {'removido de' if uninstall else 'instalado em'} {settings}")
    if not uninstall:
        print(f"comando: {command()}")
    if backup:
        print(f"backup: {backup}")
    return 0


class Parser(argparse.ArgumentParser):
    def error(self, message):
        self.exit(2, f"install_hooks.py: uso inválido ({message}). Rode com --help.\n")


def main(argv=None):
    # a ajuda inteira vai na descrição: o texto automático do argparse sai em inglês
    ap = Parser(prog="install_hooks.py", usage=argparse.SUPPRESS, add_help=False,
                formatter_class=argparse.RawDescriptionHelpFormatter, description=HELP)
    ap.add_argument("-h", "--help", action="help", help=argparse.SUPPRESS)
    ap.add_argument("--settings", metavar="CAMINHO", help=argparse.SUPPRESS)
    ap.add_argument("--uninstall", action="store_true", help=argparse.SUPPRESS)
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    args, extra = ap.parse_known_args(argv)
    if extra:
        ap.error("opção desconhecida: " + " ".join(extra))
    try:
        return run(args)
    except (OSError, ValueError) as e:  # json.JSONDecodeError é ValueError
        print(f"install_hooks.py: erro: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
