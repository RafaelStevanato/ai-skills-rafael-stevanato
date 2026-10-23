# Skills para Gemini 4 Argon (Google Antigravity)

Port das 7 skills de [`claude-code/`](../claude-code/) para o Google Antigravity (App, CLI `agy` e IDE), que é onde o Google recomenda rodar o Gemini 4 Argon. Em junho de 2026, o Antigravity CLI substituiu o Gemini CLI para usuários do plano gratuito e do Google One, e a documentação do Gemini CLI avisa que ele não foi otimizado para o Argon. O conteúdo de domínio (regras, listas, princípios, scripts, assets) é o mesmo das outras versões; o que muda é a forma de entregar esse conteúdo ao modelo.

## Instalação

Copie (ou crie um link simbólico de) cada pasta de `gemini/skills/` para:

- `~/.gemini/config/skills/<nome>` para usar em qualquer projeto (no Windows, `C:\Users\<você>\.gemini\config\skills\<nome>`, a mesma pasta onde já estão suas skills `caveman`);
- `<workspace>/.agents/skills/<nome>` para valer só em um projeto.

Confira com `/skills` e recarregue com `/skills reload` (CLI) ou reiniciando o app. No CLI, cada skill também vira o comando `/<nome>`.

## O que foi otimizado para o Gemini 4 Argon

As mudanças seguem a documentação de [skills do Antigravity](https://antigravity.google/docs/skills/), a skill nativa `agy-customizations` (instalada em `~/.gemini/antigravity/builtin/skills/`), o [codelab de skills do Google](https://codelabs.developers.google.com/getting-started-with-antigravity-skills), o [guia do Gemini 4 Argon](https://aistudio.google.com/learn/gemini-4-argon-developer-guide) e as [estratégias de prompting do Gemini](https://ai.google.dev/gemini-api/docs/prompting-strategies).

- **Descrição no formato do Antigravity.** Diz o que a skill faz (em terceira pessoa) e quando usá-la ("Use this skill when…"), com um "Don't use it for…" só onde evita ativação errada. É o campo que o agente lê para decidir se ativa a skill.
- **Estrutura das skills nativas do Google:** Step 0 (preflight), passos numerados, verificação e entrega, exemplos, "Constraints & Tips" e recursos.
- **Verificação em todo passo (`**Verify:**`).** O Antigravity manda incluir sempre como conferir que o passo deu certo, e o guia do Argon pede um sinal concreto de passou/falhou, de preferência com linha de base. Exemplo: `web-discoverability` registra o nível do primeiro scan como linha de base e re-escaneia até o check passar.
- **Preflight antes de começar.** Segue a dica 1 do Argon: confirmar entradas, ferramentas e acesso antes de uma execução longa.
- **Exemplos few-shot em todas as skills.** O Google recomenda incluir sempre exemplos com formato consistente. Os exemplos saem do material real: o par antes/depois da skill PT-BR vem de `padroes-composicao.md`, e o exemplo da `revenue-centric-design` usa um princípio e uma evidência verdadeiros.
- **Restrições críticas no topo, dicas no fim.** O guia de prompting do Gemini põe as restrições no começo, e as skills nativas do Antigravity deixam "Constraints & Tips" para o fim. Cada skill tem "Hard constraints" ou "Stop rules" logo depois do objetivo, e as dicas no fim.
- **Scripts como caixa-preta e delegação.** O agente roda os scripts com `--help` em vez de ler o código. Onde há trabalho paralelo, a skill sugere delegar a subagentes (dica 4 do Argon: o Argon orquestra, os subagentes executam).
- **Reflexão ao final** (dica 5 do Argon). A `human-browser` grava cada lição nova na própria skill, e a `revenue-centric-design` mantém o `rcd-log.md`.
- **Ferramentas e mecanismos do Antigravity:**
  - `human-browser`: no Antigravity, o browser é um subagente que só roda quando o usuário digita `/browser` e que não enxerga a skill. A skill passou a cuidar da rota de dados (`read_url_content`, `curl`, `search_web`) e a montar a mensagem de delegação com objetivo, condição de término, regras de parada e armadilhas. Os snippets foram adaptados às ferramentas do Chrome DevTools MCP (`take_snapshot` e uid, `handle_dialog`, `upload_file`, `list_network_requests`).
  - `revenue-centric-design`: a trava anti-apostas usa o `hooks.json` do Antigravity, com um adaptador (`scripts/agy_boundary_hook.py`) que devolve o JSON de decisão exigido. Quando o texto está limpo, o `allow` repassa a escrita para a política normal de permissões, sem aprovar nada sozinho.
  - `skill-evaluation`: avalia skills de Antigravity (skill, regra `GEMINI.md`/`AGENTS.md` ou uso manual; descrição; verificação; exemplos) e roda o trigger eval com `agy -p --output-format json`.
  - Jev: a descoberta procura o servidor no MCP do Antigravity (`mcp_config.json`).
- **Diretiva INPUT vs OUTPUT mantida em uma frase.** Na skill PT-BR entrou um aviso: como o Gemini responde de forma direta e enxuta por padrão, o texto autoral precisa sair em prosa no tamanho que o gênero pede.

## Validação

```bash
python -X utf8 tools/validate.py
```

O script confere frontmatter, a cláusula "Use this skill when", Step 0, "Done when", passos "Verify", seção de exemplos, links e âncoras relativos, além de restos do Claude ou do Codex. O adaptador do hook foi testado com payloads no formato do Antigravity: bloqueia "poker", libera texto normal e respeita o `.rcd-boundary-ok`.

## Limitações conhecidas

- As skills não foram testadas dentro do Antigravity. O app não tem um comando gratuito equivalente ao `codex debug prompt-input`, e o `agy` CLI não está instalado nesta máquina.
- O mapeamento da `human-browser` para o Chrome DevTools MCP segue a referência oficial das ferramentas, mas não foi testado em sites reais no Antigravity.
- Há relatos da comunidade de versões do IDE que não disparam hooks de plugin. Teste o hook uma vez depois de instalar.
- O trigger eval comportamental não foi rodado, porque consome cota.
