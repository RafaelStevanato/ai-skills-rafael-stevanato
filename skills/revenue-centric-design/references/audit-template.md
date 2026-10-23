# Audit Output Template

Attribution: principles by Richard ([@richardrx](https://x.com/richardrx)). License terms: see [LICENSE](../LICENSE).

- Deliver every audit run in this shape.
- Apply this shape to a landing page, pricing page, onboarding flow, cancellation flow, or features page.
- Obey the Usage boundary section of [SKILL.md](../SKILL.md) before every audit.
- Add a row to the Findings table only after the row passes the completion criterion.
- Find the completion criterion in [SKILL.md](../SKILL.md), Workflow step 4: named mechanism, cited principle, attached evidence or source.

## Header

Start every audit with this block. Fill all 4 fields.

> **Target:** <URL or flow name> · **Date:** <date>
> **ICP:** <buying criteria — trigger, pain, prior attempt, proof needed; not demographics>
> **Awareness level:** <Schwartz stage of the arriving traffic>
> **Verdict:** <one sentence — the single biggest revenue leak found>

- If you cannot state the ICP or the awareness level, that **is** finding #1.
- Start the debug order at the ICP: ICP → awareness → proof → visual.
- Never start at the visual layer.
- Before any design change, apply [Debug ICP and awareness level before touching design](conversion-and-landing-pages.md#debug-icp-and-awareness-level-before-touching-design).

## Findings

- Order the findings by expected revenue impact.
- Never order the findings by position on the page.
- Use the 6-column table below.
- Copy the shape of row 1 (worked example) for every finding.

| # | Finding | Mechanism | Principle (reference file) | The move | Evidence |
|---|---------|-----------|----------------------------|----------|----------|
| 1 | Hero opens with the product category, not the visitor's pain | 5-second test | "Pass the 5-second test — lead with the problem" (conversion-and-landing-pages) | Rewrite the first line to the pain: "Your team loses 6 hours a week hunting for information" | Descriptive vs transformation-led LPs: 0.5% vs 3% across 30 Brazilian SaaS ([source](https://x.com/richardrx/status/2045154631974539650)) |

- When a finding involves numbers (A/B sample size, churn→LTV, CAC per closed deal), paste the actual [`scripts/revenue_math.py`](../scripts/revenue_math.py) output into the Evidence cell.
- Never write an estimate in the Evidence cell.

## Close

- **Do first:** list the top 1–3 moves. Write one line per move on why it outranks the rest.
- **Don't:** list any tempting change that the Gotchas in [SKILL.md](../SKILL.md) rule out (fabricated scarcity, LP rules applied to content pages, review manipulation, underpowered tests…).
- Append the prescribed moves to the project's `rcd-log.md`. Use the format in [SKILL.md](../SKILL.md), Project log (Workflow step 6).
