# Catálogo de regras do filtro

Referência estática do que `scripts/turnitout_ptbr.py` troca. Fonte: `scripts/rules_ptbr.json`.
Leia este arquivo só quando precisar saber o que o filtro faz com uma frase.

## Conectivos removidos no início de frase

O filtro remove o conectivo e põe em maiúscula a letra seguinte. Conectivos empilhados saem juntos.
O início de frase é o início da linha (depois de marcador de lista, título, citação ou comentário) ou o ponto final, de exclamação ou de interrogação seguido de espaço.
A vírgula depois do conectivo é opcional. O filtro só remove o conectivo se uma letra, um dígito ou um trecho protegido vier logo depois.

1. Vale destacar que
2. Vale ressaltar que
3. É importante notar que
4. É importante destacar que
5. É fundamental ressaltar que
6. Cabe ressaltar que
7. Convém destacar que
8. Nesse sentido
9. Nesse contexto
10. Sob essa ótica
11. Diante disso
12. Além disso
13. Ademais
14. Outrossim
15. Em suma
16. Em resumo
17. Em conclusão
18. Por fim, vale lembrar que
19. Não obstante
20. Dessa forma, pode-se afirmar que

## Trocas de expressão

A troca vale com maiúscula ou minúscula. Se a expressão original começa com maiúscula, a troca também começa.

| Expressão | Vira |
|---|---|
| desempenha um papel fundamental, crucial, pivotal, vital ou essencial | é central |
| desempenham um papel fundamental, crucial, pivotal, vital ou essencial | são centrais |
| um testemunho de, do, da, dos ou das | uma prova de, do, da, dos ou das |
| uma rica tapeçaria de | uma combinação de |
| tapeçaria de | combinação de |
| mergulhar fundo no, na, nos ou nas | analisar o, a, os ou as |
| mergulhar fundo em | analisar |
| explorar a fundo | examinar |
| no que tange a, ao, à, aos ou às | quanto a, ao, à, aos ou às |
| no que concerne a, ao, à, aos ou às | quanto a, ao, à, aos ou às |
| com o intuito de | para |
| a fim de que | para que |
| possui a capacidade de | consegue |
| tem a capacidade de | pode |
| de forma ou de maneira abrangente ou holística | integralmente |
| cenário em constante evolução | contexto atual |
| paradigma transformador | mudança técnica |
| sinergia entre | integração entre |
| alavancar, alavancando, alavancado(a)(s), alavancou, alavancaram, alavancam, alavancamos, alavancará, alavancarão, alavancaria, alavancariam | usar, usando, usado(a)(s), usou, usaram, usam, usamos, usará, usarão, usaria, usariam |
| empoderar, empoderando, empoderado(a)(s), empoderou, empoderaram, empoderam, empoderamos | capacitar, capacitando, capacitado(a)(s), capacitou, capacitaram, capacitam, capacitamos |
| delve into | examine |
| pivotal role | key role |
| testament to, a testament to | proof of |

## Não muda

- "alavanca" e "alavancas": substantivo, e a forma verbal "alavanca" do presente.
- "mergulhar em" e "mergulhar no" sem "fundo": uso literal ("mergulhar no lago").
- "um testemunho" sem "de", "do", "da", "dos" ou "das" logo depois (ex.: "um testemunho ocular").
- Conectivo no meio da frase (ex.: "e além disso, ...").
- Conectivo seguido de pontuação (ex.: "Além disso - z").

## Pontuação e caracteres invisíveis

| Entrada | Saída |
|---|---|
| travessão com ou sem espaços, no meio da linha (ex.: `a — b`, `a—b`) | `a - b` |
| travessão no início da linha (diálogo) | fica |
| travessão em linha de tabela Markdown (linha que começa com `|`) | fica |
| travessão no fim da linha (sem texto depois) | fica |
| traço en entre espaços (`a – b`) | `a - b` |
| traço en entre números (`1–2`) | fica |
| espaço não separável (U+00A0) | espaço comum |
| zero-width (U+200B, U+200C, U+200E, U+200F, U+202A a U+202E, U+2060 a U+206F), BOM (U+FEFF), hífen suave (U+00AD) | removido |
| ZWJ (U+200D) fora de emoji composto | removido |
| ZWJ (U+200D) entre dois emojis (ex.: homem programador) | fica |

## O que o filtro nunca altera

- Trecho entre aspas retas, aspas curvas ou aspas francesas na mesma linha.
- Código entre crases, bloco de código com cerca de crases ou de til, fórmula (`$...$`, `$$...$$`, ambientes LaTeX), comandos LaTeX de citação e referência, URL, destino de link Markdown e front matter YAML no início do arquivo.
- Em código-fonte: strings, docstrings, identificadores e a AST. O filtro altera só comentários.
- Diretivas em comentário: `@ts-`, `eslint`, `prettier-`, `nolint`, `noinspection`, `pragma`, `type:`, `noqa`, `pylint:`, `fmt:`, `#!`, `go:`, `+build`, `<reference`, `biome-ignore`, `istanbul`, `c8 `, `jshint`, `shellcheck`.
- Arquivo com `turnitout: off`, arquivo acima de 2 MB e arquivo que não decodifica como UTF-8.
- Pastas `.claude`, `.codex`, `.gemini` e `.agents`, os arquivos CLAUDE.md, AGENTS.md, GEMINI.md e SKILL.md, e qualquer arquivo dentro de pasta de skill.

## Códigos de saída do CLI

| Código | Significado |
|---|---|
| `0` | Ok. Com `--check`: nada mudaria. |
| `1` | Só com `--check`: algum arquivo mudaria. Os caminhos saem no stdout. |
| `2` | Uso inválido ou arquivo inexistente. O motivo sai no stderr. |
