---
name: human-browser
description: Do web tasks with the fewest actions and recover from what breaks, on top of Codex's Browser or Chrome plugin. Use to scrape or read sites, fill forms, run multi-step flows or find the API a page calls; covers shadow DOM, iframes, dialogs, uploads, autocomplete, infinite scroll, CAPTCHA and login stops, and Brazilian sites and public APIs (CNPJ, Gupy, PTAX).
metadata:
  translated-from: "pt-BR (navegador-humano)"
  tested: "Traps and stop rules validated on 53 tasks in 5 blind retests in another agent's browser (2026-10-20); the Codex API mapping in this version is not yet field-tested"
  version: "1.0-codex"
---

# Human Browser

Finish a web task on the first attempt with few actions and few screenshots, without breaking the stop rules. This skill does not control the browser: the Browser plugin (in-app browser) and the Chrome plugin own setup, browser selection, the `browser-client` API (`tab.playwright`, `tab.ax`, `tab.cua`) and the confirmation policy, so follow them for all of that. This skill adds the decisions around them: when not to open a browser, how to read and act cheaply, traps seen on real sites, stricter stop rules, and per-site notes.

The user's explicit instructions take precedence over this skill. The skill text is compact controlled English for precise reading; report to the user in plain prose.

- [references/snippets.md](references/snippets.md): tested page scripts for `tab.playwright.evaluate` and REPL loops. Read it when a step below names a snippet.
- [references/sites.md](references/sites.md): notes for specific sites, Brazilian job boards, ATS forms and public APIs. Read it when the task names one of them.

## Choose the route

1. **Data without UI.** Prefer a JSON API (public, or the one the page itself calls) over HTML, and HTML over clicking through the UI. Find the page's API once (x-ray `apis`, snippet 8) and test the endpoint. Use web search for general research instead of a search engine inside the browser. For exact data (a number, a quote, a full JSON), read it raw with `curl` or from the DOM; a summarizing fetch shortens and paraphrases. Public APIs that avoid CAPTCHA forms (CNPJ, Wikipedia, Gupy) are in sites.md. To read many pages, `browser.tabs.content({ urls, contentType: "text" })` loads them in background tabs without moving the selected tab.
2. **Read** the cheapest way that answers the question: visible text (`tab.playwright.locator("body").innerText()`), then the accessibility state (`tab.ax.write()`), then `tab.playwright.domSnapshot()` (it expands same-origin iframe bodies), then a read-only `evaluate` for a precise question. Take a screenshot only to verify something visual.
3. **Act** through semantic locators first: `getByRole`, `getByLabel`, `getByText`, `locator(css)`. They pierce open shadow DOM; use `frameLocator` for iframes. Use `fill` for a simple field and `pressSequentially` when the site reacts to keys (autocomplete, masks, rich editors). Use coordinates (`tab.cua.*`) only for canvas, cross-origin iframes, or after locators fail. `evaluate` is read-only, so it reads, measures and waits but never clicks or edits.
4. **Verify** after every action that matters by reading state: `value`, `checked`, the URL, visible text, the focused element. "Clicked" is not "worked". One authoritative signal (selected option, toast, URL parameter) settles a fact.
5. **Repeat until success** inside one bounded REPL loop instead of many separate calls (snippet 14).

## Per-page cycle

1. Navigate with `tab.goto(url)`. Do not `goto` the URL the tab already shows; use `tab.reload()` when a reload is intended.
2. Check that `await tab.url()` is the requested page. A redirect to the home page, a login page or `account-verification` is a session problem or a block, not the page.
3. Run the x-ray (snippet 1) in one `evaluate`: anti-bot blocks, cookie banners, modals, iframes, shadow DOM, forms and APIs.
4. On a block, stop (Stop rules). Reject a cookie banner that is in the way and close a modal.
5. Read the page or map the form (snippet 3) and plan all actions.
6. Act, verify, and move to the next step. Run the x-ray again after each new step, because blocks can appear after the first interaction.

## Stop rules

The plugin's confirmation policy applies. These limits are stricter, and they win where the two differ:

- **CAPTCHA or anti-bot check.** Stop on any x-ray `bloqueio`, "não sou um robô" ("I'm not a robot"), Turnstile, "Just a moment", "Verificação adicional" ("Additional verification") or `account-verification`. Do not solve or bypass it, even with confirmation, and do not change the user agent or use stealth tools or solver services. Tell the user where the block is and what to do. In recurring automation, exclude the site or switch to assisted mode: the agent prepares, the human submits.
- **`protecaoNoEnvio: true`** (invisible CAPTCHA on submit): fill the form and leave the submit to the human.
- **Login and passwords.** Open the login page and let the user sign in. Never type a password or click "Entrar" ("Sign in") with a browser-filled password. Stop on HTTP Basic Auth (a native dialog or `usuario:senha@` in the URL), even with a public playground password.
- **Browser permissions** (location, camera, microphone, notifications, clipboard): never grant them. Before a click that triggers one, check `navigator.permissions.query({ name: "geolocation" })` (or the permission's name) in `evaluate`; report `denied` or `prompt`, and ask the user to allow it only if they want that.
- **Downloads.** List names and links without clicking (`[...document.querySelectorAll("a[download], a[href$='.pdf']")]`). Download only after the user says yes to the file's name, origin and size.
- **Government documents and financial data** (CPF, RG, card, bank account): never fill them; hand that step to the user. A public API lookup of company data (CNPJ) is a read and is allowed.

## Traps seen on real sites

### Finding the element

| Symptom | Action |
|---|---|
| A visible control is not found by locators | Closed shadow root or a cross-origin iframe. Open shadow DOM is pierced by locators; same-origin iframes need `frameLocator`. For cross-origin frames (payment, reCAPTCHA), use a screenshot and coordinates |
| A locator matches, but the click fails or the text "appeared" without being on screen | Hidden element (`display:none`, a search box collapsed behind an icon in the narrow layout). Check with snippet 11, then click the icon or button that reveals it |
| A label locator returns the `<label>` and the select does not change | Target the `<select>` itself (`getByRole("combobox")` or `locator("select")`) and call `selectOption` |
| `checkVisibility()` says visible but the click does not land | It ignores covered, zero-size and off-page elements. Snippet 11 reports `coberto-por X` (covered by X), `tamanho-zero` (zero size) or `fora-da-pagina` (off the page) |
| Text with `&nbsp;` does not match | Normalize with `/\s+/g` in JS (covers U+00A0); never use XPath `text()=` |

### Clicking

| Symptom | Action |
|---|---|
| A coordinate click lands in the wrong place | `tab.cua` takes screenshot coordinates. Confirm the target with `tab.playwright.elementInfo({ x, y })`, or scale CSS pixels by screenshot width ÷ `innerWidth` |
| A coordinate that was right goes wrong after a wait | The layout moved (a field enabled, a banner closed, content loaded; one field moved 48 px on enable in testing). Re-measure after every wait, or click by locator |
| A click on a hover menu gets lost | Hover recreates the element. Hover with `tab.cua.move`, wait 0.5 s, then click |
| Cascading submenu (hover inside hover) | Hover the parent, wait 600 ms, measure the child, hover the child; one level per call. A hidden item has empty `innerText`, so match on `textContent` |
| Drag and drop (sortable list, drop zone) | Bring the source into view, measure source and target centers in one `evaluate` (snippet 12), then `tab.cua.drag({ path: [from, to] })` and verify. "Above X" means the upper half of X. Worked on HTML5, react-sortable and jQuery UI |
| A click on a modal that is still opening misses | Entry animation: wait until it stops moving (snippet 5), then click |
| A checked filter does not change the list | Many filters apply only after "Aplicar" or "Filtrar" ("Apply", "Filter"). Find that button and check the URL or list afterwards |
| Clicking a column header does not sort | Verify the order after each click. After 2 clicks with no change while `elementFromPoint` is the `th`, the site does not sort: sort the extracted data yourself (snippet 10) |

### Typing and forms

| Symptom | Action |
|---|---|
| `fill` times out on a field | The field is disabled until another field is set. Fill the dependency, wait for `isEnabled()`, then verify the value |
| Autocomplete does not filter | Use `pressSequentially` and wait 0.5-1 s. If nothing filters, press `Backspace` and retype the last letter. If the option is outside the accessibility tree, press `ArrowDown` then `Enter` |
| `Enter` in a filled form field | Implicit submission can send the form. Press `Enter` only in react-select, autocompletes and library date pickers (react-datepicker and similar), and afterwards check that no confirmation modal or new page appeared |
| "Escolher arquivo" ("Choose file") button | It opens the OS picker, which no tool operates. Use the plugin's file-chooser flow (snippet 7) |

### Windows, dialogs and frames

| Symptom | Action |
|---|---|
| An action hangs or `alert`/`confirm`/`prompt` appeared | Call `tab.getJsDialog()` and dismiss by default. Accept only when that outcome is what the user wants, for example "leave this page?" inside an authorized flow (snippet 6) |
| A link or `window.open` opened a new tab | Find it in `browser.tabs.list()`, read it, close it and return; or read the link's `href` and `goto` it in the current tab |
| Iframe or frame text is missing | `domSnapshot()` expands iframe bodies; for a frameset `<frame>`, use snippet 13 |
| An "exit intent" modal does not appear | Usually leave it alone. The read-only `evaluate` cannot dispatch the `mouseleave` event that triggers it |

### Reading and waiting

| Symptom | Action |
|---|---|
| Waiting for something slow (AJAX, SPA, 15 s) | `locator.waitFor({ state: "visible" })`, `waitForURL`, or the polling loop in snippet 4. Never alternate fixed waits and screenshots |
| An action must happen at an exact moment | Poll in the REPL and act on the same iteration the condition holds (for example, stop at 75%) |
| Text drawn in `<canvas>` | It is not in the DOM. Search the inline scripts (one-liner below) or read a screenshot |
| HTTP status | Current page: `performance.getEntriesByType("navigation")[0].responseStatus` in `evaluate`. Another URL: `curl -sI <url>` |
| Infinite scroll does not load | Each round needs at least 1.5 s (less did not load in testing). Use snippet 9, or better, find the API (snippet 8) |
| A table does not come out of `table tr` | It is built from `div role=row`. Snippet 10 indexes columns by header, never by position |

```js
[...document.scripts].map(s => s.textContent.match(/(fill|stroke)Text\([^)]*\)/g)).filter(Boolean).flat()
```

### Network and blocks

| Symptom | Action |
|---|---|
| A search URL ignores the city or filter | The parameter is an internal ID. Search once through the UI and copy the resulting URL or API call |
| `curl` gets 403 | Cloudflare refuses HTTP clients. Open the site in the browser; if the browser also gets the challenge, it is a block, so stop |
| Verification appears only after the first search | Blocks can come after the first interaction; run the x-ray at every new step |

## Common components

- **Cookie banner:** ignore it when it does not block, since page text reads underneath it. When it blocks, click "Rejeitar" ("Reject"), "Recusar" ("Refuse"), "Somente necessários" ("Only necessary") or "Não aceito nenhum" ("I accept none"), sometimes inside "Saiba mais" ("Learn more") or "Configurar" ("Configure"). Ask the user before accepting cookies or terms.
- **Native select:** `selectOption` with the option's text or `value`.
- **react-select or custom combobox:** click the field, type, wait 0.5 s, press `Enter`. The first option is highlighted, so `ArrowDown` ×N selects option N+1. In multi-select the menu stays open: type + `Enter` per option. A dependent field enables afterwards; locate it again.
- **Date picker:** for `type=date`, `fill` with `YYYY-MM-DD` (`type=time`: `HH:MM`). For a library picker (react-datepicker and similar), click, select all, type in the displayed format (for example "February 15, 2003 2:30 PM"), press `Enter`, verify the `value`, and check that no confirmation modal or page appeared.
- **Slider (`input type=range`):** focus it (click near it or Tab), press `ArrowLeft` or `ArrowRight` to the value, and verify both `value` and the displayed number.
- **Masked input (phone, CEP = Brazilian postal code):** type only the digits and let the mask format them; verify the value.
- **Styled radio or checkbox:** `check()` or `setChecked()` on the input or its label, then verify `.checked`.
- **Rich editor (TinyMCE, contenteditable in an iframe):** click inside the editor body, select all, type, and verify through the iframe's `innerText` or the editor API.
- **Tooltip:** hover the target with `tab.cua.move`, wait 0.5 s, then read `[role=tooltip]` or the new text.
- **Modal:** the close button can be a `<p>`, a `<span>` or "×"; find it by the text "Fechar" or "Close". Prefer it to `Escape`, which sometimes opens something else (on Catho, the plans page).
- **Pagination vs. infinite scroll:** look for `aria-label` "Página N" ("Page N") or "Próxima" ("Next") before scrolling. The API usually takes `limit`, `offset` or `page`.
- **Multi-step flows:** per step, map the form (snippet 3), fill it, run `form.checkValidity()`, advance, and wait for the next step's text (snippet 4). Treat modals such as "perguntas opcionais não respondidas" ("optional questions unanswered") as a step; they appear after "Continuar" ("Continue").

## Unattended robots (standalone Playwright)

Inside a Codex browser session, Playwright means the plugin's `tab.playwright` API. When the user wants a recurring robot that runs on its own, write a standalone Playwright script:

- Use `chromium.launchPersistentContext(perfil, { channel: "chrome", headless, locale: "pt-BR" })`. The profile (`perfil`) keeps the session the user logged in by hand; never open one profile in two processes.
- Locate by role and text: `getByRole("button", { name: "Continuar" })`, `getByText`, `getByLabel`.
- On a new step, wait with `waitForFunction` for the expected text, never with `waitForTimeout` alone.
- Optional modal: `locator.click({ timeout: 3000 }).catch(() => {})`. New tab: `context.waitForEvent("page")`. Upload: `setInputFiles`.
- Dialogs: `page.on("dialog", d => d.dismiss())` by default; `accept()` only when the user wants that outcome.
- Expired session (no "Sair" or avatar; "Sair" = "Sign out"): do not mark the item as an error. Pause the robot and ask for a new login.
- On failure, save `page.screenshot` and the URL so the next run starts from them.
- Human-like pauses are for stability and to spare the site, never to fool detection.

## Close the task

Report what was done and verified, what stopped and why (the exact signal, such as "Turnstile on search" or "asks for login"), and what the user must do next. Add each new lesson as one row in the matching trap table or in sites.md.
