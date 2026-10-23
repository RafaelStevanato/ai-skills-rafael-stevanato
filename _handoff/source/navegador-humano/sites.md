# Notas por site (testadas em 2026-10)

Atualize quando um site mudar. Formato: o que funciona, onde trava, atalho.

## APIs públicas que poupam o navegador

| Dado | Chamada | Campos |
|---|---|---|
| Empresa por CNPJ (o formulário da Receita tem CAPTCHA) | `https://brasilapi.com.br/api/cnpj/v1/{14 dígitos}` | `razao_social`, `descricao_situacao_cadastral`, `data_situacao_cadastral` |
| Título exato de artigo da Wikipedia (evita 404 por chute) | `https://pt.wikipedia.org/w/api.php?action=opensearch&search=TERMO&limit=3&format=json` | 2º item: títulos; 4º: URLs |
| Vagas da Gupy | `https://portal.gupy.io/api/job-search/jobs?jobName=X&limit=12&offset=0&workplaceType=remote` | `name` (cargo), `careerPageName` (empresa; não existe `companyName`), `jobUrl`, `workplaceType`, `city`, `state` |
| Vagas remotas (agregador) | `https://api.remotar.com.br/jobs?search=X` | `externalLink` (ATS da empresa) |
| Dólar PTAX (Banco Central) | `https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='MM-DD-AAAA'&@dataFinalCotacao='MM-DD-AAAA'&$orderby=dataHoraCotacao%20desc&$top=1&$format=json` | `cotacaoVenda`, `cotacaoCompra`, `dataHoraCotacao` (um fechamento por dia; sai por volta das 13h; não tem `tipoBoletim`) |

Use `curl` ou `fetch` para o JSON inteiro; WebFetch resume e pode cortar campos.

## Vagas de emprego (Brasil)

| Site | Busca | Candidatura | Bloqueio | Atalho |
|---|---|---|---|---|
| Gupy (`portal.gupy.io`, `*.gupy.io`) | API pública `portal.gupy.io/api/job-search/jobs?jobName=X&limit=12&offset=0` (+ `&workplaceType=remote`); UI paginada; filtro da UI só vale depois de "Aplicar" | Conta logada; etapas "Vamos continuar", "Dados adicionais", "Perguntas criadas pela empresa", "Finalizar candidatura" | Nenhum no fluxo logado | Banner: "Rejeitar Todos". Reprovação aparece na URL `/curriculum/reproved` |
| Catho | SSR `catho.com.br/vagas/{cargo-slug}/{cidade-uf}/` (deslogado vê só 5; cartão `article.offer`; sem resultado mostra "Ops! não encontramos nenhuma vaga") | "Quero me candidatar" (`data-apply`); logado abre modais por fetch: `/apply/modal/kq` (perguntas eliminatórias, pode pedir CPF), `checkresume`, `cvsent` | Sem CAPTCHA no fluxo | Deslogado redireciona para `/cadastro-candidato/`. `Escape` no modal de boas-vindas abre planos: navegue por URL |
| InfoJobs | `empregos.aspx?palabra=X&poblacion=ID` (Bauru = 5210599; `provincia=` é ignorado). Total no `h1`: "N Vagas de Emprego de X em Cidade - UF" (2026-10-20: 43 analista financeiro, 68 analista de dados) | "Candidatar-me" exige login (Google, Microsoft, LinkedIn, e-mail) | Sem CAPTCHA no login | Banner: "Saiba mais" > "Não aceito nenhum". Autocomplete "Onde?" só filtra com tecla real |
| BNE | URL amigável `/vagas-de-emprego-para-X-em-cidade-uf` (às vezes redireciona para a home: compare `location.href`) | Login | **Turnstile na busca** (direto pela URL ou depois da busca pela UI) | Não automatizar |
| Vagas.com.br | `/vagas-de-X-em-cidade` | Login | reCAPTCHA na página | Pouco resultado no interior |
| Indeed | `br.indeed.com/jobs?q=X&l=Cidade, UF` | Login | 403 para cliente HTTP; navegador normal lê | Só leitura |
| LinkedIn | `linkedin.com/jobs/search?keywords=X&location=Cidade` abre sem login para leitura; `jobs-guest` público | Easy Apply exige login | 429 frequente em sequência | Pausas de 6-12 s |
| Remotar | API `api.remotar.com.br/jobs?search=X` (só remotas) | `externalLink` leva ao ATS da empresa | Nenhum | Contagem de ATS nos links: InHire > Gupy > Sólides > Greenhouse > Workable > Lever |

## ATS de empresas

| ATS | Formulário | Proteção | Conclusão |
|---|---|---|---|
| InHire (`*.inhire.app`) | Sem login; LinkedIn obrigatório, PDF, perguntas | reCAPTCHA Enterprise no envio | Modo assistido no máximo |
| Greenhouse (`job-boards.greenhouse.io`) | Longo, LinkedIn obrigatório | reCAPTCHA invisível | Modo assistido no máximo |
| Workable (`apply.workable.com`) | Sem login | Turnstile | Modo assistido no máximo |
| Lever (`jobs.lever.co/.../apply`) | `name`, `email`, `phone`, `location`, `org`, `urls[LinkedIn]` obrigatórios + `cards[...]` | hCaptcha | Modo assistido no máximo |
| TOTVS (`atracaodetalentos.totvs.app`) | "Enviar candidatura" é link para `centraldocandidato.totvs.app` | Login | Ler o `href` antes de clicar |
| Sólides (`*.vagas.solides.com.br`) | API `vagas.solides.com.br/api/vacancies` com `killerQuestions` | Login | Avaliado e não usado |

Regra que saiu daqui: ATS público sem login quase sempre tem CAPTCHA no envio. Automação completa só em plataforma com conta logada pelo usuário.

## Outros

| Site | Observação |
|---|---|
| Mercado Livre | Lista abre `/gz/account-verification` ("Para continuar, acesse sua conta"): muro anti-robô. Parar; usar a API oficial ou pedir login |
| g1 | Banner só com "Prosseguir": ignore, `get_page_text` lê a matéria inteira |
| Wikipedia | Com 1024 px de largura a busca fica recolhida atrás de um ícone; `find` devolve o input oculto. Clique no ícone/botão de busca primeiro. Para um artigo conhecido, `navigate` direto em `pt.wikipedia.org/wiki/Nome` |
| IBGE Cidades | SPA: `cidades.ibge.gov.br/brasil/{uf}/{cidade}/panorama`; espere o número com o snippet 4 |
| Gmail | Para ler e organizar, IMAP ou o conector do Gmail é melhor que a UI |

## Playgrounds para treinar (seguros, feitos para automação)

- `uitestingplayground.com` (só `http://`: não abre no Claude in Chrome, use o painel): clique que ignora evento DOM, input por teclado, shadow DOM, iframes aninhados, diálogos, upload, barra de progresso, overlapped, hover, nbsp, campo desabilitado.
- `demoqa.com`: formulário com react-select, date picker, upload, modais, abas, frames. É SPA: espere o elemento (snippet 4) antes de ler. `/webtables` é `<table>` simples e não ordena pelo cabeçalho. `/accordian`: o painel de cada seção é o `aria-controls` do botão, que só existe depois do clique (2026-10-20).
- `the-internet.herokuapp.com`: drag and drop, modal de entrada, scroll infinito, TinyMCE, carregamento dinâmico. `/challenging_dom`: a resposta do canvas está no `<script>` inline (`strokeText('Answer: N')`, muda a cada carga).
- Não usar páginas de login dos playgrounds (senha) nem enviar formulários sem necessidade.
