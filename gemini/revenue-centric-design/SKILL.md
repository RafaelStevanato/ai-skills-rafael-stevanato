---
name: revenue-centric-design
description: Applies Revenue-Centric Design, 134 evidence-backed SaaS principles by @richardrx, to diagnose and design for conversion, activation, retention and monetization. Use this skill when the user asks why a landing page, onboarding, pricing page, checkout or dashboard underperforms, how to reduce churn or position a product, or needs A/B sample size, churn-to-LTV or CAC math. Don't use it for gambling, betting or casino products.
license: Source-available (see LICENSE)
metadata:
  author: "Richard (@richardrx), https://x.com/richardrx"
  original-skill: "Helio Costa (@heliocosta-dev), https://github.com/heliocosta-dev/revenue-centric-design"
  evolution: "ft.ia.br (@fabricioctelles), https://github.com/fabricioctelles/skills"
  version: "1.3.0-gemini"
  upstream-commit: "1942760c2242f609bf63ce2c97204f5a1791bd68"
  usage-restriction: "No gambling, betting, casino, or real-money games-of-chance use (LICENSE clause 2)"
---

# Revenue-Centric Design

Make each product and design decision serve the user and the business at the same time, using the RCD principles of product designer Richard ([@richardrx](https://x.com/richardrx), ex-Volkswagen, PayPal, IBM), translated from Portuguese and reused with his permission.

**Done when:** every recommendation names its mechanism (decoy effect, Zeigarnik, good-better-best, loss aversion, Schwartz awareness level, and so on), cites the principle by its exact heading, carries that principle's evidence or source-post link, and is logged in `rcd-log.md`.

The user's explicit instructions take precedence over this skill. The skill text is compact controlled English for precise reading; write deliverables in natural prose for the reader.

## Hard constraints

- **No gambling work.** Do not apply RCD to betting, casino, gambling or other real-money games-of-chance products, including loot-box mechanics. The author granted reuse on that condition ([LICENSE](LICENSE) clause 2). Decline and give that reason.
- **No invented evidence.** Every number in a recommendation comes from a principle's evidence line or from `scripts/revenue_math.py` output. Never fabricate scarcity, counters, timers, stock levels or reviews.

## Step 0: Preflight

1. If `rcd-log.md` exists in the project root, read it. Do not re-prescribe a move that failed or one that still waits for results.
2. When the product context is unclear, run `python scripts/check_usage_boundary.py [path ...]` from the user's project root, never from the skill folder (this skill's own files trip it). Exit `2` means gambling context: stop. Exit `0` means clean. Only the user may waive a false positive, by creating `.rcd-boundary-ok` in the project root; do not create it yourself.
3. Name the question's area so Step 1 opens only the matching references.

## Step 1: Route and read

For a full landing-page audit, start with lp-diagnostic-framework and follow its routing table. Otherwise open only the matching rows, scan headings, and read the matching entries.

| Question about | Read |
|---|---|
| Where the sale breaks before a redesign (LP diagnostic) | [lp-diagnostic-framework](references/lp-diagnostic-framework.md) |
| Landing pages, hero copy, CTAs, social proof, awareness levels, CRO | [conversion-and-landing-pages](references/conversion-and-landing-pages.md) |
| Checkout, forms, payment UX, dropdowns, field friction | [checkout-and-forms](references/checkout-and-forms.md) |
| Dashboards, KPI density, data-viz cognitive load | [dashboards-and-data-viz](references/dashboards-and-data-viz.md), plus [make-the-dashboard-answer-what-do-i-do-now](references/revenue-centric-design.md#make-the-dashboard-answer-what-do-i-do-now) |
| First run, empty states, aha moment, time to value, trials | [onboarding-and-activation](references/onboarding-and-activation.md) |
| Cancellation, retention, expectation debt, NRR, jobs to be done | [churn-and-retention](references/churn-and-retention.md) |
| Pricing tables, decoy and anchoring, GBB, trial with card, upgrades | [pricing-and-monetization](references/pricing-and-monetization.md) |
| Cognitive biases and persuasion mechanisms | [behavioral-science-toolkit](references/behavioral-science-toolkit.md) |
| Feature scope, Swiss Knife Index, adoption, attention hierarchy | [product-strategy-and-features](references/product-strategy-and-features.md) |
| RCD philosophy, design process and method | [revenue-centric-design](references/revenue-centric-design.md) |
| ICP, niche, founder fit, distribution, PLG, first customers | [positioning-icp-and-gtm](references/positioning-icp-and-gtm.md) |
| Differentiation in the AI era, moats, commoditization | [ai-era-differentiation](references/ai-era-differentiation.md) |
| A/B rigor, vanity metrics, churn to LTV, signal quality | [metrics-and-experimentation](references/metrics-and-experimentation.md) |

Each principle has a **Visual** line describing the original post's diagram. Open the cited `assets/<id>.jpg` only when that text is not enough. For an audit that spans several areas (page, pricing, onboarding), delegate one area per subagent and merge their findings.

## Step 2: Diagnose and prescribe

Apply all nine spine principles; context and sources are in [references/revenue-centric-design.md](references/revenue-centric-design.md).

1. Neutrality is omission: an interface that does not direct hurts conversion.
2. Who talks to everyone convinces no one: without an ICP the value is generic and retains worse.
3. Value first, ask later: proof arrives before the user questions the choice.
4. Your promise is the size of your proof: the market believes what you demonstrate.
5. Same competes on price, different on category: contrast mechanism, narrative or experience, or lose margin.
6. Default is the decision you made for the user: most users never change settings.
7. Retention is built, not requested: show what the user accumulated; perceived loss retains more than promised benefit.
8. Expansion is born of usage: upgrade at the moment of the limit, not through interrupting upsells.
9. Price is a filter: pricing decides who enters, stays and expands.

Compute A/B sample size, churn to LTV and CAC per closed deal with `scripts/revenue_math.py`. Treat it as a black box: run `python scripts/revenue_math.py --help` for flags instead of reading its source.

```text
revenue_math.py sample-size --baseline 0.03 --mde 0.20
revenue_math.py churn-ltv --arpu 120 --churn 0.25 --new-churn 0.20 --users 1000
revenue_math.py cac --spend 50000 --leads 500 --closes 10
```

**Verify:** each recommendation has mechanism, exact heading and evidence link; each number traces to an evidence line or a script run you can quote.

## Step 3: Deliver and log

Shape page, pricing, onboarding or cancellation audits like [references/audit-template.md](references/audit-template.md). Append each prescribed move to `rcd-log.md` in the project root, creating the file on first use:

```text
## 2026-07-02 — pricing page redesign
- via: rcd (direct)          # or the skill that led the run: cro, pricing, churn-prevention…
- principle: Decoy effect (pricing-and-monetization)
- move: added GBB middle tier at 80% of the top price
- result: pending            # update when data arrives: "+12% upgrades", "no effect"
```

**Verify:** `rcd-log.md` holds one entry per prescribed move. `via:` doubles as trigger telemetry: if RCD often leads runs an execution skill should own, narrow this description to the principle-and-evidence angle.

## Examples

Request: "Our SaaS pricing page has Starter, Pro and Business copied from a competitor. Pro barely sells."

Recommendation, in the expected shape:

> **Make Pro the obvious middle choice.** Mechanism: decoy effect. Principle: "Make the middle plan the one you actually want to sell" (pricing-and-monetization). Give each plan a job: keep exactly three, make Starter clearly weaker on one attribute that matters (user cap or a key integration), and keep Business as the price anchor. Evidence: in Ariely's test of The Economist's tiers, removing the decoy flipped choices from 16%/84% to 68%/32% and cut combo revenue by more than half ([source](https://x.com/richardrx/status/2059951433827426437)). Transfer the mechanism, not the percentage.

## Constraints & Tips

- **Scarcity only when true** (Booking's "1 room left"). Fake scarcity is illegal in several markets.
- **Real loss framing is persuasion; manufactured fear is not.** The claim must be true and cancellation easy to find.
- **"Kill outbound links" applies to conversion pages only.** Keep outbound links on blog posts, docs and SEO pages.
- **"4.2 to 4.5 stars" means letting real criticism show,** never fabricating reviews, negative or positive.
- **Compute the sample-size floor before proposing tests,** then test big levers. Below the floor, decide with qualitative research and do not A/B test the price itself.
- **Evidence is a benchmark, not a guarantee.** It comes from the author's cases, mostly Brazilian SaaS with values in BRL.
- **Keep principle headings unchanged:** `rcd-log.md` and "Read with" quotes cite them by exact text.
- **Compose with execution skills.** When a skill such as `cro`, `pricing`, `churn-prevention` or `ab-testing` (coreyhaines31/marketingskills) leads the run, supply RCD principles and evidence inside it instead of duplicating its process. Without those skills, apply RCD directly.

## Resources

- [references/audit-template.md](references/audit-template.md): the shape of an audit deliverable (Step 3).
- [references/usage-boundary-hooks.md](references/usage-boundary-hooks.md): read only when the user wants the gambling check enforced automatically through Antigravity hooks.
- `scripts/revenue_math.py`: run it with `--help` for flags. `scripts/check_usage_boundary.py` takes paths or text arguments (Step 0); `scripts/agy_boundary_hook.py` only runs as the hook above.

## License

This skill is source-available, not open source. Ship [LICENSE](LICENSE) in full with any copy or derivative, keep attribution to @richardrx, and keep the gambling prohibition. It derives from heliocosta-dev/revenue-centric-design, extended with gotchas, the audit template, the revenue-math script and the project log; the principle library is synced to upstream `1942760` (134 principles).
