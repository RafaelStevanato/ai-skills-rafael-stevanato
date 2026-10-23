# AI-Era Differentiation & Moats

Attribution: principles by Richard ([@richardrx](https://x.com/richardrx), "Richard — Design for startups"), translated from Portuguese. License terms: see [LICENSE](../LICENSE).

- Treat each entry as one reusable principle.
- Follow the Source link of each entry to read the original post.
- Find the workflow and core rules in [SKILL.md](../SKILL.md).

## Faster building doesn't fix churn — activation does

**Principle:**
- Build speed was never the bottleneck.
- Shipping the same confusing interface faster is a more efficient route to churn.
- The real gap is the space between a user entering the product and understanding what to do.

**Apply when:**
- Vibe coding is sold to a founder as "the product got cheaper to build".
- The team equates speed with progress.

**Do:**
- Obsess over activation, not velocity.
- Attack the three things vibe coding never touches: onboarding, attention hierarchy, and value delivery in the first sessions (TTV).
- Close the entry-to-understanding gap, because more products now compete for the same user attention.

**Quote:** "Build speed without an obsession for activation is just a more efficient way to reach churn."

**Source:** [@richardrx · 2026-04-02](https://x.com/richardrx/status/2039685818273378644)

## Same engine, different UX: don't compete on the commodity

**Principle:**
- Treat the AI-built codebase as a near-commodity.
- Know that under the hood ~90% of new tools call the same APIs.
- Use engineering to solve the base function.
- Use design and packaging to differentiate and to resist copying.

**Apply when:**
- Your "engine" is effectively identical to a competitor's.
- A generic interface is pulling you into a price war.

**Do:**
- Win on UX architecture, not on the engine.
- Build superior UX with three effects:
  1. Remove initial friction. This lifts conversion.
  2. Fit the user's workflow. This cuts churn and raises LTV.
  3. Ease continuous/collaborative use. This enables upsell.
- Use this UX to build a differentiator that lowers copy risk and keeps the customer paying.

**Evidence:**
- VW Up, Seat Mii, and Skoda Citigo share the exact same platform: chassis, drivetrain, and the identical EA211 engine.
- Each car is designed and packaged for a different ICP (young, pragmatic-utility, reliability).

**Quote:** "The engine may be identical, but it's the architecture of the user experience that builds your moat."

**Source:** [@richardrx · 2026-03-03](https://x.com/richardrx/status/2028837448717926518)

## A validated idea is a short-term game — plan the moat

**Principle:**
- Treat a codebase-only advantage as a validated MVP that better-funded competitors can execute.
- Plan structural barriers to entry (the moat).
- Never leave the moat to accident.

**Apply when:**
- Your tech is easy to replicate.
- The product identity is generic.
- Clones can ship within days.

**Do:**
- Plan three deliberate moats:
  1. Brand Power: build a proprietary visual identity with above-average UX signals. It signals less risk and sells perceived safety (conversion).
  2. Switching cost via UX: build intuitive flows that users have internalized. They make moving to a 20%-cheaper clone costly in productivity (retention).
  3. Expansion architecture: build internal network effects (invite-to-collaborate). They are harder to copy and pull in new users (LTV).
- Expect users who perceive a value ecosystem to prefer paying more over adapting to a worse, cheaper product.

**Evidence:**
- The "Roast My Startup" tool was cloned within a week.
- Copies flooded the timeline.
- Read this as proof that a codebase-only edge is no defense.

**Quote:** "Clones can't copy trust."

**Source:** [@richardrx · 2026-03-03](https://x.com/richardrx/status/2028777831233114152)

## Design for shrinking attention spans

**Principle:**
- Treat short-form video as a variable-reward slot machine for the brain.
- It switches off the attention filter and erodes self-control.
- It leaves users with high anxiety and low focus.
- Make design militarily focused if your user's attention keeps shrinking.

**Apply when:**
- You build any product whose users are conditioned by infinite short-video feeds (attention economy).

**Do:**
- Engineer for the attention limit with three rules:
  1. Drastically reduce cognitive load.
  2. Direct the interface absolutely toward the target task (conversion).
  3. Build interfaces that respect the human attention ceiling.

**Evidence:**
- An EEG study (Fabiano et al., Frontiers in Human Neuroscience) links short-form-video addiction to reduced frontal-lobe activity and weakened ability to focus.

**Quote:** "TikTok is the hot dog of social media — hyper-palatable, but nutrient-poor: you consume endlessly and it never nourishes you."

**Source:** [@richardrx · 2026-02-26](https://x.com/richardrx/status/2026978144343687177)

## Sell the value, not the feature list — and show the product

**Principle:**
- Expect AI to auto-generate landing pages.
- Expect ~90% of them to share the same defects.
- Blame a generic, inconsistent hero for lost visitors.
- Never blame the absence of fancy design for lost visitors.

**Apply when:**
- You audit an AI-generated LP that leans on features and trendy gradients instead of the user's pain.

**Do:**
- Fix the three recurring failures:
  1. Generic, inconsistent aesthetics (every component a different color, purple/green gradients on dark/white).
  2. Over-indexing on features instead of the value/pain they address.
  3. Barely showing the actual product.
- Build the hero to pass the 5-second test: what does this do, why care, what next.

**Visual:** `../assets/2025246347587162602__q__1.jpg`
- The image shows Supafast's "SaaS Hero Section Formula".
- The image shows 5 elements with before/after copy.
- Apply the 5 elements:
  1. Write the Headline (≤8 words, attack the #1 pain).
  2. Write the Subheadline (show the transformation).
  3. Write the Primary CTA (specific to outcome).
  4. Write the Secondary CTA (low-commitment).
  5. Add the Trust Bar (5 logos or one specific number).

**Source:** [@richardrx · 2026-02-21](https://x.com/richardrx/status/2025246347587162602)

## Don't let AI-to-Figma-to-code factory technical debt

**Principle:**
- Know that a Claude → Figma → Code flow looks like speed.
- Know that it creates two documents that drift out of sync, plus inconsistent components.
- Treat the result as a maintenance Frankenstein, not velocity.

**Apply when:**
- A tool promises to round-trip AI output through the design canvas into code as a shortcut.

**Do:**
- Refuse the false shortcut.
- Expect generated components without a design system and context to be superficially similar but fundamentally inconsistent (random button padding, off-brand colors, inconsistent UX patterns).
- Expect manual tweaks not to flow back to code.
- Expect the source of truth to revert to the canvas, so the two files desync.
- Judge the flow useless for devs: V0/Lovable already emit code without the full-seat toll.
- Judge the flow a distraction for designers: it skips information architecture to spit out a screen fast.

**Quote:** "A technical-debt factory."

**Source:** [@richardrx · 2026-02-18](https://x.com/richardrx/status/2024076972565963186)

## Beat the four AI failure modes that make a vibe-coded SaaS feel like a fraud

**Principle:**
- Know that when the barrier to entry tends to zero, competition tends to infinity.
- Know that AI lowered that barrier and amplified Dunning-Kruger.
- Expect to feel omniscient while lacking the base to judge if AI output is a solution or wasted time.
- Know that you shipped code, not a seductive product, and you are diving into a red ocean.
- Treat code as one ingredient, not the asset.

**Apply when:**
- A "complete SaaS in a weekend" is validated but feels hollow, generic, and clonable by Wednesday.

**Do:**
- Fix the four pillars where AI fails.
- **1. Generic-product trap**
  - Know that AI is trained on the internet's average, and average builds nothing extraordinary.
  - Escape commoditization: build the only possible tool for an ignored niche.
  - Example: not "CRM for doctors" but "CRM for facial-harmonization clinics" with a `last_toxin_date` field and a 110-day retouch-alert cron.
- **2. Value delivery / TTV**
  - Never ship login → empty dashboard (the 99% default).
  - Build an on-ramp to value, an onboarding assistant, not a desert.
- **3. Trust / visual confidence**
  - Know that in a sea of V0/Tailwind templates, aesthetics, personality, and consistency are the last remaining trust proxies.
  - Use intentional, human-aligned pixels. They signal authority, build trust, and lower CAC.
- **4. Human touch**
  - Spend the time that cheaper code buys on the memorable details.
  - Write kind error messages.
  - Build a 404 that returns the user.
  - Write business logic that anticipates mistakes.
  - Add a 200ms confirming micro-interaction.
  - Know that humans are predictably irrational, full of bias.

**Evidence:**
- Johnson & Goldstein (2003), *Science*: a mere "opt-out" default produced +90% organ-donation consent.
- Read this as proof that small design choices move behavior.

**Visual:** `../assets/2013264068518289753__2.jpg`
- The image shows the Dunning-Kruger curve.
- Confidence spikes at "Ignorant" (low knowledge).
- Confidence craters at "Cultured".
- Confidence climbs toward "Expert".
- A labeled "confidence gap" marks the difference.

**Quote:** "You can own all the cement in the world, but without the blueprint and structural engineering you're just a pile of gray concrete."

**Source:** [@richardrx · 2026-01-19](https://x.com/richardrx/status/2013264068518289753)
