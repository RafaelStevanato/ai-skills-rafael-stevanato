# TypeSafe Jev Integration

Contents: Scope · Discovery in Codex · Jev question format · Request/response structure · Workflow integration · Integration files · When to skip Jev

Use this file in EVALUATE mode of [anti-slop](../SKILL.md) when the harness has access to [TypeSafe Jev](https://docs.typesafe.ai).
Jev is optional. It returns typed score/noul decisions and does not generate text.

## Scope

|Component|Jev Used?|Reason|
|-----------|-----------|--------|
|**Axes 1-6**|❌ No|Tell detection is factual (cite-or-cut). `score.py` handles arithmetic.|
|**Axis 7 (Signature)**|✅ Yes|S1-S7 are subjective 0/50/100 rubric scores|
|**Axis 8 (Cohesion)**|✅ Yes|H1-H4 are subjective 0/50/100 rubric scores|
|**Quality Checklist**|✅ Yes|27 binary verification checks|
|**Gates & Caps**|❌ No|Deterministic rules applied by `score.py`|

## Discovery in Codex

Jev is optional; do not assume it is available, install it, or pick a paid provider for the user. Check in this order:

1. MCP: look for a tool whose name contains `jev` or `typesafe` (for example `jev_eval`, `jev_evaluate`) in the session's tools, or run `codex mcp list`. If one exists, use it for Axis 7-8 scoring and the Quality Checklist.
2. Model provider: if the user's Codex config routes to OpenRouter and `typesafe/jev-latest` is in its catalog, use that model for the scoring calls.
3. Fallback: score inline with the current model, using the same 0/50/100 rubric from premium-markers.md.

## Jev question format

Use [`../scripts/jev_questions.json`](../scripts/jev_questions.json) when Jev is available.

- Axes 7-8: 11 Score questions (S1-S7 Signature, H1-H4 Cohesion).
- Quality Checklist: 27 Noul questions in 6 categories:
  - **Pre-sweep** (4): Evidence inventory, brief, context, references
  - **During-sweep** (6): Cite-or-cut, premium pairs, portability test, defense test, attribution, severity
  - **Exclusions** (3): Documentation, genuineness, count
  - **Post-sweep** (8): Unverifiable marked, absolute rules, scores, ledger, gates, script
  - **Report** (3): Template, fixes ranking, language
  - **Final audit** (3): Obvious slop, over-correction, trust test

## Request/response structure

### Request (Axis 7-8 scoring)

- Put the design evidence in `state.design_evidence`. Set `model` to `jev-latest`.
- Add one `questions` entry per Score question: `type`, `instructions`, `levels`.
- Replace each `...` with the text from `jev_questions.json`.

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

Map the Jev score 0-2 to the 0/50/100 rubric: **0** → 0 points (absent); **1** → 50 points (attempted); **2** → 100 points (strong).

Read a fractional score (e.g., 1.2) as a probability-weighted estimate. Round it to the nearest integer for the axis calculation.
Require P(yes) > 0.5 on every Noul question.

## Workflow integration

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

### Modified workflow step 7 (Quality Checklist)

```markdown
7. **Quality Checklist** —
   a. If Jev available: submit 27 Noul questions, all must be P(yes) > 0.5
   b. If Jev unavailable: run through checklist manually
   c. Any failure = report not ready, fix and re-check
```

## Integration files

|File|Description|
|------|-------------|
|[`../scripts/jev_questions.json`](../scripts/jev_questions.json)|38 typed questions (11 Score + 27 Noul)|
|[`../scripts/score.py`](../scripts/score.py)|Tell arithmetic for Axes 1-6 (unchanged)|
|`references/jev-integration.md`|This document|
|[`premium-markers.md`](premium-markers.md)|Rubric for S1-S7, H1-H4 (used with or without Jev)|

Jev does not replace `score.py` (tell-based scoring and gates), cite-or-cut tell detection, the Slop Report template ([slop-report-template.md](slop-report-template.md)), or manual premium pair checks.

## When to skip Jev

Skip Jev, even when available, for:

1. **Quick/informal review**: overhead outweighs value.
2. **Code-only channel**: without visual evidence, Axes 7-8 scoring is limited.
3. **Single-element check**: one aspect does not need the full integration.

Then use the [premium-markers.md](premium-markers.md) rubric directly with inline LLM scoring.

References: [TypeSafe AI Docs](https://docs.typesafe.ai), [Jev API Reference](https://docs.typesafe.ai/api), [OpenRouter - Jev](https://openrouter.ai/typesafe/jev-latest).
