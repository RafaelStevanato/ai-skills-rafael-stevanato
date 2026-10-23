# Design Contexts

Use this file to set tell priorities and tolerances per design context.
EVALUATE uses it for score adjustments and `// CONTEXT:` exclusions.
BUILD uses it for context-specific guidance, such as fold ownership.

Related files:
- Tell IDs (L, K, C, T, X, W, M): [tells.md](tells.md)
- Signature and soul IDs (S1-S7, H1-H4): [premium-markers.md](premium-markers.md)
- Axis weights and caps: [evaluate-scoring.md](evaluate-scoring.md)
- `context` parameter and sweep steps: [evaluate-procedure.md](evaluate-procedure.md)
- Exclusion tags and limits: [evaluate-exclusions-qa.md](evaluate-exclusions-qa.md)
- Section Ledger format: [slop-report-template.md](slop-report-template.md)
- Router and core rules: [../SKILL.md](../SKILL.md)

## Context parameter

- Set the `context` parameter to one of: `landing`, `saas`, `editorial`, `ecommerce`, `auto`.
- Default is `auto`: infer the context from the design.

## How to use this file

1. **Identify the context** before the sweep.
   - If `auto`, look for these signals:
     - Pricing cards, feature grids, integrations → `saas`
     - Product cards, cart, checkout → `ecommerce`
     - Articles, bylines, reading time → `editorial`
     - Hero + CTA + social proof only → `landing`
   - Use the [Context detection heuristics](#context-detection-heuristics) table for the full signal list.

2. **Apply priority weights.**
   - Treat tells in the Priority table as more damaging in this context.

3. **Apply tolerances.**
   - Exclude tells in the Tolerance table with lighter justification.
   - Still document each exclusion.
   - Use `// CONTEXT:` as the exclusion tag.
   - Use `// CONTEXT:` only for tells listed in the Tolerance table of the active context.

4. **Note context-specific tells.**
   - Some patterns are tells only in certain contexts.

Scope of the tolerances:
- Apply the Tolerance tables in EVALUATE mode only.
- In BUILD and SYSTEM modes, keep the outright ban on eyebrows, kickers, decorative pills (K2, K20, L5, L6) and em dashes (W1).
- In BUILD mode, use the Priority tells and Context-specific guidance of the target context as design constraints.

---

## Landing Page / Marketing

- Context value: `landing`.
- Covers: hero, value prop, social proof, CTA.

### Priority tells (most damaging here)

| ID | Tell | Why it matters more |
|----|------|---------------------|
| L1 | Default hero stack | The hero IS the page — a generic hero sinks everything |
| L2 | Split hero | Same — the skeleton is immediately recognizable |
| S1 | Signature artifact (missing) | A landing page with no focal object is a template |
| C1 | Blue→purple gradient | The "AI landing page" signature; instant credibility loss |
| K9 | Default CTA button pair | The action is the point; generic buttons kill conversion |
| L4 | Pre-footer CTA slab | The closer matters; a template closer is a missed opportunity |

### Tolerance (lighter justification OK)

| ID | Tell | Why tolerance applies |
|----|------|----------------------|
| K2 | Pill / eyebrow badge | Common convention, low harm if the rest is strong |
| K14 | Countdown timer | Legitimate if tied to a real deadline (launch, sale end) |
| L9 | Email-pill + button form | Standard capture pattern; the form itself isn't the problem |
| K10 | Testimonial card | The format is expected; focus on whether content is real |

### Context-specific guidance

- Fold ownership (L16):
  - Rate L16 as critical.
  - Make the first viewport the pitch.
  - Rate a hero that does not own the fold as a structural failure.
- Signature artifact (S1) above the fold:
  - Place S1 above the fold.
  - Never bury S1 below the fold, because that wastes the most valuable real estate.
- Real specificity (S7):
  - Treat S7 as table stakes.
  - Rate fake logos, placeholder testimonials, and lorem-adjacent copy as instant credibility killers.

---

## SaaS Product / Dashboard

- Context value: `saas`.
- Covers: product pages, feature tours, pricing, and the product UI itself.

### Priority tells (most damaging here)

| ID | Tell | Why it matters more |
|----|------|---------------------|
| X1 | Nothing actually centered | Dashboards live or die on alignment |
| X3 | Ragged comparison columns | Pricing comparison is often the decision point |
| K6 | Kitchen-sink card | Overloaded UI signals poor product thinking |
| K22 | Metadata pills everywhere | Dashboard-kit aesthetic = no brand |
| L3 | Three-tier pricing preset | The pricing page IS the product pitch |
| L15 | SaaS meta-skeleton | Stripe/Linear/Vercel clone is the most common SaaS slop |

### Tolerance (lighter justification OK)

| ID | Tell | Why tolerance applies |
|----|------|----------------------|
| K1 | Icon-pack icons | System UI icons are expected in product UI |
| K13 | Hairline borders | Legitimate UI pattern for card separation |
| T4 | Mono as house voice | Acceptable for code, data, timestamps in product UI |
| K7 | App window mock | Legitimate if showing real product UI, not filler |

### Context-specific guidance

- Execution axis (6):
  - Give the Execution axis (6) more weight.
  - Let a SaaS page survive a generic layout only when execution is flawless.
  - Rate broken alignment, contrast failures, and dead controls as fatal.
- K7 (fake window) flips in context:
  - Treat a detailed, populated, real product UI as a signature, not a tell.
  - Flag K7 only for an empty mock with traffic lights and placeholder kanban.
- L15 (SaaS skeleton) compounds:
  - Apply both the skeleton tell (L15) and the individual section tells when both conditions hold.
  - Condition 1: the page follows the Stripe sequence.
  - Condition 2: each section is a known template.

---

## Editorial / Magazine

- Context value: `editorial`.
- Covers: content-first designs: articles, blogs, publications, portfolios.

### Priority tells (most damaging here)

| ID | Tell | Why it matters more |
|----|------|---------------------|
| T1 | Google-shelf signature face | Editorial identity lives in type |
| T2 | Recognizable slop pairing | Type pairing IS the voice |
| T3 | Didone-as-luxury reflex | The "premium editorial" autopilot |
| L7 | Big serif statement block | The philosophy-beat cliché |
| W2 | Wall of copy | Editorial should know better |
| L10 | Image card with overlay caption | The magazine-grid autopilot |

### Tolerance (lighter justification OK)

| ID | Tell | Why tolerance applies |
|----|------|----------------------|
| C7 | Cream/beige editorial default | Legitimate editorial palette choice if consistent |
| L5 | Kicker + serif-H2 section head | Expected editorial convention |
| K21 | Hairline rules as decoration | Traditional editorial element |
| T6 | Letterspaced serif wordmark | May be the actual brand identity |

### Context-specific guidance

- Typography axis (2):
  - Give the Typography axis (2) 3x effective weight.
  - Treat type as the design in editorial.
  - Treat a generic typeface choice as sinking the whole piece.
- C7 (cream background) is context-dependent:
  - Treat warm cream as premium when it is a deliberate paper-texture choice.
  - Treat cream as slop when it is "I need a background that isn't white".
  - Check that cream is carried with intent: grain, texture, or tonal variation.
  - Flag cream that is only a flat fill.
- Reading experience tells:
  - Check line length: 45–75 chars.
  - Check body line height: 1.4–1.6.
  - Check paragraph spacing.
  - Note that these checks are not in the catalog.
  - Note that they strongly affect the editorial context.

---

## E-commerce / Retail

- Context value: `ecommerce`.
- Covers: product listings, category pages, cart, checkout.

### Priority tells (most damaging here)

| ID | Tell | Why it matters more |
|----|------|---------------------|
| X3 | Ragged comparison columns | Product comparison must be scannable |
| X5 | Unreadable contrast | Price and CTA must be instantly legible |
| K23 | Faked or missing logos | Trust signals are everything in commerce |
| W3 | Fake metrics | Invented social proof destroys trust |
| M8 | Dead controls | Add-to-cart that doesn't work = lost sale |
| L3 | Three-tier pricing preset | Subscription/plan selection UX matters |

### Tolerance (lighter justification OK)

| ID | Tell | Why tolerance applies |
|----|------|----------------------|
| K14 | Countdown timer | Legitimate for real sales, flash deals, inventory |
| K22 | Metadata pills | Product tags, categories, badges are expected |
| K17 | Floating tag on image | Price tags, sale badges on product images are standard |
| L12 | Numbered steps | Checkout progress indicators are expected |

### Context-specific guidance

- Trust signals are non-negotiable:
  - Rate K23 (fake logos) and W3 (fake metrics) as effectively critical in e-commerce context.
  - Use real payment badges, security seals, and customer logos.
- K14 (countdown) splits by reality:
  - Treat a countdown to a real sale end as legitimate UX.
  - Flag an evergreen fake countdown as manipulative slop.
  - Document which case applies.
- Execution axis (6):
  - Treat the Execution axis (6) as conversion-critical.
  - Treat every pixel of friction in checkout as costing money.
  - Rate alignment issues, contrast failures, and confusing states as business failures, not only design failures.

---

## Multi-context pages

- Apply these steps when a page spans contexts.
- Example 1: a SaaS landing page with an editorial blog section.
- Example 2: an e-commerce site with magazine-style lookbooks.

1. **Identify the primary context.**
   - Ask what the main job of the page is.
2. **Switch context per section.**
   - Apply different tolerances to different sections where appropriate.
3. **Document in the report.**
   - Note when a section was evaluated under a different context than the page default.

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

---

## Context detection heuristics

Use these signals when `context: auto`:

| Signal | Likely context |
|--------|---------------|
| Pricing cards with tiers | `saas` |
| "Start free trial", "Book demo" CTAs | `saas` |
| Product grid with prices | `ecommerce` |
| Cart icon, "Add to cart" | `ecommerce` |
| Byline, reading time, article body | `editorial` |
| Category/tag taxonomy | `editorial` |
| Single hero + CTA + testimonials only | `landing` |
| No product UI shown | `landing` |

- If signals conflict, ask the user or default to `landing`.
- `landing` is the most common evaluation target.
