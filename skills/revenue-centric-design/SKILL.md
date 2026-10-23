---
name: revenue-centric-design
description: >-
  Revenue-Centric Design (RCD): 134 evidence-backed principles by Richard (@richardrx) to make a SaaS or startup product convert, retain, and monetize. Use for a landing page or CRO ("my page isn't converting"), onboarding/activation ("users sign up but don't stick"), churn/retention ("customers keep canceling"), pricing/monetization ("how should I price this"), checkout/forms ("dropdowns kill conversion", "annotated checkout"), dashboards/data viz ("cognitive load", "KPI shortlists"), positioning, ICP, go-to-market, feature scope, A/B-test sample size, churn-to-LTV or CAC math, AI-era differentiation, or the behavioral-science mechanism behind a design choice. Also use when another skill needs RCD evidence. Never apply to gambling, betting, or casino products.
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
  version: "1.3.0"
  date: "2026-09-17"
  upstream_commit: "1942760c2242f609bf63ce2c97204f5a1791bd68"
  category: "runbooks"
  usage_restriction: "No gambling, betting, casino, or real-money games-of-chance use (LICENSE clause 2)"
  consolidated: "2026-10-23 ASD-STE100 rewrite"
  merged-from: "revenue-centric-design"
---

> **⚠️ EXECUTION DIRECTIVE (INPUT vs. OUTPUT SEPARATION):**
> The rules in this skill use strict ASD-STE100 controlled language solely for zero-ambiguity parsing and token efficiency.
> - **NEVER copy this telegraphic or robotic style into human-facing outputs.**
> - Apply 80% ASD-STE100 in final outputs ONLY when explaining dense technical concepts.

# Revenue-Centric Design

Attribute this material to Richard ([@richardrx](https://x.com/richardrx)) and link the source. It holds 134 principles, distilled with the author's permission from the posts of product designer Richard (ex-Volkswagen, PayPal, IBM), translated from Portuguese. Link every principle to its source post.

Follow **Revenue-Centric Design (RCD)**: serve the user and the business in every design decision, never one alone.

## Usage boundary (required)

> 🚫 **Do not apply this skill to betting, casino, gambling, or other real-money games-of-chance
> products** (including loot-box / real-money-gaming mechanics).

Decline such requests: the source author's permission excludes that use. The ban is a hard constraint. The author granted reuse "on the explicit condition that it never be used for gambling, betting, or casino work" ([LICENSE](LICENSE) clause 2).

### Enforcement and hooks

- Run `scripts/check_usage_boundary.py` on every prompt and every file write/edit while this skill is active. Block the operation on exit code `2` (gambling context detected); proceed on `0`.
- Without hook support, run the check manually before applying RCD in unknown context.
- Let only the **user** waive the guard on a false positive (example: "bet" as an unrelated codename): the user creates `.rcd-boundary-ok` in the project root. Never create it on the user's behalf.

Configure these hooks (`<skill_dir>` = skill root):

| Event | Matcher | Command |
|-------|---------|---------|
| Before processing user prompt | `*` (all) | `python3 <skill_dir>/scripts/check_usage_boundary.py` |
| Before writing/editing a file | `Write\|Edit` | `python3 <skill_dir>/scripts/check_usage_boundary.py` |

Claude Code: row 1 = `UserPromptSubmit`, row 2 = `PreToolUse`. `<skill_dir>` = `~/.claude/skills/revenue-centric-design` (plugin: `${CLAUDE_PLUGIN_ROOT}/skills/revenue-centric-design`).

## Workflow

1. Read `rcd-log.md` first when it exists in the project root. Never re-prescribe a failed move or repeat one that awaits results.
2. Route with the [Reference router](#reference-router). Scan the headings and read only the matching entries.
3. Run `scripts/revenue_math.py` for A/B sample size, churn→LTV, and CAC per closed deal. Never estimate them.
4. Mark a recommendation **done** only when it (a) names the mechanism (decoy effect, Zeigarnik, GBB, loss aversion, Schwartz awareness level…), (b) cites the specific principle, and (c) carries that principle's evidence or source link.
5. Deliver audit runs (page, pricing, onboarding, cancellation) in the shape of [references/audit-template.md](references/audit-template.md).
6. Append what you prescribed to `rcd-log.md` ([Project log](#project-log-rcd-logmd)). Create the file on first use.

## Core rules: the RCD spine (9)

Apply all nine. Context and sources: [references/revenue-centric-design.md](references/revenue-centric-design.md).

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

For a full LP audit, load lp-diagnostic-framework first and follow its routing table.

Load when the question is about… | Open
--- | ---
**LP audit / diagnostic** — where the sale breaks before redesign | [lp-diagnostic-framework](references/lp-diagnostic-framework.md)
Landing pages, hero/copy, CTAs, social proof, awareness levels, CRO | [conversion-and-landing-pages](references/conversion-and-landing-pages.md)
Checkout, forms, payment UX, dropdowns, field friction | [checkout-and-forms](references/checkout-and-forms.md)
Dashboards, KPI density, data viz cognitive load | [dashboards-and-data-viz](references/dashboards-and-data-viz.md) and [make-the-dashboard-answer-what-do-i-do-now](references/revenue-centric-design.md#make-the-dashboard-answer-what-do-i-do-now)
First-run, empty states, aha moment, TTV, activation, trial-as-onboarding | [onboarding-and-activation](references/onboarding-and-activation.md)
Cancellation, retention, expectation debt, NRR, jobs-to-be-done, support load | [churn-and-retention](references/churn-and-retention.md)
Pricing tables, decoy/anchoring, GBB, trial-with-card, upgrade paths | [pricing-and-monetization](references/pricing-and-monetization.md)
Cognitive biases and persuasion tactics (cross-cutting) | [behavioral-science-toolkit](references/behavioral-science-toolkit.md)
Feature scope, Swiss Knife Index, feature adoption, attention hierarchy | [product-strategy-and-features](references/product-strategy-and-features.md)
Design philosophy, the RCD principles, design process and method | [revenue-centric-design](references/revenue-centric-design.md)
ICP, niche, founder-fit, distribution, PLG, Bullseye, first customers | [positioning-icp-and-gtm](references/positioning-icp-and-gtm.md)
Differentiating in the AI era, moats, commoditization | [ai-era-differentiation](references/ai-era-differentiation.md)
A/B testing rigor, vanity metrics, churn→LTV math, signal quality | [metrics-and-experimentation](references/metrics-and-experimentation.md)
Audit run: deliverable shape | [audit-template](references/audit-template.md)
A/B sample size, churn→LTV, CAC per closed deal | [revenue_math.py](scripts/revenue_math.py)
Usage-boundary guard: hook or gate | [check_usage_boundary.py](scripts/check_usage_boundary.py)

Read a principle's **Visual** line first: it describes the original post's diagram. Open the cited `../assets/<id>.jpg` (skill root: `assets/<id>.jpg`) only if the text is insufficient.

## Gotchas

- Use scarcity claims only when true (Booking's "1 room left"). Never invent counters, timers, or stock levels. Fake scarcity is illegal in several markets.
- Frame a real loss: that is persuasion. Never manufacture fear or trap cancellation. The claim must be true and the exit easy.
- Apply "Kill outbound links" on conversion pages only. Keep outbound links on blog posts, docs, and SEO pages.
- Read "4.2–4.5 stars" as: let real criticism show. Never fabricate reviews, negative or positive, to hit the number.
- Never answer with 30 A/B tests. Compute the sample-size floor first (`scripts/revenue_math.py sample-size`) and test big levers. Below the floor, decide by qualitative research. Never A/B test the price itself below the floor. Run pricing-page experiments only above it.
- Treat evidence as a benchmark, not a guarantee. The figures come from the author's cases (mostly Brazilian SaaS, values in BRL). Transfer the mechanism, not the exact percentage.
- Never rename a principle heading: `rcd-log.md` and "Read with" quotes cite headings by exact text.

## Scripts

`scripts/revenue_math.py --help` lists the flags.

- `sample-size`: minimum per-variant n for an A/B test.
- `churn-ltv`: churn → LTV, plus the cash impact of cutting churn N points.
- `cac`: CAC per *closed deal*, not per lead.

```
revenue_math.py sample-size --baseline 0.03 --mde 0.20
revenue_math.py churn-ltv --arpu 120 --churn 0.25 --new-churn 0.20 --users 1000
revenue_math.py cac --spend 50000 --leads 500 --closes 10
```

Gate mode: run `check_usage_boundary.py [path ...]` from the user's project root. It scans the paths, text args, or the top-level `README*`, `*.md`, `package.json`, `pyproject.toml`, `composer.json`. Never run the gate from the skill directory: this skill's own `SKILL.md` and `LICENSE` trigger the guard. A `.rcd-boundary-ok` file skips the check.

## Related skills

RCD supplies the **principle and its evidence**; execution skills own the workflow. Cite RCD principles inside them; never duplicate their process.

From [Corey Haines' marketingskills](https://github.com/coreyhaines31/marketingskills): full page-audit workflow → `cro` · cancellation-flow build → `churn-prevention` · test design & stats → `ab-testing` · writing the copy → `copywriting` · pricing-page build → `pricing` · post-signup flow build → `onboarding`. Apply the RCD principles directly when they are not installed. Never defer.

## Project log (rcd-log.md)

Keep `rcd-log.md` in the project root. Entry format:

```
## 2026-07-02 — pricing page redesign
- via: rcd (direct)          # or the skill that led the run: cro, pricing, churn-prevention…
- principle: Decoy effect (pricing-and-monetization)
- move: added GBB middle tier at 80% of the top price
- result: pending            # update when data arrives: "+12% upgrades", "no effect"
```

Use `via:` as trigger telemetry. When RCD often leads a run that an execution skill should own (a full page audit, a cancellation build), narrow this description to the principle/evidence angle.

## License

This skill is source-available, **not** open-source. Ship [LICENSE](LICENSE) in full with any copy or derivative. Keep attribution to @richardrx; gambling, betting, and casino use is prohibited. It derives from [heliocosta-dev/revenue-centric-design](https://github.com/heliocosta-dev/revenue-centric-design), restructured and extended (gotchas, audit template, revenue-math script, project log). The principle library is synced to upstream `1942760` (CHANGELOG 1.3.0 / 134 principles). See `metadata.upstream_commit` for the full hash.
