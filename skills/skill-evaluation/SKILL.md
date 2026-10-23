---
name: skill-evaluation
description: >-
  Evaluate, audit, or grade a Claude agent skill against Anthropic and Matt Pocock skill-writing guidance. Scores 18 criteria on 4 axes, runs a 10-prompt trigger eval, diagnoses failure modes, and writes an EVALUATION.md scorecard. Use when the user asks "evaluate this skill" or "skill scorecard", or to review SKILL.md, check a trigger rate, compare two skills, or gate skills in CI (--fail-below).
license: Apache-2.0
metadata:
  author: "ft.ia.br"
  version: "2.1.0"
  date: "2026-07-03"
  repository: "https://github.com/fabricioctelles/skills"
  category: "code-quality-and-review"
  source: "Anthropic, How we use skills (Jun 2026); Matt Pocock, The Missing Manual (2026)"
  attribution: "Anthropic best practices plus Matt Pocock writing-great-skills"
  consolidated: "2026-10-23 ASD-STE100 rewrite"
  merged-from: "skill-evaluation"
---

> **⚠️ EXECUTION DIRECTIVE (INPUT vs. OUTPUT SEPARATION):**
> The rules in this skill use strict ASD-STE100 controlled language solely for zero-ambiguity parsing and token efficiency.
> - **NEVER copy this telegraphic or robotic style into human-facing outputs.**
> - Apply 80% ASD-STE100 in final outputs ONLY when explaining dense technical concepts.

# Skill Evaluation

## Router

- Step 2: load [references/mechanics.md](references/mechanics.md) before Axes 1, 3, and 4.
- Step 3: load [references/categories.md](references/categories.md).
- Step 8: run [scripts/score.py](scripts/score.py).
- Step 9: load [references/output-template.md](references/output-template.md).

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `target` | Path to skill directory or SKILL.md to evaluate | Ask user |
| `output` | Path to write the scorecard | `<target>/EVALUATION.md` |
| `compare` | Optional second skill to compare side-by-side | None |

- Run unattended in CI: point `target` at skills changed in a PR. Gate with `scripts/score.py --fail-below 60 ...`.
- A non-zero exit below the threshold fails the check.
- Invoke the script as `python3 scripts/score.py`. Never as `./scripts/score.py`.

## Criteria

- Score 18 criteria from 0 to 100: 14 core criteria on every skill, 4 conditional criteria.
- Allow N/A on a core criterion only by criterion #8's rule, or with a written reason under cite-or-cut.

### Axis 1 — Trigger (invocation)

| # | Criterion | Weight | Key question |
|---|-----------|--------|---------------|
| 1 | Invocation design | 2x | Is model-invoked vs. user-invoked deliberate and fitting? Model-invoked pays **context load** (the description loads every turn); user-invoked pays **cognitive load** (the human is the index). A skill that only ever fires by hand should be user-invoked. |
| 2 | Description quality | 2x | Model-invoked: leading word up front, one trigger per branch (synonyms renaming the same branch are duplication), no identity that's redundant with the body. User-invoked (`disable-model-invocation: true`): a human-facing one-liner, no trigger list. Score against the mode the skill actually uses — never penalize a user-invoked skill for lacking trigger phrases. |

### Axis 2 — Structure

| # | Criterion | Weight | Key question |
|---|-----------|--------|---------------|
| 3 | Steps vs. reference clarity | 1x | Does the skill distinguish ordered steps from on-demand reference? All-reference and all-steps skills are both valid — score clarity, not the mix. Is related material co-located (definition, rules, caveats under one heading)? |
| 4 | Branch-aware disclosure & pointers | 2x | Is material every branch needs inline, and material only some branches need behind a context pointer? Does each pointer's wording say when to follow it ("if you need X, read Y")? A weakly worded pointer to must-have material is a variance bug. |
| 5 | Conciseness (no sprawl) | 2x | Is SKILL.md lean — under 500 lines as a ceiling, smaller is better — with every line earning its context cost? |
| 6 | Coherent scope | 1x | Does the skill do one thing and compose with others, rather than covering too much? |

### Axis 3 — Steering

| # | Criterion | Weight | Key question |
|---|-----------|--------|---------------|
| 7 | Leading words | 2x | Does the skill use compact, high-prior terms ("vertical slice", "tight", "red") to anchor behavior, repeated consistently? Could any verbose passage collapse into one? |
| 8 | Completion criteria & legwork | 2x | Skills with steps: does each step end on a checkable, exhaustive completion criterion? A vague one invites premature completion. Skills that are pure reference: is there an exhaustiveness bar over the reference itself ("every rule applied")? If neither applies, mark N/A. |
| 9 | Gotchas section | 2x | Is there explicit capture of failure points, edge cases, footguns? |
| 10 | Grounded in expertise | 2x | Does content come from observed failures and real project facts, or generic "best practices"? |
| 11 | Avoids railroading | 1x | Does the skill leave room to adapt — procedures over declarations, defaults over menus — without over-prescribing? |

### Axis 4 — Pruning

| # | Criterion | Weight | Key question |
|---|-----------|--------|---------------|
| 12 | No-ops (deletion test) | 2x | Running the deletion test sentence by sentence: if removing a sentence leaves behavior unchanged, it's a no-op — including restatements of what the model already does by default. Cite line numbers for candidates. |
| 13 | Single source of truth | 1x | Does each meaning live in exactly one place? Duplication between SKILL.md and references/ counts too. |
| 14 | Relevance & sediment | 1x | Are there stale lines, accumulated layers, or material that no longer influences what the skill does? |

### Conditional criteria

Score a criterion only when the skill's category (from [references/categories.md](references/categories.md)) applies. Otherwise mark **N/A** and drop it from the weighted average.

| # | Criterion | Weight | Applies to category |
|---|-----------|--------|----------------------|
| 15 | Setup flow | 1x | library-and-api-reference, data-fetching-and-analysis, ci-cd-and-deployment, infrastructure-operations |
| 16 | Memory mechanism | 1x | business-process-automation, data-fetching-and-analysis, runbooks |
| 17 | Scripts & libraries | 1x | product-verification, code-scaffolding-and-templates, code-quality-and-review, data-fetching-and-analysis, infrastructure-operations |
| 18 | On-demand hooks | 1x | code-quality-and-review, ci-cd-and-deployment |

- Override this table with judgment, in either direction. Explain every override in the scorecard.
- Score a criterion outside the listed categories when the skill clearly benefits (e.g., a non-`product-verification` skill that obviously needs a helper script).
- Mark a criterion N/A inside an applicable category when the pattern does not fit (e.g., a pure-reference vocabulary skill under `code-quality-and-review` has nothing for a hook to enforce).

### Overall score

```
overall = sum(score × weight) / sum(weight)
```

- Exclude N/A criteria from both sums. Never score N/A as 0. Never count its weight.

## Scoring Guide

| Score | Meaning |
|-------|---------|
| 0 | Not present at all |
| 1–25 | Minimal/token effort, barely addresses the criterion |
| 26–50 | Partially addressed but with significant gaps |
| 51–75 | Solid implementation with room for improvement |
| 76–90 | Strong implementation, minor gaps only |
| 91–100 | Exemplary — would use as a reference for others |

## Grade Scale

| Grade | Range | Meaning |
|-------|-------|---------|
| A | 80–100 | Production-quality, reference skill |
| B | 60–79 | Good skill, minor improvements needed |
| C | 40–59 | Functional but significant gaps |
| D | 20–39 | Needs substantial rework |
| F | 0–19 | Skeleton only, not production-ready |

## Workflow

1. **Read the target skill**: SKILL.md, its frontmatter (check `disable-model-invocation`), and every file in the skill directory.
2. **Read `references/mechanics.md`** (mandatory). Use its vocabulary and tests, including effective context-pointer wording.
3. **Classify** with `references/categories.md`. Assign one category. It sets which conditional criteria apply.
4. **Score all applicable criteria** under **cite-or-cut**: score a criterion only after its justification cites specific evidence (file, section, or line). No citation, no score.
   - Done when every applicable criterion carries a score and a citation, and every N/A a reason.
5. **Trigger eval**: follow the **Trigger Eval** section below.
6. **Diagnose failure modes**. Done when every mode in the table below was checked against the skill and either cited (file:line) or dismissed.
7. **Assess the 5 bonus patterns** in this table:

   | Bonus | Applies when | What to look for |
   |-------|-------------|-----------------|
   | Validation loops | Skill produces output or modifies state | Instructs the agent to self-check before finalizing |
   | Output templates | Skill generates structured output | Includes a concrete template/example of expected format |
   | Procedures over declarations | Skill teaches a method | Teaches *how to approach* problems, not *what to produce* for one case |
   | Defaults over menus | Skill offers tool/approach choices | Picks a clear default, mentions alternatives briefly |
   | Trace-checkable steering | Skill uses leading words | The leading words are distinctive enough that a user could grep the agent's reasoning traces to confirm the skill actually fired |

   Report each as Present / Absent / N/A.
8. **Compute the weighted score**: run `python3 scripts/score.py` with one `criterion:score:weight` triple per criterion. Score `NA` to exclude a criterion.
   - The script prints both sums, the overall, and the grade. Never do this arithmetic by hand.
   - Pass weight and score as bare numbers (`2`, not `2x`; `80`, not `80%`). The script crashes on non-numeric values.
9. **Write the scorecard** to the output path. Read `references/output-template.md` first, including its comparison-mode template when `compare` is set. Emit exactly that structure.

## Trigger Eval

Test whether the description makes a model invoke the skill when it should, and ignore it when it should not. Use the result as evidence, never as a gate.

### When to run

- Run the eval for model-invoked skills only.
- Skip user-invoked skills (`disable-model-invocation: true`), which have no description to test. Mark the section N/A.

### Prompt generation

Generate **10 prompts** from the skill's description, scope, and gotchas:

- **5 should-trigger**: realistic requests squarely within scope. Vary the phrasing: skill vocabulary in some, naive/indirect language in others.
- **5 should-not-trigger**: adjacent requests clearly outside scope, from 3 sources: a sibling skill's territory, a task the description explicitly excludes, a generic request a model handles without any skill.
- Write each prompt as a real user would, with no meta-language about skills and no hints.

### Sub-agent execution

Run each prompt in an independent sub-agent session with the target skill available. Append this instruction to its system context:

```
At the end of your response, output exactly one line in this format:
SKILLS_USED: <comma-separated list of skill names you loaded during this task, or "none">
```

Keep the instruction generic: never name the skill under test, never hint at what should trigger. Let the sub-agent operate normally.

### Detection

Parse the `SKILLS_USED:` line from each sub-agent's response. Record per prompt:

| Field | Value |
|-------|-------|
| Prompt | The test prompt text |
| Expected | should-trigger / should-not-trigger |
| Triggered | yes / no (was the target skill name in the list?) |
| Other skills | Any other skills that fired |

### What to report

Report raw counts, with no pass/fail judgment:

- **Should-trigger hit rate** — X/5 triggered
- **Should-not-trigger leak rate** — X/5 triggered (lower is better)
- **Other skills observed** — which siblings fired on the same prompts

Feed these numbers to criteria #1 and #2. Watch for over-triggering and description weakness.

### Practical notes

- Skip the eval when the environment cannot spawn sub-agents (e.g., CI without agent access). Write "trigger eval: skipped (no agent access)" in the scorecard.
- Run one trial per prompt. Run more only if results are ambiguous.
- Keep the prompts in the scorecard as a regression set.

## Failure-mode diagnosis

Name the failure mode, cite evidence, and prescribe the defense from [references/mechanics.md](references/mechanics.md) §5. Never write a generic "top improvements" list.

| Mode | Evidence to look for |
|------|----------------------|
| Premature completion | Vague completion criteria with future steps still visible |
| Weak steering | Instruction present but the agent doesn't reliably follow it |
| Duplication | Same meaning in 2+ places, including SKILL.md vs. references/ |
| Sediment | Stale layers, outdated references, dead instructions |
| Sprawl | Long even with no duplication or sediment |
| No-ops | Lines that don't change behavior versus the model's default |
| Buried steps | Inline reference so heavy it soaks the steps |

- Write a **Prioritized Actions** section after the table: the 3–5 highest-impact actions from the detected failure modes, each citing its evidence.
- Never score **context overload** (too many model-invoked skills competing for attention in one environment): it is portfolio-level, out of scope. Record the description's context-load cost when notable.

## Gotchas

- Tiny skills (under ~50 lines) flood the scorecard with N/A. Score what is there: a small, sharp skill can reach grade A on few criteria.
- Self-evaluation bias: when you wrote the skill, apply the deletion test with extra skepticism.
- Fresh rewrites still carry duplication: sediment needs time, duplication does not. Run the pruning axis on new skills too.

## Quality Checklist

Final gate: re-check steps only. Add no new checks.

- [ ] cite-or-cut held everywhere (step 4)
- [ ] every N/A justified (step 4)
- [ ] trigger eval run or skipped with reason (step 5)
- [ ] every failure mode cited or dismissed (step 6)
- [ ] 5 bonus patterns assessed (step 7)
- [ ] score computed by `scripts/score.py`, not by hand (step 8)

## Sources

- [Lessons from building Claude Code: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills) — Anthropic, Jun 2026
- "The Missing Manual: How to Write Great Skills" — Matt Pocock, AI Engineer World's Fair 2026 ([video](https://www.youtube.com/watch?v=UNzCG3lw6O0)), and his `writing-great-skills` skill
