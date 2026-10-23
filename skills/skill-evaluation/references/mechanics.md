# Mechanics: Predictability, Invocation, Hierarchy, Steering, Failure Modes

- Use this file to score Axes 1, 3, and 4 of the skill-evaluation rubric (see [../SKILL.md](../SKILL.md)).
- Treat this file as a self-contained condensation of Matt Pocock's `writing-great-skills` GLOSSARY.
- Look up each bolded term here. Never re-derive it.
- Sync this file manually when the upstream `writing-great-skills` GLOSSARY changes.
- Never require `writing-great-skills` to be installed at runtime.

## 1. Root virtue: Predictability

- Define **Predictability** as the agent taking the same *process* every run.
- Never define predictability as producing the same output.
- Example: a brainstorming skill should predictably diverge. Its tokens vary. Its behavior does not.
- Judge every criterion in the rubric as a lever on predictability.
- Treat conciseness, steering, and pruning as symptoms of predictability, not separate virtues competing with it.

## 2. Invocation trade-off

- Classify each skill into one of two invocation modes. Each mode pays a different cost.

Model-invoked mode:

- Define **Model-invoked** as the default mode: the skill has no `disable-model-invocation` field.
- Expect the skill to keep a description the agent reads every turn.
- Charge the skill permanent **context load**: tokens and attention spent on every turn.
- Count autonomous firing and reachability by other skills as the benefit.

User-invoked mode:

- Define **User-invoked** as the mode set by `disable-model-invocation: true`.
- Expect the description to be stripped from the agent's reach.
- Expect that only a human typing the skill's name can fire the skill.
- Expect that no other skill can reach the skill.
- Charge the skill zero context load.
- Charge the skill **cognitive load**: the human becomes the index of which skills exist and when to reach for each.

Selection rule:

- Pick model-invocation only in these two cases:
  - The agent must reach the skill on its own.
  - Another skill must reach the skill.
- Make a skill that only ever fires by hand user-invoked.
- Remove from a hand-fired skill any trigger scaffolding it does not need.
- Define a **router skill** as one user-invoked skill that names the other skills and when to reach for each.
- Use a **router skill** to cure accumulated cognitive load when user-invoked skills multiply past what a human can remember.
- Treat the router-skill fix as portfolio-level, not single-skill level.
- Never score portfolio-level problems in this evaluation. This evaluation scores one skill.

## 3. Content types & hierarchy

- Expect a skill to mix two content types freely.
- Define **steps** as ordered actions, each ending on a **completion criterion**.
- Define **reference** as definitions, rules, and facts consulted on demand.
- Treat all-steps, all-reference, and mixed skills as equally valid.
- Never flag any one of these shapes as a smell.

Information hierarchy:

- Define the **information hierarchy** as a ranking of material by how immediately the agent needs it.
- Rank 1: in-skill step.
- Rank 2: in-skill reference.
- Rank 3: reference disclosed behind a **context pointer** in a linked file.

Branch disclosure test:

- Define a **branch** as a distinct way the skill is invoked.
- Put material that every branch needs inline.
- Put material that only some branches need behind a pointer.
- Use branching as the disclosure test.

Pointer wording:

- Judge a pointer by its *wording*, not its target.
- Expect the wording to decide whether the agent reaches the target and how reliably.
- Flag a must-have target behind weak pointer wording as a variance bug.
- Fix the bug by sharpening the pointer wording first.
- Pull the material back inline only after sharper wording fails.

Co-location:

- Apply **Co-location** to content once it is placed.
- Keep a concept's definition, rules, and caveats under one heading.
- Never scatter them. Reading one part must bring its neighbors with it.

## 4. Steering

Leading words:

- Define **Leading words** as compact, pretrained concepts (*tight*, *red*, *lesson*) the agent thinks with while executing.
- Repeat each leading word consistently.
- Expect repeated leading words to recruit priors the model already holds.
- Expect them to anchor a region of behavior in the fewest tokens.
- Prefer one leading word over a prose passage that spells out the same quality.
- Use a leading word in the body to anchor execution. The same behavior fires every time the word appears.
- Use a leading word in the description to anchor invocation.
- Define **trace-checkable** as distinctive enough that the word's appearance in the agent's reasoning traces confirms the skill actually shaped behavior.

Completion criteria:

- Require each completion criterion to be *checkable*: the agent can tell done from not-done.
- Require a completion criterion to be *exhaustive* where it matters.
- Write "every X accounted for". Never write "produce a list".
- Flag a vague criterion. It invites **premature completion**: attention slipping to being done rather than to the work.
- Apply the exhaustiveness demand to flat reference with no steps.
- Write "every rule applied" for flat reference.
- Expect "every rule applied" to drive thorough **legwork** over a checklist.
- Expect a sharp step criterion to drive the same legwork over an action.

Railroading:

- Make skills **avoid railroading**.
- Write procedures the agent adapts, not declarations of exact output.
- Write defaults with brief alternatives, not exhaustive menus.

## 5. Failure modes

- Name the failure mode, then prescribe its defense from this section.
- Define each defense once, here. Never restate a defense elsewhere.

**Premature completion**:

- Define **Premature completion** as ending a step before it is genuinely done.
- Apply these defenses in order.
- Defense 1: sharpen the completion criterion. This is cheap and local.
- Defense 2: split the sequence so later steps are hidden.
- Apply defense 2 only if the criterion is irreducibly vague *and* the rush is actually observed.

**Duplication**:

- Define **Duplication** as the same meaning in more than one place, including across SKILL.md and references/.
- Expect two costs: maintenance and tokens.
- Expect duplication to inflate that meaning's rank past its real weight.
- Fix: collapse the meaning to a **single source of truth**.
- Collapse via a leading word where possible.

**Sediment**:

- Define **Sediment** as stale layers that accumulate in a skill.
- Expect sediment in any skill without a pruning discipline.
- Run the pruning axis (Axis 4) on every skill.

**Sprawl**:

- Define **Sprawl** as a skill that is simply too long.
- Judge sprawl independent of whether lines are stale or duplicated.
- Cure sprawl: disclose reference behind pointers.
- Cure sprawl: split by branch or sequence so each path carries only what it needs.

**No-op**:

- Define **No-op** as a line that changes nothing because the model already does it by default.
- Test each line: does it change behavior versus the default?
- Apply the **deletion test** sentence by sentence, not paragraph by paragraph.
- Delete the whole sentence if removing it leaves behavior unchanged.
- Never trim words from a no-op sentence.
- Classify a weak leading word as a no-op. Example: *be thorough* when the agent is already thorough-ish.
- Fix a weak leading word with a stronger word (*relentless*), not a different technique.

**Weak steering**:

- Define **Weak steering** as an instruction that is present but the agent does not reliably follow.
- Check for a leading word too weak to beat the default.
- Check for no leading word at all where a verbose passage is trying to do its job.

**Buried steps**:

- Define **Buried steps** as in-file reference so heavy it soaks the steps beneath it.
- Expect attention to those steps to become a coin-flip.
- Defense: use progressive disclosure. Push the reference behind a pointer.

**Relevance vs. no-op**:

- Define **Relevance vs. no-op** as two separate checks.
- Check relevance: does the line still bear on the task?
- Check no-op: does the line change behavior?
- Run both checks. Neither implies the other.
- Expect a line to be relevant (right topic) and still be a no-op (the model would do it anyway).
