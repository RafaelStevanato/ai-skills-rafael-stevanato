# AI-Era Differentiation & Moats

Attribution: principles by Richard ([@richardrx](https://x.com/richardrx), "Richard — Design for startups"), translated from Portuguese. License: [LICENSE](../LICENSE).

## Faster building doesn't fix churn — activation does

**Principle:** Build speed was never the bottleneck. The real gap is between product entry and understanding what to do.

**Apply when:** Vibe coding is sold to a founder as "the product got cheaper to build," and the team equates speed with progress.

**Do:**
- Obsess over activation, not velocity.
- Attack the three things vibe coding never touches: onboarding, attention hierarchy, and value delivery in the first sessions (TTV).
- Close the entry-to-understanding gap. More products now compete for the same user attention.

**Quote:** "Build speed without an obsession for activation is just a more efficient way to reach churn."

**Source:** [@richardrx · 2026-04-02](https://x.com/richardrx/status/2039685818273378644)

## Same engine, different UX: don't compete on the commodity

**Principle:** AI turned the codebase into a near-commodity: under the hood ~90% of new tools call the same APIs. Engineering solves the base function; design and packaging differentiate.

**Apply when:** Your "engine" is effectively identical to a competitor's. A generic interface pulls you into a price war.

**Do:**
- Win on UX architecture, not the engine. Superior UX lowers copy risk and keeps the customer paying: remove initial friction (lifts conversion); fit the user's workflow (cuts churn, raises LTV); ease continuous/collaborative use (enables upsell).

**Evidence:** VW Up, Seat Mii, and Skoda Citigo share the exact same platform (chassis, drivetrain, identical EA211 engine). Each is designed and packaged for a different ICP (young, pragmatic-utility, reliability).

**Quote:** "The engine may be identical, but it's the architecture of the user experience that builds your moat."

**Source:** [@richardrx · 2026-03-03](https://x.com/richardrx/status/2028837448717926518)

## A validated idea is a short-term game — plan the moat

**Principle:** A codebase-only advantage is a validated MVP for better-funded competitors to execute.

**Apply when:** Your tech is easy to replicate and the product identity is generic. Clones can ship within days.

**Do:**
- Plan three deliberate moats (structural barriers to entry), never accidental ones:
  1. Brand Power (conversion): build a proprietary visual identity with above-average UX signals. It signals less risk and sells perceived safety.
  2. Switching cost via UX (retention): build intuitive flows that users have internalized. Moving to a 20%-cheaper clone then costs productivity.
  3. Expansion architecture (LTV): build internal network effects (invite-to-collaborate). They are harder to copy and pull in new users.
- Expect users who perceive a value ecosystem to pay more rather than adapt to a worse, cheaper product.

**Evidence:** The "Roast My Startup" tool was cloned within a week, and copies flooded the timeline.

**Quote:** "Clones can't copy trust."

**Source:** [@richardrx · 2026-03-03](https://x.com/richardrx/status/2028777831233114152)

## Design for shrinking attention spans

**Principle:** Short-form video acts on the brain like a variable-reward slot machine. It switches off the attention filter, erodes self-control, and leaves users with high anxiety and low focus.

**Apply when:** Your users are conditioned by infinite short-video feeds (attention economy).

**Do:**
- Engineer for the attention limit, with design militarily focused:
  1. Reduce cognitive load drastically.
  2. Direct the interface absolutely toward the target task (conversion).
  3. Build interfaces that respect the human attention ceiling.

**Evidence:** An EEG study (Fabiano et al., Frontiers in Human Neuroscience) links short-form-video addiction to reduced frontal-lobe activity and weakened ability to focus.

**Quote:** "TikTok is the hot dog of social media — hyper-palatable, but nutrient-poor: you consume endlessly and it never nourishes you."

**Source:** [@richardrx · 2026-02-26](https://x.com/richardrx/status/2026978144343687177)

## Sell the value, not the feature list — and show the product

**Principle:** ~90% of AI-generated landing pages share the same defects. A generic, inconsistent hero loses visitors, not the absence of fancy design.

**Apply when:** You audit an AI-generated LP that leans on features and trendy gradients instead of the user's pain.

**Do:**
- Fix the three recurring failures:
  1. Generic, inconsistent aesthetics (every component a different color, purple/green gradients on dark/white).
  2. Over-indexing on features instead of the value/pain they address.
  3. Barely showing the actual product.
- Build the hero to pass the 5-second test: what does this do, why care, what next.

**Visual:** Supafast's "SaaS Hero Section Formula": 5 elements with before/after copy: Headline (≤8 words, attack the #1 pain); Subheadline (show the transformation); Primary CTA (specific to outcome); Secondary CTA (low-commitment); Trust Bar (5 logos or one specific number). (`../assets/2025246347587162602__q__1.jpg`)

**Source:** [@richardrx · 2026-02-21](https://x.com/richardrx/status/2025246347587162602)

## Don't let AI-to-Figma-to-code factory technical debt

**Principle:** A Claude → Figma → Code flow looks like speed but is a maintenance Frankenstein, not velocity.

**Apply when:** A tool promises to round-trip AI output through the design canvas into code as a shortcut.

**Do:**
- Refuse the false shortcut.
- Expect components generated without a design system and context to be superficially similar but fundamentally inconsistent (random button padding, off-brand colors, inconsistent UX patterns).
- Expect manual tweaks not to flow back to code: the source of truth reverts to the canvas, so the two files desync.
- Judge the flow useless for devs: V0/Lovable already emit code without the full-seat toll.
- Judge the flow a distraction for designers: it skips information architecture to spit out a screen fast.

**Quote:** "A technical-debt factory."

**Source:** [@richardrx · 2026-02-18](https://x.com/richardrx/status/2024076972565963186)

## Beat the four AI failure modes that make a vibe-coded SaaS feel like a fraud

**Principle:** When the barrier to entry tends to zero, competition tends to infinity (red ocean). AI lowered that barrier and amplified Dunning-Kruger: you feel omniscient but cannot judge if AI output is a solution or wasted time. You shipped code, not a seductive product. Code is one ingredient, not the asset.

**Apply when:** A "complete SaaS in a weekend" is validated but feels hollow, generic, and clonable by Wednesday.

**Do:** Fix the four pillars where AI fails.
1. **Generic-product trap.** AI trains on the internet's average, which builds nothing extraordinary. Escape commoditization with the only possible tool for an ignored niche. Example: not "CRM for doctors" but "CRM for facial-harmonization clinics" with a `last_toxin_date` field and a 110-day retouch-alert cron.
2. **Value delivery / TTV.** Never ship login → empty dashboard (the 99% default). Build an on-ramp to value, an onboarding assistant, not a desert.
3. **Trust / visual confidence.** In a sea of V0/Tailwind templates, aesthetics, personality, and consistency are the last remaining trust proxies. Use intentional, human-aligned pixels: they signal authority, build trust, and lower CAC.
4. **Human touch.** Spend the time that cheaper code buys on memorable details: kind error messages, a 404 that returns the user, business logic that anticipates mistakes, a 200ms confirming micro-interaction. Humans are predictably irrational, full of bias.

**Evidence:** Johnson & Goldstein (2003), *Science*: a mere "opt-out" default produced +90% organ-donation consent. Small design choices move behavior.

**Visual:** The Dunning-Kruger curve: confidence spikes at "Ignorant" (low knowledge), craters at "Cultured," and climbs toward "Expert," with a labeled "confidence gap". (`../assets/2013264068518289753__2.jpg`)

**Quote:** "You can own all the cement in the world, but without the blueprint and structural engineering you're just a pile of gray concrete."

**Source:** [@richardrx · 2026-01-19](https://x.com/richardrx/status/2013264068518289753)
