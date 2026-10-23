# Onboarding & Activation

Contents: Map the whole journey to value — then fix the biggest drop, not the first step · An onboarding video welcomes — it doesn't teach · Rising MRR with rising churn means you lost them on day one · Measure activation, not signups · Put friction in the right place, not zero friction everywhere · Never ship a blank dashboard · Design onboarding as a behavioral trigger, not a feature tour · Map the journey from session replays, not from your diagram · Add declarative friction, cut administrative friction · Trial conversion is a journey problem, not a pricing problem · Make onboarding active, not passive · Treat sub-30-day churn as an onboarding fix, not a feature gap · Deliver the promised result before teaching mechanics · Qualify by behavior, not by a long signup form · Celebrate the activation moment, don't just confirm it · Cut time-to-value by reorder and removal, not feature changes · Give the trial an active goal, not passive access · Calibrate the first step to the user's real willingness · Treat onboarding as the bridge between CAC and LTV · Pick onboarding patterns by awareness × flow complexity

Attribution: principles by Richard (@richardrx), "Richard — Design for startups". Translated from Portuguese.

Router: [../SKILL.md](../SKILL.md).

## Map the whole journey to value — then fix the biggest drop, not the first step

**Apply when:** Activation is low and you cannot see where it leaks.

**Do:**
- Look for the leak in the middle of the journey (high effort, no proof of worth yet), not at the top of the funnel.
- Define "value": the first moment the user gets the promised result. Make it measurable in data.
- List on paper every step from signup to value (screen, click, wait, field). Expect more steps than you remember: the map in your head always looks shorter.
- Measure the drop per step. Fix the steepest fall first.
- Diagnose the cause: friction (cut), confusion (direct attention), ordering (deliver value before asking for effort).
- Build the shortest path to first result, not the most complete product. Each step before it is a chance to quit.

**Source:** [@richardrx · 2026-07-08](https://x.com/richardrx/status/2074814716824731651)

## An onboarding video welcomes — it doesn't teach

**Apply when:** Designing first-run onboarding or a welcome video.

**Do:**
- Write a welcome, never a manual (nobody reads their car's or iPhone's). Build connection, show the product at a glance, point to where value comes fastest.
- Aim at cutting TTV, support tickets, and the lost feeling. Never aim at educating.
- Set the length from your ICP's urgency: someone rushing vs. someone happy to build Lego.
- Skip the actor and the fancy set. Richard recorded his in Screen Studio and it beat many big products' videos.

**Visual:** A "Your account was created!" welcome modal with an embedded intro-video thumbnail and a single "Next" CTA — `../assets/2067987722954735812__1.jpg`

**Quote:** "Your product doesn't need a manual either — have you read your car's?"

**Source:** [@richardrx · 2026-06-19](https://x.com/richardrx/status/2067987722954735812)

## Rising MRR with rising churn means you lost them on day one

**Apply when:** Churn creeps up and you want to blame the product or add features.

**Do:**
- Read rising MRR with rising churn as a day-one loss, not a feature gap (dead empty-state dashboard).
- Measure **TTV** (time-to-value). Shrink it obsessively.
- Classify CAC, LTV and activation as *product* metrics, not marketing.
- Never buy more acquisition with weak retention. It fills a leaky bucket faster.

**Quote:** "It took two months to cancel, but you lost him the first day after signup."

**Source:** [@richardrx · 2026-06-18](https://x.com/richardrx/status/2067591574138052804)

## Measure activation, not signups

**Apply when:** You are judging onboarding by signups, time-in-product, or "completed the tour."

**Do:**
- Never use signups, session time, or tour completion as the success metric. Swap each:
  - signups → activation rate
  - session time → time-to-first-useful-action (and its repetition)
  - onboarding completion → D7 retention
- Find the aha moment empirically: list what every paying customer did in week one that churned users did not. Check collaborative acts first: invite, share, comment. Anchor on TTV/time-to-value.

**Evidence:**
- Userpilot benchmark (547 companies): avg TTV 1d 12h 23m; top performers under 5 min.
- SaaS activation rate avg 30–37%, top quartile 40%+, under 20% = structural problem.
- D7 retention avg 10–15%, over 30% is strong.

**Quote:** "If you can't say how long your user takes from signup to aha moment, you're not measuring what matters."

**Source:** [@richardrx · 2026-05-27](https://x.com/richardrx/status/2059616501544468624)

## Put friction in the right place, not zero friction everywhere

**Apply when:** You reflexively cut clicks and fields, or your human sales team does qualification the product should do.

**Do:**
- Never treat "Less friction" as a universal law: remove friction at trial signup and checkout, where it kills acquisition. Add calibrated friction only in three spots:
  1. Trial with card upfront. It filters commercial intent.
  2. Mandatory onboarding before the dashboard. It turns users into power-users faster.
  3. A 6–8 field enterprise demo form (role, team size, current tool, budget, timeline). It lowers lead volume but raises close rate.
- Mechanism: effort justification (Aronson & Mills, 1959), same root as the endowment and IKEA effects.

**Evidence:**
- ChartMogul 2026: opt-in trial (no card) converts 8.9%; opt-out (with card) converts 31.4%.
- Superhuman requires a 30-min human call before access.

**Quote:** "How much qualification effort is your human seller doing that the product should do before they even step in?"

**Source:** [@richardrx · 2026-05-21](https://x.com/richardrx/status/2057436163841941980)

## Never ship a blank dashboard

**Apply when:** A new user lands post-signup on a screen with no data and no direction.

**Do:**
- Treat the empty dashboard as the main trial-loss point: each second spent deciding is closer to quitting.
- Apply four fixes:
  1. Add an empty state with a next-action hint. Point the CTA straight to value.
  2. Seed sample data so the user sees the destination before starting.
  3. Offer one single clear action ("Import your first spreadsheet"). Never eight. Never a 12-step tour.
  4. Show visible progress from the first click. Start the bar at 20% or higher, never at 0%, so completion feels already underway.

**Quote:** "A blank dashboard looks neutral, even tidy — but it just makes the user stop and think about what to do."

**Source:** [@richardrx · 2026-05-12](https://x.com/richardrx/status/2054283657934758021)

## Design onboarding as a behavioral trigger, not a feature tour

**Apply when:** New users evaporate without complaint and you never learn their name.

**Do:**
- Classify silent non-activation (users sign up, vanish in five minutes, never formally churn) as an activation problem, not a product problem.
- Fire a behavior fast. Never narrate features.
- Find the single behavior that statistically separates retained from lost users. Make it the activation north star. Measure every onboarding decision against it.
- Exploit the Zeigarnik effect: open small loops (complete profile, invite 3 colleagues, send first message) so the user carries an unfinished task.

**Evidence:**
- Slack: teams exchanging 2,000 messages had 93% probability of staying.
- Facebook's equivalent: 7 friends in 10 days — the company's single focus, repeated at every all-hands.

**Quote:** "What's the number that separates who stays from who evaporates — and how does the user hit it in under 24h?"

**Source:** [@richardrx · 2026-05-11](https://x.com/richardrx/status/2053878928494690414)

## Map the journey from session replays, not from your diagram

**Apply when:** You "know" the happy path but can't state what % of users actually execute it.

**Do:**
- Distrust the founder's journey map. The founder builds 12 steps top-down (what the product wants). The user runs 4 steps bottom-up (the problem they opened the tab to solve). Avoidable early-stage churn lives in the gap.
- Run three steps, no Figma:
  1. Write your version of the user journey in numbered steps, on paper.
  2. Open five real session recordings from the first 7 days. Note what each user does, in order, with timing, including what they try and abandon.
  3. Lay both lists side by side.
- Read the report in the differences. Treat each divergence as a hypothesis to confirm or kill.

**Quote:** "The user journey is what shows up in the replay; what's in Figma and Excalidraw is a hypothesis."

**Source:** [@richardrx · 2026-05-08](https://x.com/richardrx/status/2052711138572263474)

## Add declarative friction, cut administrative friction

**Apply when:** Auditing onboarding steps; deciding what to cut versus expand.

**Do:**
- Classify each friction ("Good onboarding is short onboarding" is incomplete):
  - Administrative: collects data the system uses later; buys the user nothing.
  - Declarative: forces the user to state what they came to do; costs a beat; buys commitment, customization, and journey direction.
- Cut a step that only collects data. Expand a step that makes the user declare intent.
- Ask for a declaration ("what do you sell, what's your long-term goal?"). It creates a micro-commitment before the user touches the product. Branch the journey (recommendations, tutorials, next actions) off that answer.

**Evidence:** Brazilian payments platform cut time-from-signup-to-first-sale from 24.2 to 2.5 days by adding a ~30-second intent step (positioned between signup and product), not by removing steps.

**Quote:** "Onboarding is also the first chance the user has to declare to themselves what they came to do."

**Source:** [@richardrx · 2026-05-07](https://x.com/richardrx/status/2052350703541039324)

## Trial conversion is a journey problem, not a pricing problem

**Apply when:** Users sign up, do "a bunch of nothing," and never return.

**Do:**
- Treat a trial as a test of value. Diagnose which of the three failure modes applies:
  1. Blank dashboard: make the first step obvious and immediate. Drive to value or a micro-win. Drop "explore our product".
  2. Lost before value: install Clarity. Watch where they stall. Optimize that click.
  3. Lost to life: send a progress email ("you created 3 reports, your team accessed 12 times, you're in the top 20%"), not a generic "trial ending."

**Quote:** "The longest trial in the world doesn't save bad onboarding."

**Source:** [@richardrx · 2026-05-06](https://x.com/richardrx/status/2052096365128273956)

## Make onboarding active, not passive

**Apply when:** Your onboarding opens with "Welcome, here's the documentation."

**Do:**
- Ban passive onboarding (tooltips, guided tour, docs: learn if you want) as the main path.
- Design a sequence where each action delivers value and that value triggers the next.
- Assume you know the shortest path to value better than the user does. Design it, strip the friction, make the user arrive.
- Never ask "what's the minimum the user must do?" Ask "what's the smallest action that delivers the most value in the least time?"

**Evidence:** Slack drops you into a channel and makes you send a message first — you use the product before any tutorial.

**Quote:** "Understanding by doing beats understanding by reading."

**Source:** [@richardrx · 2026-04-22](https://x.com/richardrx/status/2046959126245249288)

## Treat sub-30-day churn as an onboarding fix, not a feature gap

**Apply when:** Users leave before they like the product and you want to ship features.

**Do:**
- Treat first-30-day churn in early-stage SaaS as an onboarding problem. Never add features to fix it.
- Diagnose with three questions:
  1. How long to the first real result? "It depends" or over a day means you bleed users.
  2. Does the user know where they are? Use a progress bar or checklist.
  3. What happens when they drop mid-flow: email, push, nothing? Use the Zeigarnik effect to remind them they started.
- Apply the Progress effect: someone seeing 30% done is likelier to finish than someone at 0%. A 0% start is a design error: start every progress bar at 20% or higher.

**Quote:** "Sub-30-day churn rarely dies to features; it dies to the right sequence of micro-interactions that deliver value before asking for effort."

**Source:** [@richardrx · 2026-04-20](https://x.com/richardrx/status/2046212675017887881)

## Deliver the promised result before teaching mechanics

**Apply when:** Your onboarding is a checklist of setup mechanics rather than a path to the outcome.

**Do:**
- Deliver the result promised in the landing-page hero. Never teach mechanics first ("create a project → add a member → configure integrations"). Deliver value first: it converts.
- Lead with the outcome: "In 2 minutes you'll see your first report → let's start with the data you already have → done, that's the insight competitors pay consultants for".
- Credit effort already spent (Progress effect): "You've done the hard part, just 3 steps left".
- Keep loops small (Zeigarnik effect): people close only loops that look closable.
- Pre-select the right plan from data you collected, instead of asking. Then offer the upsell.

**Quote:** "The gap between 5% and 15% trial conversion is in these details — not features, not price — in the sequence of micro-decisions you designed without realizing you were designing."

**Source:** [@richardrx · 2026-04-16](https://x.com/richardrx/status/2044785090832543998)

## Qualify by behavior, not by a long signup form

**Apply when:** You are weighing an 8-field signup form against email + password.

**Do:**
- Qualify by behavior, not by form: default to the minimal form and qualify later, inside the product. The "more qualified leads" argument usually loses.
- Decide friction by context ("it depends"). Apply the rule in [Put friction in the right place, not zero friction everywhere](#put-friction-in-the-right-place-not-zero-friction-everywhere).

**Evidence:** Same product, two founders: 8-field form (name, email, company, role, phone, segment, team size, how-did-you-hear) → 12% signup rate; email + password only → 34%.

**Visual:** Annotated onboarding step (DevNoodles): an ICP/intent question flagged "Zeigarnik effect" (the step progress dots) and a B2C/B2B card selector flagged "Default effect" (the B2C card is pre-badged "Mais comum") — `../assets/2042558822825239030__1.jpg`

**Source:** [@richardrx · 2026-04-10](https://x.com/richardrx/status/2042558822825239030)

## Celebrate the activation moment, don't just confirm it

**Apply when:** A user completes a hard-won first action (first transaction, first integration) and gets a static success state.

**Do:**
- Show a rising graph, not a number: it is progress and builds an emotional memory of the product.
- Engineer the peak moment at the point of highest emotional vulnerability: right after the user clears the effort. Scale motion and accomplishment to the effort invested.
- Apply the peak-end rule: users judge an experience by its emotional peak and its ending, rarely by the average.

**Evidence:** Stripe shows a rising graph (not a number) the moment the first transaction processes — the founder who integrated it at 3am remembers exactly where they were.

**Quote:** "A number would have done the job. The graph created a customer."

**Source:** [@richardrx · 2026-04-04](https://x.com/richardrx/status/2040415841628651689)

## Cut time-to-value by reorder and removal, not feature changes

**Apply when:** Your activation flow is slow and you assume the product itself is the bottleneck.

**Do:**
- Treat high TTV as a form-and-order problem, almost never product complexity. Each day to first result adds abandonment risk, and abandonment = churn.
- Run three iteration cycles with no product changes:
  1. Reduce cognitive load. Group and standardize what the user must fill in.
  2. Work with legal/compliance. Strip everything required by habit but not by actual necessity.
  3. Invert the sequence so the user feels value before facing the heaviest step.

**Evidence:** Major Brazilian payments platform: 24 days → 2.5 days to first sale (89.7% reduction), no product changes, no cutting of mandatory compliance steps.

**Visual:** Month-by-month TTV table: Jan 24.2d → Feb 19.6d → Mar 16.8d → Apr 9.3d → May 2.5d, alongside accounts created / approved / new sellers per month. — `../assets/2037583944283996418__1.jpg`

**Source:** [@richardrx · 2026-03-27](https://x.com/richardrx/status/2037583944283996418)

## Give the trial an active goal, not passive access

**Apply when:** Your trial is open-ended access with no challenge or target.

**Do:**
- Replace the passive trial ("use it if you want, cancel guilt-free"). A trial with an active goal builds commitment before billing.
- Set a recurring daily goal. Require the user to opt in and complete it. Name the mechanism: progressive commitment.
- Expect each completed day to raise the psychological cost of canceling.

**Evidence:** Wispr Flow challenges trial users to dictate 100+ words a day for 7 days — looks generous, is behavioral science.

**Source:** [@richardrx · 2026-03-26](https://x.com/richardrx/status/2037316988981174464)

## Calibrate the first step to the user's real willingness

**Apply when:** Your first onboarding step bundles setup, data import, team invites, and project creation, or demands a campaign-sized action.

**Do:**
- Judge the first task by perceived effort. Ban a first step that asks too much: imagining the cost paralyzes the user (activation-barrier effect).
- Apply two biases:
  1. Started-progress effect: show what the user has already done before what is left. A loyalty card with the first stamp pre-filled beats a blank 9-stamp card.
  2. Small-steps effect: "Create one story today" has radically lower perceived cost than "post 5×/week," even when the underlying task is identical.
- Sequence effort so the user hits first value before noticing how much they invested.

**Evidence:** Instagram A/B test made "Create 5 new public reels" the first task — for someone who barely posts weekly, that's paralyzing.

**Visual:** Bad first-step example: a weekly-progress checklist at "0% completed" whose top item is "Create 5 new public reels (0/5)." — `../assets/2036461688505909250__1.jpg`

**Quote:** "Asking for more isn't necessarily the problem; asking for all of it at once, with no progress anchor and no commitment ladder, is."

**Source:** [@richardrx · 2026-03-24](https://x.com/richardrx/status/2036461688505909250)

## Treat onboarding as the bridge between CAC and LTV

**Apply when:** Users enter the trial without intent to a result and ghost before ever paying.

**Do:**
- Treat onboarding as the bridge from CAC to LTV and the point of maximum leverage to expand revenue.
- Track activation cost.
- Expect cancellation on day one. Stripe's billing reminder only formalizes it.
- Apply two fixes:
  1. Turn support into UX. Treat every onboarding support ticket as a design failure. Map recurring setup questions. Convert the answers into features or in-flow tooltips.
  2. Compress TTV obsessively. Make the user experience the product's core promise in the least time possible. If they must configure 5 screens before any result, you have already lost.

**Quote:** "Letting a user into the trial without intent of a result isn't self-service. Design's job doesn't end at signup — that's where it starts paying you back."

**Source:** [@richardrx · 2026-03-13](https://x.com/richardrx/status/2032485654811083005)

## Pick onboarding patterns by awareness × flow complexity

**Apply when:** Choosing or combining onboarding patterns for a new flow (SaaS, PLG, B2B early stage).

**Do:**
- Pick the onboarding that removes friction and delivers value early for your users.
- Treat the nine patterns as behavior-shaping mechanisms, not UI components.

**The nine patterns (pattern → ideal use / tradeoff):**
1. **Welcome modal** → high-awareness ICP or low-complexity products; easy to build, easy to ignore.
2. **Wizard / product tour** → B2B and complex/high-cost-of-error flows (fintech, compliance); long tours cause boredom and need constant upkeep.
3. **Contextual tooltips** → advanced/secondary features; slashes support tickets but users may miss them if contrast is poor.
4. **Empty state** (Richard's favorite) → dashboards, lists, data-dependent areas; if executed well it's mandatory, directs the first action and accelerates TTV.
5. **Personalization** → products serving many ICPs with different journeys; great CRM data, but too long kills signup conversion.
6. **Checklists** → critical flows with mandatory prerequisites (webhook, KYC); exploits the Zeigarnik effect, but a long list breeds aversion — every item must move toward value, no bureaucratic tasks.
7. **Goal-setting** → habit products (finance, productivity, health); uses commitment bias, but a broken goal can break the emotional contract.
8. **Sample data** → sell the dream of a full, organized product before the user inputs anything (distinct from skeleton screens).
9. **Use cases / demos** → products burning expensive resources (AI tokens) with infinite outputs; show max potential without forcing creativity from scratch.

**Selection rule (two axes):** Score **awareness level** (low = needs guidance; high = needs speed) and **flow complexity** (high = needs structure). Pick patterns from the four cases:
- low awareness + high complexity → tours + checklists + personalization
- low awareness + low complexity → modal + empty state
- high awareness + high complexity → checklist + tooltip + empty state
- high awareness + low complexity → modal + empty state (then get out of the user's way)

**Build vs. buy:** Treat it as a financial/operational decision, not an aesthetic one.
- Buy (Wistia, PostHog, Sprig) when speed is critical, dev is overloaded, or you are running A/B tests.
- Build when onboarding is strategic, you need perfect aesthetic integration, or you must avoid third-party dependence.

**Quote:** "Onboarding's job isn't to teach the user — nobody likes an instruction manual — it's to remove cognitive effort and deliver utility as fast as possible. TTV correlates directly with churn."

**Source:** [@richardrx · 2026-02-04](https://x.com/richardrx/status/2019019293761941566)
