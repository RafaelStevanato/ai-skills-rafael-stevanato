# Premium Markers

## Contents

- [Use](#use)
- [Axis 7: Signature & Uniqueness](#axis-7-signature--uniqueness)
- [Axis 8: Cohesion](#axis-8-cohesion)
- [Slop to premium pairs](#slop-to-premium-pairs)
- [Field notes that outrank everything](#field-notes-that-outrank-everything)
- [Adding Soul by axis](#adding-soul-by-axis)
  - [Soul axis 1: Color & Light](#soul-axis-1-color--light)
  - [Soul axis 2: Typography & Copy](#soul-axis-2-typography--copy)
  - [Soul axis 3: Components & Ornament](#soul-axis-3-components--ornament)
  - [Soul axis 4: Layout & Composition](#soul-axis-4-layout--composition)
  - [Soul axis 5: Motion & Interaction](#soul-axis-5-motion--interaction)
  - [Soul axis 6: Execution & Craft](#soul-axis-6-execution--craft)
  - [Soul axis 7: Signature](#soul-axis-7-signature)
  - [Soul axis 8: Cohesion](#soul-axis-8-cohesion)
- [Prescription template](#prescription-template)

## Use

- Load this file in BUILD mode and in EVALUATE mode. See [SKILL.md](../SKILL.md).
- In BUILD mode, decide the signature first.
- In BUILD mode, pick the premium version from the pairs table.
- In BUILD mode, use the soul guide to replace generic choices.
- In EVALUATE mode, score S1-S7 (Axis 7) and H1-H4 (Axis 8) with the tables below.
- In EVALUATE mode, check the pairs table before recording a tell.
- In EVALUATE mode, write fixes with the prescription template.
- Read tell IDs (K25, L8, C1, and so on) in [tells.md](tells.md).
- Score Axes 7 and 8 on what the design did, not on what it avoided.

## Axis 7: Signature & Uniqueness

- Use this uniqueness formula:

```
uniqueness = one signature artifact + atmosphere + layered depth
           + character display face + one bespoke silhouette
           + a treated nav + real specificity
```

- Score each element S1-S7 as 0, 50 or 100.
- Write a one-line justification for each score.
- Compute the axis score as the mean of the seven element scores.
- Apply the signature gate from [evaluate-scoring.md](evaluate-scoring.md).
- Require the signature artifact and a character face on every premium site, including the most minimal one.

| # | Element | 0 (absent) | 50 (attempted) | 100 (strong) |
|---|---------|------------|----------------|---------------|
| S1 | Signature artifact | No custom focal object; hero is text on a fill or a stock/prop visual | A custom visual exists but is generic enough to paste onto another site | ONE high-effort focal object (crafted SVG scene, populated product artifact, illustration, render) that could only belong to this brand |
| S2 | Atmosphere | Flat color fill behind everything | Some texture/tone in the hero only (dies at the fold — see L11) | The background is a composed environment (scene, texture, grain, light) carried down the whole scroll |
| S3 | Layered depth | One flat plane | Two reads, nothing crossing a boundary | Foreground copy / midground focal object / background scene, with at least one element overlapping or bleeding across a layer edge |
| S4 | Character display face | Identity rests on a neutral grotesque or a Google-shelf default (T1) | A distinctive face chosen by reputation, not brief (T9) | A licensed/self-hosted display face with real personality, set large, chosen for this brief (body may stay neutral; system-ui is a legitimately neutral body) |
| S5 | Bespoke silhouette | Every shape is a default rectangle/pill | One mild customization (a radius decision, a simple notch) | One unmistakable custom-cut geometry signing the page (a receipt-torn edge, an invented marker, a specific arrow drawn for the system) |
| S6 | Treated nav | Default flush row of links bolted on top | Centered or contained but generic | The nav is a decision: floated pill, real presence, brand marks threaded in — it belongs to the system |
| S7 | Real specificity | Placeholder logos, fake names, lorem-adjacent copy | Mixed: some real data among placeholders | Real recognizable logos honestly claimable, real names/data inside the product shot, copy written for this product |

## Axis 8: Cohesion

- Flag parts that are individually fine but do not belong to each other.
- Source rule: "Cohesion is the whole game".
- Score each check H1-H4 as 0, 50 or 100.
- Compute the axis score as the mean of the four check scores.

| # | Check | What 100 looks like |
|---|-------|---------------------|
| H1 | One palette, held with discipline | A monochrome or tightly-related set; adjacent sections share or hand off tone. 0 = "blue AND green AND a warm accent", each fine alone, ugly together. |
| H2 | One type voice | A single family across weights/optical sizes, or one display + one quiet neutral — never two display faces arguing. |
| H3 | One system | Nav, buttons, arrows, radii, borders, background speak one language (sharp everywhere, one arrow reused, one gradient threaded through). A page of mismatched fine components reads cheap. |
| H4 | Composed from the brief | Sections designed from what this product actually is — not known skeletons restacked and recolored, not a reference site's content reproduced. Reference = direction, never a stencil. |

## Slop to premium pairs

- Check the pair before recording a tell.
- Treat an element as slop when it is the obvious preset.
- Treat the same element as premium when it is clearly made on purpose for this one screen.

| Pattern | Slop version | Premium version |
|---------|-------------|-----------------|
| Glass | Frosted box + blue glow ignoring its background; banding, leak, halo, pop (K25) | Material over a backdrop worth refracting: refraction, edge dispersion, top-lip highlight, light frost, tuned inner+drop shadows. The gloss is the good part — keep it, fix everything around it |
| Borders | Hard contrasting 1px line on every box (K13) | Self-colored border: surface value shifted a hair, 1px stroke at the surface's own color low-opacity, soft top inner highlight — an edge you feel |
| Accent bar | Straight preset bar on a card edge (K15) | Invented silhouette: diagonal cut-in, chamfer, notch, custom bracket — geometry drawn on purpose |
| Icons | Pack icons in tiles (K1/K4/K24); zero icons as over-correction | Bare bespoke marks in one house style, consistent stroke/corner/grid |
| Shadow | Symmetric black bloom on everything (X6) | Tight, low-offset, small blur, tinted to surface or element color, cast from one direction — or no shadow, depth from tone |
| Glow/light | Blue-purple bloom, centered halo (C1/C5) | Specific, unexpected color with chosen direction and falloff: a warm volumetric rake, a single beam |
| Grid | Full-page faint graph paper (C15) | Tight textured micro-grid behind one panel; sparse blueprint marks (ruler ticks, corner crops, dashed guides) |
| Gradient | Smooth banded wash (C14) | Grain/noise dithered into every large transition — a surface that feels physical |
| App window | Empty generic mock with traffic lights (K7) | Detailed, fully-populated, real-feeling product UI, floated with depth, clipped at an edge — and only when a product UI actually exists |
| Footer wordmark | Text pasted big: off-center, clipped, no treatment (L20) | Anchored flush to the bottom, above the texture, deliberate case + spacing, intentional bleed |
| Motion | Entrance reveals gating content (M1); boops and underline fills (M2/M3) | Scroll-authored motion on already-visible elements, authored micro-interactions tuned for one element, gated behind prefers-reduced-motion |
| Inset island | The default closing CTA panel every time (L8) | A section floated with margin on all sides, on its own surface + grain, used once where detachment means something |
| Noise | Grain sheet over text and controls (K26 — grain over content) | Grain on the substrate at very low opacity: felt, not seen. One masked display word can carry grain as a chosen move |

## Field notes that outrank everything

These six notes win over every other rule in this file.

Signature first:

- Decide the signature FIRST.
- Build sections around the signature.
- Never expect clean spacing to rescue a page that misses the artifact.

Clean is the floor:

- Treat clean as the floor, never the achievement.
- Flag "Correct spacing + quiet type + zero authored moments" as "unfinished work wearing restraint as an alibi".
- Calm is a style; empty is a miss.

Creative is not realistic:

- Never treat "creative" as "realistic".
- Never use photoreal stock as the creative choice. It reads as the opposite of creative.
- Use an authored treatment in ONE medium: cyanotype, riso, pixel art, or one illustration style.
- Expect a one-medium treatment to auto-cohere and sign the page.

Type without the Google shelf:

- Source display faces from outside the Google shelf.
- Use Fontshare faces: Pally, Gambarino, Sentient, Tanker.
- Use Velvetyne faces.
- Use licensed faces: Pangram Pangram, Displaay, Klim.
- Self-host the font files.
- Avoid Clash Display and General Sans. They already read generic.
- View candidates rendered before picking.
- Never name faces from memory.

Component libraries:

- Use component libraries as legitimate foundations: Motion, shadcn/ui, tailark, motion-primitives, kokonut.
- Take the accessible behavior from the library.
- Throw away the generic styling.
- Art-direct on top.
- De-slop every prebuilt block as if it were your own work.

Specific visual reference:

- Start from a specific visual reference. It is the antidote to the slop floor.
- Point to a concrete reference when prescribing fixes: Mobbin, Godly, Awwwards-tier sites.
- Take language from the reference, never its content (H4).

## Adding Soul by axis

- Name the replacement in every fix.
- Never write only "remove tell X".
- Take the replacement from the tables below.
- Apply the soul test after each table.

### Soul axis 1: Color & Light

| Generic | With soul |
|---------|-----------|
| UI kit palette, safe neutrals | One unexpected hero color with a reason (orange in fintech, black in wellness, warm rust in tech) |
| Blue-purple gradient | A gradient in an unexpected hue family (amber→coral, forest→sage, midnight→slate) or a single-hue luminosity shift |
| Flat color fill | Color with behavior: grain, noise, subtle radial falloff, directional light |
| Symmetric glow | Light from a direction — top-left rake, single beam, edge bloom that suggests a source |
| Generic dark mode | Dark with character: warm charcoal, deep forest, not the default slate-900 |

- Run the soul test: "Would I recognize this palette in a lineup of 10 sites?"
- Add more intention when the answer is no.

### Soul axis 2: Typography & Copy

| Generic | With soul |
|---------|-----------|
| Inter/Space Grotesk | A face with opinion: Gambarino for warmth, Reckless for edge, Migra for tech, Sentient for editorial |
| Safe pairing (Fraunces+Work Sans) | An invented pairing: display + system-ui, one face at multiple optical sizes, or a monospace doing display work |
| Clean copy that could fit anywhere | Copy with a voice: short sentences, opinions, humor, the occasional imperfection |
| Em-dash-heavy AI prose | Human rhythm: fragments where earned, varied sentence length, contractions |

- Run the soul test: "If I removed the logo, would the voice still feel like this brand?"
- Add more character to the type and copy when the answer is no.
- Route prose and copy writing to the skill anti-ai-slop-escrita-ptbr.

### Soul axis 3: Components & Ornament

| Generic | With soul |
|---------|-----------|
| Lucide icons everywhere | Bespoke icons in a house style: one stroke weight, one corner treatment, one grid |
| Pills and badges as decoration | Functional shapes: a receipt-edge card, a torn-paper testimonial, a custom bracket |
| Cards from the UI kit | One invented card silhouette used consistently: notched corner, chamfered edge, asymmetric padding |
| Generic CTAs | A CTA with an authored detail: custom arrow, icon that only this brand uses, specific hover state |

- Run the soul test: "Could I swap these components into another site without noticing?"
- Add more invention when the answer is yes.

### Soul axis 4: Layout & Composition

| Generic | With soul |
|---------|-----------|
| Centered hero stack | Asymmetric composition: left-weighted type with a right visual, or a diagonal axis |
| Three-column features | A rhythm break: one wide callout among smaller cards, an intentional asymmetry |
| Template section sequence | Sections that respond to content: a quote that goes full-bleed, a feature that breaks the grid |
| Safe margins | One bold layout decision: hero that bleeds, footer that anchors to the absolute bottom, a section with no padding |

- Run the soul test: "Did the layout respond to the content, or did the content fill a layout?"
- Add composition when the content filled a layout.

### Soul axis 5: Motion & Interaction

| Generic | With soul |
|---------|-----------|
| Fade-in on scroll | Motion that responds to user input: parallax on mouse, tilt on hover, physics-based springs |
| Hover lift on everything | One authored micro-interaction: a button whose icon slides, a card that breathes |
| No motion at all | Subtle ambient motion: a slow rotation, a gentle pulse, something that says "this is alive" |
| Underline-fill hover | A hover state that couldn't be predicted: color inversion, icon swap, a micro-reveal |

- Run the soul test: "Does the motion feel like it was designed for this element, or applied from a library?"
- Add authorship when the motion was applied from a library.

### Soul axis 6: Execution & Craft

| Generic | With soul |
|---------|-----------|
| Default drop shadow | Tinted shadow that picks up the element's color, cast from a consistent direction |
| Borders everywhere | Depth from tone: no borders, just value shifts between planes |
| Good enough alignment | Obsessive alignment: optical centering, baseline grids honored, consistent rhythm |
| Standard focus states | Focus states that match the brand: a custom ring color, an animated outline |

- Run the soul test: "Would a perfectionist notice something wrong?"
- Add more craft attention when the answer is yes.

### Soul axis 7: Signature

| Generic | With soul |
|---------|-----------|
| Text on a gradient | ONE signature artifact that could only belong here |
| Stock photo hero | An authored illustration, custom 3D render, or real product screenshot |
| Template + new colors | A visual system invented for this brief |
| "Clean and minimal" as excuse | Minimal with intention: every choice defended, nothing by default |

- Run the soul test: "If this went viral, would people know which brand it's from without seeing the logo?"
- Treat the signature as missing when the answer is no.

### Soul axis 8: Cohesion

| Generic | With soul |
|---------|-----------|
| Fine parts that don't belong together | One palette, one type voice, one system of shapes |
| Reference site copied | Reference used as direction, not stencil — language borrowed, content invented |
| Sections that feel like different sites | Transitions that hand off: color fades, texture continues, rhythm carries |

- Run the soul test: "Does every section feel like it was designed by the same person on the same day?"
- Treat cohesion as missing when the answer is no.

## Prescription template

- Write each fix in the report with this structure.
- See [slop-report-template.md](slop-report-template.md) for the full report.

```markdown
### 1. {what to fix}

**Evidence:** {tell ID + citation}
**Impact:** {axis, estimated score delta}

**Remove:** {what the slop version looks like}
**Replace with:** {specific premium alternative from the pairs or soul guide}
**Reference:** {optional link to Mobbin/Godly/Awwwards example}
```

Example:
```markdown
### 1. Replace default hero layout with composed asymmetry

**Evidence:** L1 (default hero stack) — hero section uses centered eyebrow →
headline → subline → buttons stack
**Impact:** Axis 4 (+15), Axis 7/S1 (+25 if artifact added)

**Remove:** Centered stack with text on gradient fill
**Replace with:** Left-weighted type column (60%) + right signature artifact
(40%), with the artifact bleeding past the section edge. Add one custom SVG
illustration that couldn't exist on another site.
**Reference:** https://godly.website/website/linear-530
```
