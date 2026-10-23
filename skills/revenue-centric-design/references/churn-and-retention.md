# Churn & Retention

Attribution: Richard (@richardrx), "Richard — Design for startups", translated from Portuguese.
Each entry links to its source post.
Return to [SKILL.md](../SKILL.md).
Related files: [onboarding-and-activation.md](onboarding-and-activation.md), [metrics-and-experimentation.md](metrics-and-experimentation.md).

## The funnel leaks at three points — diagnose which before fixing

**Principle:**
- Diagnose which of the three most common SaaS funnel holes leaks before you fix anything.
- The three holes are the most common ones for Brazilian founders.
- Hole 1: users cancel in month 1–2.
- Hole 1 cause: onboarding is missing, or the LP promised the wrong thing and brought off-ICP users.
- Fix missing onboarding as a product problem: shorten the path to value.
- Fix the wrong LP promise as a marketing problem: tighten the promise.
- Hole 2: many trials, few paid.
- Hole 2 cause: the paywall sits at the wrong moment, or the value ladder is broken.
- Hole 3: many visits, few signups.
- Hole 3 cause: confused ICP, generic value proposition, or both.
- Check the acquisition source first for hole 3. Copy cannot save wrong traffic.

**Apply when:**
- Triage where the funnel is leaking.

**Do:**
- Match the symptom to the owner.
- Month-1 churn: fix activation and expectation.
- Trial but no conversion: fix paywall timing and value ladder.
- Visit but no signup: fix ICP, positioning and traffic source.
- Expect the three causes to mix.
- Build a clear ICP and a good offer first.
- Then build an experience aligned to the promise.

**Evidence:**
- Kyle Poyar/ChartMogul+ProductLed (Jan): median free-to-paid 8%; trial-without-card good 4–6%, great 10–15%; trial-with-card good 25–35% (US).

**Source:** [@richardrx · 2026-08-05](https://x.com/richardrx/status/2085056354360729949)

## Churn and payback are one problem, measured in two places

**Principle:**
- Treat churn and payback as one problem. They look like two problems, often with different owners.
- Know that the user's first session decides both.
- The decision happens in the gap between entering and feeling that the product works.

**Apply when:**
- You fix churn at the cancel screen and chase cheaper CAC in the ad manager at the same time.

**Do:**
- Never fix churn at the cancel screen alone. The decision happened earlier.
- Never chase cheaper CAC in the ad manager alone. The decision happened earlier.
- Fix activation to fix both.
- Shrink TTV to retain more users.
- Shrink TTV to get each customer across the payback line before they vanish.
- Know this case: a customer who dies in month 2 with a 4-month payback never closes the account.
- Check for churn that is not activation churn: price, a bad channel.
- Count how many customers die before they repay what they cost.
- Run that count before you chase cheaper CAC.

**Quote:** "A customer who dies before repaying his CAC is a bill you paid and never collected."

**Source:** [@richardrx · 2026-06-30](https://x.com/richardrx/status/2071931705573748896)

## Switching cost is what turns months of LTV into years

**Principle:**
- Know that the same product, designed differently, yields months or years of LTV.
- Define switching cost: the effort a user *perceives* in leaving.
- Know that low switching cost means thin history and an easy exit.

**Apply when:**
- You design for retention or lock-in.
- You explain why a useful product still churns.

**Do:**
- Engineer switching cost deliberately.
- Treat switching cost as a "compound interest" that grows the product's value over time.
- Use five levers.
- Lever 1: **muscle memory** (Superhuman/Photoshop shortcuts).
- Lever 2: **mental model** (Mac↔Windows, Gmail labels).
- Lever 3: **accumulated personalization** (Spotify playlists, home-screen layout).
- Lever 4: the **vault effect** (iCloud/Drive/years of WhatsApp).
- Lever 5: **autopilot/habit** (variable-reward Skinner-box loops).
- Know that sunk cost holds users the way it holds an investor in a falling stock.
- Install habit on purpose. Habit can take months to install.
- Know that habit is the difference between LTV of months and LTV of years.

**Source:** [@richardrx · 2026-06-23](https://x.com/richardrx/status/2069382946214080985)

## Tell the existing base about upgrades before they want to leave

**Principle:**
- Know that reactive improvement communication is a sneaky churn vector.
- Failure pattern: you market new versions only to cold traffic, to avoid cannibalizing the old product.
- Result: your base assumes the old version is the ceiling.
- Result: your base leaves when a competitor looks better.

**Apply when:**
- You shipped a better version or feature but announced it only externally.
- Support pitches the migration only at the cancel moment.

**Do:**
- Offer upgrades and migrations proactively to active users.
- Never rely on release emails nobody reads.
- Never rely on an Instagram post.
- Ask: "When we shipped the last relevant feature or version, how many active customers were told?"
- Never wait for the cancel moment to offer migration.
- Know that offering migration at cancellation converts a clean expansion into emergency retention.
- Track Net Revenue Retention (NRR).
- Use NRR above 110% in B2B SaaS to separate sustainable growth from a leaky funnel.

**Quote:** "The migration only showed up as a reaction to my complaint, after I started making noise."

**Source:** [@richardrx · 2026-05-19](https://x.com/richardrx/status/2056715097796411514)

## Design the cancel screen — it's your last conversation, not a form

**Principle:**
- Know that the cancellation screen is the most ignored page in the product.
- Know that it is also one of the most important pages.
- Never treat it as a bureaucratic form. A form wastes your final chance to retain.

**Apply when:**
- The cancel flow is only "Are you sure?" with two buttons.
- The cancel flow is Stripe's default template, while signup was crafted with care.

**Do:**
- Run three plays on the cancel screen.
- Play 1: show concrete loss.
- Play 1 microcopy: "You'll lose access to relationship data on your 476 configured clients and 8 months of history"
- Use concrete loss over abstract benefit. Concrete loss outweighs abstract benefit (loss aversion).
- Play 2: offer an alternative before goodbye.
- Play 2 microcopy: "Pause 30 days instead?"
- Or offer one more free month (ChatGPT nails this).
- Play 3: collect the reason with an open question.
- Play 3 microcopy: "What was missing for you to stay?"
- Never collect the reason with a dropdown. A dropdown rarely lists the real reason.

**Quote:** "If you invested to bring your user here, invest the last 30 seconds trying to keep them."

**Source:** [@richardrx · 2026-05-13](https://x.com/richardrx/status/2054562119962501186)

## Churn starts on the landing page, not at cancel

**Principle:**
- Know that an LP promise the product does not deliver creates an expectation debt.
- The debt charges interest every day the user thinks "this isn't what I expected".
- Know that the disappointment is pre-programmed, even if the product is excellent.

**Apply when:**
- 30-day churn is high but NPS is fine.
- In that case, suspect what you promised before users entered, not the product.

**Do:**
- Audit three common mismatches.
- Mismatch 1: result promise vs. tool delivery ("Increase sales 30%" → a metrics dashboard).
- Mismatch 2: simplicity promise vs. complex product ("Set up in 5 minutes" → 47 fields, 3 integrations, 20-min tutorial).
- Mismatch 3: promise aimed at the wrong ICP (LP speaks to a 2-person startup; product was built for a 15-person team at scale).
- Recalibrate the promise to match real delivery and ICP.

**Quote:** "The user bought a result and got a colorful spreadsheet."

**Source:** [@richardrx · 2026-04-29](https://x.com/richardrx/status/2049568514311172355)

## Anchor one-time-job products to a recurring life event

**Principle:**
- Know that a product hired to solve a one-off problem generates structural churn.
- A user who loves the product and still cancels is not unhappy.
- That user finished the job they came to do.
- Know that there was no continuous value to bring them back.

**Apply when:**
- You have 4.2 stars and positive NPS, yet churn rises.
- The product solves a point problem.
- Point-problem examples: resume builder, contract/legal-doc generator, data migration tool, pitch-deck builder, due-diligence platform.

**Do:**
- Use jobs-to-be-done thinking.
- Never fake engagement.
- Anchor the product to an event that already recurs in the user's life.
- Pick an event that returns yearly without a push.
- Ask: "If the job my product does is finished, what life event justifies the user coming back?"
- If there is no answer, classify the issue as a business-model problem, not a product problem.

**Evidence:**
- TurboTax (US income-tax software) tied itself to tax season, turning the product into a ritual because the event makes the use inevitable.

**Source:** [@richardrx · 2026-04-24](https://x.com/richardrx/status/2047620778338795918)

## Treat support volume as a design problem, not a staffing one

**Principle:**
- Know that a support problem is usually a design problem.
- Cut ticket volume during onboarding itself.
- Use an interface that answers questions before users ask them.
- Know that low-ticket digital products generate up to 3x more support than conventional tickets.

**Apply when:**
- Support is your biggest bottleneck, especially with low-ticket/impulse-buy products.
- You are tempted to just automate tickets.

**Do:**
- Know the three drivers of low-ticket support load.
- Driver 1: different buyer profile (less patience, less digital familiarity, more expectation of human help).
- Driver 2: impulse purchase (low friction → buys without understanding → seeks support).
- Driver 3: inverted opportunity cost (asking is easier than searching).
- For SaaS, redesign the journey.
- Add a contextual in-product FAQ.
- Add a self-answering UI.
- Never stop at automating support. Automation treats the symptom.
- Redesign the journey. This fixes the cause and can cut churn too.

**Evidence:**
- An old McAfee case cut support volume by 90% by implementing an FAQ.
- The FAQ was plain text. It had no chatbot.

**Source:** [@richardrx · 2026-04-23](https://x.com/richardrx/status/2047289409238712726)

## Strip the jargon before you blame onboarding

**Principle:**
- Know that churn that looks like a product problem is often a language problem.
- Chain of events: a technical founder writes product and sales copy in jargon.
- The ICP buys on a leap of faith and never perceives value.
- The ICP accumulates small disappointments and cancels.
- Know that this churn looks like a missing feature on the dashboard.

**Apply when:**
- Churn is high and you already revised onboarding and product.
- Revise language and structure next.

**Do:**
- Watch two biases.
- Bias 1: the curse of knowledge. You know too much and forget the other person does not.
- Bias 2: the easy-speech bias. Simple language reads as more trustworthy and raises awareness.
- Rewrite dense, jargon-heavy copy into plain language, even for complex topics.

**Visual:** Side-by-side: a dense, legalese contract clause (red X) vs. a plain-language rewrite "In this contract you authorize the bank…" (green check), with an "Easy-speech bias" callout. — `../assets/2041829519611371727__1.jpg`

**Quote:** "On the dashboard it looks like a missing feature; it was a mismatch between your discourse and their understanding."

**Source:** [@richardrx · 2026-04-08](https://x.com/richardrx/status/2041829519611371727)

## Retention is raising the cost of leaving day after day — iFood's behavioral lock-in

**Principle:**
- Know that iFood is not just a business model. It is Brazil's most sophisticated behavioral lock-in.
- Each layer raises the psychological and operational cost of leaving.
- The layers are delivery, data, credit and card.
- The mechanism is the sunk-cost effect plus ecosystem dependency.
- Know that the restaurant does not stay because iFood is good. It stays because leaving got too expensive.
- Treat retention as the accumulated cost of exit. Retention is not a feature.

**Apply when:**
- You design long-term retention or lock-in at any scale.

**Do:**
- Learn from the mechanism, ethically.
- Add layers of value that make leaving more expensive.
- Layer examples: data history, integrations, financial products, workflow embedding.
- Set the design goal to increase the cost of leaving over time.
- Never limit the design goal to "satisfy".

**Source:** [@richardrx · 2026-03-27](https://x.com/richardrx/status/2037543117612630126)

## Churn math: restructured onboarding can preserve R$4.8k MRR from an existing base

**Principle:**
- Baseline: 6% churn on 900 users at R$300 ARPU is 54 cancellations.
- Baseline loss: R$16.2k MRR leaves each month.
- Restructured onboarding cut cancellations by ~30%.
- The restructure had three parts: contextual welcome + empty state + activation checklist.
- Result: about 16 accounts retained, preserving R$4.8k MRR.
- Run-rate: R$57.6k ARR.
- Cohort value: R$52.8k over the post's stated 11-month average lifetime.
- Cost: no new traffic, no new feature.

**Apply when:**
- You justify onboarding investment to a numbers-driven founder.

**Do:**
- Keep the units explicit.
- Compute monthly cancellations = base × monthly churn.
- Compute prevented cancellations = cancellations × relative reduction.
- Compute recovered MRR = prevented cancellations × ARPU.
- Compute ARR run-rate = recovered MRR × 12.
- For cohort value, multiply recovered MRR by the stated average lifetime in months.
- Know that lower churn also raises valuation, because every growth action operates with more margin.

**Source:** [@richardrx · 2026-03-19](https://x.com/richardrx/status/2034571753263939621)

## Engineer addiction like a game so CS isn't a churn tax

**Principle:**
- Know that Customer Success is the tax you pay for a non-addictive product.
- If you need an army of CSMs to stop cancellations, the product failed.
- Name your real competitor: boredom. Boredom has infinite CAC.
- Know that the CNPJ buying your SaaS is the same brain that plays Candy Crush.
- Know that reward neuroscience is identical.
- Win retention across three game-design phases.

**Apply when:**
- Diagnose by behavior.
- Dropout at minutes 2–8 of onboarding: Phase 1.
- ~1.3 logins/week when it should be 4x: Phase 2.
- One departing employee kills the whole account: Phase 3.
- LTV:CAC below 3:1 means you are funding a product that cannot stand organically.

**Do:**

**Phase 1 — Time-to-value vs. cognitive load:**
- Ditch the setup wizard.
- Know that asking for work before delivering value reads as hostile territory in 10 seconds.
- Use progressive disclosure.
- Let users create and see results before you ask for email/card.
- Mechanism 1: Zeigarnik effect (incomplete-loop tension).
- Mechanism 2: endowment effect (people value 3x more what they helped build).
- Make empty states sell the dream.
- Never show "0 data" or blank templates.
- Populate a demo that simulates day-30 usage.

**Phase 2 — Habit loop / retention as biology:**
- Never ship passive software that only reacts. Passive software fails to build dependency.
- Ship proactive variable rewards.
- Know that the mesolimbic reward system releases dopamine on anticipation, not on the reward itself.
- Know that predictable rewards (monthly report) build tolerance.
- Use variable rewards to keep the loop alive. Example: "we detected a positive anomaly yesterday".
- Convert vanity metrics into loss-aversion triggers. Example: "Your team broke a record and you haven't seen it".
- Add temporal data scarcity. Example: "sync in 24h or lose the weekly benchmark".

**Phase 3 — Defensive moat:**
- Know that single-player products die when the champion leaves.
- Know that single-player products build dependence on a person, not on the org.
- Build multiplayer mode.
- Build data debt via social switching cost and network effects.
- Make User A's work block or depend on User B.
- Add reports that need multi-stakeholder approval.
- Add dashboards that aggregate 3 departments.
- Target this state: quitting requires an alignment meeting across Sales, Ops and Finance.
- In that state, you reach negative churn by bureaucratic inertia.
- Let accumulated datasets add organizational endowment effect.

**Quote:** "Stop blaming the customer. Your product is boring. And in the attention game, boring is bankruptcy."

**Source:** [@richardrx · 2026-01-30](https://x.com/richardrx/status/2017274698699067466)

## The 3 biggest churn reasons — and the fix for each

**Principle:**
- Know that most churn traces to three causes.
- Know that each cause has a distinct fix.
- Cause 1: bad onboarding.
- Fix 1: use gradual guided immersion to what users value most.
- Fix 1: add a Zeigarnik progress bar (incompleteness nags).
- Fix 1: add targeted tooltips on unexplored features.
- Cause 2: missing perceived value.
- Fix 2: show user ROI in a simple dashboard (Grammarly shows words helped).
- Fix 2: promote feature discovery continuously.
- Fix 2: build community.
- Cause 3: hard/confusing interface.
- Fix 3: run a proper product design project.

**Apply when:**
- Churn is high and you do not know which of the three causes it is.

**Do:**
- Diagnose first.
- Separate three user groups.
- Group 1: users who never reach value (activation).
- Group 2: users who reached value and still left (perceived value).
- Group 3: users who struggled (interface).
- Give each group its own owner and its own fix.
- Never treat all churn as one problem.

**Source:** [@richardrx · 2025-12-17](https://x.com/richardrx/status/2001408166404530231)
