---
name: anti-ai-slop-escrita-ptbr
description: Escreve e revisa texto em PT-BR (e em inglês) sem marcas de escrita de IA, preservando fatos, números, fontes, modalidade e argumento. Use para redigir texto que alguém vai assinar ou publicar, humanizar, tirar cara de ChatGPT ou simplificar linguagem. Não use em código, texto normativo (lei, contrato) ou texto de segurança crítica.
license: Apache-2.0
metadata:
  author: "https://ft.ia.br"
  version: "1.0.0-codex"
  repository: "https://github.com/fabricioctelles/skills"
  source: "Fusão de fabricioctelles/skills v1.7.0 (PT-BR, Apache 2.0) e Anti-AI-Slop Writing Directive v2"
  attribution: "Inventário e auditoria adaptados de phuryn/work-humanizer, commit 0a9065791d021f3dda695f3887cb2ae4c0eacbcf; tropos de tropes.fyi; ablação semântica de The Register (fev 2026); Português Simplificado baseado em PorSimples (NILC/USP), Lei 15.263/2025, NILC-Metrix e SIMPLEX-PB"
  license-compliance: "Apache-2.0 herdada de fabricioctelles/skills v1.7.0; obra derivada com alterações (reescrita ASD-STE100 e port para Codex em 2026-10-23); mantenha esta atribuição ao redistribuir"
---

# Anti-AI slop: escrita PT-BR

Remova os sinais de escrita mecânica de IA e recupere ritmo, precisão e voz sem criar uma nova história. O objetivo é melhorar o texto, não enganar detectores: nunca prometa que uma ferramenta de detecção vai classificar o resultado como humano.

O trabalho está pronto quando o texto final passa na verificação do Passo 7 de [references/auditoria-entrega.md](references/auditoria-entrega.md) e cada proposição protegida da fonte sobrevive intacta.

As instruções explícitas do usuário prevalecem sobre esta skill. As regras abaixo estão em linguagem controlada (ASD-STE100) só para leitura precisa. O texto entregue deve sair fluido, natural e com ritmo humano em PT-BR; use a densidade do ASD-STE100 apenas em trechos que expliquem um conceito técnico complexo.

## Escopo e idioma

- Escreva e reescreva em PT-BR por padrão. As regras deste arquivo valem para todo texto, em qualquer idioma.
- Para texto em inglês, carregue [references/modo-ingles.md](references/modo-ingles.md) e não aplique ao inglês as convenções do PT-BR. Em texto multilíngue, aplique a cada segmento as regras do seu idioma.
- Antes de escrever ou reescrever, carregue [references/palavras-banidas.md](references/palavras-banidas.md) e rode a Checklist de saída dele antes de entregar. Nunca use item da lista em texto que você gera (`modo_criacao` e toda frase nova). Em texto existente do autor, vale a guarda de acúmulo do Passo 6: palavra formal isolada não é sinal.

## Proteções obrigatórias

1. **TRAVA FACTUAL.** O texto-fonte é imutável. Preserve nomes, números, datas, citações, fontes, exemplos, relações causais, modalidade (certeza, dúvida, obrigação ou possibilidade), estado temporal, responsáveis, compromissos, prazos, condições, exceções, avisos, argumento, intenção, código e notação. Condense, reorganize e reformule quando necessário, mas nunca acrescente, retire ou altere esses elementos sem autorização explícita. Nunca invente vivência pessoal, anedota, estatística, fonte, exemplo, benefício, promessa ou pedido de desculpas para dar concretude ou calor ao texto.
2. **Concretude sem invenção.** Reutilize detalhes já presentes e mantenha lacunas fora do texto publicável. Se faltar dado essencial, preserve a generalidade, peça o dado ou, só em rascunho de trabalho solicitado, marque `[DADO OU EXEMPLO REAL NECESSÁRIO]`. Crie conteúdo fictício só a pedido do usuário e identifique-o como fictício.
3. **Argumento preservado.** Mantenha a posição e a conclusão do autor, mesmo que você discorde delas.
4. **Registro preservado.** Não force informalidade, primeira pessoa, humor ou opinião. O perfil de voz orienta a forma e nunca autoriza conteúdo novo.
5. **Precisão antes de estilo.** Preserve integralmente código, fórmulas, citações e trechos normativos. Em contexto crítico, aceite um resultado menos solto para não criar ambiguidade.
6. **Sem infantilização.** Simplificar a forma nunca simplifica o raciocínio.

Toda verificação de TRAVA FACTUAL usa esta definição. Em conflito com exemplos ou referências, estas proteções vencem.

## Triagem

Antes de diagnosticar ou reescrever:

1. Confirme que há material (texto, notas ou transcrição). Em `modo_criacao`, confirme tema, gênero e material factual disponível.
2. Não reescreva bulas, procedimentos médicos, manuais de aviação ou outros textos de segurança crítica.
3. Não reescreva contratos, leis, cláusulas ou documentos que sejam a própria referência normativa, e nunca altere texto normativo. O perfil Jurídico serve só para comentários, resumos e peças autorais.
4. Em traduções literais bilíngues ou conteúdo avaliado por correspondência exata, não varie a redação.
5. Em texto técnico, marque antes os trechos protegidos: código, equações, comandos, citações e identificadores.
6. Fora do escopo, explique o risco e ofereça só revisão superficial, se for seguro e o usuário autorizar.

## Modos

O modo define o nível do relatório e o máximo de tentativas; nunca altera as proteções. Preserve o modo escolhido pelo usuário.

| Modo | Quando usar | Tentativas máximas | Entrega |
|---|---|---:|---|
| `modo_completo` (padrão) | Pedido comum de humanização | 3 | Texto final e resumo das mudanças; pontuação só se pedida |
| `modo_direto` | Fluxo automatizado ou pedido de rapidez | 1 | Texto final e relatório sintético; sem repetição |
| `modo_revisão` | Auditoria de texto produzido por outro agente | 3 | Texto final, diagnóstico e relatório detalhado |
| `modo_criacao` | O texto ainda não existe | 2 | Só o texto final |

Sem `texto_fonte`, o único modo possível é `modo_criacao`, com as mesmas proteções ([Escrita do zero](#escrita-do-zero-modo_criacao)). Com mais de 500 palavras, trabalhe por blocos semânticos e faça uma verificação global depois de recompor o texto.

## Inventário e perguntas

Antes de editar ou criar, inventarie as proposições (campos em [references/auditoria-entrega.md](references/auditoria-entrega.md), que também trata de várias fontes, notas e transcrições). Depois, confira nos dois sentidos: o que estava protegido sobrevive e o que entrou tem respaldo. Mantenha as fontes imutáveis e registre à parte as adições aprovadas.

Pergunte só sobre lacunas reais: no máximo 3 perguntas, numa única rodada, e nunca no `modo_direto` nem em pipeline sem interlocutor. Resposta ausente nunca autoriza inventar nem cortar conteúdo protegido.

## Regras de escrita limpa

Estas regras valem para todo texto que você escreve ou reescreve; gatilhos e exemplos estão nas referências do Passo 3. Em reescrita, nunca mexa em conteúdo protegido para cumprir uma regra: em conflito, a TRAVA FACTUAL vence.

### Estrutura

- Evite a regra de três: use 1, 2, 4 ou 5 itens, ou 3 só quando o conteúdo tem exatamente 3. Em reescrita, quebre a simetria sem acrescentar nem retirar itens.
- Em reescrita, mantenha a modalidade da fonte e nunca aumente a certeza. Use qualificador só para incerteza real e nunca alterne ressalvas dos dois lados (gangorra).
- Em `modo_criacao`, assuma posição só se o material do usuário a sustenta, dê ao contraponto no máximo 1 frase e não abra com "Como [cargo], eu...".
- Em reescrita, tire a credencial da abertura sem apagá-la e reordene só proposições existentes.
- Ao quebrar a parataxe, una frases com oração subordinada, conjunção, ponto e vírgula ou vírgula, sem criar relação que a fonte não expressa. Varie a forma de parágrafos e seções ([references/padroes-composicao.md](references/padroes-composicao.md)).

### Escopo por perfil

| Regra | Isenção ou regra que prevalece |
|---|---|
| Parataxe: não encadeie 3 ou mais frases curtas declarativas | Isentos: Português Simplificado, Assertivo, Enxuto, Resumo e voz de autor cuja amostra usa fragmentos |
| Comprimento: nunca 3 frases seguidas do mesmo comprimento; misture frases de 4 e de 30 palavras | Português Simplificado: máximo de 25 palavras (alvo de 13 a 18), limite que prevalece. Parágrafo com menos de 3 frases não exige 3 tamanhos |
| Bullets: no máximo 5 seguidos, desiguais | Isentos: Português Simplificado e Resumo |
| Fragmento dramático: no máximo 1 por texto fora do Twitter | Fragmento ou frase longa encadeada só em perfil autoral cuja voz os sustenta |
| Palavra menos óbvia: evite a palavra de maior probabilidade (o clichê) e nunca troque sinônimos só para variar | Português Simplificado: a regra R4 (palavras comuns) prevalece |
| Voz ativa: nunca invente agente para eliminar a passiva; sinalize 3 ou mais passivas seguidas | Passiva legítima com agente desconhecido ou irrelevante, e em gêneros formais (jurídico, acadêmico, normativo) |
| Emoji decorativo (🚀💡🎯✨): proibido | Resumo: ✅🟡⬜❔🔴 são notação funcional de status |
| Cabeçalho markdown e negrito de ênfase: proibidos em redes sociais, e-mail e texto casual | Assertivo, Enxuto e Resumo: negrito em abertura de item como hierarquia |

### Pontuação e formatação

- Troque todo travessão (—), meia-risca (–) ou " -- " usado como aparte por vírgula, ponto, dois-pontos ou parênteses, ou reescreva a frase. Preserve-o em diálogo de ficção, na frequência da amostra do autor, em citação, título ou exemplo.
- Em PT-BR: no máximo 1 exclamação por 1.000 palavras e 1 reticência por texto, nunca como transição; sem vírgula antes do "e" ou "ou" final de lista (salvo orações de sujeitos diferentes); ponto fora das aspas quando a citação é parte da frase e dentro quando é frase completa; aspas retas; títulos em caixa de frase. Detalhes e formatação por canal (emoji, hashtags, markdown) em [references/padroes-estilo.md](references/padroes-estilo.md).
- Entregue no formato do gênero. O modelo que executa esta skill tende a responder com títulos, listas, tabelas e negrito; em e-mail, post, mensagem, artigo ou carta, entregue prosa corrida, sem markdown que o gênero ou o usuário não peçam.

### Especificidade sem invenção

- Use dado, nome, data, número, tempo, lugar e contexto só se estiverem na fonte ou no material do usuário. Mostre em vez de descrever. Sem o dado, a vagueza honesta vence a especificidade fabricada.
- Nunca invente dado, estudo, estatística ou citação (parafraseie com atribuição ou omita). Use "cerca de" ou "aproximadamente" só quando o número da fonte já é aproximado.
- Marque hipótese com "Suponha que" ou "Por hipótese". Nunca a apresente como fato nem abra com "Imagine um mundo onde" ou "Imagine se".
- Sem perfil nem amostra, use voz neutra. Use "pra", "tá" e "né" só em perfil informal ou quando a fonte os usa.

### Tiques do próprio GPT-6

A OpenAI documenta tiques recorrentes da família GPT-6, o modelo que executa esta skill. Varra o seu rascunho atrás deles, além da lista de palavras banidas:

- Rótulo de conclusão: "Resumo:", "Ponto principal:", "Em suma:", "Moral da história:", "O modelo mental mais simples é:" (no inglês, "Bottom Line:", "In short:", "The simplest mental model is:").
- Pergunta retórica seguida de resposta ("O resultado? Uma queda de 20%.").
- Falsa revelação "Não é sobre X. É sobre Y." e contraste "X, não Y" que traz uma alternativa que ninguém mencionou.
- Rótulos compostos inventados ("checagem de cabeça exata", "layout de linha editorial") e adjetivos compostos hifenizados em série.
- "genuinamente", "de fato", "vale notar", "importante destacar" usados como ênfase vazia (no inglês: "genuinely", "it's worth noting", "importantly", "delve", "foster", "leverage").
- Anúncio do que não vai mudar ou de como os resultados serão separados, em vez de dizer a ação.

### Aplicação silenciosa

- Aplique as regras sem mencioná-las. Nunca escreva "conforme as diretrizes" nem "as per the guidelines" no texto entregue.
- Nos modos com relatório, escreva-o fora do texto entregue e nunca afirme ter feito uma checagem que não rodou.
- Antes de entregar, rode a checagem de prioridade do Passo 7 ([references/auditoria-entrega.md](references/auditoria-entrega.md)): banidas, comprimentos iguais, parataxe, trios, ressalva, travessão, passiva, transições, especificidade inventada, texto genérico, cara de ChatGPT. Reescreva enquanto houver tentativa no modo.

## Escrita do zero (`modo_criacao`)

Use a lista de padrões como filtro de saída sobre o próprio rascunho, nunca como conserto de um original.

1. Escolha o perfil de voz (Passo 1). Sem perfil e sem amostra, use voz neutra.
2. Escreva direto, com o inventário e o material factual aprovado, sem tentar desviar dos padrões durante a redação. Com notas ou transcrição, preserve raciocínio, ordem e expressões do autor.
3. Rode o diagnóstico (Passo 2) sobre o rascunho. Varra primeiro 5 padrões: travessão de aparte; "não apenas X, mas também Y"; conectivo abrindo parágrafo ("Além disso", "Dessa forma", "Por fim"); trio forçado; fecho otimista genérico. Depois percorra o resto da tabela e os tiques do GPT-6.
4. Aplique a guarda de falso positivo (Passo 6) e a verificação final (Passo 7).
5. Entregue só o texto, sem rascunho, diagnóstico ou lista de padrões, e nunca anuncie que passou pela lista.

Em `modo_criacao`, a TRAVA FACTUAL significa usar só o que o usuário forneceu ou o que você verificou de fato. Nunca tape buraco com número plausível, data aproximada ou fonte que soa certa: escreva a frase mais simples e diga ao usuário o que falta.

## Processo

Comece pela Triagem e pelo inventário, mantendo `texto_fonte` imutável durante todo o processo. Em `modo_criacao`, o rascunho da primeira tentativa ocupa o lugar de `texto_atual`.

### Passo 1: perfil de voz

Sem perfil indicado pelo usuário, detecte-o pelo conteúdo:

| Sinal no texto | Perfil sugerido |
|---|---|
| Citações legais, artigos de lei, "art.", "§", "REsp", petição | ⚖️ Jurídico |
| Título informativo, lide, atribuições, falas de fontes, estrutura de reportagem | 📰 Jornalístico |
| Referências acadêmicas ("et al.", metodologia, hipótese, valor-p) | 🎓 Acadêmico |
| Tutorial, documentação amigável, "passo a passo", "vamos ver" | 🧑‍🏫 Didático |
| E-mail ou mensagem profissional com jargão técnico e nomes de ferramentas | 💬 Corporativo Informal |
| Texto de até 100 palavras, frases incompletas, abreviações, gírias | 📲 WhatsApp |
| Texto curto (menos de 300 palavras), opinativo, em 1ª pessoa, sem estrutura formal | 📱 Post de Rede Social |
| 1.500 palavras ou mais, narrativo, sem jargão dominante | 🖋️ Crônica |
| Texto institucional ou governamental, manual de produto, FAQ, pedido de "simplificar" ou "linguagem simples" | 📋 Português Simplificado |
| Resposta a decisão, briefing, "direto ao ponto", pergunta-resposta com escopo técnico | ➡️ Assertivo |
| Coding ou debugging, comandos, troubleshooting, confirmação de ação, respostas curtas | 🔹 Enxuto |
| Status update, standup, sprint review, "como está X?", "resumo de status", notas de reunião | 📊 Resumo |
| Nenhum sinal claro | Voz neutra: preserve o registro original e só remova padrões mecânicos |

Regras de decisão:

1. O perfil explícito limita o gênero e nunca é trocado automaticamente.
2. Dentro desse limite, a amostra fornecida controla as escolhas finas de estilo. Sem perfil explícito, a amostra vence a detecção.
3. Sem perfil nem amostra, use o perfil detectado; sem sinal claro, voz neutra.
4. Em conflito material, pergunte ao usuário nos modos completo e revisão. No `modo_direto`, escolha o registro mais próximo da fonte, aja de modo conservador e registre a ambiguidade.
5. Em texto com vários registros, mantenha um perfil principal e ajuste só os trechos de outro gênero.

No relatório, registre `🎯 Tipo detectado: [tipo] → Perfil: [perfil]`. Características e exemplos de cada perfil estão em [references/perfis-voz.md](references/perfis-voz.md).

### Passo 2: diagnóstico

Percorra cada categoria e marque ✓ (encontrado) ou ✗ (ausente). Cada linha detectada conta como um sinal, qualquer que seja o número de repetições.

| Categoria | Sinal | Peso (1-3) | Ação |
|---|---|---|---|
| Conteúdo | Atribuição vaga ("estudos mostram", "especialistas dizem") | 3 | Preservar a atribuição; especificar só se a fonte já estiver na entrada; senão, sinalizar a lacuna no relatório |
| | Ênfase inflada sem base ("revolucionário", "sem precedentes") | 3 | Preservar força e autoria da avaliação; sugerir redução no relatório, sem alterar sem autorização |
| | Dados possivelmente fabricados ou imprecisos | 3 | Preservar no texto e sinalizar para verificação; corrigir só com fonte ou autorização |
| | Fonte específica cuja existência não se confirma (autor, ano, DOI, link, página) | 3 | Não corrigir nem trocar a referência; marcar para verificação e retirar a afirmação que dependa só dela |
| Linguagem | Vocabulário genérico ("impacto", "contexto", "cenário") | 3 | Trocar por termo preciso já sustentado pela fonte |
| | Perífrases rebuscadas para evitar "ser", "ter" ou "estar" | 2 | Restaurar o verbo simples quando natural ao registro |
| | Paralelismo perfeito em 3 ou mais itens | 2 | Quebrar a simetria |
| Tom | Ressalva excessiva ("pode ser que talvez", "parece que") | 2 | Cortar a redundância sem aumentar a certeza |
| | Autorreferência de IA ("como modelo de linguagem...") | 3 | Remover o aviso padrão sem criar opinião |
| | Inflação de gravidade ("questão crucial para a humanidade") | 2 | Reduzir a escala sem criar comparação nova |
| | Máxima de camiseta ("X é a linguagem de Y", "X não é ferramenta, é espelho") | 2 | Trocar a frase de efeito pela afirmação específica que ela substitui |
| Composição | Molde introdutório ("Neste artigo, exploraremos...") | 3 | Cortar e ir direto ao conteúdo existente |
| | Conclusão em molde ("em resumo", "conclui-se que") | 3 | Enxugar ou reorganizar a conclusão existente |
| | Transições artificiais ("primeiramente", "em segundo lugar") | 2 | Usar conectivos naturais |
| | Primeira frase repete o título | 1 | Cortar a repetição e começar pelo conteúdo |
| | Alternativa falsa levantada e descartada em meia frase | 2 | Remover a opção descartada e manter só a restrição real |
| | Documentação que descreve a versão anterior em vez do comportamento atual | 2 | Descrever o estado atual; histórico só em changelog, nota de versão e guia de migração |
| Estilo | Travessão (—) ou meia-risca (–) como aparte no meio da frase | 2 | Trocar por vírgula, ponto, dois-pontos ou parênteses, ou reescrever. Exceções no Passo 6 |
| | Negrito ou formatação excessiva | 1 | Moderar conforme o gênero |
| | Emoji em cada item (padrão ChatGPT) | 1 | Remover os que não têm função |
| | Markdown não solicitado (títulos e listas automáticas em prosa) | 2 | Remover quando não servir ao gênero |
| PT-BR | Oficialês ("cumpre salientar", "no âmbito de") | 2 | Substituir por construção direta |
| | Gerundismo ("vamos estar analisando") | 2 | Converter para forma verbal direta |
| | ENEM-ismo (frase de efeito genérica no final) | 2 | Trocar por reflexão específica |
| Estrangeirismos | Tradução forçada de termos de tecnologia | 2 | Restaurar o termo consagrado no domínio |
| | Anglicismo artificial fora de contexto técnico | 1 | Remover |

- Com 5 ou mais sinais de peso 3 e nenhum modo escolhido pelo usuário, use `modo_revisão`.
- No perfil Jurídico, o oficialês pode ser deliberado: avalie repetição mecânica e falta de função, não a mera presença da expressão.
- Métricas quantitativas (TTR, entropia, `-mente`, `-ando/-endo/-indo`) só a pedido do usuário, com [references/auditoria-entrega.md](references/auditoria-entrega.md).

### Passo 3: remoção de padrões

Para cada categoria marcada no Passo 2, carregue a referência indicada no [Mapa de referências](#mapa-de-referências); com perfil Português Simplificado, Assertivo, Enxuto ou Resumo ativo, carregue também a do perfil. Consulte outra referência só quando surgir sinal novo, dúvida de classificação ou sobreposição entre categorias. No `modo_revisão`, inclua sempre [references/padroes-linguagem-ptbr.md](references/padroes-linguagem-ptbr.md). Nenhuma referência substitui a TRAVA FACTUAL: descarte exemplo que exija informação ausente da fonte.

### Passo 4: restauração de especificidade

| Problema | Solução | Exemplo |
|---|---|---|
| Metáfora morta | Cortar ou recuperar uma imagem já presente na fonte | "Ponto de inflexão" → descrever a mudança concreta que a fonte já informa |
| Termo genérico | Recuperar o vocabulário de domínio disponível | "Impacto positivo" → "queda no churn", só se a fonte disser que o churn caiu |
| Molde previsível | Reorganizar o fluxo | Inverter a ordem: exemplo → contexto → tese, sem mudar a relação entre eles |
| Abstração excessiva | Concretizar só com informação disponível | "Muitas pessoas sofrem" → "Muita gente passa por isso" |
| Ritmo monótono | Variar o comprimento das frases | Alternar frases curtas e longas |

Se a concretude necessária não existir na fonte, mantenha a formulação honesta e anote: `⚠️ Falta um dado ou exemplo real para tornar este trecho mais concreto.`

### Passo 5: aplicação da voz

Aplique só os recursos que o perfil ativo permite (tabela Aplicar e Evitar, seção Aplicação da voz por perfil de [references/perfis-voz.md](references/perfis-voz.md)). Com amostra de voz, siga a seção Calibração de voz do mesmo arquivo e nunca copie dela fatos, opiniões, personagens ou experiências. Se a skill `write-like-me` estiver disponível e o texto for escrito em nome do usuário, as referências de estilo que ela recuperar valem como amostra de voz.

### Passo 6: guarda de falso positivo

Antes da verificação final, revise os sinais marcados no Passo 2, desmarque os que esta seção explica e registre a decisão no relatório. Um padrão isolado nunca prova origem artificial: o sinal está no acúmulo. Na dúvida, procure vários padrões no mesmo parágrafo; um travessão sozinho não é nada.

| Não é sinal de IA | Por quê |
|---|---|
| Gramática impecável e estilo constante | Muita gente escreve bem ou passou por edição; texto polido não é texto de máquina |
| Texto seco ou "sem graça" | Escrita de IA tem marcas específicas; secura sem elas é só prosa econômica |
| Palavra formal ou acadêmica isolada | A lista aponta excesso, não proíbe o termo; não simplifique toda palavra difícil |
| Registro jurídico, acadêmico ou normativo | Impessoalidade e passiva são exigência do gênero; não converta petição, laudo ou ata em post de blog |
| Travessão de diálogo em ficção | É norma da língua; o sinal vale para o travessão de aparte |
| Travessão presente na amostra do autor | Mantenha na mesma frequência |
| Conectivo isolado ("no entanto", "portanto") | Só denuncia quando empilhado no início de vários parágrafos seguidos |
| Aspas curvas sozinhas | Editores curvam por padrão; só contam junto com outras marcas |
| Vírgula usada corretamente | Vírgula de vocativo ("Oi, João") é norma |
| Uma frase curta para dar ênfase | Fragmento dramático só quando vários vêm seguidos |
| Repetição proposital de abertura | "Cheguei. Vi. Venci." é ritmo; mexa só quando a repetição não acrescenta nada |
| "Olha" ou "sinceramente" dentro da frase | Normais na fala e no registro informal; o vício é a abertura teatral solta |
| Ressalva com função | Mantenha delimitação de escopo, aviso legal ou de segurança, correção real, objeção com autor nomeado e item de FAQ |
| Alternativa real | Em arquitetura, tutorial ou argumentação, mantenha as opções que o leitor consideraria; corte só a opção improvável levantada e nunca mais usada |
| Ausência de citação | Boa parte do texto publicado não cita fonte |
| Formatação complexa e correta | Editor visual e template produzem saída limpa sem IA |
| Expressão de alerta em segunda mão | Não reescreva a expressão dentro de citação, título, nome próprio ou exemplo em que ela é discutida, não usada |
| Texto anterior a 30/11/2022 | Lançamento público do ChatGPT; o que é mais antigo quase nunca é de IA |
| Negrito em lead-in nos perfis Assertivo e Enxuto | Hierarquia de escaneabilidade, não decoração |
| Seta (→) indicando resultado ou fluxo | Notação do gênero para relação causal |
| Frases de 1 a 3 palavras no perfil Enxuto | Densidade é a estrutura do perfil |
| Checklist com ✅🟡⬜❔🔴 no perfil Resumo | Cada emoji indica um status |
| Listas com 5 ou mais itens no perfil Resumo | Síntese é o formato declarado |
| Parágrafos de uma linha no perfil Assertivo | Uma ideia por bloco é a estrutura do perfil |

Nunca use a pontuação de detectores automáticos como prova nem como critério do que reescrever: eles erram muito, erram torto e penalizam mais quem é neurodivergente e quem não é falante nativo.

Preserve estas marcas humanas e nunca as "conserte" por padronização, salvo quando atrapalham o sentido:

| Marca | Exemplo |
|---|---|
| Contração e fala escrita | "pra", "tá", "cê", "né", "tô", "pro": em registro informal não expanda, é escolha do autor; em texto formal, a forma plena é a correta |
| Regionalismo | "uai", "oxe", "tchê", "massa", "mano": não padronize para um português neutro de manual |
| Detalhe específico e estranho | Um endereço real, uma citação torta, "o advogado que trabalhava em cima do meu dentista" |
| Sentimento misto e tensão sem resolução | "No geral é bom, mas me incomoda, e não sei explicar direito por quê" |
| Gíria e referência datada | Meme e piada interna presos a um ano e a um grupo |
| Aparte, parêntese e autocorreção | "(Fico querendo escrever 'quase' aqui, mas foi certeza mesmo.)" |
| Variação no tamanho das frases | Alternância entre curto e longo; texto de IA tende a um comprimento médio constante |
| Escolha consciente em primeira pessoa | O corte ou a palavra que o autor sabe justificar |

Se a entrada já traz marca forte de autoria (regionalismo, opinião assumida, primeira pessoa, humor, autocorreção, detalhe concreto que só quem viveu conhece), trate-a como escrita de alguém que pede revisão e como amostra de estilo do autor, nunca como saída de chatbot. Nesse caso, os sinais de travessão e de abertura teatral deixam de valer como regra: aponte-os no relatório e deixe a escolha com o autor.

### Passos 7 a 9: verificação, avaliação, tentativas e entrega

Carregue [references/auditoria-entrega.md](references/auditoria-entrega.md): lista do Passo 7, pontuação do Passo 8, laço do Passo 9, contrato de saída e suíte de regressão.

- A candidata que falhar no item 1 (TRAVA FACTUAL) ou no item 2 (argumento, intenção, modalidade e trechos protegidos) do Passo 7 é inválida: descarte-a e registre pontuação `nula`. Nos demais itens, corrija só se houver tentativa disponível, sem distorcer o gênero. Naturalidade nunca compensa alteração factual ou semântica.
- Calcule pontuação só quando o usuário pedir ou fornecer `limiar` (padrão 80), e nunca itere atrás de um número.
- O limite de tentativas do modo (3, 1, 3 e 2) é um máximo, não uma meta. Pare quando outro passe não melhora o resultado e conserve a melhor candidata segura, não a última.
- Sem candidata segura, devolva o `texto_fonte` sem nota, com estado `reprovada_trava_factual`. No `modo_direto`, gere 1 candidata e não repita.
- No `modo_criacao`, reescreva a candidata que falhar no teste factual e nunca a entregue com ressalva. Se faltar dado, entregue a versão mais simples e nomeie a lacuna.

## Estrangeirismos preservados

Preserve estes termos: `feedback, deploy, sprint, churn, feature, bug, hotfix, pipeline, stakeholder, deadline, call, onboarding, pitch, runway, burn rate, product-market fit, growth, awareness, branding, lead, funnel, conversion, landing page, copywriting, UX, UI, framework, stack, backend, frontend, fullstack, DevOps, SaaS, API, endpoint, webhook, dashboard, KPI, OKR, ROI, ROAS, CRM, MVP`.

Estrangeirismo de tecnologia é marca de autenticidade, não erro, e a tradução forçada é sinal de IA purista. Para leitor leigo, mantenha o termo de domínio e explique-o no primeiro uso. Regra de ouro: se o termo é usado no dia a dia do domínio em PT-BR, mantenha; se é anglicismo artificial sem necessidade, remova.

## Avaliação externa com Jev (opcional)

Use TypeSafe Jev só quando o usuário pedir avaliação externa e Jev já estiver disponível; rode antes o protocolo de descoberta de [references/jev-integration.md](references/jev-integration.md). A reescrita continua com o modelo; Jev só avalia, e nenhuma decisão dele supera uma violação semântica detectada. Nunca instale serviços, escolha provedor pago ou delegue automaticamente. Use o banco [assets/jev_questions.json](assets/jev_questions.json) sem modificá-lo.

## Mapa de referências

| Arquivo | Carregue quando |
|---|---|
| [references/palavras-banidas.md](references/palavras-banidas.md) | Antes de escrever ou reescrever qualquer texto; ao rodar a Checklist de saída |
| [references/modo-ingles.md](references/modo-ingles.md) | O texto ou um segmento está em inglês |
| [references/perfis-voz.md](references/perfis-voz.md) | Passos 1 e 5; calibração de voz; perfil Assertivo, Enxuto ou Resumo ativo (seção Perfis de consumo rápido) |
| [references/padroes-conteudo-tom.md](references/padroes-conteudo-tom.md) | Passo 3 com Conteúdo ou Tom marcado |
| [references/padroes-linguagem-ptbr.md](references/padroes-linguagem-ptbr.md) | Passo 3 com Linguagem, PT-BR ou Estrangeirismos marcado; sempre em `modo_revisão` |
| [references/padroes-composicao.md](references/padroes-composicao.md) | Passo 3 com Composição marcado |
| [references/padroes-estilo.md](references/padroes-estilo.md) | Passo 3 com Estilo marcado; dúvida de pontuação, formatação ou ritmo |
| [references/padroes-portugues-simplificado.md](references/padroes-portugues-simplificado.md) | Perfil Português Simplificado ativo |
| [references/auditoria-entrega.md](references/auditoria-entrega.md) | Inventário com várias fontes; Passos 7 a 9; contrato de saída; suíte de regressão |
| [references/jev-integration.md](references/jev-integration.md) | O usuário pede avaliação externa com Jev |
