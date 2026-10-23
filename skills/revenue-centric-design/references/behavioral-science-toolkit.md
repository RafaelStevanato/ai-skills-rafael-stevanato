# Behavioral Science & Persuasion

Attribution: principles by Richard ([@richardrx](https://x.com/richardrx), "Richard — Design for startups"), translated from Portuguese. License terms: see [LICENSE](../LICENSE).

- Treat each entry as one reusable principle.
- Follow the Source link of each entry to read the original post.
- Find the workflow and core rules in [SKILL.md](../SKILL.md).
- Entry labels: **Apply when** = trigger condition. **Do** = rules. **Evidence** = data. **Visual** = image description and path. **Quote** = Richard's words, verbatim. **Source** = original post.

## You can't un-hear your own product

**Principle:**
- Know that product knowledge permanently rewrites your perception.
- Know that what feels obvious to you is just "tap-tap-tap" to a first-time user.
- Never mistake confused users for dumb users.

**Apply when:**
- You think onboarding is unnecessary because "the product is simple".
- A question your support answers weekly seems already answered on screen.

**Do:**
- Treat this bias as the curse of knowledge. You cannot switch the music off.
- Collect feedback from people who have never seen the product.
- Never steer these people. Never name things for them.
- Watch behavior.
- Run this collection continuously.
- Use support/CX as an insight collector.
- Tabulate each issue by %, impact, insight.
- Use Clarity/PostHog for heatmaps and session replays.
- Run sampled user interviews.
- Run competitor benchmarking.

**Evidence:**
- Tapping-vs-listening study: tappers hear the full song in their head. Listeners only get the taps.
- Listeners guessed 3 of 120 songs correctly (2.5%).
- This result is far below tappers' expectations.

**Quote:** "You're humming the whole song in your head; your user only hears 'tap, tap, tap.'"

**Source:** [@richardrx · 2026-06-04](https://x.com/richardrx/status/2062509937037590997)

## Set the default — it's the most underrated lever in conversion

**Principle:**
- The pre-selected option captures the overwhelming majority of choices.
- Deciding is expensive. The lazy brain takes the easiest path.
- Smart defaults beat copy persuasion.

**Apply when:**
- The user must make any choice: pricing tier, billing cadence, seat count, notifications, checkout.
- Apply it before you spend hours rewriting CTAs.

**Do:**
- Exploit status-quo bias plus cognitive-load reduction.
- Pre-select the mid-tier you want to sell. The default takes 60–80% of choices.
- Default billing to annual. This lifts contracted MRR without changing price.
- Start the seat selector at your ICP's typical count (anchoring).
- Run a reverse trial: premium is the default and free is the opt-out.
- Make the user actively give up what they already have.
- Rule 1: Keep defaults ethically defensible. Checkbox tricks become churn and complaints.
- Rule 2: Prefer smart defaults over copy.
- Rule 3: Accept that the user will not burn energy on what is trivial to you. Set the default for it.

**Evidence:**
- Organ-donor study (Science, 2003): opt-out countries register ~6× more donors than opt-in.
- Germany (opt-in) ~12% vs Austria (opt-out) ~100%.
- Culture and religion do not explain it. It is a pre-checked box.
- Richard raised average ticket 60% when he applied this to plan acquisition.
- Richard saw up to 4× LTV when he applied this to plan acquisition.

**Visual:** Bar chart of effective organ-donor consent by country: opt-in nations low (Denmark 4.25%, Germany 12%, UK 17.17%, Netherlands 27.5%) vs opt-out nations ~100% (Austria, France, Hungary, Portugal). — `../assets/2057872036718899256__1.jpg`

**Quote:** "You can spend the rest of your life optimizing copy, or you can change 5 defaults over the weekend."

**Source:** [@richardrx · 2026-05-22](https://x.com/richardrx/status/2057872036718899256)

## Reinforce the decision the user just made

**Principle:**
- After a commitment, people actively seek information that supports their choice.
- This is choice-supportive bias.
- Feed that need to make the decision feel right.

**Apply when:**
- The user just completed a signup, a purchase, or any meaningful commitment.
- Buyer's remorse or doubt could creep in.

**Do:**
- Use choice-supportive bias deliberately.
- Send a strong welcome email with clear next steps.
- Make the new user feel embraced and validated for choosing you.
- Analogy: someone joins an EV-lovers group right after buying the car.

**Source:** [@richardrx · 2026-04-29](https://x.com/richardrx/status/2049392897598849333)

## Architect for what users fear losing, not just what they gain

**Principle:**
- Builders obsess over features (gains).
- What the user fears losing cements conversion and retention.
- The pain of abandoning a built-up ecosystem outweighs the pain of paying a subscription.

**Apply when:**
- You design trials, retention/renewal flows, and offboarding.
- Users of the product accumulate data, history, or workflows.

**Do:**
- Exploit loss aversion and sunk cost.
- Convert with zero risk: let users import real competitor data in shadow mode.
- Let users test without fear.
- Retain users: design the product so users build workflows and accumulate history from day 1.
- At renewal, the user then weighs the headache of rebuilding from scratch, not the monthly fee.
- At offboarding, never add friction.
- Make cancellation easy.
- Make the loss tangible (e.g., "You'll instantly lose 41 active automations and 6 months of data").

**Evidence:**
- Sunk cost is what keeps many users on certain LLMs.
- The cause is fear of losing your memory/history, even when it could be exported with a copy/paste.

**Visual:** Hotel-listing UI using scarcity ("Only 2 rooms left") — illustrative example of a loss-framed cue. — `../assets/2028471666297217460__1.jpg`

**Source:** [@richardrx · 2026-03-02](https://x.com/richardrx/status/2028471666297217460)

## Use precise numbers, not round ones, to signal truth

**Principle:**
- Exact figures read as more credible than rounded ones.
- Round numbers signal marketing.
- Specific numbers signal reality.

**Apply when:**
- You write any claim, stat, or social-proof number.
- Surfaces: landing pages, ads, results, testimonials.

**Do:**
- Use the precise-number effect.
- Write "526 houses", not "over 500".
- Change only the precision of the claim. Trust rises.

**Evidence:**
- Schindler & Yalch (2006), 199 participants, fictional deodorant.
- Claims of "47%" or "53%" longer-lasting were judged ~10% more accurate than the rounded "50%" claim.
- Only the precision changed.

**Visual:** Real billboard: "LAST YEAR WE SOLD 526 HOMES. YOUR COUSIN SOLD 2. LIST RESPONSIBLY." — the precise number doing the persuasion. — `../assets/2024141244717281514__1.jpg`

**Quote:** "'526 houses' inspires confidence; 'over 500 houses' signals marketing."

**Source:** [@richardrx · 2026-02-18](https://x.com/richardrx/status/2024141244717281514)

## Guide the eye — don't give every option equal weight

**Principle:**
- The brain uses contrast to make fast decisions (Von Restorff effect).
- Competing options with identical visual weight create mental friction.
- Decision time rises. Conversion falls.
- Guiding the user is not manipulation. It respects their time.

**Apply when:**
- You have 3 plans, two equally-weighted buttons, or any "democratic" interface where everything looks the same.
- This is a common founder error.
- This is a default of AI-generated UIs.

**Do:**
- Exploit the Von Restorff effect.
- Make the value-generating option visually dominant.
- De-emphasize the rest (e.g., a ghost-styled "Cancel" beside a bold, colored primary).
- Highlight the highest-value solution when you know your ICP's pains and desires. Treat it as a duty.
- Know that slow decisions accumulate into a "hard-to-use" perception.
- Know that this perception becomes churn.

**Visual:** Good/bad confirm dialog: bad = both buttons same green weight; good = a ghost-text "Cancel" beside a solid red "Delete now," so the primary action stands out. — `../assets/2014317885494059106__1.jpg`

**Quote:** "If everything grabs attention, NOTHING grabs attention."

**Source:** [@richardrx · 2026-01-22](https://x.com/richardrx/status/2014317885494059106)

## Cut cognitive load — every choice you remove can lift conversion

**Principle:**
- Each extra field, choice, or block of complex text spends the user's mental energy.
- It triggers analysis paralysis.
- Your product can be complex. Your interface does not have to be.

**Apply when:**
- Screens: checkout, signup, and subscription.
- The user must decide or input under doubt.

**Do:**
- Strip the interface to the essential decision.
- When you cannot cut options, break the flow into smaller steps (e.g., a 4-step checkout).
- Know that the failure is invisible. Users do not complain or open tickets.
- Users close the tab as "silent churn". Your CAC is wasted.
- Dogfood your own onboarding as if you were a stranger.

**Evidence:**
- Removing 1 checkout field raised conversion 10%.
- Richard has seen reworked subscription screens lift LTV 200% just by simplifying the decision.

**Visual:** Mobile checkout labeled "Analysis paralysis": payment options split into smaller stages — advice to break choices into ~4 steps. — `../assets/2013597792447394034__1.jpg`

**Quote:** "They don't file a support ticket. They just close the tab — and your CAC goes in the trash."

**Source:** [@richardrx · 2026-01-20](https://x.com/richardrx/status/2013597792447394034)
