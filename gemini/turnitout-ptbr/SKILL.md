---
name: turnitout-ptbr
description: Higieniza texto e comentários de código em PT-BR com um script determinístico, sem LLM. Remove conectivos de IA no início de frase, clichês de tradução, travessão e caracteres invisíveis. Use esta skill quando o usuário pedir para escrever, editar ou revisar documentação, README, LaTeX, mensagem de commit, PR ou comentário de código em português, ou para tirar a cara de IA de um arquivo. Rode o script depois de editar arquivos e confira com --check antes da resposta final.
metadata:
  author: "Rafael Stevanato"
  version: "1.0.0-gemini"
  repository: "https://github.com/RafaelStevanato/ai-skills-rafael-stevanato"
  source: "Arquitetura inspirada em AhmadHassan-BTed/Turnitout-Humanizer, reescrita para PT-BR com motor próprio em Python (biblioteca padrão)"
  requires: "python 3.8+ (só biblioteca padrão); git opcional"
---

# Turnitout PT-BR

## Goal

Entregar texto e comentários de código em PT-BR sem sotaque de IA.

**Pronto quando:** `--check` sai com `0` para todo arquivo que você criou ou editou.

## Instructions

### Escrever

1. Nunca inicie frase ou parágrafo com conectivo de IA: "Vale destacar que", "Vale ressaltar que", "É importante notar que", "É importante destacar que", "É fundamental ressaltar que", "Cabe ressaltar que", "Convém destacar que", "Nesse sentido", "Nesse contexto", "Sob essa ótica", "Diante disso", "Além disso", "Ademais", "Outrossim", "Em suma", "Em resumo", "Em conclusão", "Não obstante", "Por fim, vale lembrar que", "Dessa forma, pode-se afirmar que". Comece pelo sujeito ou pelo dado técnico.
2. Nunca use clichê de tradução: "desempenha um papel fundamental", "desempenha um papel crucial", "uma rica tapeçaria de", "um testemunho de", "mergulhar fundo em", "explorar a fundo", "no que tange a", "no que concerne a", "com o intuito de", "a fim de que", "possui a capacidade de", "tem a capacidade de", "de forma holística", "de forma abrangente", "cenário em constante evolução", "paradigma transformador", "sinergia entre", "alavancar", "empoderar". Escreva o verbo ou o substantivo direto: "é central", "usar", "analisar", "examinar", "para", "pode", "consegue".
3. Nunca use travessão (—, U+2014) para separar orações. Use vírgula, dois-pontos, parênteses ou hífen entre espaços (" - "). Mantenha o travessão de diálogo no início da linha.
4. Nunca emita caractere Unicode zero-width, hífen suave (U+00AD) nem espaço não separável (U+00A0). Mantenha o ZWJ (U+200D) só dentro de emoji composto.
5. Varie o ritmo. Alterne frases curtas (4 a 8 palavras) com períodos longos e densos (20 a 32 palavras). Nunca escreva três frases seguidas com a mesma estrutura (Sujeito + Verbo + Complemento). Prefira voz ativa e verbo concreto.
6. Comente código só com o porquê: decisão de arquitetura, restrição de concorrência, contorno de bug de terceiro, complexidade de algoritmo. Nunca comente o que a linha seguinte faz. Use o prefixo `# invariante:`, `# motivo:`, `# contorno:` ou `# custo: O(...)`. Nunca altere identificador de API, string de negócio, fórmula matemática ou AST para "humanizar" código.

Para saber o que o filtro troca em cada frase, leia [resources/catalogo-de-regras.md](resources/catalogo-de-regras.md). Leia só quando precisar.

### Filtro determinístico (script caixa-preta)

1. Defina `S` como a pasta que contém este `SKILL.md`. Por exemplo: `~/.gemini/config/skills/turnitout-ptbr` ou `<workspace>/.agents/skills/turnitout-ptbr`.
2. Use `python` no Windows e `python3` nos outros sistemas.
3. Trate `scripts/turnitout_ptbr.py` como caixa-preta. Não leia nem edite o código. Rode `python $S/scripts/turnitout_ptbr.py --help` se precisar das opções.
4. Rode `python $S/scripts/turnitout_ptbr.py ARQUIVO...` em todo arquivo que você criou ou editou, depois da última edição. O comando imprime `higienizado: <caminho>` por arquivo alterado.
5. Rode `python $S/scripts/turnitout_ptbr.py --check ARQUIVO...` e decida pelo código de saída:

| Código | Significado | Ação |
|---|---|---|
| `0` | Nada a mudar | Termine |
| `1` | `--check` achou arquivo que mudaria (os caminhos saem no stdout) | Rode o passo 4 nesses caminhos e repita o passo 5 |
| `2` | Uso inválido ou arquivo inexistente (o motivo sai no stderr) | Corrija o caminho ou a opção e repita o passo 5 |

**Verify:** `--check` saiu com `0` depois da última edição de cada arquivo.

Cobertura e proteções do filtro:

- Prosa (texto inteiro): `.md` `.txt` `.tex` `.rst` `.adoc`.
- Código (só comentários): `.py` `.js` `.ts` `.tsx` `.jsx` `.go` `.rs` `.c` `.cpp` `.h` `.hpp` `.java` `.php` `.sh` `.rb` `.sql`.
- O filtro não altera trecho entre aspas, código entre crases, bloco de código, fórmula, URL, link nem front matter YAML.
- O filtro ignora arquivo com `turnitout: off`, as pastas `.claude`, `.codex`, `.gemini` e `.agents`, os arquivos CLAUDE.md, AGENTS.md, GEMINI.md e SKILL.md, e qualquer arquivo dentro de pasta de skill.
- Em arquivo rastreado pelo git, o padrão higieniza só as linhas alteradas em relação ao HEAD. `--all` higieniza o arquivo inteiro.

## Examples

Cada par abaixo é saída real do script.

**Par 1: conectivos e travessão (.md)**

Entrada:

> Vale destacar que o módulo falha sob carga. Além disso, a latência dobra — afetando o banco.

Saída:

> O módulo falha sob carga. A latência dobra - afetando o banco.

**Par 2: clichês de tradução (.md)**

Entrada:

> Esse serviço desempenha um papel fundamental no que tange ao cache com o intuito de alavancar a rede.

Saída:

> Esse serviço é central quanto ao cache para usar a rede.

**Par 3: comentário em Python, string intacta (.py)**

Entrada:

```python
msg = "Vale destacar que — além disso"
# Além disso, desempenha um papel fundamental — revisar
```

Saída:

```python
msg = "Vale destacar que — além disso"
# É central - revisar
```

**Par 4: menção entre aspas fica intacta (.md)**

Entrada e saída (iguais):

> Evite "desempenha um papel fundamental" no texto.

**Par 5: diretiva e palavra ambígua (.ts)**

Entrada:

```ts
// @ts-ignore
// Vale ressaltar que isso alavanca o estado
```

Saída:

```ts
// @ts-ignore
// Isso alavanca o estado
```

**Par 6: sessão de CLI**

```text
$ python3 scripts/turnitout_ptbr.py --check notas.md
notas.md
$ echo $?
1
$ python3 scripts/turnitout_ptbr.py notas.md
higienizado: notas.md
$ python3 scripts/turnitout_ptbr.py --check notas.md
$ echo $?
0
```

## Constraints & Tips

- **Caixa-preta:** nunca leia nem edite `scripts/turnitout_ptbr.py`. Use `--help` e o código de saída.
- **Menção literal:** escreva frases banidas entre aspas ou crases quando precisar citá-las. O filtro preserva esses trechos.
- **Opt-out:** escreva `turnitout: off` em qualquer linha do arquivo para o filtro ignorá-lo. Use só quando o usuário pedir.
- **Palavras ambíguas:** "alavanca" e "alavancas" ficam intactas, e "mergulhar no lago" também. O filtro troca só as formas verbais de "alavancar" e "empoderar".
- **Arquivo antigo:** o padrão protege linhas antigas em arquivo rastreado pelo git. Use `--all` só quando o usuário pedir o arquivo inteiro.
- **Edição depois do `--check`:** rode o script e o `--check` de novo.
- **Limite de tamanho:** o filtro ignora arquivo acima de 2 MB.
