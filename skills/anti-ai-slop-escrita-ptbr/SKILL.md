---
name: anti-ai-slop-escrita-ptbr
description: >-
  Escreve e reescreve texto em português brasileiro (e em inglês, pelo modo próprio) sem marcas de escrita de IA, preservando fatos, números, fontes, modalidade e argumento. Use para tirar cara de IA, remover AI slop, anti-AI slop em texto, humanização de texto, palavras banidas, linguagem simples, revisão anti-IA e para escrever do zero qualquer texto que alguém vai assinar ou publicar: post de LinkedIn, tweet, thread, e-mail, artigo, proposta, release, README, bio, legenda, carta de apresentação, relatório, descrição de produto, mensagem de WhatsApp ou Slack, status update. Aciona com pedidos como escreva, redija, reescreva, deixe mais humano, sem cara de ChatGPT, simplifique, direto ao ponto, resumo de status, e com pedidos em inglês como write, draft, rewrite, make this sound human, not AI. Aplica perfis de voz (crônica, jornalístico, acadêmico, jurídico, didático, assertivo, enxuto, resumo e outros), lista de palavras banidas, regras de estrutura e pontuação, guarda de falso positivo e trava factual.
license: Apache-2.0
metadata:
  author: "https://ft.ia.br"
  version: "1.0.0"
  source: "Fusão de fabricioctelles/skills v1.7.0 (PT-BR, Apache 2.0) e Anti-AI-Slop Writing Directive v2"
  repository: "https://github.com/fabricioctelles/skills"
  upstream_version: "1.7.0"
  upstream_date: "2026-10-10"
  attribution: "Inventário e auditoria adaptados de phuryn/work-humanizer, commit 0a9065791d021f3dda695f3887cb2ae4c0eacbcf; tropos de tropes.fyi; ablação semântica de The Register (fev 2026); Português Simplificado baseado em PorSimples (NILC/USP), Lei 15.263/2025, NILC-Metrix e SIMPLEX-PB"
  category: "code-quality-and-review"
  license-compliance: "Apache-2.0 herdada de fabricioctelles/skills v1.7.0; obra derivada com alterações (consolidação e reescrita ASD-STE100 em 2026-10-23); mantenha esta atribuição ao redistribuir"
  consolidated: "2026-10-23 ASD-STE100 rewrite"
  merged-from: "fabricioctelles/skills v1.7.0 (skill PT-BR de escrita); Anti-AI-Slop Writing Directive v2 (skill EN de escrita)"
---

> **⚠️ DIRETRIZ DE EXECUÇÃO (SEPARAÇÃO INPUT vs. OUTPUT):**
> As regras desta skill estão escritas no padrão técnico ASD-STE100 exclusivamente para precisão lógica de leitura e economia de tokens.
> - **PROIBIDO copiar este estilo seco, telegráfico ou fragmentado no texto final (Output).**
> - Ao escrever roteiros, textos, artigos, legendas ou copys, entregue um texto 100% fluido, natural, humano e com ritmo orgânico em PT-BR.
> - **Única exceção:** Aplique cerca de 80% do padrão ASD-STE100 no texto final apenas em trechos específicos que exijam explicar um conceito técnico muito complexo de forma simples.

# anti-AI-slop-escrita-PTBR

- Remova sinais de escrita mecânica de IA.
- Recupere ritmo, precisão e voz sem criar uma nova história.
- Melhore o texto. Nunca tente enganar detectores.
- Nunca garanta que uma ferramenta de detecção classificará o resultado como humano.

## Escopo e idioma

- Escreva e reescreva em PT-BR por padrão.
- Aplique as regras deste arquivo a todo texto, em qualquer idioma.
- Para texto em inglês, carregue [references/modo-ingles.md](references/modo-ingles.md).
- Em texto multilíngue, aplique as regras de cada idioma ao seu segmento.
- Preserve os segmentos escritos em outros idiomas.
- Não aplique ao inglês as convenções do PT-BR (sem vírgula Oxford, ponto fora das aspas, títulos sem Title Case, aspas retas).

## Palavras banidas

- Carregue references/palavras-banidas.md antes de escrever ou reescrever qualquer texto. [Abrir arquivo](references/palavras-banidas.md).
- Rode a Checklist de saída de references/palavras-banidas.md antes de entregar. [Abrir checklist](references/palavras-banidas.md).
- Nunca use item da lista em texto que você gera (`modo_criacao` e toda frase nova).
- Troque o item da lista por alternativa concreta que a fonte sustenta, ou reestruture a frase.
- Em texto existente do autor, aplique a guarda de acúmulo do Passo 6: palavra formal isolada não é sinal.

## Proteções obrigatórias

1. **TRAVA FACTUAL (definição canônica).**
   - Trate o texto-fonte como imutável.
   - Preserve: nomes, números, datas, citações, fontes, exemplos, relações causais, modalidade (certeza, dúvida, obrigação ou possibilidade), estado temporal, responsáveis, compromissos, prazos, condições, exceções, avisos, argumento, intenção, código e notação.
   - Condense, reorganize e reformule quando necessário.
   - Nunca acrescente, retire ou altere os elementos acima sem autorização explícita do usuário.
   - Nunca invente vivência pessoal, anedota, estatística, fonte, exemplo, benefício, promessa ou pedido de desculpas para dar concretude ou calor ao texto.
2. **Concretude sem invenção.**
   - Reutilize detalhes já presentes.
   - Mantenha lacunas fora do texto publicável.
   - Use marcador apenas em rascunho de trabalho solicitado.
   - Se faltar dado essencial: preserve a generalidade, peça o dado ao usuário ou, em rascunho de trabalho, marque `[DADO OU EXEMPLO REAL NECESSÁRIO]`.
   - Crie conteúdo fictício somente quando o usuário pedir. Identifique-o como fictício.
3. **Argumento preservado.** Mantenha a posição e a conclusão do autor, mesmo que você discorde delas.
4. **Registro preservado.**
   - Não force informalidade, primeira pessoa, humor ou opinião.
   - Use o perfil de voz para orientar a forma. O perfil nunca autoriza conteúdo novo.
5. **Precisão antes de estilo.**
   - Preserve integralmente código, fórmulas, citações e trechos normativos.
   - Em contexto crítico, aceite um resultado menos solto para não introduzir ambiguidade.
6. **Sem infantilização.** Nunca simplifique o raciocínio ao simplificar a forma.

- Remeta toda verificação de **TRAVA FACTUAL** a esta definição.
- Em conflito com exemplos ou referências, aplique estas proteções.

## Triagem obrigatória

Execute antes de diagnosticar ou reescrever:

1. Confirme que há material: texto, notas ou transcrição.
   - Em `modo_criacao` não há texto-fonte: confirme tema, gênero e material factual disponível antes de escrever.
   - Para inglês, siga [references/modo-ingles.md](references/modo-ingles.md).
   - Em texto multilíngue, aplique as regras de cada idioma ao seu segmento e preserve os demais.
2. Não reescreva bulas, procedimentos médicos, manuais de aviação ou outros textos de segurança crítica.
3. Não reescreva contratos, leis, cláusulas ou documentos legais que sejam a própria referência normativa.
   - Use o perfil Jurídico apenas para comentários, resumos e peças autorais.
   - Nunca altere texto normativo.
4. Em traduções literais bilíngues ou conteúdo avaliado por correspondência exata, não varie a redação.
5. Em textos técnicos, identifique antes da reescrita os trechos protegidos: código, equações, comandos, citações e identificadores.
6. Quando a tarefa estiver fora do escopo, explique o risco.
   - Ofereça apenas revisão superficial, se for seguro e o usuário autorizar.

## Modos de operação

- Use o modo para definir o nível do relatório e o número máximo de tentativas.
- Nunca use o modo para alterar as proteções.

| Modo | Quando usar | Tentativas máximas | Entrega |
|---|---|---:|---|
| `modo_completo` (padrão) | Pedido comum de humanização | 3 | Texto final e resumo das mudanças; pontuação somente se solicitada |
| `modo_direto` | Fluxo automatizado ou pedido de rapidez | 1 | Texto final e relatório sintético; sem repetição automática |
| `modo_revisão` | Auditoria de texto produzido por outro agente | 3 | Texto final, diagnóstico e relatório detalhado |
| `modo_criacao` | O texto ainda não existe; o usuário pede para escrever | 2 | Somente o texto final |

- Use `modo_criacao` quando não existir `texto_fonte`. Nenhum outro modo vale sem `texto_fonte`.
- Em `modo_criacao`, aplique as mesmas proteções.
- Em `modo_criacao`, aplique a lista de padrões como filtro de saída sobre o próprio rascunho, nunca como conserto de um original. Veja [Escrita do zero](#escrita-do-zero-modo_criacao).
- Preserve sempre o modo escolhido pelo usuário.
- Sem modo informado e com 5 ou mais sinais graves no diagnóstico, use `modo_revisão`.
- Em texto com mais de 500 palavras, trabalhe por blocos semânticos.
- Faça uma verificação global depois de recompor o texto.

## Inventário e perguntas

- Antes de editar ou criar, inventarie: afirmações, responsáveis, força de cada compromisso, prazos, condições e proveniência.
- Confira depois nos dois sentidos: tudo que estava protegido sobrevive; tudo que entrou tem respaldo.
- Em texto curto, faça o inventário mentalmente.
- Com múltiplas fontes, notas, transcrições ou lacunas essenciais, carregue [references/auditoria-entrega.md](references/auditoria-entrega.md).
- Trate notas e transcrições do autor como base principal. Preserve seu raciocínio e suas expressões. Use eventual rascunho de IA só como apoio.
- Resolva conflitos de fontes sem inventar nem excluir informação em silêncio.
- Pergunte apenas sobre lacunas reais. Faça no máximo 3 perguntas, em uma rodada.
- Nunca inicie entrevista automática no `modo_direto` nem em pipeline sem interlocutor.
- Nunca trate resposta ausente como autorização para inventar ou cortar conteúdo protegido.
- Mantenha as fontes imutáveis. Registre separadamente as adições aprovadas pelo usuário.

## Regras de escrita limpa (todo texto)

- Aplique estas regras a todo texto que você escrever ou reescrever.
- Em reescrita, nunca acrescente, retire ou altere conteúdo protegido para cumprir uma regra.
- Se uma regra conflitar com a TRAVA FACTUAL, aplique a TRAVA.

### Estrutura

- Evite a regra de três. Use dois, quatro, um ou cinco itens. Use três apenas quando o conteúdo tem exatamente três itens.
- Em reescrita, quebre a simetria de 3 ou mais itens sem acrescentar nem retirar itens.
- Nunca escreva 3 frases consecutivas com o mesmo comprimento.
- Misture frases de 4 palavras com frases de 30 palavras.
- Em Português Simplificado, limite a frase a 25 palavras (alvo de 13 a 18). Esse limite prevalece.
- Em parágrafo com menos de 3 frases, não exija 3 tamanhos distintos.
- Não encadeie 3 ou mais frases curtas declarativas seguidas (parataxe).
- Una as ideias com oração subordinada, conjunção, ponto e vírgula ou vírgula. Mostre causa, contraste e qualificação.
- Isente da regra de parataxe: Português Simplificado, Assertivo, Enxuto, Resumo e voz de autor cuja amostra usa fragmentos.
- Exemplo (EN, original): "Short sentence. Then another. Then another." vira "AI chains short sentences together because it's easier than constructing a thought with actual connective tissue."
- Nunca alterne ressalvas dos dois lados (gangorra).
- Em `modo_criacao`, assuma posição somente se o material do usuário a sustenta. Dê ao contraponto no máximo 1 frase.
- Em reescrita, mantenha a modalidade da fonte. Nunca aumente a certeza.
- Use qualificador apenas para incerteza real, nunca por hábito de ressalva.
- Não use tom de torcida corporativa. Escreva como quem tem experiência.
- Inclua atrito, dúvida ou bagunça apenas quando a fonte ou o usuário os trouxer.
- Não repita em todo parágrafo a sequência frase-tópico, explicação, exemplo, transição.
- Comece alguns parágrafos com pergunta e outros com afirmação direta. Deixe alguns com uma frase só.
- Pare o parágrafo quando a ideia fechar. Não termine todo parágrafo com resumo ou transição.
- Em reescrita, reordene apenas as proposições existentes.
- Use bullets com moderação. Escreva no máximo 5 bullets seguidos em perfil autoral ou neutro. Português Simplificado e Resumo ficam isentos.
- Faça os bullets desiguais. Se cabe numa frase, escreva uma frase.
- Em `modo_criacao`, não abra com "Como [cargo], eu...".
- Em reescrita, mova a credencial para fora da abertura sem apagá-la.
- Varie o tratamento e o comprimento das seções. Não dê estrutura paralela a pontos diferentes.
- Use voz ativa. A passiva é legítima quando o agente é desconhecido ou irrelevante e em gêneros formais (jurídico, acadêmico, normativo).
- Nunca invente um agente para eliminar a passiva. Sinalize 3 ou mais passivas consecutivas.
- Permita fragmento ou frase longa encadeada apenas em perfil autoral cuja voz os sustenta.
- Limite fragmentos dramáticos a 1 por texto fora do Twitter.

### Pontuação

- Substitua todo travessão (—), meia-risca (–) ou " -- " usado como aparte por vírgula, ponto, dois-pontos ou parênteses, ou reescreva a frase.
- Preserve o travessão nestes casos: diálogo em ficção, frequência da amostra do autor, citação, título ou exemplo.
- Use no máximo 1 exclamação por 1.000 palavras. Expresse entusiasmo pela escolha das palavras.
- Use reticências apenas quando a frase realmente se perde. Nunca as use como transição. Use no máximo 1 por texto.
- Trate "..." como notação em lista de gatilhos, não como reticências.
- Use ponto e vírgula para ligar orações relacionadas.
- Use dois-pontos para preparar um ganho. Faça o que vem depois cumprir a promessa de antes.
- Em PT-BR, não coloque vírgula antes de "e" ou "ou" final de lista. Mantenha a vírgula quando o "e" liga orações de sujeitos diferentes.
- Em PT-BR, coloque o ponto fora das aspas quando a citação é parte da frase. Coloque o ponto dentro quando a citação é frase completa.
- Em PT-BR, use aspas retas em texto informal ou técnico. Nunca misture aspas curvas e retas.
- Em PT-BR, escreva títulos em caixa de frase, nunca em Title Case.
- Consulte [references/padroes-estilo.md](references/padroes-estilo.md) para os detalhes.

### Formatação por canal

- Não use cabeçalhos markdown em redes sociais, e-mail ou texto casual.
- Não use negrito aleatório para ênfase em redes sociais.
- Perfis de leitura rápida (Assertivo, Enxuto e Resumo) podem usar negrito em abertura de item como hierarquia.
- Não use emoji como marcador. Use 1 ou 2 emoji por post, no máximo.
- Nunca comece toda linha com ✅ ou 🔥.
- No perfil Resumo, use ✅🟡⬜❔🔴 como notação funcional de status.
- Proíba emoji decorativo (🚀💡🎯✨).
- Não abra com "🧵", "Thread:" ou "Fio:".
- Use 0 a 2 hashtags, integradas ao texto. Nunca empilhe hashtags.
- Não use markdown em texto simples (e-mail, DM, SMS). Asteriscos aparecem como símbolos.

### Especificidade sem invenção

- Seja específico. Use dado, nome, data ou número apenas se estiver na fonte ou no material do usuário.
- Mostre em vez de descrever.
- Use números reais. Nunca crie número aproximado.
- Use "cerca de" ou "aproximadamente" apenas quando o número da fonte já é aproximado.
- Nomeie coisas reais citadas na fonte. Use nomes, empresas e datas verificáveis.
- Inclua tempo, lugar e contexto apenas quando a fonte os trouxer.
- Sem o dado necessário, mantenha a generalidade e sinalize a lacuna. Prefira a vagueza honesta à especificidade fabricada.
- Nunca invente anedota, dado, estudo, estatística ou citação. Parafraseie com atribuição ou omita.
- Nunca apresente hipótese como fato. Marque hipótese com "Suponha que" ou "Por hipótese".
- Nunca abra com "Imagine um mundo onde" nem com "Imagine se".
- Evite a palavra de maior probabilidade (o clichê). Em Português Simplificado, a regra R4 (palavras comuns) prevalece.
- Nunca alterne sinônimos só para variar a palavra (padrão Variação lexical forçada em [references/padroes-linguagem-ptbr.md](references/padroes-linguagem-ptbr.md)).
- Em PT-BR, use contrações como "pra", "tá" e "né" apenas em perfil informal ou quando a fonte já as usa.
- Para contrações em inglês, siga [references/modo-ingles.md](references/modo-ingles.md).
- Sem perfil nem amostra, use voz neutra. Nunca force informalidade.
- Não explique demais. Confie no leitor. Comece uma frase com "E" ou "Mas" só quando isso mantiver a relação lógica.
- Para calibrar a voz de uma pessoa específica, siga a seção Calibração de voz em [references/perfis-voz.md](references/perfis-voz.md).
- Para os pares de exemplo em inglês, consulte [references/modo-ingles.md](references/modo-ingles.md).

### Aplicação silenciosa

- Aplique todas as regras sem mencioná-las.
- Nunca escreva "as per the guidelines" nem "conforme as diretrizes" no texto entregue.
- Em `modo_criacao`, entregue somente o texto.
- Nos modos que exigem relatório, escreva o relatório fora do texto entregue.
- Nunca afirme ter feito uma checagem que você não rodou.
- Rode esta checagem de prioridade antes de entregar:
  1. Verifique palavra ou frase banida. Troque.
  2. Verifique 3 frases consecutivas do mesmo comprimento. Varie.
  3. Verifique 3 ou mais frases curtas declarativas seguidas (parataxe). Una com conjunção, oração ou pontuação.
  4. Verifique agrupamento em trios. Quebre o padrão.
  5. Verifique ressalva no lugar de compromisso. Assuma posição só em `modo_criacao` e com respaldo.
  6. Verifique travessão de aparte. Remova todos.
  7. Verifique voz passiva com agente conhecido. Passe para a ativa.
  8. Verifique parágrafos que terminam todos em transição. Corte alguns.
  9. Verifique especificidade inventada. Remova ou marque como hipótese.
  10. Pergunte se qualquer IA poderia escrever isto para qualquer pessoa. Se sim, acrescente detalhe da fonte ou sinalize a lacuna.
  11. Pergunte se o texto soa como ChatGPT. Reescreva até a resposta ser não, dentro do limite de tentativas do modo.
- Use a lista completa em [references/auditoria-entrega.md](references/auditoria-entrega.md) (Passo 7).

## Escrita do zero (`modo_criacao`)

- Use a lista de padrões como filtro de saída, nunca como conserto, quando o texto ainda não existe.

1. Escolha o perfil de voz antes de escrever (Passo 1). Sem perfil e sem amostra, use voz neutra.
2. Escreva direto, com o inventário e o material factual aprovado.
   - Com notas ou transcrição, preserve o raciocínio, a ordem e as expressões do autor.
   - Não tente desviar dos padrões durante a redação.
3. Rode o diagnóstico sobre o próprio rascunho (Passo 2) antes de entregar. Varra estes 5 padrões primeiro:
   - travessão de aparte;
   - "não apenas X, mas também Y";
   - conectivo abrindo parágrafo ("Além disso", "Dessa forma", "Por fim");
   - trio forçado;
   - fecho otimista genérico.
4. Percorra o resto da tabela do Passo 2 depois dos 5 padrões.
5. Aplique a guarda de falso positivo (Passo 6) e a verificação final (Passo 7).
6. Entregue só o texto. Sem rascunho, sem diagnóstico, sem lista de padrões.

**TRAVA FACTUAL em `modo_criacao`.**
- Use apenas o que o usuário forneceu ou o que você verificou de fato.
- Nunca tape buraco com número plausível, data aproximada ou fonte que soa certa.
- Se faltar dado para a frase funcionar, escreva a frase mais simples e diga ao usuário o que falta.
- Em rascunho de trabalho, marque `[DADO OU EXEMPLO REAL NECESSÁRIO]`.
- Trate ficção pedida explicitamente como exceção. Identifique-a como ficção.
- Nunca anuncie que passou pela lista.
- Nunca afirme ter conferido um texto sem ter conferido.

## Processo

- Execute primeiro a **Triagem obrigatória** e o inventário semântico.
- Mantenha `texto_fonte` imutável durante todo o processo.
- Em `modo_criacao` não há `texto_fonte`: o rascunho da primeira tentativa ocupa o lugar de `texto_atual`.
- Em `modo_criacao`, siga a validação factual de [Escrita do zero](#escrita-do-zero-modo_criacao).

### Passo 1: seleção do perfil de voz

- Detecte o perfil pelo conteúdo quando o usuário não especificar um.

| Sinal no texto | Perfil sugerido |
|---|---|
| Citações legais, artigos de lei, "art.", "§", "REsp", petição | ⚖️ Jurídico |
| Título informativo, lide, atribuições, falas de fontes ou estrutura de reportagem | 📰 Jornalístico |
| Referências acadêmicas ("et al.", metodologia, hipótese, valor-p) | 🎓 Acadêmico |
| Tutorial, documentação amigável, "passo a passo" ou "vamos ver" | 🧑‍🏫 Didático |
| E-mail ou mensagem profissional com jargão técnico e nomes de ferramentas | 💬 Corporativo Informal |
| Texto ≤100 palavras, frases incompletas, abreviações, gírias | 📲 WhatsApp |
| Texto curto (<300 palavras), opinativo, em 1ª pessoa, sem estrutura formal | 📱 Post de Rede Social |
| ≥1500 palavras, narrativo, sem jargão dominante | 🖋️ Crônica |
| Texto institucional/governamental, manual de produto, FAQ, pedido de "simplificar" ou "linguagem simples" | 📋 Português Simplificado |
| Resposta a decisão, briefing, "direto ao ponto", estrutura pergunta-resposta com escopo técnico | ➡️ Assertivo |
| Contexto de coding/debugging, comandos, troubleshooting, confirmação de ação, respostas curtas | 🔹 Enxuto |
| Status update, standup, sprint review, "como está X?", "resumo de status", notas de reunião | 📊 Resumo |
| **Nenhum sinal claro** | Voz neutra — preservar o registro original e apenas remover padrões mecânicos |

Regras de decisão:

1. Use o perfil explícito como limite do gênero. Nunca o substitua automaticamente.
2. Dentro desses limites, deixe a amostra fornecida controlar as escolhas finas de estilo. Sem perfil explícito, a amostra tem prioridade sobre a detecção.
3. Sem perfil nem amostra, use o perfil detectado. Sem sinal claro, use voz neutra.
4. Em conflito material, pergunte ao usuário nos modos completo e revisão.
   - No `modo_direto`, escolha o registro mais próximo do texto-fonte, aja de modo conservador e registre a ambiguidade.
5. Em texto com múltiplos registros, mantenha um perfil principal. Ajuste apenas os trechos que pertencem a outro gênero.

> **Saída no relatório**: `🎯 Tipo detectado: [tipo] → Perfil: [perfil]`

- Carregue [references/perfis-voz.md](references/perfis-voz.md) para as características e os exemplos de cada perfil.

### Passo 2: diagnóstico

- Percorra cada categoria da tabela. Marque ✓ (encontrado) ou ✗ (ausente).

| Categoria | Sinal | Peso (1-3) | ✓/✗ | Ação |
|---|---|---|---|---|
| **Conteúdo** | Atribuição vaga ("estudos mostram", "especialistas dizem") | 3 | | Preservar a atribuição; especificar somente se a fonte já estiver na entrada e, caso contrário, sinalizar a lacuna no relatório |
| | Ênfase inflada sem base ("revolucionário", "sem precedentes") | 3 | | Preservar força e autoria da avaliação; sugerir redução no relatório, sem alterá-la sem autorização |
| | Dados possivelmente fabricados ou imprecisos | 3 | | Preservar no texto e sinalizar para verificação; corrigir apenas com fonte ou autorização do usuário |
| | Fonte específica cuja existência não se confirma (autor, ano, DOI, link, número de página) | 3 | | Não corrigir nem trocar a referência; marcar para verificação e retirar a afirmação que dependa só dela |
| **Linguagem** | Vocabulário genérico ("impacto", "contexto", "cenário") | 3 | | Trocar por termo preciso já sustentado pela fonte |
| | Perífrases rebuscadas para evitar "ser", "ter" ou "estar" | 2 | | Restaurar o verbo simples quando natural ao registro |
| | Paralelismo perfeito em 3+ itens | 2 | | Quebrar a simetria |
| **Tom** | Ressalva excessiva ("pode ser que talvez", "parece que") | 2 | | Cortar redundância sem aumentar a certeza |
| | Autorreferência de IA ("como modelo de linguagem...") | 3 | | Remover o aviso padrão sem criar opinião |
| | Inflação de gravidade ("questão crucial para a humanidade") | 2 | | Reduzir a escala sem criar comparação nova |
| | Máxima de camiseta ("X é a linguagem de Y", "X não é ferramenta, é espelho") | 2 | | Trocar a frase de efeito pela afirmação específica que ela substitui |
| **Composição** | Molde introdutório ("Neste artigo, exploraremos...") | 3 | | Cortar e ir direto ao conteúdo existente |
| | Conclusão em molde ("em resumo", "conclui-se que") | 3 | | Enxugar ou reorganizar a conclusão existente |
| | Transições artificiais ("primeiramente", "em segundo lugar") | 2 | | Usar conectivos naturais |
| | Primeira frase repete o título | 1 | | Cortar a frase repetida e começar pelo conteúdo |
| | Alternativa falsa levantada e descartada em meia frase | 2 | | Remover a opção descartada e manter apenas a restrição real |
| | Documentação que descreve a versão anterior em vez do comportamento atual | 2 | | Descrever o estado atual; preservar o histórico apenas em changelog, nota de versão e guia de migração |
| **Estilo** | Travessão (—) ou meia-risca (–) usados como aparte no meio da frase | 2 | | Substituir por vírgula, ponto, dois-pontos ou parênteses, ou reescrever a frase. Exceções no Passo 6 |
| | Negrito ou formatação excessiva | 1 | | Moderar conforme o gênero |
| | Emoji em cada item (padrão ChatGPT) | 1 | | Remover os que não têm função |
| | Markdown não solicitado (títulos e listas automáticas em prosa) | 2 | | Remover quando não servir ao gênero |
| **PT-BR** | Oficialês ("cumpre salientar", "no âmbito de") | 2 | | Substituir por construção direta |
| | Gerundismo ("vamos estar analisando") | 2 | | Converter para forma verbal direta |
| | ENEM-ismo (frase de efeito genérica no final) | 2 | | Trocar por reflexão específica |
| **Estrangeirismos** | Tradução forçada de termos de tecnologia | 2 | | Restaurar o termo consagrado no domínio |
| | Uso artificial de anglicismos fora de contexto técnico | 1 | | Remover |

- Conte cada linha detectada como um sinal, independentemente do número de repetições.
- Se encontrar 5 ou mais sinais de peso 3 e o usuário não tiver escolhido um modo, use `modo_revisão`.
- No perfil Jurídico, trate o oficialês como possivelmente deliberado.
- No perfil Jurídico, avalie repetição mecânica e falta de função, nunca a mera presença da expressão.

- Para métricas quantitativas opcionais (TTR, desvio-padrão de frases, entropia, `-mente`, `-ando/-endo/-indo`), carregue [references/auditoria-entrega.md](references/auditoria-entrega.md) somente quando o usuário pedir métricas.

### Passo 3: remoção de padrões

- Comece pelas referências das categorias marcadas ✓ no diagnóstico:

| Categoria com ✓ no Passo 2 | Arquivo inicial |
|---|---|
| Conteúdo | [references/padroes-conteudo-tom.md](references/padroes-conteudo-tom.md): atribuições vagas, ênfase inflada |
| Linguagem | [references/padroes-linguagem-ptbr.md](references/padroes-linguagem-ptbr.md): vocabulário IA, copulativas, paralelismos |
| Tom | [references/padroes-conteudo-tom.md](references/padroes-conteudo-tom.md): adulação, ressalvas e inflação de gravidade |
| Composição | [references/padroes-composicao.md](references/padroes-composicao.md): moldes e conclusões previsíveis |
| Estilo | [references/padroes-estilo.md](references/padroes-estilo.md): formatação, travessão, negrito e emojis |
| PT-BR ou Estrangeirismos | [references/padroes-linguagem-ptbr.md](references/padroes-linguagem-ptbr.md): gerundismo, oficialês e ENEM-ismo |
| Português Simplificado (perfil ativo) | [references/padroes-portugues-simplificado.md](references/padroes-portugues-simplificado.md): operações, substituições lexicais e métricas |
| Perfil Assertivo, Enxuto ou Resumo ativo | [references/perfis-voz.md](references/perfis-voz.md) (seção Perfis de consumo rápido): formatação, regras de corte, exceções |

- Consulte também a referência relacionada quando surgir outro sinal durante a reescrita, houver dúvida de classificação ou houver sobreposição entre categorias.
- Não carregue todas as referências por padrão.
- No `modo_revisão`, inclua sempre [references/padroes-linguagem-ptbr.md](references/padroes-linguagem-ptbr.md).
- Nunca use uma referência para substituir a **TRAVA FACTUAL**.
- Descarte qualquer exemplo de referência que exija informação ausente do texto-fonte.

### Passo 4: restauração de especificidade

- Restaure precisão e ritmo onde o texto os perdeu:

| Problema | Solução | Exemplo |
|---|---|---|
| Metáfora morta | Cortar ou recuperar uma imagem já presente na fonte | "Ponto de inflexão" → descrever a mudança concreta que a fonte já informa |
| Termo genérico | Recuperar o vocabulário de domínio disponível | "Impacto positivo" → "queda no churn", somente se a fonte disser que o churn caiu |
| Molde previsível | Reorganizar o fluxo | Inverter ordem: exemplo → contexto → tese, sem mudar a relação entre eles |
| Abstração excessiva | Concretizar apenas com informação disponível | "Muitas pessoas sofrem" → "Muita gente passa por isso" |
| Ritmo monótono | Variar comprimento de frases | Alternar frases curtas com longas |

- Se a concretude necessária não existir na fonte, mantenha a formulação honesta.
- Anote nesse caso: `⚠️ Falta um dado ou exemplo real para tornar este trecho mais concreto.`

### Passo 5: aplicação da voz

- Aplique somente os recursos que o perfil ativo permite.
- Consulte a tabela Aplicar e Evitar na seção Aplicação de [references/perfis-voz.md](references/perfis-voz.md).
- Quando o usuário fornecer amostra de voz, espelhe: comprimento de frases, nível vocabular, início de parágrafos, pontuação e uso de estrangeirismos.
- Nunca copie fatos, opiniões, personagens ou experiências da amostra para o texto reescrito.

### Passo 6: guarda de falso positivo

- Rode antes da verificação final.
- Percorra os sinais marcados ✓ no Passo 2. Desmarque os que esta seção explica. Registre a decisão no relatório.
- Nunca trate um padrão isolado como prova de origem artificial: o sinal está no acúmulo.
- Na dúvida, procure vários padrões no mesmo parágrafo. Um travessão sozinho não é nada.

#### O que não marcar

| Não é sinal de IA | Por quê |
|---|---|
| Gramática impecável e estilo constante | Muita gente escreve bem ou passou por edição. Texto polido não é texto de máquina |
| Texto seco ou "sem graça" | Escrita de IA tem marcas específicas. Secura sem essas marcas é só prosa econômica |
| Palavra formal ou acadêmica isolada | A lista de vocabulário aponta excesso, não proíbe o termo. Não simplificar toda palavra difícil |
| Registro jurídico, acadêmico ou normativo | Impessoalidade e voz passiva são exigência do gênero. Não converter petição, laudo ou ata em post de blog |
| Travessão de diálogo em ficção | É norma da língua. O sinal do Passo 2 vale para o travessão de aparte, não para a fala |
| Travessão presente na amostra do autor | Se a amostra usa, manter na mesma frequência |
| Conectivo isolado ("no entanto", "portanto") | Só denuncia quando empilhado no início de vários parágrafos seguidos |
| Aspas curvas sozinhas | Word, Google Docs e a maioria dos editores curvam por padrão. Só contam junto com outras marcas |
| Vírgula usada corretamente | Vírgula de vocativo ("Oi, João") é norma. Pontuação correta não indica nada |
| Uma frase curta para dar ênfase | Só marcar fragmento dramático quando vierem vários seguidos |
| Repetição proposital de abertura | "Cheguei. Vi. Venci." é ritmo. Só mexer quando a repetição não acrescenta nada |
| "Olha" ou "sinceramente" dentro da frase | Normais na fala e no registro informal. O vício é a abertura teatral solta |
| Ressalva com função | Manter delimitação de escopo, aviso legal ou de segurança, correção real, objeção com autor nomeado e item de FAQ |
| Alternativa real | Em documento de arquitetura, tutorial ou argumentação, manter as opções que o leitor consideraria. Cortar só a opção improvável levantada e nunca mais usada |
| Ausência de citação | Boa parte do texto publicado não cita fonte. Falta de citação não prova nada |
| Formatação complexa e correta | Editor visual e template produzem saída limpa sem IA nenhuma |
| Expressão de alerta em segunda mão | Não reescrever expressão que aparece dentro de citação, título, nome próprio ou exemplo em que ela está sendo discutida, não usada |
| Texto anterior a 30/11/2022 | Lançamento público do ChatGPT. O que é mais antigo quase nunca é de IA |
| Negrito em lead-in nos perfis Assertivo/Enxuto | Funciona como hierarquia de escaneabilidade, não decoração |
| Seta (→) indicando resultado ou fluxo | Notação específica do gênero — indica relação causal, não decora |
| Frases de 1-3 palavras no perfil Enxuto | Densidade é a estrutura do perfil, não fragmento dramático |
| Checklist com ✅🟡⬜❔🔴 no perfil Resumo | Estado funcional, não decoração — cada emoji indica um status |
| Listas com 5+ itens no perfil Resumo | Síntese é o formato declarado — não é listicle disfarçado |
| Parágrafos de uma linha no perfil Assertivo | Uma ideia por bloco é a estrutura do perfil |

**Detectores automáticos.**
- Nunca use a pontuação de ferramenta de detecção como prova nem como critério do que reescrever.
- Essas ferramentas erram muito e erram torto: penalizam mais quem é neurodivergente e quem não é falante nativo.
- Nenhuma reescrita aqui tem como objetivo enganar detector.

#### Marcas humanas para preservar

- Preserve estes detalhes de voz.
- Exceção: o detalhe atrapalha o sentido.
- Nunca "conserte" estes detalhes por padronização.

| Marca | Exemplo |
|---|---|
| Contração e fala escrita | "pra", "tá", "cê", "né", "tô", "pro". Em registro informal, não expandir para "para", "está", "você" — a forma contraída é escolha do autor. Em texto formal, aí sim a forma plena é a correta |
| Regionalismo | "uai", "oxe", "tchê", "massa", "mano". Não padronizar para um português neutro de manual |
| Detalhe específico e estranho | Um endereço real, uma citação torta, "o advogado que trabalhava em cima do meu dentista" |
| Sentimento misto e tensão sem resolução | "No geral é bom, mas me incomoda, e não sei explicar direito por quê" |
| Gíria e referência datada | Meme e piada interna presos a um ano e a um grupo |
| Aparte, parêntese e autocorreção | "(Fico querendo escrever 'quase' aqui, mas foi certeza mesmo.)" |
| Variação no tamanho das frases | Alternância entre curto e longo. Texto de IA tende a um comprimento médio constante |
| Escolha consciente em primeira pessoa | O corte ou a palavra que o autor sabe justificar |

**O próprio texto como amostra.**
- Se a entrada já traz marca forte de autoria, trate-a como escrita de alguém que pede revisão, nunca como saída de chatbot.
- Marcas fortes de autoria: regionalismo, opinião assumida, primeira pessoa, humor, autocorreção, detalhe concreto que só quem viveu conhece.
- Trate esse texto como a amostra de estilo do autor.
- Nesse caso, o sinal de travessão e o de abertura teatral deixam de valer como regra.
- Aponte no relatório o que encontrar. Deixe a escolha com o autor.

### Passos 7 a 9: verificação, avaliação, tentativas e entrega

- Carregue [references/auditoria-entrega.md](references/auditoria-entrega.md) para a lista completa do Passo 7, a pontuação do Passo 8, o laço de tentativas do Passo 9, o contrato de saída e a suíte de regressão.
- Audite primeiro nos dois sentidos contra o texto-fonte e as adições aprovadas. Em criação, audite contra o material factual aprovado.
- Invalide a candidata que falhar no item 1 (TRAVA FACTUAL) ou no item 2 (argumento, intenção, modalidade e trechos protegidos) do Passo 7.
- Nos demais itens, corrija apenas se ainda houver tentativa disponível. Não distorça o gênero para satisfazer a lista.
- Valide a TRAVA FACTUAL antes da avaliação de estilo. Se falhar, descarte a candidata e registre pontuação `nula`.
- Nunca deixe a naturalidade compensar alteração factual ou semântica.
- Calcule pontuação somente quando o usuário pedir ou fornecer `limiar`. Use 80 se o usuário pedir nota sem limiar.
- Sem pontuação, avalie de forma qualitativa. Nunca itere para alcançar um número.
- Respeite o limite de tentativas do modo (3, 1, 3 e 2 na tabela de modos). O limite é um máximo, não uma meta.
- Pare quando outro passe não melhorar o resultado.
- Conserve a melhor candidata segura, não necessariamente a última.
- No `modo_direto`, produza exatamente uma candidata e não repita. Se ela falhar na TRAVA FACTUAL, devolva o texto-fonte com estado `reprovada_trava_factual`.
- Se nenhuma candidata for segura, devolva o `texto_fonte` sem nota, com estado `reprovada_trava_factual`.
- No `modo_criacao`, reescreva a candidata que não passar no teste factual. Nunca a entregue com ressalva.
- No `modo_criacao`, se faltar dado, entregue a versão mais simples e nomeie a lacuna.

## Estrangeirismos preservados

- Preserve estes termos:

`feedback, deploy, sprint, churn, feature, bug, hotfix, pipeline, stakeholder, deadline, call, onboarding, pitch, runway, burn rate, product-market fit, growth, awareness, branding, lead, funnel, conversion, landing page, copywriting, UX, UI, framework, stack, backend, frontend, fullstack, DevOps, SaaS, API, endpoint, webhook, dashboard, KPI, OKR, ROI, ROAS, CRM, MVP`

- Trate estrangeirismos de tecnologia como marca de autenticidade, nunca como erro.
- Nunca force tradução desses termos. A tradução forçada é sinal de IA purista.
- Para leitor leigo, mantenha o termo de domínio e explique-o no primeiro uso.

> **Regra de ouro**: se o termo é usado no dia a dia do domínio em PT-BR, mantenha. Se é anglicismo artificial sem necessidade, remova.

## Avaliação externa com Jev (opcional)

- Use **TypeSafe Jev** somente quando o usuário solicitar avaliação externa e Jev já estiver disponível.
- Nunca assuma que Jev está disponível. Rode o protocolo de descoberta de [references/jev-integration.md](references/jev-integration.md).
- Continue fazendo a reescrita com o LLM. Jev apenas avalia.
- Mantenha a pontuação opcional. Nenhuma decisão do avaliador supera uma violação semântica detectada.
- Nunca instale serviços, escolha provedores pagos ou delegue automaticamente.
- Use o banco de perguntas [assets/jev_questions.json](assets/jev_questions.json). Nunca o modifique.

## Mapa de referências

| Arquivo | Carregue quando |
|---|---|
| [references/palavras-banidas.md](references/palavras-banidas.md) | Antes de escrever ou reescrever qualquer texto; ao rodar a Checklist de saída |
| [references/modo-ingles.md](references/modo-ingles.md) | O texto ou um segmento está em inglês; ao precisar da lista inglesa e dos exemplos em inglês |
| [references/perfis-voz.md](references/perfis-voz.md) | Nos Passos 1 e 5; ao calibrar voz; ao escrever em Assertivo, Enxuto ou Resumo |
| [references/padroes-conteudo-tom.md](references/padroes-conteudo-tom.md) | Passo 3 com Conteúdo ou Tom marcado |
| [references/padroes-linguagem-ptbr.md](references/padroes-linguagem-ptbr.md) | Passo 3 com Linguagem, PT-BR ou Estrangeirismos marcado; sempre em `modo_revisão` |
| [references/padroes-composicao.md](references/padroes-composicao.md) | Passo 3 com Composição marcado |
| [references/padroes-estilo.md](references/padroes-estilo.md) | Passo 3 com Estilo marcado; dúvida de pontuação, formatação ou ritmo |
| [references/padroes-portugues-simplificado.md](references/padroes-portugues-simplificado.md) | Perfil Português Simplificado ativo |
| [references/auditoria-entrega.md](references/auditoria-entrega.md) | Inventário com várias fontes; Passos 7 a 9; contrato de saída; suíte de regressão |
| [references/jev-integration.md](references/jev-integration.md) | O usuário pede avaliação externa com Jev |
| [assets/jev_questions.json](assets/jev_questions.json) | Durante a avaliação com Jev, como banco de perguntas |
