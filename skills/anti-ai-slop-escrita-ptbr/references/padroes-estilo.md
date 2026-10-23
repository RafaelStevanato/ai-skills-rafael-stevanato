# Padrões de estilo, pontuação e formatação

- Carregue este arquivo no Passo 3 quando a categoria Estilo estiver marcada.
- Volte a [SKILL.md](../SKILL.md) para triagem, modos, Passos 1 a 9 e proteções obrigatórias.
- Consulte [perfis-voz.md](perfis-voz.md) para as exceções por perfil de voz.
- Consulte [palavras-banidas.md](palavras-banidas.md) para o vocabulário proibido em PT-BR.
- Consulte [modo-ingles.md](modo-ingles.md) para texto escrito em inglês.
- Consulte [jev-integration.md](jev-integration.md) para a avaliação Jev.
- Use este arquivo como fonte canônica das regras de travessão, exclamação, reticências, ponto e vírgula, dois-pontos, marcadores, emoji, formatação por canal, parataxe e comprimento de frase.
- Use o id Jev indicado em cada padrão para mapear o padrão à pergunta do banco.

## Regra transversal

- Altere somente apresentação, pontuação e organização.
- Preserve fatos, números, fontes, causalidade, prazo, estado temporal, modalidade e perfil de voz.
- Nunca compense a retirada de um recurso visual com dado, opinião, humor ou certeza inexistentes.
- Cumpra a TRAVA FACTUAL definida em [SKILL.md](../SKILL.md), seção Proteções obrigatórias.
- Consulte o Passo 6 de [SKILL.md](../SKILL.md) antes de marcar qualquer padrão (guarda de falso positivo).
- Aplique estas regras só aos trechos em PT-BR de um texto multilíngue.
- Nunca aplique a texto em inglês as convenções PT-BR deste arquivo: sem vírgula de Oxford, ponto fora das aspas, capitalização só da primeira palavra do título, aspas retas.
- Siga [modo-ingles.md](modo-ingles.md) para texto em inglês.

## Pontuação

### Travessão e meia-risca

Id Jev: `estilo_travessao_excessivo`.
Peso no diagnóstico: 2.

**Regra:**
- Substitua todo travessão (—) e meia-risca (–) usado como aparte.
- Nunca use travessão em títulos nem no corpo do texto que você gera.
- Troque cada aparte por vírgula, ponto, dois-pontos ou parênteses.
- Reescreva a frase quando a troca de pontuação não resolver.
- Use parênteses para comentário lateral.
- Use vírgula para aparte leve.
- Use dois-pontos, ponto ou vírgula para contraste forte.
- Preserve a relação entre oração principal, ressalva, causa e contraste ao trocar a pontuação.

**Varredura obrigatória antes de entregar:**
- Procure `—`, `–` e ` -- ` usados como aparte no meio da frase.
- Substitua cada ocorrência por vírgula, ponto, dois-pontos ou parênteses, ou reescreva a frase.

**Medidas e limites registrados:**
- Medida de corpus: texto médio de IA tem 15-25 travessões por texto.
- Medida de corpus: humano brasileiro usa 2-3 e prefere vírgula, ponto ou parênteses.
- Limite superado (diretriz em inglês): no máximo 1 travessão por 500 palavras.
- Limite superado (diretriz em português): no máximo 2 travessões por parágrafo, com o excedente convertido em vírgulas, pontos ou parênteses.
- Limiar do banco Jev: mais de 2 por parágrafo ou mais de 5 no texto inteiro.
- Aplique a varredura obrigatória no lugar de todos os limites acima.

**Antes (IA):**
> O projeto — que começou em 2022 — trouxe resultados impressionantes — especialmente na área de dados — e agora está sendo expandido — mesmo com orçamento limitado — para outras regionais.

**Depois (humano):**
> O projeto começou em 2022 e trouxe resultados impressionantes, especialmente na área de dados. Mesmo com orçamento limitado, agora está sendo expandido para outras regionais.

**Evite em PT-BR:**
- Mais de 2 travessões por parágrafo
- Travessão onde vírgula resolve
- Encadeamento de apartes com travessão (— X — Y — Z)

**Marque como sinal:**
- Travessões usados para **tudo**: apartes, conclusões, reformulações, exemplos
- Texto onde >10% dos sinais de pontuação são travessões
- Travessão duplo usado como parênteses em toda ocorrência

**Correção:**
- Aplique o Teste do editor: se um editor humano teria cortado o travessão, corte.

**Exceções (não marque):**
- Travessão de fala em diálogo de ficção. É norma da língua portuguesa, não vício de IA.
- Amostra do autor que usa travessão: mantenha a mesma frequência da amostra. A amostra tem prioridade sobre esta regra.
- Travessão dentro de citação, título ou exemplo em discussão: o sinal é mencionado, não usado.

**Ressalva sobre exemplos verbatim:**
- Exemplos verbatim desta skill que contêm travessão de aparte mostram só o padrão.
- Nunca copie o travessão desses exemplos ao gerar texto.

### Exclamação

- Limite a exclamação a 1 por 1.000 palavras.
- Crie entusiasmo pela escolha das palavras, não pelo sinal.

### Reticências

- Use reticências só quando a frase realmente se perde, sem fechar o pensamento.
- Nunca use reticências como transição.
- Limite a 1 reticência por texto.
- Não conte "..." usado como espaço reservado em listas de gatilhos. É notação.

### Ponto e vírgula

- Use ponto e vírgula para ligar orações relacionadas.
- Use ponto e vírgula com naturalidade. A IA o subusa; quem escreve bem o usa.

### Dois-pontos

- Use dois-pontos para preparar um desfecho.
- Entregue, depois dos dois-pontos, o que a parte anterior prometeu.
- Nunca use dois-pontos para criar falso suspense.
- Veja o padrão Falso suspense em [padroes-conteudo-tom.md](padroes-conteudo-tom.md).

### Vírgula de Oxford

Id Jev: `estilo_oxford_comma`.

**Regra PT-BR:**
- Trate a vírgula antes de "e" em lista como marcador de modelo treinado em inglês.
- Não use vírgula antes de "e" no último item de lista.
- Não use vírgula antes de "ou" final.
- Mantenha a vírgula quando "e" liga orações com sujeitos diferentes (vírgula de clareza, não de lista).
- Mantenha a vírgula quando ela evita ambiguidade real.
- Nunca aplique esta regra a texto em inglês.

**Antes (IA):**
> A plataforma oferece dashboards, relatórios customizados, e integração com APIs externas. O time trabalha com React, Node.js, e PostgreSQL.

**Depois (humano):**
> A plataforma oferece dashboards, relatórios customizados e integração com APIs externas. O time trabalha com React, Node.js e PostgreSQL.

**Evite em PT-BR:**
- Vírgula antes de "e" no último item de lista: "A, B, e C" → "A, B e C"
- Vírgula antes de "ou" final: "X, Y, ou Z" → "X, Y ou Z"
- Exceção legítima: quando o "e" liga orações com sujeitos diferentes (vírgula de clareza, não de lista)

**Marque como sinal:**
- Vírgula antes de "e" em listas de 3+ itens
- Vírgula antes de "ou" em alternativas
- Mistura de textos com e sem Oxford comma no mesmo documento

**Correção:**
- Aplique o Teste do vestibular: se a frase passaria no ENEM como correta, a vírgula está certa.

### Ponto final e aspas

Id Jev: `estilo_ponto_aspas`.

**Regra PT-BR:**
- Coloque o ponto dentro das aspas quando a citação é frase completa e independente: Ele disse: "Vamos resolver isso."
- Coloque o ponto fora das aspas quando a citação é parte da frase do autor: O plano é "escalar rápido".
- Na dúvida, coloque o ponto fora. É o padrão brasileiro em texto corrido.
- Proíba a convenção americana (ponto dentro) em citação que é parte da frase.

**Antes (IA, convenção americana):**
> O CEO disse que a empresa está "no caminho certo."
>
> A meta é atingir o que chamam de "product-market fit."

**Depois (humano, convenção brasileira):**
> O CEO disse que a empresa está "no caminho certo".
>
> A meta é atingir o que chamam de "product-market fit".

**Marque como sinal:**
- Ponto dentro das aspas quando a citação é parte da frase do autor
- Inconsistência: às vezes dentro, às vezes fora, no mesmo texto
- Citações de 1 palavra com ponto dentro ("impacto.")

**Correção:**
- Padronize a convenção em todo o documento.
- Aplique o Teste da citação: se a citação termina com "que", o ponto vai fora.

### Aspas curvas vs retas

Id Jev: `estilo_aspas_curvas`.

**Regra:**
- Use aspas retas (U+0022) e apóstrofo reto (U+0027) em texto informal ou técnico.
- Aceite aspas curvas (U+201C, U+201D, U+2018, U+2019) só em diagramação profissional, como livro e revista.
- Nunca misture aspas curvas e retas no mesmo texto.
- Escolha um padrão e mantenha-o em todo o texto (regra de consistência).
- Trate aspas curvas em texto informal ou técnico como sinal de IA.
- Texto de teclado brasileiro usa aspas retas.
- Texto que parece conversa de app exige aspas retas.
- Não use aspas curvas como prova isolada: aplique o Passo 6 de [SKILL.md](../SKILL.md).

**Nota de código:** o par abaixo aparece idêntico porque o arquivo-fonte normalizou as aspas curvas. Leia o Antes com U+201C e U+201D (curvas) e o Depois com U+0022 (retas).

**Antes (IA):**
> O gestor disse que o projeto está "no caminho certo" e que a equipe está "engajada".

**Depois (humano):**
> O gestor disse que o projeto está "no caminho certo" e que a equipe está "engajada".

**Evite em PT-BR:**
- " " (curvas) em qualquer contexto que não seja diagramação profissional
- ' ' (apóstrofos curvos) no lugar de ' '
- Misturar aspas curvas e retas no mesmo texto

Leia as aspas curvas da lista como U+201C e U+201D, os apóstrofos curvos como U+2018 e U+2019 e os substitutos retos como U+0022 e U+0027.

**Marque como sinal:**
- Mistura de aspas curvas e retas no mesmo documento
- Aspas curvas em texto que claramente veio de teclado brasileiro (onde o padrão é reta)
- Aspas curvas em mensagens de WhatsApp ou Slack (impossível no mobile)

**Correção:**
- Aplique a regra de consistência: escolha um padrão e mantenha-o. Se o texto é de teclado brasileiro, use aspas retas.
- Aplique o Teste do WhatsApp: se o texto parece conversa de app, aspas retas obrigatórias.

## Formatação

### Negrito excessivo

Id Jev: `estilo_negrito_excessivo`.

**Regra contextual canônica:**
- Em prosa corrida, e-mail, artigo e texto autoral, use negrito só com contraste editorial deliberado.
- Em prosa corrida, e-mail, artigo e texto autoral, use negrito também quando a fonte já traz ênfase relevante.
- Em documentação, material didático, interfaces e listas de consulta, use negrito para rótulos e hierarquia quando isso melhora a navegação.
- Trate negrito em cada substantivo importante como catálogo de produto, não como escrita humana.
- Nunca aplique cotas simultâneas por parágrafo e por seção.
- Marque o excesso funcional: a marcação se repete sem hierarquia e vários trechos competem pela mesma atenção.
- Nos perfis Assertivo e Enxuto, preserve o negrito de abertura. Ele é hierarquia, não decoração (tabela em [perfis-voz.md](perfis-voz.md)).
- Em rede social, proíba negrito aleatório (veja Formatação por canal).
- Prevalece esta regra de prosa sobre o limiar do banco Jev (mais de 5 trechos em negrito em texto corrido).

**Antes (IA):**
> A **plataforma** oferece **integração nativa** com os principais **CRMs do mercado**, garantindo **escalabilidade** e **segurança** para equipes de **vendas** e **marketing**.

**Depois (humano):**
> A plataforma oferece integração nativa com os principais CRMs do mercado, garantindo escalabilidade e segurança para equipes de vendas e marketing.

**Marque como sinal:**
- Negrito em substantivos comuns (plataforma, equipe, resultado) sem razão editorial
- Negrito usado como substituto de hierarquia de informação (quando a estrutura deveria fazer o trabalho)
- Negrito espalhado por tantas palavras que deixa de indicar prioridade

**Correção:**
- Use negrito só para contraste intencional: "O problema não é a ferramenta — é o **processo**"
- Reestruture a frase quando o negrito tenta compensar falta de clareza.
- Preserve negritos funcionais do gênero.
- Remova os negritos decorativos sem alterar as palavras nem a ênfase semântica do trecho.
- Aplique o Teste de hierarquia: ao olhar a página, fica claro por que cada destaque existe?
- Troque o travessão do exemplo acima por dois-pontos ao gerar texto (o exemplo mantém o travessão como dado verbatim).

### Listas com rótulo em negrito

Id Jev: nenhum no banco atual.

**Regra:**
- Evite o rótulo em negrito seguido de dois-pontos em todo item sem hierarquia real.
- Aceite o formato em documentação e material de consulta.
- Marque como sinal o uso automático do formato em prosa ou em categorias artificiais.

**Antes (IA):**
> - **Agilidade:** O time reduziu o ciclo de entrega em 40%.
> - **Qualidade:** Os bugs em produção caíram pela metade.
> - **Engajamento:** A satisfação do time subiu 12 pontos no eNPS.

**Depois (humano):**
> - Agilidade: a equipe reduziu o ciclo de entrega em 40%.
> - Qualidade: os bugs em produção caíram pela metade.
> - Engajamento: a satisfação da equipe subiu 12 pontos no eNPS.

**Evite em PT-BR:**
- Estrutura "**Palavra:** frase explicativa" repetida em série sem hierarquia real
- Listas de 3+ itens onde o gênero não pede consulta rápida e a prosa preserva melhor as relações
- Forçar categorias artificiais para criar itens

**Marque como sinal:**
- Estrutura repetitiva: "**Termo:** frase explicativa" em 3+ itens consecutivos
- Itens que são minitópicos de documentação, não pontos argumentativos
- A lista poderia ser uma tabela 2xN

**Correção:**
- Converta em tabela quando a informação é factual e tabular, preservando rótulos, valores e correspondências.
- Converta em prosa corrida quando a informação é argumentativa, sem criar relação causal nem conclusão nova.
- Use marcadores simples, sem cabeçalho em negrito, quando a lista é inevitável.
- Mantenha cabeçalhos em negrito quando são rótulos funcionais do gênero (regra contextual canônica em Negrito excessivo).
- Aplique o Teste do slide: se a lista parece um slide de apresentação, formate como slide (ou reescreva como parágrafo).

### Listas de marcadores

- Use marcadores com moderação.
- Limite a 5 itens seguidos em perfil autoral e em voz neutra.
- Varie o tamanho dos itens: alguns longos, outros curtos.
- Use uma frase quando o conteúdo cabe em uma frase.
- Isente o perfil Português Simplificado (R10: lista para 3+ itens).
- Isente o perfil Resumo (listas com mais de 5 itens quando o status exige).
- Registro: a diretriz em inglês aceita 5-7 itens seguidos; vale o limite mais estrito, 5.

### Title Case em títulos

Id Jev: `estilo_title_case`.

**Regra PT-BR:**
- Aplique a regra ABNT: maiúscula só na primeira letra do título e em nomes próprios.
- Trate Title Case em PT-BR como sinal de modelo treinado em inglês.
- Aceite Title Case só quando o documento é explicitamente para público americano.
- Nunca aplique esta regra a título em inglês.

**Antes (IA):**
> ## Estratégias De Marketing Digital Para Pequenas Empresas

**Depois (humano):**
> ## Estratégias de marketing digital para pequenas empresas

**Evite em PT-BR:**
- Capitalizar preposições (De, Para, Com, Em)
- Capitalizar substantivos comuns em títulos (Empresas, Estratégias, Resultados)
- Qualquer padrão que lembre capa de livro americano

**Marque como sinal:**
- Títulos onde preposições e artigos estão capitalizados
- Títulos que parecem capa de livro americano ("Estratégias De Marketing Para Pequenas Empresas")
- Mistura de Title Case com sentenças em minúsculo no mesmo documento

**Correção:**
- Aplique o Teste do jornal brasileiro: abra matéria da Folha ou Piauí; os títulos usam minúsculas em preposições.

### Emojis decorativos

Id Jev: `estilo_emoji_decorativo`.

**Regra:**
- Use emoji em mensagem informal.
- Proíba emoji em título de seção e em tópico técnico.
- Proíba emoji decorativo em título, item e marcador de texto profissional.
- Nunca use emoji como marcador de item.
- Limite posts de rede social a 1-2 emojis.
- Trate como slop a lista em que toda linha começa com ✅ ou 🔥.
- Proíba 🚀💡🎯✨ como decoração em qualquer perfil.
- Trate 🚀💡✅🎯 em texto profissional como assinatura de máquina.
- Preserve o emoji que comunica estado, alerta ou categoria funcional.
- Isente o perfil Resumo: ✅🟡⬜❔🔴 são notação funcional de estado (tabela em [perfis-voz.md](perfis-voz.md)).

**Antes (IA):**
> 🚀 **Lançamento:** Produto entra no ar em setembro
> 💡 **Observação:** Usuários preferem onboarding curto
> ✅ **Próximos passos:** Agendar reunião com stakeholders
> 🎯 **Meta:** Crescer 30% no trimestre

**Depois (humano):**
> Lançamento: o produto entra no ar em setembro.
> Observação: os usuários preferem um onboarding curto.
> Próximos passos: agendar uma reunião com os stakeholders.
> Meta: crescer 30% no trimestre.

**Evite em PT-BR:**
- Emoji antes de título ou item quando for puramente decorativo
- 🚀💡✅🎯📊 como decoração de estrutura
- Emoji incompatível com o perfil de voz ou sem função comunicativa

**Marque como sinal:**
- Emojis em headings de seção, títulos de artigo, ou como marcadores em texto profissional
- Sequência de emojis sem função comunicativa (decoração pura)
- Emoji em texto que não é mensagem pessoal ou post de rede social

**Correção:**
- Em texto formal ou técnico, remova o emoji puramente decorativo.
- Em texto formal ou técnico, preserve o ícone que comunica estado, alerta ou categoria funcional.
- Em WhatsApp e rede social, mantenha os emojis compatíveis com o perfil de voz.
- Em WhatsApp e rede social, retire só a repetição mecânica.
- Ao remover o emoji, não acrescente humor, ironia, surpresa nem nova ênfase.
- Aplique o Teste do canal: o emoji cumpre uma função aceita nesse gênero ou serve apenas de enfeite?

### Decoração Unicode

Id Jev: `estilo_unicode_decorativo`.

**Regra:**
- Use só caracteres que o teclado brasileiro produz: -, *, > e ponto final.
- Proíba setas (→, ←, ↗), marcadores especiais (•, ▸, ▪), marcas de verificação (✓, ✗) e separadores (│, ─) como decoração.
- Preserve a seta → no perfil Assertivo quando ela indica resultado, consequência ou próximo passo (veja [perfis-voz.md](perfis-voz.md)).

**Antes (IA):**
> Benefícios do novo processo:
> → Redução de 40% no tempo de resposta
> → Aumento na satisfação do cliente
> → Integração com sistemas legados
>
> Stack: React │ Node.js │ PostgreSQL

**Depois (humano):**
> Benefícios do novo processo:
> - Redução de 40% no tempo de resposta
> - Aumento na satisfação do cliente
> - Integração com sistemas legados
>
> Stack: React, Node.js, PostgreSQL

**Evite em PT-BR:**
- → como marcador de item (usar - ou *)
- │ como separador (usar vírgula, barra ou ponto)
- ✓ e ✗ no corpo do texto quando não houver função; se houver, usar o estado textual equivalente sem inferi-lo

**Marque como sinal:**
- Setas (→, ↗), marcadores especiais (▸, ▪), marcas de verificação (✓, ✗) e separadores (│, ─) que não são renderizados pelo teclado padrão brasileiro
- Uso de emojis como marcadores em texto formal
- Texto que parece ter sido copiado de um Notion com modelos de produtividade

**Correção:**
- Troque setas por hífens ou asteriscos: "→" → "-"
- Remova separadores Unicode: "React │ Node.js │ PostgreSQL" → "React, Node.js, PostgreSQL"
- Converta marcas de verificação em texto somente quando houver equivalente explícito.
- Preserve o estado original ao converter: aprovado, reprovado, sim, não ou pendente.
- Aplique o Teste do terminal: se o texto renderiza com caracteres quebrados num terminal sem Unicode, é decoração artificial.

### Formatação por canal

- Proíba cabeçalhos markdown em rede social, e-mail e texto casual.
- Proíba negrito aleatório para ênfase em rede social. Deixe as palavras fazerem o trabalho.
- Proíba markdown em contexto de texto simples: e-mail, DM e SMS.
- Trate asteriscos renderizados como símbolos como sinal imediato de IA.
- Proíba abertura com "🧵", "Fio:" ou "Thread:". Faça o conteúdo prender o leitor por si.
- Limite hashtags a 0-2, integradas ao texto.
- Proíba pilhas de hashtags.
- Permita negrito de abertura nos perfis de leitura rápida (Assertivo, Enxuto, Resumo), inclusive no TL;DR do Resumo em Slack e e-mail.
- Mantenha proibidos os cabeçalhos markdown nesses perfis em rede social, e-mail e texto casual.
- Aplique a regra de emoji de Emojis decorativos (1-2 por post; nunca como marcador).

## Ritmo

### Comprimento de frase

- Nunca escreva 3 frases consecutivas do mesmo comprimento.
- Misture frases de 4 palavras com frases de 30 palavras.
- Trate o comprimento uniforme como o sinal de IA mais mensurável.
- Em parágrafo com menos de 3 frases, não exija 3 tamanhos distintos.
- No perfil Português Simplificado, mantenha o teto de 25 palavras por frase (alvo 13-18). O teto prevalece sobre a mistura de 4 e 30 palavras.

### Parataxe

- Defina parataxe: 3 ou mais frases declarativas curtas em sequência, sem conectivos.
- Trate a parataxe como sinal imediato de autoria de IA.
- Proíba parataxe em voz neutra e em prosa autoral.
- Permita fragmentos em prosa autoral só quando a amostra de voz os usa.
- Conecte pensamentos relacionados com oração subordinada, conjunção, ponto e vírgula ou vírgula.
- Escreva uma sintaxe que mostre a relação entre as ideias: causa, contraste, qualificação.
- Mostre essas relações só quando a fonte já as expressa. Nunca crie causa, contraste ou conclusão nova.
- Isente os perfis Português Simplificado, Enxuto, Assertivo e Resumo: dividir em frases curtas é a regra deles.
- Preserve os fragmentos de Crônica e de Post de Rede Social que fazem parte da voz.
- Verifique no fim: 3 ou mais frases declarativas curtas seguidas? Una ou conecte por conjunção, oração ou pontuação.

**Exemplo (tradução do original em inglês; o original está em [modo-ingles.md](modo-ingles.md)):**
> "Frase curta. Depois outra. Depois outra." vira "A IA encadeia frases curtas porque é mais fácil do que construir um pensamento com conectivos de verdade."

### Fragmentos curtos dramáticos

Id Jev: `estilo_fragmentos_dramaticos`.

**Regra:**
- Integre o fragmento ao período correspondente em prosa neutra.
- Preserve o fragmento em Crônica e em Rede Social quando ele faz parte da voz.
- Preserve as frases curtas do perfil Enxuto: uma linha é o formato, não fragmento dramático.
- Aceite o recurso no Twitter. Evite em artigo e e-mail.
- Permita frase "feia" (fragmento, ou período longo que segue porque o pensamento não acabou) só em perfil autoral cuja voz a sustenta.
- Mantenha o limite: mais de 1 fragmento por texto, fora do Twitter, é sinal.

**Antes (IA):**
> O mercado mudou.
>
> Radicalmente.
>
> E quem não se adaptar vai ficar para trás. A pergunta não é se, mas quando. O futuro já chegou.
>
> Literalmente.

**Depois (humano):**
> O mercado mudou radicalmente. Quem não se adaptar vai ficar para trás. A pergunta não é se, mas quando: o futuro já chegou, literalmente.

**Evite em PT-BR:**
- Palavra isolada como parágrafo sem função no perfil de voz ("Radicalmente.", "Literalmente.", "Ponto.")
- Sequência de fragmentos dramáticos sem função no perfil de voz
- Fragmento + ponto final para criar "peso" artificial

**Marque como sinal:**
- Palavra ou frase de 1-3 palavras isolada como parágrafo inteiro
- Uso repetido (mais de 1 por texto) em contexto que não é Twitter
- Fragmento que não acrescenta informação — só "peso" artificial

**Correção:**
- Integre o fragmento sem perder o intensificador: "Mudou. Radicalmente." → "Mudou radicalmente."
- Ajuste só a pontuação quando o fragmento é pura ênfase.
- Nunca acrescente urgência, conclusão ou avaliação ao integrar.
- Aplique o Teste do gênero: o fragmento combina com o perfil de voz ou apenas simula impacto?

## Ressalva com preâmbulo (minimiza e infla)

Id Jev: `estilo_ressalva_preambulo`.

**Regra:**
- Marque o padrão de IA de 2025/2026: uma minimização genérica seguida de inflação automática.
- Preserve o contraste legítimo.
- Marque o padrão só quando a moldura se repete mecanicamente.
- Marque o padrão também quando os dois lados não têm apoio no texto-fonte.
- Preserve os dois lados quando o autor afirma um contraste.
- Remova apenas a moldura repetitiva.
- Nunca escolha uma posição nova ao remover a moldura.
- Mostre a tensão com dados somente quando esses dados já estão na fonte.
- Mantenha a formulação qualitativa quando a fonte não traz os dados.

**Antes (IA):**
> Embora pareça um conceito simples, a consistência na publicação de conteúdo representa um dos pilares mais fundamentais e transformadores de qualquer estratégia de marketing digital moderna.
>
> À primeira vista, essa pode parecer uma mudança incremental, mas na verdade constitui uma transformação paradigmática na forma como organizações interagem com seus stakeholders.

**Depois (humano):**
> A consistência na publicação de conteúdo é um dos pilares mais fundamentais e transformadores de qualquer estratégia moderna de marketing digital. Mesmo assim, pode parecer um conceito simples.
>
> A mudança constitui uma transformação paradigmática na forma como as organizações interagem com seus stakeholders, embora à primeira vista possa parecer incremental.

**Evite em PT-BR:**
- "Embora pareça simples, na verdade é [superlativo]"
- "À primeira vista... mas na verdade constitui..."
- "Pode parecer óbvio, porém [inflação]"
- "Apesar de ser um conceito básico, representa um dos mais [superlativo]"
- Qualquer estrutura que minimiza no preâmbulo e infla na oração principal

**Marque como sinal:**
- Estrutura "minimiza → infla" em uma única frase: "Embora pareça simples, é transformador"
- Uso de "na verdade" como ponte entre minimização e inflação
- O preâmbulo é sempre genérico ("parece simples", "à primeira vista") e a inflação é sempre superlativa

**Correção:**
- Aplique o Teste do podcast host: se o apresentador diria isso sem soar como vendedor, a frase é honesta.
