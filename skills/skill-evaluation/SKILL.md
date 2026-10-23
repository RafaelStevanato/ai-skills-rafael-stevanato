---
name: skill-evaluation
description: >-
  Evaluate, audit, or grade any Claude agent skill (SKILL.md plus its references and scripts) against a merged framework of Anthropic Claude Code skill best practices and Matt Pocock's writing-great-skills methodology. Scores 18 criteria across 4 axes (Trigger, Structure, Steering, Pruning) with file:line evidence, computes a weighted 0-100 overall score and A-F grade with scripts/score.py, runs a 10-prompt sub-agent trigger eval, diagnoses failure modes (premature completion, weak steering, duplication, sediment, sprawl, no-ops, buried steps), and writes an EVALUATION.md scorecard with prioritized fixes. Use when the user asks to evaluate this skill, rate or audit a skill, build a skill scorecard, review SKILL.md, check a skill description or trigger rate, compare two skills side by side, or gate changed skills in CI with a minimum score (--fail-below).
license: Apache-2.0
metadata:
  author: "ft.ia.br"
  version: "2.1.0"
  date: "2026-07-03"
  repository: "https://github.com/fabricioctelles/skills"
  category: "code-quality-and-review"
  source: "Anthropic, Lessons from building Claude Code: How we use skills (Jun 2026); Matt Pocock, The Missing Manual: How to Write Great Skills (AI Engineer World's Fair 2026) and writing-great-skills"
  attribution: "Framework merges Anthropic skill best practices with Matt Pocock writing-great-skills methodology"
  consolidated: "2026-10-23 ASD-STE100 rewrite"
  merged-from: "skill-evaluation"
---

> **⚠️ EXECUTION DIRECTIVE (INPUT vs. OUTPUT SEPARATION):**
> The rules in this skill use strict ASD-STE100 controlled language solely for zero-ambiguity parsing and token efficiency.
> - **NEVER copy this telegraphic or robotic style into human-facing outputs.**
> - Apply 80% ASD-STE100 in final outputs ONLY when explaining dense technical concepts.

# Skill Evaluation

## Router

- Load [references/mechanics.md](references/mechanics.md) at step 2, before you score Axes 1, 3, and 4. It defines leading words, completion criteria, context pointers, the deletion test, and failure-mode defenses.
- Load [references/categories.md](references/categories.md) at step 3 to classify the target skill. It holds the 9 categories and the decision tree.
- Run [scripts/score.py](scripts/score.py) at step 8 to compute the weighted score and grade.
- Load [references/output-template.md](references/output-template.md) at step 9 before you write the scorecard. It also holds the comparison-mode template.

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `target` | Path to skill directory or SKILL.md to evaluate | Ask user |
| `output` | Path to write the scorecard | `<target>/EVALUATION.md` |
| `compare` | Optional second skill to compare side-by-side | None |

- Run unattended in CI: point `target` at skills changed in a PR.
- Gate with `scripts/score.py --fail-below 60 ...`.
- Expect a non-zero exit when the overall score is below the threshold. The check fails.
- Invoke the script as `python3 scripts/score.py`. Never invoke it as `./scripts/score.py`.

## Criteria

- Score 18 criteria: 14 core criteria plus 4 conditional criteria.
- Score the 14 core criteria on every skill.
- Score a conditional criterion only when the skill's category makes it apply (see Conditional criteria).
- Mark every other criterion **N/A**. Apply the N/A rule in Overall score.
- Allow N/A on a core criterion only by criterion #8's own rule, or with a written reason under cite-or-cut.
- Score each criterion from 0 to 100.
- Cite file, section, or line as evidence for every score.

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

- Score a conditional criterion only when the skill's category applies. Take the category from [references/categories.md](references/categories.md).
- Otherwise mark N/A. Drop the criterion from the weighted average entirely.

| # | Criterion | Weight | Applies to category |
|---|-----------|--------|----------------------|
| 15 | Setup flow | 1x | library-and-api-reference, data-fetching-and-analysis, ci-cd-and-deployment, infrastructure-operations |
| 16 | Memory mechanism | 1x | business-process-automation, data-fetching-and-analysis, runbooks |
| 17 | Scripts & libraries | 1x | product-verification, code-scaffolding-and-templates, code-quality-and-review, data-fetching-and-analysis, infrastructure-operations |
| 18 | On-demand hooks | 1x | code-quality-and-review, ci-cd-and-deployment |

- Override this table with judgment, in either direction.
- Score a criterion for a skill outside the listed categories when the skill clearly benefits. Example: a non-`product-verification` skill that obviously needs a helper script.
- Mark a criterion N/A inside an applicable category when the pattern does not fit the skill's shape. Example: a pure-reference vocabulary skill filed under `code-quality-and-review` has nothing for a hook to enforce.
- Explain every override in the scorecard, in either direction.

### Overall score

```
overall = sum(score × weight) / sum(weight)
```

- Exclude N/A criteria from both sums.
- Never score an N/A criterion as 0.
- Never count the weight of an N/A criterion.

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

- Keep this heading name `Grade Scale`. The scorecard template copies this table.

| Grade | Range | Meaning |
|-------|-------|---------|
| A | 80–100 | Production-quality, reference skill |
| B | 60–79 | Good skill, minor improvements needed |
| C | 40–59 | Functional but significant gaps |
| D | 20–39 | Needs substantial rework |
| F | 0–19 | Skeleton only, not production-ready |

## Workflow

1. **Read the target skill**.
   - Read SKILL.md.
   - Read its frontmatter. Check for `disable-model-invocation`.
   - Read every file in the skill directory.
2. **Read `references/mechanics.md`**. This read is mandatory.
   - Read [references/mechanics.md](references/mechanics.md) before you score Axes 1, 3, and 4.
   - Use its vocabulary and tests, including what makes a context pointer's wording effective.
3. **Classify** the target skill.
   - Use [references/categories.md](references/categories.md) and its decision tree.
   - Assign one category.
   - The category determines which conditional criteria apply (see Conditional criteria).
4. **Score all applicable criteria**. Apply **cite-or-cut**.
   - Score a criterion only after its justification cites specific evidence (file, section, or line).
   - No citation, no score.
   - Mark N/A wherever the conditional table, or your own judgment, says a criterion does not apply.
   - Done when every applicable criterion carries a score and a citation, and every N/A carries a reason.
5. **Trigger eval**. Test empirically whether the skill's description causes invocation.
   - Follow the **Trigger Eval** section below.
   - Apply the skip rule in Trigger Eval > When to run.
6. **Diagnose failure modes**.
   - Done when every mode in the table below was checked against the skill and either cited (file:line) or dismissed.
7. **Assess bonus patterns**. Assess the 5 patterns in this table:

   | Bonus | Applies when | What to look for |
   |-------|-------------|-----------------|
   | Validation loops | Skill produces output or modifies state | Instructs the agent to self-check before finalizing |
   | Output templates | Skill generates structured output | Includes a concrete template/example of expected format |
   | Procedures over declarations | Skill teaches a method | Teaches *how to approach* problems, not *what to produce* for one case |
   | Defaults over menus | Skill offers tool/approach choices | Picks a clear default, mentions alternatives briefly |
   | Trace-checkable steering | Skill uses leading words | The leading words are distinctive enough that a user could grep the agent's reasoning traces to confirm the skill actually fired |

   Report each as Present / Absent / N/A.
8. **Compute the weighted score**.
   - Run `python3 scripts/score.py` with one `criterion:score:weight` triple per criterion.
   - Score `NA` to exclude a criterion.
   - Expect the script to print both sums, the overall, and the grade.
   - Never do this arithmetic by hand.
   - Pass the weight as a bare number (`2`, not `2x`). Pass the score as a bare number (`80`, not `80%`). The script crashes on non-numeric values.
9. **Write the scorecard** to the output path.
   - Read [references/output-template.md](references/output-template.md) first. It also holds the comparison-mode template used when `compare` is set.
   - Emit exactly that structure.

## Trigger Eval

- Test whether the skill's description causes a model to invoke it when it should, and to ignore it when it should not.
- Never use the trigger eval as a pass/fail gate.
- Produce observational data. Feed it to the scorecard and to the failure-mode diagnosis.

### When to run

- Run the eval for model-invoked skills only.
- Skip user-invoked skills (`disable-model-invocation: true`). They have no description to test.
- Mark the section N/A for a skipped skill.

### Prompt generation

Generate **10 prompts** from the skill's description, scope, and gotchas:

- **5 should-trigger**: realistic user requests that fall squarely within the skill's stated scope.
  - Vary the phrasing.
  - Use the skill's vocabulary in some prompts.
  - Describe the same need in naive/indirect language in other prompts.
- **5 should-not-trigger**: requests that are adjacent but clearly outside scope.
  - Draw them from 3 sources.
  - Source 1: a sibling skill's territory.
  - Source 2: a task the description explicitly excludes.
  - Source 3: a generic request a model handles without any skill.
- Write each prompt as a real user would type it.
- Use no meta-language about skills. Give no hints.

### Sub-agent execution

- Run each prompt in an independent sub-agent session with the target skill available.
- Append one additional instruction to the sub-agent's system context:

```
At the end of your response, output exactly one line in this format:
SKILLS_USED: <comma-separated list of skill names you loaded during this task, or "none">
```

- Keep this instruction generic.
- Never name the skill under test in it.
- Never hint at what should be triggered.
- Let the sub-agent operate normally. It loads the skill or not, based on the prompt alone.

### Detection

- Parse the `SKILLS_USED:` line from each sub-agent's response.
- Record these fields per prompt:

| Field | Value |
|-------|-------|
| Prompt | The test prompt text |
| Expected | should-trigger / should-not-trigger |
| Triggered | yes / no (was the target skill name in the list?) |
| Other skills | Any other skills that fired |

### What to report

Report raw counts. Make no pass/fail judgment:

- **Should-trigger hit rate** — X/5 triggered
- **Should-not-trigger leak rate** — X/5 triggered (lower is better)
- **Other skills observed** — which siblings fired on the same prompts

- Feed these numbers to criterion #1 (invocation design) and criterion #2 (description quality) as empirical evidence.
- Watch the numbers for failure modes such as over-triggering and description weakness.

### Practical notes

- Skip the trigger eval if the evaluation environment cannot spawn sub-agents (e.g., CI without agent access).
- Write "trigger eval: skipped (no agent access)" in the scorecard when you skip.
- Run a single trial per prompt. The eval is observational (non-gating).
- Run multiple trials only if results are ambiguous.
- Keep the prompts in the scorecard output. The skill author reuses them as a regression set.

## Failure-mode diagnosis

- Name the failure mode, cite evidence, and prescribe the defense.
- Prescribe each defense from [references/mechanics.md](references/mechanics.md) §5. That file defines each defense once.
- Never write a generic "top improvements" list.

| Mode | Evidence to look for |
|------|----------------------|
| Premature completion | Vague completion criteria with future steps still visible |
| Weak steering | Instruction present but the agent doesn't reliably follow it |
| Duplication | Same meaning in 2+ places, including SKILL.md vs. references/ |
| Sediment | Stale layers, outdated references, dead instructions |
| Sprawl | Long even with no duplication or sediment |
| No-ops | Lines that don't change behavior versus the model's default |
| Buried steps | Inline reference so heavy it soaks the steps |

- After the table, write a **Prioritized Actions** section.
- List 3–5 highest-impact actions derived directly from the detected failure modes.
- Cite the evidence for each action.
- Never score **context overload** (too many model-invoked skills competing for attention in one environment). It is a portfolio-level problem, out of scope for evaluating a single skill.
- Record the description's context-load cost when it is notable.
- Never score the portfolio.

## Gotchas

- Tiny skills (under ~50 lines) flood the scorecard with N/A. Score what is there. A small, sharp skill can reach grade A on few criteria.
- Self-evaluation bias: when the skill under review is one you (or this session) wrote, apply the deletion test with extra skepticism. You will want your own lines to matter.
- Fresh rewrites still carry duplication. Sediment needs time to settle, but duplication can ship on day one. Run the pruning axis even on brand-new skills.

## Quality Checklist

- Run this final gate before you deliver.
- Each item re-checks the completion of one step. Add no new checks.

- [ ] cite-or-cut held everywhere (step 4)
- [ ] every N/A justified (step 4)
- [ ] trigger eval run or skipped with reason (step 5)
- [ ] every failure mode cited or dismissed (step 6)
- [ ] 5 bonus patterns assessed (step 7)
- [ ] score computed by `scripts/score.py`, not by hand (step 8)

## Sources

- [Lessons from building Claude Code: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills) — Anthropic, Jun 2026
- "The Missing Manual: How to Write Great Skills" — Matt Pocock, AI Engineer World's Fair 2026 ([video](https://www.youtube.com/watch?v=UNzCG3lw6O0)), and his `writing-great-skills` skill
