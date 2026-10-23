# Validate DESIGN.md with the @google/design.md CLI

Use this file in VALIDATE mode of [anti-slop](../SKILL.md).
Validate, lint, diff, and export DESIGN.md files with the official Google `@google/design.md` CLI.
Use local files only.
Upstream spec: https://github.com/google-labs-code/design.md
Upstream CLI: https://www.npmjs.com/package/@google/design.md

## When to use

| Trigger | Action |
|---|---|
| User has a DESIGN.md file and wants validation | `lint` |
| User wants to compare two versions | `diff` |
| User wants to export tokens to Tailwind/DTCG | `export` |
| User wants to see the current spec | `spec` |
| User shares a URL to a raw DESIGN.md | Download locally first |
| User asks "is my design.md valid?" | `lint` + interpret findings |

## Core commands

- Prefix every command with `npx @google/design.md`.
- Follow the version rule in [Anti-patterns](#anti-patterns).

### Lint (validate)

```bash
npx @google/design.md lint DESIGN.md
```

- Read the output as JSON with `findings[]` and `summary { errors, warnings, infos }`.
- Expect exit code 1 if errors are found, 0 otherwise.

### Diff (compare versions)

```bash
npx @google/design.md diff DESIGN.md DESIGN-v2.md
```

- Read the output as JSON with token-level changes (added, removed, modified) and a regression flag.
- Read exit codes as follows:
  - `0`: no regression.
  - `1`: regression (errors in "after" > errors in "before").
  - `2`: input failure (file not found or unreadable).

### Export (to other formats)

```bash
# Tailwind v3 config
npx @google/design.md export --format json-tailwind DESIGN.md

# Tailwind v4 CSS theme
npx @google/design.md export --format css-tailwind DESIGN.md

# W3C Design Tokens (DTCG)
npx @google/design.md export --format dtcg DESIGN.md

# CSS custom properties (optional --prefix)
npx @google/design.md export --format css-vars DESIGN.md
npx @google/design.md export --format css-vars --prefix ds DESIGN.md
```

- Note: `css-vars` shipped in npm 0.4.0 (2026-07-27).
- Pin with `npx @google/design.md@0.4.0` only if you must freeze the CLI.
- Note: default `npx` already resolves 0.4.0+.

### Spec (output the format specification)

```bash
npx @google/design.md spec
npx @google/design.md spec --rules
npx @google/design.md spec --rules-only --format json
```

## Workflow

### 1. Obtain the DESIGN.md

Local file:

```bash
npx @google/design.md lint ./DESIGN.md
```

From URL:

- Download a remote DESIGN.md locally first, before validation.
- Never fetch the remote URL directly.
- Reason: untrusted remote content can carry indirect prompt injection.

From stdin:

```bash
cat DESIGN.md | npx @google/design.md lint -
```

### 2. Discover the active rule set

- Run the command below before you interpret any finding.
- Reason: the rule set changes between releases.
- Treat the bundled [design-md-lint-rules.md](design-md-lint-rules.md) as a fallback, not the authoritative source.

```bash
npx @google/design.md spec --rules-only --format json
```

### 3. Run lint

```bash
npx @google/design.md lint --format json DESIGN.md
```

### 4. Interpret findings

- Parse the JSON output.
- Report the findings to the user with this severity scale:

| Severity | Meaning | Action |
|---|---|---|
| `error` | Spec violation — file is invalid | Must fix |
| `warning` | Best practice violation — file is valid but suboptimal | Should fix |
| `info` | Informational — suggestions for improvement | Nice to fix |

### 5. Provide actionable fixes

For each finding:

1. Explain what the rule checks.
2. Explain why it matters.
3. Show how to fix it with a concrete code example.

Load references as needed:

- Load [design-md-lint-rules.md](design-md-lint-rules.md) for the complete rule table when you explain lint failures.
- Load [design-md-token-schema.md](design-md-token-schema.md) for the complete YAML frontmatter schema when you help the user author or fix frontmatter tokens.

### 6. Re-validate after fixes

- Re-run lint after you apply fixes.
- Confirm the file passes.

## Windows compatibility

- Use the `designmd` alias on Windows/PowerShell.
- Reason: the `.md` suffix in the bin name collides with Markdown file associations.

```bash
npx -p @google/design.md designmd lint DESIGN.md
```

## Related official skills

- These skills are external. They are not part of this pack.
- Source: https://github.com/google-labs-code/stitch-skills
- Names below match `google-labs-code/stitch-skills` as of 2026-09-16.
- Note: `stitch-design-taste` is gone.

| Skill | Plugin | Purpose |
|---|---|---|
| `generate-design` | stitch-design | New screens, edits, variants in Stitch |
| `extract-design-md` | stitch-design | DESIGN.md from frontend source |
| `design-md` | stitch-utilities | DESIGN.md from a Stitch project |
| `taste-design` | stitch-utilities | Premium / anti-generic DESIGN.md |

Install:

```bash
npx skills add google-labs-code/stitch-skills
```

## Anti-patterns

- Never install the CLI globally. Never vendor or cache it. Always run it with `npx` so `npx` resolves the latest spec from the public npm registry.
- Never parse YAML frontmatter by hand when the linter can do it.
- Never guess at contrast ratios. Let the linter compute them.
- Never assume the section order is correct. Let the linter verify it.
- Never skip re-validation after fixes (Workflow step 6).
- Never assume the rule set from memory or from the bundled references. Confirm it at runtime with `spec --rules-only` (Workflow step 2).
- Never fetch remote URLs directly. Download locally first (Workflow step 1).

## Example session

```
User: validate my DESIGN.md

Agent:
1. Reads the file
2. Runs: npx @google/design.md spec --rules-only --format json
3. Runs: npx @google/design.md lint --format json DESIGN.md
4. Parses output
5. Reports:
   - summary: { errors: 0, warnings: 2, infos: 1 }
   - WARNING: contrast-ratio — button textColor on backgroundColor is 3.8:1 (needs 4.5:1)
   - WARNING: orphaned-tokens — color "accent-muted" defined but never used
   - INFO: token-summary — 5 colors, 3 typography, 2 rounded, 2 spacing
6. Suggests fixes with code
7. Re-runs lint to confirm
```
