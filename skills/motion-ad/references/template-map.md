# Template map — `assets/template.html`

Copy the template. Edit the copy. Name the edited file `index.html`: `render.cjs` defaults to `--page index.html`.

**Contents**

- [Render contract](#render-contract)
- [CONFIG reference](#config-reference)
- [Color system](#color-system)
- [DOM map by beat](#dom-map-by-beat)
- [Geometry constants](#geometry-constants)
- [Timeline map](#timeline-map)
- [Optional elements and guards](#optional-elements-and-guards)
- [Helper functions](#helper-functions)
- [Asset specs](#asset-specs)
- [Recipes](#recipes)
  - [Cut a beat](#cut-a-beat)
  - [Add a beat](#add-a-beat)
  - [Re-lay out for 9:16](#re-lay-out-for-916)
  - [Re-lay out for 1:1](#re-lay-out-for-11)
  - [2× master](#2-master)
  - [Swap the font](#swap-the-font)
  - [Logo on the end card](#logo-on-the-end-card)
  - [Drop the proof row](#drop-the-proof-row)

---

## Render contract

Keep these four items at the bottom of the script after every edit. `render.cjs` depends on them:

|Line (approx.)|Statement|Why it exists|
|---|---|---|
|~440|`window.seek = t => { tl.seek(t, false); return true }`|The renderer calls this per frame. `false` suppresses callbacks so the loop guard can't restart the timeline mid-render.|
|~441|`window.DURATION = 15`|Single source of truth for the frame count: `total = round(DURATION × FPS)`. It is *not* read from the timeline.|
|~442|`window.ready = Promise.all([document.fonts.ready, ...imgs.map(i => i.decode().catch(() => {}))])`|Renderer waits on this so no frame is captured before fonts and images land.|
|~443|`if (!/render/.test(location.search)) { tl.play(); ... }`|`render.cjs` loads the page as `file://…?render`. Without this guard, autoplay races the seek loop and every frame is a coin flip.|

- `render.cjs` waits 500ms after `window.ready` resolves: a font swap or image decode can land a frame later. Never shorten that wait. A fallback-font flash on the first frames means the wait is too short.
- Hard-code timeline durations in seconds. Never derive them from `DURATION`. After you shorten the timeline, set `DURATION` to match and move the loop guard `tl.to({}, { duration: 0.01 }, 15)`. The guard pins the total length to 15s.

## CONFIG reference

`CONFIG` is one object at the top of the script. It holds everything brand- and product-specific. Use `null` or `[]` for any optional field: the template then degrades to labelled placeholders and drops optional rows. It does not break.

### Identity

|Field|Type|Effect|
|---|---|---|
|`brand`|string|Wordmark fallback when no `logo` is set. Also the default in `cta.foot` context.|
|`logo`|path \| null|Shown top-left on the light background.|
|`logoOnDark`|path \| null|End card. Falls back to `logo` inverted to white.|
|`colors`|object|See [Color system](#color-system).|

### Beat A — hook + phone (0–2.2s)

|Field|Type|Effect|
|---|---|---|
|`hook`|string|Beat A headline. `*word*` accents, `\n` breaks.|
|`screen`|path \| null|Tall phone-width screenshot that scrolls. Portrait ≈488×1600.|
|`screenScroll`|number|Pixels the screen image scrolls **up** (negative).|
|`tap`|`{x, y}`|Stage point the finger lands on. The hero card grows out of this point, and the tap ring/dot are centered on it. Must coincide with the meaningful spot of `screen` *after* `screenScroll`.|

### Beat B — before → after (2.2–5.4s)

|Field|Type|Effect|
|---|---|---|
|`reveal`|string|Beat B headline.|
|`before`, `after`|path \| null|Hero pair. Same framing is what sells the transformation.|
|`beforeLabel`, `afterLabel`|string|Tag chips over the hero. Set them to what the images actually show.|
|`benefits`|string[3]|Benefit pills. Only the first three render (`slice(0, 3)`), and there are exactly three `PILL_POS` slots — a fourth pill would be positioned at `undefined`.|

### Beat C — wall of outputs (5.5–8.7s)

|Field|Type|Effect|
|---|---|---|
|`scale`|string|Beat C headline.|
|`scaleChip`|string|Supporting chip under the headline.|
|`gallery`|path[]|Output images. Padded to a minimum of 12 and drawn across a 7×7 grid, so fewer than ~12 distinct images repeat visibly side by side.|

Supply at least 12 distinct gallery images. Ignore the `6–20 output images` comment in `assets/template.html`.

### Beat D — showcase + proof (8.7–11.8s)

|Field|Type|Effect|
|---|---|---|
|`proofHl`|string|Beat D headline.|
|`showcase`|`[{img, inset, insetLabel, tag}]`|Exactly three cards. `inset` is the optional small "before" image; `tag` is the small "after" label. Both are omitted when falsy.|
|`showChip`|string|Chip under the carousel.|
|`proof`|`{stars, text}` \| null|Social-proof row. `text` supports `**bold**`. `null` removes the row entirely — the right answer when there's no real number to show.|

### Beat E — end card (11.8–15s)

|Field|Type|Effect|
|---|---|---|
|`cta.headline`|string|End-card headline. `*word*` accents, `\n` breaks.|
|`cta.chip`|string|Reassurance line under the headline (HTML allowed — it uses `innerHTML`).|
|`cta.button`|string|Button label. The arrow is a separate span.|
|`cta.foot`|string|Small line at the bottom, usually the domain.|

## Color system

`CONFIG.colors` writes CSS custom properties onto `document.documentElement` at load:

```js
Object.entries(CONFIG.colors).forEach(([k, v]) => root.setProperty(`--${k}`, v))
```

Set only the five base tokens: `primary`, `accent`, `page`, `ink2`, `line`. `color-mix()` derives every other token:

|Derived|Formula|Used by|
|---|---|---|
|`--accent-deep`|accent 82% + black|Accent text on light|
|`--accent-soft`|accent 45% + white|Accent on the dark end card|
|`--accent-tint`|accent 14% + transparent|Tint chips, dot|
|`--primary-raised`|primary 80% + accent|End-card radial glow|
|`--primary-deep`|primary 70% + black|Phone body, notch, tags|
|`--warm`|page 92% + primary 8%|Tile and card backgrounds|

Re-check `#topFade` and `#botFade` after you change `page` to a dark value. Both blend to `--page` and then hide the wall edges in the wrong direction.

## DOM map by beat

Position every element `position:absolute` inside `#stage`. To add an element, put it inside `#stage` and position it in px.

|Beat|Element ids|Key classes|
|---|---|---|
|Frame|`#stage` `#bgGlow` `#dots` `#brand`|`.abs`, `.wordmark`|
|A|`#hl1` `#phone` `#screen` `#screenImg` `#notch` `#ring` `#dot`|`.hl`|
|B|`#hl2` `#hero` `#heroBefore` `#heroAfter` `#beam` `#beamTrail` `#scanGrid` `#tagBefore` `#tagAfter` `#pills`|`.tag`, `.pill`|
|C|`#wallWrap` `#wall` `#topFade` `#botFade` `#hl3` `#sub3` `#spark`|`.t`|
|D|`#hl4` `#car` `#track` `#sc0`–`#sc2` `#showChip` `#proof` `#stars`|`.sc`, `.bef`, `.aft`, `.stars`|
|E|`#wipe` `#end` `#endGlow` `#orbs` `#orb0`–`#orb5` `#endLogo` `#endHl` `#endChip` `#endBtn` `#btn` `#btnArrow` `#endFoot` `#tap`|`.orb`, `.chip`|

- `words()` generates the headline structure: each line becomes `<span class="w"><span class="wi">…</span></span>` per word, with `<br>` between lines. The outer `.w` clips (`overflow:hidden`). The inner `.wi` slides, which masks words in and out. Accented words wrap their text in `<em>`.
- Headlines are `position:absolute` at a fixed `top` in a 960px box (the phone is at `top:392`). Words wrap at spaces. Use `\n` in the `CONFIG` string to fix where the breaks land.

## Geometry constants

CSS positions live in `<style>`. JS positions live in the script.

### JS constants

|Constant|Value|Meaning / when to change|
|---|---|---|
|`TAP`|`CONFIG.tap`|Finger target and hero growth origin.|
|`HERO`|`{x:240, y:392, w:600, h:744}`|Hero card box in beat B. `y` is the single most important number for 9:16.|
|`PILL_POS`|`[{70,560}, {690,780}, {110,1010}]`|Three benefit-pill positions. Exactly three slots.|
|`SC_W`, `SC_GAP`|`570`, `44`|Showcase card width and gap. Card `i` sits at `left = 255 + i × 614`; `carTo(i) = -i × 614`.|
|`orbData`|6 × `{x, y, r}`|End-card floating thumbnails, kept at the frame edges (4 corners, 2 mid-sides). The centered end-card stack — headline, chip, button, foot — is what must stay readable.|
|`WALL_CENTER`|`24`|Center cell of the 7×7 grid; holds the hero "after" image.|
|wall grid|7 cols × 210px, gap 22, 49 tiles of 210×262|`gallery[(i×3 + floor(i/7)×5) % len]` picks each cell — the formula is why few images repeat.|
|gallery pad|`Math.max(gallery.length, 12)`|Minimum 12 entries.|

### CSS positions (1080×1350 stage)

|Selector|Position|
|---|---|
|`html, body, #stage`|1080 × 1350|
|`.hl` (all headlines)|`top:128px; left:60px; width:960px; font-size:82px`|
|`#phone`|`left:280; top:392; 520×1100`|
|`#sub3`|`top:246` (inline style in markup)|
|`#car` / `#track`|`top:372; height:708`|
|`#showChip`|`top:1108`|
|`#proof`|`top:1196`|
|`#wipe`|centered 3400×3400 circle, `z-index:60`|
|`#endLogo`|`top:330`|
|`#endHl`|`top:440; font-size:92px`|
|`#endChip`|`top:710`|
|`#endBtn`|`top:840` (button 110px tall)|
|`#endFoot`|`top:1010`|
|`#topFade` / `#botFade`|560px / 260px gradients blending to `--page`|

## Timeline map

Every call passes an absolute second. To retime, edit these numbers, not durations. These are the exact call-site windows. The windows in the `CONFIG` headings and in [SKILL.md](../SKILL.md) are nominal (storyboard).

|Window|Beat|Call sites|
|---|---|---|
|0.00–2.18|A: hook, phone rise, screen scroll, tap ring + dot, screen dims|`0`, `0.05`, `0.25`, `1.5`, `1.56`, `1.64`, `1.8`|
|2.15–5.45|B: hero grows from tap, beat A words out, B words in, before tag, scan beam 3.4→4.4, after tag, hero pulse, benefit pills in and floating|`2.15`, `2.18`, `2.2`, `2.55`, `2.95`, `3.1`, `3.35`, `3.4`, `4.3`, `4.35`, `4.4`, `4.42`, `4.45`, `4.8`|
|5.45–8.55|C: pills out, hero shrinks and rotates into the wall, wall tiles fly in from `z:-900` on a center-out grid stagger, wall drifts, fades in, words swap|`5.45`, `5.5`, `5.55`, `5.6`, `5.95`, `6.3`, `6.45`, `6.55`|
|8.50–11.75|D: wall scales away, carousel slides in with `rotateY`, cards 1 and 2 dim, chip, stars, proof, two `slide()` calls|`8.5`, `8.55`, `8.9`, `8.95`, `9.0`, `9.2`, `9.3`, `9.35`, `9.4`, `9.45`, `9.7`, `10.05`, `10.95`|
|11.70–15.00|E: circle wipe, end card in, logo, words, chip, button, orbs in and floating, foot, tap ring, button press and elastic settle, arrow nudge, duration guard|`11.7`, `11.75`, `12.3`, `12.35`, `12.45`+`0.07i`, `12.5`, `12.95`, `13.1`, `13.35`, `13.85`, `14.05`, `14.12`, `14.17`, `14.3`, `15`|

- Check: Beat B also has call site `3.6` (`#tagBefore` out).
- Use `wordsIn(sel, at, stagger, dur)` to slide words up from below with a slight rotate. Use `wordsOut(sel, at)` to slide them up and out. Never re-derive the word-mask transforms.

## Optional elements and guards

Animate optional elements only when present, via `has(sel)`:

```js
const has = sel => document.querySelector(sel) !== null
```

Guarded: `.pill` (no benefits → no pills), `#proof` (`proof: null` removes the element), `#stars i` (`stars: false`). The reveal and end-card tweens filter their targets through `has` for the same reason.

- `benefits: []` leaves the markup empty. The guarded tweens are skipped without errors.
- `showcase` is `slice(0, 3)`-ed. `slide(1, 10.05)` and `slide(2, 10.95)` are hard-coded for exactly three cards. With fewer cards, remove the matching `slide()` call, or the track slides into empty space.
- Element removal happens at build time (`$('#proof').remove()`). The guards keep a `null` proof from breaking the timeline.
- Two tweens take a `.filter(has)` target list instead of a single selector: the initial-state block for beat D and the end-card exit. Add every new optional element to both lists, or the timeline tweens it after removal.

## Helper functions

|Function|Purpose|
|---|---|
|`words(str)`|Headline markup: `*word*` → `<em>` accent, `\n` → `<br>`, per-word mask spans.|
|`bold(str)`|`**text**` → `<b>`. Used only by `proof.text`.|
|`ph(label, i, w, h)`|Labelled placeholder SVG as a data URI; hue varies with `i`.|
|`setImg(el, src, label, i, w, h)`|Sets `src`; on error swaps in the placeholder **once** (`el.onerror = null` first, so a failing placeholder can't loop).|
|`imgTag(src, label, i, w, h)`|`<img data-src data-label data-i data-w data-h>` for images created via `innerHTML`.|
|`hydrate(root)`|Applies `setImg` to every `img[data-label]` under `root`. New image grids must be hydrated.|
|`brandMark(src, dark)`|`<img>` or wordmark; inverts to white when `dark` and no `logoOnDark`.|

## Asset specs

Real images land in fixed CSS boxes with `object-fit: cover` and `object-position: 50% 0%` (top-aligned: the top of an image survives the crop). The `w` and `h` arguments to `ph`, `setImg` and `imgTag` size the **placeholder** only.

|Asset|Placeholder ratio|Box|Notes|
|---|---|---|---|
|`screen`|488×1600|`#screen` 100%×100%, image `height:auto`|Must be tall; a square capture leaves the phone mostly empty.|
|`before` / `after`|600×744|`#hero` 600×744|≈4:5. Match the framing of the pair.|
|`gallery`|210×262|wall tile 210×262|Portrait.|
|`showcase[].img`|570×708|`.sc` 570×708|Portrait; the card is 708px tall in a 708px-tall `#car`.|
|`showcase[].inset`|176×208|`.bef` 176×208|Rotated −4°.|
|orbs|150×188|`.orb` 150×188|Cropped from `gallery`.|

## Recipes

### Cut a beat

Keep the markup, so the initial-state `gsap.set` calls and guards still resolve. Delete the `tl.*` block of the beat:

1. Delete the `tl` calls for that window from the [timeline map](#timeline-map).
2. Re-time every later `at` value so the remaining beats close up.
3. Update `window.DURATION` and move the `tl.to({}, { duration: 0.01 }, 15)` guard.
4. To hide an element that must not appear at all, run `gsap.set('#el', { display: 'none' })` in the initial-state block. Guard its tweens with `has()`.

Never delete calls without re-timing: the video holds a still frame for the length of the removed beat.

### Add a beat

1. Add a DOM block inside `#stage` plus its CSS in the `<style>` block.
2. Set its initial state in the initial-state block (`gsap.set('#newEl', { autoAlpha: 0, … })`).
3. Add the `tl` calls at a chosen second, and shift everything after it.
4. If a `CONFIG` flag can remove the element, wrap its tweens in `if (has('#newEl'))`. Add the element to the `.filter(has)` lists of the reveal and end-card tweens.

### Re-lay out for 9:16

- Keep every horizontal position. The stage grows vertically: change `html, body, #stage` to `1080 × 1920`.
- Move these down: `.hl` `top`; `#phone` `top` (and `height`, or let it stay tall and start lower); `HERO.y`; `PILL_POS[*].top`; `#sub3`, `#car`, `#showChip` and `#proof` `top`; the whole end card (`#endLogo` 330, `#endHl` 440, `#endChip` 710, `#endBtn` 840, `#endFoot` 1010 → spread these out proportionally); `orbData[*].y`, so orbs don't sit behind the headline.
- Leave `#wipe` unchanged: it is already a 3400px circle centered on the stage. Render with `--size 1080x1920`.
- Check the stills after re-spacing. Headlines and cards collide. The end card is where the vertical room runs out.

### Re-lay out for 1:1

- 1080×1080 has *less* vertical room than 4:5. The phone is 520×1100 and cannot fit.
- Either scale the phone down (roughly 0.55×) and shrink `#screenImg` with it, or replace beat A with a hero-card open.
- Compress everything below the phone: `HERO`, `PILL_POS`, `#car`, the end card. Render with `--size 1080x1080`.
- Offer 4:5 or 9:16 when the user has a choice. Both fit the template honestly. 1:1 usually means a different edit, not a re-space.

### 2× master

`--size` alone fails: the CSS is fixed at 1080×1350 and `render.cjs` uses `deviceScaleFactor: 1`. A 2160×2700 viewport then renders a 1080×1350 ad centered in a larger frame. To double the pixels, scale the stage in CSS and match the viewport:

```css
#stage { transform: scale(2); transform-origin: top left; }
```

- Render with `--size 2160x2700`. Text scales with the stage. Re-check the headline budget and the contact sheet: an over-budget headline that fit at 1× can overflow at 2×.
- Check (not render-verified): `assets/template.html` sets `html,body{width:1080px;height:1350px;overflow:hidden}`, which can clip a `scale(2)` `#stage` to the top-left quarter. Set `html, body` to 2160×2700 before a 2× render.

### Swap the font

- Change the family in the Google Fonts `<link>` **and** the `--font` variable.
- Keep `display=block` in the query string. Without it the browser paints the fallback face and swaps later. Symptom: a font flicker in the first second of the video.

### Logo on the end card

- The template uses `logoOnDark` when set. Otherwise it inverts `logo` with `filter: brightness(0) invert(1)`.
- That inversion is correct only for a dark-on-transparent mark: a full-color logo turns into a white silhouette.
- Provide `logoOnDark` for every full-color logo, and when in doubt.

### Drop the proof row

- Set `proof: null`. The build removes the row. `has('#proof')` guards every proof tween, so the timeline is unaffected.
- Use `proof: null` whenever there is no real rating or review count.

---

License: CC-BY-NC-4.0. Original by [danny.md](https://www.danny.md/skills/motion-ad). Modified 2026-10-23: prose rewritten to ASD-STE100. See `metadata.modified` in [SKILL.md](../SKILL.md).
