# Site notes (tested 2026-10)

Update a note when a site changes.
Format: what works, where it blocks, shortcut.
Placeholders: `AAAA` = YYYY, `TERMO` = search term, `{14 dígitos}` = 14-digit CNPJ, `{cargo-slug}` = job-title slug, `{cidade-uf}` / `Cidade, UF` = city, state code, `Nome` = article title, `{uf}` / `{cidade}` = state code / city, `X` = query.

## Public APIs that save the browser

|Data|Call|Fields|
|---|---|---|
|Company by CNPJ (the tax agency form has a CAPTCHA)|`https://brasilapi.com.br/api/cnpj/v1/{14 dígitos}`|`razao_social`, `descricao_situacao_cadastral`, `data_situacao_cadastral`|
|Exact Wikipedia article title (avoids a 404 from a guess)|`https://pt.wikipedia.org/w/api.php?action=opensearch&search=TERMO&limit=3&format=json`|2nd item: titles; 4th: URLs|
|Gupy jobs|`https://portal.gupy.io/api/job-search/jobs?jobName=X&limit=12&offset=0&workplaceType=remote`|`name` (job title), `careerPageName` (company; `companyName` does not exist), `jobUrl`, `workplaceType`, `city`, `state`|
|Remote jobs (aggregator)|`https://api.remotar.com.br/jobs?search=X`|`externalLink` (company ATS)|
|US dollar PTAX (Central Bank)|`https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='MM-DD-AAAA'&@dataFinalCotacao='MM-DD-AAAA'&$orderby=dataHoraCotacao%20desc&$top=1&$format=json`|`cotacaoVenda`, `cotacaoCompra`, `dataHoraCotacao` (one close per day; published around 13:00 Brasília time; no `tipoBoletim`)|

## Job boards (Brazil)

|Site|Search|Application|Block|Shortcut|
|---|---|---|---|---|
|Gupy (`portal.gupy.io`, `*.gupy.io`)|Public API `portal.gupy.io/api/job-search/jobs?jobName=X&limit=12&offset=0` (+ `&workplaceType=remote`); paginated UI; a UI filter applies only after "Aplicar" ("Apply")|Logged-in account; steps "Vamos continuar" ("Continue"), "Dados adicionais" ("Extra data"), "Perguntas criadas pela empresa" ("Company questions"), "Finalizar candidatura" ("Finish application")|None when logged in|Banner: "Rejeitar Todos" ("Reject All"); a rejection shows in URL `/curriculum/reproved`|
|Catho|SSR `catho.com.br/vagas/{cargo-slug}/{cidade-uf}/`; logged out sees only 5; card `article.offer`; no result shows "Ops! não encontramos nenhuma vaga" ("Oops! we found no job")|"Quero me candidatar" ("I want to apply") (`data-apply`); logged in opens modals by fetch: `/apply/modal/kq` (knockout questions; may ask for CPF), `checkresume`, `cvsent`|No CAPTCHA in the flow|Logged out redirects to `/cadastro-candidato/`; `Escape` in the welcome modal opens plans: navigate by URL|
|InfoJobs|`empregos.aspx?palabra=X&poblacion=ID` (Bauru = 5210599; `provincia=` is ignored); total in the `h1`: "N Vagas de Emprego de X em Cidade - UF" ("N Job Openings for X in City - State") (2026-10-20: 43 analista financeiro, 68 analista de dados)|"Candidatar-me" ("Apply") needs login (Google, Microsoft, LinkedIn, e-mail)|No CAPTCHA at login|Banner: "Saiba mais" ("Learn more") > "Não aceito nenhum" ("I accept none"); autocomplete "Onde?" ("Where?") filters only with a real key|
|BNE|Friendly URL `/vagas-de-emprego-para-X-em-cidade-uf` (sometimes redirects to home: compare `location.href`)|Login|**Turnstile on search** (direct URL or after a UI search)|Never automate|
|Vagas.com.br|`/vagas-de-X-em-cidade`|Login|reCAPTCHA on the page|Few results in the interior|
|Indeed|`br.indeed.com/jobs?q=X&l=Cidade, UF`|Login|403 for an HTTP client; a normal browser reads|Read only|
|LinkedIn|`linkedin.com/jobs/search?keywords=X&location=Cidade` opens without login for reading; `jobs-guest` is public|Easy Apply needs login|429 often in sequence|Pause 6-12 s|
|Remotar|API `api.remotar.com.br/jobs?search=X` (remote jobs only)|`externalLink` leads to the company ATS|None|ATS count in the links: InHire > Gupy > Sólides > Greenhouse > Workable > Lever|

## Company ATS

|ATS|Form|Protection|Result|
|---|---|---|---|
|InHire (`*.inhire.app`)|No login; LinkedIn required, PDF, questions|reCAPTCHA Enterprise on submit|Assisted mode only|
|Greenhouse (`job-boards.greenhouse.io`)|Long, LinkedIn required|Invisible reCAPTCHA|Assisted mode only|
|Workable (`apply.workable.com`)|No login|Turnstile|Assisted mode only|
|Lever (`jobs.lever.co/.../apply`)|Required: `name`, `email`, `phone`, `location`, `org`, `urls[LinkedIn]`, plus `cards[...]`|hCaptcha|Assisted mode only|
|TOTVS (`atracaodetalentos.totvs.app`)|"Enviar candidatura" ("Submit application") is a link to `centraldocandidato.totvs.app`|Login|Read the `href` before the click|
|Sólides (`*.vagas.solides.com.br`)|API `vagas.solides.com.br/api/vacancies` with `killerQuestions`|Login|Evaluated and not used|

A public ATS without login almost always has a CAPTCHA on submit.
Automate the full flow only on a platform where the user is logged in.

## Other sites

|Site|Note|
|---|---|
|Mercado Livre|The list opens `/gz/account-verification` with "Para continuar, acesse sua conta" ("To continue, log in"): an anti-robot wall. Stop. Use the official API or ask for a login|
|g1|The banner has only "Prosseguir" ("Proceed"): ignore it. the page text reads the whole article|
|Wikipedia|At 1024 px width, the search is collapsed behind an icon; `find` returns the hidden input. Click the search icon or button first. For a known article, `navigate` directly to `pt.wikipedia.org/wiki/Nome`|
|IBGE Cidades|SPA: `cidades.ibge.gov.br/brasil/{uf}/{cidade}/panorama`; wait for the number with snippet 4 ([snippets.md](snippets.md))|
|Gmail|To read and organize, use IMAP or the Gmail connector, not the UI|

## Practice playgrounds (safe, built for automation)

- `uitestingplayground.com` (`http://` only: real Chrome forces HTTPS and shows an error page, so use the in-app browser). Tests: click that ignores the DOM event, keyboard input, shadow DOM, nested iframes, dialogs, upload, progress bar, overlapped, hover, nbsp, disabled field.
- `demoqa.com`: form with react-select, date picker, upload, modals, tabs, frames. SPA: wait for the element (snippet 4 ([snippets.md](snippets.md))) before you read. `/webtables` is a simple `<table>` and does not sort by header. `/accordian`: the panel of each section is the `aria-controls` of its button, which exists only after the click (2026-10-20).
- `the-internet.herokuapp.com`: drag and drop, entry modal, infinite scroll, TinyMCE, dynamic loading. `/challenging_dom`: the canvas answer is in the inline `<script>` (`strokeText('Answer: N')`, changes on each load).
- Never use the playground login pages (password). Never submit forms without need.
