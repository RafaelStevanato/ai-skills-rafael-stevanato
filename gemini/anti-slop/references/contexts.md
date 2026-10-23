# Design Contexts

Contents: How to use · Landing Page / Marketing (`landing`) · SaaS Product / Dashboard (`saas`) · Editorial / Magazine (`editorial`) · E-commerce / Retail (`ecommerce`) · Multi-context pages · Context detection heuristics

EVALUATE: use this file for score adjustments and `// CONTEXT:` exclusions ([evaluate-exclusions-qa.md](evaluate-exclusions-qa.md)).
Tell IDs: [tells.md](tells.md).

Set `context` to `landing`, `saas`, `editorial`, `ecommerce`, or `auto`.

## How to use

1. **Identify the context** before the sweep. If `auto`, use these signals:
   - Pricing cards, feature grids, integrations → `saas`
   - Product cards, cart, checkout → `ecommerce`
   - Articles, bylines, reading time → `editorial`
   - Hero + CTA + social proof only → `landing`
2. **Apply priority weights.** Treat Priority tells as more damaging here.
3. **Apply tolerances** in EVALUATE only. Exclude Tolerance-table tells with lighter justification, but document each exclusion.
   - Use `// CONTEXT:` only for tells in the active Tolerance table.
4. **Note context-specific tells.** Some patterns are tells only in certain contexts.

Scope of the tolerances:
- BUILD and SYSTEM: keep the outright ban on eyebrows, kickers, decorative pills (K2, K20, L5, L6) and em dashes (W1).
- BUILD: use the Priority tells and Guidance as design constraints.

## Landing Page / Marketing (`landing`)

**Priority**

|ID|Tell|Why it matters more|
|----|------|---------------------|
|L1|Default hero stack|The hero IS the page — a generic hero sinks everything|
|L2|Split hero|Same — the skeleton is immediately recognizable|
|S1|Signature artifact (missing)|A landing page with no focal object is a template|
|C1|Blue→purple gradient|The "AI landing page" signature; instant credibility loss|
|K9|Default CTA button pair|The action is the point; generic buttons kill conversion|
|L4|Pre-footer CTA slab|The closer matters; a template closer is a missed opportunity|

**Tolerance**

|ID|Tell|Why tolerance applies|
|----|------|----------------------|
|K2|Pill / eyebrow badge|Common convention, low harm if the rest is strong|
|K14|Countdown timer|Legitimate if tied to a real deadline (launch, sale end)|
|L9|Email-pill + button form|Standard capture pattern; the form itself isn't the problem|
|K10|Testimonial card|The format is expected; focus on whether content is real|

**Guidance**

- Rate L16 (fold ownership) as critical: a hero that does not own the first viewport is a structural failure.
- Place S1 above the fold.
- Require S7 (real specificity): fake logos, placeholder testimonials, and lorem-adjacent copy are instant credibility killers.

## SaaS Product / Dashboard (`saas`)

**Priority**

|ID|Tell|Why it matters more|
|----|------|---------------------|
|X1|Nothing actually centered|Dashboards live or die on alignment|
|X3|Ragged comparison columns|Pricing comparison is often the decision point|
|K6|Kitchen-sink card|Overloaded UI signals poor product thinking|
|K22|Metadata pills everywhere|Dashboard-kit aesthetic = no brand|
|L3|Three-tier pricing preset|The pricing page IS the product pitch|
|L15|SaaS meta-skeleton|Stripe/Linear/Vercel clone is the most common SaaS slop|

**Tolerance**

|ID|Tell|Why tolerance applies|
|----|------|----------------------|
|K1|Icon-pack icons|System UI icons are expected in product UI|
|K13|Hairline borders|Legitimate UI pattern for card separation|
|T4|Mono as house voice|Acceptable for code, data, timestamps in product UI|
|K7|App window mock|Legitimate if showing real product UI, not filler|

**Guidance**

- Weight the Execution axis (6) more: flawless execution offsets a generic layout. Rate broken alignment, contrast failures, and dead controls as fatal.
- Rate K7 (fake window) by content: a detailed, populated, real product UI is a signature, not a tell. Flag only an empty mock with traffic lights and placeholder kanban.
- Apply L15 and the section tells together when the page follows the Stripe sequence AND each section is a known template.

## Editorial / Magazine (`editorial`)

**Priority**

|ID|Tell|Why it matters more|
|----|------|---------------------|
|T1|Google-shelf signature face|Editorial identity lives in type|
|T2|Recognizable slop pairing|Type pairing IS the voice|
|T3|Didone-as-luxury reflex|The "premium editorial" autopilot|
|L7|Big serif statement block|The philosophy-beat cliché|
|W2|Wall of copy|Editorial should know better|
|L10|Image card with overlay caption|The magazine-grid autopilot|

**Tolerance**

|ID|Tell|Why tolerance applies|
|----|------|----------------------|
|C7|Cream/beige editorial default|Legitimate editorial palette choice if consistent|
|L5|Kicker + serif-H2 section head|Expected editorial convention|
|K21|Hairline rules as decoration|Traditional editorial element|
|T6|Letterspaced serif wordmark|May be the actual brand identity|

**Guidance**

- Give the Typography axis (2) 3x effective weight: a generic typeface sinks the piece.
- Judge C7 (cream) by intent: deliberate paper texture (grain, texture, tonal variation) is premium; a flat fill ("I need a background that isn't white") is slop.
- Check line length (45–75 chars), body line height (1.4–1.6), and paragraph spacing. No catalog tell covers them.

## E-commerce / Retail (`ecommerce`)

**Priority**

|ID|Tell|Why it matters more|
|----|------|---------------------|
|X3|Ragged comparison columns|Product comparison must be scannable|
|X5|Unreadable contrast|Price and CTA must be instantly legible|
|K23|Faked or missing logos|Trust signals are everything in commerce|
|W3|Fake metrics|Invented social proof destroys trust|
|M8|Dead controls|Add-to-cart that doesn't work = lost sale|
|L3|Three-tier pricing preset|Subscription/plan selection UX matters|

**Tolerance**

|ID|Tell|Why tolerance applies|
|----|------|----------------------|
|K14|Countdown timer|Legitimate for real sales, flash deals, inventory|
|K22|Metadata pills|Product tags, categories, badges are expected|
|K17|Floating tag on image|Price tags, sale badges on product images are standard|
|L12|Numbered steps|Checkout progress indicators are expected|

**Guidance**

- Rate K23 (fake logos) and W3 (fake metrics) as effectively critical. Use real payment badges, security seals, and customer logos.
- Judge K14 (countdown) by reality: a real sale end is legitimate; an evergreen fake countdown is manipulative slop. Document which applies.
- Treat the Execution axis (6) as conversion-critical. Rate alignment issues, contrast failures, and confusing states as business failures.

## Multi-context pages

Handle a mixed page (SaaS + editorial blog; e-commerce + magazine-style lookbooks) in 3 steps:

1. **Identify the primary context:** the page's main job.
2. **Switch context per section.** Apply different tolerances to different sections.
3. **Document in the report** each section evaluated under a non-default context.

Example:
```markdown
> Context: `saas` (primary), `editorial` for Blog section

## Section Ledger
| Section | Context | Verdict | ... |
|---------|---------|---------|-----|
| Hero | saas | SUSPICIOUS | ... |
| Features | saas | CLEAN | ... |
| Blog | editorial | INFLATED | ... |
```

## Context detection heuristics

`context: auto` is the default. Use these signals:

|Signal|Likely context|
|--------|---------------|
|Pricing cards with tiers|`saas`|
|"Start free trial", "Book demo" CTAs|`saas`|
|Product grid with prices|`ecommerce`|
|Cart icon, "Add to cart"|`ecommerce`|
|Byline, reading time, article body|`editorial`|
|Category/tag taxonomy|`editorial`|
|Single hero + CTA + testimonials only|`landing`|
|No product UI shown|`landing`|

If signals conflict, ask the user or default to `landing`.
