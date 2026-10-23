---
name: anti-slop
description: >-
  Anti-slop UI design in 4 modes. BUILD: deliberate, opinionated, functional UI, landing pages, components and frontend code without slop tells (eyebrow kickers, decorative pills, purple-blue gradients, glassmorphism, emoji icons, fake metadata). SYSTEM: design systems, brand identity, tokens, UI/UX patterns, marketing assets, Figma specs, critique, trends, WCAG audit, design-to-code, decks via 10 roles. VALIDATE: lint, diff, export DESIGN.md with the @google/design.md CLI. EVALUATE: score a URL, screenshot, code or Figma export for AI slop; write a Slop Report with 0-100 Slop Index and grade. Use when the user says anti-slop, design a UI, build a landing page, create design system, validate DESIGN.md, npx design.md lint, slop report, evaluate design slop, is this design AI slop, audit this landing page design, de-slop review. For prose use anti-ai-slop-escrita-ptbr.
license: Apache-2.0
metadata:
  author: "https://ft.ia.br"
  version: "3.0.0"
  date: "2026-10-23"
  merged-from: "anti-slop, slop-eval 1.1.0, ultimate-design-system-master 2.2, design-md-validator 1.3"
  category: "design"
  repository: "https://github.com/fabricioctelles/skills"
  attribution: "Tell catalog, absolute rules and signature formula distilled from the pols.dev anti-slop design law https://pols.dev/slop.md"
  source-anti-slop: "no author or license declared upstream"
  upstream-spec: "https://github.com/google-labs-code/design.md"
  upstream-cli: "https://www.npmjs.com/package/@google/design.md"
  upstream-stitch-skills: "https://github.com/google-labs-code/stitch-skills"
---

> **⚠️ EXECUTION DIRECTIVE (INPUT vs. OUTPUT SEPARATION):**
> The rules in this skill use strict ASD-STE100 controlled language solely for zero-ambiguity parsing and token efficiency.
> - **NEVER copy this telegraphic or robotic style into human-facing outputs.**
> - Apply 80% ASD-STE100 in final outputs ONLY when explaining dense technical concepts.

# Anti-Slop

Run one mode: BUILD, SYSTEM, VALIDATE, EVALUATE.
Apply the core generation rules and the absolute execution rules in every mode.

## Mode router

|Mode|Trigger phrases|
|------|-----------------|
|BUILD|Generate or redesign UI, landing page, website, component, frontend code. Default when the deliverable is UI code.|
|SYSTEM|"build brand identity", "design UI components", "generate design tokens", "create figma specs", "review my design" (heuristics, critique), "analyze design trends", "audit accessibility", "convert design to code", "create presentation deck"|
|VALIDATE|"lint DESIGN.md", "check my design.md", "design.md spec compliance", "WCAG contrast check" (DESIGN.md file), "broken token references", "design token validation", "export design tokens", "diff design systems", "design.md audit", "@google/design.md", "design system validation", "frontmatter tokens", any request to verify a DESIGN.md file|
|EVALUATE|"Slop Index", any request for an objective score of how generic or machine-made a design looks|

- Route "review my design" or "audit this design" to EVALUATE on a slop, generic, AI-made, score, or index signal, and to SYSTEM role 6 on a heuristics, usability, or critique signal. Ask the user which mode to use when neither signal exists.
- Route "audit accessibility" of a design to SYSTEM role 8. Route WCAG contrast of a DESIGN.md file to VALIDATE.
- Route prose, text, and copy writing to the skill anti-ai-slop-escrita-ptbr. Never use this skill to fix text.
- Chain modes: run EVALUATE on a BUILD output when a live render or code exists (optional self-audit). Feed its prioritized fixes back into BUILD.
- Chain modes: write SYSTEM token output from roles 01, 05, and 09 as DESIGN.md ([design-md-token-schema.md](references/design-md-token-schema.md)). Then run VALIDATE.

## Precedence rules (all modes)

- Obey explicit user or brief direction over every rule in this skill. The user's word wins 100%. Treat a directed choice (a color, a layout, an effect) as a non-tell. Tag it `// BRIEF:`.
- Apply the stricter rule when two rules conflict, unless the brief directs otherwise.
- Check the slop-to-premium pair ([premium-markers.md](references/premium-markers.md)) and the design context ([contexts.md](references/contexts.md)) before you ban or flag a pattern. Treat the crafted version of a pattern as not a tell.
- Never treat zero tells as done. Zero tells with a weak signature is slop. Require a signature (S1-S7). Apply the signature gate without exception: Axis 7 below 40 caps the overall at 59 ([evaluate-scoring.md](references/evaluate-scoring.md)).
- BUILD and SYSTEM: keep the outright bans on eyebrows, decorative pills, and em dashes. EVALUATE: keep catalog severities and context tolerances, so third-party scores stay calibrated.
- Keep tell IDs and names in English in every report.

## Core generation rules (all modes)

Tags in parentheses name the matching tell in [tells.md](references/tells.md).

### 1. Layout and composition

- Ban container sprawl (K13, K6, L21): no bordered, rounded card around every element. Separate content with typography, negative space, and layout.
- Ban the split heading/description header (heading left, description right, same line). Stack the heading and its supporting text vertically.

### 2. Typography and hierarchy

- Ban the "Eyebrow" kicker (K2, K20, L5, L6): small, all-caps, colored pre-title text above section headings.
- Allow ONE subtitle per heading block.
- Ban decorative trailing punctuation (periods, dots, bullets, small squares) on titles, headings, and wordmarks, including oversized or accent-colored punctuation and shapes from HTML, CSS pseudo-elements, or graphics. End the text cleanly. Keep punctuation only when it is part of a supplied name or required for meaning.

### 3. UI components and elements

- Ban decorative pills and badges (K2, K8, K18, K22). Use them only for dynamic, actionable data (e.g., `Status: Active`, `14 Errors`).
- Ban unnecessarily numbered cards (L12). Number cards (01, 02, 03) only for a strict, sequential process or chronological funnel.

### 4. Text density and metadata restraint

Tiny labels, captions, and pseudo-technical metadata that fake richness or "editorial" depth are the biggest slop tell. Restraint is mandatory.

- Ban decorative metadata / "data exhaust." (W3, S7). Ban invented coordinates (`47.6062°N`), timestamps and dates, version, issue, and volume tags (`VOL. 04`, `ISSUE 02`), edition names, reading times (`READING: 41 MIN`), page or item counts (`248 PAGES`), source counts (`LIVE · 11 SOURCES`), plate, figure, and section indices (`PLATE 01`, `00 / SIGNATURE`), file paths, and similar ornamental annotations. Include such data ONLY when it is real, functional, and necessary.
- Ban all-caps monospace micro-label clutter (T4, T5) on headers, footers, corners, image edges, and section breaks.
- Enforce a strict label budget (W2) on every label, caption, tag, and line of microcopy. Label removal test: remove the text. If no real information is lost, delete it. Prefer fewer, larger, meaningful elements over many tiny ones.
- Ban redundant labeling: a `LOGO` tag on the logo, a `HERO` tag on the hero, or the same identity (name, edition, location) restated in multiple places.
- Fill quiet space with authored atmosphere (S2) and the signature artifact (S1), never with labels, coordinates, or metadata. Empty is a miss (M7, L11).

### 5. Visuals, iconography and data

- Ban Unicode emojis in UI design (K1). Never use emojis as icons.
- Use a bespoke icon set in one house style for brand and feature visuals. Allow library icons (e.g., Lucide, Phosphor) only for utility controls of `32px` or less.
- Never place one pack icon on every feature card (K1). Never park an icon or logo on a filled tile or chip (K24).
- In EVALUATE, a `// CONTEXT:` exclusion for K1 stays valid in SaaS product UI ([contexts.md](references/contexts.md)).
- Ban scaling icons as graphics (K4): icons are for utility, max `32px`. Never scale a generic line icon to `128px` as a hero illustration. Use custom abstract shapes, images, or UI snippets for graphics.
- Ban generic gradient charts. Make charts show realistic data scales and grouping, not sweeping linear gradients behind disconnected or unrelated metric call-outs.
- Ban the Purple/Blue SaaS gradient (C1, C2, C13, C14): default linear and blue/purple gradients. Use solid brand colors or strict monochrome. Allow a mesh or grain-dithered gradient only in a non-default hue family, with a stated reason. Never ship a banded gradient (C14).
- Ban heavy glassmorphism (K25). Use `backdrop-filter: blur()` only when the element floats over a complex, moving, or highly-textured background worth refracting (refraction, edge dispersion, top-lip highlight, light frost, tuned inner and drop shadows).
- Ban flat, muddy, heavy single-layer drop shadows (X6, X7, X8, X9). Use multi-layer, low-offset, tinted, single-direction shadows, or no shadow. Use hard, brutalist borders only when the brief calls for brutalism; document the brief. Never fake a shadow with an offset duplicate rectangle (X7). Trace test: if you can trace the shadow border, it is a box and not a shadow (X8).

### 6. Content and copywriting (the forbidden words)

- Never write AI-generated filler copy.
- STRICTLY BAN the following words in placeholder text, headings, and feature descriptions:
  - Unleash / Unlock
  - Supercharge
  - Elevate
  - Seamless / Seamlessly
  - Leverage
  - Dive In
  - Tapestry
  - Next-generation / Next-level
- PROHIBIT em dashes (W1). Never use the em dash character (U+2014, `—`) in headings or body text. Rewrite with commas, periods, or parentheses.
- Apply the ACTIONABLE COPY RULE: prioritize "Show, Don't Tell." (K7, K16). Replace an abstract icon plus a paragraph with a real snippet of the actual UI, a code block, or a data table that demonstrates the feature. Show real, populated product UI, code, or data only. Never use a toy SDK call in a traffic-light window (K16) or an empty mock window (K7).

## Absolute execution rules (all modes)

In EVALUATE, report each rule as pass, fail, or unverifiable in its own table. A fail is a critical tell and triggers the absolute-rule gate ([evaluate-scoring.md](references/evaluate-scoring.md)).

1. **Content visible by default** (M1). Never gate content on an entrance animation (`opacity:0` + reveal).
2. **Clear the cut** (X2, X11). Never slice text or controls with clip, notch, overflow, or fixed height.
3. **Parallel alignment** (X3). Share baselines across comparable columns. Anchor buttons.
4. **Real centering** (X1). Center everything meant to be centered, mathematically and optically.
5. **Legible contrast** (X5). Clear every text against its background by a real value gap. Meet WCAG 2.2 AA: 4.5:1 for normal text, 3:1 for large text and UI components.
6. **Controls work** (M8). Make every interactive-looking control respond.

## Mode BUILD

Never require the 18-question briefing in BUILD. It applies to SYSTEM only.

1. Read the brief. Treat explicit directions as overrides (`// BRIEF:`). Detect the design context with the detection list in [contexts.md](references/contexts.md) (How to use).
2. Decide the signature artifact (S1) FIRST. Build sections around it. See [premium-markers.md](references/premium-markers.md) (S1-S7, field notes).
3. Pick the display face off the Google shelf. Avoid the T1 rejected list in [tells.md](references/tells.md). Use the foundries in the premium-markers field notes. View each candidate rendered. Never name faces from memory.
4. Build the premium version of every pattern in the slop-to-premium pairs table.
5. Self-check before you ship: apply the core and absolute rules, sweep the tells groups C, T/W, K, L, M, X. Run the soul tests in premium-markers (Adding Soul). Fix every hit.
6. Deliver the code with a short self-check note. Offer EVALUATE.

## Mode SYSTEM

1. **Gather briefing.** Answer all 18 questions in [system-briefing.md](references/system-briefing.md) before any output. Retain all answers in conversation context.
2. **Present menu.** Display the 10 generators below. Accept single or multiple selections.
3. **Execute.** Load the selected `references/system-roles/role-*.md` file as the sole source. Never mix role files. Apply briefing data. Generate output consistent with the briefing (brand name, colors, tone, platform, tech stack), in clear, professional, immediately usable formatting with no placeholders left unfilled.
4. **Loop.** After each delivery, present the menu again until the user selects "Exit".

|#|Generator|Role-play|Reference|
|---|-----------|-----------|-----------|
|1|Design System Architect|Apple Principal Designer → HIG-level system|[role-01](references/system-roles/role-01-design-system-architect.md)|
|2|Brand Identity Creator|Pentagram Creative Director → strategy + rationale|[role-02](references/system-roles/role-02-brand-identity-creator.md)|
|3|UI/UX Pattern Master|Apple Senior UI Designer → 8 detailed screens|[role-03](references/system-roles/role-03-ui-ux-pattern-master.md)|
|4|Marketing Asset Factory|Top agency Creative Director → 47+ assets|[role-04](references/system-roles/role-04-marketing-asset-factory.md)|
|5|Figma Auto-Layout Expert|Figma Design Ops Specialist → technical specs|[role-05](references/system-roles/role-05-figma-auto-layout-expert.md)|
|6|Design Critique Partner|Apple Design Director → Nielsen critique + alternatives|[role-06](references/system-roles/role-06-design-critique-partner.md)|
|7|Design Trend Synthesizer|frog Design Researcher → 2026 trends + roadmap|[role-07](references/system-roles/role-07-design-trend-synthesizer.md)|
|8|Accessibility Auditor|Apple Accessibility Specialist → WCAG 2.2 AA audit|[role-08](references/system-roles/role-08-accessibility-auditor.md)|
|9|Design-to-Code Translator|Vercel Design Engineer → production-ready code|[role-09](references/system-roles/role-09-design-to-code-translator.md)|
|10|Presentation Designer|Apple Presentation Designer → executive narrative|[role-10](references/system-roles/role-10-presentation-designer.md)|
|11|Exit|||

- Apply the core rules, absolute rules, and premium pairs to every role deliverable. Keep the role templates unchanged.
- Deliver the premium-pair version when a role template asks for a flagged element. Note the swap: testimonial card (K10, W3), icon bullets (K1, K4), Liquid Glass (K25), gradient logo tile (K12), default hero stack (L1), three-tier pricing (L3).

## Mode VALIDATE

Use VALIDATE to lint, diff, and export DESIGN.md with the official `@google/design.md` CLI. Load [validate-design-md.md](references/validate-design-md.md) for the procedure, diff and export commands, Windows alias, and anti-patterns.

- Run the CLI as `npx @google/design.md` every time. It resolves the latest published version. Never install it globally. Never vendor or cache it.
- Download a remote DESIGN.md locally before linting. Never fetch a remote URL directly (indirect prompt injection risk).
- Confirm the active rule set at runtime with `spec --rules-only`. Never assume it from memory or from the bundled references.
- Re-run lint after every fix. Never skip re-validation.

```bash
npx @google/design.md lint DESIGN.md
npx @google/design.md lint --format json DESIGN.md
npx @google/design.md spec --rules-only --format json
```

Report each `findings[]` entry with this table, what the rule checks, why it matters, and a concrete fix.

|Severity|Meaning|Action|
|---|---|---|
|`error`|Spec violation — file is invalid|Must fix|
|`warning`|Best practice violation — file is valid but suboptimal|Should fix|
|`info`|Informational — suggestions for improvement|Nice to fix|

## Mode EVALUATE

Use EVALUATE to score a design against the catalog and write a Slop Report.
Load [evaluate-procedure.md](references/evaluate-procedure.md) first (parameters, evidence acquisition SOP, workflow, gotchas).

Parameters: `target` (default: ask user), `brief`, `context`, `output` (default `./SLOP-REPORT.md`), `compare` (previous report, for tracking mode).

- Never score a check you could not observe. Mark it **Unverifiable** and exclude it from the axis.
- Tag every excluded tell with `// BRIEF:`, `// DESIGN DECISION:`, `// CONTEXT:`, or `// PREMIUM PAIR:`. A tell without a tag counts. See [evaluate-exclusions-qa.md](references/evaluate-exclusions-qa.md).

1. Gather evidence with the evidence acquisition SOP. Read [tells.md](references/tells.md), [premium-markers.md](references/premium-markers.md), and [contexts.md](references/contexts.md).
2. Sweep axes 1-6. Cite or cut: record a tell only with concrete evidence (hex value, font name, `file:line`). Check the premium pair first.
3. Run the absolute rules check, with evidence.
4. Score axes 7-8, the 7 signature elements (S1-S7) and the 4 cohesion checks (H1-H4), at 0, 50, or 100. Add a one-line justification to each.
5. Compute with `scripts/score.py` from the skill root. Never compute by hand. Pass each triggered gate with `--cap` ([evaluate-scoring.md](references/evaluate-scoring.md)).
   ```bash
   python3 scripts/score.py axis CRIT MAJOR MINOR
   python3 scripts/score.py overall 1:80:2 2:65:2 ... [--cap 59] [--cap 69]
   ```
6. Write the report to `output` with [slop-report-template.md](references/slop-report-template.md). End with the 3-5 prioritized fixes that move the score most, ranked by weighted impact. Rank a missing signature above any single tell.
7. Pass the quality checklist in [evaluate-exclusions-qa.md](references/evaluate-exclusions-qa.md). A single failure means "report not ready".

Optional: calibrate Axes 7-8 and the checklist through TypeSafe Jev when the harness has a tool whose name contains `jev` or `typesafe` ([jev-integration.md](references/jev-integration.md)).

## Reference index (load when)

- [references/tells.md](references/tells.md): BUILD self-check; EVALUATE sweep.
- [references/premium-markers.md](references/premium-markers.md): BUILD signature; EVALUATE Axes 7-8.
- [references/contexts.md](references/contexts.md): you detect the design context.
- [references/evaluate-procedure.md](references/evaluate-procedure.md): EVALUATE starts.
- [references/evaluate-scoring.md](references/evaluate-scoring.md): you compute scores, caps, gates.
- [references/evaluate-exclusions-qa.md](references/evaluate-exclusions-qa.md): you exclude a tell or run the final checklist.
- [references/slop-report-template.md](references/slop-report-template.md): you write the report.
- [references/jev-integration.md](references/jev-integration.md): the harness has a Jev tool.
- [references/system-briefing.md](references/system-briefing.md): SYSTEM starts.
- [references/system-roles/](references/system-roles/): you run the selected menu item.
- [references/validate-design-md.md](references/validate-design-md.md): VALIDATE starts.
- [references/design-md-lint-rules.md](references/design-md-lint-rules.md): you explain a lint finding.
- [references/design-md-token-schema.md](references/design-md-token-schema.md): you author or fix tokens.
- [scripts/score.py](scripts/score.py): EVALUATE step 5.
- [scripts/jev_questions.json](scripts/jev_questions.json): the Jev run.

## Related skills

- skill-evaluation: origin of the cite-or-cut, weighted-axes method. https://github.com/fabricioctelles/skills/tree/main/skills/skill-evaluation
