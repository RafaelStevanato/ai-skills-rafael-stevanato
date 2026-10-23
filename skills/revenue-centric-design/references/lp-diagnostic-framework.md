# LP Diagnostic Framework

Run this 10-step diagnostic, in order, before you redesign a landing page (LP). Attribution: see [Source](#source). License: [LICENSE](../LICENSE).

## The Core Insight

> "Percebeu que o visual aparece quase no final?"

Treat the visual layer as almost last (Step 9 of 10). Before you open Figma, answer 8 questions: who arrives, where they came from, what they are looking for, what they already know, what problem they are trying to solve, what result they expect, what objections they carry, what action you want to generate.

## SOP: The 10-Step LP Diagnostic

### Step 1: Context — Where did this user come from?

Continue the conversation that started before the "landing".

**Apply when:** Diagnosing any LP, especially when paid traffic scales and conversion drops.

**Questions:**
1. What's the traffic source? (Meta ads, Google, outbound, SEO, founder post, referral?)
2. What happened before the click? What promise brought them here?
3. Desktop or mobile?
4. First contact with the company or returning visitor?
5. Dedicated session or distracted mobile user?

**Failure mode:** Paying expensive CPCs to send users to a page that does not match the ad's promise.

**Voice:** "Se você está pagando caro para levar um usuário até uma LP, cada desalinhamento entre anúncio e página pode virar dinheiro queimado."

### Step 2: ICP — Who is this page selling to?

Name one specific ICP. Generic ICP definitions ("B2B companies with 10-500 employees") are useless.

**Apply when:** The LP uses vague, broad language, or the copy has not evolved to match learned segments.

**Questions:**
1. What job does this customer need to accomplish?
2. What problem are they trying to solve?
3. What context are they living in?
4. How much does this problem cost them?
5. Which segment delivers best LTV, lowest churn, highest expansion potential?

**Failure mode:** Selling the same way to a 15-person startup and a 300-person enterprise. Pain, urgency, objections, acceptable ticket, and reason to buy all change.

**Voice:** "Quer me falar que tanto o G4 quanto uma oficina de bairro são seu ICP?"

### Step 3: Awareness Level — What does this user already know?

The visitor's knowledge level changes the page structure. Schwartz defines 5 stages; use these 3 operational levels.

**Apply when:** Structuring any LP, or one page serves traffic sources with different awareness.

|Level|User state|Page must do|
|---|---|---|
|**Unaware**|Problem exists but isn't clear to user|Build perception, show impact of current scenario, create space for solution|
|**Problem-aware**|Pain is clear, looking for a way out|Structure: pain → impact → opportunity → mechanism → solution → proof → offer → FAQ|
|**Solution-aware**|Category known, comparing alternatives|Move faster to mechanism, differentiation, proof, reason to choose you|

**Failure mode:** Selling "Solution" to the "Unaware" = proposing on a first date. Build different LPs for different channels, segments, and funnel moments.

**Visual reference:** Eugene Schwartz's 5 awareness stages diagram (Unaware → Problem → Solution → Product → Most Aware) — `../assets/2011427153133351046__3.jpg`

### Step 4: Message — What's being sold here?

"What's being sold?" must be understandable in seconds and matter to **this ICP**.

**Apply when:** The hero uses generic positioning, feature-first language, or internal jargon.

**Questions:**
1. What's being sold here?
2. Can you understand it in a few seconds?
3. Does this matter to this ICP?

**Failure modes:** Ban these hero lines. Each says nothing: "Plataforma all-in-one" (all-in-one platform), "IA de última geração" (state-of-the-art AI), "Transforme seu negócio" (transform your business).

**Move:** Communicate (1) what problem the page solves and (2) what result that produces. Match the channel: if the ad promises churn reduction, develop that conversation.

**Visual reference:** XKCD comic on the gap between what users want and what university sites offer.

### Step 5: Sales Structure — Is there a narrative progression?

Read the page as a narrative that leads the user from the first question to the decision.

**Expected structure:**
```
Problem → Consequence → Opportunity → Mechanism → Solution → Proof → Offer → Risk Reduction → CTA
```

**Rule:** A small difference in LP efficiency becomes a large difference in CAC, opportunity volume, and revenue from the same investment.

**Voice:** "A LP como parte do sistema de aquisição, não como página isolada."

### Step 6: Value Proposition — Does the hero work?

Put three elements in the hero.

**Apply when:** Auditing the above-the-fold section of any LP.

|Component|Job|
|---|---|
|**Headline**|Speaks to the problem or result (promise) that matters to this ICP|
|**Description (subheadline)**|Explains how the product delivers that|
|**Trust element**|Answers "Why should I believe you?" — clients, numbers, logos, results, demo, guarantee, certifications|

**Move:** For SaaS at scale, show **specific evidence from the ICP you want to attract**, not a collection of unknown logos: a case from a similar company sells more than ten unfamiliar logos.

### Step 7: Proof & Objections — Are objections broken during the narrative?

Break objections throughout the page, not only in the FAQ.

|Objection|Counter|
|---|---|
|Price|Comparative proving better cost-benefit|
|Implementation|"Setup in 5 minutes, see how"|
|Security|"Secure site seal"|
|Learning curve|"See how this company transformed their process in 3 days with X"|
|Team required|"You alone can use it, assisted by up to 50 agents"|

**Ticket scale:** Scale objection handling with ticket size. A R$100 subscription can be impulsive. A R$1,000 or R$10,000 purchase involves more people, questions, and perceived risk.

**Proof principle:** In the AI era, a real WhatsApp screenshot, a customer-recorded video, or a result capture carries more credibility than a perfect card written by marketing.

**Visual reference:** The "paredão" (wall): a social proof wall where each card links to the original LinkedIn post.

### Step 8: Friction + CTA — What's blocking conversion?

Hunt everything that can hinder conversion.

**Apply when:** Auditing the conversion path and form experience.

**Friction checklist:**
- [ ] Too many fields (cognitive overload)
- [ ] Too many decisions (analysis paralysis)
- [ ] Too many steps
- [ ] Confusing offer
- [ ] Hidden pricing without reason
- [ ] Form asking unnecessary information
- [ ] CTA doesn't explain the next step

|Lower commitment|Higher commitment|
|---|---|
|"Start free"|"Schedule a demo"|
|"Test for 14 days"|"Talk to sales"|

Each CTA places a different effort burden on the user: choose with that burden in mind.

**Move:** Make the primary action clear. Show it at the right points, especially after arguments that increase purchase intent. Create the transition: "this seems relevant to me" → "I'll take the next step".

### Step 9: Attention & UI — How does the interface direct attention?

Create rhythm, hierarchy, and focal points.

**Apply when:** Reviewing visual design, only **after** Steps 1-8 are diagnosed.

**Failure mode:** Every section has the same composition (image right, text block left).

**Moves:**
- Vary composition when it helps the narrative
- Change density, create contrast
- Highlight important information (skeuomorphism helps)
- Draw attention to proofs and CTAs
- Control reading rhythm

Check typography, color, grid, spacing, components, images, and animations. Give each decision a clear function.

### Step 10: Strangeness — Where's the personality?

Add personality after the structure works: an unexpected image, a metaphor, an absurd illustration, an unusual composition, or an easter egg.

**Apply when:** The page works structurally but feels generic, with the same visual language as everyone in the category.

**Rule:** Strangeness creates attention, differentiation, and memory, and supports brand positioning.

**Constraint:** Give strangeness a function (but not always).

**Visual reference:** Car silhouettes image: "Which cars do you recognize here?"

## The Framework in Practice

### Diagnostic sequence
```
1. Context    → 2. ICP        → 3. Awareness → 4. Message   → 5. Structure
     ↓              ↓               ↓             ↓              ↓
6. Hero       → 7. Proof      → 8. Friction  → 9. UI        → 10. Strangeness
```

### Connect to metrics (for SaaS in traction)

Tie the diagnostic to real numbers:
- **CAC** — Cost per Acquired Customer
- **Conversion Rate** — Overall and by stage
- **Activation** — First value moment reached
- **Trial to Paid** — Conversion of trials
- **Revenue** — Not leads, revenue
- **LTV** — Lifetime Value
- **Churn** — Yes, the LP can affect churn (especially if it makes promises the product can't keep)

### The LP doesn't exist in a vacuum

> "A LP faz parte de um sistema que começa no canal de aquisição e termina em receita."

Check where the sale breaks before you redesign an LP:
- Traffic (wrong people arriving)
- ICP (talking to everyone, convincing no one)
- Message (doesn't resonate)
- Awareness level (selling solution to unaware)
- Offer (not compelling)
- Proof (insufficient for the ask)
- Something else entirely

More traffic, salespeople, creatives, or acquisition spend do not fix this.

## Theoretical Foundations

|Framework element|Origin|
|---|---|
|5 Levels of Awareness|Eugene Schwartz, *Breakthrough Advertising* (1966)|
|Problem → Solution structure|PAS (Problem-Agitate-Solution), AIDA|
|Hero section pattern|Copyhackers (Joanna Wiebe), StoryBrand (Donald Miller)|
|Objection handling in narrative|Classic copywriting principle|
|"Strangeness" / Pattern interrupt|Marketing differentiation theory|
|Context-first diagnosis|Growth/performance marketing practice|
|Metrics connection|Modern SaaS operations (CAC, LTV, Churn)|

## Source

**Framework author.** Richard ([@richardrx](https://x.com/richardrx)) — "Design for startups"

**Original article.** [Um framework para descobrir por que uma LP não converte](https://x.com/richardrx/status/2089755232511123628) — published 2026-08-18

## Integration with RCD Workflow

Use this framework as the **diagnostic phase** before you apply specific RCD principles:

1. Run the 10-step diagnostic
2. Identify the breaking point(s)
3. Open the relevant RCD reference file for principles addressing that break
4. Apply principles with mechanism, citation, and evidence ([SKILL.md](../SKILL.md) Workflow step 4)
5. Log to `rcd-log.md` ([SKILL.md](../SKILL.md) Workflow steps 1 and 6, and Project log)

|Breaking point identified|Open RCD reference|
|---|---|
|Steps 1-4 (Context, ICP, Awareness, Message)|[positioning-icp-and-gtm](positioning-icp-and-gtm.md), [conversion-and-landing-pages](conversion-and-landing-pages.md)|
|Step 5 (Structure)|[conversion-and-landing-pages](conversion-and-landing-pages.md)|
|Step 6 (Hero/Value Prop)|[conversion-and-landing-pages](conversion-and-landing-pages.md)|
|Step 7 (Proof & Objections)|[behavioral-science-toolkit](behavioral-science-toolkit.md), [conversion-and-landing-pages](conversion-and-landing-pages.md)|
|Step 8 (Friction + CTA)|[conversion-and-landing-pages](conversion-and-landing-pages.md), [onboarding-and-activation](onboarding-and-activation.md)|
|Steps 9-10 (UI, Strangeness)|[product-strategy-and-features](product-strategy-and-features.md)|
|Metrics disconnected|[metrics-and-experimentation](metrics-and-experimentation.md)|
