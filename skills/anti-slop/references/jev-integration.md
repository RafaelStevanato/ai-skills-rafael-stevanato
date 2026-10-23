# TypeSafe Jev Integration

Use this file when the anti-slop skill (EVALUATE mode) detects and uses Jev for calibrated evaluation of Axes 7-8 and Quality Checklist verification.

This file is the single copy of the Jev material.
Return to [SKILL.md](../SKILL.md) for the mode router.

## Contents

- [Scope](#scope)
- [Discovery protocol](#discovery-protocol)
- [Instructions by harness](#instructions-by-harness)
- [Jev question format](#jev-question-format)
- [Request/response structure](#requestresponse-structure)
- [Workflow integration](#workflow-integration)
- [Integration files](#integration-files)
- [When to skip Jev](#when-to-skip-jev)
- [References](#references)

## Scope

- Treat Jev as optional.
- Use [TypeSafe Jev](https://docs.typesafe.ai) only when the harness has access to it.
- Use Jev for the subjective scoring of Axes 7-8 and for Quality Checklist verification.
- Use Jev selectively. Use it only where subjective judgment needs calibration.
- Expect typed score/noul decisions from Jev. Jev does not generate text.

| Component | Jev Used? | Reason |
|-----------|-----------|--------|
| **Axes 1-6** | No | Tell detection is factual (cite-or-cut). `score.py` handles arithmetic. |
| **Axis 7 (Signature)** | Yes | S1-S7 are subjective 0/50/100 rubric scores |
| **Axis 8 (Cohesion)** | Yes | H1-H4 are subjective 0/50/100 rubric scores |
| **Quality Checklist** | Yes | 27 binary verification checks |
| **Gates & Caps** | No | Deterministic rules applied by `score.py` |

Where Jev is used:

- Axis 7 (Signature): 7 Score questions (S1-S7) with the 0/50/100 rubric.
- Axis 8 (Cohesion): 4 Score questions (H1-H4) with the 0/50/100 rubric.
- Quality Checklist: 27 Noul questions for binary verification.

Where Jev is not used:

- Axes 1-6: Tell detection is factual (cite-or-cut). [`score.py`](../scripts/score.py) handles the arithmetic.
- Gates and Caps: [`score.py`](../scripts/score.py) applies these deterministic rules.

Rules for the split:

- Cite evidence for each Axes 1-6 tell: hex value, font name, or screenshot region.
- Score each Axis 7-8 element as strong (100), attempted (50), or absent (0).
- Run the Quality Checklist as binary yes/no checks through Jev Noul questions.

## Discovery protocol

- Never assume Jev is available.
- Run the discovery protocol to detect what the harness offers.
- Follow this priority order:

```
1. MCP Tool `jev_eval` already configured in harness
   ↓ (not found)
2. Model `typesafe/jev-latest` via OpenRouter
   ↓ (not available)
3. Model `jev-latest` in auxiliary slot (Hermes, Devin, Codex)
   ↓ (not configured)
4. Fallback: inline evaluation via harness's current LLM
```

- Match any MCP tool whose name contains "jev" or "typesafe".
- Treat `jev_eval` and `jev_evaluate` as examples of that match. The tool name varies by harness.

### Step 1: Check MCP tools

```
Ask the harness: "What MCP tools are available?"

If a tool exists with name containing "jev" or "typesafe":
  → Use that tool for Axis 7-8 scoring
  → Skip to execution
```

### Step 2: Check OpenRouter

```
If the harness uses OpenRouter as provider:
  → Check if `typesafe/jev-latest` is in the catalog
  → If yes, request that model for Axis 7-8 scoring
```

### Step 3: Check auxiliary slots

```
In Hermes Agent:
  → Check if `approval` slot is configured with Jev
  → If yes, use that slot for scoring

In Devin:
  → Check if subagent profile exists with model: jev-latest
  → If yes, delegate scoring to that subagent

In OpenAI Codex:
  → Check if auxiliary model slot is configured with Jev
  → If yes, route scoring calls to that slot

In Cursor:
  → Check if alternative model is available via OpenRouter
  → If yes, request typesafe/jev-latest for scoring
```

### Step 4: LLM fallback

```
If no Jev option available:
  → Execute scoring inline using current LLM
  → Use the same 0/50/100 rubric, but via prompt engineering
```

## Instructions by harness

Use the block for the active harness.

### Claude Code / Kiro CLI

```markdown
## Jev Discovery

1. Check MCP: run `claude mcp list` or consult .mcp.json
2. If `jev-eval` MCP server configured → use tool `jev_evaluate`
3. If not → inline scoring via Claude using premium-markers.md rubric
```

### Cursor

```markdown
## Jev Discovery

1. Check if OpenRouter is configured as provider
2. If yes, request model `typesafe/jev-latest` for Axis 7-8 scoring
3. If not → inline scoring via current model
```

### GitHub Copilot

```markdown
## Jev Discovery

1. Check available tools and extensions
2. If MCP server with Jev available → use that tool
3. If not → inline scoring via Copilot model
```

### Devin

```markdown
## Jev Discovery

1. Check custom subagent profiles in agents/
2. If profile exists with `model: typesafe/jev-latest`:
   → Delegate scoring: "score Axes 7-8 using subagent jev-eval"
3. If not → inline scoring
```

### Hermes Agent

```markdown
## Jev Discovery

1. Check config.yaml → auxiliary.approval
2. If configured with `model: typesafe/jev-latest`:
   → Scoring will use approval slot automatically
3. If not → inline scoring via main model
```

### OpenAI Codex / ChatGPT

```markdown
## Jev Discovery

1. Check if auxiliary model slots are configured
2. Check if OpenRouter integration is available
3. If not → inline scoring via GPT
```

### Cline / Aider / Continue / Windsurf

```markdown
## Jev Discovery

1. Check MCP servers configured
2. Check if provider supports Jev model
3. Fallback → inline scoring
```

## Jev question format

- Use [`../scripts/jev_questions.json`](../scripts/jev_questions.json) when Jev is available.
- Expect 38 typed questions in that file: 11 Score questions and 27 Noul questions.
- Take the level text of S1-S7 and H1-H4 from [premium-markers.md](premium-markers.md) and from that file.
- Do not restate the rubric levels in a second place.

### Axis 7 Signature (7 Score questions)

- Ask one Score question per element S1-S7.
- Score each element 0, 50, or 100.

### Axis 8 Cohesion (4 Score questions)

- Ask one Score question per check H1-H4.
- Score each check 0, 50, or 100.

### Quality Checklist (27 Noul questions)

Run binary verification across 6 categories:

- **Pre-sweep** (4): Evidence inventory, brief, context, references
- **During-sweep** (6): Cite-or-cut, premium pairs, portability test, defense test, attribution, severity
- **Exclusions** (3): Documentation, genuineness, count
- **Post-sweep** (8): Unverifiable marked, absolute rules, scores, ledger, gates, script
- **Report** (3): Template, fixes ranking, language
- **Final audit** (3): Obvious slop, over-correction, trust test

## Request/response structure

### Request (Axis 7-8 scoring)

- Put the design evidence in `state.design_evidence`.
- Set `model` to `jev-latest`.
- Add one `questions` entry per Score question.
- Give each entry `type`, `instructions`, and `levels`.
- Treat the `...` entries in the sample as placeholders. Take the full text from [`../scripts/jev_questions.json`](../scripts/jev_questions.json).

```json
{
  "state": {
    "design_evidence": {
      "hero_screenshot": "path/to/hero.png",
      "full_page": "path/to/full.png",
      "fonts": ["Inter", "Space Grotesk"],
      "colors": ["#6366f1", "#8b5cf6", "#ffffff"],
      "context": "SaaS landing page"
    }
  },
  "model": "jev-latest",
  "questions": {
    "signature_s1_artifact": {
      "type": "score",
      "instructions": "Evaluate the signature artifact. Is there ONE high-effort focal object that could only belong to this brand?",
      "levels": [
        "0 — Absent: No custom focal object",
        "50 — Attempted: Custom visual exists but generic",
        "100 — Strong: ONE high-effort focal object unique to this brand"
      ]
    },
    "cohesion_h1_palette": {
      "type": "score",
      "instructions": "Evaluate palette discipline...",
      "levels": ["0 — ...", "50 — ...", "100 — ..."]
    }
  }
}
```

### Response

```json
{
  "answers": {
    "signature_s1_artifact": {
      "type": "score",
      "score": 1.2,
      "probabilities": {"0": 0.15, "1": 0.55, "2": 0.30},
      "confidence": 0.55
    },
    "cohesion_h1_palette": {
      "type": "score",
      "score": 2.1,
      "probabilities": {"0": 0.05, "1": 0.10, "2": 0.85},
      "confidence": 0.85
    }
  },
  "usage": {"input_tokens": 823, "output_tokens": 0}
}
```

### Score interpretation

Map the Jev score 0-2 to the 0/50/100 rubric:

- **0** → 0 points (absent)
- **1** → 50 points (attempted)
- **2** → 100 points (strong)

Handle fractional scores like this:

- Read a fractional score (e.g., 1.2) as a probability-weighted estimate.
- Round it to the nearest integer for the final axis calculation.
- Example: 1.2 rounds to 1, which is 50 points.

Apply the Quality Checklist threshold:

- Require P(yes) > 0.5 on every Noul question.

## Workflow integration

- Apply the modified steps below only when Jev is available.
- Keep every other EVALUATE step unchanged. See [evaluate-procedure.md](evaluate-procedure.md).

### Modified workflow step 5

When Jev is available, change Step 5 from:

```markdown
5. **Score Axes 7–8** — read `references/premium-markers.md`, score the 7
   signature elements and 4 cohesion checks with one-line justifications each.
```

To:

```markdown
5. **Score Axes 7–8** — 
   a. Prepare design evidence (screenshots, fonts, colors, context)
   b. If Jev available: submit 11 Score questions, receive calibrated 0/50/100
   c. If Jev unavailable: score manually using premium-markers.md rubric
   d. Write one-line justification for each score (required regardless of Jev)
```

- Write a one-line justification for each Axis 7-8 score, with or without Jev.

### Modified workflow step 7 (Quality Checklist)

When Jev is available:

```markdown
7. **Quality Checklist** —
   a. If Jev available: submit 27 Noul questions, all must be P(yes) > 0.5
   b. If Jev unavailable: run through checklist manually
   c. Any failure = report not ready, fix and re-check
```

- Treat any failed check as "report not ready". Fix the report and re-check.
- Run the full checklist, as defined in [evaluate-exclusions-qa.md](evaluate-exclusions-qa.md), before delivery.

## Integration files

| File | Description |
|------|-------------|
| [`../scripts/jev_questions.json`](../scripts/jev_questions.json) | 38 typed questions (11 Score + 27 Noul) |
| [`../scripts/score.py`](../scripts/score.py) | Tell arithmetic for Axes 1-6 (unchanged) |
| `references/jev-integration.md` | This document |
| [`premium-markers.md`](premium-markers.md) | Rubric for S1-S7, H1-H4 (used with or without Jev) |

### What Jev does not replace

- Keep `score.py`. It still handles all tell-based axis scoring and gates.
- Keep tell detection. It stays factual cite-or-cut.
- Keep the Slop Report template. Its structure is unchanged. See [slop-report-template.md](slop-report-template.md).
- Keep premium pair checks. They stay manual verification.
- Keep Jev as a supplement. See [evaluate-scoring.md](evaluate-scoring.md) for the full arithmetic.

## When to skip Jev

Skip Jev, even when it is available, in these cases:

1. **Quick/informal review**: The overhead is not worth it for a rough assessment.
2. **Code-only channel**: Without visual evidence, Axes 7-8 scoring is limited.
3. **Single-element check**: Verifying one aspect does not need the full integration.

In these cases, use the [premium-markers.md](premium-markers.md) rubric directly with inline LLM scoring.

## References

- [TypeSafe AI Docs](https://docs.typesafe.ai)
- [Jev API Reference](https://docs.typesafe.ai/api)
- [OpenRouter - Jev](https://openrouter.ai/typesafe/jev-latest)
- [`../scripts/jev_questions.json`](../scripts/jev_questions.json): Typed questions
- [`../scripts/score.py`](../scripts/score.py): Tell-based scoring script
- [`premium-markers.md`](premium-markers.md): S1-S7 and H1-H4 rubric
