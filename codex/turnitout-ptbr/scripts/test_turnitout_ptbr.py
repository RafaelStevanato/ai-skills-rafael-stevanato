"""Testes do turnitout-ptbr. Rode: python test_turnitout_ptbr.py"""
import ast
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import turnitout_ptbr as T  # noqa: E402

SCRIPT = HERE / "turnitout_ptbr.py"
# motivo: caracteres invisíveis entram por chr(), para o código-fonte do teste nunca carregá-los literais
DASH, EN = chr(0x2014), chr(0x2013)
ZWSP, FEFF, SHY, NBSP, ZWJ, VS16 = (chr(c) for c in (0x200B, 0xFEFF, 0x00AD, 0x00A0, 0x200D, 0xFE0F))
MAN, LAPTOP, FLAG, RAINBOW = (chr(c) for c in (0x1F468, 0x1F4BB, 0x1F3F3, 0x1F308))


class TurnitoutTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self._marker_dir = T.MARKER_DIR
        T.MARKER_DIR = self.root / "markers"
        T.MARKER_DIR.mkdir()

    def tearDown(self):
        T.MARKER_DIR = self._marker_dir
        self._tmp.cleanup()

    def put(self, rel, text):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(text.encode("utf-8"))
        return p

    @staticmethod
    def get(p):
        return Path(p).read_bytes().decode("utf-8")

    def test_zero_width_and_em_dash_removal(self):
        self.assertEqual(T.sanitize(f"ab{ZWSP}c{FEFF}d{SHY}e {DASH} f{NBSP}g", ".md"), "abcde - f g")
        self.assertEqual(T.sanitize(f"a{DASH}b e c {EN} d 1{EN}2", ".md"), f"a - b e c - d 1{EN}2")

    def test_ptbr_starters_and_auto_capitalization(self):
        src = f"Vale destacar que o módulo falha sob carga. Além disso, a latência dobra {DASH} afetando o banco."
        self.assertEqual(T.sanitize(src, ".md"), "O módulo falha sob carga. A latência dobra - afetando o banco.")
        self.assertEqual(T.sanitize("Além disso, vale ressaltar que x.", ".md"), "X.")

    def test_lexical_replacements_ptbr(self):
        src = "Esse serviço desempenha um papel fundamental no que tange ao cache com o intuito de alavancar a rede."
        self.assertEqual(T.sanitize(src, ".md"), "Esse serviço é central quanto ao cache para usar a rede.")
        self.assertEqual(T.sanitize("Alavancar a rede.", ".md"), "Usar a rede.")
        self.assertEqual(
            T.sanitize("Vamos mergulhar fundo nos logs e explorar a fundo o cache.", ".md"),
            "Vamos analisar os logs e examinar o cache.",
        )

    def test_markdown_and_latex_protection(self):
        src = (
            "Além disso, o texto muda.\n\n"
            f"```python\n# Além disso {DASH} intacto\nx = 1\n```\n\n"
            "$$\\text{Além disso} = x^2$$\n\n"
            f"Em resumo, fim {DASH} ok.\n"
        )
        want = (
            "O texto muda.\n\n"
            f"```python\n# Além disso {DASH} intacto\nx = 1\n```\n\n"
            "$$\\text{Além disso} = x^2$$\n\n"
            "Fim - ok.\n"
        )
        self.assertEqual(T.sanitize(src, ".md"), want)

    def test_python_ast_and_string_preservation(self):
        src = (
            f'msg = "Vale destacar que {DASH} além disso"\n'
            f"# Além disso, desempenha um papel fundamental {DASH} revisar\n"
        )
        want = f'msg = "Vale destacar que {DASH} além disso"\n# É central - revisar\n'
        out = T.sanitize(src, ".py")
        self.assertEqual(out, want)
        self.assertEqual(ast.dump(ast.parse(out)), ast.dump(ast.parse(src)))

    def test_typescript_comment_vs_string(self):
        src = (
            "// @ts-ignore\n"
            f'const a = "Vale destacar que {DASH} além disso";\n'
            f"const b = `Além disso, ${{x}} {DASH} texto`;\n"
            "// Vale ressaltar que isso alavanca o estado\n"
            f"const c = 'Nesse sentido, ok'; /* Ademais, bloco {DASH} ok */\n"
        )
        want = (
            "// @ts-ignore\n"
            f'const a = "Vale destacar que {DASH} além disso";\n'
            f"const b = `Além disso, ${{x}} {DASH} texto`;\n"
            "// Isso alavanca o estado\n"
            "const c = 'Nesse sentido, ok'; /* Bloco - ok */\n"
        )
        self.assertEqual(T.sanitize(src, ".ts"), want)

    def test_edit_scope_only_new_lines(self):
        p = self.put("a.md", "Além disso, antigo.\nAlém disso, novo.\n")
        msg = T.handle({
            "hook_event_name": "PostToolUse", "tool_name": "Edit", "session_id": "t", "cwd": str(self.root),
            "tool_input": {"file_path": "a.md", "old_string": "x", "new_string": "Além disso, novo."},
        })
        self.assertEqual(self.get(p), "Além disso, antigo.\nNovo.\n")
        self.assertIn("higienizou", msg)

    def test_exclusions_and_optout(self):
        txt = "Além disso, x.\n"
        quoted = 'Evite "desempenha um papel fundamental" no texto.\n'
        files = {
            ".claude/x.md": txt,
            ".codex/x.md": txt,
            ".gemini/x.md": txt,
            ".agents/x.md": txt,
            "skill/SKILL.md": txt,
            "skill/references/r.md": txt,
            "proj/CLAUDE.md": txt,
            "off.md": "turnitout: off\n" + txt,
            "quoted.md": quoted,
        }
        for rel, content in files.items():
            with self.subTest(rel=rel):
                p = self.put(rel, content)
                self.assertFalse(T.process_file(p))
                self.assertEqual(self.get(p), content)
        control = self.put("ok.md", txt)
        self.assertTrue(T.process_file(control))
        self.assertEqual(self.get(control), "X.\n")

    def test_false_positives(self):
        for text in (
            "CJ precisa mergulhar no lago.",
            "Puxe a alavanca da esquerda.",
            "## Em resumo\n\nO jogo acaba.\n",
            f"{DASH} Vamos embora.\n",
            f"texto {DASH}\noutra linha\n",
            "| a  | b  |\n",
        ):
            with self.subTest(text=text):
                self.assertEqual(T.sanitize(text, ".md"), text)
        self.assertEqual(T.sanitize("Uma tapeçaria de sons.", ".md"), "Uma combinação de sons.")
        # conectivo seguido de pontuação não é removido (virava "- z")
        self.assertEqual(T.sanitize(f"Além disso {DASH} z.", ".md"), "Além disso - z.")
        # ponto final não faz parte da URL
        self.assertEqual(T.sanitize("Veja https://x.com/a. Além disso, y.", ".md"), "Veja https://x.com/a. Y.")

    def test_crlf_and_emoji(self):
        p = self.put("crlf.md", "Além disso, x.\r\nLinha.\r\n")
        self.assertTrue(T.process_file(p))
        self.assertEqual(p.read_bytes(), "X.\r\nLinha.\r\n".encode("utf-8"))
        programmer = MAN + ZWJ + LAPTOP
        rainbow = FLAG + VS16 + ZWJ + RAINBOW
        self.assertEqual(T.sanitize(f"{programmer} ok{ZWSP}", ".md"), f"{programmer} ok")
        self.assertEqual(T.sanitize(f"{rainbow} a{ZWJ}b", ".md"), f"{rainbow} ab")

    def test_python_guards(self):
        broken = "def f(:\n    pass  # Além disso, x\n"
        self.assertEqual(T.sanitize(broken, ".py"), broken)
        src = 'x = 1\ns = f"{{x}}"  # Além disso, comentário\n'
        self.assertEqual(T.sanitize(src, ".py"), 'x = 1\ns = f"{{x}}"  # Comentário\n')

    def test_shell_comment(self):
        src = f'#!/bin/sh\necho "a // b {DASH} c"  # Além disso, comentário\n'
        want = f'#!/bin/sh\necho "a // b {DASH} c"  # Comentário\n'
        self.assertEqual(T.sanitize(src, ".sh"), want)

    def test_stop_turn_scope(self):
        if not shutil.which("git"):
            self.skipTest("git ausente")
        repo = self.root / "repo"
        repo.mkdir()

        def git(*args):
            subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)

        git("init", "-q")
        for key, value in (("user.name", "t"), ("user.email", "t@t"), ("core.autocrlf", "false"),
                           ("commit.gpgsign", "false")):
            git("config", key, value)
        a = self.put("repo/a.md", "Além disso, velho.\nmeio\n")
        c = self.put("repo/c.md", "ok\n")
        git("add", ".")
        git("commit", "-q", "-m", "init")
        self.put("repo/c.md", "Além disso, do usuário.\n")
        past = time.time() - 3600
        os.utime(c, (past, past))
        base = {"session_id": "s1", "cwd": str(repo)}
        T.handle({**base, "hook_event_name": "UserPromptSubmit"})
        with open(a, "ab") as f:
            f.write("Além disso, novo pelo bash.\n".encode("utf-8"))
        d = self.put("repo/d.md", "Além disso, arquivo novo.\n")
        T.handle({**base, "hook_event_name": "Stop"})
        self.assertEqual(self.get(a), "Além disso, velho.\nmeio\nNovo pelo bash.\n")
        self.assertEqual(self.get(c), "Além disso, do usuário.\n")
        self.assertEqual(self.get(d), "Arquivo novo.\n")
        self.assertEqual(list(T.MARKER_DIR.iterdir()), [])

    def test_stdin_utf8_path(self):
        f = self.put("Vídeos/a.md", "Além disso, x.")
        payload = {
            "hook_event_name": "PostToolUse", "tool_name": "Write", "session_id": "utf8-test",
            "cwd": str(self.root), "tool_input": {"file_path": str(f)},
        }
        r = subprocess.run([sys.executable, str(SCRIPT)], input=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
                           capture_output=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.get(f), "X.")
        out = json.loads(r.stdout)["hookSpecificOutput"]
        self.assertEqual(out["hookEventName"], "PostToolUse")
        self.assertIn("higienizou", out["additionalContext"])

    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)], capture_output=True)

    def make_repo(self):
        # a.md fica rastreado e confirmado; depois ganha uma linha nova sem commit
        if not shutil.which("git"):
            self.skipTest("git ausente")
        repo = self.root / "repo"
        repo.mkdir()
        for args in (("init", "-q"), ("config", "user.name", "t"), ("config", "user.email", "t@t"),
                     ("config", "core.autocrlf", "false"), ("config", "commit.gpgsign", "false")):
            subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)
        a = self.put("repo/a.md", "Além disso, velho.\nmeio\n")
        for args in (("add", "."), ("commit", "-q", "-m", "init")):
            subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)
        with open(a, "ab") as f:
            f.write("Além disso, novo.\n".encode("utf-8"))
        return a

    def test_cli_untracked_file_whole(self):
        p = self.put("n/a.md", "Além disso, um.\nAdemais, dois.\n")
        r = self.run_cli(p)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stdout.decode("utf-8").strip(), f"higienizado: {p}")
        self.assertEqual(self.get(p), "Um.\nDois.\n")

    def test_cli_check_never_writes(self):
        p = self.put("c.md", "Além disso, x.\n")
        r = self.run_cli("--check", p)
        self.assertEqual((r.returncode, r.stdout.decode("utf-8").strip()), (1, str(p)))
        self.assertEqual(self.get(p), "Além disso, x.\n")
        self.assertEqual(self.run_cli(p).returncode, 0)
        r = self.run_cli("--check", p)
        self.assertEqual((r.returncode, r.stdout), (0, b""))
        r = self.run_cli("--check", self.root / "nao-existe.md")
        self.assertEqual(r.returncode, 2)
        self.assertIn("não encontrado", r.stderr.decode("utf-8"))

    def test_cli_tracked_file_only_new_lines(self):
        a = self.make_repo()
        r = self.run_cli(a)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.get(a), "Além disso, velho.\nmeio\nNovo.\n")

    def test_cli_all_flag_whole_file(self):
        a = self.make_repo()
        r = self.run_cli("--all", a)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.get(a), "Velho.\nmeio\nNovo.\n")

    def test_cli_help_and_usage_error_in_portuguese(self):
        r = self.run_cli("--help")
        self.assertEqual(r.returncode, 0)
        self.assertIn("Uso: turnitout_ptbr.py", r.stdout.decode("utf-8"))
        r = self.run_cli("--check")
        self.assertEqual(r.returncode, 2)
        self.assertIn("falta ARQUIVO", r.stderr.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
