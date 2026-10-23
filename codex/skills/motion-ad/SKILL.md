---
name: motion-ad
description: Produce a 15-second, sound-off motion-graphics video ad (H.264 MP4) for Meta, Instagram, TikTok or Reels from a product's landing page, using the bundled GSAP template and a frame-accurate Playwright + ffmpeg render; also re-renders earlier ads and 9:16, 1:1 or 2x cuts. Not for in-app UI animation, static image ads, long-form or voiceover video.
license: CC-BY-NC-4.0
metadata:
  author: "danny.md (https://www.danny.md)"
  original-project: "https://www.danny.md/skills/motion-ad"
  license-url: "https://creativecommons.org/licenses/by-nc/4.0/"
  version: "1.0-codex"
  requires: "node 20+, google-chrome or playwright chromium, ffmpeg, python3 + pillow"
  modified: "Codex port: tool-neutral page reading, skill-dir resolution for Codex, outcome-first steps; scripts/ and assets/ unchanged"
---

# Motion Ad

Deliver one sound-off-friendly 15-second H.264 MP4 ad. The ad is one HTML page driven by one paused GSAP timeline, and every frame is rendered by seeking that timeline, never by recording playback. [assets/template.html](assets/template.html) is a finished 4:5 ad, not a blank scaffold: keep all brand and product content in its `CONFIG` object, rewrite the beats, and never build a timeline from zero. Read [references/template-map.md](references/template-map.md) before the first edit of `index.html`, and again for any recipe (cut or add a beat, 9:16, 1:1, 2x master, font, end-card logo, proof row).

The task is done when the MP4 is in `~/Downloads/` under a versioned name, `ffprobe` reports the expected duration and frame count, every on-screen claim traces to the landing page, and your message lists the caveats.

The user's explicit instructions take precedence over this skill. The skill text is compact controlled English for precise reading; write ad copy and messages in natural language that fits the brand.

## Non-negotiables

1. Every on-screen claim exists on the page the ad links to. Read that page (web fetch, browser, or the page source in the repo) before writing headlines, and check prices, counts, speeds, guarantees and "free" claims against it. If the user asks for copy that contradicts the page, write it, flag the mismatch once and clearly, and never ship it silently.
2. Only real assets: the user's images or images pulled from their live site with [scripts/fetch-images.cjs](scripts/fetch-images.cjs). Never invent customers, reviews, ratings or results. With no real number for the proof row, set `proof: null` so the row disappears.
3. Never fabricate a person. When a beat needs more shots of someone than exist, crop or mirror real shots and tell the user.
4. Match the brand, not the template defaults: colors (primary, accent, page), font, logo and tone come from the product. No hype, exclamation marks or emoji unless the brand uses them.

## Setup

Set `S` to this skill's folder, the one that contains this `SKILL.md` (Codex shows its path in the skill list; usually `~/.agents/skills/motion-ad` or `~/.codex/skills/motion-ad`). Run the preflight once per session. It installs two npm dependencies in `scripts/` and downloads no browser, because the scripts drive the installed Chrome.

```bash
test -f $S/assets/template.html && test -f $S/scripts/render.cjs || echo "S is wrong"
node -v && ffmpeg -version | head -1 && python3 -c 'import PIL; print("pillow ok")'
(cd $S/scripts && npm install)
google-chrome --version || (cd $S/scripts && npx playwright install chromium && echo "use --channel chromium")
```

Node must be v20 or higher (playwright-core 1.63). Stop and report if `ffmpeg` is missing, since nothing downstream works without it. Setup is done when node, ffmpeg, Pillow and Chrome (or the chromium fallback) each print a version.

## Workflow

### 1. Research

Establish the product, destination URL, audience and format: 4:5 feed by default, 9:16 for stories and reels, 1:1 for feed squares. The destination URL is the one required input; infer the rest when you can. Read the destination page plus the homepage or pricing page and note the headline promise, prices, rating and review counts, speed claims, and what is free versus paid. Take primary and accent colors, font family and logo from the site's CSS or design system, and ask only if the site does not show them.

Done when you have the URL, the format, and a written list of claims, each traceable to a specific page.

### 2. Workdir and assets

Work in a scratch directory, never inside the skill folder, and never edit the template in place.

```bash
W=<scratch>/video && mkdir -p $W/a && cd $W
cp $S/assets/template.html index.html
cp $S/scripts/node_modules/gsap/dist/gsap.min.js .
node $S/scripts/fetch-images.cjs --url <destination-url>   # -> a/web/NN.jpg + images.json
python3 $S/scripts/contact-sheet.py images a/web           # -> images.jpg
```

View `images.jpg` to pick assets, and prefer images the user supplies over scraped ones. Put the logo in `a/`: a light-background version, plus a white version for the end card when it exists. For the hero before/after pair, choose the clearest transformation; for SaaS, "messy input → finished output" screenshots often beat photos. Use portrait (about 4:5) images for the hero and showcase cards and supply at least 12 distinct wall images.

Done when `a/` holds the logo(s) and enough distinct images for the hero pair, the wall and three showcase cards, and you have named each file you will reference in `CONFIG`.

### 3. Storyboard and copy

Write 4 to 5 beats in 15 seconds with one short headline each. These windows are nominal; use the exact ones in [Timeline map](references/template-map.md#timeline-map) when retiming.

| Time | Beat | CONFIG fields |
|---|---|---|
| 0–2.2s | Hook headline, phone scrolls a screen capture, finger taps the input | `hook`, `screen`, `screenScroll`, `tap` |
| 2.2–5.4s | Tapped card grows into the hero; scan beam reveals before → after; benefit pills | `reveal`, `before`, `after`, `beforeLabel`, `afterLabel`, `benefits` |
| 5.5–8.7s | Hero shrinks into a tilted 3D wall of outputs | `scale`, `scaleChip`, `gallery` |
| 8.7–11.8s | Showcase carousel (3 cards, optional "before" inset) + proof row | `proofHl`, `showcase`, `showChip`, `proof` |
| 11.8–15s | Brand-color circle wipe → logo, CTA headline, chip, button tap | `cta.headline`, `cta.chip`, `cta.button`, `cta.foot` |

Keep each headline line to about 20 characters at 82px in a 960px box, and set breaks with `\n`. Lines wrap at spaces and grow downward from a fixed `top`, so an over-budget headline collides with the element below instead of shrinking. Change or cut a beat that does not fit the product rather than forcing it; open a desktop-only tool on the hero card, not the phone. 1:1 is the tight format: the 520×1100 phone does not fit a square frame (4:5 and 9:16 fit). When the user asks for square, tell them and let them choose between rescaling the phone and replacing the hook beat ([Re-lay out for 1:1](references/template-map.md#re-lay-out-for-11)).

Done when every beat has final copy and every claim traces to a page you read in step 1.

### 4. Fill CONFIG and edit the timeline

- Set `brand`, `logo`, `logoOnDark` and `colors`. Change both the Google Fonts `<link>` family and the `--font` variable ([Swap the font](references/template-map.md#swap-the-font)).
- Mark accent words in headlines with `*word*` or `*several words*`; force a break with `\n`.
- Write image paths relative to `index.html` (for example `a/web/03.jpg`). Crop or mirror with PIL when an image needs different framing.
- Set `tap` so the finger lands on the relevant spot of `screen` after it has scrolled by `screenScroll`; the two values are one gesture.
- Keep `window.seek`, `window.DURATION`, `window.ready` and the `?render` autoplay guard intact, because `render.cjs` depends on all four ([Render contract](references/template-map.md#render-contract)).
- For 9:16 or 1:1, change `html,body,#stage` to the new size, re-space vertical positions, and render with the matching `--size` ([Re-lay out for 9:16](references/template-map.md#re-lay-out-for-916)).
- Replace every other template default in `CONFIG`. For the made-up proof text `**4.8** · 1,000 reviews`, set a real value or `proof: null`.

Done when `node $S/scripts/render.cjs --stills 0.3` produces a frame with real copy, real images and the brand colors, with no leftover `Acme` or `Benefit one`.

### 5. Stills review

```bash
node $S/scripts/render.cjs --stills 0.3,1.9,2.7,3.8,4.9,6.6,9.8,11.5,13.6
python3 $S/scripts/contact-sheet.py stills
```

View `stills.jpg` and look for leftover placeholders, text overlapping the end-card orbs, empty gaps, labels that contradict the image beside them, and the same image repeated side by side in the wall. Judge legibility at thumbnail size, because that is how the ad is seen: muted, on a phone.

Done when every still shows the intended content, nothing overlaps, and each headline reads in the contact-sheet thumbnail.

### 6. Full render and delivery

```bash
node $S/scripts/render.cjs --out ad-4x5.mp4          # ~1 min for 450 frames
ffprobe -v error -show_entries format=duration:stream=width,height,nb_frames -of csv=p=0 ad-4x5.mp4
mkdir -p ~/Downloads && mv ad-4x5.mp4 ~/Downloads/<brand>-<topic>-ad-4x5-vN.mp4
```

Spot-check the circle wipe and the carousel slides, since a still can hide a bad ease: extract a frame with `ffmpeg -ss <t> -i <mp4> -frames:v 1 f.png`. Confirm that `duration` and `nb_frames` match the expected values; a frozen tail means the timeline is shorter than `DURATION`. Never overwrite an earlier version; bump `vN`. Report the file path, the beat-by-beat copy, and every caveat: low-resolution sources, crops and mirrors, any placeholder left in, any copy that differs from the landing page.

## Revisions

Keep the workdir. A revision is a `CONFIG` edit plus a re-render, never a rebuild: swap the hero pair or hook, or change `cta.button` or `proof.text`, then repeat steps 5 and 6 and deliver as `vN+1`. For another aspect ratio, copy the workdir so 4:5 and 9:16 keep their own `CONFIG`.

## Gotchas

- Absolute timeline: every `tl.*()` call passes a hard-coded second. After you remove the phone beat, the next beat still starts at 2.55s and the video holds a still frame. Re-time every later `at`, set `window.DURATION` to the new length, and move the loop guard `tl.to({}, { duration: 0.01 }, 15)` with it ([Cut a beat](references/template-map.md#cut-a-beat)).
- Wrong image path: `setImg` swaps in a labelled SVG on `onerror`, so a typo, wrong case or missing file yields a valid MP4 full of gradient placeholders. Check the contact sheet every time and prefer the `images.json` filenames over guessing.
- Fewer than about 12 gallery images make the wall repeat visibly; accept that only as a deliberate choice.
- 2x master: `--size` alone fails because the CSS is fixed at 1080×1350 and `render.cjs` uses `deviceScaleFactor: 1`. Scale `#stage` with `transform: scale(2)` and render at `2160x2700` ([2× master](references/template-map.md#2-master), including the `html, body` clipping check).
- Too-long headline: an extra line pushes into the phone (top 392), the carousel or the end-card stack, and shows only on rendered stills. Trim the copy; never shrink the font below about 64px.
- Tap on empty white: `screenScroll` can move the target away from the fixed `tap` point. Render the 1.64s still and check that the dot sits on something meaningful (a 1.5s still shows neither dot nor ring).
- `zsh` unmatched glob: `rm still-*.jpg` in a clean workdir aborts with `no matches found`; use `find . -maxdepth 1 -name 'still-*.jpg' -delete`.
- `npm install` creates `node_modules/` inside the skill's `scripts/` (gitignored). Never copy the scripts into the workdir: they resolve their own dependencies and fail there with `Cannot find module 'playwright-core'`.
- Site-hosted images are often small. Tell the user when a hero or carousel card looks soft and offer to drop higher-resolution originals into `a/` under the same filenames; never render at a size the source cannot support.
- No Google Chrome: `render.cjs` and `fetch-images.cjs` default to `channel: 'chrome'`. Run `npx playwright install chromium` in `scripts/` once and pass `--channel chromium` to both.

## Script flags

- `scripts/render.cjs`: seeks the paused timeline per frame and pipes PNGs to ffmpeg. Flags `--stills`, `--out`, `--size`, `--fps`, `--page`, `--channel`.
- `scripts/fetch-images.cjs`: scrolls the destination page and downloads its real imagery. Flags `--url`, `--out`, `--min`, `--limit`, `--channel`.
- `scripts/contact-sheet.py`: tiles images or stills into one labelled JPG.

## Attribution and license

Created by [danny.md](https://www.danny.md/skills/motion-ad) and published under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/): free to use and remix, not to sell. Redistributed via github.com/fabricioctelles/skills; modifications are listed in `metadata.modified`.
