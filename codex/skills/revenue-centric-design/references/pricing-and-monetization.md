# Pricing & Monetization Psychology

Contents: Use a disfluent font for genuine deals — and name tiers for the mix you want · Price from cost+margin floor and value ceiling — never tarot or competitor-minus-20% · The freemium trap, in numbers: higher conversion, far lower cash · Whether freemium works is decided by the cost to serve a free user · Price is the cheapest money — stop anchoring it to the cheapest competitor · 1% on price beats 1% on acquisition — you raise prices too little and too late · Competing on price is adverse selection — you filter in the worst client · Make the middle plan the one you actually want to sell · Ask for the card in trial — but optimize for the right ICP, not raw conversion · Frame the upgrade as a loss at the moment of value, not a feature you're selling · Engineer the comparison frame with a decoy and a high anchor — and drop Free from the top · Tie the trial's end to value consumed, not the calendar · Order pricing rows by the serial-position effect: killer feature first, differentiator last · Engineer the pricing page with Good-Better-Best and control the comparison · Build a single value axis, then tune the decoy's distance to your target plan

Attribution: Richard (@richardrx), "Richard — Design for startups", translated from Portuguese. Return to [SKILL.md](../SKILL.md).

## Use a disfluent font for genuine deals — and name tiers for the mix you want

A polished pricing page scans easily but sells weakly.

**Apply when:** Plan distribution is flat for months, or pricing cards look interchangeable.
**Do:**
- Test a disfluent (ugly) font on the price of a genuine promotion only. Keep the rest of the UI legible.
- Choose tier labels by outcome (Wang et al.): Silver/Gold/Platinum (superior-sounding) reduced choice deferral but moved the mix down; Bronze/Silver/Gold (inferior-sounding) moved it toward higher-priced tiers.
- Treat Richard's application of that result to functional names (Basic/Standard/Essential) as a hypothesis. Measure purchase incidence and initial tier selection separately.
- Read with "Build a single value axis, then tune the decoy's distance to your target plan" (2026-02-02): that post recommends aspirational Starbucks-style tier names. This one prices that choice: aspirational names sell more units, unglamorous ones sell more high tier. Pick by the metric you optimize.

**Evidence:** Motyka et al. (2016): a disfluent font on a deal's price prompts deeper processing and raises purchases, although people like the display less. Wang et al. (2024), five experiments, 1,954 participants: superior-sounding labels raised purchase incidence but shifted choices toward cheaper options.
**Visual:** Three generic pricing templates from the quoted post by @pankajstwt (3-column Basic/Starter/Pro, near-identical includes; 2-column Launch/Scale; one-time Starter/Premium/Pro plus Ultimate): `../assets/2092692547244007852__q__1.jpg`, `../assets/2092692547244007852__q__2.jpg`, `../assets/2092692547244007852__q__3.jpg`
**Source:** [@richardrx · 2026-08-26](https://x.com/richardrx/status/2092692547244007852)

## Price from cost+margin floor and value ceiling — never tarot or competitor-minus-20%

- Floor = cost to serve (infra, support, tools, tokens) + target margin. R$10 per account at 80% margin gives R$50.
- Ceiling = reference value: what the client pays today to solve it their way (Excel + 1.5h/day of admin), or the loss from not solving.
- Traps: a price too low signals low quality before use. CAC eats margin: CAC R$100 + margin R$40/mo = 2.5-month payback; churn at month 3 = you worked 3 months for R$20.

**Apply when:** Setting or revisiting SaaS pricing.
**Do:**
- Quantify the delta in money for the client. ICP auto repair shop: ~12 quotes/month lost to no follow-up × R$800 ticket × 30% margin × recovering 1/3 → R$3,200/mo revenue, R$960/mo profit.
- Slide the price between floor and ceiling. Value easy to prove, buyer convinced, little competition: move up. Value hard to prove, buyer skeptical, a competitor on every corner: settle for ~10% of the value generated.
- Never rely on commodity features (work orders, scheduling, reports) to sustain price. They only put you in the same comparison table.

**Source:** [@richardrx · 2026-08-03](https://x.com/richardrx/status/2084250609687884144)

## The freemium trap, in numbers: higher conversion, far lower cash

**Apply when:** Freemium's better conversion rate tempts you.
**Do:**
- Run both funnels before you choose a free plan. Same inputs: R$80k/mo traffic, plans from R$199.
- With freemium: ~8% → 800 signups → 80% activate → 5% pay = 32 payers (R$6,368 MRR), saturating ~160 payers under 20% churn. The 768 free users burn AI tokens (~$0.08 each). Real CAC ≈ R$2,540/payer, payback ~13 months.
- Without freemium: ~3% → 300 payers = R$59,700 MRR (~10×), CAC ~R$275, payback ~6 weeks, LTV:CAC 5:1.
- Use freemium only if free brings *organic/viral* users you did not pay for.

**Quote:** "One scenario reinvests its own profit; the other funds losses until the money runs out."
**Source:** [@richardrx · 2026-07-01](https://x.com/richardrx/status/2072312844784152628)

## Whether freemium works is decided by the cost to serve a free user

The *cost of free* decides: (1) the cost to serve non-payers and (2) how long and expensive activation is.

**Apply when:** Considering a free plan, especially as a bootstrapped (non-bigtech) founder.
**Do:**
- Use free as an acquisition channel when serving a free user costs almost nothing and TTV is short. Slack: first message in minutes; short TTV, not cash, sustains it.
- Treat a free account as an expensive bet when the product runs on AI (dollar-priced tokens) or activation is long. A small fraction of users funds that bet, which needs deep pockets: the exception, not the average founder.
- Otherwise charge, charge well, and charge early.
- Plan with the conservative 3–4% free-to-paid. The [freemium-trap funnel](#the-freemium-trap-in-numbers-higher-conversion-far-lower-cash) models 5% of activated users paying. [churn-and-retention.md](churn-and-retention.md) cites a median 8% (Kyle Poyar).

**Evidence:** On a friendly average, only ~3–4% of freemium converts.
**Quote:** "For an AI product, your free user was never free."
**Source:** [@richardrx · 2026-06-30](https://x.com/richardrx/status/2071962778072469560)

## Price is the cheapest money — stop anchoring it to the cheapest competitor

Pricing is a SaaS's biggest lever, yet ~90% of products are underpriced. The founder, who knows every limitation, anchors on the cheapest competitor; the buyer only sees the problem solved.

**Apply when:** Setting or revisiting price, or fearing a "no."
**Do:**
- Raise the price toward value.
- Expect a 30% price increase to yield less than 30% MRR (some churn). What remains is nearly pure cash, with no acquisition in between. Growing a channel 30% costs money and time, and has a ceiling.
- Avoid a low price. It costs you later: less budget to reach your ICP; a CAC-obsession trap (the real metric is the CAC↔LTV *gap*, which price widens on both sides); higher churn, because cheap attracts uncommitted buyers.
- Sustain the price with perceived value: your page and first use justify or destroy it.

**Quote:** "Charging more without seeming to be worth more is just raising the price of rejection."
**Source:** [@richardrx · 2026-06-29](https://x.com/richardrx/status/2071634185228329219)

## 1% on price beats 1% on acquisition — you raise prices too little and too late

A 1% price improvement drives ~8–11% more profit (ProfitWell) on typical SaaS margins. A 1% acquisition improvement yields ~2%. Yet 70% of executives rank acquisition as the top growth lever. Loss aversion leaves price untouched: fear of loss outweighs the chance to gain.

**Apply when:** More than 12 months since a price change, and the product improved meanwhile.
**Do:**
- Test the new price only on new customers. Never touch the base.
- Count the test as a win if the higher ticket offsets the conversion drop. Users who pay more churn less.
- Raise the price gradually, anchored in value. Communicate what improved. Never send a naked increase.
- Never A/B test price. You lack volume. Segment customers and run willingness-to-pay research instead.

**Quote:** "If 1% on price pays five times more than 1% on acquisition, why is nearly all your energy at the top of the funnel?"
**Source:** [@richardrx · 2026-06-03](https://x.com/richardrx/status/2062127283977019757)

## Competing on price is adverse selection — you filter in the worst client

Price-led copycats attract bargain hunters. They enter because you are cheapest and leave the second someone is R$1 cheaper. Expect high churn, zero loyalty and the most support tickets.

**Apply when:** Tempted to differentiate purely on being cheaper than a big player.
**Do:**
- Follow Kawasaki's "Be a baker, not an eater". Bake your own pie via niche (a CRM for facial-aesthetics clinics, not another CRM). Charge 5x with no comparison.
- Use the giant's weight against it (jiu-jitsu). Find the big players' blind spots in public complaints: ReclameAqui, app stores, Google Places, communities, FB/WhatsApp groups, niche sites. Each complainer represents ~26 equally unhappy silent ones.
- Mine complaints for the niche, angle, vocabulary, pain and promise for your LP.
- Accept that you will be copied. Storefronts look equal, but the model underneath (your niche, angle, economics) does not. McDonald's is a real-estate company dressed as a burger joint. BK is royalties.

**Source:** [@richardrx · 2026-06-03](https://x.com/richardrx/status/2062314549483589691)

## Make the middle plan the one you actually want to sell

**Apply when:** Building or auditing a SaaS pricing page, especially with competitor tiers copied and no role assigned to each tier.
**Do:**
- Give each plan a behavioral job, not just a price. Use the decoy effect: place your target (e.g. Pro) in the middle, flanked by a decoy below and an anchor above.
- Make the tier below it clearly inferior on one important attribute (user cap, no critical integration, no priority support), so Pro looks obvious.
- Keep exactly three plans. Four+ plans trigger the paradox of choice and users stall.
- Add a top tier (Enterprise) purely to anchor price perception.
- Ask: "What is my decoy today?" If you cannot name one, it likely does not exist.

**Conflict note (plan count):** The Good-Better-Best entry allows 2–5 plans and shows a four-tier mockup. Use exactly 3 plans by default; 2–5 is the outer bound.
**Evidence:** Ariely's MIT test of The Economist's tiers: with the print-only decoy, 16%/84% chose online/combo. Removing the decoy flipped choices to 68%/32% and cut combo revenue by more than half. Estimated +30–43% subscription revenue.
**Visual:** Economist subscription page with and without the decoy: `../assets/2059951433827426437__1.jpg`
**Quote:** "Option B was never built to be sold — it was built to make C look obvious. It's the bait."
**Source:** [@richardrx · 2026-05-28](https://x.com/richardrx/status/2059951433827426437)

## Ask for the card in trial — but optimize for the right ICP, not raw conversion

**Apply when:** Choosing between trial-with-card and trial-without-card (or freemium), or designing recurring billing for a Brazilian market.
**Do:**
- Expect a required credit card to multiply trial-to-paid conversion but shrink signups.
- Weigh the funnel both ways: trial-with-card converts harder but starves you of volume; trial-without-card floods the funnel with low-intent users. Run the full math, not just the conversion rate.
- In Brazil, account for PIX recorrente. Its dynamics differ from monthly card billing.

**Evidence:** ChartMogul 2026 (US, 200 products): trial-with-card converts ~31.4% vs 8.9% without (3x+). Worked funnel: 1,000 visitors → 30 trials → 9.4 paying (with card) vs 85 trials → 7.5 paying (without). The author observes that PIX-recorrente cohorts churn more than card cohorts.
**Quote:** "Don't ask which model converts more — ask which model attracts and retains the right ICP."
**Source:** [@richardrx · 2026-05-15](https://x.com/richardrx/status/2055247161349054950)

## Frame the upgrade as a loss at the moment of value, not a feature you're selling

**Apply when:** A happy, active free user never upgrades, or the upgrade rate is below 5%.
**Do:** Remind users what they invested and stand to lose, with three framings. They beat generic limit/discount/feature-gate prompts:
- (1) Sunk cost: surface the assets the user built — "You created 47 custom reports. On the free plan you lose access to 40."
- (2) Loss aversion: framing loss outconverts framing gain — "You'll lose access to 8 months of history" beats "Get unlimited history."
- (3) Limited-access gate: time it to an imminent, known result — "Your report is ready. To export as PDF, activate Pro."

Gate timing and context matter more than the gate itself.

**Quote:** "If your upgrade rate is below 5%, the problem probably isn't price — it's how and when you're asking."
**Source:** [@richardrx · 2026-04-21](https://x.com/richardrx/status/2046544442216054981)

## Engineer the comparison frame with a decoy and a high anchor — and drop Free from the top

Change the frame of comparison, not the product, to shift conversion. Equal-looking options cause delay.

**Apply when:** Running the default Free / Pro / Enterprise (sob consulta, meaning "price on request") ladder, and Pro is not converting.
**Do:**
- Insert a decoy: a Starter just below Pro with irritating limitations (e.g. R$79 vs Pro R$99). Users then compare Starter↔Pro, and Pro wins for R$20 more.
- Remove Free from the visible top. Showing Free first anchors everyone to zero, so everything else feels expensive.
- Use anchoring: the first price seen sets the reference. Lead with a higher, previous or Enterprise price, so Pro at R$99 reads as cheap.

**Evidence:** The Economist sold 3x more print+digital after adding a same-price print-only decoy nobody bought. The author cites documented tests lifting conversion 10–20% via reframing alone.
**Quote:** "You're competing against your own free plan. And losing."
**Source:** [@richardrx · 2026-04-14](https://x.com/richardrx/status/2044014136770580743)

## Tie the trial's end to value consumed, not the calendar

**Apply when:** A competitor's 14-day trial was copied and paid conversion fails, or trial length is set from scratch.
**Do:**
- Never block access on a fixed day count (7/14/28). Fire the billing trigger on value consumption, after the user's first real win.
- Never paywall before a clear micro-win or before the user solves the core problem: an early paywall kills conversion and breeds bad word of mouth.
- Set trial length with four variables:
  1. Product complexity: enterprise needs time for compliance/security review, not just the user.
  2. Time to Value: Spotify delivers in seconds; a CRM needs days of data.
  3. Usage frequency: rarely-used products may need long trials, or none at all. A once-a-year tax tool should not have a trial.
  4. Card entry: no card means a shorter trial to create urgency. With card, watch silent next-month churn.
- Count on sunk cost only if the user built a real asset. A bad onboarding produces frustration, not switching cost.

**Quote:** "Locking access purely on the calendar is a lazy rule that can cost you dearly — you're burning CAC without knowing where value lands."
**Source:** [@richardrx · 2026-03-16](https://x.com/richardrx/status/2033502548301091057)

## Order pricing rows by the serial-position effect: killer feature first, differentiator last

**Apply when:** Laying out the feature rows inside a pricing card or comparison table.
**Do:** Exploit the serial-position effect (primacy + recency): attention and memory cluster on the first and last items.
- Top, the value anchor: never lead with "24/7 support". Lead with the core/killer feature that solves the ICP's main pain and justifies ~80% of the ticket and the ROI.
- Middle: list the utilitarian features (exports, integrations, storage limits). Users scan them to compare against the next plan and do not memorize them. The middle is "a cognitive black hole."
- Bottom (nearest the CTA): put the differentiator, bonus or loss-aversion hook, such as a lifetime guarantee or dedicated support.

**Visual:** Pricing card with a bold first row (core feature), a bold last row (super bonus) and greyed utilitarian middle rows: `../assets/2029623167900061970__1.jpg`
**Quote:** "Pricing success depends not just on what you deliver, but on the order the brain is led to process the value."
**Source:** [@richardrx · 2026-03-05](https://x.com/richardrx/status/2029623167900061970)

## Engineer the pricing page with Good-Better-Best and control the comparison

Lost LTV is rarely about price: a missing choice architecture causes analysis paralysis. The brain judges by relative comparison (priming + anchoring). Without your anchor, users compare you to "nothing" or to the cheapest competitor.

**Apply when:** Designing or fixing a pricing page, or conversions die at the final step despite strong CAC spend.
**Do:** Use a Good-Better-Best (GBB) structure.
- **Good** = a stripped entry plan that anchors a low price. Limit it enough that users feel pain and look up. Never make it free: everything above would look expensive.
- **Better** = your standard plan, the target for ~80% of buyers. Price it closer to Good than to Best. Aim for the user thought: "paying only ~20% more I get double?"
- **Best** = the value anchor that exists mainly to make Better look cheap. Bicycle analogy: without the carbon-fiber Best, the carbon-wheel Better looks expensive.
- Golden rule: keep comparisons on one axis. Never pit "10,000 tokens" against "Priority Support". Prefer linear, ideally asymmetric, growth.
- Cap at 2–5 plans (6 = anxiety, paradox of choice). Default to exactly 3: see the [plan-count conflict note](#make-the-middle-plan-the-one-you-actually-want-to-sell).
- Control which attributes you compare, like your own "Brazil vs Paraguay" table. Choose indicators that favor your value thesis. Highlight Better with color, size or badges.
- Do the math for the user: "Stop making the user do the math — do the math for them."

**Evidence:** Cites Briesch et al. (1997) and Mazumdar et al. (2005) on reference-price models, and Chernev (2015) on choice overload.
**Visual:** Two mirrored BR-vs-PY indicator tables: swapping the metrics shown flips which country "wins": `../assets/2018693884449009956__2.jpg`, `../assets/2018693884449009956__3.jpg`. Four-tier mockup highlights a "Most Popular" target beside a high anchor (Hick's law / few options): `../assets/2018693884449009956__4.jpg`
**Quote:** "Your pricing page is killing your LTV — and I can prove it."
**Source:** [@richardrx · 2026-02-03](https://x.com/richardrx/status/2018693884449009956)

## Build a single value axis, then tune the decoy's distance to your target plan

**Apply when:** Naming and pricing tiers, or the "value staircase" between plans is not obvious to users.
**Do:**
- Make the plan ladder one clear progression of value. Pick quantitative (rising credits/users) or qualitative (24/7 human support, special features), never both.
- Borrow Starbucks-style naming (Tall/Grande/Venti), so every tier sounds good and lifts the brand.
- Place the decoy's price deliberately: it decides which plan looks like the deal. Near the most expensive plan, the expensive plan looks cheap. Near the cheapest plan, the decoy itself becomes the most attractive option.
- Read with "Use a disfluent font for genuine deals — and name tiers for the mix you want" (2026-08-26): aspirational names lift purchase incidence, but unglamorous ones shift the mix toward higher-priced tiers.

**Source:** [@richardrx · 2026-02-02](https://x.com/richardrx/status/2018357024543715480)
