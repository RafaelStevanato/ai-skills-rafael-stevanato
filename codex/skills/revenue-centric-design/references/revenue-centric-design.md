# Revenue-Centric Design — Philosophy & Process

Contents: The 9 principles of Revenue Centric Design (RCD) · Design's leverage isn't constant — it changes with the product stage · Design owns the flow, not the final coat of paint · Find the leaks before you rebuild the bucket · Refactor to solve a real problem, not to repaint the wall · Mine the tactical layer — it's the most under-explored · Leave the over-used parts alone; improve around them · Don't hire a designer to make software "pretty" · Treat the interface as data, not opinion · Measure changes; don't argue from opinion · Better design wins even when the tech is worse · Make the dashboard answer "what do I do now?" · (Earlier draft) The 10 design principles

Attribution: Richard (@richardrx), "Richard — Design for startups", translated from Portuguese. Return to [SKILL.md](../SKILL.md).

## The 9 principles of Revenue Centric Design (RCD)

Richard built this framework (RCD) after Dieter Rams' 10 laws (form/function) and Amber Case's Calm Technology (attention/context).

**Apply when:** You design a product that must convert, retain, and expand and need a north-star checklist.

**Do:** Apply all nine principles. Read the list in [SKILL.md > Core rules](../SKILL.md#the-rcd-spine).

**Quote:** "Rams taught me form and function. Amber Case taught me attention and context. Neither taught me to think about revenue."

**Source:** [@richardrx · 2026-05-05](https://x.com/richardrx/status/2051672248348479691)

## Design's leverage isn't constant — it changes with the product stage

Design payoff is near zero at MVP and grows to decisive at scale. Look at design last when a product is dying. Know the stage to learn whether design moves cash or is vanity.

**Apply when:** You decide where to put design effort at your current stage.

**Do:** Match the discipline to the stage.
- **MVP:** shorten the path to value. Say no to "obvious" features.
- **Survival:** fix onboarding/activation. The first week beats the whole roadmap and buys runway.
- **Traction:** fix conversion. Sharpen the LP and tune onboarding as channels saturate.
- **PMF:** add depth. Design the second "aha," the upgrade path, and expansion so retention stabilizes higher.
- **Scale:** make design a system. Build a design system so 3–4 teams ship without you.

Follow the order: Shorten → Activate → Convert → Expand → Systematize.

**Quote:** "Polishing the UI of a product nobody wants is the most beautiful mistake there is. It dies pretty."

**Source:** [@richardrx · 2026-06-15](https://x.com/richardrx/status/2066476811177877962)

## Design owns the flow, not the final coat of paint

Information order, card-request timing, what appears at moments of doubt, and the first moment of felt value decide convert or churn. Product, eng, and requirements set and code these long before a "finished" product reaches design.

**Apply when:** Design is scoped as "make it pretty before launch". Product/eng/requirements own the flow (common in big orgs or eng-led teams).

**Do:** Pull design upstream to own the flow. Show the argument: Richard built the same app twice (requirements-led vs UX-led). The side-by-side won him project leadership.

**Quote:** "If I got a buck every time I heard 'design comes in when the product's almost ready,' I'd buy a GT3 RS."

**Source:** [@richardrx · 2026-06-09](https://x.com/richardrx/status/2064327349894553855)

## Find the leaks before you rebuild the bucket

Products rarely die from one dramatic error. They bleed out as micro-disappointments accumulate across the journey. Patch the leaks instead of redesigning from scratch: a fraction of the effort for most of the gain.

**Apply when:** Conversion or retention drops and the team's reflex is a full redesign (the blank-page urge).

**Do:** Run a heuristic analysis.
- Walk the product area by area, from landing to activation.
- Mark each point OK or not-OK and screenshot every failure.
- Grade severity on four levels, from aesthetic (ugly but harmless) to critical (user stalls, conversion dies).
- Output a map of holes, then seal the drips.

**Visual:** Journey graph — cumulative score sliding downward, green dots = wins, small red dots = micro-disappointments stacking up — `../assets/2062621019978760424__1.jpg`

**Quote:** "Redesign from zero says more about the desire of whoever's drawing than the pain of whoever's using."

**Source:** [@richardrx · 2026-06-04](https://x.com/richardrx/status/2062621019978760424)

## Refactor to solve a real problem, not to repaint the wall

Designers loop forever ("it's great → could be better → better → repeat") and refactor UI like code. True refactoring waits for user feedback and fixes a problem. Repainting because the old color got boring is vanity: it burns a week on pixel-perfect work nobody asked for.

**Apply when:** You feel the itch to redo a screen mid-project. Separate "this resolves a known pain" from "this just looks nicer."

**Do:** Gate the change: ask whether it attacks a real, validated pain. Richard's example passed because it tackled an old industry pain: customers not trusting the repair shop's quote. Until usage proves it, "you're just selling the visual."

**Visual:** RepareCar quote builder — parts pre-loaded with photo, code, and cost; live financial summary (labor + parts → total) — `../assets/2062554393447141438__1.jpg`

**Source:** [@richardrx · 2026-06-04](https://x.com/richardrx/status/2062554393447141438)

## Mine the tactical layer — it's the most under-explored

Product design has three leverage drivers: Tactical → Organizational → Strategic. Strategic has the most asymmetric upside. But everyone outsourced aesthetics to the same AI-generated UI kit, so the tactical layer (aesthetics + function) is the most under-explored: lowest leverage in theory, highest return in practice, because nobody looks.

**Apply when:** Your SaaS UI looks like every competitor's. You assume polish is "too obvious" to bother with.

**Do:** Invest the basic care most skip.
- Use distinctive aesthetics for differentiation and branding, even for a commodity (example: Resend dressing its ICP).
- Cut cost here too. Square Johnnie Walker bottles cut breakage and shipping. The smaller iPhone box fit more units per container. Both go straight to margin.

**Evidence:** Ferrari's first EV (Luce, Jony Ive–led) drew the worst brand reception in recent company history: ~8% stock drop, billions in market value erased in 48 hours. Mockers compared it to a Honda Accord and a luxury toaster. The revolt was almost entirely visual.

**Source:** [@richardrx · 2026-05-28](https://x.com/richardrx/status/2059997257156399233)

## Leave the over-used parts alone; improve around them

Heavily-used parts of a working product form a "cognitive map": users memorized where everything is and which gesture does what. The map is part of the product. An aggressive redesign makes users pay a re-learning cost and signals that you think you know better.

**Apply when:** You are tempted to overhaul a working, well-adopted product.

**Do:** Ask: "Which part is so used that touching it would feel hostile?" Freeze that part. Improve around it. Cause: status-quo bias. People keep the current state when the gain seems smaller than the re-learning effort.

**Evidence:** Snapchat's Feb 2018 redesign (separating friends from brand/creator content) triggered a 1.2M-signature Change.org reversal petition. Kylie Jenner's "does anyone else not open Snapchat anymore?" preceded a sharp stock drop.

**Quote:** "While we see every redesign as an upgrade, the user can see it as a threat."

**Source:** [@richardrx · 2026-05-12](https://x.com/richardrx/status/2054180098392178796)

## Don't hire a designer to make software "pretty"

Aesthetics is subjective, does not scale, and cannot save a product from high churn. The interface steers user behavior toward a KPI; aesthetics is sometimes a by-product. Hiring design for looks is technical founders' biggest financial mistake.

**Apply when:** You scope design as cosmetics, not as a growth lever for conversion, retention, and expansion.

**Do:** Aim design at three outcomes.
1. **Conversion via lower cognitive load.** Hick's Law: each extra on-screen option raises decision time and abandonment. Remove friction (Ability in the Fogg model) so the target task is the path of least resistance.
2. **Retention via perceived progress.** Users churn when they don't see value, not when the UI is ugly. Onboarding progress (contrast + progress effect) gives momentum toward value, measured as TTV.
3. **Expansion via loss aversion.** Design plans so users hit value limits, then upgrade to avoid losing an efficiency they just discovered.

**Visual:** Goal Gradient Effect in onboarding — a booking flow headlined "Just two steps left for your Bahamas trip!" with a single primary CTA, showing progress proximity to push completion — `../assets/2029226965580804593__1.jpg`

**Source:** [@richardrx · 2026-03-04](https://x.com/richardrx/status/2029226965580804593)

## Treat the interface as data, not opinion

When churn rises, one founder opens analytics: where users stalled, hesitated, and which screen preceded cancellation. The other debates color palettes in product meetings. One builds a company; the other builds a portfolio.

**Apply when:** You decide how the team reasons about design changes and what product meetings start from.

**Do:**
- Start from LTV, CAC, and activation rate. Judge delivery on next quarter's MRR.
- Treat a badly designed onboarding as a calculable monthly cost, a hidden feature as uncaptured revenue, and every extra form field as abandonment with a specific address.
- Treat design as a lever, like a funnel to a growth engineer or cost structure to a CFO.

**Source:** [@richardrx · 2026-03-30](https://x.com/richardrx/status/2038566978760122661)

## Measure changes; don't argue from opinion

Teams say "change the color, swap the CTA, kill the pop-up" and test nothing. Faith in gut beats faith in data science. Product design is experimentation and analysis, not guesswork. Without tests there is no improvement and no growth.

**Apply when:** A team ships UI changes driven by "I think this is ugly / too long / annoying" and skips the real question: "What's the actual impact of this change on the result?"

**Do:** Where there is direction, run a process: A/B tests with a clear hypothesis and a KPI. Say "I measure," not "I think." Trust the data over ego.

**Evidence:** A pricing-page experiment generated 68% more AOV (average order value) — "and it wasn't even the coolest experiment we ran."

**Visual:** Before/After of a pricing block — same product, redesigned tiers, "+68% AOV" badge on the winning variant — `../assets/2026605258152038780__1.jpg`

**Source:** [@richardrx · 2026-02-25](https://x.com/richardrx/status/2026605258152038780)

## Better design wins even when the tech is worse

A competitor with worse technology still wins with better design: smoother onboarding, clearer copy, easier features, human error messages, a product that feels cared for.

**Apply when:** You are convinced you lose unfairly because your underlying tech is superior.

**Do:** Stop treating design as decoration. Audit the felt experience end to end: onboarding friction, copy clarity, error-message tone, the sense that a human cared. Treat these as the real competitive battleground, not raw tech. Richard endorses @oykun's "dear founder" note.

**Quote:** "Dear founder, yes, you're right — their tech is worse. But their design is better. That's why they're winning. And you are not."

**Source:** [@richardrx · 2026-03-24](https://x.com/richardrx/status/2036374984206025082)

## Make the dashboard answer "what do I do now?"

A dashboard is the front door of your software, not NASA mission control. Colorful charts, five-decimal counters, and endless tables overload the user, who feels dumb and churns. A good dashboard answers one question: "What do I do now to get more value?" That drives LTV.

**Apply when:** You build or audit any data-heavy screen (dashboards, reports, analytics views).

**Do:** Apply eight rules.
1. **Define your "who".** List the users' top 3 pains and your top 3 value deliveries. Combine them.
2. **Treat noise as a cognitive tax.** Every pixel that does not communicate (thick borders, heavy shadows, colored fills) competes for attention. Less ink = more signal.
3. **Show insights, not raw data.** Bad: "sales Jan–Dec". Good: "Revenue up 15% vs last month, likely cause: Twitter," with an expandable card (and a free 15-day upsell to act on it).
4. **Run the "so what?" test** (from Scott Belsky's *Making Ideas Happen*). For each component, if a number is red, put the fix button right beside it.
5. **Round everything.** Drop decimals, currency symbols, and cents the ICP does not need: "R$10,234.56" → "10k". White space cuts anxiety.
6. **Group by business context**, not chart type: sales in one block, support in another. The eye scans Z-within-F. Use Gestalt proximity/similarity to shorten the scan.
7. **Use size + position as hierarchy.** "if everything is important, nothing is". Give the user's North Star metric the largest font on screen.
8. **Design for humans.** Celebrate when a goal is hit. Redirect with good humor when something breaks. Reinforce positive behavior to build habit and retention.

**Visual:**
- "Raw data → Actionable" LEGO value ladder (collection → preparation → visualization → analysis → storytelling, rising from −value to +value) — `../assets/2022255404743381289__3.jpg`
- Bad example: an aesthetic-looking dashboard crammed with modules and numbers that fails to direct attention — `../assets/2022255404743381289__4.jpg`
- Hierarchy fix: a tiny "13" buried at the right edge of the middle row (✗) vs a large "13" placed top-left in the F-pattern (✓) — `../assets/2022255404743381289__5.jpg`

**Quote:** "Your dashboard is a graveyard of data, and that's going to kill your LTV."

**See also:** [dashboards-and-data-viz](dashboards-and-data-viz.md)

**Source:** [@richardrx · 2026-02-13](https://x.com/richardrx/status/2022255404743381289)

## (Earlier draft) The 10 design principles

This is an earlier draft of the canonical RCD framework above, "focused on influencing behavior and generating revenue." The 9-principle list supersedes it.

**Apply when:** You cross-reference the evolution of RCD.

**Do:** Keep three framings. The rest overlaps with RCD.
- "Everything is an experiment": each interface change is a hypothesis. Without a success metric you cannot know what works.
- "Remember the Swiss Army knife": every added feature raises the learning curve, cognitive load, and maintenance cost. Past a peak, each feature lowers perceived usefulness. Find your ideal.
- "Cancellation begins after signup": reactive CS does not fix churn. Use interventions that anticipate abandonment before it becomes intent.

**Source:** [@richardrx · 2026-04-06](https://x.com/richardrx/status/2041117825436106979)
