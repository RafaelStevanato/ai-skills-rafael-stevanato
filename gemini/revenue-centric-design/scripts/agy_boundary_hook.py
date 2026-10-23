#!/usr/bin/env python3
"""Antigravity PreToolUse adapter for check_usage_boundary.py.

Reads the hook payload on stdin, runs the boundary check from the first workspace path
(so a user-created .rcd-boundary-ok there is honored), and prints the JSON decision Antigravity
expects: "deny" with the reason on a gambling hit, otherwise "allow", which hands the call
to the normal permission policy.
"""
import json
import pathlib
import subprocess
import sys

raw = sys.stdin.read()
try:
    cwd = (json.loads(raw).get("workspacePaths") or [None])[0]
except (json.JSONDecodeError, AttributeError):
    cwd = None
check = pathlib.Path(__file__).with_name("check_usage_boundary.py")
result = subprocess.run([sys.executable, str(check)], input=raw, capture_output=True, text=True, cwd=cwd)
if result.returncode == 2:
    print(json.dumps({"decision": "deny", "reason": result.stderr.strip()}))
else:
    print(json.dumps({"decision": "allow"}))
