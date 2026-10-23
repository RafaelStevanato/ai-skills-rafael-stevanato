---
name: revenue-centric-design
description: >-
  Revenue-Centric Design (RCD): 134 evidence-backed principles by Richard (@richardrx) to make a SaaS or startup product convert, retain, and monetize. Use for landing pages and CRO (my page is not converting, LP audit, hero, CTA copy, social proof, awareness level), onboarding and activation (users sign up but do not stick, empty state, aha moment, time-to-value, trial conversion), churn and retention (customers keep canceling, cancel flow, NRR, switching cost), pricing and monetization (how should I price this, decoy, anchoring, Good-Better-Best, freemium, trial with card, upgrade), checkout and forms (dropdowns kill conversion, cart abandonment), dashboards (cognitive load, KPI shortlist), positioning, ICP, go-to-market, PLG, feature creep, A/B-test sample size, churn-to-LTV or CAC math, AI-era differentiation, or the behavioral-science mechanism behind a design choice. Also use when another skill needs RCD evidence. Never apply to gambling, betting, or casino products.
license: "Source-available (see LICENSE)"
metadata:
  author: "Richard (@richardrx)"
  author_url: "https://x.com/richardrx"
  author_role: "original content (134 principles)"
  original_skill_author: "Helio Costa (@heliocosta-dev)"
  original_skill_url: "https://github.com/heliocosta-dev/revenue-centric-design"
  original_skill_role: "original skill (extraction, translation, structure)"
  evolution_author: "ft.ia.br (@fabricioctelles)"
  evolution_url: "https://ft.ia.br"
  evolution_role: "evolution (audit template, scripts, hooks, project log, gotchas)"
  repository: "https://github.com/fabricioctelles/skills"
  source: "https://x.com/richardrx"
  version: "1.3.0"
  date: "2026-09-17"
  upstream_commit: "1942760c2242f609bf63ce2c97204f5a1791bd68"
  upstream_changelog: "1.3.0 (134 principles)"
  category: "runbooks"
  license_terms: "Attribution to Richard (@richardrx) with source link; ship LICENSE in full with any copy or derivative; no gambling, betting, or casino use"
  usage_restriction: "No gambling, betting, casino, or real-money games-of-chance use (LICENSE clause 2)"
  consolidated: "2026-10-23 ASD-STE100 rewrite"
  merged-from: "revenue-centric-design"
---

> **⚠️ EXECUTION DIRECTIVE (INPUT vs. OUTPUT SEPARATION):**
> The rules in this skill use strict ASD-STE100 controlled language solely for zero-ambiguity parsing and token efficiency.
> - **NEVER copy this telegraphic or robotic style into human-facing outputs.**
> - Apply 80% ASD-STE100 in final outputs ONLY when explaining dense technical concepts.

# Revenue-Centric Design

- Attribute this material to Richard ([@richardrx](https://x.com/richardrx)) and link the source.
- Know the scope: 134 principles, distilled with the author's permission from the posts of product designer Richard (ex-Volkswagen, PayPal, IBM).
- Know the origin: the posts are translated from Portuguese.
- Link every principle to its source post.
- Name the philosophy **Revenue-Centric Design (RCD)**.
- Serve the user and the business in every design decision.
- Deliver value and revenue together, never one without the other.

## Usage boundary (required)

> 🚫 **Do not apply this skill to betting, casino, gambling, or other real-money games-of-chance
> products** (including loot-box / real-money-gaming mechanics).

- Never apply this skill to betting, casino, gambling, or real-money games-of-chance products.
- Include loot-box and real-money-gaming mechanics in the ban.
- Decline the request when the user asks for such use.
- State that the source author's permission excludes that use.
- Treat the ban as a hard constraint, not a stylistic choice.
- Know the reason: the author granted reuse "on the explicit condition that it never be used for gambling, betting, or casino work" ([LICENSE](LICENSE) clause 2).

### Enforcement and hooks

- Run `scripts/check_usage_boundary.py` on every prompt while this skill is active.
- Run `scripts/check_usage_boundary.py` on every file write/edit while this skill is active.
- Block the operation when the script exits with code 2 (gambling context detected).
- Let only the **user** waive the guard on a false positive (example: "bet" as an unrelated codename).
- Waive the guard only when the user creates `.rcd-boundary-ok` in the project root.
- Never create `.rcd-boundary-ok` on the user's behalf.

Configure these hooks in agents that support automated execution:

| Event | Matcher | Command |
|-------|---------|---------|
| Before processing user prompt | `*` (all) | `python3 <skill_dir>/scripts/check_usage_boundary.py` |
| Before writing/editing a file | `Write\|Edit` | `python3 <skill_dir>/scripts/check_usage_boundary.py` |

- Set `<skill_dir>` to the root directory of this skill.
- Block the operation on exit code `2` (violation detected).
- Proceed on exit code `0` (cleared).
- Require the operator to run the check manually before applying RCD principles in unknown context, when the agent has no hook support.

Claude Code mapping:

- Map "Before processing user prompt" to the `UserPromptSubmit` event.
- Map "Before writing/editing a file" to the `PreToolUse` event with matcher `Write|Edit`.
- Set the command to `python3` plus the absolute installed path, for example `~/.claude/skills/revenue-centric-design/scripts/check_usage_boundary.py`.
- Use `${CLAUDE_PLUGIN_ROOT}/skills/revenue-centric-design/scripts/check_usage_boundary.py` when you ship the skill as a plugin.

Maintainer notes:

- Expect the guard to flag this skill's own files: `SKILL.md`, `LICENSE`, `references/ai-era-differentiation.md` ("slot machine"), `references/metrics-and-experimentation.md` (heading "Don't bet your product..."), `references/pricing-and-monetization.md` ("an expensive bet").
- Edit those files with the `Write|Edit` hook disabled. The maintainer disables the hook, not the agent.
- Keep `scripts/check_usage_boundary.py` and its regex unchanged.
- Never reword the "Don't bet your product..." heading (stable ID).

## Workflow

1. Read `rcd-log.md` first when it exists in the project root.
   - Use the log to see which principles were already applied to this product and what happened.
   - Never re-prescribe a move that the log shows as failed.
   - Never repeat a move that still awaits results.
2. Route with the [Reference router](#reference-router) and open only the matching reference file(s).
   - Scan the headings first.
   - Read only the entries that match the user's situation.
   - Expect this fixed shape per entry: principle (heading), Apply when, Do (the move), Evidence, Visual, Quote, Source.
3. Run `scripts/revenue_math.py` (see `--help`) when the advice involves numbers.
   - Run it for A/B sample size, churn→LTV, and CAC per closed deal.
   - Never estimate these numbers.
4. Mark a recommendation as **done** only when all three conditions are true:
   - (a) It names the mechanism (decoy effect, Zeigarnik, GBB, loss aversion, Schwartz awareness level…).
   - (b) It cites the specific principle.
   - (c) It carries that principle's evidence or source link.
   - Treat a recommendation that misses any of the three as not done.
5. Deliver audit runs (page, pricing, onboarding, cancellation) in the shape of [references/audit-template.md](references/audit-template.md).
6. Close the loop: append what you prescribed to `rcd-log.md` (format in [Project log](#project-log-rcd-logmd)).
   - Create the file on first use.

## Core rules: the RCD spine (9)

- Apply all nine principles to every design decision.
- Load [references/revenue-centric-design.md](references/revenue-centric-design.md) for the principle context (Dieter Rams, Amber Case), Apply when, Quote, and Source.

1. **Neutrality is omission** — an interface that doesn't direct hurts conversion.
2. **Who talks to everyone convinces no one** — no ICP means generic value, which retains worse.
3. **Value first, ask later** — proof must arrive before the user questions their choice.
4. **Your promise is the size of your proof** — the market believes what you demonstrate, not what you claim.
5. **Same competes on price, different on category** — contrast in mechanism, narrative, or experience; no contrast, no margin.
6. **Default is the decision you made for the user** — most never change settings; the initial state defines mass behavior.
7. **Retention is built, not requested** — show what the user accumulated; perceived loss retains more than promised benefit.
8. **Expansion is born of usage** — upsell that interrupts breeds resistance; upgrade at the moment of the limit converts frictionlessly.
9. **Price is a filter** — pricing defines who enters, who stays, who expands; wrong price attracts the wrong ICP.

## Reference router

- Open only the files that match the question.
- Load [lp-diagnostic-framework](references/lp-diagnostic-framework.md) first for a full LP audit. Follow its own routing table for later steps.

| Load when the question is about… | Open |
| --- | --- |
| **LP audit / diagnostic** — where is the sale breaking before redesign | [lp-diagnostic-framework](references/lp-diagnostic-framework.md) |
| Landing pages, hero/copy, CTAs, social proof, awareness levels, CRO | [conversion-and-landing-pages](references/conversion-and-landing-pages.md) |
| Checkout, forms, payment UX, dropdowns, field friction | [checkout-and-forms](references/checkout-and-forms.md) |
| Dashboards, KPI density, data viz cognitive load | [dashboards-and-data-viz](references/dashboards-and-data-viz.md) and [make-the-dashboard-answer-what-do-i-do-now](references/revenue-centric-design.md#make-the-dashboard-answer-what-do-i-do-now) |
| First-run, empty states, aha moment, TTV, activation, trial-as-onboarding | [onboarding-and-activation](references/onboarding-and-activation.md) |
| Cancellation, retention, expectation debt, NRR, jobs-to-be-done, support load | [churn-and-retention](references/churn-and-retention.md) |
| Pricing tables, decoy/anchoring, GBB, trial-with-card, upgrade paths | [pricing-and-monetization](references/pricing-and-monetization.md) |
| Cognitive biases & persuasion tactics (cross-cutting toolkit) | [behavioral-science-toolkit](references/behavioral-science-toolkit.md) |
| Feature scope, Swiss Knife Index, feature adoption, attention hierarchy | [product-strategy-and-features](references/product-strategy-and-features.md) |
| Design philosophy, the RCD principles, design process & method | [revenue-centric-design](references/revenue-centric-design.md) |
| ICP, niche, founder-fit, distribution, PLG, Bullseye, first customers | [positioning-icp-and-gtm](references/positioning-icp-and-gtm.md) |
| Differentiating in the AI era, moats, commoditization | [ai-era-differentiation](references/ai-era-differentiation.md) |
| A/B testing rigor, vanity metrics, churn→LTV math, signal quality | [metrics-and-experimentation](references/metrics-and-experimentation.md) |
| Audit run (page, pricing, onboarding, cancellation): deliverable shape | [audit-template](references/audit-template.md) |

## Visual lines and assets

- Know that some principles carry a **Visual** line.
- Read the Visual line first. It describes in text the diagram or screenshot from the original post.
- Open the cited `../assets/<id>.jpg` file only when the text is insufficient.
- Resolve `../assets/<id>.jpg` from the `references/` folder. From the skill root the path is `assets/<id>.jpg`.
- Follow the principle's **Source** link to see the original post.
- Treat a Visual line without a path as a text description only. No file exists for it.
- Know that `assets/` holds exactly the 44 JPGs that the reference files cite.

## Gotchas

- Use scarcity claims only when the scarcity is real.
  - Example: Booking's "1 room left" works because it's true.
  - Never invent counters, timers, or stock levels.
  - Expect trust loss when users detect fabricated scarcity.
  - Flag fabricated scarcity: it is illegal in several markets.
- Draw the line between loss aversion and a dark pattern at two checks: the claim is true and the exit stays easy.
  - Frame a real loss. This is persuasion.
  - Never manufacture fear.
  - Never trap cancellation.
- Apply "Kill outbound links" on conversion pages only.
  - Keep outbound links on blog posts, docs, and SEO pages.
  - Never export LP rules to content pages.
- Read "4.2–4.5 stars" as: let real criticism show.
  - Never fabricate negative reviews to hit the number.
  - Never fabricate positive reviews to hit the number.
- Never answer with 30 A/B tests. Follow [metrics-and-experimentation](references/metrics-and-experimentation.md) on underpowered tests.
  - Compute the sample-size floor first (`scripts/revenue_math.py sample-size`).
  - Test big levers.
  - Decide by qualitative research when traffic is below the floor.
  - Never A/B test the price itself below the sample-size floor.
  - Run pricing-page experiments only when `scripts/revenue_math.py sample-size` shows the floor is reachable.
- Treat evidence as a benchmark, not a guarantee.
  - Know that the figures come from the author's cases (mostly Brazilian SaaS, values in BRL).
  - Transfer the mechanism.
  - Never promise the exact percentage.
- Keep principle headings unchanged in the reference files. `rcd-log.md` entries and "Read with" quotes cite them by exact text.

## Scripts

### scripts/revenue_math.py

- Run [scripts/revenue_math.py](scripts/revenue_math.py) instead of estimating.
- Run `scripts/revenue_math.py --help` to list the flags.
- Use the subcommand that matches the question:
  - `sample-size`: minimum per-variant n for an A/B test. Never start a test you cannot finish.
  - `churn-ltv`: churn → LTV, plus the cash impact of cutting churn N points.
  - `cac`: CAC per *closed deal*, not per lead.
- Set the flags per subcommand:
  - `sample-size`: `--baseline` (current conversion rate, e.g. 0.03), `--mde` (relative lift to detect, e.g. 0.20 for +20%), `--alpha` (default 0.05), `--power` (default 0.80), `--traffic` (monthly visitors, to estimate test duration).
  - `churn-ltv`: `--arpu` (monthly revenue per user), `--churn` (monthly churn as fraction, e.g. 0.25), `--new-churn` (target churn to compare against), `--users` (current paying users, for cash impact).
  - `cac`: `--spend`, `--leads`, `--closes` (deals actually closed), `--close-rate` (fraction of leads that close, e.g. 0.02).
- Keep `baseline` and `baseline*(1+mde)` within (0, 1).
- Set `--churn` as a fraction between 0 and 1.
- Set `--closes` or a positive `--close-rate` for `cac`.
- Read the `sample-size` verdict: with `--traffic`, a test that needs more than 8 weeks is underpowered.
- Decide by qualitative research when the verdict is underpowered. Five good interviews beat this test.
- Lower CAC per closed deal with a filter on the landing page: specific copy, visible pricing, a qualification question.
- Expect fewer, better leads to lower CAC at the same spend.

Examples:

```
revenue_math.py sample-size --baseline 0.03 --mde 0.20
revenue_math.py churn-ltv --arpu 120 --churn 0.25 --new-churn 0.20 --users 1000
revenue_math.py cac --spend 50000 --leads 500 --closes 10
```

### scripts/check_usage_boundary.py

- Know that [scripts/check_usage_boundary.py](scripts/check_usage_boundary.py) blocks RCD use on gambling/betting/casino products ([LICENSE](LICENSE) clause 2).
- Run it as a hook: the script reads the hook JSON from stdin, scans its text fields, and exits 2 to block.
- Run it as a gate: `check_usage_boundary.py [path ...]` scans project files and any literal text args, and exits 2 on a hit.
- Know the gate scan scope: `README*`, `*.md`, `package.json`, `pyproject.toml`, `composer.json` at the top level.
- Run the gate from the user's project root, never from the skill directory. The skill's own `SKILL.md` and `LICENSE` trigger the guard.
- Read the exit codes: `0` = clean, `2` = gambling context detected (blocks when run as a hook).
- Read the term list in `TERMS` inside the script. It covers EN and PT-BR terms with word boundaries.
- Expect the script to skip the check when `.rcd-boundary-ok` exists in the working directory.

## Related skills

- Treat RCD as the supplier of the **principle and its evidence**. Let execution skills own the workflow.
- Use these skills from [Corey Haines' marketingskills](https://github.com/coreyhaines31/marketingskills) when they are installed:

| Need | Skill |
| --- | --- |
| Full page-audit workflow | `cro` |
| Cancellation-flow build | `churn-prevention` |
| Test design & stats | `ab-testing` |
| Writing the copy | `copywriting` |
| Pricing-page build | `pricing` |
| Post-signup flow build | `onboarding` |

- Apply the RCD principles directly when those skills are not installed. Never defer.
- Cite RCD principles inside the running skill. Never duplicate its process here.
- Use `anti-slop` for UI execution.
- Use `anti-ai-slop-escrita-ptbr` for PT-BR copy.
- Use `web-discoverability` for SEO and content pages, where outbound links stay.

## Project log (rcd-log.md)

- Keep `rcd-log.md` in the project root as per-project memory.
- Read it at the start of every engagement (Workflow step 1).
- Append to it at the end of every engagement (Workflow step 6).
- Write one entry per engagement.
- Create the file on first use.
- Set `via:` to `rcd (direct)`, or to the skill that led the run: cro, pricing, churn-prevention…
- Set `result:` to `pending` until data arrives. Update it when data arrives: "+12% upgrades", "no effect".
- Use this entry format:

```
## 2026-07-02 — pricing page redesign
- via: rcd (direct)          # or the skill that led the run: cro, pricing, churn-prevention…
- principle: Decoy effect (pricing-and-monetization)
- move: added GBB middle tier at 80% of the top price
- result: pending            # update when data arrives: "+12% upgrades", "no effect"
```

- Use the `via:` field as trigger telemetry.
- Narrow this skill's description to the principle/evidence angle when entries accumulate where RCD led a run that an execution skill should own (a full page audit, a cancellation build).

## License

- Know that this skill is source-available, **not** open-source.
- Ship [LICENSE](LICENSE) in full with any copy or derivative.
- Keep attribution to @richardrx.
- Never use this skill for gambling, betting, or casino work.
- Know the lineage: this skill is a derivative of [heliocosta-dev/revenue-centric-design](https://github.com/heliocosta-dev/revenue-centric-design).
- Know the changes made here: restructured and extended (gotchas, audit template, revenue-math script, project log).
- Know the sync state: principle library synced to upstream `1942760` (CHANGELOG 1.3.0 / 134 principles). See `metadata.upstream_commit` for the full hash.
