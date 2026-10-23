# Dashboards & Data Visualization (Retention Surface)

Attribution: Richard (@richardrx), "Richard — Design for startups", translated from Portuguese.
Each entry links to its source post.
Return to [SKILL.md](../SKILL.md).

Rules for every dashboard:
- Treat dashboards as retention surfaces, not reporting tools.
- Design every dashboard to eliminate churn.
- Deliver so much value that the user feels the need to return.

See also: [revenue-centric-design.md > Make the dashboard answer "what do I do now?"](revenue-centric-design.md#make-the-dashboard-answer-what-do-i-do-now)

## Removing information creates room for direction — the dashboard should say what to do with the data

**Principle:**
- Do most product design work by removing: show less.
- Give clarity to what remains, based on what the user needs on that screen.
- Use the freed space for direction.
- Make the app stop showing data and start saying what to do with it. This is the actionable layer.

**Apply when:**
- A dashboard shows everything but guides nothing.

**Do:**
- Compare before and after.
- Before: a giant number fights the chart below.
- Before: tabs sit inside tabs.
- Before: bars tell nothing.
- After: the chart breathes.
- After: the selected month pops.
- After: a card has space to warn "two installments end in August, save what's left over."
- Cut information to shorten the learning curve.
- Guide the user. A product that guides gives a reason to return.
- Expect engagement to become retention (+LTV).

**Source:** [@richardrx · 2026-07-10](https://x.com/richardrx/status/2075623473565647202)

## A good dashboard informs at a glance — like a car dashboard, the user must focus on where they're going

**Principle:**
- Make the dashboard informative and effortless to read.
- Put the main KPI top-left (F-pattern).
- Keep an element only if it earns its place. Treat every other element as noise.
- Aim to eliminate churn and maximize LTV, not to inform.
- Deliver value so large that the user feels the need to return.

**Apply when:**
- Design or audit any analytics/admin dashboard.

**Do:**
1. Define who the dashboard is for (ICP).
   - Information without context is spam.
2. Cut everything not useful.
   - Count each extra line, card or icon as cognitive load.
   - Keep it only if it is indispensable for consuming the data.
3. Apply the F-pattern.
   - Put the main KPI top-left.
4. Attach meaning to data.
   - Write "You generated 500 tickets" → "That's 15% above your monthly target".
   - Use framing ("You're in the top 20%") for belonging/social proof.
5. Design for the empty state.
   - Write good empty states.
   - Guide users to fill them.
6. Drive to action, not excess.
   - An actionable panel beats a "complete" one (GA4 has everything, little usable).
7. Personalize by role.
   - Never give a CEO and a marketing analyst the same panel.

**Visual:** An annotated repair-shop dashboard ("Quadro Geral") with seven callouts:
- 01: logo.
- 02: sidebar navigation.
- 03: the main revenue KPI (R$57,257, ↗6.2% vs last month) top-left.
- 04: average ticket.
- 05: the Max / 12-month / 3-month / 30-day range tabs.
- 06: a single primary action ("Adicionar OS").
- 07: the composition card's ⋮ options menu (personalize what the panel shows).
- The dashboard also shows a revenue-composition donut, a 12-month revenue history and services / parts / outsourcing breakdown cards.
- Image: `../assets/2000930776636940333__1.jpg`

**Quote:** "Information without context is spam."

**Source:** [@richardrx · 2025-12-16](https://x.com/richardrx/status/2000930776636940333)

## Dashboards: not a pile of gauges — every extra indicator slows the scan for what's actionable

**Principle:**
- Never build a software dashboard as a pile of gauges.
- Know that more information on screen raises cognitive load.
- Know that more information lengthens the scan for what is important and actionable.
- Build the dashboard around the main indicators of the business.

**Apply when:**
- Stakeholders keep asking to add "just one more" KPI.

**Do:**
- Pick the KPI shortlist for the business type.
- Leave the rest off the panel.
- E-commerce, 6 KPIs: conversion rate, average order value (AOV), CAC, customer lifetime value (CLV), cart-abandonment rate, ad return (ROAS/CPA).
- SaaS, 5 KPIs: MRR, churn, CAC, LTV, ARPU.
- Apps, 7 KPIs: DAU, MAU, retention rate, ARPU, app-store rating, engagement (session length, frequency), cost per install (CPI).

**Evidence:**
- The original "dashboard" was a board on carriages that kept horse mud off the passengers.
- The first Ford T kept the design with just an ignition key and an ammeter.
- Gauges accumulated from there.
- That industrial-era aesthetic survives in luxury cars and watches: the "complications" on a Patek Philippe or a Pagani.
- It is interesting there. It is not interesting in a software dashboard.

**Source:** [@richardrx · 2025-11-04](https://x.com/richardrx/status/1985828780838097317)
