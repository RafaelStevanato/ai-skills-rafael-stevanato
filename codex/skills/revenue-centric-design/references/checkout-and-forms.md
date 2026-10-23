# Checkout & Forms (Conversion-Completion Layer)

Attribution: Richard ([@richardrx](https://x.com/richardrx), "Richard — Design for startups"), translated from Portuguese. License: [LICENSE](../LICENSE).

## Friction kills conversion — field count, input type, and perceived risk all compound

**Principle:** Perceived effort differs from real effort: 5 steps with 2 fields per screen can beat 2 screens with 7 fields each.

**Apply when:** You optimize lead forms, pre-checkout or signup.

**Do:**
- Cut fields: more fields lower conversion. Text fields usually have less impact. Dropdowns and textareas hurt more. A phone field, or any data that raises perceived risk or invasiveness, drops conversion.
- Count perceived effort, not steps. A screen full of text, warnings and secondary info raises cognitive load without interaction.
- Ask: how much effort can I remove without destroying the business value of that data?
- Add breathing room, remove noise, set a clearer hierarchy. Make the form look like a corridor, not an interrogation room.
- Cut friction at trial signup and checkout. Add calibrated friction only at three spots: card-upfront trial, mandatory onboarding, enterprise demo form. See [Put friction in the right place](onboarding-and-activation.md#put-friction-in-the-right-place-not-zero-friction-everywhere).

**Evidence:** HubSpot study across 40,000+ landing pages: 3-field forms convert above 25%, and adding fields trends conversion down. A phone field drops conversion to ~13.5% vs 19% without.

**Source:** [@richardrx · 2026-08-12](https://x.com/richardrx/status/2087502085151424711)

## Microcopy at the point of fraud risk beats friction everywhere else

**Principle:** Protect the user from the real environment of the product, especially in low-trust economies. One line of microcopy in the right place prevents scams that cost more than the friction of adding it.

**Apply when:** Users get scammed through a flow your product enables (delivery PIN sharing, social engineering).

**Do:**
- Add microcopy at the exact risk moment: "Never share your number outside the app. The store and courier already have your contact via chat."
- Use transparency as the antidote in low-trust verticals (auto repair, delivery).

**Quote:** "Scam costs more than friction."

**Source:** [@richardrx · 2026-06-29](https://x.com/richardrx/status/2071546806987538924)

## You lose money on the boring screens

**Principle:** Registration forms lose users one input at a time and waste CAC, while founders polish the hero. Remove cognitive load until the user does not notice the flow.

**Apply when:** Conversion leaks between signup and first value, or onboarding has many forms.

**Do:**
1. Ask less. Ask only what is relevant at that step: more questions, less conversion.
2. Avoid typing when possible. Swipe/tap costs less than entering data, especially on mobile.
3. Explain why when you ask for sensitive data (documents). This increases completion.
4. Never block paste. Card numbers and CEP (Brazilian postal code) get copied, not memorized.
5. Help users not mistype passwords: add an optional visibility toggle.
6. Avoid dropdowns: they hide the answers from the user. With fewer than ~6 options, use a button group.

**Quote:** "You lose money on the boring screens."

**Source:** [@richardrx · 2025-12-23](https://x.com/richardrx/status/2003495704849760387)

## Checkout is where ~70% of drops happen — every extra input is less conversion

**Principle:** Checkout is the highest-leverage page. Less is more: each extra input lowers conversion. Any new negative surprise is a reason to cancel.

**Apply when:** You audit or build any checkout, signup-to-paid flow or high-stakes form.

**Do:**
1. Use the minimum fields only.
2. Show no surprise fees: expensive shipping, paid shipping at all, service fee, packaging fee. Bake every extra charge into the product price.
3. Show security signals. A lock icon with "Compra segura" ("Secure purchase") lifts conversion.
4. Show an extra discount in the cart if you have one: anchoring works for you there.
5. Display the CNPJ (Brazilian company-registration number): a real company converts more.
6. Show product photos, even for digital products.
7. Split what you can to reduce barriers and cognitive load.
8. Use mobile-appropriate inputs (numeric keyboard for phone).
9. Use social proof in checkout.
10. Test: different ICPs perceive risk differently.

**Visual:** Richard's checkout applying the list: lock icon + "Site Seguro" in the header, four fields only (name, surname, e-mail, +55 phone with a numeric mask), a product thumbnail in the order summary, "Desconto 5% PIX" and free shipping on the receipt, a "Compre com confiança" trust list (100% money-back, support 7 days a week, 10,000+ sales) with a named testimonial, and the CNPJ in the footer — `../assets/1999584679247134761__1.jpg`

**Quote:** "I worked at PayPal literally designing checkouts for the biggest e-commerces and brands in Brazil. Hundreds of them."

**Source:** [@richardrx · 2025-12-12](https://x.com/richardrx/status/1999584679247134761)

## 97% of visitors buy nothing — the leaks are known and fixable

**Principle:** Cart abandonment reasons are mapped, and design fixes most of them.

**Apply when:** You diagnose why traffic does not convert to purchase.

**Evidence:** Late extra costs (49%), forced account creation (24%), slow delivery (19%), complicated checkout (18%), distrust of the site (17%), unclear price (17%), site errors (12%), bad return policy (11%).

**Do:**
- Fix all 8 reasons: eliminate late costs; allow guest checkout; show delivery time early; simplify checkout; add trust signals; show total price upfront; test for errors; publish return policy.
- Copy Amazon: it shows international products with "no additional costs after".

**Quote:** "You can frame this as winning new conversions, or as better capturing what you're losing today."

**Source:** [@richardrx · 2025-12-09](https://x.com/richardrx/status/1998432350842016222)
