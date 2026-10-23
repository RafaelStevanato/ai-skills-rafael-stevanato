# Onboarding & Activation

Attribution: principles by Richard (@richardrx), "Richard — Design for startups". Translated from Portuguese. Each entry links to its source post.

Router: [../SKILL.md](../SKILL.md). Related files: [pricing-and-monetization.md](pricing-and-monetization.md) (card-in-trial), [churn-and-retention.md](churn-and-retention.md), [metrics-and-experimentation.md](metrics-and-experimentation.md), [checkout-and-forms.md](checkout-and-forms.md), [dashboards-and-data-viz.md](dashboards-and-data-viz.md).

Entry labels: **Apply when** = trigger condition. **Do** = rules. **Evidence** = data. **Visual** = image description and path. **Quote** = Richard's words, verbatim. **Source** = original post.

## Map the whole journey to value — then fix the biggest drop, not the first step

**Apply when:** Activation is low and you are not sure where the leak is.

**Do:**
- Look for the leak in the middle of the journey, not at the top of the funnel.
- Find the step where effort is already high and the user has no proof it is worth it.
- Define "value" as the first moment the user gets the promised result.
- Make value measurable and visible in data.
- List every step between signup and value: every screen, click, wait, field.
- Expect more steps than you remember.
- Measure the drop per step.
- Find the steepest fall.
- Fix the biggest drop first.
- Diagnose the cause of that drop: friction, confusion, or ordering.
- Cut friction.
- Direct attention when the cause is confusion.
- Deliver value before asking for effort when the cause is ordering.
- Count the steps before first value. Treat each step as a chance to quit.
- Build the shortest path to first result. Do not build the most complete product before it.
- Write the journey map on paper. The map in your head always looks shorter.

**Source:** [@richardrx · 2026-07-08](https://x.com/richardrx/status/2074814716824731651)

## An onboarding video welcomes — it doesn't teach

**Apply when:** Designing first-run onboarding or a welcome video.

**Do:**
- Write the video as a welcome. Never write it as a manual (nobody reads their car's or iPhone's).
- Build connection.
- Show the product at a glance.
- Point to where value comes fastest.
- Aim the video at cutting TTV, support tickets, and the lost feeling.
- Never aim the video at educating.
- Set the video length from your ICP's urgency: someone rushing vs. someone happy to build Lego.
- Skip the actor and the fancy set.
- Record the video in a screen recorder. Richard recorded his in Screen Studio. It beat the welcome videos of many big products.

**Visual:** A "Your account was created!" welcome modal with an embedded intro-video thumbnail and a single "Next" CTA — `../assets/2067987722954735812__1.jpg`

**Quote:** "Your product doesn't need a manual either — have you read your car's?"

**Source:** [@richardrx · 2026-06-19](https://x.com/richardrx/status/2067987722954735812)

## Rising MRR with rising churn means you lost them on day one

**Apply when:** Churn is creeping up and you are tempted to blame the product or add features.

**Do:**
- Treat rising MRR with rising churn as a day-one loss.
- Never read it as a month-2 loss.
- Expect the cause: the user landed in a dead empty-state dashboard with nothing guiding them to value.
- Never treat it as a feature gap.
- Measure **TTV** (time-to-value).
- Shrink TTV obsessively.
- Classify CAC, LTV and activation as *product* metrics, not marketing.
- Never buy more acquisition with weak retention. It fills a leaky bucket faster.

**Quote:** "It took two months to cancel, but you lost him the first day after signup."

**Source:** [@richardrx · 2026-06-18](https://x.com/richardrx/status/2067591574138052804)

## Measure activation, not signups

**Apply when:** You are judging onboarding by signups, time-in-product, or "completed the tour."

**Do:**
- Never use signups, session time, or tour completion as the onboarding success metric. They flatter you without proving the user reached value.
- Swap each vanity metric for its real counterpart:

| Vanity metric | Real metric |
|---|---|
| signups | activation rate |
| session time | time-to-first-useful-action (and its repetition) |
| onboarding completion | D7 retention |

- Find your aha moment empirically.
- List what every paying customer did in week one that churned users did not.
- Check collaborative acts first: invite, share, comment.
- Anchor on TTV/time-to-value.

**Evidence:**
- Userpilot benchmark (547 companies): avg TTV 1d 12h 23m; top performers under 5 min.
- SaaS activation rate avg 30–37%, top quartile 40%+, under 20% = structural problem.
- D7 retention avg 10–15%, over 30% is strong.

**Quote:** "If you can't say how long your user takes from signup to aha moment, you're not measuring what matters."

**Source:** [@richardrx · 2026-05-27](https://x.com/richardrx/status/2059616501544468624)

## Put friction in the right place, not zero friction everywhere

**Apply when:** You are reflexively cutting clicks and fields, or your human sales team is doing qualification the product should do.

**Do:**
- Never treat "less friction" as a universal law.
- Place friction deliberately. Friction in the wrong place kills the product. Friction in the right place qualifies and retains.
- Remove friction at trial signup. It kills acquisition.
- Add calibrated friction only in these three spots:
  1. Trial with card upfront. It filters commercial intent.
  2. Mandatory onboarding before the dashboard. It turns users into power-users faster.
  3. A 6–8 field enterprise demo form (role, team size, current tool, budget, timeline). It lowers lead volume but raises close rate.
- Use effort justification as the mechanism (Aronson & Mills, 1959). Same root as the endowment and IKEA effects.
- Scope rule: cut friction at trial signup and checkout. Add friction only at the three spots above.
- Ask: how much qualification effort is your human seller doing that the product should do?

**Evidence:**
- ChartMogul 2026: opt-in trial (no card) converts 8.9%; opt-out (with card) converts 31.4%.
- Superhuman requires a 30-min human call before access.

**Quote:** "How much qualification effort is your human seller doing that the product should do before they even step in?"

**Source:** [@richardrx · 2026-05-21](https://x.com/richardrx/status/2057436163841941980)

## Never ship a blank dashboard

**Apply when:** A new user lands post-signup on a screen with no data and no direction.

**Do:**
- Treat the empty dashboard as the main trial-loss point. It meets the user's peak of curiosity with a void.
- Cut decision time. Every second spent deciding what to do is a second closer to quitting.
- Apply four fixes:
  1. Add an empty state with a next-action hint. Point the CTA straight to value.
  2. Seed sample data so the user sees the destination before starting.
  3. Offer one single clear action ("Import your first spreadsheet"). Never offer eight. Never use a 12-step tour.
  4. Show visible progress from the first click. Start the bar at 20%, not 0%, so completion feels already underway.
- Start every progress bar at 20% or higher. Never start at 0%.

**Quote:** "A blank dashboard looks neutral, even tidy — but it just makes the user stop and think about what to do."

**Source:** [@richardrx · 2026-05-12](https://x.com/richardrx/status/2054283657934758021)

## Design onboarding as a behavioral trigger, not a feature tour

**Apply when:** New users evaporate without complaint and you never learn their name.

**Do:**
- Classify silent non-activation as an activation problem, not a product problem.
- Define silent non-activation: users who sign up, vanish in five minutes, and never formally churn.
- Fire a behavior in onboarding. Never narrate features.
- Find the single behavior that statistically separates retained users from lost users.
- Set that behavior as your activation north star.
- Measure every onboarding decision against it.
- Shift focus from explaining features to forcing that behavior fast.
- Exploit the Zeigarnik effect: open small loops (complete profile, invite 3 colleagues, send first message) so the user carries an unfinished task.

**Evidence:**
- Slack: teams exchanging 2,000 messages had 93% probability of staying.
- Facebook's equivalent: 7 friends in 10 days — the company's single focus, repeated at every all-hands.

**Quote:** "What's the number that separates who stays from who evaporates — and how does the user hit it in under 24h?"

**Source:** [@richardrx · 2026-05-11](https://x.com/richardrx/status/2053878928494690414)

## Map the journey from session replays, not from your diagram

**Apply when:** You "know" the happy path but can't state what % of users actually execute it.

**Do:**
- Distrust the founder's journey map. The founder builds a 12-step journey top-down (what the product wants).
- Expect the user to run 4 steps bottom-up (the specific problem they opened the tab to solve).
- Look for avoidable early-stage churn in the gap between the two.
- Expect the gap to be invisible. The founder only ever lived the creator's journey.
- Run three steps, no Figma:
  1. Write your version of the user journey in numbered steps, on paper.
  2. Open five real session recordings from the first 7 days. Note what each user actually does, in order, with timing. Include what they try and abandon.
  3. Lay both lists side by side.
- Read the report in the differences.
- Treat each divergence as a hypothesis. Confirm it or kill it.

**Quote:** "The user journey is what shows up in the replay; what's in Figma and Excalidraw is a hypothesis."

**Source:** [@richardrx · 2026-05-08](https://x.com/richardrx/status/2052711138572263474)

## Add declarative friction, cut administrative friction

**Apply when:** Auditing onboarding steps; deciding what to cut versus expand.

**Do:**
- Reject the rule "Good onboarding is short onboarding". It is incomplete.
- Classify each friction as administrative or declarative.
- Define administrative friction: it collects data the system uses later and buys the user nothing.
- Define declarative friction: it forces the user to state what they came to do. It costs a beat. It buys commitment, customization, and journey direction.
- Test each step: does it collect data, or does it make the user declare intent?
- Cut a step that only collects data.
- Expand a step that makes the user declare intent.
- Ask for a declaration ("what do you sell, what's your long-term goal?"). It creates a micro-commitment to the outcome before the user touches the product.
- Branch the journey (recommendations, tutorials, next actions) off that answer.

**Evidence:**
- Brazilian payments platform cut time-from-signup-to-first-sale from 24.2 to 2.5 days by adding a ~30-second intent step (positioned between signup and product), not by removing steps.

**Quote:** "Onboarding is also the first chance the user has to declare to themselves what they came to do."

**Source:** [@richardrx · 2026-05-07](https://x.com/richardrx/status/2052350703541039324)

## Trial conversion is a journey problem, not a pricing problem

**Apply when:** Users sign up, do "a bunch of nothing," and never return.

**Do:**
- Treat a trial as a test of value.
- Never expect price or trial length to save a user who never proves value to themselves.
- Diagnose which of the three failure modes applies:
  1. Blank dashboard: make the first step obvious and immediate. Drive to value or a micro-win. Drop "explore our product".
  2. Lost before value: install Clarity. Watch where they stall. Optimize that click.
  3. Lost to life: send a progress email ("you created 3 reports, your team accessed 12 times, you're in the top 20%"). Never send a generic "trial ending."

**Quote:** "The longest trial in the world doesn't save bad onboarding."

**Source:** [@richardrx · 2026-05-06](https://x.com/richardrx/status/2052096365128273956)

## Make onboarding active, not passive

**Apply when:** Your onboarding opens with "Welcome, here's the documentation."

**Do:**
- Ban passive onboarding (tooltips, guided tour, docs: learn if you want) as the main path.
- Expect the user not to explore. They have 47 tabs open and WhatsApp pinging.
- Expect the user to do the bare minimum before deciding whether to return.
- Design a sequence where each action delivers value and that value triggers the next.
- Assume you know the shortest path to value better than the user does.
- Design that path.
- Strip the friction.
- Make sure the user arrives.
- Never ask "what's the minimum the user must do?"
- Ask "what's the smallest action that delivers the most value in the least time?"

**Evidence:**
- Slack drops you into a channel and makes you send a message first — you use the product before any tutorial.

**Quote:** "Understanding by doing beats understanding by reading."

**Source:** [@richardrx · 2026-04-22](https://x.com/richardrx/status/2046959126245249288)

## Treat sub-30-day churn as an onboarding fix, not a feature gap

**Apply when:** Users leave before they ever liked what you built, and you are tempted to ship more features.

**Do:**
- Treat early-stage SaaS churn in the first 30 days as an onboarding problem, not a product problem.
- Never add features to fix it. Features add complexity and make it worse.
- Diagnose with three questions:
  1. How long to the first real result? If the answer is "it depends" or over a day, you are bleeding users.
  2. Does the user know where they are? Use a progress bar or checklist.
  3. What happens when they drop mid-flow: email, push, nothing? Use the Zeigarnik effect to remind them they started.
- Apply the Progress effect: someone seeing 30% done is likelier to finish than someone at 0%.
- Treat a 0% start as a design error.
- Start every progress bar at 20% or higher.

**Quote:** "Sub-30-day churn rarely dies to features; it dies to the right sequence of micro-interactions that deliver value before asking for effort."

**Source:** [@richardrx · 2026-04-20](https://x.com/richardrx/status/2046212675017887881)

## Deliver the promised result before teaching mechanics

**Apply when:** Your onboarding is a checklist of setup mechanics rather than a path to the outcome.

**Do:**
- Deliver the result you promised in the landing-page hero. Nobody wants to learn to use your product.
- Never teach mechanics first ("create a project → add a member → configure integrations"). It is boring.
- Deliver value first. It converts.
- Lead with the outcome: "In 2 minutes you'll see your first report → let's start with the data you already have → done, that's the insight competitors pay consultants for".
- Reframe progress with the Progress effect. Credit effort already spent: "You've done the hard part, just 3 steps left".
- Keep loops small (Zeigarnik effect). People close loops only if they look closable.
- Pre-select the right plan from data you collected. Do not ask. Then offer the upsell.

**Quote:** "The gap between 5% and 15% trial conversion is in these details — not features, not price — in the sequence of micro-decisions you designed without realizing you were designing."

**Source:** [@richardrx · 2026-04-16](https://x.com/richardrx/status/2044785090832543998)

## Qualify by behavior, not by a long signup form

**Apply when:** You are weighing an 8-field signup form against email + password.

**Do:**
- Qualify by behavior, not by form. Behavior is more precise.
- Expect the "more qualified leads" argument for long forms to usually lose.
- Default to the minimal form.
- Qualify later, inside the product, from real behavior.
- Decide where to add versus remove friction by context ("it depends"). This decision separates a product that grows from one that spins its wheels.
- Scope rule: cut friction at trial signup and checkout. Add calibrated friction only at the three named spots (card-upfront trial, mandatory onboarding, enterprise demo form). See [Put friction in the right place, not zero friction everywhere](#put-friction-in-the-right-place-not-zero-friction-everywhere).

**Evidence:**
- Same product, two founders: 8-field form (name, email, company, role, phone, segment, team size, how-did-you-hear) → 12% signup rate; email + password only → 34%.

**Visual:** Annotated onboarding step (DevNoodles): an ICP/intent question flagged "Zeigarnik effect" (the step progress dots) and a B2C/B2B card selector flagged "Default effect" (the B2C card is pre-badged "Mais comum") — showing where each bias is engineered into the flow. — `../assets/2042558822825239030__1.jpg`

**Source:** [@richardrx · 2026-04-10](https://x.com/richardrx/status/2042558822825239030)

## Celebrate the activation moment, don't just confirm it

**Apply when:** A user completes a hard-won first action (first transaction, first integration) and you respond with a static success state.

**Do:**
- Celebrate the activation moment. Never only confirm it.
- Show a rising graph, not a number. A number is data. A rising graph is progress.
- Use progress to trigger dopamine and an emotional memory tied to the product.
- Replace the static success state. Most SaaS confirms where it should celebrate.
- Engineer the peak moment at the point of highest emotional vulnerability in activation: right after the user clears the effort.
- Show motion and accomplishment proportional to the effort invested.
- Apply the peak-end rule: users judge an experience by its emotional peak and its ending, rarely by the average.

**Evidence:**
- Stripe shows a rising graph (not a number) the moment the first transaction processes — the founder who integrated it at 3am remembers exactly where they were.

**Quote:** "A number would have done the job. The graph created a customer."

**Source:** [@richardrx · 2026-04-04](https://x.com/richardrx/status/2040415841628651689)

## Cut time-to-value by reorder and removal, not feature changes

**Apply when:** Your activation flow is slow and you assume the product itself is the bottleneck.

**Do:**
- Treat high TTV as a form-and-order problem. It is almost never product complexity.
- Count each day between signup and first result as another day of abandonment risk. Abandonment = churn.
- Run three iteration cycles with no product changes:
  1. Reduce cognitive load. Group and standardize what the user must fill in.
  2. Work with legal/compliance. Strip everything required by habit but not by actual necessity.
  3. Invert the sequence so the user feels value before facing the heaviest step.
- Keep the mandatory compliance steps.

**Evidence:**
- Major Brazilian payments platform: 24 days → 2.5 days to first sale (89.7% reduction), no product changes, no cutting of mandatory compliance steps.

**Visual:** Month-by-month TTV table: Jan 24.2d → Feb 19.6d → Mar 16.8d → Apr 9.3d → May 2.5d, alongside accounts created / approved / new sellers per month. — `../assets/2037583944283996418__1.jpg`

TTV by month (from the Visual above):

| Month | TTV (days) |
|---|---|
| Jan | 24.2 |
| Feb | 19.6 |
| Mar | 16.8 |
| Apr | 9.3 |
| May | 2.5 |

**Source:** [@richardrx · 2026-03-27](https://x.com/richardrx/status/2037583944283996418)

## Give the trial an active goal, not passive access

**Apply when:** Your trial is open-ended access with no challenge or target.

**Do:**
- Replace the passive trial ("use it if you want, cancel guilt-free"). It builds no commitment.
- Build an active-goal trial. It builds commitment before billing.
- Set a recurring daily goal during the trial.
- Require the user to opt into the goal and complete it.
- Name the mechanism: progressive commitment.
- Expect each completed day to raise the psychological cost of canceling. The user starts defending a decision they already made, before paying.
- Apply the pattern to any product, good or bad. Done right, the onboarding itself is excellent.

**Evidence:**
- Wispr Flow challenges trial users to dictate 100+ words a day for 7 days — looks generous, is behavioral science.

**Source:** [@richardrx · 2026-03-26](https://x.com/richardrx/status/2037316988981174464)

## Calibrate the first step to the user's real willingness

**Apply when:** Your first onboarding step bundles setup, data import, team invites, and project creation, or demands a campaign-sized action.

**Do:**
- Judge the first task by perceived effort. Users do not evaluate it rationally.
- Ban a first step that asks too much. The cognitive cost of imagining the task paralyzes the user, and they quit before starting. This is the activation-barrier effect.
- Apply two biases to fix it:
  1. Started-progress effect: show what the user has already done before what is left. A loyalty card with the first stamp pre-filled beats a blank 9-stamp card, because the starting point changes perceived distance to the finish.
  2. Small-steps effect: "Create one story today" has radically lower perceived cost than "post 5×/week," even when the underlying task is identical.
- Sequence effort so the user hits first value before noticing how much they invested.
- Build momentum.

**Evidence:**
- Instagram A/B test made "Create 5 new public reels" the first task — for someone who barely posts weekly, that's paralyzing.

**Visual:** Bad first-step example: a weekly-progress checklist at "0% completed" whose top item is "Create 5 new public reels (0/5)." — `../assets/2036461688505909250__1.jpg`

**Quote:** "Asking for more isn't necessarily the problem; asking for all of it at once, with no progress anchor and no commitment ladder, is."

**Source:** [@richardrx · 2026-03-24](https://x.com/richardrx/status/2036461688505909250)

## Treat onboarding as the bridge between CAC and LTV

**Apply when:** Users enter the trial without intent to a result and ghost before ever paying.

**Do:**
- Treat onboarding as the bridge from CAC to LTV. It is not an interface tutorial.
- Treat onboarding as the point of maximum leverage to expand revenue.
- Track activation cost. Founders obsess over CAC and landing-page conversion but are blind to it.
- Expect cancellation to happen on day one. It is only formalized when Stripe's billing reminder lands.
- Apply two fixes:
  1. Turn support into UX. Treat every onboarding support ticket as a design failure. Map recurring setup questions. Convert the answers into features or in-flow tooltips.
  2. Compress TTV obsessively. Make the user experience the product's core promise in the least time possible. If they must configure 5 screens before any result, you have already lost.

**Quote:** "Letting a user into the trial without intent of a result isn't self-service. Design's job doesn't end at signup — that's where it starts paying you back."

**Source:** [@richardrx · 2026-03-13](https://x.com/richardrx/status/2032485654811083005)

## Pick onboarding patterns by awareness × flow complexity

**Apply when:** Choosing or combining onboarding patterns for a new flow (SaaS, PLG, B2B early stage).

**Do:**
- Never look for the best onboarding in the abstract. Pick the one that removes friction and delivers value early for your users.
- Treat the nine patterns as behavior-shaping mechanisms, not UI components.
- Select patterns by two axes (see Selection rule below).

**The nine patterns (pattern → ideal use / tradeoff):**

| # | Pattern | Ideal use / tradeoff |
|---|---|---|
| 1 | **Welcome modal** | high-awareness ICP or low-complexity products; easy to build, easy to ignore. |
| 2 | **Wizard / product tour** | B2B and complex/high-cost-of-error flows (fintech, compliance); long tours cause boredom and need constant upkeep. |
| 3 | **Contextual tooltips** | advanced/secondary features; slashes support tickets but users may miss them if contrast is poor. |
| 4 | **Empty state** (Richard's favorite) | dashboards, lists, data-dependent areas; if executed well it's mandatory, directs the first action and accelerates TTV. |
| 5 | **Personalization** | products serving many ICPs with different journeys; great CRM data, but too long kills signup conversion. |
| 6 | **Checklists** | critical flows with mandatory prerequisites (webhook, KYC); exploits the Zeigarnik effect, but a long list breeds aversion — every item must move toward value, no bureaucratic tasks. |
| 7 | **Goal-setting** | habit products (finance, productivity, health); uses commitment bias, but a broken goal can break the emotional contract. |
| 8 | **Sample data** | sell the dream of a full, organized product before the user inputs anything (distinct from skeleton screens). |
| 9 | **Use cases / demos** | products burning expensive resources (AI tokens) with infinite outputs; show max potential without forcing creativity from scratch. |

**Selection rule (two axes):**
- Score **awareness level**: low = needs guidance; high = needs speed.
- Score **flow complexity**: high = needs structure.
- Pick patterns from the four cases:

| Awareness | Flow complexity | Patterns |
|---|---|---|
| low | high | tours + checklists + personalization |
| low | low | modal + empty state |
| high | high | checklist + tooltip + empty state |
| high | low | modal + empty state (then get out of the user's way) |

**Build vs. buy:**
- Treat build vs. buy as a financial/operational decision, not an aesthetic one.
- Buy (Wistia, PostHog, Sprig) in these cases:
  - Speed is critical.
  - Dev is overloaded.
  - You are running A/B tests.
- Build in these cases:
  - Onboarding is strategic.
  - You need perfect aesthetic integration.
  - You must avoid third-party dependence.

**Quote:** "Onboarding's job isn't to teach the user — nobody likes an instruction manual — it's to remove cognitive effort and deliver utility as fast as possible. TTV correlates directly with churn."

**Source:** [@richardrx · 2026-02-04](https://x.com/richardrx/status/2019019293761941566)
