# LP Diagnostic Framework

- Attribution: Richard ([@richardrx](https://x.com/richardrx)), "Design for startups". Original article: [Um framework para descobrir por que uma LP não converte](https://x.com/richardrx/status/2089755232511123628).
- Run this 10-step diagnostic before you redesign any landing page (LP).
- Use it to find where a sale breaks before you touch visual design.
- Base: Eugene Schwartz awareness levels, PAS/AIDA narrative structures, and modern CRO practices.
- Run the steps in order, from Step 1 to Step 10.
- Use [SKILL.md](../SKILL.md) for the workflow, the completion criterion, and the project log rules.

---

## The Core Insight

> "Percebeu que o visual aparece quase no final?"

*(Gloss: "Did you notice that the visual layer appears almost at the end?")*

- Treat the visual layer as one of the last steps (Step 9 of 10).
- Never open Figma before you answer these 8 context questions.
  1. Who arrives?
  2. Where did they come from?
  3. What are they looking for?
  4. What do they already know?
  5. What problem are they trying to solve?
  6. What result do they expect?
  7. What objections do they carry?
  8. What action do you want to generate?

---

## SOP: The 10-Step LP Diagnostic

### Step 1: Context — Where did this user come from?

**Principle.**
- Make the LP continue the conversation that started before the "landing".
- Expect a different expectation from each traffic source.
- Count any misalignment between ad and page as burned money.

**Apply when.**
- Diagnose any LP.
- Prioritize this step when paid traffic scales and conversion drops.

**The diagnostic questions.**
1. What's the traffic source? (Meta ads, Google, outbound, SEO, founder post, referral?)
2. What happened before the click? What promise brought them here?
3. Desktop or mobile?
4. First contact with the company or returning visitor?
5. Dedicated session or distracted mobile user?

**The failure mode.**
- Flag this failure: paying expensive CPCs to send users to a page that doesn't match the ad's promise.
- Count each mismatch as money burned: every mismatch = money burned.

**Voice.** "Se você está pagando caro para levar um usuário até uma LP, cada desalinhamento entre anúncio e página pode virar dinheiro queimado."

*(Gloss: "If you pay a high price to bring a user to an LP, each mismatch between ad and page can turn into burned money.")*

---

### Step 2: ICP — Who is this page selling to?

**Principle.**
- Name one specific ICP for the page.
- Expect communication to try to speak to everyone as a product matures. It convinces no one.
- Ban generic ICP definitions such as "B2B companies with 10-500 employees". They are useless.

**Apply when.**
- The LP uses vague, broad language.
- The product has traction but the copy has not evolved to match learned segments.

**The diagnostic questions.**
1. What job does this customer need to accomplish?
2. What problem are they trying to solve?
3. What context are they living in?
4. How much does this problem cost them?
5. Which segment delivers best LTV, lowest churn, highest expansion potential?

**The failure mode.**
- Flag this failure: trying to sell the same way to a 15-person startup and a 300-person enterprise.
- Expect the pain to change between the two.
- Expect the urgency to change.
- Expect the objections to change.
- Expect the acceptable ticket to change.
- Expect the reason someone buys to change.

**Voice.** "Quer me falar que tanto o G4 quanto uma oficina de bairro são seu ICP?"

*(Gloss: "Do you want to tell me that both G4 and a neighborhood repair shop are your ICP?")*

---

### Step 3: Awareness Level — What does this user already know?

**Principle.**
- Set the page structure from the visitor's knowledge level.
- Map the visitor to Eugene Schwartz's 5 stages.
- Simplify the 5 stages to 3 operational levels.

**Apply when.**
- Structure any LP.
- The same page serves multiple traffic sources with different awareness.

**The three operational levels.**

| Level | User state | Page must do |
|-------|-----------|--------------|
| **Unaware** | Problem exists but isn't clear to user | Build perception, show impact of current scenario, create space for solution |
| **Problem-aware** | Pain is clear, looking for a way out | Structure: pain → impact → opportunity → mechanism → solution → proof → offer → FAQ |
| **Solution-aware** | Category known, comparing alternatives | Move faster to mechanism, differentiation, proof, reason to choose you |

**The failure mode.**
- Never sell "Solution" to the "Unaware". It equals proposing on a first date.
- Build different LPs for different channels, segments, and funnel moments.
- Accept that no perfect message exists for everyone.

**Visual reference.** Eugene Schwartz's 5 awareness stages diagram (Unaware → Problem → Solution → Product → Most Aware).
- Image: `../assets/2011427153133351046__3.jpg`

---

### Step 4: Message — What's being sold here?

**Principle.**
- Make "What's being sold?" understandable in seconds.
- Make the answer matter to **this ICP**.

**Apply when.**
- The hero uses generic positioning.
- The hero uses feature-first language.
- The hero uses internal jargon.

**The diagnostic questions.**
1. What's being sold here?
2. Can you understand it in a few seconds?
3. Does this matter to this ICP?

**The failure modes.**
- Ban "Plataforma all-in-one" (all-in-one platform). It says nothing.
- Ban "IA de última geração" (state-of-the-art AI). It says nothing.
- Ban "Transforme seu negócio" (transform your business). It says nothing.

**The move.**
- Communicate (1) what problem the page solves.
- Communicate (2) what result that produces.
- Match the channel.
- Example: if the ad promises churn reduction, develop that conversation on the page.

**Visual reference.** XKCD comic satirizing the gap between what users want vs. what university sites offer. The image is not in `../assets/`.

---

### Step 5: Sales Structure — Is there a narrative progression?

**Principle.**
- Read the page as a narrative.
- Build a progression that leads the user from the first question to the decision.

**Apply when.**
- The page reads as disconnected sections rather than a coherent argument.

**The expected structure.**
```
Problem → Consequence → Opportunity → Mechanism → Solution → Proof → Offer → Risk Reduction → CTA
```

**Why it matters.**
- Treat a small difference in LP efficiency as a large difference in CAC, opportunity volume, and revenue from the same investment.

**Voice.** "A LP como parte do sistema de aquisição, não como página isolada."

*(Gloss: "The LP as part of the acquisition system, not as an isolated page.")*

---

### Step 6: Value Proposition — Does the hero work?

**Principle.**
- Put three elements in the hero: headline, description, and trust element.

**Apply when.**
- Audit the above-the-fold section of any LP.

**The three components.**

| Component | Job |
|-----------|-----|
| **Headline** | Speaks to the problem or result (promise) that matters to this ICP |
| **Description (subheadline)** | Explains how the product delivers that |
| **Trust element** | Answers "Why should I believe you?" — clients, numbers, logos, results, demo, guarantee, certifications |

**The move.**
- For SaaS at scale, show **specific evidence from the ICP you want to attract**.
- Never show a collection of unknown logos instead.
- Prefer a case from a similar company. It sells more than ten unfamiliar logos.

---

### Step 7: Proof & Objections — Are objections broken during the narrative?

**Principle.**
- Break objections throughout the page, not just in the FAQ.

**Apply when.**
- The page leaves objections unaddressed until (or only in) the FAQ section.

**Common objections and their counters.**

| Objection | Counter |
|-----------|---------|
| Price | Comparative proving better cost-benefit |
| Implementation | "Setup in 5 minutes, see how" |
| Security | "Secure site seal" |
| Learning curve | "See how this company transformed their process in 3 days with X" |
| Team required | "You alone can use it, assisted by up to 50 agents" |

**Why it scales with ticket.**
- Scale objection handling with the ticket size.
- Expect a R$100 subscription to be impulsive.
- Expect a R$1,000 or R$10,000 purchase to involve more people, more questions, and more perceived risk.
- Make the LP help advance that decision.

**The proof principle.**
- In the AI era, use a real WhatsApp screenshot, a customer-recorded video, or a result capture as proof.
- Expect these to carry more credibility than a perfect card written by marketing.

**Visual reference.** The "paredão" (wall): a social proof wall where each card links to the original LinkedIn post. The image is not in `../assets/`.

---

### Step 8: Friction + CTA — What's blocking conversion?

**Principle.**
- Hunt everything that can hinder conversion.

**Apply when.**
- Audit the conversion path and the form experience.

**The friction checklist.**
- [ ] Too many fields (cognitive overload)
- [ ] Too many decisions (analysis paralysis)
- [ ] Too many steps
- [ ] Confusing offer
- [ ] Hidden pricing without reason
- [ ] Form asking unnecessary information
- [ ] CTA doesn't explain the next step

**The commitment level insight.**

| Lower commitment | Higher commitment |
|------------------|-------------------|
| "Start free" | "Schedule a demo" |
| "Test for 14 days" | "Talk to sales" |

- Choose each CTA with its effort burden in mind. Each CTA places a different effort burden on the user.

**The move.**
- Make the primary action clear.
- Show the primary action at the right points on the page.
- Show it especially after arguments that increase purchase intent.
- Create the transition: "this seems relevant to me" → "I'll take the next step".

---

### Step 9: Attention & UI — How does the interface direct attention?

**Principle.**
- Create rhythm, hierarchy, and focal points on the page.

**Apply when.**
- Run a visual design review only **after** Steps 1-8 are diagnosed.

**The failure mode.**
- Flag this failure: every section has exactly the same composition (image right, text block left).
- Expect the experience to become predictable.

**The moves.**
- Vary composition when it helps the narrative
- Change density, create contrast
- Highlight important information (skeuomorphism helps)
- Draw attention to proofs and CTAs
- Control reading rhythm

**What to notice.**
- Check typography, color, grid, spacing, components, images, and animations.
- Give each decision a clear function.

---

### Step 10: Strangeness — Where's the personality?

**Principle.**
- Add personality after you solve the structure.
- Use one of these: an unexpected image, a metaphor, an absurd illustration, an unusual composition, or an easter egg.

**Apply when.**
- The page works structurally but feels generic, with the same visual language as everyone in the category.

**Why it matters.**
- Use strangeness to create attention, differentiation, and memory.
- Use strangeness to support brand positioning.
- Expect a growing company to fall into pages with the same visual language, layouts, and words as everyone else.

**The constraint.**
- Give strangeness a function (but not always).

**Visual reference.** Car silhouettes image: "Which cars do you recognize here?" The image is not in `../assets/`.

---

## The Framework in Practice

### Diagnostic sequence
```
1. Context    → 2. ICP        → 3. Awareness → 4. Message   → 5. Structure
     ↓              ↓               ↓             ↓              ↓
6. Hero       → 7. Proof      → 8. Friction  → 9. UI        → 10. Strangeness
```

### Connect to metrics (for SaaS in traction)

- Tie the diagnostic to real numbers:
  - **CAC** — Cost per Acquired Customer
  - **Conversion Rate** — Overall and by stage
  - **Activation** — First value moment reached
  - **Trial to Paid** — Conversion of trials
  - **Revenue** — Not leads, revenue
  - **LTV** — Lifetime Value
  - **Churn** — Yes, the LP can affect churn (especially if it makes promises the product can't keep)

### The LP doesn't exist in a vacuum

> "A LP faz parte de um sistema que começa no canal de aquisição e termina em receita."

*(Gloss: "The LP is part of a system that starts at the acquisition channel and ends in revenue.")*

- Find where the sale is breaking before you redesign an LP.
- Check these possible breaking points:
  - Traffic (wrong people arriving)
  - ICP (talking to everyone, convincing no one)
  - Message (doesn't resonate)
  - Awareness level (selling solution to unaware)
  - Offer (not compelling)
  - Proof (insufficient for the ask)
  - Something else entirely
- Expect an LP that keeps losing opportunities in the middle of the system to keep leaking water.
- This stays true when you increase traffic, hire more salespeople, produce more creatives, or put more money into acquisition.

---

## Theoretical Foundations

- Credit each framework element to its origin in this table.

| Framework element | Origin |
|-------------------|--------|
| 5 Levels of Awareness | Eugene Schwartz, *Breakthrough Advertising* (1966) |
| Problem → Solution structure | PAS (Problem-Agitate-Solution), AIDA |
| Hero section pattern | Copyhackers (Joanna Wiebe), StoryBrand (Donald Miller) |
| Objection handling in narrative | Classic copywriting principle |
| "Strangeness" / Pattern interrupt | Marketing differentiation theory |
| Context-first diagnosis | Growth/performance marketing practice |
| Metrics connection | Modern SaaS operations (CAC, LTV, Churn) |

---

## Source

**Framework author.** Richard ([@richardrx](https://x.com/richardrx)) — "Design for startups"

**Original article.** [Um framework para descobrir por que uma LP não converte](https://x.com/richardrx/status/2089755232511123628) — published 2026-08-18

- Keep this attribution and both links when you reuse any step of this framework.

---

## Integration with RCD Workflow

- Use this framework as the **diagnostic phase** before you apply specific RCD principles:

1. Run the 10-step diagnostic
2. Identify the breaking point(s)
3. Open the relevant RCD reference file for principles addressing that break
4. Apply principles with mechanism, citation, and evidence. Follow the completion criterion in [SKILL.md](../SKILL.md) (Workflow step 4).
5. Log to `rcd-log.md`. Follow the project log rules in [SKILL.md](../SKILL.md) (Workflow steps 1 and 6, and Project log).

- Use the table below to pick the reference file for each breaking point.
- Use the topic router in [SKILL.md](../SKILL.md) to pick a file by topic.

| Breaking point identified | Open RCD reference |
|--------------------------|-------------------|
| Steps 1-4 (Context, ICP, Awareness, Message) | [positioning-icp-and-gtm](positioning-icp-and-gtm.md), [conversion-and-landing-pages](conversion-and-landing-pages.md) |
| Step 5 (Structure) | [conversion-and-landing-pages](conversion-and-landing-pages.md) |
| Step 6 (Hero/Value Prop) | [conversion-and-landing-pages](conversion-and-landing-pages.md) |
| Step 7 (Proof & Objections) | [behavioral-science-toolkit](behavioral-science-toolkit.md), [conversion-and-landing-pages](conversion-and-landing-pages.md) |
| Step 8 (Friction + CTA) | [conversion-and-landing-pages](conversion-and-landing-pages.md), [onboarding-and-activation](onboarding-and-activation.md) |
| Steps 9-10 (UI, Strangeness) | [product-strategy-and-features](product-strategy-and-features.md) |
| Metrics disconnected | [metrics-and-experimentation](metrics-and-experimentation.md) |
