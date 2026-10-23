---
name: anti-slop
description: >-
  Anti-slop UI design in 4 modes. BUILD: generate deliberate, opinionated, functional UI, landing pages, components and frontend code that bans slop tells (eyebrow kickers, decorative pills, purple-blue gradients, glassmorphism, emoji icons, fake metadata, filler words, em dashes). SYSTEM: design systems, brand identity, design tokens, UI/UX patterns, marketing assets, Figma auto-layout specs, design critique, trends, WCAG 2.2 accessibility audit, design-to-code, presentation decks via 10 specialist roles. VALIDATE: lint, diff and export DESIGN.md with the @google/design.md CLI (broken token references, contrast, Tailwind or DTCG export). EVALUATE: score a URL, screenshot, code or Figma export for AI slop; write a Slop Report with 0-100 Slop Index and grade. Use when the user says anti-slop, design a UI, build a landing page, create design system, validate DESIGN.md, npx design.md lint, slop report, is this design AI slop, de-slop review. For prose use anti-ai-slop-escrita-ptbr.
license: Apache-2.0
metadata:
  author: "https://ft.ia.br"
  version: "3.0.0"
  date: "2026-10-23"
  consolidated: "2026-10-23 ASD-STE100 rewrite"
  merged-from: "anti-slop, slop-eval 1.1.0, ultimate-design-system-master 2.2, design-md-validator 1.3"
  category: "design"
  repository: "https://github.com/fabricioctelles/skills"
  attribution: "Tell catalog, absolute rules and signature formula distilled from the pols.dev anti-slop design law https://pols.dev/slop.md"
  source-anti-slop: "no author or license declared upstream"
  source-slop-eval: "author https://ft.ia.br, version 1.1.0, date 2026-08-24, license Apache-2.0, category code-quality-and-review"
  source-ultimate-design-system-master: "author ft.ia.br, version 2.2, date 2026-03-08, license Apache 2.0, category code-scaffolding-and-templates"
  source-design-md-validator: "author https://ft.ia.br, version 1.3, date 2026-09-16, license Apache 2.0, category product-verification"
  license-compliance: "SPDX Apache-2.0 normalized from the spellings Apache-2.0 and Apache 2.0 in the three licensed sources"
  upstream-spec: "https://github.com/google-labs-code/design.md"
  upstream-cli: "https://www.npmjs.com/package/@google/design.md"
  upstream-stitch-skills: "https://github.com/google-labs-code/stitch-skills"
---

> **⚠️ EXECUTION DIRECTIVE (INPUT vs. OUTPUT SEPARATION):**
> The rules in this skill use strict ASD-STE100 controlled language solely for zero-ambiguity parsing and token efficiency.
> - **NEVER copy this telegraphic or robotic style into human-facing outputs.**
> - Apply 80% ASD-STE100 in final outputs ONLY when explaining dense technical concepts.

# Anti-Slop

Run one of four modes: BUILD, SYSTEM, VALIDATE, EVALUATE.
Apply the core generation rules and the absolute execution rules in every mode.

## Mode router

| Mode | Trigger phrases | Load | Deliverable |
|------|-----------------|------|-------------|
| BUILD | Generate or redesign UI, landing page, website, component, frontend code. Default when the output is UI. "design a UI", "build a landing page", "anti-slop" | Core rules below, [premium-markers.md](references/premium-markers.md), [tells.md](references/tells.md), [contexts.md](references/contexts.md) | UI code + self-check note |
| SYSTEM | "create design system", "build brand identity", "design UI components", "generate design tokens", "create figma specs", "review my design" (heuristics, critique), "analyze design trends", "audit accessibility", "convert design to code", "create presentation deck" | [system-briefing.md](references/system-briefing.md) + exactly one role file from the [SYSTEM menu](#mode-system) | Role deliverable + menu loop |
| VALIDATE | "validate DESIGN.md", "lint DESIGN.md", "check my design.md", "design.md spec compliance", "WCAG contrast check" (DESIGN.md file), "broken token references", "design token validation", "export design tokens", "diff design systems", "design.md audit", "@google/design.md", "npx design.md lint", "design system validation", "frontmatter tokens", any request to verify a DESIGN.md file | [validate-design-md.md](references/validate-design-md.md), [design-md-lint-rules.md](references/design-md-lint-rules.md), [design-md-token-schema.md](references/design-md-token-schema.md) | Lint findings + fixes + re-lint |
| EVALUATE | "evaluate design slop", "slop report", "is this design AI slop", "audit this landing page design", "de-slop review", "Slop Index", any request for an objective score of how generic or machine-made a design looks | [evaluate-procedure.md](references/evaluate-procedure.md), [evaluate-scoring.md](references/evaluate-scoring.md), [tells.md](references/tells.md), [premium-markers.md](references/premium-markers.md), [contexts.md](references/contexts.md), [evaluate-exclusions-qa.md](references/evaluate-exclusions-qa.md), [slop-report-template.md](references/slop-report-template.md), [score.py](scripts/score.py) | `./SLOP-REPORT.md` |

### Disambiguation rules

- Default to BUILD when the deliverable is UI code.
- Route "review my design" or "audit this design" to EVALUATE when the user mentions slop, generic, AI-made, score, or index.
- Route "review my design" to SYSTEM role 6 when the user mentions heuristics, usability, or critique.
- Ask the user which mode to use when neither signal exists.
- Route "audit accessibility" of a design to SYSTEM role 8.
- Route WCAG contrast of a DESIGN.md file to VALIDATE.
- Route prose, text, and copy writing tasks to the skill anti-ai-slop-escrita-ptbr.
- Never use this skill to fix text. It fixes design.

### Mode chaining

- Run EVALUATE on a BUILD output when a live render or code exists (optional self-audit).
- Write SYSTEM token output from roles 01, 05, and 09 as DESIGN.md. Then run VALIDATE.
- Feed EVALUATE prioritized fixes back into BUILD.

## Precedence rules (all modes)

- Obey explicit user or brief direction over every rule in this skill.
- Treat a directed choice (a color, a layout, an effect) as a non-tell. The user's word wins 100%.
- Document each override with a `// BRIEF:` tag.
- Apply the stricter rule when two rules conflict, unless the brief directs otherwise.
- Check the slop-to-premium pair before banning or flagging a pattern. See [premium-markers.md](references/premium-markers.md).
- Treat the crafted version of a pattern as not a tell.
  - Mono on real data is correct.
  - A populated, real-feeling product window is a signature, not the K7 fake window.
  - A tight textured micro-grid is premium. A full-page graph paper is slop (C15).
- Check the design context before flagging. See [contexts.md](references/contexts.md).
- Never treat zero tells as done. Require a signature (S1-S7).
- Treat zero tells with a weak signature as slop.
- Apply the signature gate without exception: Axis 7 below 40 caps the overall at 59. See [evaluate-scoring.md](references/evaluate-scoring.md).
- Keep quiet space free of labels and metadata.
- Add authored atmosphere (S2) and one signature artifact (S1). Empty is a miss (M7, L11).
- BUILD and SYSTEM: keep the outright bans on eyebrows, decorative pills, and em dashes.
- EVALUATE: keep catalog severities and context tolerances, so third-party scores stay calibrated.
- Keep tell IDs and tell names in English in every report.
- Write report text in the user's language.

## Core generation rules (all modes)

Apply all 21 rules in BUILD and SYSTEM.
Tags in parentheses name the matching tell in [tells.md](references/tells.md).

### 1. Layout and composition

- Ban container sprawl (K13, K6, L21).
  - Never wrap every element in a bordered card with a border radius.
  - Separate content with typography, negative space, and layout.
- Ban the split heading/description header.
  - Never place a section heading on the left and its description on the right side of the same line.
  - Stack the heading and its supporting text vertically.

### 2. Typography and hierarchy

- Ban the "Eyebrow" kicker (K2, K20, L5, L6).
  - Never use the small, all-caps, colored pre-title text above section headings.
  - Keep primary titles free of pre-title text.
- Enforce a strict subtitle limit.
  - Set a maximum of ONE subtitle per heading block.
  - Force conciseness in hierarchy.
- Ban decorative trailing punctuation.
  - Never append periods, dots, bullets, or small squares to titles, headings, or wordmarks as a visual flourish.
  - Include oversized or accent-colored punctuation in the ban.
  - Include shapes added through HTML, CSS pseudo-elements, or graphics in the ban.
  - End the text cleanly.
  - Keep punctuation only when it is part of a supplied name or required for meaning.

### 3. UI components and elements

- Ban decorative pills and badges (K2, K8, K18, K22).
  - Tie pills, badges, and status indicators to dynamic, actionable data (e.g., `Status: Active`, `14 Errors`).
  - Never use them as decorative flair.
- Ban unnecessarily numbered cards (L12).
  - Never number cards (01, 02, 03) unless the content describes a strict, sequential process or chronological funnel.

### 4. Text density and metadata restraint

Treat tiny labels, captions, and pseudo-technical metadata that fake richness or "editorial" depth as the biggest slop tell.
Restraint is mandatory.

- Ban decorative metadata / "data exhaust" (W3, S7).
  - Never scatter fake technical micro-labels to make a layout look detailed.
  - Ban invented coordinates (`47.6062°N`).
  - Ban timestamps and dates.
  - Ban version, issue, and volume tags (`VOL. 04`, `ISSUE 02`).
  - Ban edition names.
  - Ban reading times (`READING: 41 MIN`).
  - Ban page or item counts (`248 PAGES`).
  - Ban source counts (`LIVE · 11 SOURCES`).
  - Ban plate, figure, and section indices (`PLATE 01`, `00 / SIGNATURE`).
  - Ban file paths.
  - Ban similar ornamental annotations.
  - Include such data ONLY when it is real, functional, and necessary for the user.
- Ban all-caps monospace micro-label clutter (T4, T5).
  - Never line headers, footers, corners, image edges, and section breaks with small all-caps or monospace tags.
  - Treat these tags as decoration masquerading as information.
- Enforce a strict label budget (W2).
  - Make every label, caption, tag, and line of microcopy carry real, necessary meaning.
  - Run the label removal test: remove the text. If no real information is lost, delete the text.
  - Prefer fewer, larger, meaningful elements over many tiny ones.
- Ban redundant or obvious labeling.
  - Never label what the user can already see (e.g., a `LOGO` tag on the logo, a `HERO` tag on the hero).
  - Never restate the same identity (name, edition, location) in multiple places.
- Enforce generous quiet space over filler (S2, M7).
  - Keep empty regions free of decorative labels, coordinates, and metadata.
  - Never fill a region with metadata just to occupy it.

### 5. Visuals, iconography and data

- Ban Unicode emojis in UI design (K1).
  - Never use emojis as icons.
  - Use a bespoke icon set in one house style for brand and feature visuals.
  - Allow library icons (e.g., Lucide, Phosphor) only for utility controls of `32px` or less.
  - Never place one pack icon on every feature card (K1).
  - Never park an icon or logo on a filled tile or chip (K24).
  - In EVALUATE, a `// CONTEXT:` exclusion for K1 stays valid in SaaS product UI. See [contexts.md](references/contexts.md).
- Ban scaling icons as graphics (K4).
  - Cap icon size at `32px` (utility use only).
  - Never scale a generic line icon to `128px` as a hero illustration.
  - Use custom abstract shapes, images, or UI snippets when a graphic is needed.
- Ban generic gradient charts.
  - Make charts represent realistic data scales and grouping.
  - Never use sweeping linear gradients behind disconnected or unrelated metric call-outs.
- Ban the Purple/Blue SaaS gradient (C1, C2, C13, C14).
  - Ban default linear gradients and blue/purple gradients.
  - Use solid brand colors or strict monochrome.
  - Allow a mesh or grain-dithered gradient only in a non-default hue family, with a stated reason.
  - Never ship a banded gradient (C14).
- Ban heavy glassmorphism (K25).
  - Use `backdrop-filter: blur()` only when the element floats over a complex, moving, or highly-textured background.
  - Require a backdrop worth refracting: refraction, edge dispersion, top-lip highlight, light frost, tuned inner and drop shadows.
  - Never ship banding, shadow leak, a resting halo, or blur that pops on hover.
- Ban flat, muddy drop shadows (X6, X7, X8, X9).
  - Ban heavy, single-layer drop shadows.
  - Use multi-layer, low-offset, tinted, single-direction shadows, or use no shadow.
  - Use hard, brutalist borders only when the brief calls for brutalism. Document the brief.
  - Never fake a shadow with an offset duplicate rectangle (X7).
  - Run the trace test: if you can trace the shadow border, it is a box and not a shadow (X8).

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
- PROHIBIT em dashes (W1).
  - Never use the em dash character (U+2014, `—`) in headings or body text.
  - Rewrite with commas, periods, or parentheses.
- Apply the ACTIONABLE COPY RULE: prioritize "Show, Don't Tell" (K7, K16).
  - Replace an abstract icon plus a paragraph with a real snippet of the actual UI, a code block, or a data table that demonstrates the feature.
  - Show real, populated product UI, code, or data only.
  - Never use a toy SDK call in a traffic-light window (K16).
  - Never use an empty generic mock window (K7).

## Absolute execution rules (all modes)

Obey all six rules in BUILD and SYSTEM output.
In EVALUATE, report each rule as pass, fail, or unverifiable in its own table.
In EVALUATE, count a fail as a critical tell.
In EVALUATE, a fail triggers the absolute-rule gate ([evaluate-scoring.md](references/evaluate-scoring.md)).

1. **Content visible by default** (M1). Never gate content on an entrance animation (`opacity:0` + reveal).
2. **Clear the cut** (X2, X11). Never slice text or controls with clip, notch, overflow, or fixed height.
3. **Parallel alignment** (X3). Share baselines across comparable columns. Anchor buttons.
4. **Real centering** (X1). Center everything meant to be centered, mathematically and optically.
5. **Legible contrast** (X5). Clear every text against its background by a real value gap. Meet WCAG 2.2 AA: 4.5:1 for normal text, 3:1 for large text and UI components.
6. **Controls work** (M8). Make every interactive-looking control respond.

## Mode BUILD

Use BUILD to generate UI, landing pages, components, and frontend code.
Never require the 18-question briefing in BUILD. That gate applies to SYSTEM only.

1. Read the brief. Treat explicit directions as overrides (`// BRIEF:`).
2. Detect the design context with the detection list in [contexts.md](references/contexts.md) (How to use).
3. Decide the signature artifact (S1) FIRST. Build sections around it. See [premium-markers.md](references/premium-markers.md) (S1-S7, field notes).
4. Pick the display face off the Google shelf.
   - Avoid the T1 rejected list in [tells.md](references/tells.md).
   - Use the foundries in the field notes of [premium-markers.md](references/premium-markers.md).
   - View each candidate face rendered before you pick it.
   - Never name faces from memory.
5. Apply the core generation rules and the absolute execution rules.
6. Build the premium version of every pattern in the slop-to-premium pairs table ([premium-markers.md](references/premium-markers.md)).
7. Self-check before you ship.
   - Sweep the [tells.md](references/tells.md) groups C, T/W, K, L, M, X.
   - Run the soul tests in [premium-markers.md](references/premium-markers.md) (Adding Soul).
   - Fix every hit.
8. Deliver the code with a short self-check note. Offer EVALUATE.

## Mode SYSTEM

Use SYSTEM to produce design-system deliverables through 10 specialist roles.

### Workflow

1. **Gather briefing.** Answer all 18 questions in [system-briefing.md](references/system-briefing.md) before any output. Retain all answers in conversation context.
2. **Present menu.** Display the 10 generators below. Accept single or multiple selections.
3. **Execute.** Load the selected `references/system-roles/role-*.md` file as the sole source. Apply briefing data. Generate output.
4. **Loop.** After each delivery, present the menu again until the user selects "Exit".

### Menu

| # | Generator | Role-play | Reference |
|---|-----------|-----------|-----------|
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
| 11 | Exit | | |

### Rules

- Maintain full consistency with briefing data across all outputs.
- Load only the selected role file. Never mix role files.
- Use clear, professional, immediately usable formatting.
- Present the menu again after each delivery.

### Anti-slop overlay

- Apply the core generation rules, the absolute execution rules, and the premium pairs to every role deliverable.
- Keep the role templates unchanged. Enforce the overlay on the output.
- Deliver the premium-pair version when a role template asks for a flagged element. Note the swap in the deliverable.
  - Testimonial card (K10, W3).
  - Icon bullets (K1, K4).
  - Liquid Glass (K25).
  - Gradient logo tile (K12).
  - Default hero stack (L1).
  - Three-tier pricing (L3).
- Obey the brief when it directs a flagged element. See the precedence rules.
- Write token output from roles 01, 05, and 09 as DESIGN.md. Follow [design-md-token-schema.md](references/design-md-token-schema.md). Then run VALIDATE.

### Quality checklist

- [ ] Verify all 18 briefing questions are answered before generating output.
- [ ] Verify only the selected role file was loaded.
- [ ] Verify the output is consistent with the briefing (brand name, colors, tone, platform, tech stack).
- [ ] Verify the formatting is production-ready (no placeholders left unfilled).
- [ ] Verify the menu is presented again after delivery.
- [ ] Verify the core rules, the absolute rules, and the premium pairs are applied to the deliverable.

## Mode VALIDATE

Use VALIDATE to lint, diff, and export DESIGN.md with the official Google `@google/design.md` CLI.
Load [validate-design-md.md](references/validate-design-md.md) for the full procedure, diff and export commands, Windows alias, and anti-patterns.

### Rules

- Run the CLI as `npx @google/design.md` every time. It resolves the latest published version.
- Never install the CLI globally. Never vendor or cache it.
- Download a remote DESIGN.md locally before linting.
- Never fetch a remote URL directly. Untrusted content risks indirect prompt injection.
- Confirm the active rule set at runtime with `spec --rules-only`.
- Never assume the rule set from memory or from the bundled references.
- Never parse YAML frontmatter manually when the linter can do it.
- Never guess contrast ratios. Let the linter compute them.
- Never assume section order is correct. Let the linter verify it.
- Re-run lint after every fix. Never skip re-validation.

### Route by intent

| Trigger | Action |
|---|---|
| User has a DESIGN.md file and wants validation | `lint` |
| User wants to compare two versions | `diff` |
| User wants to export tokens to Tailwind/DTCG | `export` |
| User wants to see the current spec | `spec` |
| User shares a URL to a raw DESIGN.md | Download locally first |
| User asks "is my design.md valid?" | `lint` + interpret findings |

### Commands

```bash
npx @google/design.md lint DESIGN.md
```

Expect JSON with `findings[]` and `summary { errors, warnings, infos }`.
Expect exit code 1 if errors are found, 0 otherwise.

```bash
npx @google/design.md spec
npx @google/design.md spec --rules
npx @google/design.md spec --rules-only --format json
```

### Steps

1. **Obtain the DESIGN.md.**
   - Local file: run `npx @google/design.md lint ./DESIGN.md`.
   - Remote URL: download the file locally first.
   - Stdin: run `cat DESIGN.md | npx @google/design.md lint -`.
2. **Discover the active rule set.** Run before you interpret anything. The rule set changes between releases. The bundled references are a fallback, not the authority.
   ```bash
   npx @google/design.md spec --rules-only --format json
   ```
3. **Run lint.**
   ```bash
   npx @google/design.md lint --format json DESIGN.md
   ```
4. **Interpret findings.** Parse the JSON output and report with this table.

   | Severity | Meaning | Action |
   |---|---|---|
   | `error` | Spec violation — file is invalid | Must fix |
   | `warning` | Best practice violation — file is valid but suboptimal | Should fix |
   | `info` | Informational — suggestions for improvement | Nice to fix |

5. **Provide actionable fixes.** For each finding, explain:
   1. What the rule checks.
   2. Why it matters.
   3. How to fix it, with a concrete code example.
6. **Re-validate after fixes.** Re-run lint to confirm the file passes.

Load [design-md-lint-rules.md](references/design-md-lint-rules.md) for the complete rule table when you explain lint failures.
Load [design-md-token-schema.md](references/design-md-token-schema.md) for the YAML frontmatter schema when you author or fix tokens.

## Mode EVALUATE

Use EVALUATE to score a design against the catalog and write a Slop Report.
Load [evaluate-procedure.md](references/evaluate-procedure.md) first for the parameters, the evidence acquisition SOP, and the gotchas.

### Parameters

| Parameter | Default |
|-----------|---------|
| `target` (live URL, screenshot(s), code path, or Figma export) | Ask user |
| `brief` (brand brief or explicit user directions) | None |
| `context` (`landing`, `saas`, `editorial`, `ecommerce`, or `auto`) | `auto` |
| `output` | `./SLOP-REPORT.md` |
| `compare` (previous report path, for tracking mode) | None |

### Rules

- Never score a check you could not observe. Mark it **Unverifiable** and exclude it from the axis.
- Ask the user for the brief when the design clearly follows one.
- Tag every excluded tell with `// BRIEF:`, `// DESIGN DECISION:`, `// CONTEXT:`, or `// PREMIUM PAIR:`. A tell without a tag counts. See [evaluate-exclusions-qa.md](references/evaluate-exclusions-qa.md).
- Run all arithmetic through `scripts/score.py`. Never compute by hand.

### Steps

1. **Gather evidence.** Route the `target` through the evidence acquisition SOP in [evaluate-procedure.md](references/evaluate-procedure.md).
   - Done when the evidence inventory states what was captured and what is Unverifiable.
2. **Read the references.** Load [tells.md](references/tells.md), [premium-markers.md](references/premium-markers.md), and [contexts.md](references/contexts.md) before the sweep. Identify the design context.
3. **Sweep axes 1-6.** Walk the catalog group by group.
   - Cite or cut: record a tell only with concrete evidence (hex value, font name, `file:line`, or screenshot region).
   - Check the premium pair before you record a tell.
   - Done when every group is swept and every recorded tell carries a citation.
4. **Run the absolute rules check.** Report all six as pass, fail, or unverifiable, with evidence.
5. **Score axes 7-8.** Score the 7 signature elements (S1-S7) and the 4 cohesion checks (H1-H4) at 0, 50, or 100. Add a one-line justification to each.
   - Done when all 11 items carry a score and a justification.
6. **Compute.** Run from the skill root. Pass any triggered gate with `--cap`. See [evaluate-scoring.md](references/evaluate-scoring.md).
   ```bash
   python3 scripts/score.py axis CRIT MAJOR MINOR
   python3 scripts/score.py overall 1:80:2 2:65:2 ... [--cap 59] [--cap 69]
   ```
7. **Write the report.** Read [slop-report-template.md](references/slop-report-template.md). Emit exactly that structure to `output`.
   - End with the 3-5 prioritized fixes that move the score most. Rank by weighted impact.
   - Rank a missing signature above any single tell.
8. **Pass the quality checklist** in [evaluate-exclusions-qa.md](references/evaluate-exclusions-qa.md). Treat a single failure as "report not ready".

Optional: calibrate Axes 7-8 and the quality checklist through TypeSafe Jev. Load [jev-integration.md](references/jev-integration.md) when the harness has a tool whose name contains `jev` or `typesafe`.

## Reference index

| File | Load when |
|------|-----------|
| [references/tells.md](references/tells.md) | BUILD self-check or the EVALUATE sweep. Holds the tell catalog. |
| [references/premium-markers.md](references/premium-markers.md) | BUILD signature decision, premium pairs, soul tests; EVALUATE scoring of Axes 7-8 and fix prescriptions. |
| [references/contexts.md](references/contexts.md) | You detect the design context, or adjust EVALUATE priorities and tolerances. |
| [references/evaluate-procedure.md](references/evaluate-procedure.md) | You start EVALUATE: parameters, modes, evidence channels, SOP, 7-step workflow, gotchas. |
| [references/evaluate-scoring.md](references/evaluate-scoring.md) | You compute EVALUATE scores: axes, weights, caps, gates, Slop Index, grade scale, CI gate. |
| [references/evaluate-exclusions-qa.md](references/evaluate-exclusions-qa.md) | You exclude a tell, challenge an exclusion, or run the final quality checklist. |
| [references/slop-report-template.md](references/slop-report-template.md) | You write the Slop Report, a comparison, or a tracking report. |
| [references/jev-integration.md](references/jev-integration.md) | The harness has a Jev tool and you calibrate Axes 7-8 or the checklist. |
| [references/system-briefing.md](references/system-briefing.md) | SYSTEM mode starts, before any role output. |
| [references/system-roles/](references/system-roles/) | SYSTEM mode: load only the file of the selected menu item (links in the menu table). |
| [references/validate-design-md.md](references/validate-design-md.md) | VALIDATE mode: full procedure, diff, export, Windows alias, anti-patterns, example session. |
| [references/design-md-lint-rules.md](references/design-md-lint-rules.md) | You explain a lint finding. The runtime spec stays authoritative. |
| [references/design-md-token-schema.md](references/design-md-token-schema.md) | You author or fix DESIGN.md tokens, or write SYSTEM token output as DESIGN.md. |
| [scripts/score.py](scripts/score.py) | EVALUATE step 6: axis and overall arithmetic, caps, CI fail gate. |
| [scripts/jev_questions.json](scripts/jev_questions.json) | The Jev calibration run needs the 38 typed questions. |

## Related skills

- anti-ai-slop-escrita-ptbr: use for prose and copy de-slop (PT-BR).
- skill-evaluation: origin of the cite-or-cut, weighted-axes method. https://github.com/fabricioctelles/skills/tree/main/skills/skill-evaluation
- Credit the pols.dev anti-slop design law as the origin of the tell catalog, absolute rules, and signature formula: https://pols.dev/slop.md
