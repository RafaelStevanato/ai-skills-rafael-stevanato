# Metrics, Experimentation & Business Math

Attribution: Richard (@richardrx), "Richard — Design for startups", translated from Portuguese.
Each entry links to its source post.
Return to [SKILL.md](../SKILL.md).
Related files: [churn-and-retention.md](churn-and-retention.md), [onboarding-and-activation.md](onboarding-and-activation.md), [pricing-and-monetization.md](pricing-and-monetization.md), [dashboards-and-data-viz.md](dashboards-and-data-viz.md).
Run the math with [scripts/revenue_math.py](../scripts/revenue_math.py). Do not estimate.

## Duolingo's lesson: optimize the metric that moves DAU, not the borrowed mechanic

**Principle:**
- Duolingo copied game mechanics twice and failed both times.
- Failure 1: a Gardenscapes moves-counter had a neutral effect.
- Failure 2: a referral program copied from Uber gave +3%, because the reward excluded the best users.
- Duolingo then stopped picking mechanics and modeled which number to move.
- Duolingo bucketed users by engagement.
- Duolingo simulated +2%/quarter for 3 years.
- Result: CURR (current-user retention rate) had ~5x the impact of the next-best metric.
- After that, gamification worked.
- CURR: +21% over 4 years.
- Daily churn of best users: −40%+.
- DAU: ×4.5.
- Leaderboards alone: +17% total learning time.
- Leaderboards alone: tripled highly-engaged learners.
- Cause: Duolingo switched to competing with users of *similar prior-week engagement*.
- Auto opt-in = default effect, with no extra tasks.

**Apply when:**
- You add gamification by copying a mechanic instead of finding your CURR.

**Do:**
- Find the single retention metric that compounds your DAU before you choose mechanics.
- Treat PBL (points, badges, leaderboards) as the free sample.
- Know that there are ~290 gamification mechanics.
- Use these three mechanics first.
- Mechanic 1, competition: use defined start/middle/end missions.
- Mechanic 2, progress bars as trajectory achievement: use them beyond onboarding.
- Mechanic 3, engagement-unlocked content: a forecast panel opens only after 30 real entries.
- Block engagement-unlocked content as a ladder, not a paywall.

**Visual:** Duolingo's DAU curve from mid-2018 to mid-2022, marked "Started working on CURR" at the inflection, with a 4.5× arrow from there to the top right — `../assets/2081714430811730162__1.jpg`

**Source:** [@richardrx · 2026-07-27](https://x.com/richardrx/status/2081714430811730162)

## Don't mistake signups for traction

**Principle:**
- Signups are the cheapest action a user takes.
- Signups measure curiosity, not value, especially in freemium.
- Real growth is whether people come back and do the action that delivers value.

**Apply when:**
- A rising signup curve on the dashboard feels like proof of traction, particularly under a freemium model.

**Do:**
- Treat signups as top-of-funnel only.
- Never stop reading the funnel at signups.
- Track who returns on day 2 and day 7 (D1/D7 retention).
- Track how many users complete the value-delivering action (activation).
- Expect paid media to inflate signups while real retention stays flat.

**Quote:** "The signup curve climbs with paid traffic, but usage and activation only climb with a good product."

**Source:** [@richardrx · 2026-06-11](https://x.com/richardrx/status/2065082771987394651)

## Don't bet your product on an underpowered A/B test

**Principle:**
- Most A/B tests in small SaaS lack the volume to prove anything.
- Founders still swap the whole product on the result.
- Testing without enough sample to conclude is the trap.

**Apply when:**
- You are in traction or survival stage.
- You ran a test for a week, saw "variant B won by 12%," and want to ship it everywhere.

**Do:**
- Compute the minimum sample size before you run the test.
- Compute it with [scripts/revenue_math.py](../scripts/revenue_math.py) (`sample-size`). Free calculators also exist.
- Do not start the test if you cannot hit that floor in reasonable time.
- Test big things: headline, offer, pricing structure, onboarding.
- Test big things because large effects need less sample.
- Never stop a test because the number looked pretty mid-way.
- With no volume, decide by qualitative research.
- Know that five good interviews beat an underpowered A/B test.
- Beware the law of small numbers and confirmation bias.

**Script usage:**
- Run this command (from the script docstring): `revenue_math.py sample-size --baseline 0.03 --mde 0.20`
- Add `--traffic <monthly visitors>` to get the weeks needed to conclude.
- Read the script verdict: the script reports "underpowered" when the test needs more than 8 weeks.
- When the verdict is "underpowered", decide by qualitative research instead.

**Evidence:**
- ProfitWell is categorical: do not A/B test price.
- ProfitWell: you will never have the volume or context for the result to mean anything.

**Source:** [@richardrx · 2026-06-01](https://x.com/richardrx/status/2061463480868229189)

## Celebrate signal quality, not list size

**Principle:**
- A waitlist exists to validate that a pain is one people pay to solve.
- A waitlist does not exist to sell.
- Absolute size is a vanity metric.
- Conversion-weighted quality is the real signal.

**Apply when:**
- You launch a waitlist and feel tempted to celebrate raw headcount.

**Do:**
- Convert size to expected customers before you react.
- Benchmark: a good waitlist converts 15–20% to paying.
- Benchmark: above 30% is excellent.
- Example: 53 people at 20% = 10 customers.
- Example: 1,000 people at 1% = 10 customers.
- Know that both examples give the same result with a different perception.
- Treat the hypothesis as unvalidated until a transaction exists.

**Quote:** "Founders celebrate the size of the list when they should celebrate the quality of the signal."

**Source:** [@richardrx · 2026-04-17](https://x.com/richardrx/status/2045094511106220220)

## Translate churn points into LTV, not percentages

**Principle:**
- Most people watch churn %.
- Few people compute what each point costs in accumulated LTV over 12 months.
- Cutting churn is a cash lever.
- Cutting churn needs no price hike and no new acquisition.

**Apply when:**
- You stare at a churn percentage and treat it as a vanity number instead of money.

**Do:**
- Do the churn→LTV math.
- Example: at 25% monthly churn on 1,000 users, you must add 250 new users/month just to break even.
- Example: kill paid traffic and the product dies in ~4 months.
- Then improve retention without Figma.
- Step 1: define the Aha Moment.
- Step 2: measure time-to-value (TTV) from signup to the Aha Moment.
- Step 3: ask "how do I deliver this faster?"
- Step 4: break the path into micro-wins if you cannot deliver it faster.
- Step 5: test, measure, repeat.

**Script usage:**
- Compute LTV and the cash impact with [scripts/revenue_math.py](../scripts/revenue_math.py) (`churn-ltv`).
- Run this command (from the script docstring): `revenue_math.py churn-ltv --arpu 120 --churn 0.25 --new-churn 0.20 --users 1000`
- Expect the script yearly figure to differ from the R$72,000 evidence below.
- The script counts retained revenue over a 12-month ramp.

**Evidence:**
- Finance SaaS, ARPU R$120: cutting churn 5 points (25%→20%) is +R$72,000/year in cash.
- No price change.
- No extra acquisition.

**Source:** [@richardrx · 2026-04-06](https://x.com/richardrx/status/2041184077106004289)

## Nine product metrics, each telling one thing

**Principle:**
- Read each metric as a diagnostic for one layer of the business.

| Metric | Tells you | Threshold or caveat |
|---|---|---|
| ARR | Size | Not necessarily health. |
| Burn rate | Risk | Time until death. |
| CAC | Efficiency | Obsessing over lowering it can worsen conversion with a less-qualified cohort. |
| DAU/MAU | Engagement | <20% = bad sign. |
| LTV | Product | Does the customer see value? |
| Churn | Fit | User doesn't understand or see value → cancels. |
| NRR | Real growth | >100% = good. |
| Gross margin | Model | <70% in SaaS = problem, except AI wrappers. |
| Runway | Survival | <12 months = danger. |

- Read metrics like a blood panel.
- One bad reading is critical.
- All-good readings mean real health.

**Apply when:**
- A founder fixates on one number.
- A founder conflates what each metric diagnoses.

**Do:**
- Use each metric as a diagnostic for its matching layer.
- Read the full panel before you prescribe a fix.
- Never use ARR alone to prove health.
- Check for a weak cohort when CAC is low.
- Check margin and runway when growth is strong. Strong growth without margin or runway can still be fatal.
- Treat one bad result as a specific warning.
- Treat the bundle of nine as the business's health check.

**Source:** [@richardrx · 2026-01-12](https://x.com/richardrx/status/2010675817483817384)
