# Page snippets for the Codex browser

Operating rules: [SKILL.md](../SKILL.md). Per-site notes: [sites.md](sites.md).

Contents: 1 x-ray · 2 locate anywhere · 3 form map · 4 wait for a condition · 5 element stopped moving · 6 dialogs and new tabs · 7 file upload · 8 the page's API · 9 infinite scroll · 10 table or list as data · 11 real visual state · 12 centers for drag and drop · 13 frames text · 14 repeat until success

## Usage

- Run these in the Node REPL `js` tool where your plugin binding `tab` lives (and `browser` for tab lists). Page code goes inside `tab.playwright.evaluate(fn, arg)`, which runs in a read-only page scope: it reads, measures and waits, but cannot click, type, scroll or change the page. Actions use the plugin's locator, `tab.ax` or `tab.cua` methods.
- Print results with `nodeRepl.write(JSON.stringify(result, null, 1))`.
- Keep the code unchanged except placeholders: `SELETOR-DO-ITEM` (item selector, 9), `SELETOR-DO-CARTAO` (card selector, 10), `SELETOR` (target selector, 11), `#origem` and `#destino` (source and target, 12).
- The page logic was tested in another agent's Chromium browser (2026-10); the Codex wrappers follow the plugin API and are not yet field-tested. If a read fails in the read-only scope, read the same data with `domSnapshot()` or a locator method instead.

## Output token glossary

Portuguese tokens are returned as written; do not translate them in code.

| Snippet | Token and meaning |
|---|---|
| 1 | `titulo` title; `bloqueio` detected blocks (not empty = stop); `protecaoNoEnvio` submit protection (reCAPTCHA, hCaptcha or Turnstile script in the HTML; `true` = invisible CAPTCHA on submit: fill the form, never submit it by automation); `modais` modals; `formularios` field count per form; in `iframes`, `mesma-origem` same origin (readable), `outra-origem` cross-origin (unreadable) |
| 1 | `bloqueio` values: `recaptcha-visivel` visible reCAPTCHA; `hcaptcha-visivel` visible hCaptcha; `muro-de-login` login wall; `texto-verificacao` verification text; `google-sorry` Google "unusual traffic" page |
| 1 | `cookies` regex stems `aceit`, `rejeit`, `recus`, `não aceito`, `necess`, `configur`, `prosseguir`, `concordo` = accept, reject, refuse, I do not accept, necessary, configure, proceed, I agree (Portuguese only: `rejeit` does not match "reject") |
| 2 | `ALVO` target; `PULAR` skip (tags the text search ignores); `varrer` sweep (recursive walk); `via` path (`doc`, then `>shadow:<tag>`, `>iframe` or `>frame`); `x`, `y` element center in CSS viewport pixels; `iframeOutraOrigem` cross-origin iframe `src` |
| 3 | `rotulo` label; `obrig` required (` *` after the name); `desab`, `(desab)` disabled (not enabled yet: it depends on another field) |
| 4 | `ate` until (returns the condition value, or `null` on timeout) |
| 11 | `fora-do-DOM` out of the DOM (null or detached); `oculto-css` hidden by CSS; `tamanho-zero` zero size; `fora-da-pagina` off the page; `fora-da-viewport (role até ele)` outside the viewport ("role até ele" = scroll to it); `ok` visible and receives the click; `coberto-por <tag>#<id>` covered by that element |
| 12-14 | `#origem`, `#destino` `#source`, `#destination`; `antes` before (last count); `parado` stalled rounds; `sucesso` success (regex word `/successful\|sucesso/i`) |

## 1. Page x-ray (run right after opening)

```js
const xray = await tab.playwright.evaluate(() => {
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
  return {
    url: location.href, titulo: document.title, viewport: [innerWidth, innerHeight],
    bloqueio, protecaoNoEnvio,
    cookies: botoes.map(b => b.innerText.trim()).filter(t => /cookie|aceit|rejeit|recus|não aceito|necess|configur|prosseguir|concordo/i.test(t)).slice(0, 8),
    modais: [...document.querySelectorAll('[role=dialog],[aria-modal=true],.modal,[class*=Modal],[class*=overlay]')].filter(vis).map(m => m.innerText.slice(0, 80)).slice(0, 3),
    iframes: [...document.querySelectorAll("iframe,frame")].filter(vis).map(f => { try { return f.contentDocument ? "mesma-origem " + f.src.slice(0, 60) : "outra-origem " + f.src.slice(0, 60); } catch { return "outra-origem " + f.src.slice(0, 60); } }),
    shadowHosts: [...document.querySelectorAll("*")].filter(e => e.shadowRoot).map(e => e.tagName.toLowerCase()).slice(0, 5),
    formularios: [...document.forms].map(f => f.querySelectorAll("input:not([type=hidden]),select,textarea").length),
    apis: performance.getEntriesByType("resource").map(r => r.name).filter(n => /\/api\/|graphql|\.json(\?|$)/i.test(n) && !/google|gtm|doubleclick|facebook|hotjar|clarity|analytics|sentry|unleash/i.test(n)).slice(-8),
  };
});
nodeRepl.write(JSON.stringify(xray, null, 1));
```

## 2. Locate anywhere (shadow DOM + iframes)

Try locators first; they pierce open shadow DOM. Use this when a locator finds nothing and you need to know where the text lives, or a coordinate for `tab.cua`.

```js
const achados = await tab.playwright.evaluate((ALVO) => {
  const norm = s => (s || "").replace(/\s+/g, " ").trim().toLowerCase(), alvo = norm(ALVO), out = [];
  const PULAR = new Set(["SCRIPT", "STYLE", "NOSCRIPT", "TEMPLATE", "HEAD", "IFRAME", "FRAME"]);
  const visivel = e => !!e.checkVisibility?.({ checkOpacity: true, checkVisibilityCSS: true }) && e.getBoundingClientRect().width > 0;
  const textoDe = e => norm(e.innerText || e.value || e.getAttribute("aria-label") || e.getAttribute("placeholder") || e.title);
  function varrer(raiz, ox, oy, via) {
    let porSeletor = []; try { porSeletor = [...raiz.querySelectorAll(ALVO)]; } catch {}
    const todos = [...raiz.querySelectorAll("*")];
    const porTexto = porSeletor.length ? [] : todos.filter(e => !PULAR.has(e.tagName) && !e.shadowRoot && textoDe(e).includes(alvo) && ![...e.children].some(c => textoDe(c).includes(alvo)));
    for (const e of [...porSeletor, ...porTexto]) { const r = e.getBoundingClientRect(); out.push({ via, tag: e.tagName.toLowerCase(), texto: textoDe(e).slice(0, 60), visivel: visivel(e), desabilitado: !!e.disabled, x: Math.round(ox + r.x + r.width / 2), y: Math.round(oy + r.y + r.height / 2) }); }
    for (const e of todos) {
      if (e.shadowRoot) varrer(e.shadowRoot, ox, oy, via + ">shadow:" + e.tagName.toLowerCase());
      if (e.tagName === "IFRAME" || e.tagName === "FRAME") { const r = e.getBoundingClientRect(); try { varrer(e.contentDocument, ox + r.x + e.clientLeft, oy + r.y + e.clientTop, via + ">" + e.tagName.toLowerCase()); } catch { out.push({ via, iframeOutraOrigem: e.src.slice(0, 80) }); } }
    }
  }
  varrer(document, 0, 0, "doc");
  return out.sort((a, b) => (b.visivel ?? 0) - (a.visivel ?? 0)).slice(0, 10);
}, "Click me");
nodeRepl.write(JSON.stringify(achados));
```

- `x` and `y` are CSS viewport pixels. `tab.cua` takes screenshot coordinates: scale by screenshot width ÷ `innerWidth` when they differ, and confirm the target with `tab.playwright.elementInfo({ x, y })` before clicking.
- An element outside the viewport must be scrolled into view first (`tab.cua.scroll`), then measured again.
- For a cross-origin iframe (payment, reCAPTCHA), only a screenshot plus coordinates works.

## 3. Form map (all fields in one call)

```js
const campos = await tab.playwright.evaluate(() => {
  const limpo = s => (s || "").replace(/\s+/g, " ").trim().slice(0, 80);
  const rotulo = e => {
    const direto = limpo(e.labels?.[0]?.innerText) || limpo(e.getAttribute("aria-label")) || limpo(e.getAttribute("aria-labelledby")?.split(" ").map(id => document.getElementById(id)?.innerText).join(" "));
    if (direto) return direto;
    for (let p = e.parentElement, i = 0; p && i < 8; p = p.parentElement, i++) { const l = [...p.querySelectorAll("label,legend,h3,h4,[class*=label],[class*=Label],[class*=placeholder]")].find(l => !l.contains(e) && limpo(l.innerText)); if (l) return limpo(l.innerText); }
    return limpo(e.placeholder || e.name);
  };
  return [...document.querySelectorAll("input:not([type=hidden]),select,textarea,[contenteditable=true],[role=combobox],[role=radiogroup]")]
    .filter(e => e.checkVisibility?.() || e.type === "radio" || e.type === "checkbox" || e.type === "file")
    .map(e => ({ rotulo: rotulo(e), tipo: e.type || e.getAttribute("role"), nome: e.name || e.id, obrig: e.required || e.getAttribute("aria-required") === "true", valor: e.type === "radio" || e.type === "checkbox" ? e.checked : (e.value ?? e.innerText)?.slice?.(0, 40), desab: e.disabled, opcoes: e.tagName === "SELECT" ? [...e.options].map(o => o.text).slice(0, 15).join("/") : "" }))
    .map(o => `${o.rotulo} | ${o.tipo} | ${o.nome}${o.obrig ? " *" : ""}${o.desab ? " (desab)" : ""} = ${o.valor}${o.opcoes ? " [" + o.opcoes + "]" : ""}`);
});
nodeRepl.write(campos.join("\n"));
```

- One line per field: `label | type | name * = value`. Radios of one group repeat `name`.
- A react-select field shows as `text`, label "Select ...", empty value. Read the chosen value with `[...document.querySelectorAll("[class*=singleValue],[class*=multiValue]")].map(e => e.innerText)`.
- Validate without submitting: `form.checkValidity()`, and list invalid fields with `[...form.querySelectorAll(":invalid")].map(e => e.name || e.id)`.

## 4. Wait for a condition

Prefer `locator.waitFor({ state: "visible", timeoutMs })` or `waitForURL` when a selector or URL marks the condition. Otherwise poll a read:

```js
const ate = async (cond, ms = 20000, passo = 250) => {
  const t0 = Date.now();
  for (;;) {
    const v = await tab.playwright.evaluate(cond);
    if (v || Date.now() - t0 > ms) return v || null;
    await tab.playwright.waitForTimeout(passo);
  }
};
nodeRepl.write(String(await ate(() => document.querySelector(".bg-success")?.innerText)));
```

## 5. Element stopped moving (animated modal, sliding menu)

```js
const parado = await tab.playwright.evaluate(async () => {
  const el = document.querySelector(".modal"); const pos = () => JSON.stringify(el.getBoundingClientRect());
  let a = pos(); for (let i = 0; i < 20; i++) { await new Promise(r => setTimeout(r, 150)); const b = pos(); if (a === b) break; a = b; }
  return a;
});
```

## 6. Native dialogs and new tabs

```js
const d = await tab.getJsDialog();   // undefined when no dialog is open
if (d) {
  nodeRepl.write(d.type);
  if (d.type === "prompt") await d.accept("RESPOSTA"); else await d.dismiss();
}
```

- Dismiss by default. Accept a `confirm` only when that outcome is what the user wants (for example "are you sure you want to leave?" inside an authorized flow), and answer a `prompt` only with text the user supplied.
- If an action hangs, a dialog is the usual cause: check `getJsDialog()` before retrying.
- New tab from `target=_blank` or `window.open`: `await browser.tabs.list()` shows it; read it, close it, and return. Or read the link's `href` and `goto` it in the current tab.

## 7. File upload without the OS picker

```js
const chooserPromise = tab.playwright.waitForEvent("filechooser", { timeoutMs: 10000 });
await tab.playwright.locator('input[type="file"]').click();
const chooser = await chooserPromise;
await chooser.setFiles(["C:/absolute/path/curriculo.pdf"]);
```

Start waiting for the chooser before the click, use absolute paths, and verify the uploaded name with `evaluate(() => document.querySelector("input[type=file]").files[0]?.name)`.

## 8. Find the API the page uses (skip the UI)

First read the x-ray `apis`. If they are empty, list the page's scripts and search them from the shell:

```js
const scripts = await tab.playwright.evaluate(() => [...document.scripts].map(s => s.src).filter(Boolean));
nodeRepl.write(scripts.join("\n"));
```

```bash
curl -s "<script-src>" | grep -oE "[\"'\`](/(api|v[0-9]+|graphql|apply|search)[^\"'\`[:space:]]{2,80})" | sort -u | head -40
```

Test a candidate endpoint with `curl` (public) before building on it. If it needs the page's cookies, open the endpoint URL in the tab and read its text.

## 9. Infinite scroll

```js
const conta = () => tab.playwright.evaluate(() => document.querySelectorAll("SELETOR-DO-ITEM").length);
const [w, h] = await tab.playwright.evaluate(() => [innerWidth, innerHeight]);
let antes = -1, parado = 0;
for (let i = 0; i < 15 && parado < 2; i++) {
  await tab.cua.scroll({ x: Math.round(w / 2), y: Math.round(h / 2), scrollX: 0, scrollY: 3000 });
  await tab.playwright.waitForTimeout(1500);
  const n = await conta(); parado = n === antes ? parado + 1 : 0; antes = n;
}
nodeRepl.write(String(antes));
```

## 10. Extract a table or list as data

The selector covers a `<table>` and a `div` table with `role=row`.

```js
const linhas = await tab.playwright.evaluate(() => {
  const l = [...document.querySelectorAll("table tr, [role=row]")].map(r => [...r.querySelectorAll("th,td,[role=columnheader],[role=cell]")].map(c => c.innerText.trim()));
  const [cab, ...dados] = l;
  return dados.map(d => Object.fromEntries(cab.map((h, i) => [h, d[i]])));   // e.g. .find(o => o.Name === "Chrome")?.CPU
});
```

For cards: `[...document.querySelectorAll("SELETOR-DO-CARTAO")].map(c => ({ titulo: c.querySelector("h2,h3")?.innerText, link: c.querySelector("a")?.href }))`.

## 11. Real visual state (what checkVisibility misses)

```js
const estado = await tab.playwright.evaluate((sel) => {
  const e = document.querySelector(sel);
  if (!e?.isConnected) return "fora-do-DOM";
  if (!e.checkVisibility({ checkOpacity: true, checkVisibilityCSS: true })) return "oculto-css";
  const r = e.getBoundingClientRect();
  if (r.width < 1 || r.height < 1) return "tamanho-zero";
  if (r.bottom + scrollY <= 0 || r.right + scrollX <= 0) return "fora-da-pagina";
  if (r.bottom <= 0 || r.top >= innerHeight || r.right <= 0 || r.left >= innerWidth) return "fora-da-viewport (role até ele)";
  const t = document.elementFromPoint(r.x + r.width / 2, r.y + r.height / 2);
  return t === e || e.contains(t) ? "ok" : `coberto-por ${t?.tagName.toLowerCase()}${t?.id ? "#" + t.id : ""}`;
}, "SELETOR");
nodeRepl.write(estado);
```

`coberto-por` means a click there goes to the named element (overlay, modal, banner): close it first.

## 12. Centers of two elements (drag and drop)

Scroll the source into view first, then measure both in one call so neither coordinate goes stale.

```js
const [de, para] = await tab.playwright.evaluate(([a, b]) => [a, b].map(s => { const r = document.querySelector(s).getBoundingClientRect(); return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) }; }), ["#origem", "#destino"]);
await tab.cua.drag({ path: [de, para] });
```

Values are CSS viewport pixels; scale to screenshot coordinates if they differ (snippet 2). Verify the new order after the drag.

## 13. Read text from iframes and frames (recursive)

A frameset `<frame>` is not an iframe, so `querySelectorAll("iframe")` is empty there.

```js
const frames = await tab.playwright.evaluate(() => {
  const ler = (doc, via = "doc") => [...doc.querySelectorAll("frame,iframe")].flatMap(f => { const nome = `${via}>${f.tagName.toLowerCase()}${f.name ? "[" + f.name + "]" : ""}`; try { const d = f.contentDocument; return [{ via: nome, texto: (d.body?.innerText ?? "").trim().slice(0, 300) }, ...ler(d, nome)]; } catch { return [{ via: nome, texto: null, src: f.src.slice(0, 60) }]; } });
  return ler(document);
});
```

`texto: null` means another origin (ad, payment, CAPTCHA): use a screenshot only.

## 14. Repeat until success

```js
let m = "";
for (let i = 0; i < 10; i++) {
  await tab.playwright.locator("#botao").click();
  m = await tab.playwright.evaluate(() => document.querySelector("#flash")?.innerText?.trim() ?? "");
  if (/successful|sucesso/i.test(m)) break;
}
nodeRepl.write(m);
```

Keep the loop bounded, and stop early on a block or dialog.
