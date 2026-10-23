# Padrões de estilo, pontuação e formatação

- Use este arquivo no Passo 3 de [SKILL.md](../SKILL.md) quando Estilo estiver marcado.
- Trate este arquivo como fonte canônica das regras de pontuação, formatação, emoji, parataxe e comprimento de frase.
- Use o id Jev de cada padrão com [jev-integration.md](jev-integration.md).
- Para as exceções por perfil de voz, consulte [perfis-voz.md](perfis-voz.md).

## Regra transversal

- Altere somente apresentação, pontuação e organização.
- Nunca compense a retirada de um recurso visual com dado, opinião, humor ou certeza inexistentes.
- Cumpra a TRAVA FACTUAL de [SKILL.md](../SKILL.md) (seção Proteções obrigatórias).
- Consulte o Passo 6 de [SKILL.md](../SKILL.md) antes de marcar qualquer padrão (guarda de falso positivo).
- Aplique estas regras só aos trechos em PT-BR de um texto multilíngue.
- Em texto em inglês, siga [modo-ingles.md](modo-ingles.md). Nunca aplique a ele as convenções PT-BR deste arquivo: sem vírgula de Oxford, ponto fora das aspas, capitalização só da primeira palavra do título, aspas retas.

## Pontuação

### Travessão e meia-risca

Id Jev: `estilo_travessao_excessivo`. Peso no diagnóstico: 2.

**Regra:**
- Varra o texto antes de entregar: procure `—`, `–` e ` -- ` usados como aparte no meio da frase.
- Substitua cada ocorrência por vírgula, ponto, dois-pontos ou parênteses, ou reescreva a frase.
- Nunca use travessão em título nem no corpo do texto que você gera.
- Use parênteses para comentário lateral, vírgula para aparte leve e dois-pontos, ponto ou vírgula para contraste forte.
- Ao trocar a pontuação, preserve a relação entre oração principal, ressalva, causa e contraste.

**Medidas e limites registrados (a varredura prevalece sobre todos os limites):**
- Texto médio de IA tem 15-25 travessões. Humano brasileiro usa 2-3 e prefere vírgula, ponto ou parênteses.
- Limite superado (diretriz em inglês): no máximo 1 travessão por 500 palavras.
- Limite superado (diretriz em português): no máximo 2 travessões por parágrafo, com o excedente convertido em vírgulas, pontos ou parênteses.
- Limiar do banco Jev: mais de 2 por parágrafo ou mais de 5 no texto inteiro.

**Antes (IA):**
> O projeto — que começou em 2022 — trouxe resultados impressionantes — especialmente na área de dados — e agora está sendo expandido — mesmo com orçamento limitado — para outras regionais.

**Depois (humano):**
> O projeto começou em 2022 e trouxe resultados impressionantes, especialmente na área de dados. Mesmo com orçamento limitado, agora está sendo expandido para outras regionais.

**Evite em PT-BR:**
- Mais de 2 travessões por parágrafo
- Travessão onde vírgula resolve
- Encadeamento de apartes com travessão (— X — Y — Z)

**Sinais:**
- Travessões usados para **tudo**: apartes, conclusões, reformulações, exemplos
- Texto onde >10% dos sinais de pontuação são travessões
- Travessão duplo usado como parênteses em toda ocorrência

**Correção:**
- Aplique o Teste do editor: se um editor humano teria cortado o travessão, corte.

**Exceções (não marque):**
- Travessão de fala em diálogo de ficção. É norma da língua portuguesa, não vício de IA.
- Amostra do autor que usa travessão: mantenha a mesma frequência da amostra. A amostra tem prioridade sobre esta regra.
- Travessão dentro de citação, título ou exemplo em discussão: o sinal é mencionado, não usado.

**Ressalva sobre exemplos verbatim:** os exemplos desta skill com travessão de aparte mostram só o padrão. Nunca copie o travessão desses exemplos ao gerar texto.

### Exclamação

- Limite a exclamação a 1 por 1.000 palavras.
- Crie entusiasmo pela escolha das palavras, não pelo sinal.

### Reticências

- Use reticências só quando a frase realmente se perde, sem fechar o pensamento.
- Nunca use reticências como transição.
- Limite a 1 reticência por texto.
- Não conte "..." usado como espaço reservado em listas de gatilhos. É notação.

### Ponto e vírgula

- Use ponto e vírgula para ligar orações relacionadas, com naturalidade. A IA o subusa; quem escreve bem o usa.

### Dois-pontos

- Use dois-pontos para preparar um desfecho. Entregue depois deles o que a parte anterior prometeu.
- Nunca use dois-pontos para criar falso suspense (veja o padrão Falso suspense em [padroes-conteudo-tom.md](padroes-conteudo-tom.md)).

### Vírgula de Oxford

Id Jev: `estilo_oxford_comma`.

**Regra PT-BR:**
- Trate a vírgula antes de "e" em lista como marcador de modelo treinado em inglês (ex: "maçãs, bananas, e laranjas").
- Mantenha a vírgula que evita ambiguidade real, como quando "e" liga orações com sujeitos diferentes (vírgula de clareza, não de lista).
- Nunca aplique esta regra a texto em inglês.

**Antes (IA):**
> A plataforma oferece dashboards, relatórios customizados, e integração com APIs externas. O time trabalha com React, Node.js, e PostgreSQL.

**Depois (humano):**
> A plataforma oferece dashboards, relatórios customizados e integração com APIs externas. O time trabalha com React, Node.js e PostgreSQL.

**Evite em PT-BR:**
- Vírgula antes de "e" no último item de lista: "A, B, e C" → "A, B e C"
- Vírgula antes de "ou" final: "X, Y, ou Z" → "X, Y ou Z"
- Exceção legítima: quando o "e" liga orações com sujeitos diferentes (vírgula de clareza, não de lista)

**Sinais:**
- Vírgula antes de "e" em listas de 3+ itens ou antes de "ou" em alternativas
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

**Sinais:**
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
- Trate aspas curvas em texto informal ou técnico como sinal de IA.

**Antes (IA):**
> O gestor disse que o projeto está "no caminho certo" e que a equipe está "engajada".

**Depois (humano):**
> O gestor disse que o projeto está "no caminho certo" e que a equipe está "engajada".

**Evite em PT-BR:**
- " " (curvas) em qualquer contexto que não seja diagramação profissional
- ' ' (apóstrofos curvos) no lugar de ' '
- Misturar aspas curvas e retas no mesmo texto

**Nota de código:** o arquivo-fonte normalizou as aspas, então o par e a lista acima parecem idênticos. No par, leia o Antes com U+201C e U+201D (curvas) e o Depois com U+0022 (retas). Na lista, leia as aspas curvas como U+201C e U+201D, os apóstrofos curvos como U+2018 e U+2019 e os substitutos retos como U+0022 e U+0027.

**Sinais:**
- Aspas curvas em texto que claramente veio de teclado brasileiro (onde o padrão é reta)
- Aspas curvas em mensagens de WhatsApp ou Slack (impossível no mobile)

**Correção:**
- Aplique a regra de consistência: escolha um padrão e mantenha-o. Se o texto é de teclado brasileiro, use aspas retas.
- Aplique o Teste do WhatsApp: se o texto parece conversa de app, aspas retas obrigatórias.

## Formatação

### Negrito excessivo

Id Jev: `estilo_negrito_excessivo`.

**Regra contextual canônica:**
- Em prosa corrida, e-mail, artigo e texto autoral, use negrito só com contraste editorial deliberado ou quando a fonte já traz ênfase relevante.
- Em documentação, material didático, interfaces e listas de consulta, use negrito para rótulos e hierarquia quando isso melhora a navegação.
- Nunca aplique cotas simultâneas por parágrafo e por seção.
- Marque o excesso funcional: a marcação se repete sem hierarquia e vários trechos competem pela mesma atenção.
- Nos perfis Assertivo e Enxuto, preserve o negrito de abertura. Ele é hierarquia, não decoração (tabela em [perfis-voz.md](perfis-voz.md)).
- Prevalece esta regra de prosa sobre o limiar do banco Jev (mais de 5 trechos em negrito em texto corrido).

**Antes (IA):**
> A **plataforma** oferece **integração nativa** com os principais **CRMs do mercado**, garantindo **escalabilidade** e **segurança** para equipes de **vendas** e **marketing**.

**Depois (humano):**
> A plataforma oferece integração nativa com os principais CRMs do mercado, garantindo escalabilidade e segurança para equipes de vendas e marketing.

**Sinais:**
- Negrito em substantivos comuns (plataforma, equipe, resultado) sem razão editorial
- Negrito usado como substituto de hierarquia de informação (quando a estrutura deveria fazer o trabalho)

**Correção:**
- Use negrito só para contraste intencional: "O problema não é a ferramenta — é o **processo**"
- Troque o travessão do exemplo acima por dois-pontos ao gerar texto (o exemplo mantém o travessão como dado verbatim).
- Reestruture a frase quando o negrito tenta compensar falta de clareza.
- Preserve negritos funcionais do gênero. Remova os decorativos sem alterar as palavras nem a ênfase semântica do trecho.
- Aplique o Teste de hierarquia: ao olhar a página, fica claro por que cada destaque existe?

### Listas com rótulo em negrito

Id Jev: nenhum no banco atual.

**Regra:**
- Evite o rótulo em negrito seguido de dois-pontos em todo item sem hierarquia real. Marque o uso automático do formato em prosa ou em categorias artificiais.
- Aceite o formato em documentação e material de consulta.

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

**Sinais:**
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

**Sinais:**
- Títulos onde preposições e artigos estão capitalizados, como capa de livro americano ("Estratégias De Marketing Para Pequenas Empresas")
- Mistura de Title Case com sentenças em minúsculo no mesmo documento

**Correção:**
- Aplique o Teste do jornal brasileiro: abra matéria da Folha ou Piauí; os títulos usam minúsculas em preposições.

### Emojis decorativos

Id Jev: `estilo_emoji_decorativo`.

**Regra:**
- Use emoji em mensagem informal.
- Proíba emoji em título de seção, em tópico técnico e como marcador de item.
- Limite posts de rede social a 1-2 emojis.
- Trate como slop a lista em que toda linha começa com ✅ ou 🔥.
- Proíba 🚀💡🎯✨ como decoração em qualquer perfil.
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

**Sinais:**
- Emojis em headings de seção, títulos de artigo, ou como marcadores em texto profissional
- Emoji em texto que não é mensagem pessoal ou post de rede social

**Correção:**
- Em texto formal ou técnico, remova o emoji puramente decorativo e preserve o ícone que comunica estado, alerta ou categoria funcional.
- Em WhatsApp e rede social, mantenha os emojis compatíveis com o perfil de voz e retire só a repetição mecânica.
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

**Sinais:**
- Uso de emojis como marcadores em texto formal
- Texto que parece ter sido copiado de um Notion com modelos de produtividade

**Correção:**
- Troque setas por hífens ou asteriscos: "→" → "-"
- Remova separadores Unicode: "React │ Node.js │ PostgreSQL" → "React, Node.js, PostgreSQL"
- Converta marcas de verificação em texto somente quando houver equivalente explícito, preservando o estado original: aprovado, reprovado, sim, não ou pendente.
- Aplique o Teste do terminal: se o texto renderiza com caracteres quebrados num terminal sem Unicode, é decoração artificial.

### Formatação por canal

- Proíba cabeçalhos markdown em rede social, e-mail e texto casual.
- Proíba markdown em contexto de texto simples (e-mail, DM, SMS). Asteriscos renderizados como símbolos são sinal imediato de IA.
- Proíba negrito aleatório para ênfase em rede social. Deixe as palavras fazerem o trabalho.
- Proíba abertura com "🧵", "Fio:" ou "Thread:". Faça o conteúdo prender o leitor por si.
- Limite hashtags a 0-2, integradas ao texto. Proíba pilhas de hashtags.
- Nos perfis de leitura rápida (Assertivo, Enxuto, Resumo), permita negrito de abertura, inclusive no TL;DR do Resumo em Slack e e-mail. Mantenha proibidos os cabeçalhos markdown nesses perfis.

## Ritmo

### Comprimento de frase

- Nunca escreva 3 frases consecutivas do mesmo comprimento. Esse é o sinal de IA mais mensurável.
- Misture frases de 4 palavras com frases de 30 palavras.
- Em parágrafo com menos de 3 frases, não exija 3 tamanhos distintos.
- No perfil Português Simplificado, mantenha o teto de 25 palavras por frase (alvo 13-18). O teto prevalece sobre a mistura de 4 e 30 palavras.

### Parataxe

- Defina parataxe: 3 ou mais frases declarativas curtas em sequência, sem conectivos. Trate-a como sinal imediato de autoria de IA.
- Proíba parataxe em voz neutra e em prosa autoral.
- Permita fragmentos em prosa autoral só quando a amostra de voz os usa.
- Conecte pensamentos relacionados com oração subordinada, conjunção, ponto e vírgula ou vírgula, para mostrar causa, contraste ou qualificação.
- Mostre essas relações só quando a fonte já as expressa. Nunca crie causa, contraste ou conclusão nova.
- Isente os perfis Português Simplificado, Enxuto, Assertivo e Resumo: dividir em frases curtas é a regra deles.
- Preserve os fragmentos de Crônica e de Post de Rede Social que fazem parte da voz.

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

**Sinais:**
- Palavra ou frase de 1-3 palavras isolada como parágrafo inteiro

**Correção:**
- Integre o fragmento sem perder o intensificador: "Mudou. Radicalmente." → "Mudou radicalmente."
- Quando o fragmento é pura ênfase, ajuste só a pontuação. Nunca acrescente urgência, conclusão ou avaliação ao integrar.
- Aplique o Teste do gênero: o fragmento combina com o perfil de voz ou apenas simula impacto?

## Ressalva com preâmbulo (minimiza e infla)

Id Jev: `estilo_ressalva_preambulo`.

**Regra:**
- Marque o padrão de IA de 2025/2026: uma minimização genérica seguida de inflação automática.
- Marque o padrão só quando a moldura se repete mecanicamente ou quando os dois lados não têm apoio no texto-fonte. Preserve o contraste legítimo.
- Preserve os dois lados quando o autor afirma um contraste. Remova apenas a moldura repetitiva, sem escolher uma posição nova.
- Mostre a tensão com dados somente quando esses dados já estão na fonte. Senão, mantenha a formulação qualitativa.

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

**Sinais:**
- Estrutura "minimiza → infla" em uma única frase: "Embora pareça simples, é transformador"
- Uso de "na verdade" como ponte entre minimização e inflação
- O preâmbulo é sempre genérico ("parece simples", "à primeira vista") e a inflação é sempre superlativa

**Correção:**
- Aplique o Teste do podcast host: se o apresentador diria isso sem soar como vendedor, a frase é honesta.
