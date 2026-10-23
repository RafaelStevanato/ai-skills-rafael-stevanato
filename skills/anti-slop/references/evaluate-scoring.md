# EVALUATE Scoring

Run all EVALUATE arithmetic through [score.py](../scripts/score.py) (as `scripts/score.py`, from the anti-slop skill root). Never compute by hand.

## Axes and weights

Score all 8 axes with these weights.

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

Axis 7 is the heaviest. Never reward zero tells with no signature: apply the signature gate.

## Axes 1–6 (tell-counted)

Count confirmed tells on the axis by severity. Compute `score = max(0, 100 − 30·critical − 15·major − 5·minor)`.
Run `scripts/score.py axis CRIT MAJOR MINOR`.

- Count one tell once. A pattern repeated across sections is still one tell.
- Note the repetition in the evidence. Upgrade minor to major only where the catalog says so.
- Count each tell only on its one catalog axis.

## Axes 7–8 (0/50/100 mean)

- Score each of the 7 formula elements of Axis 7 as 0 (absent), 50 (attempted, weak), or 100 (strong). Use the rubric in [premium-markers.md](premium-markers.md). Set Axis 7 to the mean.
- Score each of the 4 cohesion checks of Axis 8 on the same scale. Set Axis 8 to the mean.

## Compounding rule

Cap Axis 4 at 40 when one page has 3 or more major layout tells (L group in [tells.md](tells.md)).
Run `scripts/score.py axis CRIT MAJOR MINOR --cap 40`. Apply the cap even when each block is clean.

## Gates

Pass each triggered gate as `--cap` to the overall run.
- **Signature gate:** Axis 7 < 40 caps the overall at 59 (grade C max). Pass `--cap 59`.
- **Absolute-rule gate:** any confirmed critical tell caps the overall at 69 (no grade A with broken execution). Pass `--cap 69`.

Apply every triggered cap. Never let clean spacing lift a page past a cap.

## Overall and Slop Index

Compute the overall with this block:

```
overall    = sum(axis_score × weight) / sum(weight)   # capped by gates
Slop Index = 100 − overall
```

Run `scripts/score.py overall 1:80:2 2:65:2 ... [--cap 59] [--cap 69]`.
- Write each axis argument as `axis:score:weight`.
- Score unverifiable axes `NA` (`7:NA:3`; `N/A` also works). NA drops the axis from both sums.
- Read overall, Slop Index, and grade from the output.
- Add `--fail-below N` to exit non-zero when overall < N (CI gate).

Example: gate a PR on its preview deploy.

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

Map the capped overall to one row. Copy this table into the Slop Report.

| Grade | Overall | Slop Index | Verdict |
|-------|---------|------------|---------|
| A | 80–100 | 0–20 | Premium — deliberate, signed, executed |
| B | 60–79 | 21–40 | Considered — mostly deliberate, some defaults |
| C | 40–59 | 41–60 | Generic — clean but templated or unsigned |
| D | 20–39 | 61–80 | Slop — assembled from presets |
| F | 0–19 | 81–100 | Pure slop |

## Absolute rules check

Check the six execution laws listed in [SKILL.md](../SKILL.md). Report each as pass, fail, or unverifiable, with evidence, in its own table.
Treat every **fail** as a critical tell: count it on its axis and trigger the absolute-rule gate.
Law-to-tell map: 1 = M1, 2 = X2 and X11, 3 = X3, 4 = X1, 5 = X5, 6 = M8.
