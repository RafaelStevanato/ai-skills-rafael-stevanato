# EVALUATE Procedure

Use this file to run EVALUATE mode of [anti-slop](../SKILL.md).

Contents: Parameters, Modes, Evidence channels, Evidence SOP, Workflow, Gotchas.

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `target` | What to evaluate: live URL, screenshot(s), code path, or Figma export | Ask user |
| `brief` | Brand brief or explicit user directions the design followed | None |
| `context` | Design type: `landing`, `saas`, `editorial`, `ecommerce`, or `auto` | `auto` |
| `output` | Path to write the report | `./SLOP-REPORT.md` |
| `compare` | Path to a previous report for tracking mode (temporal evolution) | None |

- Load [contexts.md](contexts.md) to adjust priorities and tolerances for the design type.
- Write the report in the language the user is speaking.
- Keep tell IDs and names in English. They stay greppable against the catalog.

## Evaluation modes

### Standard mode (default)

- Run a single evaluation of one design.
- Produce a Slop Report with scores, tells, section ledger, and prioritized fixes.

### Comparison mode

- Use for a side-by-side evaluation of two different designs (e.g., competitor analysis, A/B variants).
- Add `--compare` pointing to another target or an existing report.

### Tracking mode

- Use to evaluate the same design over time to measure improvement.
- Use when:
  - Running weekly/sprint design reviews
  - Measuring progress after a redesign
  - Validating that fixes actually moved the score
- Treat the block below as an invocation sketch. No `anti-slop` executable exists.

```bash
# First evaluation — establishes baseline
anti-slop evaluate --target https://site.com --output ./reports/baseline.md

# Later evaluation — tracks evolution
anti-slop evaluate --target https://site.com --output ./reports/week-2.md \
  --compare ./reports/baseline.md
```

Add these 7 items to the report in tracking mode:
- Score progression table with trends (✅ improved / ⚠️ regressed)
- Tells resolved (what got fixed)
- New tells (what got introduced)
- Regressions (axes/sections that got worse)
- Section ledger evolution
- Velocity metrics (tells resolved per week, score improvement rate)
- Recommendations for next iteration

Read [slop-report-template.md](slop-report-template.md) for the full tracking output format.

## Evidence channels

- Never score a check you could not observe.
- Mark it **Unverifiable**. Exclude it from scoring (like N/A in skill-evaluation).

| Channel | Can verify | Cannot verify |
|---------|-----------|---------------|
| Code (CSS/JSX/HTML) | Fonts, hex values, gradients, shadows, radii, `opacity:0` gating, icon imports, layout skeletons | Optical centering, rendered contrast, seams, whether controls respond |
| Screenshot(s) | Everything visual: palette, type, layout, alignment, centering, clipping, contrast, seams | Hover/scroll motion, dead controls, invisible-content trap, responsive behavior |
| Live URL (browse + screenshot) | All of the above plus interactions, motion, fold ownership | Only what you didn't exercise |

With code, run these greps before you read files in full:
- `fonts.googleapis|next/font`
- `lucide-react`
- `linear-gradient`
- `box-shadow`
- `border-radius: *9999`
- `backdrop-filter`
- `opacity: *0`
- `initial={{ *opacity: *0`
- `overflow: *hidden`
- `clip-path`
- `position: *fixed`

Treat each hit as a lead, not a verdict.
Confirm each hit against its entry in [tells.md](tells.md) before you record it.

## Evidence acquisition SOP

Route by the type of `target`. End every route with the evidence inventory (last subsection).

### Live URL

- Prefer this route whenever the target is reachable. It is the richest channel.
- Use the browser automation this session has: a browser MCP such as Playwright or Chrome DevTools.
- Use `npx playwright screenshot` as the no-MCP fallback.
- Save every captured artifact to the scratchpad. Cite each finding as `file + region`.

Capture in this order:

1. Load the page at desktop (1440×900) and mobile (390×844). Wait for network idle.
2. Take a full-page screenshot of both viewports **immediately after load, before any scrolling**.
   Sections sitting at `opacity:0` waiting for a scroll reveal show up blank here (M1 evidence).
3. Scroll pass top to bottom. Then take a second full-page capture.
   Diff the two captures mentally for reveal-gated content, seams (C11, X13), and fold ownership (L16).
4. Run the interaction pass:
   - Hover the primary CTA, one card, one nav link (M2–M4).
   - Click every tab, accordion, toggle, and button (M8).
   - Tab through the page and confirm a visible focus ring (X14).
5. Take zoom crops at 2x of:
   - anything near a clipped edge (X2)
   - circled/tiled numbers and icons (X1)
   - pricing columns side by side (X3)
   - button labels (X5)
6. Pull the rendered sources for the code-channel greps:
   - font names from the network panel or `<link>`/`@font-face`
   - computed hex values from the stylesheets

### No browser automation available

- Fetch the HTML/CSS (`curl`). Run the code channel on it.
- Ask the user for full-page desktop + mobile prints.
- Mark every visual-only check and every interaction check Unverifiable until the prints arrive.
- Never score a visual check from raw HTML.

### Screenshots

- Read each image.
- Ask for full-page desktop + mobile before sweeping if only partial crops were provided.
- Never use a hero-only print to support L11, L15, or the cohesion axis.
- Mark all interaction checks (M1, M8, X14, hover tells) Unverifiable.

### Code path

- Run the greps. Read every file they hit.
- Read the layout/page components and global styles.
- Start the dev server if the project runs locally. Then continue under Live URL.
- Prefer code plus a live render. It is the only combination that can verify everything.

### Figma export

- Treat the export as Screenshots for visual tells.
- Read fonts, hex values, and spacing from the file. They are exact.
- Mark the motion and interaction checks Unverifiable.
- Score Axis 5 as `NA` unless prototypes were shared.

### Evidence inventory

- Write an inventory of what was captured and what is Unverifiable.
- Feed the inventory into the report header.

## Workflow

1. **Gather evidence.** Route the `target` through the Evidence acquisition SOP.
   - Done when: the evidence inventory states what was captured and what is Unverifiable.
2. **Read [tells.md](tells.md).** Sweep against this catalog.
3. **Sweep axes 1–6.** Walk the catalog group by group.
   - Apply **cite-or-cut**: record a tell only with concrete evidence (hex value, font name, `file:line`, or screenshot region).
   - Check each candidate against its premium-pair note. Never record the crafted version of a pattern as a tell.
   - Done when: every catalog group has been swept and every recorded tell carries a citation.
4. **Run the absolute rules check.** Check all six rules (listed in [SKILL.md](../SKILL.md)).
   - Mark each rule pass, fail, or unverifiable, with evidence.
   - Report the rules as [evaluate-scoring.md](evaluate-scoring.md) describes.
5. **Score Axes 7–8.** Read [premium-markers.md](premium-markers.md).
   - Score the 7 signature elements and the 4 cohesion checks.
   - Write a one-line justification for each score.
   - Done when: all 11 items carry a score and a justification.
6. **Compute.** Run `score.py axis` per tell-counted axis.
   - Run `score.py overall` with weights and any triggered `--cap`.
   - Run the script as `scripts/score.py` from the anti-slop skill root. Never hand-compute.
   - Take the formulas, caps, and gates from [evaluate-scoring.md](evaluate-scoring.md).
7. **Write the report.** Read [slop-report-template.md](slop-report-template.md).
   - Emit exactly that structure to `output`.
   - End with the 3–5 prioritized fixes that would move the score most, biggest weighted delta first.
   - Rank a missing signature above any single tell (it usually outranks one).
   - Run the quality checklist in [evaluate-exclusions-qa.md](evaluate-exclusions-qa.md) before delivery.

## Gotchas

- **The brief overrides the law.**
  - Do not record a choice as a tell when the user or brand explicitly directed it (a color, a layout, an effect).
  - The law says the user's word wins 100%.
  - Ask for the brief when the design clearly follows one.
  - Note each excluded tell in the report with a justification tag. See [evaluate-exclusions-qa.md](evaluate-exclusions-qa.md).
- **Context flips a tell.**
  - Mono on real data is correct.
  - A populated, real-feeling product window is a signature, not the fake-window tell.
  - A tight micro-grid with texture is premium. A full-page graph paper is slop.
  - Always check the premium pair before recording.
- **Don't reward the clean miss.** Zero tells with a weak signature is the most common failure of designs that *tried* to avoid slop. Apply the signature gate without mercy.
- **Severity discipline.** Reserve Critical for *broken*: the six absolute rules. Rate a blue-purple gradient major. It is loud but not broken.
- **One-axis bleed.**
  - Some tells could sit on two axes (cut-off glow is color and execution).
  - The catalog assigns each tell to exactly one axis. Count the tell only there.
- **Portfolio tells.** L19 (recycling your own house style) needs prior work from the same author to verify. Mark L19 Unverifiable without that prior work. Never guess.
