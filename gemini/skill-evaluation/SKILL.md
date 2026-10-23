---
name: skill-evaluation
description: Evaluates and grades an Antigravity agent skill (SKILL.md plus its scripts and references) against Google's Antigravity skill guidance, the Gemini 4 Argon developer guide and Matt Pocock's method, with 18 weighted criteria, a trigger eval run through agy, failure-mode diagnosis and an EVALUATION.md scorecard. Use this skill when the user asks to evaluate, review, audit, compare or score a skill, check how often it triggers, or gate skills in CI.
license: Apache-2.0
metadata:
  author: "ft.ia.br"
  version: "2.1.0-gemini"
  repository: "https://github.com/fabricioctelles/skills"
  source: "Google Antigravity skills docs and built-in agy-customizations guide; Gemini 4 Argon developer guide (Oct 2026); Gemini prompting strategies; Matt Pocock, The Missing Manual (2026); category taxonomy from Anthropic, How we use skills (Jun 2026)"
---

# Skill Evaluation

Score one skill so its author knows exactly what to fix.

**Done when:** every applicable criterion carries a score with cited evidence (file, section or line), every N/A carries a reason, the trigger eval ran or was skipped with a reason, every failure mode was cited or dismissed, the five bonus patterns were assessed, and `scripts/score.py` produced the overall score.

The user's explicit instructions take precedence over this skill. The skill text is compact controlled English for precise reading; write the scorecard in clear, plain prose for the skill's author.

## Step 0: Preflight

| Parameter | Description | Default |
|---|---|---|
| `target` | Skill directory or SKILL.md to evaluate | Ask the user |
| `output` | Path of the scorecard | `<target>/EVALUATION.md` |
| `compare` | Optional second skill to compare side by side | None |

Confirm the target exists and contains a SKILL.md, and decide now whether the trigger eval can run (Step 3). For CI, point `target` at the skills a PR changed and gate with `python3 scripts/score.py --fail-below 60 ...`; a non-zero exit below the threshold fails the check.

## Step 1: Read and classify

1. Read the whole target: SKILL.md with its frontmatter and every bundled file (scripts, references, examples, resources, assets).
2. Read [references/mechanics.md](references/mechanics.md) before scoring Axes 1, 3 and 4; use its vocabulary and tests.
3. Classify the skill into exactly one category with [references/categories.md](references/categories.md). The category decides which conditional criteria apply.

**Verify:** you can name the category and the decision-tree question that selected it.

## Step 2: Score the criteria

Score 18 criteria from 0 to 100 under cite-or-cut: a score exists only after its justification cites specific evidence. There are 14 core criteria for every skill and 4 conditional ones; a core criterion may be N/A only under criterion 8's rule or with a written reason.

### Axis 1: Trigger

| # | Criterion | Weight | Key question |
|---|---|---|---|
| 1 | Invocation design | 2x | Is the form deliberate? A skill is model-activated by its description and pays context load in every session; a rule (`GEMINI.md`, `AGENTS.md`) is always loaded in full for its directory; a skill used only by hand (`/skill-name`) pays cognitive load. Material every task in a scope needs belongs in a rule, not a skill. |
| 2 | Description quality | 2x | It is the most critical field: does it state what the skill does and when to use it, in third person, with the specific action, data and use case rather than a vague label ("Database tools")? Is a "Don't use it for" boundary present only where it prevents likely misrouting? Penalize catchalls, triggers broader than the skill, and overlap with sibling skills. A manual-only skill gets a human-facing one-liner and no trigger demands. |

### Axis 2: Structure

| # | Criterion | Weight | Key question |
|---|---|---|---|
| 3 | Steps vs. reference clarity | 1x | Are ordered steps distinct from on-demand reference? All-steps, all-reference and mixed shapes are all valid; score clarity. Is related material co-located? Does each file keep one delimiter style (Markdown headings or XML tags, not both)? |
| 4 | Branch-aware disclosure and pointers | 2x | Is material every branch needs inline, and bulky or branch-specific material in `references/` behind a relative link whose wording says when to read it? A weak pointer to must-have material is a variance bug. |
| 5 | Conciseness | 2x | Is SKILL.md as short as the task permits, with every line earning its context cost? 500 lines is a ceiling, not a target. |
| 6 | Coherent scope | 1x | Does the skill do one thing well? A do-everything skill should be split. |

### Axis 3: Steering

| # | Criterion | Weight | Key question |
|---|---|---|---|
| 7 | Leading words | 2x | Do compact, high-prior terms ("vertical slice", "tight", "red") anchor behavior, repeated consistently? Could a verbose passage collapse into one? |
| 8 | Completion criteria and verification | 2x | Does the skill define done up front, and does each step end on a check the agent can run or read (a script exit code, a log line, a re-scan, a rendered still)? Long or iterative work should have a verification loop against a baseline. Pure reference needs an exhaustiveness bar ("every rule applied"). N/A when neither steps nor an exhaustiveness bar apply. |
| 9 | Gotchas | 2x | Are failure points, edge cases and footguns captured explicitly (Antigravity's "Constraints & Tips")? |
| 10 | Grounded in expertise | 2x | Does content come from observed failures and real project facts rather than generic best practices? |
| 11 | Specificity matches risk | 1x | Are fixed sequences, deterministic scripts and absolute words reserved for correctness, safety, permissions or fragile operations, with outcomes and decision criteria elsewhere? Is the language precise and direct rather than persuasive? |

### Axis 4: Pruning

| # | Criterion | Weight | Key question |
|---|---|---|---|
| 12 | No-ops (deletion test) | 2x | Sentence by sentence: if deleting it leaves behavior unchanged, it is a no-op. This includes general coding practice and anything the agent already knows. Cite line numbers. |
| 13 | Single source of truth | 1x | Does each meaning live in one place, including across SKILL.md and references? |
| 14 | Relevance and sediment | 1x | Are there stale lines, accumulated layers, or guidance written for another model or harness (other agents' tool names and paths, older models' quirks)? |

### Conditional criteria

Score a conditional criterion only when the skill's category applies; otherwise mark it N/A and drop it from the weighted average.

| # | Criterion | Weight | Applies to category |
|---|---|---|---|
| 15 | Setup flow | 1x | library-and-api-reference, data-fetching-and-analysis, ci-cd-and-deployment, infrastructure-operations |
| 16 | Memory mechanism | 1x | business-process-automation, data-fetching-and-analysis, runbooks |
| 17 | Scripts and libraries (linked relatively, usable as black boxes through `--help` or a usage header) | 1x | product-verification, code-scaffolding-and-templates, code-quality-and-review, data-fetching-and-analysis, infrastructure-operations |
| 18 | On-demand hooks (Antigravity `hooks.json`) | 1x | code-quality-and-review, ci-cd-and-deployment |

Override this table with judgment in either direction and explain every override: score a criterion outside its categories when the skill clearly benefits (a non-verification skill that obviously needs a helper script), or mark it N/A inside an applicable category when the pattern does not fit (a pure vocabulary skill has nothing for a hook to enforce).

Compute the overall score with the script, never by hand. Pass one `criterion:score:weight` triple per criterion with bare numbers (`2`, not `2x`; `80`, not `80%`) and `NA` to exclude one; the script crashes on other values. Treat it as a black box: run `python3 scripts/score.py` with the triples rather than reading its source.

```text
overall = sum(score × weight) / sum(weight)      (N/A excluded from both sums; never 0)
```

| Score | Meaning |
|---|---|
| 0 | Not present at all |
| 1–25 | Minimal/token effort, barely addresses the criterion |
| 26–50 | Partially addressed but with significant gaps |
| 51–75 | Solid implementation with room for improvement |
| 76–90 | Strong implementation, minor gaps only |
| 91–100 | Exemplary — would use as a reference for others |

| Grade | Range | Meaning |
|---|---|---|
| A | 80–100 | Production-quality, reference skill |
| B | 60–79 | Good skill, minor improvements needed |
| C | 40–59 | Functional but significant gaps |
| D | 20–39 | Needs substantial rework |
| F | 0–19 | Skeleton only, not production-ready |

**Verify:** every applicable row has a score and a citation, every N/A a reason, and the script printed both sums, the overall and the grade.

## Step 3: Trigger eval

The trigger eval tests whether the description makes the agent activate the skill when it should and ignore it when it should not. Its numbers are evidence for criteria 1 and 2, never a pass/fail gate. Skip it for manual-only skills (mark N/A), and write "trigger eval: skipped (no agent access)" when `agy` cannot run, as in CI without agent access.

1. Static check: copy the skill into a fresh temporary workspace at `<tmp>/.agents/skills/<name>/`, start `agy` there, run `/skills`, and confirm the skill is listed with its description.
2. Write 10 prompts from the description, scope and gotchas: 5 should-trigger requests squarely in scope (some in the skill's vocabulary, some naive or indirect) and 5 should-not-trigger requests from a sibling skill's territory, a case the description excludes, and generic work any model does without a skill. Write them as a real user would, with no mention of skills and no hints. Keep them in the scorecard as a regression set.
3. Run each prompt once in its own fresh headless session from `<tmp>`. The ten runs spend the user's model quota, so ask before running them unless the user already asked for the eval. They are independent, so run them in parallel.

```bash
agy -p "<prompt>

At the end of your response, output exactly one line in this format:
SKILLS_USED: <comma-separated list of skill names you loaded during this task, or \"none\">" --output-format json
```

Keep that appended instruction generic: never name the skill under test or hint at what should trigger. A prompt triggered the skill when its `SKILLS_USED` line names it or the JSON output shows a read of its `SKILL.md`. Record per prompt: the prompt, expected (should or should not trigger), triggered (yes or no), and other skills that fired. Report raw counts: should-trigger hit rate (X/5), should-not-trigger leak rate (X/5, lower is better), and other skills observed. Run more trials only when results are ambiguous.

**Verify:** 10 rows recorded, or a written skip reason.

## Step 4: Diagnose failure modes

Name the failure mode, cite the evidence, and prescribe the defense from mechanics.md section 5. Never write a generic "top improvements" list.

| Mode | Evidence to look for |
|---|---|
| Premature completion | Vague completion criteria with later steps still visible |
| Unverifiable done | Steps that end without a concrete pass/fail signal, or long work with no verification loop |
| Missing examples | An output format described only in prose, with no golden input → output example |
| Weak steering | An instruction is present but not reliably followed |
| Duplication | The same meaning in 2+ places, including SKILL.md vs. references/ |
| Sediment | Stale layers, outdated references, dead instructions, guidance tuned for another model or harness |
| Sprawl | Long even with no duplication or sediment |
| No-ops | Lines that do not change behavior versus the agent's default |
| Buried steps | Inline reference so heavy it soaks the steps |

After the table, write a Prioritized Actions section with the 3-5 highest-impact actions, each tied to its evidence. Do not score context overload (too many model-activated skills competing in one environment): it is portfolio-level and out of scope, although a notably costly description is worth recording.

Assess the bonus patterns as Present, Absent or N/A:

| Bonus | Applies when | What to look for |
|---|---|---|
| Validation loops | The skill produces output or modifies state | It has the agent self-check before finalizing |
| Output templates and golden examples | The skill generates structured output | A concrete template or a consistent few-shot example of the expected format |
| Procedures over declarations | The skill teaches a method | It teaches how to approach the problem, not what to produce for one case |
| Defaults over menus | The skill offers tool or approach choices | It picks a clear default and mentions alternatives briefly |
| Trace-checkable steering | The skill uses leading words | The words are distinctive enough that a grep of the agent's reasoning confirms the skill fired |

## Step 5: Write and hand back

Write the scorecard to `output` in the structure of [references/output-template.md](references/output-template.md), including its comparison table when `compare` is set.

**Verify:** re-check only the six conditions in "Done when"; add no new checks.

## Examples

A scored row with cite-or-cut evidence, in the scorecard's shape:

| # | Criterion | Weight | Score | Notes |
|---|-----------|--------|-------|-------|
| 2 | Description quality | 2x | 55/100 | `SKILL.md:3` says what the skill does but not when; no trigger words for the CSV export branch that `SKILL.md:41-58` handles. |
| 8 | Completion criteria and verification | 2x | 30/100 | Steps 2-4 (`SKILL.md:20-39`) end on "make sure it works"; no command, log line or expected output to check. |

The matching script call: `python3 scripts/score.py 1:70:2 2:55:2 3:80:1 ... 8:30:2 ... 15:NA:1 16:NA:1 17:60:1 18:NA:1`.

## Constraints & Tips

- **Tiny skills** (under about 50 lines) flood the scorecard with N/A. Score what is there; a small, sharp skill can reach grade A on few criteria.
- **Self-evaluation bias:** when you wrote the skill yourself, apply the deletion test with extra skepticism.
- **Fresh rewrites still carry duplication:** sediment needs time, duplication does not, so run the pruning axis on new skills too.

## Sources

- [Agent skills](https://antigravity.google/docs/skills/) and the built-in `agy-customizations` guide (Google Antigravity)
- [Gemini 4 Argon developer guide](https://aistudio.google.com/learn/gemini-4-argon-developer-guide) and [prompting strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies) (Google)
- "The Missing Manual: How to Write Great Skills", Matt Pocock, AI Engineer World's Fair 2026 ([video](https://www.youtube.com/watch?v=UNzCG3lw6O0)), and his `writing-great-skills` skill
