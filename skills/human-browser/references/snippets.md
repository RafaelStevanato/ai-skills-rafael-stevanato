# Tested snippets (javascript_tool)

Operating rules: [SKILL.md](../SKILL.md). Per-site notes: [sites.md](sites.md).

## Usage rules

- Paste the whole block into `javascript_tool` with `action: "javascript_exec"`. In Claude in Chrome, also pass `tabId`. The last expression is the return value.
- Use JS only to read, wait and prepare stubs.
- Keep the code unchanged except placeholders and marked parameters.
- Replace every placeholder before you run a block: `SELETOR-DO-ITEM` (item selector, 9), `SELETOR-DO-CARTAO` (card selector, 10), `SELETOR` (target selector, 11), `URL-DO-ARQUIVO-ACESSIVEL-PELA-PAGINA` (file URL, 7).
- Tested in the Claude browser pane (Chromium, 2026-10). Snippets 6, 12 and 13 also in Claude in Chrome.

## Output token glossary

Portuguese tokens are returned as written. Never translate them in code.

|Snippet|Token and meaning|
|---|---|
|1|`titulo` title; `frameK` coordinate formula reminder (`largura do frame do screenshot` = screenshot coordinate frame width); `bloqueio` detected blocks (not empty = stop); `protecaoNoEnvio` submit protection (reCAPTCHA, hCaptcha or Turnstile script in the HTML; `true` = invisible CAPTCHA on submit: fill the form, never submit it by automation); `modais` modals; `formularios` field count per form; in `iframes`, `mesma-origem` same origin (readable), `outra-origem` cross-origin (unreadable)|
|1|`bloqueio` values: `recaptcha-visivel` visible reCAPTCHA; `hcaptcha-visivel` visible hCaptcha; `muro-de-login` login wall; `texto-verificacao` verification text; `google-sorry` Google "unusual traffic" page|
|1|`cookies` regex stems `aceit`, `rejeit`, `recus`, `não aceito`, `necess`, `configur`, `prosseguir`, `concordo` = accept, reject, refuse, I do not accept, necessary, configure, proceed, I agree (Portuguese only: `rejeit` does not match "reject")|
|2|`ALVO` target; `FRAME_W` frame width; `PULAR` skip (tags the text search ignores); `varrer` sweep (recursive walk); `via` path (`doc`, then `>shadow:<tag>`, `>iframe` or `>frame`); `x`, `y` element center in the screenshot coordinate frame; `iframeOutraOrigem` cross-origin iframe `src`|
|3|`rotulo` label; `obrig` required (` *` after the name); `desab`, `(desab)` disabled (not enabled yet: it depends on another field)|
|4, 6-8|`ate` until (returns the condition value, or `null` on timeout); `__log` log of stubbed calls (`{ k, msg }` for alert, confirm, prompt; `{ k: "open", url }` for `window.open`); `__resp` prompt response; `RESPOSTA` ANSWER, its default; `__aceitar` accept, the confirm result; `stubs prontos: ...` stubs ready; `curriculo.pdf` resume file name|
|11|`fora-do-DOM` out of the DOM (null or detached); `oculto-css` hidden by CSS; `tamanho-zero` zero size; `fora-da-pagina` off the page; `fora-da-viewport (role até ele)` outside the viewport ("role até ele" = scroll to it); `ok` visible and receives the click; `coberto-por <tag>#<id>` covered by that element|
|12-14|`#origem`, `#destino` `#source`, `#destination`; `SUCESSO` SUCCESS, prefix of the error that ends the batch; `sucesso` success (regex word `/successful\|sucesso/i`)|

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

## 2. Locate anywhere (shadow DOM + iframes) and return coordinates

- Set `ALVO` (visible text or CSS selector) and `FRAME_W` (width of the "coordinate frame" of the last screenshot).

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

- Click with `computer left_click` and `coordinate: [x, y]` (screenshot first if the page changed).
- Scroll an off-screen element into view with `computer scroll` or `el.scrollIntoView({ block: "center", behavior: "instant" })`, then run again.
- Always set `behavior: "instant"`: with `scroll-behavior: smooth` you measure mid-scroll.
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

- Read one line per field: `label | type | name * = value`. Radios of one group repeat `name`.
- A react-select field shows as `text`, label "Select ...", empty value. Read the chosen value with `[...document.querySelectorAll("[class*=singleValue],[class*=multiValue]")].map(e => e.innerText)`.
- Validate without submitting with `form.checkValidity()`. List invalid fields with `[...form.querySelectorAll(":invalid")].map(e => e.name || e.id)`.

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

```js
window.__log = []; window.__resp = "RESPOSTA"; window.__aceitar = true;
for (const k of ["alert", "confirm", "prompt"]) { window[k] = (...a) => { window.__log.push({ k, msg: a[0] }); return k === "confirm" ? window.__aceitar : k === "prompt" ? window.__resp : undefined; }; }
window.open = (u) => { window.__log.push({ k: "open", url: new URL(String(u), location.href).href }); return null; };
"stubs prontos: ajuste window.__resp/__aceitar, clique e leia window.__log"
```

- Adjust `window.__resp` and `window.__aceitar`, click, then read `window.__log`. Alerts from a right click (`computer right_click`) land there too.
- Set `__aceitar = true` only when accepting is what the user wants (example: "are you sure you want to leave?" in an authorized flow). Set `false` when in doubt: the block ships with `true`.
- For a new tab, read the URL in `__log`, then `navigate`.

## 7. File upload without the OS picker

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

- Test the endpoint with `fetch` in the page console (same origin and cookies) first.

## 9. Infinite scroll

```js
const conta = () => document.querySelectorAll("SELETOR-DO-ITEM").length; let antes = -1, parado = 0;
for (let i = 0; i < 15 && parado < 2; i++) { window.scrollTo(0, document.body.scrollHeight); await new Promise(r => setTimeout(r, 1500)); const n = conta(); parado = n === antes ? parado + 1 : 0; antes = n; }
antes
```

## 10. Extract a table or list as data

- Selector covers a `<table>` and a `div` table with `role=row`.

```js
const linhas = [...document.querySelectorAll("table tr, [role=row]")].map(r => [...r.querySelectorAll("th,td,[role=columnheader],[role=cell]")].map(c => c.innerText.trim()));
const [cab, ...dados] = linhas;
dados.map(l => Object.fromEntries(cab.map((h, i) => [h, l[i]])))  // e.g.: .find(o => o.Name === "Chrome")?.CPU
```

For cards, use: `[...document.querySelectorAll("SELETOR-DO-CARTAO")].map(c => ({ titulo: c.querySelector("h2,h3")?.innerText, link: c.querySelector("a")?.href }))`

## 11. Real visual state (what checkVisibility misses)

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

- Read `coberto-por`: a click there goes to the cited element (overlay, modal, banner). Close it first.

## 12. Coordinates of a selector (cheapest path when the selector is known)

- Check the "coordinate frame" text of the screenshot, then set `FRAME_W`.

```js
const FRAME_W = 800; // width of the "coordinate frame" of the last screenshot (Claude browser pane: 800; Claude in Chrome: innerWidth)
// scroll ONCE (to the 1st selector) and measure all afterwards; measuring one, scrolling, measuring another leaves the 1st coordinate stale
const xy = async (...seletores) => { const els = seletores.map(s => document.querySelector(s)); els[0].scrollIntoView({ block: "center", behavior: "instant" }); await new Promise(r => setTimeout(r, 300)); const k = FRAME_W / innerWidth; return els.map(e => { const r = e.getBoundingClientRect(); return [Math.round((r.x + r.width / 2) * k), Math.round((r.y + r.height / 2) * k)]; }); };
await xy("#origem", "#destino")  // [[x,y],[x,y]]
```

- Run this batch: `screenshot` (scale 0.1) → `left_click` at the coordinate → JS that verifies.

## 13. Read text from iframes and frames (recursive)

- A frameset `<frame>` is not an iframe: `querySelectorAll("iframe")` is empty there.

```js
const ler = (doc, via = "doc") => [...doc.querySelectorAll("frame,iframe")].flatMap(f => { const nome = `${via}>${f.tagName.toLowerCase()}${f.name ? "[" + f.name + "]" : ""}`; try { const d = f.contentDocument; return [{ via: nome, texto: (d.body?.innerText ?? "").trim().slice(0, 300) }, ...ler(d, nome)]; } catch { return [{ via: nome, texto: null, src: f.src.slice(0, 60) }]; } });
ler(document)
```

- Read `texto: null` as: other origin (ad, payment, CAPTCHA). Use screenshot only.
- Skip this snippet for shadow DOM: `get_page_text` already returns that text.

## 14. Repeat until success (inside a batch)

```js
const m = document.querySelector("#flash")?.innerText ?? "";
if (/successful|sucesso/i.test(m)) throw new Error("SUCESSO: " + m.trim());
m.trim()
```

- Run the batch: `[screenshot 0.1, left_click (x,y), JS above] × N`.
- Read the error "SUCESSO: ..." as success. A batch that ends without it had no success.
- Keep the screenshot in each round: a click that navigates needs a new one.
