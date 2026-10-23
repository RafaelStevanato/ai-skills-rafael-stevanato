# Pricing & Monetization Psychology

Attribution: Richard (@richardrx), "Richard — Design for startups", translated from Portuguese.
Each entry links to its source post.
Return to [SKILL.md](../SKILL.md).
Related files: [behavioral-science-toolkit.md](behavioral-science-toolkit.md), [onboarding-and-activation.md](onboarding-and-activation.md), [churn-and-retention.md](churn-and-retention.md), [metrics-and-experimentation.md](metrics-and-experimentation.md).

## Use a disfluent font for genuine deals — and name tiers for the mix you want

**Principle:**
- Treat a uniformly polished pricing page as easy to scan but weak at selling.
- Use a disfluent (ugly) font on the price of a genuinely favorable promotion.
- Expect a disfluent font to make people process the number more deeply.
- Expect tier labels to change purchase incidence.
- Expect tier labels to change which tier buyers choose.
- Expect these two effects to run in opposite directions.

**Apply when:**
- Pricing looks clean but plan distribution has been flat for months.
- Every company's pricing cards feel interchangeable.

**Do:**
- Keep the rest of the page legible.
- Test a deliberately ugly or disfluent font on a genuine promotional price.
- Never make the whole UI ugly.
- Choose tier labels by the outcome you want.
- Expect a superior-sounding metal ladder (Silver/Gold/Platinum) to reduce choice deferral but move the mix down. This is the result in Wang et al.'s experiments.
- Expect an inferior-sounding ladder (Bronze/Silver/Gold) to move the mix toward higher-priced tiers. This is the result in Wang et al.'s experiments.
- Richard applies that result to functional names such as Basic/Standard/Essential.
- Treat that mapping as a hypothesis.
- Measure purchase incidence and initial tier selection separately.

**Read with:**
- Read with "Build a single value axis, then tune the decoy's distance to your target plan" (2026-02-02).
- That post recommends aspirational Starbucks-style tier names to lift the brand.
- This post prices that choice: aspirational names sell more units, unglamorous ones sell more high tier.
- Pick the naming style by the metric you are optimizing.

**Evidence:**
- Motyka et al. (2016): disfluent fonts on price promotions prompt deeper processing.
- Motyka et al. (2016): disfluent fonts increase purchase behavior when the offer is a deal.
- Motyka et al. (2016): people like the display less.
- Wang et al. (2024), five experiments, 1,954 participants: superior-sounding labels increased purchase incidence but shifted choices toward cheaper options.
- Wang et al. (2024): inferior-sounding labels increased higher-priced choices.

**Visual:**
- Three pricing screenshots from the quoted post by @pankajstwt: 3-column Basic/Starter/Pro with near-identical includes; 2-column Launch/Scale; one-time Starter/Premium/Pro plus Ultimate.
- These are clean generic templates. Richard challenges the reader to tell them apart.
- `../assets/2092692547244007852__q__1.jpg`
- `../assets/2092692547244007852__q__2.jpg`
- `../assets/2092692547244007852__q__3.jpg`

**Source:** [@richardrx · 2026-08-26](https://x.com/richardrx/status/2092692547244007852)

## Price from cost+margin floor and value ceiling — never tarot or competitor-minus-20%

**Principle:**
- Never set price by tarot.
- Never set price by competitor price minus 20%.
- Use two calculations to get your floor and your ceiling.
- Floor = cost to serve + target margin.
- Include infra, support, tools and tokens in cost to serve.
- Example: cost R$10/account and margin 80% give a floor of R$50.
- Avoid a price that is too low. A low price signals low quality before use.
- Check CAC math. CAC can eat the margin.
- Example: CAC R$100 + margin R$40/mo = 2.5-month payback.
- Example: churn at month 3 = you worked 3 months for R$20.
- Ceiling = reference value.
- Reference value = what the client pays today to solve it their way (Excel + 1.5h/day of admin).
- Reference value also = the loss the client absorbs by not solving the problem.

**Apply when:**
- Setting or revisiting SaaS pricing.

**Do:**
- Quantify the delta in money for the client.
- Example, ICP auto repair shop: loses ~12 quotes/month to no follow-up × R$800 ticket × 30% margin × recovering 1/3 → R$3,200/mo revenue, R$960/mo profit.
- Use the sliding scale to place the price between floor and ceiling.
- Move the price up when value is easy to prove, the buyer is convinced and competition is little.
- Settle for ~10% of the value generated when value is hard to prove, the buyer is skeptical and a competitor is on every corner.
- Never rely on commodity features (work orders, scheduling, reports) to sustain price.
- Know that commodity features only put you in the same comparison table.

**Source:** [@richardrx · 2026-08-03](https://x.com/richardrx/status/2084250609687884144)

## The freemium trap, in numbers: higher conversion, far lower cash

**Principle:**
- Know that a free plan lifts signup conversion.
- Know that a free plan can crush the economics.
- Know that the higher top-of-funnel number hides a worse business.

**Apply when:**
- You are tempted by freemium's better conversion rate.

**Do:**
- Run the funnel for both scenarios before you choose a free plan.
- Use the same inputs for both scenarios: R$80k/mo traffic, plans from R$199.
- Use freemium only if free brings *organic/viral* users you didn't pay for.

**Funnel with freemium:**
- ~8% → 800 signups → 80% activate → 5% pay = 32 payers (R$6,368 MRR).
- Payers saturate at ~160 under 20% churn.
- 768 free users burn AI tokens (~$0.08 each).
- Real CAC ≈ R$2,540/payer.
- Payback ~13 months.

**Funnel without freemium:**
- ~3% → 300 payers = R$59,700 MRR (~10×).
- CAC ~R$275.
- Payback ~6 weeks.
- LTV:CAC 5:1 that reinvests its own profit.

**Quote:** "One scenario reinvests its own profit; the other funds losses until the money runs out."

**Source:** [@richardrx · 2026-07-01](https://x.com/richardrx/status/2072312844784152628)

## Whether freemium works is decided by the cost to serve a free user

**Principle:**
- Never judge freemium as good or bad in the abstract.
- Decide by the *cost of free*.
- The cost of free hinges on two factors.
- Factor 1: how much it costs to serve non-payers.
- Factor 2: how long and how expensive activation is.

**Apply when:**
- You consider a free plan.
- You are a bootstrapped (non-bigtech) founder.

**Do:**
- Use free as an acquisition channel if serving a free user costs almost nothing and TTV is short.
- Example: Slack. The first message happens in minutes.
- Know that the short TTV sustains it, not the cash.
- Treat a free account as an expensive risk if the product runs on AI (dollar-priced tokens) or activation is long.
- Know that only a small fraction of users funds that risk.
- Know that it needs deep pockets. Deep pockets are the exception, not the average founder.
- Otherwise: charge. Charge well. Charge early.
- Use 3–4% free-to-paid conversion for planning. It is the conservative figure.
- Know that the funnel in "The freemium trap, in numbers: higher conversion, far lower cash" models 5% of activated users paying.
- Know that [churn-and-retention.md](churn-and-retention.md) cites a median free-to-paid of 8% (Kyle Poyar).

**Evidence:**
- On a friendly average, only ~3–4% of freemium converts.

**Quote:** "For an AI product, your free user was never free."

**Source:** [@richardrx · 2026-06-30](https://x.com/richardrx/status/2071962778072469560)

## Price is the cheapest money — stop anchoring it to the cheapest competitor

**Principle:**
- Know that pricing is a SaaS's biggest lever.
- Know that ~90% of products are underpriced.
- Know why: the founder knows every limitation and anchors on the cheapest competitor.
- Anchor on value delivered instead. The buyer only sees the problem solved.

**Apply when:**
- Setting or revisiting price.
- You fear a "no."

**Do:**
- Raise the price toward value.
- Expect a 30% price increase to yield less than 30% MRR (some churn).
- Count what remains as nearly pure cash. No acquisition sits in between.
- Compare: growing a channel 30% costs money and time, and it has a ceiling.
- Avoid a low price. It costs you later in three ways:
  - Less budget to reach your ICP.
  - A CAC-obsession trap. The real metric is the CAC↔LTV *gap*. Price widens that gap on both sides.
  - Higher churn. Cheap attracts uncommitted buyers.
- Sustain the number with perceived value.
- Check that your page and first use justify the price. They justify it or destroy it.

**Quote:** "Charging more without seeming to be worth more is just raising the price of rejection."

**Source:** [@richardrx · 2026-06-29](https://x.com/richardrx/status/2071634185228329219)

## 1% on price beats 1% on acquisition — you raise prices too little and too late

**Principle:**
- Know that a 1% price improvement drives ~8–11% more profit (ProfitWell) on typical SaaS margins.
- Know that a 1% acquisition improvement yields ~2%.
- Know that 70% of executives rank acquisition as the most important growth lever. It pays least.
- Know why price is left untouched: loss aversion.
- Fear of losing what you have screams louder than the chance to gain.

**Apply when:**
- It has been >12 months since a price change.
- The product improved meanwhile.

**Do:**
- Test the new price only on new customers.
- Never touch the base.
- Count the test as a win if the higher ticket offsets the conversion drop.
- Expect users who pay more to churn less.
- Raise the price gradually, anchored in value.
- Communicate what improved.
- Never send a naked increase.
- Never A/B test price. You lack volume.
- Segment customers and run willingness-to-pay research instead.

**Quote:** "If 1% on price pays five times more than 1% on acquisition, why is nearly all your energy at the top of the funnel?"

**Source:** [@richardrx · 2026-06-03](https://x.com/richardrx/status/2062127283977019757)

## Competing on price is adverse selection — you filter in the worst client

**Principle:**
- Know that price-led copycats attract bargain hunters.
- Bargain hunters enter because you are cheapest.
- Bargain hunters leave the second someone is R$1 cheaper.
- Expect high churn, zero loyalty and the most support tickets.
- Know that price as bait is a filter for the client you least want.
- Follow Kawasaki's "Be a baker, not an eater".
- Bake your own pie via niche. Example: a CRM for facial-aesthetics clinics, not another CRM.
- Charge 5x with no comparison.
- Use the giant's weight against it (jiu-jitsu).
- Look for big players' blind spots in public complaints.
- Search these places: ReclameAqui, app stores, Google Places, communities, FB/WhatsApp groups, niche sites.
- Count each complainer as ~26 equally unhappy silent ones.

**Apply when:**
- You are tempted to differentiate purely on being cheaper than a big player.

**Do:**
- Mine complaints for the niche, the angle, the vocabulary, the pain and the promise for your LP.
- Accept that you will be copied.
- Know that storefronts look equal but the model underneath (your niche, angle, economics) isn't.
- Example: McDonald's is a real-estate company dressed as a burger joint.
- Example: BK is royalties.
- Remember: same storefront, different machine.

**Source:** [@richardrx · 2026-06-03](https://x.com/richardrx/status/2062314549483589691)

## Make the middle plan the one you actually want to sell

**Principle:**
- Give each plan a behavioral job, not just a price.
- Put the plan you most want to sell in the middle.
- Flank it with a decoy below and an anchor above.

**Apply when:**
- You build or audit a SaaS pricing page.
- You copied competitors without assigning each tier a role.

**Do:**
- Use the decoy effect.
- Place your target (e.g. Pro) in the middle.
- Make the tier below it clearly inferior on one important attribute so Pro looks obvious.
- Pick the attribute from these: user cap, no critical integration, no priority support.
- Keep exactly three plans.
- Know that four+ plans trigger the paradox of choice and users stall.
- Add a top tier (Enterprise) purely to anchor price perception.
- Ask: "What is my decoy today?"
- Assume the decoy does not exist if you cannot name one.

**Conflict note (plan count):**
- This section says: "Keep exactly three plans — four+ triggers the paradox of choice".
- "Engineer the pricing page with Good-Better-Best and control the comparison" says: "Cap at 2–5 plans (6 = anxiety, paradox of choice)".
- Its visual shows a four-tier mockup.
- Use exactly 3 plans by default.
- Treat 2–5 plans as the outer bound only.
- Never use 6 or more plans.
- Treat the four-tier mockup as an example inside the outer bound, not as the default.

**Evidence:**
- Ariely's MIT test of The Economist's tiers: with the print-only decoy, 16%/84% chose online/combo.
- Removing the decoy flipped choices to 68%/32%.
- Removing the decoy cut combo revenue by more than half.
- Estimated +30–43% subscription revenue.

**Visual:**
- Economist subscription page. The decoy's removal shifts combo-plan share from 84% down to 32%.
- `../assets/2059951433827426437__1.jpg`

**Quote:** "Option B was never built to be sold — it was built to make C look obvious. It's the bait."

**Source:** [@richardrx · 2026-05-28](https://x.com/richardrx/status/2059951433827426437)

## Ask for the card in trial — but optimize for the right ICP, not raw conversion

**Principle:**
- Know that requiring a credit card multiplies trial-to-paid conversion but shrinks signups.
- Pick the model that attracts and retains the right ICP.
- Never pick the model with the highest headline conversion by default.

**Apply when:**
- You choose between trial-with-card and trial-without-card (or freemium).
- You design recurring billing for a Brazilian market.

**Do:**
- Weigh the funnel both ways.
- Expect trial-with-card to convert harder but starve you of volume.
- Expect trial-without-card to flood the funnel with low-intent users.
- Run the full math, not just the conversion rate.
- In Brazil, account for PIX recorrente.
- Know that PIX recorrente dynamics differ from monthly card billing.

**Evidence:**
- ChartMogul 2026 (US, 200 products): trial-with-card converts ~31.4% vs 8.9% without. That is 3x+.
- Worked funnel from 1,000 visitors, with card: 30 trials → 9.4 paying.
- Worked funnel from 1,000 visitors, without card: 85 trials → 7.5 paying.
- Author observes PIX-recorrente cohorts churn more than card cohorts.

**Quote:** "Don't ask which model converts more — ask which model attracts and retains the right ICP."

**Source:** [@richardrx · 2026-05-15](https://x.com/richardrx/status/2055247161349054950)

## Frame the upgrade as a loss at the moment of value, not a feature you're selling

**Principle:**
- Treat low upgrade rates as a framing-and-timing problem, usually not a price problem.
- Remind users what they have already invested.
- Remind users what they stand to lose.

**Apply when:**
- A happy, active free user never upgrades.
- Your upgrade rate sits below 5%.

**Do:**
- Use three framings. They beat generic limit/discount/feature-gate prompts.
- Framing 1, sunk cost: surface the assets the user built.
- Sunk cost example: "You created 47 custom reports. On the free plan you lose access to 40."
- Framing 2, loss aversion: frame the loss, not the gain. Framing loss outconverts framing gain.
- Loss aversion example: "You'll lose access to 8 months of history" beats "Get unlimited history."
- Framing 3, limited-access gate: time it to an imminent, known result.
- Limited-access gate example: "Your report is ready. To export as PDF, activate Pro."
- Set gate timing and context first. They matter more than the gate itself.

**Quote:** "If your upgrade rate is below 5%, the problem probably isn't price — it's how and when you're asking."

**Source:** [@richardrx · 2026-04-21](https://x.com/richardrx/status/2046544442216054981)

## Engineer the comparison frame with a decoy and a high anchor — and drop Free from the top

**Principle:**
- Change the frame of comparison, not the product, to shift conversion.
- Know that equal-looking options cause delay.
- Know that showing Free first anchors everyone to zero. Everything else then feels expensive.

**Apply when:**
- You run the default Free / Pro / Enterprise (sob consulta, meaning "price on request") ladder.
- Pro isn't converting.

**Do:**
- Insert a decoy: a Starter just below Pro with irritating limitations (e.g. R$79 vs Pro R$99).
- Expect users to compare Starter↔Pro. Pro wins for R$20 more.
- Remove Free from the visible top so the first number isn't zero.
- Remember anchoring: the first price seen sets the reference.
- Lead with a higher, previous or Enterprise price so Pro at R$99 reads as cheap.

**Evidence:**
- The Economist sold 3x more print+digital after adding a same-price print-only decoy nobody bought.
- Author cites documented tests lifting conversion 10–20% via reframing alone.

**Quote:** "You're competing against your own free plan. And losing."

**Source:** [@richardrx · 2026-04-14](https://x.com/richardrx/status/2044014136770580743)

## Tie the trial's end to value consumed, not the calendar

**Principle:**
- Treat blocking access on a fixed day count (7/14/28) as a lazy rule.
- Fire the billing trigger on value consumption.
- Fire it after the user's first real win.

**Apply when:**
- You copied a competitor's 14-day trial and paid conversion is failing.
- You set trial length from scratch.

**Do:**
- Never paywall before a clear micro-win or before the user solves the core problem.
- Know that an early paywall kills conversion and breeds bad word of mouth.
- Set trial length with four variables.
- Variable 1, product complexity: enterprise needs time for compliance/security review, not just the user.
- Variable 2, Time to Value: Spotify delivers in seconds; a CRM needs days of data.
- Variable 3, usage frequency: rarely-used products may need long trials, or none at all. A once-a-year tax tool shouldn't have a trial.
- Variable 4, card entry: no card means a shorter trial to create urgency; with card, watch silent next-month churn.
- Count on sunk cost only if the user built a real asset.
- Know that a bad onboarding produces frustration, not switching cost.

**Quote:** "Locking access purely on the calendar is a lazy rule that can cost you dearly — you're burning CAC without knowing where value lands."

**Source:** [@richardrx · 2026-03-16](https://x.com/richardrx/status/2033502548301091057)

## Order pricing rows by the serial-position effect: killer feature first, differentiator last

**Principle:**
- Know that users don't read pricing lists linearly.
- Know that attention and memory cluster on the first and last items.
- Treat feature order as a conversion lever.

**Apply when:**
- You lay out the feature rows inside a pricing card or comparison table.

**Do:**
- Exploit the serial-position effect (primacy + recency).
- Top zone, the value anchor: never lead with "24/7 support".
- Top zone: lead with the core/killer feature that solves the ICP's main pain.
- Top zone: choose a feature that justifies ~80% of the ticket and the ROI.
- Middle zone: list the utilitarian features (exports, integrations, storage limits).
- Middle zone: expect the user to scan them to compare against the next plan, not memorize them.
- Bottom zone (nearest the CTA): put the differentiator, bonus or loss-aversion hook.
- Bottom zone examples: a lifetime guarantee or dedicated support.
- Know that the middle of the list is "a cognitive black hole."

**Visual:**
- Pricing card emphasizing the bold first row (core feature) and bold last row (super bonus), with greyed utilitarian middle rows.
- `../assets/2029623167900061970__1.jpg`

**Quote:** "Pricing success depends not just on what you deliver, but on the order the brain is led to process the value."

**Source:** [@richardrx · 2026-03-05](https://x.com/richardrx/status/2029623167900061970)

## Engineer the pricing page with Good-Better-Best and control the comparison

**Principle:**
- Know that lost LTV is rarely about price.
- Blame analysis paralysis from a missing choice architecture.
- Know that the brain is lazy and judges by relative comparison (priming + anchoring).
- Design the anchor yourself.
- Know that without your anchor, users compare you to "nothing" or to the cheapest competitor.

**Apply when:**
- You design or fix a pricing page.
- Conversions die at the final step despite strong CAC spend.

**Do:**
- Use a Good-Better-Best (GBB) structure.
- **Good** = a stripped entry plan that anchors a low price.
- Limit Good enough to make users feel pain and look up.
- Never make Good free. Then everything above looks expensive.
- **Better** = your standard plan, the target for ~80% of buyers.
- Price Better closer to Good than to Best.
- Aim for the user thought: "paying only ~20% more I get double?"
- **Best** = the value anchor that exists mainly to make Better look cheap.
- Bicycle analogy: without the carbon-fiber Best, the carbon-wheel Better looks expensive.
- Golden rule: keep comparisons on one axis.
- Never pit "10,000 tokens" against "Priority Support".
- Prefer linear, ideally asymmetric, growth.
- Cap at 2–5 plans (6 = anxiety, paradox of choice).
- Control which attributes you compare, like your own "Brazil vs Paraguay" table.
- Choose indicators that favor your value thesis.
- Highlight Better with color, size or badges.
- Do the math for the user: "Stop making the user do the math — do the math for them."

**Conflict note (plan count):**
- See the conflict note in [Make the middle plan the one you actually want to sell](#make-the-middle-plan-the-one-you-actually-want-to-sell).
- Use exactly 3 plans by default. Treat 2–5 as the outer bound.

**Evidence:**
- Cites Briesch et al. (1997) and Mazumdar et al. (2005) on reference-price models.
- Cites Chernev (2015) on choice overload.

**Visual:**
- Two mirrored BR-vs-PY indicator tables prove framing. Swapping which metrics are shown flips which country "wins".
- `../assets/2018693884449009956__2.jpg`
- `../assets/2018693884449009956__3.jpg`
- Four-tier mockup highlights a "Most Popular" target beside a high anchor (Hick's law / few options).
- `../assets/2018693884449009956__4.jpg`

**Quote:** "Your pricing page is killing your LTV — and I can prove it."

**Source:** [@richardrx · 2026-02-03](https://x.com/richardrx/status/2018693884449009956)

## Build a single value axis, then tune the decoy's distance to your target plan

**Principle:**
- Make a plan ladder read as one clear progression of value.
- Know that mixing quantitative and qualitative axes muddles the ladder.
- Know that the decoy's price placement decides which plan looks like the deal.

**Apply when:**
- You name and price tiers.
- The "value staircase" between your plans isn't obvious to users.

**Do:**
- Pick one progression.
- Option 1, quantitative: rising credits/users.
- Option 2, qualitative: 24/7 human support, special features.
- Never blend both.
- Borrow Starbucks-style naming (Tall/Grande/Venti).
- Expect every tier to sound good and lift the brand.
- Position the decoy near the most expensive plan: the expensive plan looks cheap.
- Position the decoy near the cheapest plan: the decoy itself becomes the most attractive option.

**Read with:**
- Read with "Use a disfluent font for genuine deals — and name tiers for the mix you want" (2026-08-26).
- Aspirational names lift purchase incidence.
- Unglamorous names shift the mix toward higher-priced tiers.

**Source:** [@richardrx · 2026-02-02](https://x.com/richardrx/status/2018357024543715480)
