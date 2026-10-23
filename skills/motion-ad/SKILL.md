---
name: motion-ad
description: >-
  Produce a 15-second motion-graphics video ad for Facebook, Instagram, TikTok, Reels or Meta as a rendered H.264 MP4. Researches the destination landing page so every on-screen claim matches it, pulls real product imagery off the live site, fills one CONFIG object in a finished 4:5 GSAP template, and renders the paused timeline frame-accurately through Playwright and ffmpeg. Use when the user wants a video ad, promo video, animated ad, motion graphics, an ad for my product, Meta or TikTok or Reels creative in video form, a 9:16 stories or reels cut, a 1:1 square cut, a 2x master, or a re-render of an earlier ad with a different hook, hero, proof row or CTA, even if they never say motion graphics. Not for animating UI inside an app, static image ads, long-form video, or voiceover-led video.
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
  modified: "2026-10-23: SKILL.md and references/template-map.md rewritten to ASD-STE100 controlled language and consolidated into a 7-skill pack; scripts/ and assets/ unchanged. Corrections: tap still 1.5s changed to 1.64s; node requirement 18 changed to 20; added 2x html/body clipping check (not render-verified); template-map: added Beat B 3.6 call-site note, reworded orbData placement, set gallery minimum to 12."
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
- Build the ad as one HTML page driven by one paused GSAP timeline.
- Render every frame by seeking the timeline.
- Never record playback. Seeking gives deterministic output and identical re-renders.
- Use [assets/template.html](assets/template.html) as the base.
- Treat the template as a finished 15s 4:5 ad, not a blank scaffold.
- Template beats: hook + phone → before/after scan reveal → 3D wall of outputs → showcase carousel + social proof → brand-color CTA end card.
- Keep all brand and product content in the `CONFIG` object at the top of the template script.
- Start from `CONFIG`. Rewrite the beats. Never build a timeline from zero.
- Read [references/template-map.md](references/template-map.md) before the first edit of `index.html`.
- Do not use this skill for in-app UI animation, static image ads, long-form video, or voiceover-led video.

## Preflight

- Set `S` to the directory that contains this `SKILL.md` (the parent of `assets/` and `scripts/`).
- Use `~/.claude/skills/motion-ad` as the default install path.
- Run the find command when the path is unknown.

```bash
find ~ -maxdepth 7 -type d -name motion-ad -path '*skills*' 2>/dev/null | head
```

- Run the toolchain check once per session.
- Install the two npm deps with the same block.
- Expect no browser download. The scripts drive the Chrome you already have.

```bash
S=~/.claude/skills/motion-ad
test -f $S/assets/template.html && test -f $S/scripts/render.cjs || echo "S is wrong"
node -v && ffmpeg -version | head -1 && python3 -c 'import PIL; print("pillow ok")'
(cd $S/scripts && npm install)
google-chrome --version || (cd $S/scripts && npx playwright install chromium && echo "use --channel chromium")
```

- Verify `node -v` prints v20 or higher (playwright-core 1.63 needs node >=20).

**Done when:**
- The toolchain line prints a version for node, ffmpeg and Pillow.
- `google-chrome --version` (or the chromium fallback) prints a version.

Stop and report when `ffmpeg` is missing. Nothing downstream works without it.

## Non-negotiables

1. Make every on-screen claim exist on the page the ad links to.
   - Check prices, counts, speeds, guarantees and "free" claims against that page.
   - Read the destination page before writing any headline.
   - Use WebFetch, or read the page source when it lives in the current repo.
   - Write the copy when the user asks for text that contradicts the page.
   - Flag the mismatch once, clearly. Never ship it silently.
2. Use only real assets.
   - Use the user's own images, or images pulled from their live site with [scripts/fetch-images.cjs](scripts/fetch-images.cjs).
   - Never invent customers, reviews, ratings or results.
   - Set `proof: null` when no real number exists for the proof row. The row then disappears.
   - Never show a placeholder claim in the proof row.
3. Never fabricate a person.
   - Crop or mirror real shots when a beat needs more shots of someone than exist.
   - Tell the user about every crop or mirror.
4. Match the brand, not the template defaults.
   - Take primary color, accent color, page color, font, logo and tone of voice from the product.
   - Use no hype.
   - Use no exclamation marks.
   - Use no emoji unless the brand itself uses them.

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

- Establish the product, the destination URL, the audience and the format.
- Set the format to 4:5 feed by default.
- Use 9:16 for stories and reels. Use 1:1 for feed squares.
- Ask only for what you cannot infer.
- Ask for the destination URL when it is missing. It is the one required input.
- WebFetch the destination page.
- WebFetch the homepage or the pricing page for current facts.
- Extract the headline promise, prices, rating and review counts, speed claims, and what is free versus paid.
- Pull the brand from the site CSS or design system: primary and accent colors, font family, logo.
- Ask the user when the site does not show the brand values.

**Done when:**
- You have the URL.
- You have the format.
- You have a written list of claims, each traceable to a specific page.

### Step 2: Workdir and assets

- Work in a scratch directory.
- Never work inside the skill folder.
- Keep the skill folder free of edited files and downloaded images.
- Never edit `assets/template.html` in place. Copy it to `index.html`.

```bash
S=~/.claude/skills/motion-ad             # wherever this skill is installed
W=<scratchpad>/video && mkdir -p $W/a && cd $W
cp $S/assets/template.html index.html
cp $S/scripts/node_modules/gsap/dist/gsap.min.js .
node $S/scripts/fetch-images.cjs --url <destination-url>   # -> a/web/NN.jpg + images.json
python3 $S/scripts/contact-sheet.py images a/web           # -> images.jpg
```

- Run the Preflight `npm install` first. `gsap.min.js` exists only after that step.
- Read `images.jpg` to pick assets.
- Put the logo in `a/`.
- Use a light-background version of the logo.
- Add a white version of the logo for the end card when it exists.
- Choose the hero before/after pair with the clearest transformation.
- For a SaaS product, use "messy input → finished output" screenshots instead of photos when they show the clearest transformation.
- Use portrait (≈4:5) images for the hero and showcase cards.
- Supply at least 12 distinct wall images.
- Ask the user for specific images.
- Prefer the user's images over scraped images.

**Done when:**
- `a/` holds the logo(s).
- `a/` holds enough distinct images for the hero pair, the wall and three showcase cards.
- You have named each file you will reference in `CONFIG`.

### Step 3: Storyboard and copy

- Write 4 to 5 beats in 15 seconds.
- Write one short headline for each beat.
- Use the beat map below. It lists the nominal (storyboard) windows and the `CONFIG` fields that drive each beat.
- Use the exact call-site windows in [Timeline map](references/template-map.md#timeline-map) for retiming.

| Time | Beat | CONFIG fields |
|---|---|---|
| 0–2.2s | Hook headline, phone scrolls a screen capture, finger taps the input | `hook`, `screen`, `screenScroll`, `tap` |
| 2.2–5.4s | Tapped card grows into the hero; scan beam reveals before → after; benefit pills | `reveal`, `before`, `after`, `beforeLabel`, `afterLabel`, `benefits` |
| 5.5–8.7s | Hero shrinks into a tilted 3D wall of outputs | `scale`, `scaleChip`, `gallery` |
| 8.7–11.8s | Showcase carousel (3 cards, optional "before" inset) + proof row | `proofHl`, `showcase`, `showChip`, `proof` |
| 11.8–15s | Brand-color circle wipe → logo, CTA headline, chip, button tap | `cta.headline`, `cta.chip`, `cta.button`, `cta.foot` |

- Limit each headline line to about 20 characters at 82px inside a 960px box.
- Expect lines to wrap at spaces.
- Expect each extra line to grow *downward* from a fixed `top`.
- Expect an over-budget headline to collide with the element below it. It does not shrink.
- Use `\n` to set where the breaks land.
- Change or cut a beat that does not fit the product. Make the change in the timeline.
- Do not force a beat that does not fit.
- Open a desktop-only tool on the hero card. Do not use the phone.
- Expect the template content to fit 4:5 and 9:16 frames. 9:16 needs the resize and re-spacing in Step 4.
- Treat 1:1 as the tight format. The phone is 520×1100 and does not fit a square frame.
- Rescale the phone, or replace the hook beat, for 1:1. Do not only re-space.
- See [Re-lay out for 1:1](references/template-map.md#re-lay-out-for-11).
- Tell the user about the 1:1 limit when they ask for square.
- Let the user choose between a rescale and a different opening beat.

**Done when:**
- Every beat has final copy.
- Every claim traces to a page you read in Step 1.

### Step 4: Fill CONFIG and edit the timeline

- Set `brand`, `logo`, `logoOnDark` and `colors`.
- Change both the Google Fonts `<link>` family and the `--font` variable to the brand font. See [Swap the font](references/template-map.md#swap-the-font).
- In headlines, mark the accent color with `*word*` or `*several words*`.
- In headlines, force a break with `\n`.
- Write image paths relative to `index.html` (e.g. `a/web/03.jpg`).
- Crop or mirror with PIL when an image needs different framing.
- Set `tap` so the finger lands on the relevant spot of `screen` *after* it has scrolled by `screenScroll`.
- Treat the tap point and the scroll offset as two halves of one gesture.
- Keep `window.seek`, `window.DURATION`, `window.ready` and the `?render` autoplay guard intact.
- See [Render contract](references/template-map.md#render-contract). `render.cjs` depends on all four.
- For 9:16 or 1:1, change `html,body,#stage` to the new size.
- For 9:16 or 1:1, re-space the vertical positions.
- For 9:16 or 1:1, render with the matching `--size`.
- See [Re-lay out for 9:16](references/template-map.md#re-lay-out-for-916) for every constant that must move.

**Done when:**
- `node $S/scripts/render.cjs --stills 0.3` produces a frame with real copy, real images and the brand's colors.
- The frame shows no leftover `Acme`.
- The frame shows no `Benefit one`.

Check that none of these template defaults remain in `CONFIG`:
- `Acme`
- `Benefit one`, `Benefit two`, `Benefit three`
- `**4.8** · 1,000 reviews` (a made-up claim: replace it or set `proof: null`)
- `yourdomain.com`
- `Supporting line for the wall`
- `Real customers, real results`
- `No credit card needed`
- `Start with *one photo.*`
- `Get the *result.*`
- `At *any scale.*`
- `Real *results.*`
- `Try it\n*today.*`
- `Get started`

### Step 5: Stills review

```bash
node $S/scripts/render.cjs --stills 0.3,1.9,2.7,3.8,4.9,6.6,9.8,11.5,13.6
python3 $S/scripts/contact-sheet.py stills
```

- Read `stills.jpg`.
- Expect a wrong image path to fail silently. It becomes a labelled placeholder.
- Check for leftover placeholders.
- Check for text overlapping the end-card orbs.
- Check for empty gaps.
- Check for labels that contradict the image beside them.
- Check for the same image repeated side by side in the wall.
- Check legibility at thumbnail size in the contact sheet.
- Judge legibility at the size where the ad is actually seen: muted, on a phone.

**Done when:**
- Every still shows the intended content.
- Nothing overlaps.
- Each headline is readable in the contact sheet thumbnail.

### Step 6: Full render and deliver

```bash
node $S/scripts/render.cjs --out ad-4x5.mp4          # ~1 min for 450 frames
ffprobe -v error -show_entries format=duration:stream=width,height,nb_frames -of csv=p=0 ad-4x5.mp4
mkdir -p ~/Downloads && mv ad-4x5.mp4 ~/Downloads/<brand>-<topic>-ad-4x5-vN.mp4
```

- Spot-check the circle wipe and the carousel slides. Stills can hide a bad ease on these fast moves.
- Extract a frame with `ffmpeg -ss <t> -i <mp4> -frames:v 1 f.png`.
- Confirm `duration` and `nb_frames` in the `ffprobe` output match the expected values.
- Treat a frozen tail as a timeline shorter than `DURATION`.
- Never overwrite an earlier version. Bump `vN`.
- Report the file path.
- Report the beat-by-beat copy.
- Report every caveat:
  - low-resolution sources
  - crops and mirrors
  - any placeholder you left in
  - any copy that differs from the landing page

**Done when:**
- The MP4 is in `~/Downloads/` under a versioned name.
- `ffprobe` reports the expected duration and frame count.
- The caveats are in your message.

## Iterating on an earlier ad

- Keep the workdir.
- Treat a revision as a `CONFIG` edit plus a re-render. Never rebuild.
- Swap the hero pair or the hook, or change `cta.button` or `proof.text`.
- Re-run Step 5 and Step 6.
- Deliver as `vN+1`.
- Copy the workdir for a different aspect ratio. The 4:5 and 9:16 spots keep their own `CONFIG`.

## Gotchas

**1. The timeline is absolute, so cutting a beat leaves a frozen gap.**
- Expect every `tl.*()` call to pass a hard-coded second.
- Example: after you remove the phone beat, the next beat still starts at 2.55s. The video holds a still frame until then.
- Re-time every later `at` value.
- Update `window.DURATION` to the new length. It is the single source of truth for the frame count.
- Move the loop guard `tl.to({}, { duration: 0.01 }, 15)` with it.
- See [Cut a beat](references/template-map.md#cut-a-beat).

**2. A wrong image path renders a placeholder, not an error.**
- Expect `setImg` to swap in a labelled SVG on `onerror`.
- A typo, a wrong case, or a file you never downloaded gives a valid MP4 full of gradient placeholders.
- Check the contact sheet every time.
- Prefer the `images.json` filenames over guessing.

**3. Fewer than ~12 gallery images makes the wall repeat visibly.**
- Expect the 7×7 grid to pick cells with a modulo over `gallery`. Neighbouring tiles then land on the same image.
- Supply at least 12 distinct outputs.
- Accept the repetition only as a deliberate choice.

**4. You cannot render 2× by changing `--size` alone.**
- Expect the CSS to be fixed at 1080×1350.
- Expect `render.cjs` to use `deviceScaleFactor: 1`.
- Expect a larger viewport to render a smaller ad in a larger frame.
- For a 2× master, scale `#stage` with `transform: scale(2); transform-origin: top left`.
- Keep the viewport at `2160x2700`.
- See [2× master](references/template-map.md#2-master).
- Re-check the stills after scaling. Text scales too and can overflow.
- Set `html, body` to 2160×2700 before a 2× render. Verify on a still.
- Note: this check is not render-tested. The template sets `html,body` to 1080px × 1350px with `overflow:hidden`. A `scale(2)` stage can clip to the top-left quarter.

**5. A too-long headline does not shrink, it collides.**
- Expect each headline to sit at a fixed `top` and wrap downward.
- Expect an extra line to push into the phone (top 392), the carousel, or the end-card stack.
- Render a still for every headline beat. The overflow shows only on stills you render.
- Trim the copy.
- Never shrink the font below ~64px. Muted-feed legibility is the point of the format.

**6. The finger tap and the screen scroll are one gesture.**
- Expect `tap` to be a fixed stage point.
- Expect the tap to land on empty white when `screenScroll` moves the target away from it.
- Render the 1.64s still. (Changed from 1.5s: the dot fades in from 1.5s, is fully visible at 1.64s, and is gone by 1.94s. The ring appears at 1.56s.)
- Check that the dot sits on something meaningful.

**7. `zsh` aborts the whole command on an unmatched glob.**
- Never run `rm still-*.jpg` in a clean workdir. It kills the line with `no matches found`.
- Use `find . -maxdepth 1 -name 'still-*.jpg' -delete`.

**8. `npm install` inside `scripts/` creates `node_modules/`.**
- Keep `node_modules/` in the skill's `scripts/` folder. It is gitignored.
- Never copy the scripts into the workdir. The scripts resolve their own dependencies.
- Expect `Cannot find module 'playwright-core'` when you run a script that you copied into the workdir.

**9. Site-hosted images are often small thumbnails.**
- Tell the user when a hero or carousel card looks soft.
- Offer to drop higher-resolution originals into `a/` under the same filenames.
- Never re-render at a size the source cannot support.

**10. No Google Chrome on the box.**
- Expect `render.cjs` and `fetch-images.cjs` to default to `channel: 'chrome'`.
- Run `npx playwright install chromium` in `scripts/` once.
- Pass `--channel chromium` to both scripts.

## Reference files

- [references/template-map.md](references/template-map.md): load before the first edit of `index.html`.
  - Load it also when you cut or add a beat, re-lay out to 9:16 or 1:1, build a 2× master, swap the font, set the end-card logo, or drop the proof row.
  - It holds the render contract, every `CONFIG` field, DOM ids and CSS variables, the geometry constants to change per aspect ratio, the timeline map, and the recipes.
- [assets/template.html](assets/template.html): load when you start Step 2. Copy it to `index.html`. Never edit it in place. It is the 15s 4:5 ad.
- [scripts/render.cjs](scripts/render.cjs): load when you render stills (Step 5) or the MP4 (Step 6). It seeks the paused timeline per frame and pipes PNGs to ffmpeg. Flags: `--stills`, `--out`, `--size`, `--fps`, `--page`, `--channel`.
- [scripts/fetch-images.cjs](scripts/fetch-images.cjs): load when you gather assets (Step 2). It scrolls the destination page and downloads its real imagery. Flags: `--url`, `--out`, `--min`, `--limit`, `--channel`.
- [scripts/contact-sheet.py](scripts/contact-sheet.py): load when you review images (Step 2) or stills (Step 5). It tiles images or stills into one labelled JPG for a single Read.

## Attribution and license

- Created by [danny.md](https://www.danny.md/skills/motion-ad).
- Published under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/): free to use and remix, not to sell.
- Redistributed via github.com/fabricioctelles/skills with added metadata, portable path resolution, a preflight check and `references/template-map.md`.
- Modified 2026-10-23: ASD-STE100 rewrite of `SKILL.md` and `references/template-map.md`, and consolidation into a 7-skill pack. `scripts/` and `assets/` are unchanged.
