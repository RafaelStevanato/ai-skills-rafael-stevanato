# Usage-boundary hooks (optional, user setup)

Read this only when the user asks to enforce the gambling boundary automatically. Hooks apply to every Codex session that loads them, not only to RCD work, so the user decides whether to install them.

Add the entries below to `~/.codex/hooks.json` (user scope) or `<repo>/.codex/hooks.json` (project scope). Replace `<skill-dir>` with the folder that holds this skill, for example `~/.agents/skills/revenue-centric-design`. On Windows, add a `commandWindows` field that calls `python` instead of `python3`.

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 <skill-dir>/scripts/check_usage_boundary.py",
            "timeout": 30,
            "statusMessage": "Checking RCD usage boundary"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "apply_patch",
        "hooks": [
          {
            "type": "command",
            "command": "python3 <skill-dir>/scripts/check_usage_boundary.py",
            "timeout": 30,
            "statusMessage": "Checking RCD usage boundary"
          }
        ]
      }
    ]
  }
}
```

The script reads the hook JSON from stdin, scans every text field (the prompt, or the patch in `tool_input.command`), and exits `2` with the reason on stderr when it finds gambling context. Codex blocks the prompt or the edit on exit `2`. The `apply_patch` matcher also covers the `Edit` and `Write` aliases.

Codex runs a new or changed hook only after the user reviews and trusts it with `/hooks`. A `.rcd-boundary-ok` file in the session's working directory waives the check; only the user creates it.
