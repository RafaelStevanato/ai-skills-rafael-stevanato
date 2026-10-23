---
name: revenue-centric-design
description: Apply Revenue-Centric Design (134 evidence-backed SaaS principles by @richardrx) when a product must convert, activate, retain or monetize better, including landing pages, onboarding, churn, pricing, checkout, dashboards, positioning, and A/B sample size or LTV/CAC math. Not for gambling, betting or casino products.
license: Source-available (see LICENSE)
metadata:
  author: "Richard (@richardrx), https://x.com/richardrx"
  original-skill: "Helio Costa (@heliocosta-dev), https://github.com/heliocosta-dev/revenue-centric-design"
  evolution: "ft.ia.br (@fabricioctelles), https://github.com/fabricioctelles/skills"
  version: "1.3.0-codex"
  upstream-commit: "1942760c2242f609bf63ce2c97204f5a1791bd68"
  usage-restriction: "No gambling, betting, casino, or real-money games-of-chance use (LICENSE clause 2)"
---

# Revenue-Centric Design

Use the RCD principles of product designer Richard ([@richardrx](https://x.com/richardrx), ex-Volkswagen, PayPal, IBM) so that each design decision serves the user and the business at the same time. The principles come from his posts, translated from Portuguese and reused with his permission.

A recommendation is done when it names the mechanism (decoy effect, Zeigarnik, good-better-best, loss aversion, Schwartz awareness level, and so on), cites the principle by its exact heading, and carries that principle's evidence or source-post link.

The user's explicit instructions take precedence over this skill. The skill text is compact controlled English for precise reading; write deliverables in natural prose for the reader.

## Usage boundary

Do not apply RCD to betting, casino, gambling or other real-money games-of-chance products, including loot-box mechanics. The author granted reuse on that condition ([LICENSE](LICENSE) clause 2). Decline such requests and give that reason.

When the product context is unclear, run `scripts/check_usage_boundary.py [path ...]` from the user's project root. Exit `2` means gambling context was detected; `0` means clean. Do not run it from the skill folder, because this skill's own files trip it. A false positive (for example "bet" as an unrelated codename) can be waived only by the user, who creates `.rcd-boundary-ok` in the project root. Do not create that file yourself. If the user wants the check enforced on every prompt and file edit, read [references/usage-boundary-hooks.md](references/usage-boundary-hooks.md).

## Working method

- If `rcd-log.md` exists in the project root, read it first. Do not re-prescribe a move that failed or one that still waits for results.
- Open only the references that match the question (router below). Scan headings and read the matching entries.
- Compute A/B sample size, churn to LTV, and CAC per closed deal with `scripts/revenue_math.py` (`--help` lists flags). Do not estimate them.
- Shape page, pricing, onboarding or cancellation audits like [references/audit-template.md](references/audit-template.md).
- Append each prescribed move to `rcd-log.md` (format below). Create the file on first use.

```text
revenue_math.py sample-size --baseline 0.03 --mde 0.20
revenue_math.py churn-ltv --arpu 120 --churn 0.25 --new-churn 0.20 --users 1000
revenue_math.py cac --spend 50000 --leads 500 --closes 10
```

## The RCD spine

Apply all nine. Context and sources are in [references/revenue-centric-design.md](references/revenue-centric-design.md).

1. Neutrality is omission: an interface that does not direct hurts conversion.
2. Who talks to everyone convinces no one: without an ICP the value is generic and retains worse.
3. Value first, ask later: proof arrives before the user questions the choice.
4. Your promise is the size of your proof: the market believes what you demonstrate.
5. Same competes on price, different on category: contrast mechanism, narrative or experience, or lose margin.
6. Default is the decision you made for the user: most users never change settings.
7. Retention is built, not requested: show what the user accumulated; perceived loss retains more than promised benefit.
8. Expansion is born of usage: upgrade at the moment of the limit, not through interrupting upsells.
9. Price is a filter: pricing decides who enters, stays and expands.

## Reference router

For a full landing-page audit, start with lp-diagnostic-framework and follow its routing table.

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

Each principle has a **Visual** line that describes the original post's diagram. Open the cited `assets/<id>.jpg` only when that text is not enough.

## Gotchas

- Use scarcity only when it is true (Booking's "1 room left"). Never invent counters, timers or stock levels; fake scarcity is illegal in several markets.
- Framing a real loss is persuasion. Manufacturing fear or trapping cancellation is not: the claim must be true and the exit easy.
- "Kill outbound links" applies to conversion pages only. Keep outbound links on blog posts, docs and SEO pages.
- "4.2 to 4.5 stars" means letting real criticism show. Never fabricate reviews, negative or positive.
- Compute the sample-size floor before proposing tests, then test big levers. Below the floor, decide with qualitative research and do not A/B test the price itself.
- The evidence comes from the author's cases (mostly Brazilian SaaS, values in BRL). Transfer the mechanism, not the exact percentage.
- Keep principle headings unchanged: `rcd-log.md` entries and "Read with" quotes cite them by exact text.
- When an execution skill (for example `cro`, `pricing`, `churn-prevention` or `ab-testing` from coreyhaines31/marketingskills) leads the run, supply RCD principles and evidence inside it instead of duplicating its process. Without those skills, apply RCD directly.

## Project log

Keep `rcd-log.md` in the project root:

```text
## 2026-07-02 — pricing page redesign
- via: rcd (direct)          # or the skill that led the run: cro, pricing, churn-prevention…
- principle: Decoy effect (pricing-and-monetization)
- move: added GBB middle tier at 80% of the top price
- result: pending            # update when data arrives: "+12% upgrades", "no effect"
```

`via:` doubles as trigger telemetry: if RCD often leads runs an execution skill should own, narrow this description to the principle-and-evidence angle.

## License

This skill is source-available, not open source. Ship [LICENSE](LICENSE) in full with any copy or derivative, keep attribution to @richardrx, and keep the gambling prohibition. It derives from heliocosta-dev/revenue-centric-design, extended with gotchas, the audit template, the revenue-math script and the project log; the principle library is synced to upstream `1942760` (134 principles).
