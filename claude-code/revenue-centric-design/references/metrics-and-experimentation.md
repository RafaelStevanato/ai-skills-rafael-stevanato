# Metrics, Experimentation & Business Math

Attribution: Richard ([@richardrx](https://x.com/richardrx)), "Richard — Design for startups", translated from Portuguese. License: [LICENSE](../LICENSE).

## Duolingo's lesson: optimize the metric that moves DAU, not the borrowed mechanic

Duolingo copied game mechanics twice and failed both: a Gardenscapes moves-counter (neutral) and an Uber-style referral program (+3%, because the reward excluded the best users). It then modeled which number to move: bucketing users by engagement and simulating +2%/quarter for 3 years. CURR (current-user retention rate) had ~5x the impact of the next-best metric. Gamification then worked: CURR +21% over 4 years, daily churn of best users −40%+, DAU ×4.5. Leaderboards alone gave +17% total learning time and tripled highly-engaged learners, after the switch to competing with users of *similar prior-week engagement* (auto opt-in = default effect, no extra tasks).

**Apply when:** You add gamification by copying a mechanic instead of finding your CURR.

**Do:**
- Find the single retention metric that compounds your DAU before you choose mechanics.
- Treat PBL (points, badges, leaderboards) as the free sample. ~290 mechanics exist.
- Use three first: competition (defined start/middle/end missions); progress bars as trajectory achievement, beyond onboarding; engagement-unlocked content (a forecast panel opens only after 30 real entries, blocked as a ladder, not a paywall).

**Visual:** Duolingo's DAU curve, mid-2018 to mid-2022, marked "Started working on CURR" at the inflection, with a 4.5× arrow to the top right — `../assets/2081714430811730162__1.jpg`

**Source:** [@richardrx · 2026-07-27](https://x.com/richardrx/status/2081714430811730162)

## Don't mistake signups for traction

Signups are the cheapest user action: they measure curiosity, not value, especially in freemium. Real growth is people who return and take the value-delivering action.

**Apply when:** A rising signup curve feels like proof of traction, especially in freemium.

**Do:**
- Treat signups as top-of-funnel only.
- Track day 2 and day 7 returns (D1/D7 retention) and completion of the value-delivering action (activation).
- Expect paid media to inflate signups while real retention stays flat.

**Quote:** "The signup curve climbs with paid traffic, but usage and activation only climb with a good product."

**Source:** [@richardrx · 2026-06-11](https://x.com/richardrx/status/2065082771987394651)

## Don't bet your product on an underpowered A/B test

Testing without enough sample is the trap: most small-SaaS A/B tests lack the volume to prove anything, yet founders swap the whole product on the result.

**Apply when:** In traction or survival stage, a one-week test shows "variant B won by 12%," and you want to ship it everywhere.

**Do:**
- Compute the minimum sample size first with `revenue_math.py sample-size`. If you cannot hit that floor in reasonable time (the script reports "underpowered" above 8 weeks), do not start.
- Test big things (headline, offer, pricing structure, onboarding): large effects need less sample.
- Never stop a test because the number looked pretty mid-way.
- With no volume, decide by qualitative research: five good interviews beat an underpowered A/B test.
- Beware the law of small numbers and confirmation bias.

**Evidence:** ProfitWell: never A/B test price. You will never have the volume or context for the result to mean anything.

**Source:** [@richardrx · 2026-06-01](https://x.com/richardrx/status/2061463480868229189)

## Celebrate signal quality, not list size

A waitlist validates that a pain is one people pay to solve; it does not exist to sell. Absolute size is a vanity metric; conversion-weighted quality is the real signal.

**Apply when:** You launch a waitlist and want to celebrate raw headcount.

**Do:**
- Convert size to expected customers first: a good waitlist converts 15–20% to paying; above 30% is excellent.
- 53 people at 20% = 10 customers; 1,000 people at 1% = 10 customers. Same result, different perception.
- Treat the hypothesis as unvalidated until a transaction exists.

**Quote:** "Founders celebrate the size of the list when they should celebrate the quality of the signal."

**Source:** [@richardrx · 2026-04-17](https://x.com/richardrx/status/2045094511106220220)

## Translate churn points into LTV, not percentages

Most people watch churn %, but few compute what each point costs in accumulated LTV over 12 months. Cutting churn is a cash lever that needs no price hike and no new acquisition.

**Apply when:** You treat a churn percentage as a vanity number instead of money.

**Do:**
- Do the churn→LTV math with `revenue_math.py churn-ltv`. Its yearly figure (12-month ramp) differs from the R$72,000 below.
- At 25% monthly churn on 1,000 users, you must add 250 new users/month just to break even; kill paid traffic and the product dies in ~4 months.
- Then improve retention without Figma:
  1. Define the Aha Moment.
  2. Measure time-to-value (TTV) from signup to it.
  3. Ask "how do I deliver this faster?"
  4. If you cannot, break the path into micro-wins.
  5. Test, measure, repeat.

**Evidence:** Finance SaaS, ARPU R$120: cutting churn 5 points (25%→20%) is +R$72,000/year in cash.

**Source:** [@richardrx · 2026-04-06](https://x.com/richardrx/status/2041184077106004289)

## Nine product metrics, each telling one thing

Metrics are like a blood panel: one bad reading is critical, but all-good is real health. The bundle is the business's health check.

**Apply when:** A founder fixates on one number or conflates what each metric diagnoses.

**Do:**
- Read each metric as a diagnostic for one layer:
  - ARR = size (not necessarily health).
  - Burn rate = risk (time until death).
  - CAC = efficiency (obsessing over lowering it can worsen conversion with a less-qualified cohort).
  - DAU/MAU = engagement (<20% = bad sign).
  - LTV = product (does the customer see value?).
  - Churn = fit (user doesn't understand or see value → cancels).
  - NRR = real growth (>100% = good).
  - Gross margin = model (<70% in SaaS = problem, except AI wrappers).
  - Runway = survival (<12 months = danger).
- Treat one bad result as a specific warning. Read the full panel before you prescribe a fix: ARR alone cannot prove health, low CAC can hide a weak cohort, and strong growth without margin or runway can be fatal.

**Source:** [@richardrx · 2026-01-12](https://x.com/richardrx/status/2010675817483817384)
