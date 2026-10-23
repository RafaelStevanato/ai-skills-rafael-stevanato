# Tested snippets (javascript_tool)

Operating rules: [SKILL.md](../SKILL.md).
Per-site notes: [sites.md](sites.md).

## Usage rules

- Paste the whole block into `javascript_tool`.
- Set `action: "javascript_exec"`.
- In Claude in Chrome, also pass `tabId`.
- Read the last expression of the block as the return value.
- Use JS only to read, wait and prepare stubs.
- Send real clicks and real typing through `computer` (ref or coordinate).
- Never replace a real click with `element.click()`.
- Keep the code unchanged except placeholders and marked parameters.
- Replace every placeholder before you run a block: `SELETOR-DO-ITEM`, `SELETOR-DO-CARTAO`, `SELETOR`, `URL-DO-ARQUIVO-ACESSIVEL-PELA-PAGINA`.
- Keep snippet numbers 1-14 unchanged: SKILL.md cites snippets by number.
- Tested in the Claude browser pane (Chromium, 2026-10).
- Snippets 6, 12 and 13 were also tested in Claude in Chrome.

## Output token glossary

- Read the Portuguese keys and values that the snippets return with the table below.
- Never translate these tokens inside code: the code returns them as written.

| Snippet | Token | English meaning |
|---|---|---|
| 1 | `url` | Current page URL. |
| 1 | `titulo` | Page title. |
| 1 | `frameK` | Reminder string of the coordinate formula. `largura do frame do screenshot` = width of the screenshot coordinate frame. |
| 1 | `bloqueio` | Block list: names of detected blocks. Empty = no block found. Non-empty = stop. |
| 1 | `protecaoNoEnvio` | Submit protection: `true` when the HTML loads reCAPTCHA, hCaptcha or Turnstile scripts. |
| 1 | `cookies` | Visible button and link texts that match cookie-banner words. Max 8. |
| 1 | `modais` | Modals: first 80 characters of text of each visible dialog. Max 3. |
| 1 | `iframes` | Visible iframes and frames, each prefixed with `mesma-origem` or `outra-origem`, then the first 60 characters of `src`. |
| 1 | `mesma-origem` | Same origin: the frame content is readable. |
| 1 | `outra-origem` | Other origin (cross-origin): the frame content is not readable. Use screenshot only. |
| 1 | `shadowHosts` | Tag names of elements that own a shadow root. Max 5. |
| 1 | `formularios` | Forms: one number per form, the count of its fields (input except hidden, select, textarea). |
| 1 | `apis` | Last 8 resource URLs that match `/api/`, `graphql` or `.json`, without analytics and tracking hosts. |
| 1 | `cloudflare/turnstile` | `bloqueio` value: Cloudflare Turnstile or "Just a moment" challenge. |
| 1 | `recaptcha-visivel` | `bloqueio` value: visible reCAPTCHA challenge. |
| 1 | `hcaptcha-visivel` | `bloqueio` value: visible hCaptcha. |
| 1 | `datadome` | `bloqueio` value: DataDome block page. |
| 1 | `perimeterx` | `bloqueio` value: PerimeterX block (`px-captcha`). |
| 1 | `imperva` | `bloqueio` value: Imperva/Incapsula block ("Pardon Our Interruption"). |
| 1 | `akamai` | `bloqueio` value: Akamai "Access Denied ... Reference #" page. |
| 1 | `google-sorry` | `bloqueio` value: Google "unusual traffic" page (`/sorry/`). |
| 1 | `muro-de-login` | `bloqueio` value: login wall. |
| 1 | `texto-verificacao` | `bloqueio` value: verification text ("I'm not a robot"). |
| 1 | `verifique se você é humano` | Page text matched: "verify you are human". |
| 1 | `tráfego incomum` | Page text matched: "unusual traffic". |
| 1 | `para continuar, acesse` | Page text matched: "to continue, sign in". |
| 1 | `faça login para continuar` | Page text matched: "log in to continue". |
| 1 | `verificação adicional` | Page text matched: "additional verification". |
| 1 | `não sou um robô` | Page text matched: "I'm not a robot". |
| 1 | `confirme que você é humano` | Page text matched: "confirm you are human". |
| 1 | `aceit`, `rejeit`, `recus`, `não aceito`, `necess`, `configur`, `prosseguir`, `concordo` | Cookie-label stems in the `cookies` regex: accept, reject, refuse, I do not accept, necessary, configure, proceed, I agree. |
| 2 | `ALVO` | Target: visible text or CSS selector to find. |
| 2 | `FRAME_W` | Frame width: width of the "coordinate frame" of the last screenshot. |
| 2 | `PULAR` | Skip: set of tag names that the text search ignores. |
| 2 | `varrer` | Sweep: recursive function over the document, shadow roots and iframes. |
| 2 | `textoDe` | Text of: helper that returns the normalized text of an element. |
| 2 | `via` | Path to the element: `doc`, then `>shadow:<tag>`, `>iframe` or `>frame` for each level. |
| 2 | `texto` | Text of the element. First 60 characters. |
| 2 | `visivel` | Visible: `true` or `false`. |
| 2 | `desabilitado` | Disabled: `true` or `false`. |
| 2 | `x`, `y` | Center of the element, in the screenshot coordinate frame. |
| 2 | `iframeOutraOrigem` | Cross-origin iframe: its `src` (first 80 characters). The content is unreadable. |
| 3 | `limpo` | Clean: helper that collapses spaces and cuts text to 80 characters. |
| 3 | `rotulo` | Label of the field. |
| 3 | `tipo` | Type of the field (`type`, or `role`). |
| 3 | `nome` | Name of the field (`name`, or `id`). |
| 3 | `obrig` | Required. Shown as ` *` after the name. |
| 3 | `valor` | Value: `checked` for radio and checkbox, else the first 40 characters. |
| 3 | `desab`, `(desab)` | Disabled: the field is not enabled yet. |
| 3 | `opcoes` | Options of a select, joined with `/`. Max 15. |
| 4 | `ate` | Until: wait helper `ate(cond, ms = 20000, passo = 250)`. Returns the value of `cond`, or `null` on timeout. |
| 4 | `passo` | Step: polling interval in ms. |
| 6 | `__log` | Log of stubbed calls: `{ k, msg }` for alert, confirm, prompt. `{ k: "open", url }` for `window.open`. |
| 6 | `__resp` | Response: the value a stubbed `prompt` returns. |
| 6 | `RESPOSTA` | ANSWER: default text of `__resp`. |
| 6 | `__aceitar` | Accept: the value a stubbed `confirm` returns. |
| 6 | `stubs prontos: ajuste window.__resp/__aceitar, clique e leia window.__log` | "stubs ready: adjust window.__resp/__aceitar, click and read window.__log". |
| 7 | `URL-DO-ARQUIVO-ACESSIVEL-PELA-PAGINA` | Placeholder: URL of a file that the page can fetch. |
| 7 | `curriculo.pdf` | File name given to the upload (resume/CV). |
| 8 | `achados` | Findings: set of API paths found in the page scripts. |
| 9 | `SELETOR-DO-ITEM` | Placeholder: CSS selector of one list item. |
| 9 | `conta`, `antes`, `parado` | Count of items, previous count, number of rounds without change. |
| 10 | `linhas`, `cab`, `dados` | Rows, header row, data rows. |
| 10 | `SELETOR-DO-CARTAO` | Placeholder: CSS selector of one card. |
| 10 | `titulo`, `link` | Card title and card link. |
| 11 | `SELETOR` | Placeholder: CSS selector of the element to check. |
| 11 | `estado` | State: function that returns the visual state of an element. |
| 11 | `fora-do-DOM` | Out of the DOM: element is null or detached. |
| 11 | `oculto-css` | Hidden by CSS (display, visibility or opacity). |
| 11 | `tamanho-zero` | Zero size: width or height under 1 px. |
| 11 | `fora-da-pagina` | Off the page: above or left of the document origin. |
| 11 | `fora-da-viewport (role até ele)` | Outside the viewport. "role até ele" = scroll to it. |
| 11 | `ok` | Visible and receives the click. |
| 11 | `coberto-por <tag>#<id>` | Covered by the cited element. `coberto-por` = covered by. |
| 12 | `xy` | Function that returns `[x, y]` for each selector. |
| 12 | `#origem`, `#destino` | Placeholders: `#source` and `#destination` selectors. |
| 13 | `ler` | Read: recursive function over frames and iframes. |
| 13 | `via`, `texto`, `src` | Path to the frame, its text (first 300 characters), its `src` (first 60 characters). |
| 14 | `SUCESSO` | SUCCESS: prefix of the error message that ends the batch. |
| 14 | `sucesso` | Success: second word of the regex `/successful\|sucesso/i`. |

## 1. Page x-ray (run right after opening)

```js
const html = document.documentElement.outerHTML, txt = document.body?.innerText ?? "";
const vis = e => e.checkVisibility?.({ checkOpacity: true, checkVisibilityCSS: true }) && e.getBoundingClientRect().height > 30;
const algumVisivel = sel => [...document.querySelectorAll(sel)].some(vis);
const bloqueio = Object.entries({
  "cloudflare/turnstile": algumVisivel('.cf-turnstile, iframe[src*="challenges.cloudflare.com"]') || /just a moment|verifying you are human|verifique se você é humano/i.test(txt),
  "recaptcha-visivel": algumVisivel('iframe[src*="recaptcha"][title*="challenge"], iframe[src*="recaptcha/api2/bframe"], .g-recaptcha'),
  "hcaptcha-visivel": algumVisivel('iframe[src*="hcaptcha.com"]'),
  "datadome": /captcha-delivery\.com/i.test(html),
  "perimeterx": /px-captcha/i.test(html),
  "imperva": /pardon our interruption|_Incapsula_Resource/i.test(html + txt),
  "akamai": /access denied[\s\S]*reference #/i.test(txt),
  "google-sorry": /\/sorry\/|unusual traffic|tráfego incomum/i.test(location.href + txt),
  "muro-de-login": /account-verification|para continuar, acesse|sign in to continue|faça login para continuar/i.test(location.href + txt),
  "texto-verificacao": /verificação adicional|não sou um robô|i'm not a robot|confirme que você é humano/i.test(txt),
}).filter(([, v]) => v).map(([k]) => k);
const protecaoNoEnvio = (html.match(/recaptcha\/(api|enterprise)\.js|hcaptcha\.com\/1\/api|challenges\.cloudflare\.com\/turnstile/gi) ?? []).length > 0;
const botoes = [...document.querySelectorAll("button,a,[role=button]")].filter(vis);
({
  url: location.href, titulo: document.title, frameK: "x_frame = x_css * (largura do frame do screenshot / " + innerWidth + ")",
  bloqueio, protecaoNoEnvio,
  cookies: botoes.map(b => b.innerText.trim()).filter(t => /cookie|aceit|rejeit|recus|não aceito|necess|configur|prosseguir|concordo/i.test(t)).slice(0, 8),
  modais: [...document.querySelectorAll('[role=dialog],[aria-modal=true],.modal,[class*=Modal],[class*=overlay]')].filter(vis).map(m => m.innerText.slice(0, 80)).slice(0, 3),
  iframes: [...document.querySelectorAll("iframe,frame")].filter(vis).map(f => { try { return f.contentDocument ? "mesma-origem " + f.src.slice(0, 60) : "outra-origem " + f.src.slice(0, 60); } catch { return "outra-origem " + f.src.slice(0, 60); } }),
  shadowHosts: [...document.querySelectorAll("*")].filter(e => e.shadowRoot).map(e => e.tagName.toLowerCase()).slice(0, 5),
  formularios: [...document.forms].map(f => f.querySelectorAll("input:not([type=hidden]),select,textarea").length),
  apis: performance.getEntriesByType("resource").map(r => r.name).filter(n => /\/api\/|graphql|\.json(\?|$)/i.test(n) && !/google|gtm|doubleclick|facebook|hotjar|clarity|analytics|sentry|unleash/i.test(n)).slice(-8),
})
```

- Stop and hand over to the user when `bloqueio` is not empty.
- Read `protecaoNoEnvio` as: the form submit has an invisible CAPTCHA.
- Read and fill the form when `protecaoNoEnvio` is `true`.
- Never submit the form by automation when `protecaoNoEnvio` is `true`.
- Note that the `cookies` regex is Portuguese-centric: `rejeit` does not match "reject".

## 2. Locate anywhere (shadow DOM + iframes) and return coordinates

- Set `ALVO` to visible text or a CSS selector.
- Set `FRAME_W` to the width of the "coordinate frame" of the last screenshot.

```js
const ALVO = "Click me", FRAME_W = 800;
const k = FRAME_W / innerWidth, norm = s => (s || "").replace(/\s+/g, " ").trim().toLowerCase(), alvo = norm(ALVO), out = [];
const PULAR = new Set(["SCRIPT", "STYLE", "NOSCRIPT", "TEMPLATE", "HEAD", "IFRAME", "FRAME"]);
const visivel = e => !!e.checkVisibility?.({ checkOpacity: true, checkVisibilityCSS: true }) && e.getBoundingClientRect().width > 0;
const textoDe = e => norm(e.innerText || e.value || e.getAttribute("aria-label") || e.getAttribute("placeholder") || e.title);
function varrer(raiz, ox, oy, via) {
  let porSeletor = []; try { porSeletor = [...raiz.querySelectorAll(ALVO)]; } catch {}
  const todos = [...raiz.querySelectorAll("*")];
  const porTexto = porSeletor.length ? [] : todos.filter(e => !PULAR.has(e.tagName) && !e.shadowRoot && textoDe(e).includes(alvo) && ![...e.children].some(c => textoDe(c).includes(alvo)));
  for (const e of [...porSeletor, ...porTexto]) { const r = e.getBoundingClientRect(); out.push({ via, tag: e.tagName.toLowerCase(), texto: textoDe(e).slice(0, 60), visivel: visivel(e), desabilitado: !!e.disabled, x: Math.round((ox + r.x + r.width / 2) * k), y: Math.round((oy + r.y + r.height / 2) * k) }); }
  for (const e of todos) {
    if (e.shadowRoot) varrer(e.shadowRoot, ox, oy, via + ">shadow:" + e.tagName.toLowerCase());
    if (e.tagName === "IFRAME" || e.tagName === "FRAME") { const r = e.getBoundingClientRect(); try { varrer(e.contentDocument, ox + r.x + e.clientLeft, oy + r.y + e.clientTop, via + ">" + e.tagName.toLowerCase()); } catch { out.push({ via, iframeOutraOrigem: e.src.slice(0, 80) }); } }
  }
}
varrer(document, 0, 0, "doc");
out.sort((a, b) => (b.visivel ?? 0) - (a.visivel ?? 0)).slice(0, 10)
```

- Expect up to 10 results, visible elements first.
- Click with `computer left_click` and `coordinate: [x, y]`.
- Take a screenshot first when the page changed since the last screenshot.
- Scroll an off-screen element into view with `computer scroll` or `el.scrollIntoView({ block: "center", behavior: "instant" })`.
- Run the snippet again after the scroll.
- Always set `behavior: "instant"`: on sites with `scroll-behavior: smooth`, you measure in the middle of the scroll.
- For a cross-origin iframe (payment, reCAPTCHA), use screenshot plus coordinate only.

## 3. Form map (all fields in one call)

```js
const limpo = s => (s || "").replace(/\s+/g, " ").trim().slice(0, 80);
const rotulo = e => {
  const direto = limpo(e.labels?.[0]?.innerText) || limpo(e.getAttribute("aria-label")) || limpo(e.getAttribute("aria-labelledby")?.split(" ").map(id => document.getElementById(id)?.innerText).join(" "));
  if (direto) return direto;
  for (let p = e.parentElement, i = 0; p && i < 8; p = p.parentElement, i++) { const l = [...p.querySelectorAll("label,legend,h3,h4,[class*=label],[class*=Label],[class*=placeholder]")].find(l => !l.contains(e) && limpo(l.innerText)); if (l) return limpo(l.innerText); }
  return limpo(e.placeholder || e.name);
};
[...document.querySelectorAll("input:not([type=hidden]),select,textarea,[contenteditable=true],[role=combobox],[role=radiogroup]")]
  .filter(e => e.checkVisibility?.() || e.type === "radio" || e.type === "checkbox" || e.type === "file")
  .map(e => ({ rotulo: rotulo(e), tipo: e.type || e.getAttribute("role"), nome: e.name || e.id, obrig: e.required || e.getAttribute("aria-required") === "true", valor: e.type === "radio" || e.type === "checkbox" ? e.checked : (e.value ?? e.innerText)?.slice?.(0, 40), desab: e.disabled, opcoes: e.tagName === "SELECT" ? [...e.options].map(o => o.text).slice(0, 15).join("/") : "" }))
  .map(o => `${o.rotulo} | ${o.tipo} | ${o.nome}${o.obrig ? " *" : ""}${o.desab ? " (desab)" : ""} = ${o.valor}${o.opcoes ? " [" + o.opcoes + "]" : ""}`)
```

- Read one output line per field: `label | type | name * = value`.
- Expect radios of the same group to repeat `name`.
- Expect a react-select field as `text` with label "Select ..." and an empty value.
- Read the chosen react-select value with `[...document.querySelectorAll("[class*=singleValue],[class*=multiValue]")].map(e => e.innerText)`.
- Read `(desab)` as: the field is not enabled yet (it depends on another field).
- Validate without submitting with `form.checkValidity()`.
- List the invalid fields with `[...form.querySelectorAll(":invalid")].map(e => e.name || e.id)`.

## 4. Wait for a condition (instead of wait + screenshot loop)

```js
const ate = (cond, ms = 20000, passo = 250) => new Promise(ok => { const t0 = Date.now(); const i = setInterval(() => { const v = cond(); if (v || Date.now() - t0 > ms) { clearInterval(i); ok(v || null); } }, passo); });
await ate(() => document.querySelector(".bg-success")?.innerText)
```

## 5. Element stopped moving (animated modal, sliding menu)

```js
const el = document.querySelector(".modal"); const pos = () => JSON.stringify(el.getBoundingClientRect());
let a = pos(); for (let i = 0; i < 20; i++) { await new Promise(r => setTimeout(r, 150)); const b = pos(); if (a === b) break; a = b; } a
```

## 6. Native dialogs (alert/confirm/prompt) and new tab

- Install this stub before any click that can open alert, confirm or prompt.
- Adjust `window.__resp` and `window.__aceitar`, click, then read `window.__log`.

```js
window.__log = []; window.__resp = "RESPOSTA"; window.__aceitar = true;
for (const k of ["alert", "confirm", "prompt"]) { window[k] = (...a) => { window.__log.push({ k, msg: a[0] }); return k === "confirm" ? window.__aceitar : k === "prompt" ? window.__resp : undefined; }; }
window.open = (u) => { window.__log.push({ k: "open", url: new URL(String(u), location.href).href }); return null; };
"stubs prontos: ajuste window.__resp/__aceitar, clique e leia window.__log"
```

- Install the stubs again after each `navigate`: they vanish when the page navigates or reloads.
- Expect alerts fired by a right click (`computer right_click`) in `__log` too.
- Set `__aceitar = true` only when accepting is what the user wants (example: "are you sure you want to leave?" in an authorized flow).
- Set `__aceitar = false` when in doubt. The snippet above ships with `true`.
- Open a new tab: read the URL in `__log`, then use `navigate`.

## 7. File upload without the OS picker

Use this snippet in the Claude browser pane.

```js
const inp = document.querySelector("input[type=file]");
const bytes = await (await fetch("URL-DO-ARQUIVO-ACESSIVEL-PELA-PAGINA")).blob(); // or new Blob(["conteúdo"])
const dt = new DataTransfer(); dt.items.add(new File([bytes], "curriculo.pdf", { type: "application/pdf" }));
inp.files = dt.files; inp.dispatchEvent(new Event("input", { bubbles: true })); inp.dispatchEvent(new Event("change", { bubbles: true }));
inp.files[0]?.name
```

## 8. Find the API the page uses (skip the UI)

```js
const achados = new Set();
for (const s of [...document.scripts].map(s => s.src).filter(Boolean)) {
  try { const t = await (await fetch(s)).text(); for (const m of t.matchAll(/["'`](\/(?:api|v\d|graphql|apply|search)[^"'`\s]{2,80})["'`]/gi)) achados.add(m[1]); } catch {}
}
[...achados].slice(0, 40)
```

- Combine with `read_network_requests` (filter by `api`) after you use the search once in the UI.
- Test the endpoint with `fetch` in the page console (same origin and cookies) before you build on it.

## 9. Infinite scroll

```js
const conta = () => document.querySelectorAll("SELETOR-DO-ITEM").length; let antes = -1, parado = 0;
for (let i = 0; i < 15 && parado < 2; i++) { window.scrollTo(0, document.body.scrollHeight); await new Promise(r => setTimeout(r, 1500)); const n = conta(); parado = n === antes ? parado + 1 : 0; antes = n; }
antes
```

- Wait at least 1.5 s per round: less than 1.5 s did not load in test.
- Use `computer scroll` (real mouse wheel) when nothing loads.
- Find the API (snippet 8) when nothing loads.

## 10. Extract a table or list as data

- Use for a `<table>` or a table made of `div` with `role=row`.
- Find columns by header, never by index: the column order changes.

```js
const linhas = [...document.querySelectorAll("table tr, [role=row]")].map(r => [...r.querySelectorAll("th,td,[role=columnheader],[role=cell]")].map(c => c.innerText.trim()));
const [cab, ...dados] = linhas;
dados.map(l => Object.fromEntries(cab.map((h, i) => [h, l[i]])))  // e.g.: .find(o => o.Name === "Chrome")?.CPU
```

For cards, use: `[...document.querySelectorAll("SELETOR-DO-CARTAO")].map(c => ({ titulo: c.querySelector("h2,h3")?.innerText, link: c.querySelector("a")?.href }))`

## 11. Real visual state (what checkVisibility misses)

Use this function to get the reason and the element that receives the click.

```js
const estado = e => {
  if (!e?.isConnected) return "fora-do-DOM";
  if (!e.checkVisibility({ checkOpacity: true, checkVisibilityCSS: true })) return "oculto-css";
  const r = e.getBoundingClientRect();
  if (r.width < 1 || r.height < 1) return "tamanho-zero";
  if (r.bottom + scrollY <= 0 || r.right + scrollX <= 0) return "fora-da-pagina";
  if (r.bottom <= 0 || r.top >= innerHeight || r.right <= 0 || r.left >= innerWidth) return "fora-da-viewport (role até ele)";
  const t = document.elementFromPoint(r.x + r.width / 2, r.y + r.height / 2);
  return t === e || e.contains(t) ? "ok" : `coberto-por ${t?.tagName.toLowerCase()}${t?.id ? "#" + t.id : ""}`;
};
estado(document.querySelector("SELETOR"))
```

- Read `coberto-por`: a click there goes to the cited element (overlay, modal, banner).
- Close the cited element before you click.

## 12. Coordinates of a selector (cheapest path when the selector is known)

- Always check the "coordinate frame" text of the screenshot, then set `FRAME_W`.
- Pass one or more selectors. Read one `[x, y]` pair per selector.

```js
const FRAME_W = 800; // width of the "coordinate frame" of the last screenshot (Claude browser pane: 800; Claude in Chrome: innerWidth)
// scroll ONCE (to the 1st selector) and measure all afterwards; measuring one, scrolling, measuring another leaves the 1st coordinate stale
const xy = async (...seletores) => { const els = seletores.map(s => document.querySelector(s)); els[0].scrollIntoView({ block: "center", behavior: "instant" }); await new Promise(r => setTimeout(r, 300)); const k = FRAME_W / innerWidth; return els.map(e => { const r = e.getBoundingClientRect(); return [Math.round((r.x + r.width / 2) * k), Math.round((r.y + r.height / 2) * k)]; }); };
await xy("#origem", "#destino")  // [[x,y],[x,y]]
```

- Take a screenshot before the click when the page changed since the last screenshot.
- Run this batch: `screenshot` (scale 0.1) → `left_click` at the coordinate → JS that verifies.

## 13. Read text from iframes and frames (recursive)

- Remember that a frameset (`<frame>`) is not an iframe: `querySelectorAll("iframe")` returns empty in it.

```js
const ler = (doc, via = "doc") => [...doc.querySelectorAll("frame,iframe")].flatMap(f => { const nome = `${via}>${f.tagName.toLowerCase()}${f.name ? "[" + f.name + "]" : ""}`; try { const d = f.contentDocument; return [{ via: nome, texto: (d.body?.innerText ?? "").trim().slice(0, 300) }, ...ler(d, nome)]; } catch { return [{ via: nome, texto: null, src: f.src.slice(0, 60) }]; } });
ler(document)
```

- Read `texto: null` as: other origin (ad, payment, CAPTCHA). Use screenshot only.
- Skip this snippet for shadow DOM: `document.body.innerText` and `get_page_text` already return that text, slots included.

## 14. Repeat until success (inside a batch)

- Throw an error from JS when it sees success: the batch stops at the first failing step, so the error ends the loop.
- Run this JS after each attempt.

```js
const m = document.querySelector("#flash")?.innerText ?? "";
if (/successful|sucesso/i.test(m)) throw new Error("SUCESSO: " + m.trim());
m.trim()
```

- Run the batch: `[screenshot 0.1, left_click (x,y), JS above] × N`.
- Read the error "SUCESSO: ..." in the result as success.
- Conclude that no attempt succeeded when the batch ends without that error.
- Keep the screenshot in each round: a click that navigates needs a new screenshot before the next coordinate.
