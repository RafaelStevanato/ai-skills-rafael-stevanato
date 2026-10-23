---
name: motion-ad
description: >-
  Produce a 15-second motion-graphics video ad for Facebook, Instagram, TikTok, Reels or Meta as a rendered H.264 MP4. Matches every on-screen claim to the destination landing page, pulls real product imagery off the live site, fills one CONFIG object in a finished 4:5 GSAP template, and renders the paused timeline frame-accurately through Playwright and ffmpeg. Use when the user wants a video ad, promo video, animated ad, motion graphics, an ad for my product, Meta or TikTok or Reels creative in video form, a 9:16 stories or reels cut, a 1:1 square cut, a 2x master, or a re-render of an earlier ad with a different hook, hero, proof row or CTA, even if they never say motion graphics. Not for animating UI inside an app, static image ads, long-form video, or voiceover-led video.
license: CC-BY-NC-4.0
metadata:
  author: "danny.md (https://www.danny.md)"
  original_project: "https://www.danny.md/skills/motion-ad"
  license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
  version: "1.0"
  date: "2026-09-27"
  repository: "https://github.com/fabricioctelles/skills"
  category: "code-scaffolding-and-templates"
  attribution: "Original skill by danny.md (https://www.danny.md), published under CC BY-NC 4.0: free to use and remix, not to sell. This copy keeps the upstream workflow and adds repo-standard metadata, portable skill-path resolution, a preflight check, and references/template-map.md."
  modified: "2026-10-23: rewritten to ASD-STE100, merged into a 7-skill pack; scripts/ and assets/ unchanged. Changes: tap still 1.5s to 1.64s; node 18 to 20; added 2x html/body clipping check (not render-verified); template-map: Beat B 3.6 note, orbData wording, gallery minimum 12."
  requires: "node 20+, google-chrome or playwright chromium, ffmpeg, python3 + pillow"
  consolidated: "2026-10-23 ASD-STE100 rewrite"
  merged-from: "motion-ad"
---

> **⚠️ EXECUTION DIRECTIVE (INPUT vs. OUTPUT SEPARATION):**
> The rules in this skill use strict ASD-STE100 controlled language solely for zero-ambiguity parsing and token efficiency.
> - **NEVER copy this telegraphic or robotic style into human-facing outputs.**
> - Apply 80% ASD-STE100 in final outputs ONLY when explaining dense technical concepts.

# Motion Ad

## Scope

- Output one sound-off-friendly 15s H.264 MP4 ad.
- Build the ad as one HTML page driven by one paused GSAP timeline. Render every frame by seeking it. Never record playback.
- Use [assets/template.html](assets/template.html) as the base. It is a finished 15s 4:5 ad, not a blank scaffold.
- Keep all brand and product content in the `CONFIG` object at the top of the template script. Start from it. Rewrite the beats. Never build a timeline from zero.
- Read [references/template-map.md](references/template-map.md) before the first edit of `index.html`.

## Preflight

- Set `S` to the directory that contains this `SKILL.md` (the parent of `assets/` and `scripts/`). Default: `~/.claude/skills/motion-ad`. When unknown, run:

```bash
find ~ -maxdepth 7 -type d -name motion-ad -path '*skills*' 2>/dev/null | head
```

- Run this check once per session. It installs the two npm deps and downloads no browser (the scripts drive your Chrome).

```bash
S=~/.claude/skills/motion-ad
test -f $S/assets/template.html && test -f $S/scripts/render.cjs || echo "S is wrong"
node -v && ffmpeg -version | head -1 && python3 -c 'import PIL; print("pillow ok")'
(cd $S/scripts && npm install)
google-chrome --version || (cd $S/scripts && npx playwright install chromium && echo "use --channel chromium")
```

- Verify `node -v` prints v20 or higher (playwright-core 1.63 needs node >=20).
- Stop and report when `ffmpeg` is missing. Nothing downstream works without it.

**Done when:** node, ffmpeg, Pillow and Chrome (or the chromium fallback) each print a version.

## Non-negotiables

1. Make every on-screen claim exist on the page the ad links to.
   - Read that page before writing any headline (WebFetch, or the page source in the current repo).
   - Check prices, counts, speeds, guarantees and "free" claims against it.
   - Write the copy when the user asks for text that contradicts the page. Flag the mismatch once, clearly. Never ship it silently.
2. Use only real assets.
   - Use the user's own images, or images pulled from their live site with [scripts/fetch-images.cjs](scripts/fetch-images.cjs).
   - Never invent customers, reviews, ratings or results.
   - Set `proof: null` when no real number exists for the proof row. The row then disappears. Never show a placeholder claim.
3. Never fabricate a person. Crop or mirror real shots when a beat needs more shots of someone than exist. Tell the user.
4. Match the brand, not the template defaults.
   - Take colors (primary, accent, page), font, logo and tone of voice from the product.
   - Use no hype, no exclamation marks, and no emoji unless the brand uses them.

## Workflow

```
- [ ] Step 1: Research the product and the destination page
- [ ] Step 2: Set up the workdir and gather assets
- [ ] Step 3: Write the storyboard and copy
- [ ] Step 4: Fill CONFIG and edit the timeline
- [ ] Step 5: Render stills, review, fix
- [ ] Step 6: Render the full MP4, spot-check, deliver
```

### Step 1: Research

- Establish the product, destination URL, audience and format. Default to 4:5 feed. Use 9:16 for stories and reels. Use 1:1 for feed squares.
- Ask only for what you cannot infer. The destination URL is the one required input.
- WebFetch the destination page and the homepage or pricing page. Note the headline promise, prices, rating and review counts, speed claims, and free versus paid.
- Pull primary and accent colors, font family and logo from the site CSS or design system. Ask the user when the site does not show them.

**Done when:** you have the URL, the format, and a written list of claims, each traceable to a specific page.

### Step 2: Workdir and assets

- Work in a scratch directory. Never work inside the skill folder.
- Copy `assets/template.html` to `index.html`. Never edit the template in place.

```bash
S=~/.claude/skills/motion-ad             # wherever this skill is installed
W=<scratchpad>/video && mkdir -p $W/a && cd $W
cp $S/assets/template.html index.html
cp $S/scripts/node_modules/gsap/dist/gsap.min.js .
node $S/scripts/fetch-images.cjs --url <destination-url>   # -> a/web/NN.jpg + images.json
python3 $S/scripts/contact-sheet.py images a/web           # -> images.jpg
```

- Read `images.jpg` to pick assets. Ask the user for specific images. Prefer them over scraped images.
- Put the logo in `a/`: a light-background version, plus a white version for the end card when it exists.
- Choose the hero before/after pair with the clearest transformation. For a SaaS product, "messy input → finished output" screenshots often beat photos.
- Use portrait (≈4:5) images for the hero and showcase cards. Supply at least 12 distinct wall images.

**Done when:** `a/` holds the logo(s) and enough distinct images for the hero pair, the wall and three showcase cards. You have named each file you will reference in `CONFIG`.

### Step 3: Storyboard and copy

- Write 4 to 5 beats in 15 seconds, with one short headline each.
- Treat the windows below as nominal (storyboard). Use the exact windows in [Timeline map](references/template-map.md#timeline-map) for retiming.

| Time | Beat | CONFIG fields |
|---|---|---|
| 0–2.2s | Hook headline, phone scrolls a screen capture, finger taps the input | `hook`, `screen`, `screenScroll`, `tap` |
| 2.2–5.4s | Tapped card grows into the hero; scan beam reveals before → after; benefit pills | `reveal`, `before`, `after`, `beforeLabel`, `afterLabel`, `benefits` |
| 5.5–8.7s | Hero shrinks into a tilted 3D wall of outputs | `scale`, `scaleChip`, `gallery` |
| 8.7–11.8s | Showcase carousel (3 cards, optional "before" inset) + proof row | `proofHl`, `showcase`, `showChip`, `proof` |
| 11.8–15s | Brand-color circle wipe → logo, CTA headline, chip, button tap | `cta.headline`, `cta.chip`, `cta.button`, `cta.foot` |

- Limit each headline line to about 20 characters at 82px inside a 960px box. Use `\n` to set the breaks.
- Lines wrap at spaces and grow *downward* from a fixed `top`. An over-budget headline collides with the element below it. It does not shrink.
- Change or cut a beat that does not fit the product, in the timeline. Never force it. Open a desktop-only tool on the hero card, not the phone.
- Treat 1:1 as the tight format: the phone is 520×1100 and does not fit a square frame. 4:5 and 9:16 fit.
- Tell the user about the 1:1 limit when they ask for square. Let them choose between rescaling the phone and replacing the hook beat. Do not only re-space. See [Re-lay out for 1:1](references/template-map.md#re-lay-out-for-11).

**Done when:** every beat has final copy, and every claim traces to a page you read in Step 1.

### Step 4: Fill CONFIG and edit the timeline

- Set `brand`, `logo`, `logoOnDark` and `colors`.
- Change both the Google Fonts `<link>` family and the `--font` variable to the brand font. See [Swap the font](references/template-map.md#swap-the-font).
- Mark the accent color in headlines with `*word*` or `*several words*`. Force a break with `\n`.
- Write image paths relative to `index.html` (e.g. `a/web/03.jpg`). Crop or mirror with PIL when an image needs different framing.
- Set `tap` so the finger lands on the relevant spot of `screen` *after* it has scrolled by `screenScroll`. The two values are one gesture.
- Keep `window.seek`, `window.DURATION`, `window.ready` and the `?render` autoplay guard intact. `render.cjs` depends on all four. See [Render contract](references/template-map.md#render-contract).
- For 9:16 or 1:1, change `html,body,#stage` to the new size, re-space the vertical positions, and render with the matching `--size`. See [Re-lay out for 9:16](references/template-map.md#re-lay-out-for-916).

**Done when:** `node $S/scripts/render.cjs --stills 0.3` produces a frame with real copy, real images and the brand's colors, with no leftover `Acme` and no `Benefit one`.

Replace every other template default in `CONFIG`. For the made-up proof text `**4.8** · 1,000 reviews`, set a real value or `proof: null`.

### Step 5: Stills review

```bash
node $S/scripts/render.cjs --stills 0.3,1.9,2.7,3.8,4.9,6.6,9.8,11.5,13.6
python3 $S/scripts/contact-sheet.py stills
```

- Read `stills.jpg`. Check for: leftover placeholders, text overlapping the end-card orbs, empty gaps, labels that contradict the image beside them, and the same image repeated side by side in the wall.
- Check legibility at thumbnail size in the contact sheet. The ad is seen at that size: muted, on a phone.

**Done when:** every still shows the intended content, nothing overlaps, and each headline is readable in the contact sheet thumbnail.

### Step 6: Full render and deliver

```bash
node $S/scripts/render.cjs --out ad-4x5.mp4          # ~1 min for 450 frames
ffprobe -v error -show_entries format=duration:stream=width,height,nb_frames -of csv=p=0 ad-4x5.mp4
mkdir -p ~/Downloads && mv ad-4x5.mp4 ~/Downloads/<brand>-<topic>-ad-4x5-vN.mp4
```

- Spot-check the circle wipe and the carousel slides: a still can hide a bad ease. Extract a frame with `ffmpeg -ss <t> -i <mp4> -frames:v 1 f.png`.
- Confirm `duration` and `nb_frames` in the `ffprobe` output match the expected values. A frozen tail means the timeline is shorter than `DURATION`.
- Never overwrite an earlier version. Bump `vN`.
- Report the file path, the beat-by-beat copy, and every caveat: low-resolution sources, crops and mirrors, any placeholder you left in, any copy that differs from the landing page.

**Done when:** the MP4 is in `~/Downloads/` under a versioned name, `ffprobe` reports the expected duration and frame count, and the caveats are in your message.

## Iterating on an earlier ad

- Keep the workdir. Treat a revision as a `CONFIG` edit plus a re-render. Never rebuild.
- Swap the hero pair or the hook, or change `cta.button` or `proof.text`. Re-run Step 5 and Step 6. Deliver as `vN+1`.
- Copy the workdir for a different aspect ratio. The 4:5 and 9:16 spots then keep their own `CONFIG`.

## Gotchas

- **Absolute timeline.** Every `tl.*()` call passes a hard-coded second. After you remove the phone beat, the next beat still starts at 2.55s. The video holds a still frame.
  - Re-time every later `at` value. Set `window.DURATION` to the new length. Move the loop guard `tl.to({}, { duration: 0.01 }, 15)` with it. See [Cut a beat](references/template-map.md#cut-a-beat).
- **Wrong image path.** `setImg` swaps in a labelled SVG on `onerror`. A typo, a wrong case or a missing file gives a valid MP4 full of gradient placeholders.
  - Check the contact sheet every time. Prefer the `images.json` filenames over guessing.
- **Fewer than ~12 gallery images.** The wall repeats visibly. Accept repetition only as a deliberate choice.
- **2× master.** `--size` alone fails: the CSS is fixed at 1080×1350 and `render.cjs` uses `deviceScaleFactor: 1`. Scale `#stage` with `transform: scale(2)` and render at `2160x2700`. See [2× master](references/template-map.md#2-master) for the CSS and the `html, body` clipping check.
- **Too-long headline.** An extra line pushes into the phone (top 392), the carousel, or the end-card stack. The overflow shows only on stills you render.
  - Trim the copy. Never shrink the font below ~64px.
- **Tap on empty white.** `screenScroll` can move the target away from the fixed `tap` point.
  - Render the 1.64s still. Check that the dot sits on something meaningful. A still at 1.5s shows neither dot nor ring.
- **`zsh` unmatched glob.** `rm still-*.jpg` in a clean workdir kills the whole command with `no matches found`. Use `find . -maxdepth 1 -name 'still-*.jpg' -delete`.
- **`npm install` inside `scripts/` creates `node_modules/`.** Keep it in the skill's `scripts/` folder. It is gitignored.
  - Never copy the scripts into the workdir. They resolve their own dependencies and fail there with `Cannot find module 'playwright-core'`.
- **Site-hosted images are often small.** Tell the user when a hero or carousel card looks soft. Offer to drop higher-resolution originals into `a/` under the same filenames. Never re-render at a size the source cannot support.
- **No Google Chrome.** `render.cjs` and `fetch-images.cjs` default to `channel: 'chrome'`. Run `npx playwright install chromium` in `scripts/` once. Pass `--channel chromium` to both.

## Reference files

- [references/template-map.md](references/template-map.md): load before the first edit of `index.html`, and for any recipe (cut or add a beat, 9:16, 1:1, 2× master, font, end-card logo, proof row).
- [assets/template.html](assets/template.html): load at Step 2. Copy it to `index.html`. Never edit it in place.
- [scripts/render.cjs](scripts/render.cjs): load at Step 5 and Step 6. It seeks the paused timeline per frame and pipes PNGs to ffmpeg. Flags: `--stills`, `--out`, `--size`, `--fps`, `--page`, `--channel`.
- [scripts/fetch-images.cjs](scripts/fetch-images.cjs): load at Step 2. It scrolls the destination page and downloads its real imagery. Flags: `--url`, `--out`, `--min`, `--limit`, `--channel`.
- [scripts/contact-sheet.py](scripts/contact-sheet.py): load at Step 2 and Step 5. It tiles images or stills into one labelled JPG.

## Attribution and license

- Created by [danny.md](https://www.danny.md/skills/motion-ad). Published under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/): free to use and remix, not to sell.
- Redistributed via github.com/fabricioctelles/skills. Modifications: see `metadata.modified`.
