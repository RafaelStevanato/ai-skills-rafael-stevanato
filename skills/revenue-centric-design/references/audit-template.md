# Audit Output Template

Attribution: principles by Richard ([@richardrx](https://x.com/richardrx)). License: [LICENSE](../LICENSE).

Deliver every audit run in this shape: landing page, pricing page, onboarding flow, cancellation flow, features page.
Add a finding row only after it passes the completion criterion ([SKILL.md](../SKILL.md), Workflow step 4).

## Header

Start every audit with this block.

> **Target:** <URL or flow name> · **Date:** <date>
> **ICP:** <buying criteria — trigger, pain, prior attempt, proof needed; not demographics>
> **Awareness level:** <Schwartz stage of the arriving traffic>
> **Verdict:** <one sentence — the single biggest revenue leak found>

- If you cannot state the ICP or awareness level, that **is** finding #1.
- Debug in this order: ICP → awareness → proof → visual. Never start at the visual layer ([detail](conversion-and-landing-pages.md#debug-icp-and-awareness-level-before-touching-design)).

## Findings

Order findings by expected revenue impact, not page position.

| # | Finding | Mechanism | Principle (reference file) | The move | Evidence |
|---|---------|-----------|----------------------------|----------|----------|
| 1 | Hero opens with the product category, not the visitor's pain | 5-second test | "Pass the 5-second test — lead with the problem" (conversion-and-landing-pages) | Rewrite the first line to the pain: "Your team loses 6 hours a week hunting for information" | Descriptive vs transformation-led LPs: 0.5% vs 3% across 30 Brazilian SaaS ([source](https://x.com/richardrx/status/2045154631974539650)) |

When a finding involves numbers (A/B sample size, churn→LTV, CAC per closed deal), paste the actual [`scripts/revenue_math.py`](../scripts/revenue_math.py) output into the Evidence cell. Never write an estimate.

## Close

- **Do first:** list the top 1–3 moves, each with one line on why it outranks the rest.
- **Don't:** list any change the Gotchas in [SKILL.md](../SKILL.md) rule out (fabricated scarcity, LP rules applied to content pages, review manipulation, underpowered tests…).
- Append the prescribed moves to `rcd-log.md` ([SKILL.md](../SKILL.md), Project log). The next engagement starts from what was tried.
