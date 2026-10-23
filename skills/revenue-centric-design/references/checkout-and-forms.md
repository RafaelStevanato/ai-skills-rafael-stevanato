# Checkout & Forms (Conversion-Completion Layer)

Attribution: Richard (@richardrx), "Richard — Design for startups", translated from Portuguese.
Each entry links to its source post.
Return to [SKILL.md](../SKILL.md).
Related files: [onboarding-and-activation.md](onboarding-and-activation.md), [conversion-and-landing-pages.md](conversion-and-landing-pages.md).
Keep every `##` heading unchanged. Other files quote each heading as a stable ID.

## Friction kills conversion — field count, input type, and perceived risk all compound

**Principle:**
- Cut field count. More fields = lower conversion.
- Check the input type. Text fields usually generate less impact.
- Dropdowns and textareas hurt more than text fields.
- Expect the phone number field to drop conversion.
- Expect any data that raises perceived risk or invasiveness to drop conversion.
- Perceived effort ≠ real effort.
- 5 steps with 2 fields per screen can beat 2 screens with 7 fields each.

**Apply when:**
- Optimizing lead forms, pre-checkout, signup.

**Do:**
- Count perceived effort, not steps.
- Know that a screen full of text, warnings, secondary info raises cognitive load even without interaction.
- Ask: how much effort can I remove without destroying the business value of that data?
- Check the space between elements. Sometimes the fix is between things.
- Add more breathing room.
- Remove noise.
- Set a clearer hierarchy.
- Make your form look like a corridor, not an interrogation room.
- Cut friction at trial signup and checkout.
- Add calibrated friction only at three spots: card-upfront trial, mandatory onboarding, enterprise demo form.
- For those three spots, see [Put friction in the right place, not zero friction everywhere](onboarding-and-activation.md#put-friction-in-the-right-place-not-zero-friction-everywhere).

**Evidence:**
- HubSpot study across 40,000+ landing pages: 3-field forms convert above 25%.
- Adding fields trends conversion down.
- Phone field drops conversion to ~13.5% vs 19% without.

**Source:** [@richardrx · 2026-08-12](https://x.com/richardrx/status/2087502085151424711)

## Microcopy at the point of fraud risk beats friction everywhere else

**Principle:**
- Design must protect the user from the real environment the product lives in.
- Apply this rule first in low-trust economies.
- Add one line of microcopy in the right place.
- That one line prevents scams that cost more than the friction of adding it.

**Apply when:**
- Users are getting scammed through a flow your product enables (delivery PIN sharing, social engineering).

**Do:**
- Add microcopy at the exact risk moment: "Never share your number outside the app. The store and courier already have your contact via chat."
- Use transparency as the antidote in low-trust verticals (auto repair, delivery).

**Quote:** "Scam costs more than friction."

**Source:** [@richardrx · 2026-06-29](https://x.com/richardrx/status/2071546806987538924)

## You lose money on the boring screens

**Principle:**
- Registration forms lose users one input at a time.
- Each lost user creates holes in your bucket and wastes CAC.
- Do not polish the hero while the registration form leaks users.
- Remove cognitive load until the flow is so smooth the user doesn't notice it.

**Apply when:**
- Conversion leaks between signup and first value.
- Onboarding is form-heavy.

**Do:**
1. Ask less. Ask only what is relevant at that specific step. More questions = less conversion.
2. Avoid typing when possible. Swipe/tap costs less than entering data, especially mobile.
3. Explain why when you ask for sensitive data (documents). This increases completion.
4. Never block paste. Card numbers and CEP (Brazilian postal code) get copied, not memorized.
5. Help users not mistype passwords. Add an optional visibility toggle.
6. Avoid dropdowns. They hide the answers from the user. With fewer than ~6 options, use a button group instead.

**Quote:** "You lose money on the boring screens."

**Source:** [@richardrx · 2025-12-23](https://x.com/richardrx/status/2003495704849760387)

## Checkout is where ~70% of drops happen — every extra input is less conversion

**Principle:**
- At checkout, less is more.
- Each extra input is less conversion.
- Ask for the minimum possible.
- Treat any new negative surprise as a reason to cancel.
- Negative surprises include: expensive shipping, paid shipping at all, service fee, packaging fee.
- Embed every extra charge into the product price.
- Never show an extra charge as a hidden extra.

**Apply when:**
- Auditing or building any checkout, signup-to-paid flow, or high-stakes form.

**Do:**
1. Use minimum fields only.
2. Show no surprise fees. Bake costs into the price.
3. Show security signals. Even a lock icon with "Compra segura" — "Secure purchase" — lifts conversion.
4. Show an extra discount in the cart if you have one. Anchoring works for you there.
5. Display the CNPJ (Brazilian company-registration number). A real company converts more.
6. Show product photos, even for digital products.
7. Split what you can to reduce barriers and cognitive load.
8. Use mobile-appropriate inputs (numeric keyboard for phone).
9. Use social proof in checkout. It works.
10. Test. Different ICPs perceive risk differently.

**Visual:** Richard's own checkout applying the list at once: lock icon + "Site Seguro" in the header, four fields only (name, surname, e-mail, +55 phone with a numeric mask), a product thumbnail in the order summary, "Desconto 5% PIX" and free shipping on the receipt, a "Compre com confiança" trust list (100% money-back, support 7 days a week, 10,000+ sales) with a named testimonial, and the CNPJ in the footer — `../assets/1999584679247134761__1.jpg`

**Quote:** "I worked at PayPal literally designing checkouts for the biggest e-commerces and brands in Brazil. Hundreds of them."

**Source:** [@richardrx · 2025-12-12](https://x.com/richardrx/status/1999584679247134761)

## 97% of visitors buy nothing — the leaks are known and fixable

**Principle:**
- Cart abandonment reasons are mapped.
- Design fixes most of them.

**Apply when:**
- Diagnosing why traffic isn't converting to purchase.

**Evidence:**
- Cart abandonment reasons, in order:
  1. Late extra costs: 49%.
  2. Forced account creation: 24%.
  3. Slow delivery: 19%.
  4. Complicated checkout: 18%.
  5. Distrust of the site: 17%.
  6. Unclear price: 17%.
  7. Site errors: 12%.
  8. Bad return policy: 11%.

**Do:**
- Treat the 8 reasons as a checklist of 8 actions:
  1. Eliminate late costs.
  2. Allow guest checkout.
  3. Show delivery time early.
  4. Simplify checkout.
  5. Add trust signals.
  6. Show total price upfront.
  7. Test for errors.
  8. Publish return policy.
- Copy Amazon. It shows international products with "no additional costs after".

**Quote:** "You can frame this as winning new conversions, or as better capturing what you're losing today."

**Source:** [@richardrx · 2025-12-09](https://x.com/richardrx/status/1998432350842016222)
