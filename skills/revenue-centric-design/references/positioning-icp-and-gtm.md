# Positioning, ICP & Go-to-Market

Attribution: Richard (@richardrx), "Richard — Design for startups", translated from Portuguese.
Each entry links to its source post.
Return to [SKILL.md](../SKILL.md).
Related files: [conversion-and-landing-pages.md](conversion-and-landing-pages.md), [churn-and-retention.md](churn-and-retention.md), [onboarding-and-activation.md](onboarding-and-activation.md), [metrics-and-experimentation.md](metrics-and-experimentation.md).
Related script: [revenue_math.py](../scripts/revenue_math.py).

## Size the market with TAM → SAM → SOM (and know which one matters)

**Principle:**
- Size the real market. It is far smaller than the population.
- Treat TAM as a theoretical ceiling.
- Example: Brazil's 213M becomes ~101M credit-card holders for a paid app.
- Expect investors to often ignore a TAM under ~R$1B.
- Optimize the number that matters: the **SOM**, what you can actually capture.

**Apply when:**
- Size a market.
- Write a deck.
- Judge whether a niche is big enough.

**Do:**
- Define TAM as the total addressable ceiling.
- Define **SAM** as the realistic slice your model reaches (~40% in his example).
- Define **SOM** as the 1–5% you truly win in ~36 months.
- Derive SOM from real CAC, activation, support capacity and LTV.
- Never set SOM as a guessed %.
- Never try to change your TAM.
- Change how much of your SAM you convert and retain.

**Evidence:**
- RepareCar: ~76k mechanic shops (honest TAM) → SAM ~47k → ~3% ≈ 1,414 shops ≈ R$1.6M ARR.
- RepareCar current pace: ~10 shops/day ≈ 7% of SAM in 12 months.

**Visual:** TAM/SAM/SOM concentric-circle diagram with definitions — `../assets/2070140923380420796__1.jpg`

**Source:** [@richardrx · 2026-06-25](https://x.com/richardrx/status/2070140923380420796)

## Frame the referral prize as a gift to the friend, not a commission to the referrer

**Principle:**
- Win member-get-member (MGM) referral programs on framing and timing.
- A two-sided reward alone is not enough.
- Money makes the exchange feel transactional.
- An in-product benefit feels like a genuine gift.

**Apply when:**
- Design or fix a referral program.
- Stop when you default to "refer a friend, get $20."

**Do:**
- Apply the framing effect: surface the prize on the receiver's side ("João gave you 500MB").
- Ask for the referral at the peak of value.
- Peak of value: right after a concrete win, or when the user hits a limit.
- Avoid cash.
- Give a reward that deepens use of your own product.
- Embed the referral as continuous in-product operation.
- Never run the referral as a one-off campaign.
- Caveat: referral amplifies a product people already love.
- Never use referral to fix a product nobody recommends for free.

**Evidence:**
- Dropbox grew 3900% in 15 months (100k → 4M users).
- Dropbox peaked near 3M invites in a single month.
- ~1/3 of Dropbox users already arrived via word-of-mouth before the program.

**Quote:** "A referral amplifies a product people already love — it doesn't fix a product nobody recommends for free."

**Source:** [@richardrx · 2026-06-02](https://x.com/richardrx/status/2061766945582559509)

## Pick a deliberately under-served niche as your ICP

**Principle:**
- A clear ICP (ideal customer profile) is not "everyone who could use my product."
- Choose a deliberately under-served niche as your ICP.
- A sharp niche beats no niche.
- You cannot out-fight the entrenched generalist giant.

**Apply when:**
- You have early traction.
- You feel tempted to "embrace the world" out of fear of a small TAM.

**Do:**
- Validate four ICP filters.
- Filter 1: the segment feels the pain with real weight.
- Pain is proportional to what is lost when the problem stays unsolved.
- Example: a lost lead costs a face-aesthetics clinic R$3,000 vs. R$60 for a barber.
- Filter 2: the TAM is big enough to sustain operations.
- Filter 3: the segment has money to pay your required ticket, so unit economics close.
- Filter 4: founder-fit.
- Founder-fit gives native language, a fast validation network, and instinct that money can't buy.
- With a clear ICP, failure has a diagnosis ("I got the messaging wrong").
- Without a clear ICP, you can't tell if product, copy, channel, price, or audience failed.
- Without a clear ICP, every test burns runway.

**Quote:** "A generalist ERP is hard to sell; an ERP for cabinetmaking is a different conversation."

**Source:** [@richardrx · 2026-05-19](https://x.com/richardrx/status/2056789797646029232)

## Don't claim PLG without the four structural conditions

**Principle:**
- Treat product-led growth (PLG) as a consequence of structural conditions.
- PLG is not a product decision you declare.
- Most B2B SaaS that pitches PLG is really sales-led wearing a PLG label.

**Apply when:**
- You write a pitch deck or strategy and call the motion "self-service" / PLG.

**Do:**
- Require all four conditions before you claim PLG.
- Condition 1: TTV < 10 minutes.
- If the product needs a consultant demo, API support, or paid implementation, it is not PLG.
- Tell: full trial, zero activation.
- Condition 2: ticket below ~R$1,000.
- A higher ticket means a buying committee.
- Condition 3: native virality or collaboration.
- Notion, Figma, Slack pull users in.
- A CRM/AI tool needs SDRs, demos, follow-up.
- Condition 4: a huge addressable market with a real bottom-up TAM.
- If you fail these conditions, run sales-led honestly.

**Evidence:**
- Brazil has ~20,000 companies with 100+ employees.
- Only ~a dozen B2B SaaS where PLG makes real economic sense.

**Quote:** "Founders love PLG because it seems to delete the part they don't master — selling."

**Source:** [@richardrx · 2026-05-04](https://x.com/richardrx/status/2051262752547536941)

## Charge your first ten users from day one

**Principle:**
- The first ten users define the product's entire curve.
- Payment is the cheapest test of real pain.
- Curiosity is free.
- An open wallet demands a concrete problem.

**Apply when:**
- You validate a new product.
- You feel tempted to give early access away to "build a base."

**Do:**
- Source the first ten users from closed communities, personal reach, or pure guerrilla.
- Charge even while the product is a prototype.
- When someone says they can't pay, ask directly: "What does the system need to do for you to pay right now?"
- Treat the payment friction as part of the test.
- Collect dense feedback.
- Start visual design only after ~20 paying users.
- For B2C apps, shift the method (e.g., pre-sale of a solution-in-progress).
- Keep the principle for B2C apps.

**Evidence:**
- RepareCar's first 25 auto shops tested the product in prototype.
- The team visited each shop and charged at the end.
- The team designed visuals only after 20 paying shops.

**Quote:** "Curiosity is free; an open wallet demands a concrete problem."

**Source:** [@richardrx · 2026-04-26](https://x.com/richardrx/status/2048359526487716333)

## Reverse-engineer the funnel math before celebrating an MRR target

**Principle:**
- Building the product is the easy part.
- Distribution is the game.
- Treat a revenue target as a traffic-and-retention problem.
- Churn quietly resets the whole funnel every month.

**Apply when:**
- Someone asks "is it hard to hit X MRR?"
- You size acquisition for a target customer count.

**Do:**
- Work backwards from the target.
- To net 2,500 customers at 5% LP conversion, you need 50,000 visitors.
- From ads at 3% creative CTR, you need ~1.6M impressions.
- Treat 5% and 3% as top-decile.
- Expect most to land at 1–2% LP and under 1% CTR, so you test dozens.
- Then add the leaky bucket.
- At 20% monthly churn, average customer life is 5 months.
- At 20% monthly churn, you replace 500 customers every month forever just to stand still (≈10,000 visitors / 333,000 impressions).
- Assign the problem to dev, design, and marketing together.
- No single function owns it.

**Evidence:**
- 20% monthly churn → 5-month average lifetime.
- At low ticket, many operate at 40–50% churn, so "the bucket never fills."

**Quote:** "Building the product is the easy part; distribution is the game."

**Source:** [@richardrx · 2026-04-20](https://x.com/richardrx/status/2046222319912132977)

## Concentrate channels with the Bullseye framework, not scattershot testing

**Principle:**
- Testing ten channels at once hides what drove results.
- You blame the channel when the business stalls.
- Prioritize distribution with focus.
- A perfect channel still fails if the receiving structure leaks.

**Apply when:**
- You spread content and traffic across many channels with no clear read on what works.

**Do:**
- Use the Bullseye framework (from the book *Traction*): three rings of priority.
- Inner ring: at most three highest-potential channels, with total focus.
- Middle ring: up to six channels you probe with small experiments.
- Outer ring: everything plausible long-term, no active focus now.
- Choose between channels with an ICE Score (Impact, Confidence, Ease, each 0–10, divide by 3, prioritize).
- Close the gap the book skips: never scale distribution onto a broken reception structure (LP, onboarding, first product steps).
- Scaling onto a broken reception structure yields no growth.
- Run distribution and retention simultaneously, not sequentially.

**Visual:** Bullseye as nested circles — What's Possible → What's Probable → What's Working — beside a "Marketing Framework for Startups" triangle (Prioritization, Testing, Quick Iteration). — `../assets/2036035304868434115__1.jpg`

**Source:** [@richardrx · 2026-03-23](https://x.com/richardrx/status/2036035304868434115)

## Diagnose the bottleneck: no entries is distribution, leaving without paying is design

**Principle:**
- Design cannot save a "ghost product."
- Design optimizes and raises the LTV of something that already has traffic.
- Design cannot manufacture demand.

**Apply when:**
- A builder ships an app, gets near-zero users, and hopes a redesign will rescue it.

**Do:**
- Split the diagnosis cleanly.
- If nobody enters your product, treat it as a distribution problem.
- If users enter, don't pay, and leave, treat it as a design problem.
- Read *Traction*, even if you can afford an agency or a marketing team.
- Check each channel's awareness level, not only cost-per-channel.
- Awareness level drives different conversion and retention behavior, depending on where and how the user arrived.

**Quote:** "If nobody enters your product, it's distribution. If they enter, don't pay, and leave, that's design."

**Source:** [@richardrx · 2026-02-28](https://x.com/richardrx/status/2027721170569564521)
