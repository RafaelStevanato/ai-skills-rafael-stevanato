# Dashboards & Data Visualization (Retention Surface)

Attribution: Richard ([@richardrx](https://x.com/richardrx), "Richard — Design for startups"), translated from Portuguese. License: [LICENSE](../LICENSE).

Treat dashboards as retention surfaces, not reporting tools. A good dashboard eliminates churn: it delivers so much value that the user feels the need to return.

See also: [revenue-centric-design.md > Make the dashboard answer "what do I do now?"](revenue-centric-design.md#make-the-dashboard-answer-what-do-i-do-now)

## Removing information creates room for direction — the dashboard should say what to do with the data

**Principle:** Good product design is mostly *removing*: show less, and give clarity to what remains, based on what the user needs on that screen. The freed space gives direction: the app stops showing data and says what to do with it. This is the actionable layer.

**Apply when:** A dashboard shows everything but guides nothing.

**Do:**
- Compare before and after. Before: a giant number fights the chart below, tabs sit inside tabs, bars tell nothing. After: the chart breathes, the selected month pops, and a card has space to warn "two installments end in August, save what's left over."
- Show less to shorten the learning curve. A product that guides gives a reason to return, so engagement becomes retention (+LTV).

**Source:** [@richardrx · 2026-07-10](https://x.com/richardrx/status/2075623473565647202)

## A good dashboard informs at a glance — like a car dashboard, the user must focus on where they're going

**Principle:** A good dashboard is informative and effortless to read. Its goal is to maximize LTV, not to inform.

**Apply when:** You design or audit any analytics/admin dashboard.

**Do:**
1. Define who the dashboard is for (ICP). Information without context is spam.
2. Cut everything not useful: an element that does not earn its place is noise. Count each extra line, card or icon as cognitive load, unless it is indispensable for consuming the data.
3. Apply the F-pattern: put the main KPI top-left.
4. Attach meaning to data: write "You generated 500 tickets" → "That's 15% above your monthly target". Use framing ("You're in the top 20%") for belonging/social proof.
5. Design for the empty state: write good empty states and guide users to fill them.
6. Drive to action, not excess. An actionable panel beats a "complete" one (GA4 has everything, little usable).
7. Personalize by role: never give a CEO and a marketing analyst the same panel.

**Visual:** An annotated repair-shop dashboard ("Quadro Geral") with seven callouts: 01 logo, 02 sidebar navigation, 03 the main revenue KPI (R$57,257, ↗6.2% vs last month) top-left, 04 average ticket, 05 the Max / 12-month / 3-month / 30-day range tabs, 06 a single primary action ("Adicionar OS"), 07 the composition card's ⋮ options menu (personalize what the panel shows). It also shows a revenue-composition donut, a 12-month revenue history and services / parts / outsourcing breakdown cards — `../assets/2000930776636940333__1.jpg`

**Quote:** "Information without context is spam."

**Source:** [@richardrx · 2025-12-16](https://x.com/richardrx/status/2000930776636940333)

## Dashboards: not a pile of gauges — every extra indicator slows the scan for what's actionable

**Principle:** Never build a pile of gauges. More information raises cognitive load and lengthens the scan for what is important and actionable. Build around the main indicators of the business.

**Apply when:** Stakeholders keep asking to add "just one more" KPI.

**Do:**
- Pick the KPI shortlist for the business type. Leave the rest off the panel.
  - E-commerce (6): conversion rate, average order value (AOV), CAC, customer lifetime value (CLV), cart-abandonment rate, ad return (ROAS/CPA).
  - SaaS (5): MRR, churn, CAC, LTV, ARPU.
  - Apps (7): DAU, MAU, retention rate, ARPU, app-store rating, engagement (session length, frequency), cost per install (CPI).

**Evidence:** The original "dashboard" was a carriage board that kept horse mud off the passengers. The first Ford T kept it with just an ignition key and an ammeter; gauges accumulated from there. That industrial-era aesthetic survives in luxury cars and watches (the "complications" on a Patek Philippe or a Pagani), where it is interesting, but not in a software dashboard.

**Source:** [@richardrx · 2025-11-04](https://x.com/richardrx/status/1985828780838097317)
