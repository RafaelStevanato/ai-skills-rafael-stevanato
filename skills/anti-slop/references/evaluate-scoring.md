# EVALUATE Scoring

Use this file for all EVALUATE arithmetic and grading.
Run the numbers with [score.py](../scripts/score.py). Never compute scores by hand.
Run `scripts/score.py` from the anti-slop skill root.
Load [evaluate-procedure.md](evaluate-procedure.md) for the workflow that produces the inputs.
Load [slop-report-template.md](slop-report-template.md) for the report structure.

## Axes and weights

Score all 8 axes. Apply the weight from the table.

| # | Axis | Weight | Scored from |
|---|------|--------|-------------|
| 1 | Color & Light | 2x | Tells C1–C15 |
| 2 | Typography & Copy | 2x | Tells T1–T10, W1–W3 |
| 3 | Components & Ornament | 1x | Tells K1–K27 |
| 4 | Layout & Composition | 2x | Tells L1–L21 |
| 5 | Motion & Interaction | 1x | Tells M1–M8 |
| 6 | Execution & Craft | 2x | Tells X1–X14 |
| 7 | Signature & Uniqueness | 3x | 7-element formula (positive rubric) |
| 8 | Cohesion | 2x | 4 checks (positive rubric) |

Weight Axis 7 at 3x. It is the heaviest axis.
Never reward a page that has zero tells and no signature. Apply the signature gate.

## Axes 1–6 (tell-counted)

Count confirmed tells on the axis by severity.
Compute the score with `score = max(0, 100 − 30·critical − 15·major − 5·minor)`.
Run `scripts/score.py axis CRIT MAJOR MINOR`. Do not compute by hand.
Count one tell once. A pattern repeated across sections is still one tell.
Note the repetition in the evidence.
Upgrade minor to major for repetition only where the catalog says so.
Count each tell on one axis only: the axis the catalog assigns.
Example: a cut-off glow could sit on color and on execution. Count it only on its catalog axis.
Reserve critical severity for the six absolute-rule failures. A blue-purple gradient is major, not critical.

## Axes 7–8 (0/50/100 mean)

Score each of the 7 formula elements of Axis 7 as 0 (absent), 50 (attempted, weak), or 100 (strong).
Apply the rubric in [premium-markers.md](premium-markers.md).
Set Axis 7 to the mean of the 7 element scores.
Score each of the 4 cohesion checks of Axis 8 with the same 0/50/100 scale.
Set Axis 8 to the mean of the 4 check scores.

## Compounding rule

Cap Axis 4 at 40 when one page has 3 or more major layout tells.
Count major tells from the L group in [tells.md](tells.md).
Run `scripts/score.py axis CRIT MAJOR MINOR --cap 40`.
Apply the cap even when each block is clean.

## Gates

Pass each triggered gate as `--cap` to the overall run.
- **Signature gate:** Axis 7 < 40 caps the overall at 59 (grade C max). Pass `--cap 59`.
- **Absolute-rule gate:** any confirmed critical tell caps the overall at 69 (no grade A with broken execution). Pass `--cap 69`.

Apply both caps when both gates trigger.
Apply the signature gate without exception.
Never let clean spacing or other axis scores lift a page past a gate cap.

## Overall and Slop Index

Compute the overall with this block:

```
overall    = sum(axis_score × weight) / sum(weight)   # capped by gates
Slop Index = 100 − overall
```

Run `scripts/score.py overall 1:80:2 2:65:2 ... [--cap 59] [--cap 69]`.
Write each axis argument as `axis:score:weight`.
Score unverifiable axes `NA`. Write them as `7:NA:3` (`N/A` also works).
Drop NA axes from both sums.
Apply caps to the weighted overall.
Read the overall, the Slop Index, and the grade from the score.py output.
Add `--fail-below N` to exit non-zero when overall < N. Use it for CI gating.
Example: gate a PR on its preview deploy. Export each axis score (A1 to A8) before the gate step.

```yaml
# .github/workflows/slop-gate.yml (step excerpt)
- name: Slop gate
  run: |
    # run anti-slop EVALUATE against $PREVIEW_URL, export each axis score, then:
    python3 skills/anti-slop/scripts/score.py overall \
      1:$A1:2 2:$A2:2 3:$A3:1 4:$A4:2 5:$A5:1 6:$A6:2 7:$A7:3 8:$A8:2 \
      --fail-below 40
```

## Grade scale

Map the capped overall to one row.
Copy this table into the Slop Report.

| Grade | Overall | Slop Index | Verdict |
|-------|---------|------------|---------|
| A | 80–100 | 0–20 | Premium — deliberate, signed, executed |
| B | 60–79 | 21–40 | Considered — mostly deliberate, some defaults |
| C | 40–59 | 41–60 | Generic — clean but templated or unsigned |
| D | 20–39 | 61–80 | Slop — assembled from presets |
| F | 0–19 | 81–100 | Pure slop |

## Absolute rules check

Check the six execution laws. The list lives in [SKILL.md](../SKILL.md).
Report each law as pass, fail, or unverifiable, with evidence.
Report the laws in their own table.
Treat every **fail** as a critical tell.
Count the fail on its axis.
Trigger the absolute-rule gate on every fail.
Use this law-to-tell map: 1 = M1, 2 = X2 and X11, 3 = X3, 4 = X1, 5 = X5, 6 = M8.
