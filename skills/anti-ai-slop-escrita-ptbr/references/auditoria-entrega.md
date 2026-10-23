> PENDENTE: reescrita ASD-STE100. Conteúdo original copiado sem alteração de `humanizar/references/material-autoral.md, humanizar/SKILL.md L524-537, L646-802, L814-831`. Ver `HANDOFF.md` na raiz do repositório.

# Material autoral e auditoria semântica

## Inventário antes de escrever

Manter um inventário de trabalho das proposições, sem exigir relatório ao usuário:

| Campo | Registrar |
|---|---|
| Afirmação | O que a fonte efetivamente diz, inclusive intenção e avaliação |
| Responsável | Quem agiu, assume a tarefa ou oferece algo |
| Força | Fato, opinião, possibilidade, estimativa, proposta, obrigação ou promessa |
| Tempo e escopo | Estado temporal, prazo, público, condição, exceção e aviso |
| Proveniência | Trecho do original, nota, transcrição ou resposta do usuário |

Registrar também chamada para ação, agradecimento e pedido de desculpas. Em uma
mensagem curta, o inventário pode ser mental; com várias fontes ou compromissos
complexos, registrar entradas explícitas. A lista orienta a reescrita e não
substitui a comparação com as fontes completas.

## Notas e transcrições

Notas, transcrições e rascunhos pessoais são material suficiente. Usar esse
material como base principal: preservar raciocínio, ordem das afirmações,
relações de causa e consequência, exemplos e expressões próprias. Manter as
frases onde funcionam; reorganizar somente quando melhorar a compreensão sem
mudar ênfase ou sentido.

Se houver também um rascunho de IA, usá-lo como lista auxiliar de pontos, sem
impor seu enquadramento ao autor. Mapear as afirmações às fontes. Fatos exclusivos
desse rascunho permanecem não verificados; não incorporar nem excluir em silêncio.
Se houver conflito material, perguntar qual informação vale, salvo quando a
precedência já estiver definida. A correção do usuário atualiza a base aprovada;
os artefatos originais permanecem imutáveis. Uma amostra de estilo fornece voz,
não fatos ou experiências para transferir.

## Perguntas sobre lacunas

Perguntar quando o usuário pedir ou quando faltar informação essencial para um
texto fiel e útil, desde que haja interlocutor. Prosa genérica, sozinha, não exige
entrevista. Mensagem operacional com fatos completos segue direto para edição.

Fazer uma rodada de até três perguntas, cada uma ligada a um trecho ou lacuna.
Pedir o exemplo real, número, acontecimento ou raciocínio em poucas frases, nas
palavras do autor. Inferir gênero, público e tom quando possível. Exemplo:
“Você escreveu ‘reduzimos bastante o atraso’. O que mudou, e qual medida ou caso
real podemos citar?”

No modo direto ou em pipeline sem interlocutor, trabalhar conservadoramente com
o material disponível e apontar a lacuna. Respostas passam a integrar a base
factual aprovada com proveniência. Pergunta pulada ou sem resposta não autoriza
inventar nem retirar conteúdo protegido: manter a generalidade sustentada,
sinalizar o dado ausente ou aguardar se a resposta for indispensável. Perguntar
novamente apenas se uma nova contradição impedir a conclusão.

## Auditoria nos dois sentidos

1. **Fonte → candidata:** toda proposição protegida permanece com a mesma força,
   responsável, prazo, condição e escopo.
2. **Candidata → fonte:** cada afirmação, causa, benefício, experiência, sentimento
   e compromisso tem respaldo na fonte ou nas adições aprovadas do usuário.

Em criação, comparar com o material factual aprovado; não tratar o primeiro
rascunho gerado como prova de suas próprias afirmações.

| Fonte | Mudança inválida |
|---|---|
| “Pode ajudar a reduzir atrasos” | “Vai reduzir atrasos” |
| “Propomos lançar na sexta” | “Vamos lançar na sexta” |
| “Reconhecemos o transtorno” | “Pedimos desculpas pelo nosso erro” |
| “O reembolso está disponível” | “O reembolso está disponível se cancelar hoje” |
| “O time vai revisar” | “Eu vou revisar” |
| “As visitas de vocês ajudaram” | “Sem vocês teria sido impossível” |

Falha em qualquer direção invalida a candidata antes da avaliação de estilo.
Uma fórmula de agradecimento pode ser simplificada, mas sua intenção não pode
sumir nem ganhar uma relação causal mais forte. “Já vi isso acontecer” também
inventa experiência se não houver essa informação na fonte.

## Proveniência editorial

Inventário, auditoria e fluxos com material autoral foram adaptados das ideias de
[phuryn/work-humanizer](https://github.com/phuryn/work-humanizer), revisado no
commit `0a9065791d021f3dda695f3887cb2ae4c0eacbcf`. A avaliação publicada em inglês
não comprova desempenho desta skill em PT-BR. Não há promessa de resultado em
detectores ou benchmark.


#### Indicadores quantitativos opcionais

Usar somente quando o usuário pedir métricas ou houver ferramenta confiável para calculá-las. Nunca estimar números. Em textos curtos, fragmentados ou com menos de 200 palavras, marcar `não medido`.

Indicadores possíveis:

- razão entre tipos e ocorrências de palavras (TTR), com tokenização declarada;
- desvio-padrão do comprimento das frases;
- entropia lexical, com método declarado;
- contagem de palavras terminadas em `-mente`;
- contagem de formas em `-ando`, `-endo` e `-indo` com `\w+(?:ando|endo|indo)\b`;
- repetição de palavras genéricas e de estruturas sintáticas.

Tratar os resultados como pistas dependentes de gênero e tamanho. Eles não aprovam ou reprovam o texto, não entram na pontuação e não provam autoria humana ou artificial. Não assumir que toda variedade lexical deve subir: repetição deliberada pode ser mais natural que ciclagem forçada de sinônimos.

### Passo 7 — 🔥 Verificação final

Auditar primeiro nos dois sentidos contra o texto-fonte e as adições aprovadas: toda proposição protegida sobrevive e toda afirmação da candidata tem respaldo. Conferir possibilidade versus promessa, proposta versus compromisso, reconhecimento versus desculpa, condições de oferta e quem assume a responsabilidade. Em criação, auditar contra o material factual aprovado.

Verificar cada item. Marcar ✓, ✗ ou N/A conforme o perfil e o tamanho do trecho.

| # | Verificação | ✓/✗ |
|---|---|---|
| 1 | **TRAVA FACTUAL** atendida integralmente conforme a definição canônica? | |
| 2 | Argumento, intenção, modalidade e trechos protegidos permanecem intactos? | |
| 3 | Transições e padrões mecânicos detectados foram corrigidos? | |
| 4 | Termos vagos foram precisados somente quando a fonte fornecia material para isso? | |
| 5 | Ritmo e comprimento das frases combinam com o perfil? Em parágrafo com menos de três frases, não exigir três tamanhos distintos. | |
| 6 | Opinião, dúvida, sentimento e primeira pessoa aparecem somente se já existiam ou foram solicitados? | |
| 7 | Perfil de voz e registro permanecem consistentes em cada trecho? | |
| 8 | Estrangeirismos naturais do domínio foram preservados sem tradução forçada? | |
| 9 | Abertura, fechamento e formatação servem ao gênero, sem molde genérico desnecessário? | |
| 10 | Foi feita varredura por `—`, `–` e ` -- ` usados como aparte, preservando o travessão de diálogo e a frequência da amostra do autor? | |
| 11 | A guarda de falso positivo do Passo 6 foi aplicada, e nenhuma marca humana do autor foi padronizada? | |
| 12 | Lido em voz alta, o texto soa natural dentro do gênero e do público pretendido? | |

**Verificação adicional para perfis de brevidade (Assertivo/Enxuto/Resumo):**

| # | Verificação | ✓/✗ |
|---|---|---|
| A | Toda proposição do original permanece, ainda que compactada? | |
| B | Nenhum aviso/warning foi removido? | |
| C | Nenhuma condição de escopo foi generalizada? | |
| D | Modalidade preservada? ("pode" não virou afirmação) | |
| E | Números e thresholds permanecem exatos? | |
| F | Regras comuns aplicadas: passo a passo numerado, fecho em ação (não recapitulação), assunto secundário fora do meio? | |

Falha nos itens 1 ou 2 invalida a candidata. Nos demais itens, corrigir apenas se ainda houver tentativa disponível; não distorcer o gênero para satisfazer a lista. O controle de tentativas do Passo 9 impede repetição indefinida.

### Passo 8 — 📊 Avaliação pós-reescrita

Validar a **TRAVA FACTUAL** antes da avaliação de estilo. Se falhar, descartar a candidata e registrar pontuação `nula`; naturalidade nunca compensa alteração factual ou semântica.

Por padrão, avaliar qualitativamente correção dos padrões, naturalidade, consistência de voz e legibilidade. Não atribuir nota nem iterar para alcançar um número.

Calcular pontuação somente quando o usuário pedir ou fornecer `limiar`. Identificá-la como julgamento editorial subjetivo, não como medição ou probabilidade calibrada. Se a validação factual passar e a pontuação estiver ativa, avaliar quatro dimensões de 0 a 100, sempre em relação ao perfil ativo:

| Dimensão | Peso | Critério de avaliação |
|---|---|---|
| **Remoção de padrões IA** | 35% | Quantos padrões do Passo 2 foram eliminados? Algum remanescente? |
| **Naturalidade** | 30% | O ritmo combina com o gênero? A voz aparece somente na medida permitida? |
| **Consistência de voz** | 20% | O perfil foi mantido do início ao fim, respeitando trechos de outro registro? |
| **Legibilidade** | 15% | Frases fluem? Conectivos naturais? Lógica clara? |

**Pontuação final** = Σ (dimensão × peso)

Com pontuação ativa, usar o `limiar` solicitado ou 80 se foi pedida uma nota sem limiar. Sem pontuação, `limiar`, `pontuacao` e `convergiu` ficam `null`. Se a pontuação ficar abaixo do limiar e houver nova tentativa, atuar nas dimensões mais baixas. Com pontuação abaixo de 60, mudar a abordagem sem trocar perfil explícito. Indicadores quantitativos opcionais nunca alteram a pontuação.

### Passo 9 — 📦 Controle de tentativas e entrega

Executar a seleção de perfil, o inventário e o diagnóstico uma vez. Em cada
tentativa, partir do melhor texto seguro e comparar ao `texto_fonte` imutável e
às adições aprovadas. Em criação, comparar ao material factual aprovado. Executar
os Passos 3–7 antes da avaliação qualitativa ou da pontuação opcional.

```text
pontuacao_ativa = usuário pediu nota ou forneceu limiar
limiar = (valor solicitado ou 80) se pontuacao_ativa, senão null
melhor_texto = nenhum

para cada tentativa, respeitando o limite do modo:
    gerar candidata
    auditar fonte → candidata e candidata → fonte
    se falhar: descartar candidata sem pontuação
    senão:
        avaliar estilo em relação ao perfil
        calcular nota somente se pontuacao_ativa
        guardar candidata se melhorar o melhor texto seguro
        parar se não houver melhoria útil a fazer
        parar se pontuacao_ativa e nota atingir limiar

se nenhuma candidata for segura:
    estado = reprovada_trava_factual
    devolver texto_fonte sem nota
senão se pontuacao_ativa e melhor nota < limiar:
    estado = melhor_resultado
    devolver melhor_texto com limitação
senão:
    estado = concluida
    devolver melhor_texto
```

O limite é um máximo, não uma meta: parar quando outro passe não melhorar o
resultado. Conservar a melhor candidata segura, não necessariamente a última.

No `modo_direto`, produzir exatamente uma candidata e não repetir. Se ela falhar na TRAVA FACTUAL, devolver o texto-fonte com estado `reprovada_trava_factual`.

No `modo_criacao` não existe `texto_fonte` para comparação. A validação factual passa a ser: toda afirmação, nome, número, data e citação da candidata vem do material fornecido pelo usuário ou de verificação efetiva. Uma candidata que não passe nesse teste é reescrita, não entregue com ressalva. Se faltar dado, entregar a versão mais simples e nomear a lacuna.

Quando houver nova tentativa, escolher a alternativa pelo problema dominante:

| Problema da candidata anterior | Próxima abordagem |
|---|---|
| Padrões mecânicos remanescentes | Reforçar a remoção dos padrões detectados |
| Voz excessiva ou artificial | Reduzir intervenções e aproximar do registro original |
| Estrutura previsível | Reordenar apenas as proposições existentes |
| Texto longo inconsistente | Trabalhar por blocos semânticos e validar o conjunto |
| Perfil detectado inadequado | Mudar somente se o usuário não o escolheu e houver evidência no texto-fonte |

### Contrato de saída

Em pipelines ou quando houver pedido de saída estruturada, usar:

```yaml
estado: concluida
texto: "texto final ou texto-fonte seguro"
modo: modo_completo  # ou modo_direto, modo_revisão, modo_criacao
perfil_de_voz: voz_neutra
limiar: null  # 80 ou valor solicitado apenas com pontuação ativa
pontuacao: null  # nota editorial somente se solicitada
convergiu: null  # true/false somente com pontuação ativa
trava_factual:
  estado: intacta
  violacoes: []
tentativas:
  usadas: 2
  maximas: 3
relatorio: {}
```

Sem pontuação ativa, `concluida` indica que a candidata passou pela auditoria e pela avaliação qualitativa; os três campos numéricos/de convergência ficam `null`. Com pontuação ativa, usar os valores conforme o estado final:

| `estado` | `convergiu` | `pontuacao` | `texto` |
|---|---:|---:|---|
| `concluida` | `true` | Número ≥ limiar | Candidata segura aprovada |
| `melhor_resultado` | `false` | Melhor número abaixo do limiar | Melhor candidata segura |
| `reprovada_trava_factual` | `false` | `null` | `texto_fonte` |
| `entrada_invalida` | `false` | `null` | Entrada sem reescrita |

Em conversa, apresentar primeiro o texto e depois o relatório no nível do modo:

| Modo | Conteúdo do relatório |
|---|---|
| `modo_completo` | Padrões corrigidos e ressalvas; nota e indicadores somente se solicitados/calculados |
| `modo_direto` | Relatório sintético e estado; nota somente se solicitada |
| `modo_revisão` | Diagnóstico e ressalvas; nota e indicadores somente se solicitados/calculados |
| `modo_criacao` | Somente o texto final. Relatório apenas se o usuário pedir, ou uma linha curta quando faltar dado factual |

### Integração com ciclos externos

Na primeira chamada, usar o texto recebido como `texto_fonte` e `texto_atual`. Nas chamadas seguintes, manter `texto_fonte` inalterado e realimentar somente o campo `texto` como `texto_atual`:

```yaml
proxima_entrada:
  texto_fonte: "original imutável"
  texto_atual: "saída.texto"
  perfil_de_voz: "mesmo perfil"
  adicoes_aprovadas: []
  limiar: null  # preservar valor solicitado se houver
```

Nunca realimentar relatório, pontuação ou o envelope inteiro como se fossem parte do texto. Toda chamada continua comparando o resultado ao `texto_fonte` original e às adições aprovadas com proveniência; em criação, preservar a base factual aprovada entre chamadas.

## Suíte de testes de regressão

Conjunto mínimo para validar evoluções futuras. Rodar cada caso em `modo_completo` e conferir preservação semântica antes de julgar estilo.

| # | Tipo | Antes (IA) | Depois esperado (síntese) |
|---|---|---|---|
| T1 | E-mail corporativo | "Venho por meio deste informar que o relatório será encaminhado oportunamente" | "O relatório será enviado oportunamente." |
| T2 | Parágrafo acadêmico | "Diversos autores discutem a questão da linguagem de forma ampla" | "Diversos autores discutem a linguagem em termos amplos." |
| T3 | Texto jurídico | "É cediço que a responsabilidade civil objetiva se aplica no âmbito das relações de consumo" | "A responsabilidade civil objetiva aplica-se às relações de consumo." |
| T4 | Modelo de abertura de blog | "Neste artigo, exploraremos 5 estratégias essenciais para otimizar seu workflow" | "Neste artigo, vamos explorar cinco estratégias essenciais para otimizar seu workflow." |
| T5 | Ressalva excessiva de IA | "Como modelo de linguagem, não posso afirmar com certeza, mas parece que talvez o sistema esteja funcionando" | "O sistema parece estar funcionando, mas ainda não é possível afirmar com certeza." |
| T6 | Didático genérico | "João tem 3 maçãs e Maria tem 5. Quantas têm ao todo?" | "João tem 3 maçãs e Maria tem 5. Quantas maçãs os dois têm ao todo?" |
| T7 | Falso positivo (marca humana) | "Oxe, eu tô achando que não vale a pena pra gente agora" | Inalterado. Regionalismo e contração são voz do autor, não vício de IA |
| T8 | Fonte inventada | "Segundo Almeida (2019, p. 84), o efeito é consistente" sem que a referência exista | Afirmação mantida como está e marcada para verificação; nunca substituir por outra referência |

> **Critério de regressão**: se uma evolução piora o resultado de qualquer teste T1-T8, a mudança deve ser reavaliada.
>
> **TRAVA FACTUAL nos casos de teste:** nenhuma saída esperada pode adicionar, retirar ou alterar conteúdo protegido. Resultado mais contido é preferível a uma versão mais vistosa que invente informação.
