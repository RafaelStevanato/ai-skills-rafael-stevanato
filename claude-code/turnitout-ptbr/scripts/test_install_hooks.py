"""Testes do instalador de hooks. Rode: python test_install_hooks.py"""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
INSTALLER = HERE / "install_hooks.py"
ENGINE = HERE / "turnitout_ptbr.py"
COMMAND = f'"{Path(sys.executable).as_posix()}" "{ENGINE.as_posix()}"'
OLD = '"/velho/python" "/velho/hooks/turnitout_ptbr.py"'
OTHER = {"type": "command", "command": "echo outro"}


class InstallHooksTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)
        self.settings = self.dir / "settings.json"

    def tearDown(self):
        self._tmp.cleanup()

    def run_installer(self, *args, installer=INSTALLER):
        return subprocess.run([sys.executable, str(installer), "--settings", str(self.settings), *args],
                              capture_output=True)

    def save(self, data, eol="\n", tail="", indent=2):
        text = json.dumps(data, indent=indent).replace("\n", eol) + tail
        self.settings.write_bytes(text.encode("utf-8"))

    def load(self):
        return json.loads(self.settings.read_bytes().decode("utf-8"))

    def ours(self, data):
        return [(event, g, h) for event, groups in data.get("hooks", {}).items()
                for g in groups for h in g["hooks"] if "turnitout_ptbr.py" in h["command"]]

    def backups(self):
        return sorted(self.dir.glob("settings.json.bak-turnitout-*"))

    def test_install_adds_one_entry_per_event_and_keeps_the_rest(self):
        self.save({"model": "x", "hooks": {"Stop": [{"hooks": [OTHER]}]}})
        r = self.run_installer()
        self.assertEqual(r.returncode, 0, r.stderr)
        data = self.load()
        self.assertEqual(data["model"], "x")
        self.assertIn(OTHER, data["hooks"]["Stop"][0]["hooks"])
        found = self.ours(data)
        self.assertEqual(sorted(e for e, _, _ in found), ["PostToolUse", "Stop", "UserPromptSubmit"])
        for event, group, hook in found:
            self.assertEqual(hook, {"type": "command", "command": COMMAND, "timeout": 10})
            self.assertEqual(group.get("matcher"), {"PostToolUse": "Write|Edit|MultiEdit", "Stop": ""}.get(event))
        self.assertNotIn("matcher", data["hooks"]["UserPromptSubmit"][0])
        self.assertEqual(len(self.backups()), 1)

    def test_install_replaces_old_command_and_is_idempotent(self):
        old = {"type": "command", "command": OLD, "timeout": 10}
        self.save({"hooks": {"PostToolUse": [{"matcher": "Write", "hooks": [old, OTHER]}], "Stop": [{"hooks": [old]}]}})
        self.assertEqual(self.run_installer().returncode, 0)
        data = self.load()
        self.assertEqual(len(self.ours(data)), 3)
        self.assertNotIn("velho", self.settings.read_text(encoding="utf-8"))
        self.assertIn(OTHER, data["hooks"]["PostToolUse"][0]["hooks"])
        first, backups = self.settings.read_bytes(), self.backups()
        r = self.run_installer()
        self.assertEqual(r.returncode, 0)
        self.assertIn("nada a fazer", r.stdout.decode("utf-8"))
        self.assertEqual((self.settings.read_bytes(), self.backups()), (first, backups))

    def test_uninstall_removes_only_ours(self):
        self.save({"model": "x", "hooks": {"Stop": [{"hooks": [OTHER]}]}})
        self.run_installer()
        self.assertEqual(self.run_installer("--uninstall").returncode, 0)
        self.assertEqual(self.load(), {"model": "x", "hooks": {"Stop": [{"hooks": [OTHER]}]}})
        self.save({"model": "y"})
        self.run_installer()
        self.run_installer("--uninstall")
        self.assertEqual(self.load(), {"model": "y"})

    def test_creates_missing_settings_without_backup(self):
        r = self.run_installer()
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(len(self.ours(self.load())), 3)
        self.assertEqual(self.backups(), [])
        self.assertTrue(self.settings.read_bytes().endswith(b"\n"))

    def test_preserves_crlf_indent_and_missing_final_newline(self):
        self.save({"a": 1}, eol="\r\n", indent=4)
        self.assertEqual(self.run_installer().returncode, 0)
        raw = self.settings.read_bytes()
        self.assertEqual(raw.count(b"\n"), raw.count(b"\r\n"))
        self.assertIn(b'\r\n    "hooks": {\r\n        "PostToolUse"', raw)
        self.assertFalse(raw.endswith(b"\n"))

    def test_invalid_json_and_missing_engine_leave_settings_untouched(self):
        self.settings.write_bytes(b"{ isto nao e json")
        r = self.run_installer()
        self.assertEqual(r.returncode, 1)
        self.assertIn("erro", r.stderr.decode("utf-8"))
        self.assertEqual(self.settings.read_bytes(), b"{ isto nao e json")
        alone = self.dir / "alone"
        alone.mkdir()
        shutil.copy(INSTALLER, alone / "install_hooks.py")
        self.save({"a": 1})
        before = self.settings.read_bytes()
        r = self.run_installer(installer=alone / "install_hooks.py")
        self.assertEqual(r.returncode, 1)
        self.assertIn("motor não encontrado", r.stderr.decode("utf-8"))
        self.assertEqual(self.settings.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
