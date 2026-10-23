# EVALUATE: Exclusions and Quality Checklist

Load this file when you record exclusions or deliver the Slop Report.

## Exclusion system

- Give every excluded tell a tag from the table below (the audit trail).
- Count every tell without a tag. No exceptions.
- Reject lazy exclusions: never accept "we liked it" or "it looked good".

### Justification tags

|Tag|When to use|Example|
|-----|-------------|---------|
|`// BRIEF:`|Client/stakeholder explicitly directed this choice|`// BRIEF: client requested blue-purple gradient as brand identity`|
|`// DESIGN DECISION:`|Documented design decision with concrete reasoning|`// DESIGN DECISION: countdown is real — sale ends 2026-08-01`|
|`// CONTEXT:`|Design context makes this pattern acceptable|`// CONTEXT: mono typeface is appropriate for code snippets in SaaS docs`|
|`// PREMIUM PAIR:`|This is the crafted version, not the slop version|`// PREMIUM PAIR: glass effect has proper refraction, edge dispersion, tuned shadows`|

Evidence bar for each tag:

- Cite an actual brief reference for `// BRIEF:`.
- Give concrete reasoning for `// DESIGN DECISION:`.
- Use `// CONTEXT:` only for a tell in the Tolerance table of the identified context ([contexts.md](contexts.md)).
- Cite attributes from the pairs table in [premium-markers.md](premium-markers.md) for `// PREMIUM PAIR:`.

### Valid vs invalid exclusions

**Valid exclusions:**
```markdown
| C1 | Blue→purple gradient | `// BRIEF: brand guidelines v2.3 specify #6366f1→#8b5cf6` |
| K14 | Countdown timer | `// DESIGN DECISION: real sale ends 2026-12-31, verified in CMS` |
| T4 | Mono as house voice | `// CONTEXT: SaaS product with code-heavy documentation` |
| K25 | Glass effect | `// PREMIUM PAIR: proper backdrop blur, chromatic dispersion, directional light` |
```

**Invalid exclusions (tell still counts):**
```markdown
| C1 | Blue→purple gradient | "we liked it" | ❌ Not a justification
| K9 | Default CTA pair | "it's our style" | ❌ Too vague
| L1 | Default hero stack | "approved by team" | ❌ Who? When? Why?
| K6 | Kitchen-sink card | "industry standard" | ❌ Slop IS the industry standard
```

## Exclusion limits

- More than 5 exclusions: review each one. Suspect an ignored brief or a lenient evaluator.
- More than 10 exclusions: treat the report as faulty. Either the brief allows nearly everything (then why evaluate?) or exclusions inflate the score.
- Treat signature-element exclusions as almost never valid. If S1–S7 are excluded, the design has no signature by definition.

## Exclusion documentation in report

Format the Excluded tells table as follows:

```markdown
## Excluded tells

| ID | Tell | Exclusion reason |
|----|------|------------------|
| C1 | Blue→purple gradient | `// BRIEF: brand guidelines v2.3 specify #6366f1→#8b5cf6` |
| K14 | Countdown timer | `// DESIGN DECISION: real sale ends 2026-12-31, verified in CMS` |

**Exclusion summary:** 2 tells excluded (1 BRIEF, 1 DESIGN DECISION)
```

## Challenging exclusions

Check exclusions first when you review another Slop Report.

1. **Check the tag is present.** No tag = tell counts.
2. **Check the tag is appropriate.** `// BRIEF:` needs an actual brief reference. Apply the evidence bar to the other tags.
3. **Check the reasoning is concrete.** Vague reasoning = tell counts.
4. **Check the exclusion count is reasonable.** More than 5 warrants scrutiny.

## Quality checklist

Run every item before delivery. One failed item means "report not ready".

### Pre-sweep checks

- [ ] **Evidence inventory complete:** Document what you captured (code, screenshots, live URL) and what is Unverifiable.
- [ ] **Brief documented:** Summarize the brief in the report header, or write "no brief".
- [ ] **Design context identified:** Identify the design type (landing page, SaaS dashboard, editorial, e-commerce). Read [contexts.md](contexts.md) to adjust priorities and tolerances.
- [ ] **All reference files read:** Load [tells.md](tells.md), [premium-markers.md](premium-markers.md), and [contexts.md](contexts.md) before the sweep.

### During-sweep checks

- [ ] **Cite-or-cut enforced:** Give every recorded tell an ID, a severity, and a concrete citation (hex value, font name, `file:line`, or screenshot region).
- [ ] **Premium pair checked:** Verify that the tell is not the crafted premium version of the pattern.
- [ ] **Portability test applied:** For borderline cases, ask: "Could this element be moved to another site without alteration?" Yes = tell. No (specific to this brand) = no tell.
- [ ] **Defense test applied:** For borderline cases, ask: "Could the designer defend this choice with concrete reasoning if asked?" No = tell. Slop cannot be defended. Deliberate choices can.
- [ ] **Section attribution:** Assign every tell to a section (Hero, Features, Pricing, Footer, etc.) for the Section Ledger.
- [ ] **Severity discipline:** Reserve critical for absolute-rule violations only. Never inflate severity.

### Exclusion checks

- [ ] **Exclusions documented:** Tag every excluded tell.
- [ ] **Exclusions are genuine:** Reject "we liked it" and "it looked good". Accept only reasons that meet the evidence bar.
- [ ] **Exclusion count reasonable:** Double-check each exclusion above 5. Mass exclusions mean an ignored brief, not tells that do not apply.

### Post-sweep checks

- [ ] **All unverifiable checks marked:** Never pass or skip a check silently.
- [ ] **All 6 absolute rules reported:** Report pass/fail/unverifiable with evidence.
- [ ] **All 11 signature/cohesion items scored:** Score each 0/50/100 with a one-line justification.
- [ ] **Section Ledger complete:** Give every major section a verdict (CLEAN/SUSPICIOUS/INFLATED/CRITICAL), tell count, and action.
- [ ] **Gates applied correctly:**
  - [ ] Signature gate: if Axis 7 < 40, cap overall at 59
  - [ ] Absolute-rule gate: if any crit, cap overall at 69
  - [ ] Compounding cap: if ≥3 major layout tells, cap Axis 4 at 40
- [ ] **Math from script only:** Run all scoring through [score.py](../scripts/score.py). Never compute by hand.

### Report checks

- [ ] **Template followed exactly:** Match the structure of [slop-report-template.md](slop-report-template.md).
- [ ] **Fixes ranked by weighted impact:** Signature issues (3x weight) typically outrank single tells.
- [ ] **Language correct:** Write the report in the user's language. Keep tell IDs in English.

### Final self-audit

- [ ] **"What still looks like obvious slop that I didn't flag?"** If something screams slop but is not in your findings, find its tell or note a catalog gap.
- [ ] **"Did I over-correct?"** A sparse report on a clearly-slop design suggests missed tells. A bloated report on a premium design suggests false positives.
- [ ] **"Would I trust this report if someone else wrote it?"** Read the report as a colleague's work. Check that every claim holds up.
