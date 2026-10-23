# Mechanics: Predictability, Invocation, Hierarchy, Steering, Failure Modes

- Use this file to score Axes 1, 3, and 4.
- This file condenses Matt Pocock's `writing-great-skills` GLOSSARY. Sync it manually when the upstream GLOSSARY changes. Never require `writing-great-skills` at runtime.
- Look up each bolded term here. Never re-derive it.

## 1. Root virtue: Predictability

- **Predictability**: the agent takes the same *process* every run, not the same output. A brainstorming skill predictably diverges: its tokens vary, its behavior does not.
- Judge every rubric criterion as a lever on predictability. Treat conciseness, steering, and pruning as symptoms of predictability, not competing virtues.

## 2. Invocation trade-off

- **Model activation**: the normal path for a skill. Antigravity injects every skill's name and description into the context, and the agent reads the full SKILL.md only when a request matches the description. The user can also force a skill by naming it, or with `/<skill-name>` in the CLI, which turns each skill into a slash command.
  - Model-activated skills pay permanent **context load**: their descriptions share the customization budget with workflows, subagents and MCP tools in every session. The benefit is autonomous activation and reachability by other skills.
- **Rule** (`GEMINI.md`, `AGENTS.md`): always active for its directory and loaded in full, inside a 20,000-token rules budget and a 24 KB per-file cap. A rule fits a constraint that every task in that scope needs; a skill fits a procedure that only some tasks need.
- **Manual use**: the documentation describes no switch that keeps a skill out of model activation. A skill meant to fire only by hand needs a narrow, human-facing description so it rarely matches, and pays **cognitive load**: the human becomes the index of which skills exist and when to type each.
- Pick model activation only when the agent must reach the skill on its own, or another skill must reach it.
- Keep a sensitive workflow discoverable and gate the mutation itself, rather than hiding the skill.
- **router skill**: one skill that names the other skills and when to reach for each.
  - Use it to cure accumulated cognitive load when manually used skills multiply past what a human can remember.
  - Treat this fix as portfolio-level. Never score portfolio-level problems: this evaluation scores one skill.

## 3. Content types & hierarchy

- **steps**: ordered actions, each ending on a **completion criterion**. **reference**: definitions, rules, and facts consulted on demand.
- Treat all-steps, all-reference, and mixed skills as equally valid. Never flag one shape as a smell.
- **information hierarchy**: a ranking of material by how immediately the agent needs it. In-skill step first, then in-skill reference, then reference disclosed behind a **context pointer** in a linked file.
- **branch**: a distinct way the skill is invoked.
  - Put material that every branch needs inline.
  - Put material that only some branches need behind a pointer. Branching is the disclosure test.
- Judge a pointer by its *wording*, not its target: the wording decides whether and how reliably the agent reaches it.
  - Flag a must-have target behind weak pointer wording as a variance bug.
  - Sharpen the wording first. Pull the material back inline only if that fails.
- **Co-location**: keep a concept's definition, rules, and caveats under one heading. Never scatter them: reading one part must bring its neighbors.

## 4. Steering

- **Leading words**: compact, pretrained concepts (*tight*, *red*, *lesson*) the agent thinks with while executing.
  - Repeat each leading word consistently. Repeats recruit priors the model already holds and anchor a region of behavior in the fewest tokens.
  - Prefer one leading word over a prose passage that spells out the same quality.
  - In the body, a leading word anchors execution: the same behavior fires every time the word appears. In the description, it anchors invocation.
  - **trace-checkable**: distinctive enough that the word's appearance in the agent's reasoning traces confirms the skill shaped behavior.
- Require each completion criterion to be *checkable* (the agent can tell done from not-done) and, where it matters, *exhaustive*. Write "every X accounted for". Never write "produce a list".
- Flag a vague criterion. It invites **premature completion**: attention slipping to being done rather than to the work.
- Apply the exhaustiveness demand to flat reference with no steps: write "every rule applied". It drives thorough **legwork** over a checklist, as a sharp step criterion does over an action.
- Make skills **avoid railroading**. Write procedures the agent adapts, not declarations of exact output. Write defaults with brief alternatives, not exhaustive menus.

## 5. Failure modes

- Name the failure mode, then prescribe its defense from this section. Never restate a defense elsewhere.
- **Premature completion**: ending a step before it is genuinely done. Apply these defenses in order:
  1. Sharpen the completion criterion. This is cheap and local.
  2. Split the sequence so later steps are hidden. Do this only if the criterion is irreducibly vague *and* the rush is actually observed.
- **Duplication**: the same meaning in more than one place, including across SKILL.md and references/. It costs maintenance and tokens and inflates that meaning's rank past its real weight. Fix: collapse it to a **single source of truth**, via a leading word where possible.
- **Sediment**: stale layers that accumulate in a skill. Expect it in any skill without a pruning discipline. Run the pruning axis (Axis 4) on every skill.
- **Sprawl**: a skill that is simply too long, regardless of stale or duplicated lines. Cure: disclose reference behind pointers, and split by branch or sequence so each path carries only what it needs.
- **No-op**: a line that changes nothing because the model already does it by default. Test each line: does it change behavior versus the default?
  - Apply the **deletion test** sentence by sentence, not paragraph by paragraph. Delete the whole sentence if removing it leaves behavior unchanged. Never trim words from it.
  - Classify a weak leading word as a no-op, such as *be thorough* when the agent is already thorough-ish. Fix it with a stronger word (*relentless*), not a different technique.
- **Weak steering**: an instruction that is present but the agent does not reliably follow. Check for a leading word too weak to beat the default. Check for no leading word where a verbose passage tries to do its job.
- **Buried steps**: in-file reference so heavy it soaks the steps beneath it. Attention to those steps becomes a coin-flip. Defense: use progressive disclosure, pushing the reference behind a pointer.

- **Unverifiable done**: steps that end without a concrete pass/fail signal make the model guess whether it succeeded. Gemini 4 Argon does its best long-horizon work against a real feedback loop. Apply these defenses in order:
  1. End each step with a check the agent can run or read (a script exit code, a log line, a re-scan, a rendered still).
  2. For long or iterative work, have the agent write a reproducible verification script, record a baseline, and re-run it after every change until the target is met.
- **Missing examples**: an output format described only in prose. Gemini follows one consistent few-shot example more reliably than a description. Fix: add 1-2 golden input → output examples with identical formatting; more than a few invites overfitting to them.

**Relevance vs. no-op**: two separate checks. Check relevance: does the line still bear on the task? Check no-op: does the line change behavior? Run both checks. Neither implies the other. A line can be relevant (right topic) and still be a no-op (the model would do it anyway).
