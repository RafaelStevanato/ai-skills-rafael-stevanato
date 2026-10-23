# Skills para ChatGPT Codex (GPT-6)

Port das 7 skills de [`claude-code/`](../claude-code/) para o Codex, otimizado para a família GPT-6 (Astra, 6.1 Sol, Luna). O conteúdo de domínio (regras, listas, princípios, scripts, assets) é o mesmo; o que muda é a forma de entregar esse conteúdo ao modelo.

## Instalação

Copie (ou crie um link simbólico de) cada pasta de `codex/skills/` para um destes lugares:

- `~/.agents/skills/<nome>` para usar em qualquer projeto (no Windows, `C:\Users\<você>\.agents\skills\<nome>`);
- `<repo>/.agents/skills/<nome>` para valer só em um repositório.

O Codex detecta skills novas sozinho; reinicie se uma não aparecer. Chame uma skill explicitamente com `$nome` ou pelo `/skills`.

## O que foi otimizado para o GPT-6

As mudanças seguem o `$skill-creator` que vem com o Codex, a documentação [Build skills](https://learn.chatgpt.com/docs/build-skills), o post [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) e as [prompting best practices do GPT-6](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra#prompting-best-practices).

- **Descrições curtas e discriminantes (316 a 360 caracteres, antes até 1.000).** O Codex põe nome e descrição de toda skill numa lista com orçamento de ~2% do contexto e encurta descrições quando há muitas skills. As listas de gatilhos foram trocadas por "o que faz + quando usar + limite", e os limites só aparecem onde evitam roteamento errado.
- **SKILL.md como roteador.** Material de um modo só foi para referências com a condição de leitura explícita. Exemplo: o índice de 23 checks de `web-discoverability` saiu do SKILL.md (de 1.938 para 862 palavras) para `references/checks.md`.
- **Pronto definido no início.** Cada skill diz no primeiro parágrafo quando o trabalho está concluído, porque o GPT-6 tende a parar cedo quando o critério de término fica vago ou aparece só no fim.
- **Precedência explícita.** Toda skill declara que a instrução do usuário prevalece sobre a skill, como recomenda a OpenAI, já que o GPT-6 é mais sensível a instruções de skills e de `AGENTS.md`.
- **Menos linguagem absoluta e menos portões de "pergunte antes".** NEVER/STRICTLY/caixa-alta só ficaram onde há segurança, licença ou trava factual. Exemplo: o modo SYSTEM de `anti-slop` não bloqueia mais em 18 perguntas; preenche o briefing pelo contexto e pergunta uma vez só o que muda a entrega.
- **Conflitos resolvidos na origem.** Leituras forçadas ("leia os 4 guias antes") viraram leituras condicionais, e a lista de banidas do modo inglês passou a reconhecer a seção nova de tiques do GPT-6.
- **Diretiva INPUT vs OUTPUT mantida, sem caixa-alta.** O banner ⚠️ virou uma frase: regras em linguagem controlada para leitura precisa, saída em prosa natural para o leitor.
- **Ferramentas do Codex no lugar das do Claude.** `human-browser` virou uma camada de táticas sobre o plugin Browser/Chrome do Codex (API `tab.playwright`, `tab.ax`, `tab.cua`, `getJsDialog`, file chooser) e não repete a política de confirmação que o plugin já aplica. `skill-evaluation` avalia skills de Codex (`agents/openai.yaml`, invocação implícita × só explícita, orçamento da lista de skills) e roda o trigger eval com `codex exec`. As integrações com Jev mantêm só a descoberta no Codex. A trava de uso da `revenue-centric-design` ganhou o `hooks.json` do Codex.
- **Tiques do próprio GPT-6.** `anti-ai-slop-escrita-ptbr` agora varre os tiques que a OpenAI documenta para o GPT-6 ("Não é sobre X. É sobre Y.", "Resumo:", pergunta retórica + resposta, rótulos compostos inventados) e manda entregar prosa sem o markdown que o modelo coloca por padrão.
- **`agents/openai.yaml` em todas.** Contém nome de exibição, descrição curta (25 a 64 caracteres) e um `default_prompt` com `$nome`. A invocação implícita foi mantida em todas, que é o padrão recomendado.
- **Índice curto nas referências longas.** Arquivos com mais de 150 linhas ganharam uma linha `Contents:`/`Conteúdo:` para servir de termos de busca.

## Validação

```bash
python tools/validate.py
```

O script confere frontmatter, nomes, tamanho do SKILL.md, campos do `openai.yaml`, links e âncoras relativos, além de restos de outro agente (nomes de ferramentas do Claude, banners antigos). As 7 skills também passam no `quick_validate.py` oficial do `$skill-creator`. No Windows, rode com `python -X utf8`, porque o script oficial lê arquivos sem declarar o encoding.

Teste de carregamento sem gastar cota: com as skills em `<pasta>/.agents/skills`, rode `codex debug prompt-input "oi"` nessa pasta e confira as 7 entradas no bloco `<skills_instructions>`. Isso foi verificado em 2026-10-23 com o Codex CLI 0.163: as 7 aparecem com a descrição completa.

## Limitações conhecidas

- O mapeamento de `human-browser` para a API do browser do Codex segue a documentação do plugin (versão 26.1016), mas ainda não foi testado em sites reais. As armadilhas e regras de parada vêm de 53 tarefas testadas no browser do Claude.
- O trigger eval comportamental (10 prompts por skill via `codex exec`) não foi rodado, porque consome cota do modelo.
- `revenue-centric-design` continua source-available: distribua sempre com o `LICENSE` e respeite a proibição de uso em apostas.
