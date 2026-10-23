# Usage-boundary hook (optional, user setup)

Read this only when the user asks to enforce the gambling boundary automatically. A hook applies to every conversation in its scope, not only to RCD work, so the user decides whether to install it.

Antigravity hooks cannot block a prompt, but a `PreToolUse` hook can deny file writes. Add this named hook to `~/.gemini/config/hooks.json` (global) or `<workspace>/.agents/hooks.json` (workspace), replacing `<skill-dir>` with this skill's folder, for example `~/.gemini/config/skills/revenue-centric-design`. On Windows, use `python` instead of `python3`.

```json
{
  "rcd-usage-boundary": {
    "PreToolUse": [
      {
        "matcher": "write_to_file|replace_file_content|multi_replace_file_content",
        "hooks": [
          {
            "type": "command",
            "command": "python3 <skill-dir>/scripts/agy_boundary_hook.py",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

`scripts/agy_boundary_hook.py` passes the payload (target file, new content, workspace paths) to `check_usage_boundary.py` and prints `{"decision": "deny", "reason": ...}` on a gambling hit. Otherwise it prints `{"decision": "allow"}`, which hands the write to the normal permission policy instead of auto-approving it. The check runs from the first workspace path, so a user-created `.rcd-boundary-ok` there waives it.

Turn the hook on or off under Settings > Customizations > Hooks (app and IDE) or inspect it with `/hooks` (CLI). Community reports say some IDE builds did not fire plugin hooks; after installing, test it once by asking for an edit in a scratch file that mentions "casino".
