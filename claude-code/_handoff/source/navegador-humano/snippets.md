# Snippets testados (javascript_tool)

Cole o bloco inteiro em `javascript_tool` (`action: "javascript_exec"`; no Claude in Chrome passe também `tabId`). A última expressão é o retorno. Todos foram testados no painel do Claude (Chromium, 2026-10); os snippets 6, 12 e 13 também no Claude in Chrome.

Regra de ouro: JS serve para LER, esperar e preparar (stubs). Clique e digitação de verdade vão por `computer` (ref ou coordenada), porque muitos sites ignoram `element.click()`.

## 1. Raio-x da página (rodar logo depois de abrir)

Responde em uma chamada: estou bloqueado? tem banner, modal, iframe, shadow DOM, formulário? quais APIs a página chama?

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

Leitura: `bloqueio` não vazio = parar e passar ao usuário. `protecaoNoEnvio` = o envio do formulário tem CAPTCHA invisível; ler e preencher pode, enviar automatizado não.

## 2. Localizar em qualquer lugar (shadow DOM + iframes) e devolver coordenada

`read_page` e `find` NÃO enxergam shadow DOM nem conteúdo de iframe. Este snippet enxerga. Ajuste `ALVO` (texto visível ou seletor CSS) e `FRAME_W` (largura do "coordinate frame" do último screenshot).

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

Depois: `computer left_click` com `coordinate: [x, y]` (tire um screenshot antes se a página mudou desde o último). Elemento fora da tela: role com `computer scroll` ou `el.scrollIntoView({ block: "center", behavior: "instant" })` e rode de novo (sem `behavior: "instant"`, sites com `scroll-behavior: smooth` deixam você medir no meio da rolagem). iframe de outra origem (pagamento, reCAPTCHA): só screenshot + coordenada.

## 3. Mapa do formulário (todos os campos numa chamada)

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

Saída: uma linha por campo, `rótulo | tipo | nome * = valor`. Radios do mesmo grupo repetem `nome`. Campo de react-select aparece como `text` com rótulo "Select ..." e `valor` vazio; o escolhido está em `[...document.querySelectorAll("[class*=singleValue],[class*=multiValue]")].map(e => e.innerText)`. `(desab)` = ainda não habilitado (dependente de outro campo). Para validar sem enviar: `form.checkValidity()` e `[...form.querySelectorAll(":invalid")].map(e => e.name || e.id)`.

## 4. Esperar uma condição (em vez de wait + screenshot em loop)

```js
const ate = (cond, ms = 20000, passo = 250) => new Promise(ok => { const t0 = Date.now(); const i = setInterval(() => { const v = cond(); if (v || Date.now() - t0 > ms) { clearInterval(i); ok(v || null); } }, passo); });
await ate(() => document.querySelector(".bg-success")?.innerText)
```

Aguenta 15 s ou mais numa chamada. Ação com timing crítico (parar em 75%, clicar quando aparecer): faça a ação dentro do mesmo JS, não em outra chamada.

## 5. Elemento parou de mexer (modal animado, menu deslizando)

```js
const el = document.querySelector(".modal"); const pos = () => JSON.stringify(el.getBoundingClientRect());
let a = pos(); for (let i = 0; i < 20; i++) { await new Promise(r => setTimeout(r, 150)); const b = pos(); if (a === b) break; a = b; } a
```

## 6. Diálogos nativos (alert/confirm/prompt) e nova aba

No painel, `confirm`/`prompt` são cancelados sem aparecer e novas abas abertas pela página são bloqueadas. No Claude in Chrome, um diálogo nativo congela a aba (timeout de 30 s, `Escape` não resolve, só fechando a aba): lá o stub é obrigatório antes de clicar em qualquer coisa que possa abrir diálogo.

```js
window.__log = []; window.__resp = "RESPOSTA"; window.__aceitar = true;
for (const k of ["alert", "confirm", "prompt"]) { window[k] = (...a) => { window.__log.push({ k, msg: a[0] }); return k === "confirm" ? window.__aceitar : k === "prompt" ? window.__resp : undefined; }; }
window.open = (u) => { window.__log.push({ k: "open", url: new URL(String(u), location.href).href }); return null; };
"stubs prontos: ajuste window.__resp/__aceitar, clique e leia window.__log"
```

- Os stubs somem quando a página navega ou recarrega: instale de novo depois de cada `navigate`.
- Alertas disparados por clique direito (`computer right_click`) também caem em `__log`.
- `__aceitar = true` só quando aceitar é o que o usuário quer (ex.: "tem certeza que quer sair?" num fluxo autorizado). Em dúvida, `false`.
- Nova aba: leia a URL em `__log` e use `navigate`. Link com `target=_blank`: leia o `href` e navegue direto.

## 7. Upload de arquivo sem o seletor do sistema

Nunca clique em "Escolher arquivo"/"Browse": abre o seletor do SO, que nenhuma ferramenta opera. No Claude in Chrome existe a ferramenta `file_upload`. No painel:

```js
const inp = document.querySelector("input[type=file]");
const bytes = await (await fetch("URL-DO-ARQUIVO-ACESSIVEL-PELA-PAGINA")).blob(); // ou new Blob(["conteúdo"])
const dt = new DataTransfer(); dt.items.add(new File([bytes], "curriculo.pdf", { type: "application/pdf" }));
inp.files = dt.files; inp.dispatchEvent(new Event("input", { bubbles: true })); inp.dispatchEvent(new Event("change", { bubbles: true }));
inp.files[0]?.name
```

## 8. Achar a API que a página usa (pular a UI)

```js
const achados = new Set();
for (const s of [...document.scripts].map(s => s.src).filter(Boolean)) {
  try { const t = await (await fetch(s)).text(); for (const m of t.matchAll(/["'`](\/(?:api|v\d|graphql|apply|search)[^"'`\s]{2,80})["'`]/gi)) achados.add(m[1]); } catch {}
}
[...achados].slice(0, 40)
```

Combine com `read_network_requests` (filtre por `api`) depois de usar a busca uma vez na UI. Teste o endpoint com `fetch` no console da página (mesma origem e cookies) antes de construir em cima.

## 9. Scroll infinito

```js
const conta = () => document.querySelectorAll("SELETOR-DO-ITEM").length; let antes = -1, parado = 0;
for (let i = 0; i < 15 && parado < 2; i++) { window.scrollTo(0, document.body.scrollHeight); await new Promise(r => setTimeout(r, 1500)); const n = conta(); parado = n === antes ? parado + 1 : 0; antes = n; }
antes
```

Menos de 1,5 s por volta não deu tempo de carregar no teste. Se nada carrega, use `computer scroll` (roda do mouse de verdade) ou procure a API (snippet 8).

## 10. Extrair tabela ou lista como dados

Tabela `<table>` ou feita de `div` com `role=row` (colunas mudam de ordem: ache pelo cabeçalho, nunca pelo índice):

```js
const linhas = [...document.querySelectorAll("table tr, [role=row]")].map(r => [...r.querySelectorAll("th,td,[role=columnheader],[role=cell]")].map(c => c.innerText.trim()));
const [cab, ...dados] = linhas;
dados.map(l => Object.fromEntries(cab.map((h, i) => [h, l[i]])))  // ex.: .find(o => o.Name === "Chrome")?.CPU
```

Cartões: `[...document.querySelectorAll("SELETOR-DO-CARTAO")].map(c => ({ titulo: c.querySelector("h2,h3")?.innerText, link: c.querySelector("a")?.href }))`

## 11. Estado visual real (o que `checkVisibility` não pega)

`checkVisibility()` devolve `true` para elemento coberto por outro, de largura zero ou posicionado fora da página. Esta função diz o motivo e quem recebe o clique:

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

`coberto-por`: um clique ali vai para o elemento citado (overlay, modal, banner). Feche-o antes.

## 12. Coordenada de um seletor (o caminho mais barato quando o seletor é conhecido)

```js
const FRAME_W = 800; // largura do "coordinate frame" do último screenshot (painel do Claude: 800; Claude in Chrome: innerWidth)
// rola UMA vez (até o 1º seletor) e mede todos depois; medir um, rolar, medir outro deixa a 1ª coordenada velha
const xy = async (...seletores) => { const els = seletores.map(s => document.querySelector(s)); els[0].scrollIntoView({ block: "center", behavior: "instant" }); await new Promise(r => setTimeout(r, 300)); const k = FRAME_W / innerWidth; return els.map(e => { const r = e.getBoundingClientRect(); return [Math.round((r.x + r.width / 2) * k), Math.round((r.y + r.height / 2) * k)]; }); };
await xy("#origem", "#destino")  // [[x,y],[x,y]]
```

Uma chamada para `xy()`, outra para o clique: o retorno de um passo do batch não alimenta o seguinte. Se a página mudou desde o último screenshot, o clique pede um screenshot antes; faça um batch `screenshot` (scale 0.1) → `left_click` na coordenada → JS que confere. No painel o frame tem 800 de largura; no Claude in Chrome é o próprio viewport (`FRAME_W = innerWidth`). Confira sempre no texto "coordinate frame" do screenshot. Recalcule depois de qualquer espera, carregamento ou campo que habilita: o layout muda (no teste o campo subiu 48 px ao habilitar).

## 13. Ler texto de iframes e frames (recursivo)

Frameset (`<frame>`) não é iframe: `querySelectorAll("iframe")` volta vazio nele.

```js
const ler = (doc, via = "doc") => [...doc.querySelectorAll("frame,iframe")].flatMap(f => { const nome = `${via}>${f.tagName.toLowerCase()}${f.name ? "[" + f.name + "]" : ""}`; try { const d = f.contentDocument; return [{ via: nome, texto: (d.body?.innerText ?? "").trim().slice(0, 300) }, ...ler(d, nome)]; } catch { return [{ via: nome, texto: null, src: f.src.slice(0, 60) }]; } });
ler(document)
```

`texto: null` = outra origem (anúncio, pagamento, CAPTCHA): só screenshot. Shadow DOM não precisa disto: `document.body.innerText` e `get_page_text` já trazem o texto (inclusive de slots).

## 14. Repetir até dar certo (dentro de um batch)

O batch para no primeiro passo que falha. Use isso: depois de cada tentativa, um JS que lança erro quando vê o sucesso.

```js
const m = document.querySelector("#flash")?.innerText ?? "";
if (/successful|sucesso/i.test(m)) throw new Error("SUCESSO: " + m.trim());
m.trim()
```

Batch: `[screenshot 0.1, left_click (x,y), JS acima] × N`. O erro "SUCESSO: ..." no resultado é o fim feliz; se terminar sem ele, nenhuma tentativa deu certo. O screenshot em cada volta é porque um clique que navega exige screenshot novo antes da próxima coordenada.
