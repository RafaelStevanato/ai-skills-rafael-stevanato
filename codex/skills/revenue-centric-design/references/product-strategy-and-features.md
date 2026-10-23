# Product Strategy & Feature Discipline

Contents: Feature requests from cancellations don't buy features · Building is the comfort zone; distribution is the game · 94% of features are filler — Pendo's data and what to do about it · PMF is step 8 in a 10-step sequence — founders start there too early · Feature creep ("fiturite") is a business cost, not just a UX one · Maturing the product means doing the same thing better, not adding power-user features · Run every feature through a two-layer "Swiss Knife filter" before building · Feature adoption is a design problem, not a communication problem · Compute your Swiss Knife Index to expose feature creep · Design the attention hierarchy to direct behavior, not just organize info · Ground feature discipline in the academic feature-fatigue research · Past the optimal feature count, a technically bigger product becomes functionally worse · Focus on your core; trying to be "all-in-one" dilutes your value proposition

Attribution: Richard ([@richardrx](https://x.com/richardrx)), "Richard — Design for startups", translated from Portuguese. License: [LICENSE](../LICENSE).

## Feature requests from cancellations don't buy features

Three auto shops canceled RepareCar over missing boleto (bank-slip) issuance. The request is logged in Linear with name and date; 20+ requests sit in the same queue, oldest since June. Cancellation does not buy a feature: the ICP is defined, and boleto sits in a deliberately-not-doing package. Support is semi-automated: AI triages, a human answers novel questions, both open Linear tickets, and a daily Claude task prioritizes. Bugs jump the queue.

**Apply when:** Cancelling customers' feature requests pressure the roadmap.

**Do:**
- Log each request with the customer and date, and aggregate demand.
- Prioritize by bug severity, ICP fit, and strategy. Never prioritize by the latest cancellation.
- Default net-new work to the parking lot.
- When asked for timing, state the real queue ("20 requests are ahead of yours"). Never make a false promise.

**Source:** [@richardrx · 2026-08-10](https://x.com/richardrx/status/2086931878251057479)

## Building is the comfort zone; distribution is the game

Founders build because selling hurts. Richard spent 90% of his time perfecting a delivery product one year before iFood existed. It died beautiful. Humane raised ~US$240M with ex-Apple founders and gorgeous hardware. Returns outpaced sales by summer 2024. HP took the assets for US$116M. In the survival phase you do both jobs, almost always pick building (your comfort zone), and pretend the next feature will make selling easier.

**Apply when:** Roadmap keeps growing while distribution is untested.

**Do:**
- Before every survival-phase roadmap item, ask: how many months of runway does this feature cost?
- Ask whether the feature makes selling easier or only postpones selling.
- If the honest answer is "it's the comfortable thing to build," spend that time on the job that hurts: selling.

**Source:** [@richardrx · 2026-07-21](https://x.com/richardrx/status/2079575881115226453)

## 94% of features are filler — Pendo's data and what to do about it

Pendo analyzed apps across ~2,500 companies. The average product reaches roughly 6% feature adoption; top-10% products reach only 15.6%. So about 94% of features are rarely or never used (84.4% even in the top decile). Unused features cause low activation, churn, a larger attack surface, and higher sustaining cost and complexity. Some features sell without use, but that does not explain the gap.

**Apply when:** Auditing a bloated roadmap or justifying a feature purge.

**Do:**
- Classify every feature by usage correlation:
  - A. Core: the 6% carrying the product (15% if you're top-10%).
  - B. Strategic: contributes to sales.
  - C. Discard.
- Shrink the product based on use and/or cash generation.

**Source:** [@richardrx · 2026-07-17](https://x.com/richardrx/status/2078079228717764886)

## PMF is step 8 in a 10-step sequence — founders start there too early

Run this sequence in order:
1. Define the ICP: does it really exist, or is it who you wish it were?
2. Surface the ICP's pains and desires: real? verified where, with how many?
3. Understand awareness level: knows the pain? the solution? yours?
4. Slice niche/sub-niche: their particularities, do they exclude each other?
5. Size TAM of niche and sub: enough market, and does enough remain after niching?
6. Actively decide who the solution serves: can you stand out there?
7. Validate the thesis: the ICP's pain solved in a way that pays; are they paying?
8. Reach PMF: does the product stick? do users recommend it unprompted? does the business sustain itself without you pushing?
9. Fix inefficiencies in acquisition, activation, retention: always leaks; measured where?
10. Scale.

**Apply when:** A founder says they "want PMF" without the groundwork.

**Do:**
- Require evidence at each gate: a verified ICP and pain, a viable niche/TAM, paying thesis validation, then PMF.
- Scale only after you measure and fix acquisition, activation, and retention leaks.

**Source:** [@richardrx · 2026-07-09](https://x.com/richardrx/status/2075192130184630688)

## Feature creep ("fiturite") is a business cost, not just a UX one

The Homer Simpson car problem: every unsatisfied user request implemented as a feature eventually makes the product hard to operate. It steepens the learning curve and worsens experience through cognitive overload and choice paradox. It also costs the business: more dev spend on features serving few users, more maintenance, and whole teams for barely-needed areas.

**Apply when:** A product keeps growing features without a subtraction ritual.

**Do:**
- Prune with four questions: who are our most strategic users? What are they using? What's unused that I can abstract? What aligns with the vision?
- Treat pruning as a cost line: grass grows by itself, you have to mow.
- Cut low-usage features that serve low-paying or high-churn subniches. Serve better those who pay more and stay longer.

**Source:** [@richardrx · 2025-11-03](https://x.com/richardrx/status/1985329704312709254) and [@richardrx · 2026-07-06](https://x.com/richardrx/status/2074118439321350163)

## Maturing the product means doing the same thing better, not adding power-user features

Technical founders keep densifying the product for heavy users. It becomes a Boeing 747 cockpit: expensive, complex, and hard for the average user. Maturing means doing better what the product already does. Hidden risk: a power-user product has a smaller top of funnel, so you must charge more. You changed markets (TAM/SAM changed): price must follow. The founder then reads "product is bad" when the ICP is not adjusted.

**Apply when:** The product keeps getting denser and conversion falls.

**Do:**
- Stop adding depth by default. Mature the product first: smoother flows, bug fixes, attention direction.
- If the product deliberately moves upmarket, recalculate TAM/SAM and price. Then align the ICP, copy, visuals, and detail quality with that smaller, higher-value market:
  - Copy: more executive, less tool-like.
  - Visuals: show the result, less product internals.
  - Detail care: a high-paying ICP tolerates AI-slop design less.

**Evidence:** Christoph Janz's five paths to $100M run from the elephant (few customers paying a lot) to the fly (millions paying little). All five work. The problem is becoming an elephant without noticing and still charging mouse prices.

**Source:** [@richardrx · 2026-07-02](https://x.com/richardrx/status/2072718071060447691)

## Run every feature through a two-layer "Swiss Knife filter" before building

A shipped feature stays forever and charges rent forever. Never ask "is this good?". Ask "does it deserve the permanent cost it imposes on the product?"

**Apply when:** A roadmap item feels appealing but nobody applied a filter before committing to build.

**Do:**
- Layer 1, does it deserve to exist? Pass all four:
  1. Cognitive load: more surface = more to learn + Hick's law decision time.
  2. ICP specificity: a CRM for facial-aesthetics clinics charges 5x a generic one.
  3. Operational cost: maintain/support/document, not build.
  4. Reinforces the core claim.
- Fail any one: kill the feature guilt-free.
- Layer 2, build now? Score two axes: easily rejectable (is there a clear "no"?) and easily implementable (cost to the validating version, not the dream version).
- Build the no-brainers first.
- Rank survivors by (New Users + New Revenue + Impact Level) / Effort.

**Visual:** Prioritization scoring table with that score formula — `../assets/2059236567533650119__1.jpg`

**Quote:** "Every feature that gets in, stays. And it charges rent forever."

**Source:** [@richardrx · 2026-05-26](https://x.com/richardrx/status/2059236567533650119)

## Feature adoption is a design problem, not a communication problem

Shipping a feature does not make users discover it. Users follow their habitual path and never see what they aren't looking for. Two killers: inattentional blindness and status-quo bias (re-learning cost outweighs perceived benefit, even when the new way is better).

**Apply when:** Three weeks post-launch only ~9% of active users opened the feature and ~4% used it twice, despite changelog, email, and "new" badges.

**Do:**
- Stop treating adoption as announcement.
- Use directional empty states that surface the feature where users need it.
- Use triggered onboarding fired by the behavior that signals need (CRM user hits the sales page → introduce the objection-busting AI).
- Track a feature adoption rate that measures habit/appropriate frequency, not clicks.
- Send any feature below an adoption threshold back into review.

**Quote:** "Launching a feature is easy; getting it used is a whole other thing."

**Source:** [@richardrx · 2026-05-20](https://x.com/richardrx/status/2057162392048476345)

## Compute your Swiss Knife Index to expose feature creep

Measure a product's worth by features actually used, not features shipped. A bloated product is expensive to sustain and hard to sell, not rich.

**Apply when:** The roadmap has become a user wishlist and every new feature feels like progress (especially with AI making building cheap).

**Do:**
- Compute: Swiss Knife Index (SKI) = (features used by >40% of active users in a 30-day window) ÷ (total features).
- Flag SKI below 0.3: you own a clumsy Swiss army knife.
- Audit quarterly on real usage data, not team opinion.
- Hide, don't delete: push rarely-used features into advanced settings (reachable for the 3%, gone for the 97%).
- Gate every new feature: "which existing feature do I kill to make cognitive room?"
- Litmus test: which feature would you show first with 30 seconds to sell? Keep the rest invisible until needed.
- Read [the academic grounding](#ground-feature-discipline-in-the-academic-feature-fatigue-research) and [the curve](#past-the-optimal-feature-count-a-technically-bigger-product-becomes-functionally-worse).

**Visual:** SKI curve — perceived utility rises then declines past the optimal point as complexity keeps climbing — `../assets/2057124008445796659__1.jpg`

**Quote:** "Which feature would I show first if I had 30 seconds to sell the product?"

**Source:** [@richardrx · 2026-05-20](https://x.com/richardrx/status/2057124008445796659)

## Design the attention hierarchy to direct behavior, not just organize info

A product that organizes delivers access; a product that directs delivers activation. The visual hierarchy decides which one the user gets. Attention hierarchy decides what users see first, find with effort, or never discover. Built without intent, it makes the product sabotage itself: users use what is most salient, which is rarely what retains.

**Apply when:** "My interface looks good, but people don't use the main features" and the key feature is buried behind three clicks the user will never make.

**Do:**
- Plan the hierarchy to influence behavior: make the value-driving, retention-driving feature the most prominent thing. Never only arrange information neatly.

**Visual:** A typographic demo (huge headline "YOU WILL READ THIS FIRST") proving the eye follows visual weight, not reading order — `../assets/2039399756452057159__1.jpg`

**Quote:** "A well-designed attention hierarchy makes the user use what retains; a bad one makes them use what's most salient."

**Source:** [@richardrx · 2026-04-01](https://x.com/richardrx/status/2039399756452057159)

## Ground feature discipline in the academic feature-fatigue research

Past a cognitive-load threshold, the subjective evaluation of a product does not stay neutral. It declines into frustration, confusion, and task abandonment, hitting CAC and LTV directly. More features help pre-purchase comparison via distinction bias but hurt the decision via analysis paralysis: more options = longer decisions and more no-decisions, and no decision means no conversion. Each extra feature steepens the learning curve (measurable B2B productivity loss). When value comes slowly, users silently churn before the trial ends, blaming themselves, not the product.

**Apply when:** You need the evidence behind cutting features, or want to separate pre-purchase appeal from post-purchase utility.

**Do:**
- Apply the SKI as a decision criterion grounded in feature fatigue. Read with [the index](#compute-your-swiss-knife-index-to-expose-feature-creep) and [the curve](#past-the-optimal-feature-count-a-technically-bigger-product-becomes-functionally-worse).

**Evidence:** Thompson, Hamilton & Rust (2005), "Feature Fatigue," JMR 42(4); distinction bias (Hsee & Zhang 2004); analysis paralysis (Iyengar & Lepper 2000).

**Quote:** "A product that grows without criteria doesn't get rich — it gets expensive to sustain and hard to sell."

**Source:** [@richardrx · 2026-03-18](https://x.com/richardrx/status/2034248739557159293)

## Past the optimal feature count, a technically bigger product becomes functionally worse

Feature count and perceived utility relate non-linearly. An optimal point exists; after it, each added feature reduces perceived utility and raises sustaining cost and the learning curve.

**Apply when:** You hear "my interface looks good, but people don't use the main features", a sign you passed the optimal point.

**Do:**
- Read the SKI curve: utility peaks (~10 features in the example), then falls as complexity keeps rising.
- Reduce cognitive load so the rest becomes visible again. More visibility is not the fix.
- Flag any feature used by under 10% of the active base. Make it justify its existence or leave.
- Never assume a universal ideal feature count. Find the ideal only for your ICP, context, and device.

**Visual:** SKI graph: green perceived-utility curve peaks at the optimal point (10.3 features, 97), red complexity curve rises monotonically and overtakes utility in the "decline zone" — `../assets/2033880553607364684__1.jpg`

**Quote:** "A bloated product isn't a rich product — it's a product actively destroying the conversion and retention you paid dearly to win."

**Source:** [@richardrx · 2026-03-17](https://x.com/richardrx/status/2033880553607364684)

## Focus on your core; trying to be "all-in-one" dilutes your value proposition

Chasing a bigger TAM by going generic destroys heavy-user retention and does not convert new users. The same roadmap mistake happens in cars and in software. When UI/UX tries to cover everything, the value proposition dilutes.

**Apply when:** The product is tempted to "embrace the world" and become a do-everything tool, abandoning the specific ICP that made it loved.

**Do:**
- Remember who your ICP is. Build for the ICP, even at the expense of broad appeal. Focus relentlessly on the core.

**Evidence:** Porsche chased China's TAM with generic EVs, abandoning its ICP (visceral flat-six machines). It lost ~€3.9B reversing the roadmap. Operating profit fell from €4,000M (2022) to €40M (9M 2025), margin 18% → 0.2%. [Porsche figures from the quoted post; treat as illustrative.]

**Quote:** "Focus on your damn core."

**Source:** [@richardrx · 2026-03-11](https://x.com/richardrx/status/2031722047080960265)
