---
name: turnitout-ptbr
description: Filtra texto e comentários de código em PT-BR contra sotaque de IA (conectivos no início de frase, clichês de tradução, travessão, caracteres invisíveis) com regras de escrita e um script Python determinístico. Use ao criar ou editar documentação, README, LaTeX, mensagem de commit, PR ou comentário de código em português, e rode o script nos arquivos editados antes da resposta final.
metadata:
  author: "Rafael Stevanato"
  version: "1.0.0-codex"
  repository: "https://github.com/RafaelStevanato/ai-skills-rafael-stevanato"
  source: "Arquitetura inspirada em AhmadHassan-BTed/Turnitout-Humanizer, reescrita para PT-BR com motor próprio em Python (biblioteca padrão)"
  requires: "python 3.8+ (só biblioteca padrão); git opcional"
---

# Turnitout PT-BR

Remova o sotaque de IA de texto e de comentários de código em português.
Siga as regras 1 a 6 ao escrever. Rode o filtro determinístico (regra 7) depois de editar arquivos e antes da resposta final.

## 1. Conectivos banidos no início de frase

- Nunca inicie frase ou parágrafo com um destes conectivos: "Vale destacar que", "Vale ressaltar que", "É importante notar que", "É importante destacar que", "É fundamental ressaltar que", "Cabe ressaltar que", "Convém destacar que", "Nesse sentido", "Nesse contexto", "Sob essa ótica", "Diante disso", "Além disso", "Ademais", "Outrossim", "Em suma", "Em resumo", "Em conclusão", "Não obstante", "Por fim, vale lembrar que", "Dessa forma, pode-se afirmar que".
- Comece pelo sujeito ou pelo dado técnico.

## 2. Clichês de tradução banidos

- Nunca use estes clichês: "desempenha um papel fundamental", "desempenha um papel crucial", "uma rica tapeçaria de", "um testemunho de", "mergulhar fundo em", "explorar a fundo", "no que tange a", "no que concerne a", "com o intuito de", "a fim de que", "possui a capacidade de", "tem a capacidade de", "de forma holística", "de forma abrangente", "cenário em constante evolução", "paradigma transformador", "sinergia entre", "alavancar", "empoderar".
- Escreva o verbo ou o substantivo direto: "é central", "usar", "analisar", "examinar", "para", "pode", "consegue".

## 3. Travessão

- Nunca use travessão (—, U+2014) para separar orações.
- Use vírgula, dois-pontos, parênteses ou hífen entre espaços (" - ").
- Mantenha o travessão de diálogo no início da linha.

## 4. Caracteres invisíveis

- Nunca emita caractere Unicode zero-width.
- Nunca emita hífen suave (U+00AD) nem espaço não separável (U+00A0).
- Mantenha o ZWJ (U+200D) só dentro de emoji composto.

## 5. Burstiness (variação rítmica)

- Quebre o comprimento uniforme de frase (15 a 22 palavras) que o texto de IA tem.
- Alterne frases curtas (4 a 8 palavras) com períodos longos e densos (20 a 32 palavras).
- Nunca escreva três frases seguidas com a mesma estrutura (Sujeito + Verbo + Complemento).
- Prefira voz ativa.
- Prefira verbo concreto.

## 6. Comentários de código (engenheiro sênior PT-BR)

- Nunca comente o que a linha seguinte faz (ex.: `# Incrementa o contador`, `# Função que valida o usuário`).
- Se o código é legível, não comente.
- Comente só o porquê: decisão de arquitetura, restrição de concorrência, contorno de bug de terceiro, complexidade de algoritmo.
- Use um prefixo curto:
  - `# invariante: ...`
  - `# motivo: ...`
  - `# contorno: ...`
  - `# custo: O(...) ...`
- Nunca altere identificador de API, string de negócio, fórmula matemática ou AST para "humanizar" código.

## 7. Filtro determinístico

Script: `scripts/turnitout_ptbr.py`. Regras do filtro: `scripts/rules_ptbr.json`. O script usa só a biblioteca padrão do Python e não chama LLM. O Codex não tem hook instalado por esta skill: rode o CLI você mesmo.

### Quando rodar

- Rode o CLI depois de editar arquivos e antes da resposta final.
- Rode o CLI em todo arquivo de texto ou de código em PT-BR que você criou ou editou.
- Rode o CLI de novo se você editar o arquivo depois.

### Comandos

- Defina `S` como a pasta que contém este `SKILL.md`. O Codex mostra o caminho na lista de skills. Em geral: `~/.agents/skills/turnitout-ptbr` ou `~/.codex/skills/turnitout-ptbr`.
- Use `python` no Windows e `python3` nos outros sistemas.
- `python $S/scripts/turnitout_ptbr.py ARQUIVO...` higieniza e grava. O comando imprime `higienizado: <caminho>` por arquivo alterado.
- Em arquivo rastreado pelo git, o comando higieniza só as linhas alteradas em relação ao HEAD. Sem git, sem rastreio ou sem HEAD, higieniza o arquivo inteiro.
- `--all` higieniza o arquivo inteiro.
- `--check` não grava e imprime os caminhos que mudariam.
- `--help` mostra a ajuda em português.
- Códigos de saída: `0` = ok. `1` = `--check` achou arquivo que mudaria. `2` = uso inválido ou arquivo inexistente.
- O CLI grava só os arquivos que você passa.

### Extensões cobertas

- Prosa (texto inteiro): `.md` `.txt` `.tex` `.rst` `.adoc`.
- Código (só comentários): `.py` `.js` `.ts` `.tsx` `.jsx` `.go` `.rs` `.c` `.cpp` `.h` `.hpp` `.java` `.php` `.sh` `.rb` `.sql`.
- Outras extensões: o filtro ignora.

### Laço de verificação

1. Rode o CLI nos arquivos que você criou ou editou.
2. Rode `--check` nos mesmos arquivos.
3. Se `--check` sair com `1`, rode o CLI de novo nos arquivos listados e repita o passo 2.
4. Se `--check` sair com `2`, corrija o caminho ou a opção e repita o passo 2.
5. Termine só quando `--check` sair com `0`.

### Proteções

- O filtro não altera trecho entre aspas retas, aspas curvas ou aspas francesas na mesma linha.
- O filtro não altera código entre crases, bloco de código, fórmula, URL, link nem front matter YAML.
- Escreva menções literais de frases banidas entre aspas ou crases.
- Escreva `turnitout: off` em qualquer linha do arquivo para o filtro ignorá-lo.
- O filtro ignora as pastas `.claude`, `.codex`, `.gemini` e `.agents`.
- O filtro ignora os arquivos CLAUDE.md, AGENTS.md, GEMINI.md e SKILL.md, e qualquer arquivo dentro de pasta de skill (pasta que contém SKILL.md).
- Em código, o filtro altera só comentários. Strings, docstrings e AST ficam intactas.
- O filtro preserva diretivas: `# noqa`, `# type:`, `// @ts-ignore`, `// eslint-...`, `#!`.
