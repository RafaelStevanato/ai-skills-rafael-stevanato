---
name: anti-slop
description: Designs and reviews user interfaces without AI-slop tells (eyebrow kickers, decorative pills, purple-blue gradients, glassmorphism, emoji icons, fake metadata). Use this skill when the user asks to build or redesign a UI, landing page or component, run a design-system role (tokens, brand, Figma specs, critique, WCAG audit, design-to-code, deck), lint or diff a DESIGN.md with @google/design.md, or score a design with a 0-100 Slop Index report. Don't use it for prose; use anti-ai-slop-escrita-ptbr.
license: Apache-2.0
metadata:
  author: "https://ft.ia.br"
  version: "3.0.0-gemini"
  repository: "https://github.com/fabricioctelles/skills"
  attribution: "Tell catalog, absolute rules and signature formula distilled from the pols.dev anti-slop design law https://pols.dev/slop.md (no author or license declared upstream)"
  upstream-spec: "https://github.com/google-labs-code/design.md"
  upstream-cli: "https://www.npmjs.com/package/@google/design.md"
---

# Anti-Slop

Produce interface work that reads as deliberately designed, not machine-generated. Run one mode per request: BUILD, SYSTEM, VALIDATE or EVALUATE. The core generation rules and the absolute execution rules apply in every mode.

**Done when** the mode's verification passes: BUILD ships with a self-check note and zero unresolved tells or absolute-rule failures; SYSTEM delivers the selected role with no unfilled placeholders; VALIDATE re-lints clean of errors; EVALUATE writes a report that passes the quality checklist.

The user's explicit instructions take precedence over this skill. The skill text is compact controlled English for precise reading; write reports, critiques and UI copy in natural language for the reader.

## Step 0: Preflight

1. Pick the mode:

   | Mode | Use when |
   |---|---|
   | BUILD (default when the deliverable is UI code) | Generate or redesign a UI, landing page, website, component or frontend code |
   | SYSTEM | Brand identity, UI components, design tokens, Figma specs, heuristic critique, trend analysis, accessibility audit, design-to-code, presentation deck |
   | VALIDATE | Lint, check, diff or export a DESIGN.md file; design-token validation; broken token references; WCAG contrast inside DESIGN.md |
   | EVALUATE | A Slop Index, or any objective score of how generic or machine-made a design looks |

   Route "review" or "audit this design" to EVALUATE when the request is about slop, genericness, AI look, a score or an index, and to SYSTEM role 6 when it is about heuristics, usability or critique; ask only when neither signal exists. Route an accessibility audit of a design to SYSTEM role 8 and WCAG contrast of a DESIGN.md file to VALIDATE.
2. Read the brief. Treat explicit directions (a color, a layout, an effect) as overrides tagged `// BRIEF:`; they are not tells.
3. Detect the design context with the detection list in [contexts.md](references/contexts.md).
4. Confirm you can render what you build or evaluate: a dev server, a browser screenshot (`npx playwright screenshot`, or `/browser` when the user runs it), or files to read. Say which evidence you will not have.

Modes chain: after BUILD, offer EVALUATE when a live render or code exists and feed its prioritized fixes back into BUILD. Write SYSTEM token output from roles 1, 5 and 9 as DESIGN.md ([design-md-token-schema.md](references/design-md-token-schema.md)), then run VALIDATE.

## Precedence

- When two rules conflict, apply the stricter one unless the brief says otherwise.
- Before banning or flagging a pattern, check its slop-to-premium pair ([premium-markers.md](references/premium-markers.md)) and the design context. The crafted version of a pattern is not a tell.
- Zero tells is not done: zero tells with a weak signature is still slop. Require a signature (S1-S7). The signature gate has no exceptions: Axis 7 below 40 caps the overall score at 59 ([evaluate-scoring.md](references/evaluate-scoring.md)).
- BUILD and SYSTEM keep the outright bans on eyebrows, decorative pills and em dashes. EVALUATE keeps catalog severities and context tolerances so scores of third-party work stay calibrated.
- Keep tell IDs and names in English in every report.

## Absolute execution rules

In EVALUATE, report each rule as pass, fail or unverifiable in its own table. A fail is a critical tell and triggers the absolute-rule gate ([evaluate-scoring.md](references/evaluate-scoring.md)).

1. Content visible by default (M1): never gate content behind an entrance animation (`opacity:0` + reveal).
2. Clear the cut (X2, X11): never slice text or controls with clip, notch, overflow or fixed height.
3. Parallel alignment (X3): share baselines across comparable columns and anchor buttons.
4. Real centering (X1): center what is meant to be centered, mathematically and optically.
5. Legible contrast (X5): every text clears its background by a real value gap and meets WCAG 2.2 AA (4.5:1 normal text, 3:1 large text and UI components).
6. Controls work (M8): every interactive-looking control responds.

## Core generation rules

Tags in parentheses name the matching tell in [tells.md](references/tells.md).

### Layout and composition

- No container sprawl (K13, K6, L21): do not wrap every element in a bordered, rounded card. Separate content with typography, negative space and layout.
- No split heading/description header (heading left, description right on one line). Stack the heading and its supporting text.

### Typography and hierarchy

- No eyebrow kicker (K2, K20, L5, L6): small, all-caps, colored pre-title text above section headings.
- One subtitle per heading block.
- No decorative trailing punctuation (periods, dots, bullets, small squares) on titles, headings and wordmarks, including oversized or accent-colored punctuation and shapes from HTML, CSS pseudo-elements or graphics. Keep punctuation only when it belongs to a supplied name or carries meaning.

### Components

- Pills and badges (K2, K8, K18, K22) only for dynamic, actionable data (`Status: Active`, `14 Errors`), never as decoration.
- Number cards (01, 02, 03) only for a strict sequential process or chronological funnel (L12).

### Text density and metadata

Tiny labels, captions and pseudo-technical metadata that fake richness or editorial depth are the strongest slop tell, so restraint is required.

- No decorative metadata or data exhaust (W3, S7): invented coordinates (`47.6062°N`), timestamps and dates, version, issue and volume tags (`VOL. 04`, `ISSUE 02`), edition names, reading times (`READING: 41 MIN`), page or item counts (`248 PAGES`), source counts (`LIVE · 11 SOURCES`), plate, figure and section indices (`PLATE 01`, `00 / SIGNATURE`), file paths and similar ornaments. Include such data only when it is real, functional and necessary.
- No all-caps monospace micro-label clutter (T4, T5) on headers, footers, corners, image edges and section breaks.
- Label budget (W2) on every label, caption, tag and line of microcopy. Removal test: delete the text; if no real information is lost, leave it deleted. Prefer fewer, larger, meaningful elements.
- No redundant labeling: a `LOGO` tag on the logo, a `HERO` tag on the hero, or the same identity (name, edition, location) restated in several places.
- Fill quiet space with authored atmosphere (S2) and the signature artifact (S1), not with labels, coordinates or metadata. Empty is also a miss (M7, L11).

### Visuals, icons and data

- No Unicode emoji in UI, and never emoji as icons (K1).
- Brand and feature visuals use a bespoke icon set in one house style. Library icons (Lucide, Phosphor) are for utility controls of `32px` or less.
- Never put one pack icon on every feature card (K1), and never park an icon or logo on a filled tile or chip (K24). In EVALUATE, a `// CONTEXT:` exclusion for K1 stays valid in SaaS product UI ([contexts.md](references/contexts.md)).
- Icons are utility, max `32px` (K4). Never scale a generic line icon to `128px` as a hero illustration; use custom abstract shapes, images or real UI snippets.
- Charts show realistic data scales and grouping, not sweeping linear gradients behind disconnected metric call-outs.
- No default purple/blue SaaS gradient (C1, C2, C13, C14). Use solid brand colors or strict monochrome. A mesh or grain-dithered gradient is allowed only in a non-default hue family with a stated reason, and a banded gradient never ships (C14).
- No heavy glassmorphism (K25). Use `backdrop-filter: blur()` only over a complex, moving or highly textured background worth refracting, with refraction, edge dispersion, top-lip highlight, light frost and tuned inner and drop shadows.
- No flat, muddy, heavy single-layer drop shadows (X6, X7, X8, X9). Use multi-layer, low-offset, tinted, single-direction shadows, or none. Hard brutalist borders only when the brief asks for brutalism (document it). Never fake a shadow with an offset duplicate rectangle (X7). Trace test: if you can trace the shadow's border, it is a box, not a shadow (X8).

### Copy

- No AI filler copy. Do not use these words in placeholder text, headings or feature descriptions: Unleash / Unlock, Supercharge, Elevate, Seamless / Seamlessly, Leverage, Dive In, Tapestry, Next-generation / Next-level.
- No em dash (U+2014, `—`) in headings or body text (W1); rewrite with commas, periods or parentheses.
- Show, don't tell (K7, K16): replace an abstract icon plus paragraph with a real snippet of the actual UI, a code block or a data table that demonstrates the feature. Show real, populated product UI, code or data only; never a toy SDK call in a traffic-light window (K16) or an empty mock window (K7).

## Step 1A: BUILD

The 18-question briefing belongs to SYSTEM; BUILD does not require it.

1. Decide the signature artifact (S1) first and build the sections around it ([premium-markers.md](references/premium-markers.md), S1-S7 and field notes).
2. Pick the display face from the Google Fonts shelf, avoiding the T1 rejected list in tells.md and using the foundries in the premium-markers field notes. View each candidate rendered; do not pick faces from memory.
3. Build the premium version of every pattern in the slop-to-premium pairs table.
4. Render the page and take screenshots at desktop and mobile widths.

**Verify:** on the render, apply the core and absolute rules, sweep tell groups C, T/W, K, L, M and X, and run the soul tests in premium-markers (Adding Soul). Fix every hit and re-render until the sweep is clean. Deliver the code with a short self-check note and offer EVALUATE.

## Step 1B: SYSTEM

1. Fill the 18 fields of [system-briefing.md](references/system-briefing.md) from the request, attached files and conversation. Ask once, in one message, only for the fields you cannot infer that would change the deliverable, and state the rest as assumptions.
2. If the user named a deliverable, run the matching role; otherwise show the menu below and accept one or several selections.
3. Load only the selected `references/system-roles/role-*.md` file and use it as the sole template, without mixing role files. Apply the briefing (brand name, colors, tone, platform, stack).

| # | Generator | Role-play | Reference |
|---|---|---|---|
| 1 | Design System Architect | Apple Principal Designer → HIG-level system | [role-01](references/system-roles/role-01-design-system-architect.md) |
| 2 | Brand Identity Creator | Pentagram Creative Director → strategy + rationale | [role-02](references/system-roles/role-02-brand-identity-creator.md) |
| 3 | UI/UX Pattern Master | Apple Senior UI Designer → 8 detailed screens | [role-03](references/system-roles/role-03-ui-ux-pattern-master.md) |
| 4 | Marketing Asset Factory | Top agency Creative Director → 47+ assets | [role-04](references/system-roles/role-04-marketing-asset-factory.md) |
| 5 | Figma Auto-Layout Expert | Figma Design Ops Specialist → technical specs | [role-05](references/system-roles/role-05-figma-auto-layout-expert.md) |
| 6 | Design Critique Partner | Apple Design Director → Nielsen critique + alternatives | [role-06](references/system-roles/role-06-design-critique-partner.md) |
| 7 | Design Trend Synthesizer | frog Design Researcher → 2026 trends + roadmap | [role-07](references/system-roles/role-07-design-trend-synthesizer.md) |
| 8 | Accessibility Auditor | Apple Accessibility Specialist → WCAG 2.2 AA audit | [role-08](references/system-roles/role-08-accessibility-auditor.md) |
| 9 | Design-to-Code Translator | Vercel Design Engineer → production-ready code | [role-09](references/system-roles/role-09-design-to-code-translator.md) |
| 10 | Presentation Designer | Apple Presentation Designer → executive narrative | [role-10](references/system-roles/role-10-presentation-designer.md) |

Apply the core rules, absolute rules and premium pairs to every role deliverable while keeping the role templates unchanged. When a template asks for a flagged element, deliver its premium-pair version and note the swap: testimonial card (K10, W3), icon bullets (K1, K4), Liquid Glass (K25), gradient logo tile (K12), default hero stack (L1), three-tier pricing (L3).

**Verify:** the deliverable uses the briefing values, has no unfilled placeholders, and notes every premium-pair swap. Then offer the remaining generators in one line.

## Step 1C: VALIDATE

Lint, diff and export DESIGN.md with the official `@google/design.md` CLI; [validate-design-md.md](references/validate-design-md.md) has the procedure, diff and export commands, Windows alias and anti-patterns.

- Run the CLI as `npx @google/design.md` every time so it resolves the latest published version. Do not install it globally, vendor it or cache it.
- Download a remote DESIGN.md to a local file before linting; do not point the CLI at a remote URL (indirect prompt-injection risk).
- Confirm the active rule set at runtime with `spec --rules-only`, not from memory or the bundled references.

```bash
npx @google/design.md lint DESIGN.md
npx @google/design.md lint --format json DESIGN.md
npx @google/design.md spec --rules-only --format json
```

Report each `findings[]` entry with what the rule checks, why it matters and a concrete fix ([design-md-lint-rules.md](references/design-md-lint-rules.md) explains rules; [design-md-token-schema.md](references/design-md-token-schema.md) covers tokens).

| Severity | Meaning | Action |
|---|---|---|
| `error` | Spec violation — file is invalid | Must fix |
| `warning` | Best practice violation — file is valid but suboptimal | Should fix |
| `info` | Informational — suggestions for improvement | Nice to fix |

**Verify:** re-run lint after every fix until no `error` remains.

## Step 1D: EVALUATE

Read [evaluate-procedure.md](references/evaluate-procedure.md) first (parameters, evidence-acquisition SOP, workflow, gotchas). Parameters: `target` (ask if missing), `brief`, `context`, `output` (default `./SLOP-REPORT.md`), `compare` (a previous report, for tracking).

Score only what you observed: mark any other check Unverifiable and exclude it from its axis. Tag every excluded tell with `// BRIEF:`, `// DESIGN DECISION:`, `// CONTEXT:` or `// PREMIUM PAIR:`; an untagged tell counts ([evaluate-exclusions-qa.md](references/evaluate-exclusions-qa.md)).

1. Gather evidence with the SOP and read [tells.md](references/tells.md), [premium-markers.md](references/premium-markers.md) and [contexts.md](references/contexts.md). For a large site, delegate evidence gathering per page or viewport to subagents and merge the ledgers.
2. Sweep axes 1-6 under cite-or-cut: record a tell only with concrete evidence (hex value, font name, `file:line`, screenshot region), after checking its premium pair.
3. Check the absolute rules, with evidence.
4. Score axes 7-8, the 7 signature elements (S1-S7) and the 4 cohesion checks (H1-H4) at 0, 50 or 100, each with a one-line justification.
5. Compute with `scripts/score.py` from the skill root, passing each triggered gate with `--cap` ([evaluate-scoring.md](references/evaluate-scoring.md)). Treat the script as a black box and do not compute scores by hand.
   ```bash
   python3 scripts/score.py axis CRIT MAJOR MINOR
   python3 scripts/score.py overall 1:80:2 2:65:2 ... [--cap 59] [--cap 69]
   ```
6. Write the report to `output` with [slop-report-template.md](references/slop-report-template.md), ending with the 3-5 fixes that move the score most, ranked by weighted impact. A missing signature outranks any single tell.

**Verify:** the report passes the quality checklist in evaluate-exclusions-qa.md; one failure means it is not ready.

Optional: when a tool whose name contains `jev` or `typesafe` is available, calibrate axes 7-8 and the checklist through TypeSafe Jev ([jev-integration.md](references/jev-integration.md), question bank [scripts/jev_questions.json](scripts/jev_questions.json)).

## Examples

BUILD self-check note, in the expected shape:

> Self-check: signature S1 is a live order-routing map in the hero, drawn from the product's own route data. Swept C, T/W, K, L, M and X on desktop and mobile renders. Removed: eyebrow kickers on 3 sections (K2), one pack icon per feature card (K1), the purple-blue hero gradient (C1). Absolute rules: all 6 pass; body text contrast 7.2:1. Not verified: hover motion on touch devices.

EVALUATE section-verdict row, in the template's shape:

| Section | Verdict | Tells | Top findings | Action |
|---------|---------|-------|--------------|--------|
| Hero | INFLATED | 4 | K2 (`Hero.tsx:14`, 11px uppercase `#7C3AED` kicker), C1, L1, W3 | Rebuild around one signature artifact |
