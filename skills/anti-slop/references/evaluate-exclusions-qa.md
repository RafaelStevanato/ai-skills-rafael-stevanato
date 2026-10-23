# EVALUATE: Exclusions and Quality Checklist

Load this file in EVALUATE mode when you record exclusions and before you deliver the Slop Report.

Related files:

- Router: [SKILL.md](../SKILL.md)
- Procedure: [evaluate-procedure.md](evaluate-procedure.md)
- Scoring: [evaluate-scoring.md](evaluate-scoring.md)
- Report structure: [slop-report-template.md](slop-report-template.md)
- Tell catalog: [tells.md](tells.md)
- Premium pairs: [premium-markers.md](premium-markers.md)
- Context tolerances: [contexts.md](contexts.md)

## Exclusion system

- Give every excluded tell a justification tag.
- Count every tell that has no tag. No exceptions.
- Use the tag as the audit trail for each exclusion.
- Reject lazy exclusions.
- Exclude a tell only under one of these four conditions:
  1. The brief or client explicitly directed it (`// BRIEF:`).
  2. A documented design decision justifies it with concrete reasoning (`// DESIGN DECISION:`).
  3. The design context makes the pattern acceptable (`// CONTEXT:`).
  4. The element is the crafted premium version, not the slop version (`// PREMIUM PAIR:`).
- Never accept "we liked it" or "it looked good" as an exclusion reason.

### Justification tags

| Tag | When to use | Example |
|-----|-------------|---------|
| `// BRIEF:` | Client/stakeholder explicitly directed this choice | `// BRIEF: client requested blue-purple gradient as brand identity` |
| `// DESIGN DECISION:` | Documented design decision with concrete reasoning | `// DESIGN DECISION: countdown is real — sale ends 2026-08-01` |
| `// CONTEXT:` | Design context makes this pattern acceptable | `// CONTEXT: mono typeface is appropriate for code snippets in SaaS docs` |
| `// PREMIUM PAIR:` | This is the crafted version, not the slop version | `// PREMIUM PAIR: glass effect has proper refraction, edge dispersion, tuned shadows` |

Evidence bar for each tag:

- Cite an actual brief reference for `// BRIEF:`.
- Give concrete reasoning for `// DESIGN DECISION:`.
- Use `// CONTEXT:` only for a tell listed in the Tolerance table of the identified context in [contexts.md](contexts.md).
- Cite attributes from the pairs table in [premium-markers.md](premium-markers.md) for `// PREMIUM PAIR:`.

### Valid vs invalid exclusions

Model every exclusion on the valid rows.

**Valid exclusions:**
```markdown
| C1 | Blue→purple gradient | `// BRIEF: brand guidelines v2.3 specify #6366f1→#8b5cf6` |
| K14 | Countdown timer | `// DESIGN DECISION: real sale ends 2026-12-31, verified in CMS` |
| T4 | Mono as house voice | `// CONTEXT: SaaS product with code-heavy documentation` |
| K25 | Glass effect | `// PREMIUM PAIR: proper backdrop blur, chromatic dispersion, directional light` |
```

Count the tell for every reason in the invalid rows.

**Invalid exclusions (tell still counts):**
```markdown
| C1 | Blue→purple gradient | "we liked it" | ❌ Not a justification
| K9 | Default CTA pair | "it's our style" | ❌ Too vague
| L1 | Default hero stack | "approved by team" | ❌ Who? When? Why?
| K6 | Kitchen-sink card | "industry standard" | ❌ Slop IS the industry standard
```

## Exclusion limits

- More than 5 exclusions: review each one.
- More than 5 exclusions: suspect that the brief was not followed or that the evaluator is too lenient.
- More than 10 exclusions: treat the report as faulty.
- More than 10 exclusions, cause 1: the brief allows nearly everything. Then question why the design needs evaluation.
- More than 10 exclusions, cause 2: exclusions inflate the score.
- Treat the exclusion of a signature element as almost never valid.
- If S1–S7 are excluded, the design has no signature by definition.

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

- Write one row per excluded tell: ID, tell name, tag plus reason.
- End the section with the exclusion summary line: total count, then count per tag.

## Challenging exclusions

Check exclusions first when you review another author's Slop Report.

1. **Check that the tag is present.** No tag = tell counts.
2. **Check that the tag is appropriate.** `// BRIEF:` needs an actual brief reference. `// CONTEXT:` needs a tell listed in the context Tolerance table. `// PREMIUM PAIR:` needs cited pair attributes.
3. **Check that the reasoning is concrete.** Vague reasoning = tell counts.
4. **Check that the exclusion count is reasonable.** More than 5 warrants scrutiny.

## Quality checklist

- Run every item before you deliver.
- Treat one failed item as "report not ready".
- Treat this list as the self-evaluation rubric and as a hard gate.

### Pre-sweep checks

- [ ] **Evidence inventory complete:** Document what you captured (code, screenshots, live URL). Document what is Unverifiable.
- [ ] **Brief documented:** Summarize the brief in the report header when one is provided. Write "no brief" when none is provided.
- [ ] **Design context identified:** Identify the design type (landing page, SaaS dashboard, editorial, e-commerce). Read [contexts.md](contexts.md) to adjust priorities and tolerances.
- [ ] **All reference files read:** Load [tells.md](tells.md), [premium-markers.md](premium-markers.md), and [contexts.md](contexts.md) before the sweep.

### During-sweep checks

- [ ] **Cite-or-cut enforced:** Give every recorded tell an ID, a severity, and a concrete citation (hex value, font name, `file:line`, or screenshot region).
- [ ] **Premium pair checked:** Verify, before you record any tell, that it is not the crafted premium version of the pattern.
- [ ] **Portability test applied:** For borderline cases, ask: "Could this element be moved to another site without alteration?" If yes, record a tell. If no (it is specific to this brand), record no tell.
- [ ] **Defense test applied:** For borderline cases, ask: "Could the designer defend this choice with concrete reasoning if asked?" If no, record a tell. Slop cannot be defended. Deliberate choices can.
- [ ] **Section attribution:** Assign every tell to a specific section (Hero, Features, Pricing, Footer, etc.) for the Section Ledger.
- [ ] **Severity discipline:** Reserve critical for absolute-rule violations only. Never inflate severity.

### Exclusion checks

- [ ] **Exclusions documented:** Give every excluded tell one of the four tags: `// BRIEF:`, `// DESIGN DECISION:`, `// CONTEXT:`, or `// PREMIUM PAIR:`.
- [ ] **Exclusions are genuine:** Reject "we liked it" and "it looked good". Accept only explicit brief direction, documented design decisions with concrete reasoning, a tell in the context Tolerance table, or a premium pair with cited attributes.
- [ ] **Exclusion count reasonable:** Double-check each exclusion when more than 5 tells are excluded. Read mass exclusions as "the brief was not followed", not as "the tells do not apply".

### Post-sweep checks

- [ ] **All unverifiable checks marked:** Mark each one. Never pass or skip a check silently.
- [ ] **All 6 absolute rules reported:** Report pass/fail/unverifiable with evidence for each rule.
- [ ] **All 11 signature/cohesion items scored:** Score each item 0/50/100 with a one-line justification.
- [ ] **Section Ledger complete:** Give every major section a verdict (CLEAN/SUSPICIOUS/INFLATED/CRITICAL) with tell count and action.
- [ ] **Gates applied correctly:**
  - [ ] Signature gate: if Axis 7 < 40, cap overall at 59
  - [ ] Absolute-rule gate: if any crit, cap overall at 69
  - [ ] Compounding cap: if ≥3 major layout tells, cap Axis 4 at 40
- [ ] **Math from script only:** Run all scoring through [score.py](../scripts/score.py). Never compute by hand.

### Report checks

- [ ] **Template followed exactly:** Match the structure of [slop-report-template.md](slop-report-template.md).
- [ ] **Fixes ranked by weighted impact:** Rank fixes by weighted impact. Signature issues (3x weight) typically outrank single tells.
- [ ] **Language correct:** Write the report in the user's language. Keep tell IDs in English.

### Final self-audit

Ask these questions before you deliver:

- [ ] **"What still looks like obvious slop that I didn't flag?"** If something visually screams slop but is not in your findings, find the tell that covers it. Otherwise note it as a gap in the catalog.
- [ ] **"Did I over-correct?"** A sparse report on a clearly-slop design suggests missed tells. A bloated report on a premium design suggests false positives.
- [ ] **"Would I trust this report if someone else wrote it?"** Read the report as if you review a colleague's work. Check that every claim holds up.
