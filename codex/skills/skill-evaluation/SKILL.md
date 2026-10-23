---
name: skill-evaluation
description: Evaluate or grade a Codex skill (SKILL.md, agents/openai.yaml and bundled files) against OpenAI's skill-creator and GPT-6 guidance plus Matt Pocock's method, with 18 weighted criteria, a trigger eval run through codex exec, failure-mode diagnosis and an EVALUATION.md scorecard. Use to review, compare or CI-gate skills.
license: Apache-2.0
metadata:
  author: "ft.ia.br"
  version: "2.1.0-codex"
  repository: "https://github.com/fabricioctelles/skills"
  source: "OpenAI skill-creator and Build skills docs; Rethinking skills and prompts for GPT-6 Astra (OpenAI, Sep 2026); Matt Pocock, The Missing Manual (2026); category taxonomy from Anthropic, How we use skills (Jun 2026)"
---

# Skill Evaluation

Score one skill so its author knows exactly what to fix. The scorecard is done when every applicable criterion carries a score with a cited piece of evidence (file, section or line), every N/A carries a reason, the trigger eval ran or was skipped with a reason, every failure mode was cited or dismissed, the five bonus patterns were assessed, and `scripts/score.py` produced the overall score.

The user's explicit instructions take precedence over this skill. The skill text is compact controlled English for precise reading; write the scorecard in clear, plain prose for the skill's author.

## Parameters

| Parameter | Description | Default |
|---|---|---|
| `target` | Skill directory or SKILL.md to evaluate | Ask the user |
| `output` | Path of the scorecard | `<target>/EVALUATION.md` |
| `compare` | Optional second skill to compare side by side | None |

For CI, point `target` at the skills a PR changed and gate with `python3 scripts/score.py --fail-below 60 ...`; a non-zero exit below the threshold fails the check. Call the script as `python3 scripts/score.py`, not `./scripts/score.py`.

## Workflow

1. Read the whole target: SKILL.md with its frontmatter, `agents/openai.yaml` (invocation policy, interface, dependencies) and every bundled file.
2. Read [references/mechanics.md](references/mechanics.md) before scoring Axes 1, 3 and 4; use its vocabulary and tests.
3. Classify the skill into exactly one category with [references/categories.md](references/categories.md). The category decides which conditional criteria apply.
4. Score every applicable criterion under cite-or-cut: a score exists only after its justification cites specific evidence.
5. Run the trigger eval (below).
6. Check every failure mode in the table below against the skill; cite it (file:line) or dismiss it.
7. Assess the 5 bonus patterns as Present, Absent or N/A.
8. Run `python3 scripts/score.py` with one `criterion:score:weight` triple per criterion, using `NA` as the score to exclude one. Pass bare numbers (`2`, not `2x`; `80`, not `80%`); the script crashes on other values. It prints both sums, the overall score and the grade, so do no arithmetic by hand.
9. Write the scorecard to `output` in the structure of [references/output-template.md](references/output-template.md), including its comparison table when `compare` is set.

## Criteria

Score 18 criteria from 0 to 100: 14 core criteria for every skill and 4 conditional ones. A core criterion may be N/A only under criterion 8's rule or with a written reason.

### Axis 1: Trigger

| # | Criterion | Weight | Key question |
|---|---|---|---|
| 1 | Invocation design | 2x | Is implicit invocation (the default) or explicit-only (`policy.allow_implicit_invocation: false` in `agents/openai.yaml`) chosen deliberately? An implicit skill pays context load: its name and description sit in the skill list of every session, inside a budget of about 2% of the context window, and Codex shortens descriptions when many skills compete. An explicit-only skill pays cognitive load: the user must remember `$skill-name`. A skill that only ever fires by hand should be explicit-only. |
| 2 | Description quality | 2x | Implicit: does it say what the skill does and when it applies, front-load the key use case, and add a boundary only where it prevents likely misrouting? Penalize exhaustive keyword lists, catchalls that attract adjacent work, triggers broader than the skill (the "any database task" pattern for a migrations skill), and overlap with sibling skills. Explicit-only: a human-facing one-liner, scored without trigger demands. Check `interface.short_description` (25-64 characters) and that `default_prompt` mentions `$skill-name`. |

### Axis 2: Structure

| # | Criterion | Weight | Key question |
|---|---|---|---|
| 3 | Steps vs. reference clarity | 1x | Are ordered steps distinct from on-demand reference? All-steps, all-reference and mixed shapes are all valid; score clarity. Is related material co-located? |
| 4 | Branch-aware disclosure and pointers | 2x | Is material every branch needs inline, and branch-specific material behind a pointer whose wording says when to follow it? A weak pointer to must-have material is a variance bug. A multi-workflow skill should have a minimal router; a simple skill needs none. |
| 5 | Conciseness | 2x | Is SKILL.md as short as the task permits, with every line earning its context cost? 500 lines is a ceiling, not a target. |
| 6 | Coherent scope | 1x | Does the skill do one job and compose with others, without expanding the user's task or implying extra permissions? |

### Axis 3: Steering

| # | Criterion | Weight | Key question |
|---|---|---|---|
| 7 | Leading words | 2x | Do compact, high-prior terms ("vertical slice", "tight", "red") anchor behavior, repeated consistently? Could a verbose passage collapse into one? |
| 8 | Completion criteria and legwork | 2x | Does the skill define done up front, and does each step end on a checkable, exhaustive criterion? Pure reference needs an exhaustiveness bar ("every rule applied"). A mandatory stop for review after a first pass pulls GPT-6 toward stopping early. N/A when neither steps nor an exhaustiveness bar apply. |
| 9 | Gotchas | 2x | Are failure points, edge cases and footguns captured explicitly? |
| 10 | Grounded in expertise | 2x | Does content come from observed failures and real project facts rather than generic best practices? |
| 11 | Specificity matches risk | 1x | Are fixed sequences, narrow parameters and absolute words (always, never, must) reserved for correctness, safety, permissions or genuinely fragile operations, with outcomes and decision criteria elsewhere? "Ask first" gates on reversible work make GPT-6 pause. |

### Axis 4: Pruning

| # | Criterion | Weight | Key question |
|---|---|---|---|
| 12 | No-ops (deletion test) | 2x | Sentence by sentence: if deleting it leaves behavior unchanged, it is a no-op. This includes what Codex already does (generic advice, "be thorough", pushes to test or verify that it does by default) and policies already enforced by AGENTS.md, plugins or the harness. Cite line numbers. |
| 13 | Single source of truth | 1x | Does each meaning live in one place, including across SKILL.md and references? |
| 14 | Relevance and sediment | 1x | Are there stale lines, accumulated layers, or guidance written for another model or harness (other agents' tool names, older models' quirks, rules that compensated for weaker judgment)? |

### Conditional criteria

Score a conditional criterion only when the skill's category (from categories.md) applies; otherwise mark it N/A and drop it from the weighted average.

| # | Criterion | Weight | Applies to category |
|---|---|---|---|
| 15 | Setup flow | 1x | library-and-api-reference, data-fetching-and-analysis, ci-cd-and-deployment, infrastructure-operations |
| 16 | Memory mechanism | 1x | business-process-automation, data-fetching-and-analysis, runbooks |
| 17 | Scripts and libraries | 1x | product-verification, code-scaffolding-and-templates, code-quality-and-review, data-fetching-and-analysis, infrastructure-operations |
| 18 | On-demand hooks (Codex `hooks.json`) | 1x | code-quality-and-review, ci-cd-and-deployment |

Override this table with judgment in either direction and explain every override in the scorecard: score a criterion outside its categories when the skill clearly benefits (a non-verification skill that obviously needs a helper script), or mark it N/A inside an applicable category when the pattern does not fit (a pure vocabulary skill has nothing for a hook to enforce).

### Overall score and grades

```text
overall = sum(score × weight) / sum(weight)
```

Exclude N/A criteria from both sums; N/A is never 0 and never carries weight.

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

## Trigger eval

The trigger eval tests whether the description makes Codex use the skill when it should and ignore it when it should not. Its numbers are evidence for criteria 1 and 2, never a pass/fail gate. Skip it for explicit-only skills (mark N/A), and write "trigger eval: skipped (no agent access)" when Codex cannot run, as in CI without agent access.

Start with the free static check. Copy the skill into a fresh temporary workspace at `<tmp>/.agents/skills/<name>/`, run `codex debug prompt-input "hello"` from `<tmp>`, and confirm the skill appears in the `<skills_instructions>` list with its whole description. A shortened or missing entry is a criterion 2 finding.

Then write 10 prompts from the description, scope and gotchas: 5 should-trigger requests squarely in scope (some in the skill's vocabulary, some naive or indirect) and 5 should-not-trigger requests from a sibling skill's territory, a case the description excludes, and generic work any model does without a skill. Write them as a real user would, with no mention of skills and no hints. Keep them in the scorecard as a regression set.

Run each prompt once in its own fresh session in that workspace, read-only and not persisted. The ten runs spend the user's model quota, so ask before running them unless the user already asked for the eval.

```bash
codex exec --json --ephemeral --skip-git-repo-check -s read-only -C <tmp> -o <tmp>/out-N.txt "<prompt>

At the end of your response, output exactly one line in this format:
SKILLS_USED: <comma-separated list of skill names you loaded during this task, or \"none\">"
```

Keep that appended instruction generic: never name the skill under test or hint at what should trigger. A prompt triggered the skill when its `SKILLS_USED` line names it or the JSONL event stream shows a read of its `SKILL.md`. Record per prompt: the prompt, expected (should or should not trigger), triggered (yes or no), and other skills that fired. Report raw counts without judgment: should-trigger hit rate (X/5), should-not-trigger leak rate (X/5, lower is better), and other skills observed on the same prompts. Run more trials only when results are ambiguous.

## Failure-mode diagnosis

Name the failure mode, cite the evidence, and prescribe the defense from mechanics.md section 5. Never write a generic "top improvements" list.

| Mode | Evidence to look for |
|---|---|
| Premature completion | Vague completion criteria with later steps still visible |
| Early stop | Absolute language, "ask first" gates on reversible work, or guidance that conflicts with the user, AGENTS.md or another skill, which makes GPT-6 pause or ask for approval it does not need |
| Weak steering | An instruction is present but not reliably followed |
| Duplication | The same meaning in 2+ places, including SKILL.md vs. references/ |
| Sediment | Stale layers, outdated references, dead instructions, guidance tuned for another model |
| Sprawl | Long even with no duplication or sediment |
| No-ops | Lines that do not change behavior versus Codex's default |
| Over-testing | Instructions that push tests or repeated verification for small reversible changes |
| Buried steps | Inline reference so heavy it soaks the steps |

After the table, write a Prioritized Actions section with the 3-5 highest-impact actions, each tied to its evidence. Do not score context overload (too many implicit skills competing in one environment): it is portfolio-level and out of scope, although a notably costly description is worth recording.

## Bonus patterns

| Bonus | Applies when | What to look for |
|---|---|---|
| Validation loops | The skill produces output or modifies state | It has the agent self-check before finalizing |
| Output templates | The skill generates structured output | A concrete template or example of the expected format |
| Procedures over declarations | The skill teaches a method | It teaches how to approach the problem, not what to produce for one case |
| Defaults over menus | The skill offers tool or approach choices | It picks a clear default and mentions alternatives briefly |
| Trace-checkable steering | The skill uses leading words | The words are distinctive enough that a grep of the agent's reasoning confirms the skill fired |

## Gotchas

- Tiny skills (under about 50 lines) flood the scorecard with N/A. Score what is there; a small, sharp skill can reach grade A on few criteria.
- When you wrote the skill yourself, apply the deletion test with extra skepticism.
- Fresh rewrites still carry duplication: sediment needs time, duplication does not, so run the pruning axis on new skills too.
- Before the final write, re-check only the six completion conditions in the opening paragraph; add no new checks.

## Sources

- OpenAI `$skill-creator` (bundled with Codex) and [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra), OpenAI, Sep 2026, and the GPT-6 [prompting best practices](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra#prompting-best-practices)
- "The Missing Manual: How to Write Great Skills", Matt Pocock, AI Engineer World's Fair 2026 ([video](https://www.youtube.com/watch?v=UNzCG3lw6O0)), and his `writing-great-skills` skill
