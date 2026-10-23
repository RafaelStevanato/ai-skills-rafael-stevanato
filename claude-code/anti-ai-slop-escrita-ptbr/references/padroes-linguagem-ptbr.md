# Padrões de linguagem e exclusivos do PT-BR

- Carregue este arquivo no Passo 3 quando Linguagem, PT-BR ou Estrangeirismos estiver marcado, e sempre no `modo_revisão`.
- Volte a [SKILL.md](../SKILL.md) para triagem, modos, Passos 1 a 9 e proteções obrigatórias.
- Consulte [perfis-voz.md](perfis-voz.md) para exceções por perfil, [palavras-banidas.md](palavras-banidas.md) para o vocabulário proibido e [jev-integration.md](jev-integration.md) para a avaliação Jev.
- Os padrões da Parte A correspondem a tropos catalogados em tropes.fyi.

## Regras de uso

- Cumpra a TRAVA FACTUAL definida em [SKILL.md](../SKILL.md), seção Proteções obrigatórias.
- Use os pares "Antes/Depois" como modelo de forma. Eles não autorizam completar lacunas.
- Descarte a alternativa que exija informação ausente ou mude o grau de certeza.
- Não remova informação só para quebrar um padrão.
- Ajuste a correção ao perfil de voz. Os exemplos "Depois" usam registro neutro.
- Nos perfis Acadêmico, Jornalístico e Jurídico, preserve terminologia, atribuições e formalidade funcional.
- Nos perfis informais, use oralidade somente quando o usuário pedir ou o original já a tiver.
- A naturalidade vem da adequação ao registro, não da informalidade obrigatória.
- Consulte o Passo 6 de [SKILL.md](../SKILL.md) antes de marcar qualquer padrão (guarda de falso positivo).
- Mantenha inteiras as listas de gatilhos, Evite e Alternativas de cada padrão, mesmo quando os itens se repetem entre padrões.
- Use o id Jev de cada padrão para mapeá-lo à pergunta do banco.
- Os exemplos com travessão de aparte mostram só o padrão. Nunca copie esse travessão ao gerar texto.

## Parte A: linguagem e gramática

### A1. Vocabulário de IA em PT-BR

Id Jev: `linguagem_vocabulario_ia`.

Os gatilhos equivalem a termos recorrentes em inglês, como "delve", "crucial" e "landscape". Muitos são tradução direta e soam artificiais em português. Ninguém fala "rica tapeçaria" ou "desbloquear potencial" no Brasil.

**Gatilhos:** crucial, fundamental, cenário, landscape/panorama, no âmbito de, no bojo de, nesse diapasão, destarte, outrossim, mister se faz, em última análise, inegável, indubitavelmente, exponencialmente, de forma exponencial, disruptivo, paradigma, holístico, sinergia, alavancar, robusto, escalável, ecossistema (abstrato), jornada (figurativo), mergulhar em (delve into), desbloquear (unlock), desvendar insights (uncover insights), rica tapeçaria (rich tapestry), um testemunho de (a testament to), serve como um lembrete (serves as a reminder), na paisagem/cenário em constante evolução (ever-evolving landscape), navegar [complexidades] (navigate), ponta de lança (spearhead), sem costura/sem fricção (seamless), multifacetado, catalisador, orquestrar, delinear

**Antes (IA):**
> É fundamental destacar que o ecossistema de startups brasileiro passa por um momento crucial de maturação. No âmbito da inovação, diversas empresas estão alavancando soluções disruptivas que prometem transformar o panorama do mercado de forma exponencial.

**Depois (humano):**
> O mercado brasileiro de startups está amadurecendo. Nesse processo, várias empresas usam soluções que prometem transformar o mercado de forma exponencial.

**Evite em PT-BR:**
- "É fundamental/crucial/inegável destacar que..."
- "No âmbito/bojo/cenário de..."
- "Alavancar soluções robustas e escaláveis"
- "Mergulhar em/Mergulhar fundo em" → "explorar" / "ver de perto" / "entrar em"
- "Desbloquear o potencial" → "aproveitar" / "usar melhor"
- "Desvendar insights" → "descobrir" / "achar" / "perceber"
- "Rica tapeçaria de experiências" → cortar (sempre é enchimento)
- "É um testemunho de/da" → declarar diretamente o fato já apresentado, sem trocar indício por prova
- "Serve como um lembrete de que" → "lembra que" / cortar
- "No cenário/paisagem em constante evolução" → cortar o cenário, ir direto ao ponto
- "Navegar as complexidades de" → "lidar com"; use "resolver" somente se o original afirmar que houve solução
- "Sem costura" / "sem fricção" → "fluido" / "que funciona bem" / "redondo"
- "Catalisador de mudanças" → descrever a função causal somente se ela já estiver afirmada no original
- "Orquestrar a transformação" → "coordenar a transformação", quando essa ação constar do original

### A2. Evitação de verbos de ligação

Id Jev: `linguagem_evitacao_copula`.

- Aplique o padrão B7. B7 reúne as duas listas de gatilhos, os dois pares "Antes/Depois" e a nota sobre o "ter" existencial.

### A3. Paralelismos negativos

Id Jev: `linguagem_paralelismo_negativo`.

A construção finge rejeitar algo para afirmar algo maior, mas as duas partes dizem a mesma coisa.

**Gatilhos:** não é apenas X, mas também Y; não se trata apenas de X, trata-se de Y; mais do que X, é Y; vai muito além de X; transcende o simples X; não é meramente X, é sobretudo Y

**Antes (IA):**
> Produto não é apenas sobre funcionalidades. Não se trata meramente de entregar código — trata-se de resolver problemas reais. O PM vai muito além de escrever histórias de usuário; ele é, sobretudo, um tradutor entre negócio e tecnologia.

**Depois (humano):**
> Produto envolve funcionalidades, entrega de código e resolução de problemas reais. O trabalho de PM inclui escrever histórias de usuário e traduzir necessidades entre negócio e tecnologia.

**Evite em PT-BR:**
- "Não se trata apenas de X, trata-se de Y"
- "Vai muito além de simplesmente..."
- "Mais do que X, é sobretudo Y"

### A4. Regra de três

Id Jev: `linguagem_regra_tres`.

Repetido em todo parágrafo, o trio vira cacoete.

**Gatilhos:** clareza, concisão e coerência; inovação, tecnologia e transformação; planejar, executar e medir; qualquer tríade rítmica com "e" antes do terceiro item; três adjetivos em sequência; três substantivos abstratos agrupados

**Antes (IA):**
> Nossa cultura é baseada em transparência, colaboração e inovação. Buscamos agilidade, qualidade e impacto. Valorizamos autonomia, responsabilidade e aprendizado contínuo.

**Depois (humano):**
> Transparência e colaboração orientam nossa cultura. A inovação também conta. Buscamos agilidade sem abrir mão da qualidade nem do impacto; valorizamos autonomia, responsabilidade e aprendizado contínuo.

**Regra por modo:**
- Em `modo_criacao`, use 1, 2, 4 ou 5 itens. Use 3 itens só quando o conteúdo tem exatamente 3.
- Em reescrita, varie a estrutura e quebre a simetria de 3 ou mais itens sem acrescentar nem retirar nenhum item.
- Mantenha a tríade quando ela for funcional ao perfil, por exemplo em texto normativo ou apresentação.

**Evite em PT-BR:**
- "Transparência, colaboração e inovação"
- "Planejamento, execução e controle"
- Três adjetivos ou substantivos abstratos em sequência, parágrafo após parágrafo

### A5. Variação lexical forçada

Id Jev: `linguagem_variacao_forcada`.

A variação forçada deixa o leitor sem saber se o referente mudou.

**Gatilhos:** ciclagem de sinônimos para o mesmo referente, por exemplo "a ferramenta" → "a solução" → "a plataforma" → "o sistema" → "o produto"; ou para pessoas: "o profissional" → "o colaborador" → "o especialista" → "o gestor"

**Antes (IA):**
> O Slack revolucionou a comunicação corporativa. A ferramenta de mensagens oferece canais temáticos. A plataforma colaborativa integra com mais de 2.000 aplicativos. A solução de produtividade é usada por 750 mil empresas.

**Depois (humano):**
> O Slack revolucionou a comunicação corporativa e é usado por 750 mil empresas. Ele oferece canais temáticos e integração com mais de 2.000 aplicativos.

**Evite em PT-BR:**
- Ciclagem "ferramenta → solução → plataforma → sistema"
- "O profissional → o colaborador → o especialista"
- Trocar referente a cada frase quando poderia repetir ou usar pronome

### A6. Falsas faixas

Id Jev: `linguagem_falsas_faixas`.

A faixa soa ampla, mas os extremos são exemplos aleatórios unidos por "de...a...", não opostos de uma escala real.

**Gatilhos:** de X a Y; desde X até Y; abrangendo desde X até Y; vai de X a Y, passando por Z; cobre desde X até Y

**Antes (IA):**
> O evento abordou desde inteligência artificial até gestão de pessoas, passando por marketing digital e produto. Os participantes variaram de estagiários a executivos, de startups em estágio inicial a corporações multinacionais.

**Depois (humano):**
> O evento reuniu inteligência artificial, gestão de pessoas, marketing digital e produto. Participaram estagiários, executivos, pessoas de startups em estágio inicial e de corporações multinacionais.

**Correção segura:**
- Desdobre somente os extremos e exemplos já citados.
- Não complete a faixa com público, quantidade, preferência ou resultado presumido.

**Evite em PT-BR:**
- "Desde inteligência artificial até gestão de pessoas"
- "De estagiários a C-levels"
- "Abrangendo desde X até Y, passando por Z"

### A7. Anáfora abusiva

Id Jev: `linguagem_anafora_abusiva`.

A anáfora é recurso legítimo em discurso, manifesto e poesia. Em texto expositivo, sem propósito estilístico, vira eco robótico.

**Gatilhos:** repetição do mesmo início em 3+ frases consecutivas: "É preciso...", "Precisamos...", "O futuro...", "A tecnologia...", "Esse é o momento de...", "Cada vez mais..."

**Antes (IA):**
> Precisamos repensar a forma como contratamos. Precisamos questionar os processos legados. Precisamos ouvir mais e falar menos. Precisamos aceitar que o modelo antigo não funciona mais. Precisamos de coragem para mudar.

**Depois (humano):**
> Precisamos repensar a forma de contratar e questionar os processos legados. O modelo antigo já não funciona; é hora de ouvir mais, falar menos e ter coragem para mudar.

**Evite em PT-BR:**
- "Precisamos..." repetido 3+ vezes
- "É hora de..." repetido em sequência
- "Cada vez mais..." como abertura de múltiplos parágrafos

### A8. O X? Um Y.

Id Jev: `linguagem_pergunta_autoresposta`.

A pergunta retórica autorrespondida imita redação publicitária. Usada uma vez, pode funcionar. Repetida em todo parágrafo, vira sequência de falsas revelações, tique de redator de LinkedIn.

**Gatilhos:** "O resultado? [Substantivo/frase dramática]." / "A resposta? [Afirmação categórica]." / "O segredo? [Revelação]." / "O problema? [Diagnóstico]." / "A solução? [Receita]." / "O impacto? [Superlativo]."

**Antes (IA):**
> O desafio? Escalar sem perder cultura. A solução? Contratar por valores, não por currículo. O resultado? Um time coeso que entrega 3x mais. O segredo? Autonomia com responsabilidade. O futuro? Uma empresa que não depende de um fundador.

**Depois (humano):**
> O desafio é escalar sem perder a cultura. A solução proposta é contratar por valores, não por currículo. O resultado é um time coeso que entrega três vezes mais. O segredo é combinar autonomia com responsabilidade. O futuro imaginado é uma empresa que não depende do fundador.

**Evite em PT-BR:**
- "O resultado? Um time coeso."
- "O segredo? Consistência."
- "A resposta? Simplicidade." (especialmente em sequência)

### A9. Decalques sintáticos (anglicismos ocultos)

Id Jev: `linguagem_decalque_sintatico`.

Decalque é estrutura do inglês traduzida ao pé da letra. Não é estrangeirismo legítimo (deploy, feedback, sprint). O brasileiro usa o jargão inglês cru OU a expressão portuguesa equivalente, nunca a tradução literal.

**Gatilhos:** "endereçar um problema" (to address), "no final do dia" (at the end of the day), "performar" (to perform), "fazer sentido" (em excesso — to make sense), "estar no lugar" (to be in place), "correr um experimento" (to run an experiment), "levantar uma questão" (to raise a question), "colocar de outra forma" (to put it another way), "em termos de" (in terms of), "baseado em" sem sujeito (based on)

**Antes (IA):**
> Precisamos endereçar esse problema antes do próximo sprint. No final do dia, o que importa é se a funcionalidade performa bem em produção. Temos todas as peças no lugar para correr esse experimento. Isso levanta uma questão importante em termos de escalabilidade.

**Depois (humano):**
> Precisamos resolver esse problema antes do próximo sprint. No fim das contas, importa saber se a funcionalidade funciona bem em produção. Está tudo pronto para executar o experimento, o que traz uma questão sobre escalabilidade.

**Evite em PT-BR:**
- "Endereçar um problema" → "resolver" / "tratar" / "atacar"
- "No final do dia" → "no fim das contas" / "no fundo" / "na prática"
- "Performar" (como verbo intransitivo) → "funcionar" / "rodar" / "se sair"
- "Fazer sentido" em excesso (1-2x ok; 5x no texto = cacoete de tradução)
- "Estar no lugar" / "ter no lugar" → "estar pronto" / "ter configurado"
- "Correr um experimento" → "rodar" / "fazer" / "executar"
- "Levantar uma questão" → "trazer uma questão" / "trazer um ponto", preservando se o original expressa dúvida ou apenas assunto
- "Colocar de outra forma" → "dizendo de outro jeito" / "ou seja"
- "Em termos de" → "sobre" / "quanto a" / "de" (geralmente dá pra cortar)
- "Baseado em" sem sujeito ("Baseado nisso, decidimos...") → "Com base nisso" / "A partir disso"
- "Dar uma olhada em" (to take a look at) → "ver" / "conferir" / "olhar"
- "Estar na mesma página" (to be on the same page) → "estar alinhado" / "ter combinado"

**Alternativas:**
- Prefira o verbo português que o brasileiro usa na fala: "resolver", "rodar", "funcionar"
- Quando o jargão inglês for natural no perfil, mantenha-o: “rodar o teste A/B” é preferível a “correr um experimento”
- Teste lendo em voz alta: se soa como legenda de série, é decalque

**Nota:**
- “Fazer sentido” já se naturalizou no PT-BR. O problema é a repetição mecânica.
- Avalie a frequência em relação ao tamanho, ao perfil e à voz do texto.
- Nunca trate a frequência isoladamente como prova de autoria.

## Parte B: exclusivos do PT-BR

Os padrões abaixo existem só em PT-BR. Eles vêm do português corporativo, jurídico e acadêmico brasileiro.

### B1. Gerundismo corporativo e gerúndio conclusivo

#### Gerundismo corporativo

Id Jev: `ptbr_gerundismo`.

O gerundismo vem de e-mails corporativos e de scripts de SAC e telemarketing. Em texto "natural", indica automação.

**Gatilhos:** "vou estar enviando", "estaremos realizando", "vai estar recebendo", "iremos estar providenciando", "vamos estar agendando"

**Antes (IA):**
> Vou estar enviando o relatório de métricas do Q2 para validação. A equipe de produto vai estar realizando a análise de impacto e estaremos agendando uma call para alinhamento na próxima semana.

**Depois (humano):**
> Vou enviar o relatório de métricas do Q2 para validação. A equipe de produto vai analisar o impacto, e vamos agendar uma call de alinhamento na próxima semana.

**Evite em PT-BR:**
- "Vou estar enviando"
- "Estaremos realizando"
- "Vai estar recebendo"
- "Iremos estar providenciando"
- "Vamos estar disponibilizando"

**Alternativas:**
- "Vou estar enviando" → "Vou enviar"
- "Estaremos realizando" → "Realizaremos"
- "Vai estar recebendo" → "Vai receber"
- "Iremos estar providenciando" → "Providenciaremos"
- "Vamos estar disponibilizando" → "Vamos disponibilizar"

**Marque como sinal:**
- "Vai estar + gerúndio" em e-mails de SAC e respostas de chatbot
- "Iremos estar + gerúndio" em comunicações formais de empresas
- Gerundismo em texto que deveria ser direto (mensagens de WhatsApp, Slack)

**Correção:**
- Converta para futuro simples.
- Se o gerúndio indica processo contínuo real, mantenha-o e simplifique só a perífrase, sem trocar o verbo da fonte.
- Preserve sujeito, prazo e modalidade. Não dê data a promessa vaga. Não transforme ação futura em ação concluída.
- Aplique o Teste do áudio: leia a frase em voz alta. Se soa como atendente de telemarketing, é gerundismo.

#### Gerúndio conclusivo (falsa análise de impacto)

Id Jev: `conteudo_gerundio_analise`. A entrada A3 de [padroes-conteudo-tom.md](padroes-conteudo-tom.md) remete a esta técnica.

A oração de gerúndio funciona como "conclusão automática por frase": finge ser análise de impacto e repete o que o leitor já deduziu. Humanos tiram a conclusão em frase separada ou a deixam para o leitor.

**Gatilhos:** "..., destacando a importância de...", "..., contribuindo para...", "..., demonstrando que...", "..., reforçando a necessidade de...", "..., evidenciando que...", "..., mostrando como...", "..., sublinhando o papel de...", "..., consolidando a posição de..."

**Antes (IA):**
> A Nubank atingiu 100 milhões de clientes em 2025, consolidando sua posição como maior fintech da América Latina. O app teve nota 4.8 na App Store, demonstrando que a experiência do usuário continua sendo prioridade. A empresa expandiu para México e Colômbia, reforçando a necessidade de adaptação local.

**Depois (humano):**
> A Nubank atingiu 100 milhões de clientes em 2025 e consolidou sua posição como a maior fintech da América Latina. O app teve nota 4,8 na App Store; isso demonstrou que a experiência do usuário continua sendo prioridade. A empresa expandiu para México e Colômbia, o que reforçou a necessidade de adaptação local.

**Evite em PT-BR:**
- "..., destacando a importância de [coisa óbvia]"
- "..., contribuindo para o fortalecimento de..."
- "..., demonstrando que [conclusão que já estava implícita]"
- "..., reforçando a necessidade de..."
- "..., evidenciando o compromisso com..."
- "..., consolidando [posição/presença/papel]"
- Qualquer gerúndio no final que funciona como "mini-conclusão" redundante

**Alternativas:**
- Corte a oração de gerúndio somente quando ela for semanticamente redundante.
- Se a oração expressa conclusão, causalidade ou modalidade, transforme-a em frase finita sem apagar essa relação.
- Reaproveite um detalhe concreto já presente, sem substituí-lo por uma conclusão que também faça parte da fonte.
- Use coordenação simples: "e consolidou sua posição como a maior" em vez de "consolidando sua posição como a maior"

**Marque como sinal:**
- Oração reduzida de gerúndio no final de frase como "conclusão automática"
- Padrão: [afirmação], [gerúndio conclusivo] → "O app tem nota 4.8, demonstrando que UX é prioridade"

**Correção:**
- Corte o gerúndio apenas se a remoção não alterar nenhuma proposição.
- Se a conclusão integra o conteúdo, transforme-a em frase independente, preservando sujeito e força da afirmação.
- Aplique o Teste do copy-paste: se a frase ainda diz tudo sem a oração de gerúndio, o gerúndio é redundante.

### B2. Latinismo jurídico em texto informal

Id Jev: `ptbr_conectivo_arcaico`.

Estas palavras pertencem a contratos, decisões judiciais e regulamentos universitários.

**Gatilhos:** "ademais", "outrossim", "destarte", "não obstante", "doravante", "nesse diapasão", "mister se faz", "em última análise", "no bojo de", "ab initio"

**Antes (IA):**
> A implementação do novo sistema de pagamentos trouxe resultados expressivos. Ademais, a taxa de churn reduziu 15%. Outrossim, o NPS subiu 12 pontos. Destarte, pode-se concluir que a estratégia foi bem-sucedida.

**Depois (humano):**
> A implementação do novo sistema de pagamentos trouxe resultados expressivos: a taxa de churn caiu 15%, e o NPS subiu 12 pontos. Isso permite concluir que a estratégia foi bem-sucedida.

**Evite em PT-BR:**
- "Ademais" (fora de petições judiciais)
- "Outrossim" (em qualquer contexto que não seja um contrato)
- "Destarte" (ninguém fala isso desde 1920)
- "Nesse diapasão" (só juiz usa)
- "Mister se faz" (linguagem de despacho)
- "Doravante" (até em contratos tá caindo em desuso)

**Alternativas:**
- "Ademais" → "Além disso" / "E ainda"; use apenas vírgula se a relação aditiva continuar inequívoca
- "Outrossim" → "Também" / "E"; corte somente se não houver relação adicional a preservar
- "Destarte" → "Então" / "Por isso" / "Resultado:"
- "Não obstante" → "Mesmo assim" / "Apesar disso" / "Mas"
- "Doravante" → "A partir de agora" / "De agora em diante"

**Marque como sinal:**
- "Outrossim" em qualquer contexto que não seja petição judicial
- "Destarte" em textos pós-2000
- "Nesse diapasão" em comunicação corporativa moderna
- Texto que parece ter sido escrito por alguém que leu muito Diário Oficial

**Correção:**
- Substitua por conectivos modernos de mesmo valor lógico. Não apague contraste, conclusão nem marco temporal.
- Se o texto é jurídico, mantenha: é o registro esperado.
- Aplique o Teste do Slack: se você não escreveria no Slack da empresa, é arcaico.

### B3. Abertura estilo ENEM

Id Jev: `ptbr_abertura_enem`.

A abertura imita a redação nota 1000 do ENEM: contextualiza o tema de forma ampla antes de dizer algo específico.

**Gatilhos:** "Em um mundo cada vez mais...", "No cenário atual...", "Na contemporaneidade...", "É inegável que...", "Diante do exposto...", "No contexto de...", "Em meio a um cenário de..."

**Antes (IA):**
> Em um mundo cada vez mais digitalizado, as fintechs brasileiras vêm desempenhando um papel fundamental na democratização do acesso a serviços financeiros. No cenário atual, é inegável que a tecnologia transformou a maneira como lidamos com dinheiro.

**Depois (humano):**
> O mundo está cada vez mais digitalizado, e as fintechs brasileiras vêm desempenhando um papel fundamental na democratização do acesso a serviços financeiros. Hoje, é inegável que a tecnologia transformou a maneira como lidamos com dinheiro.

**Evite em PT-BR:**
- "Em um mundo cada vez mais [adjetivo]..."
- "No cenário atual..."
- "Na contemporaneidade..."
- "É inegável que..."
- "No contexto de [tema genérico]..."
- "Diante de um cenário de..."
- "É sabido que..."
- "Nos dias atuais..."

**Alternativas:**
- Comece com dado concreto somente quando ele já estiver no texto-fonte.
- Comece com afirmação direta que preserve a tese e o grau de certeza existentes.
- Use pergunta apenas quando ela mantiver a modalidade do trecho e combinar com o perfil de voz.
- Comece com exemplo somente se a fonte o forneceu.
- Comece pelo meio: pule o contexto e vá direto ao ponto.

**Marque como sinal:**
- "É inegável que" como abertura de parágrafo
- "No contexto contemporâneo" como introdução genérica
- "Diante do exposto" como transição entre seções
- Abertura que poderia ser copiada para qualquer redação de vestibular

**Correção:**
- Se o texto precisa de contexto, coloque o contexto DEPOIS do gancho, não antes.
- Aplique o Teste do primeiro tweet: se a abertura seria um tweet que ninguém leria, é ENEM demais.

### B4. Ressalva burocrática

Id Jev: `ptbr_ressalva_burocratica`. A entrada B6 de [padroes-conteudo-tom.md](padroes-conteudo-tom.md) remete a esta técnica.

Estas expressões preenchem espaço sem dizer nada e evitam o compromisso com a afirmação. Brasileiro real, para ressaltar algo, simplesmente diz.

**Gatilhos:** "Vale ressaltar que...", "É importante destacar que...", "Cumpre salientar que...", "Faz-se necessário...", "É fundamental observar que...", "Convém mencionar que...", "Importa registrar que...", "Merece atenção o fato de que..."

**Antes (IA):**
> Vale ressaltar que a taxa de conversão do funil apresentou crescimento significativo. É importante destacar que esse resultado está diretamente relacionado à implementação das novas landing pages. Cumpre salientar que a equipe de growth executou 14 testes A/B no período.

**Depois (humano):**
> A taxa de conversão do funil cresceu significativamente. Esse resultado está diretamente relacionado à implementação das novas landing pages. A equipe de growth executou 14 testes A/B no período.

**Evite em PT-BR:**
- "Vale ressaltar que..."
- "É importante destacar que..."
- "Cumpre salientar que..."
- "Faz-se necessário observar que..."
- "É fundamental que se reconheça..."
- "Convém mencionar que..."
- "Importa registrar que..."
- "Merece destaque o fato de que..."

**Alternativas:**
- Corte a expressão inteira e comece pela informação, sem quantificar o que a fonte não quantificou: "A taxa de conversão cresceu significativamente."
- Se precisa enfatizar, use a posição na frase (coloque no início) ou itálico.
- Em perfil neutro, use transição discreta ou nenhuma.
- Em perfil informal, escolha uma chamada compatível com a voz já existente.

**Marque como sinal:**
- "Cumpre salientar" como abertura de frase
- "Faz-se necessário" em e-mails de trabalho
- "Importa registrar" em textos que não são registro oficial
- Duas ou mais expressões de ressalva no mesmo parágrafo

**Correção:**
- Para ênfase, use também a repetição intencional.
- Aplique o Teste do post-it: se a informação cabe num post-it sem perder sentido, a muleta era desnecessária.

### B5. Formalidade deslocada

Id Jev: `ptbr_formalidade_deslocada`.

O modelo confunde "escrever bem" com "escrever formal". O registro formal extremo pertence a ofícios, memorandos e atas, não a e-mail de produto, blog de tecnologia ou comunicação interna de startup.

**Gatilhos:** "No que tange a", "Tendo em vista que", "O referido", "Conforme mencionado anteriormente", "O supracitado", "No tocante a", "Em face do exposto", "Haja vista que"

**Antes (IA):**
> No que tange à implementação do novo design system, tendo em vista que a equipe de front-end sinalizou gargalos, faz-se necessário priorizar a refatoração do referido sistema de componentes. Conforme mencionado anteriormente, o supracitado projeto tem deadline no Q3.

**Depois (humano):**
> Sobre a implementação do design system: como a equipe de front-end sinalizou gargalos, é necessário priorizar a refatoração desse sistema de componentes. Como já mencionado, o projeto tem deadline no Q3.

**Evite em PT-BR:**
- "No que tange a" (fora de parecer jurídico)
- "Tendo em vista que" (fora de justificativa formal)
- "O referido" / "O supracitado" (fora de processo judicial)
- "Conforme mencionado anteriormente" (redundante: se mencionou, o leitor sabe)
- "Em face do exposto" (conclusão de parecer)
- "Haja vista que" (pedante em qualquer contexto informal)
- "No tocante a" (burocracia pura)

**Alternativas:**
- "No que tange a" → "Sobre" / "Quanto a"
- "Tendo em vista que" → "Como" / "Já que" / "Porque"
- "O referido" → "Esse" / "O"; corte somente se o referente continuar inequívoco
- "Conforme mencionado anteriormente" → "Como já mencionado"; corte somente se a referência anterior não tiver função
- "Em face do exposto" → "Diante disso" / "Por isso", quando introduzir conclusão
- "Haja vista que" → "Já que" / "Porque"

**Marque como sinal:**
- "No que tange a" em e-mails de produto
- "Tendo em vista que" em mensagens de Slack
- "O referido projeto" em comunicação interna
- Registro formal em contexto onde a informalidade é esperada

**Correção:**
- Mapeie o **perfil de voz** antes de reescrever e reduza apenas a formalidade deslocada.
- Substitua por equivalentes brasileiros compatíveis com o canal, sem forçar coloquialidade.
- Aplique o Teste do canal: a formulação combina com o meio, o público e a voz do texto-fonte?

### B6. Oficialês

Id Jev: `ptbr_oficiales`.

Oficialês é o dialeto de ofício, memorando e despacho. Fora do contexto público ou legal, denuncia geração automática.

**Gatilhos:** "Segue em anexo para os devidos fins", "Venho por meio deste", "Solicito a gentileza de", "Segue para conhecimento e providências", "Informo para os devidos fins", "Encaminho o presente para apreciação", "Trata o presente de"

**Antes (IA):**
> Venho por meio deste comunicar que a feature de onboarding encontra-se em fase final de implementação. Solicito a gentileza de agendar a revisão de código para os devidos fins de validação. Segue em anexo o documento de especificação para conhecimento e eventuais providências.

**Depois (humano):**
> A feature de onboarding está na fase final de implementação. Solicito o agendamento da revisão de código para validação. O documento de especificação segue anexo para conhecimento e eventuais providências.

**Evite em PT-BR:**
- "Venho por meio deste [comunicar/informar/solicitar]"
- "Segue em anexo para os devidos fins"
- "Solicito a gentileza de"
- "Para conhecimento e providências"
- "Informo para os devidos fins que"
- "Trata o presente [e-mail/documento] de"
- "Sirvo-me do presente para"
- "Encaminho para apreciação superior"

**Alternativas:**
- "Venho por meio deste informar que [fato]" → "[Fato]", sem apresentá-lo como novidade se a fonte não fizer isso
- "Segue em anexo" → "O arquivo segue anexo" / "O arquivo está anexado", conforme o perfil
- "Solicito a gentileza de [ação]" → "Solicito que [ação]"; em perfil informal, "Pode [ação]?"
- "Para conhecimento" → "Para informar" / "Para ciência", preservando a finalidade
- "Para os devidos fins" → cortar somente quando não designar uma finalidade específica

**Marque como sinal:**
- "Venho por meio deste" em qualquer canal que não seja ofício público
- "Para os devidos fins" como fechamento de e-mail
- "Solicito a gentileza de" em mensagens internas
- Texto que parece ter sido gerado por um chatbot de órgão público

**Correção:**
- Converta para linguagem direta sem criar prazo ou responsável: "Preciso que você faça X". Mantenha o prazo somente se ele existir na fonte.
- Em comunicação externa formal, mantenha um nível mínimo de polidez, sem oficialês.
- Aplique o Teste do canal: a formulação mantém a polidez e a voz esperadas naquele contexto?

### B7. Evitação de verbos simples (inclui os verbos de ligação de A2)

Id Jev: `linguagem_evitacao_copula`.

O modelo substitui "É/São/Tem" por eufemismos rebuscados que ninguém diria em voz alta. Substitui também o "ter" existencial por "haver" ou "existir", hipercorreção que o brasileiro não pratica na fala.

**Gatilhos (verbos de ligação):** configura-se como, constitui, representa, figura como, posiciona-se como, desponta como, consolida-se como, atua como, funciona como, opera como, se estabelece como

**Gatilhos (verbos simples):** "constitui", "configura-se como", "dispõe de", "encontra-se", "figura como", "representa", "serve como", "afigura-se como", "situa-se", "apresenta-se como", "há [quantidade]", "existem [quantidade]", "haver necessidade"

**Antes (IA), par 1:**
> O Nubank configura-se como a maior fintech da América Latina. A plataforma desponta como referência em experiência do usuário e consolida-se como alternativa aos bancos tradicionais.

**Depois (humano), par 1:**
> O Nubank é a maior fintech da América Latina. A plataforma é referência em experiência do usuário e uma alternativa aos bancos tradicionais.

**Antes (IA), par 2:**
> O Nubank constitui uma das maiores fintechs da América Latina e configura-se como referência em experiência do usuário. A empresa dispõe de mais de 80 milhões de clientes e encontra-se em expansão para novos mercados. Seu modelo de negócios figura como paradigma para startups do setor.

**Depois (humano), par 2:**
> O Nubank é uma das maiores fintechs da América Latina e é referência em experiência do usuário. A empresa tem mais de 80 milhões de clientes e está em expansão para novos mercados. Seu modelo de negócios é um paradigma para startups do setor.

**Evite em PT-BR:**
- "Configura-se como / consolida-se como"
- "Desponta como referência em"
- "Posiciona-se como alternativa a"
- "constitui [algo]" (quando "é" resolve)
- "configura-se como" (quando "é" resolve)
- "dispõe de" (quando "tem" resolve)
- "encontra-se [em algum estado]" (quando "está" resolve)
- "figura como" (quando "é" resolve)
- "situa-se" (quando "fica" ou "está" resolve)
- "apresenta-se como" (quando "parece" ou "é" resolve)
- "afigura-se como" (ninguém fala isso)
- "há muitos/muitas [X]" (quando "tem muito/muita [X]" é mais natural: perfis Crônica, Corporativo Informal e WhatsApp)
- "existem diversas opções" (quando "tem várias opções" resolve)
- "não há como negar" (quando "não tem como negar" soa brasileiro)

**Alternativas:**
- "constitui uma referência" → "é referência"
- "dispõe de 80 milhões" → "tem 80 milhões"
- "encontra-se em expansão" → "está em expansão"
- "configura-se como líder" → "é líder"
- "situa-se entre os maiores" → "está entre os maiores" / "é um dos maiores"
- "há muitas pessoas" → "tem muita gente"
- "existem diversos fatores" → "tem vários fatores" / "são vários fatores"
- "há necessidade de" → "precisa de" / "tem que"
- "não há dúvidas de que" → "não tem dúvida que" / "é claro que"

**Nota sobre "ter" existencial:**
- Em perfis formais (Acadêmico), "haver" pode permanecer.
- Em Crônica, Corporativo Informal, Rede Social e WhatsApp, o "ter" existencial pode ser a forma natural brasileira.
- Escolha conforme o perfil de voz. Não altere quantidade, existência nem modalidade.

**Marque como sinal:**
- Texto onde os verbos "ser", "ter", "estar" foram sistematicamente substituídos
- "Dispõe de" em vez de "tem", "Configura-se como" em vez de "é", "Encontra-se em" em vez de "está"

**Correção:**
- Restaure verbos simples quando apropriado ao registro.
- Se o texto é acadêmico ou jurídico, mantenha a formalidade, mas evite o excesso.
- Aplique o Teste da fala: se você não falaria assim, não escreva assim.

### B8. Expressões infladas

O modelo produz expressões que parecem tradução de jargão corporativo americano. Elas aparecem em relatório anual e PowerPoint, não na explicação de alguém. Se você não diria a frase em voz alta numa reunião, não a escreva.

**Gatilhos:** "contribui significativamente para", "no âmbito de", "de forma expressiva", "em termos de", "a nível de", "no que diz respeito a", "sob a ótica de", "à luz de", "na esfera de", "potencializar"

**Antes (IA):**
> A estratégia de product-led growth contribui significativamente para a escalabilidade do negócio no âmbito do mercado brasileiro de SaaS. No que diz respeito à aquisição de usuários, a abordagem potencializa os resultados de forma expressiva, sob a ótica da eficiência operacional.

**Depois (humano):**
> A estratégia de product-led growth contribui bastante para a escalabilidade do negócio no mercado brasileiro de SaaS. Na aquisição de usuários, a abordagem melhora os resultados de forma expressiva do ponto de vista da eficiência operacional.

**Evite em PT-BR:**
- "contribui significativamente para" sem explicar o efeito; se a fonte não quantifica, preserve a intensidade qualitativa sem criar número
- "no âmbito de" (99% das vezes é só "em")
- "de forma expressiva/significativa" quando encobre um valor que já existe na fonte
- "no que diz respeito a" (é "sobre")
- "sob a ótica de" (é "pra" ou "do ponto de vista de")
- "potencializar" quando a fonte já permite escolher com precisão entre "melhorar" e "aumentar"
- "à luz de" (é "considerando" ou "com base em")
- "a nível de" (errado gramaticalmente E vazio semanticamente)
- "na esfera de" (é "em")

**Alternativas:**
- "contribui significativamente" → "contribui bastante"; use número somente quando ele já existir na fonte
- "no âmbito de" → "em" / "dentro de"; corte somente se não delimitar o escopo
- "potencializar resultados" → "melhorar resultados"; nomeie a métrica somente se a fonte a identificar
- "de forma expressiva" → mantenha a intensidade qualitativa ou use a medida já informada
- "no que diz respeito a" → "sobre" / "quanto a"
- "sob a ótica de" → "do ponto de vista de", sem criar um agente ausente

**Marque como sinal:**
- "No que diz respeito a" em vez de "sobre", "Sob a ótica de" em vez de "do ponto de vista de", "À luz de" em vez de "com base em"
- Expressões que parecem tradução literal de "in terms of", "from the perspective of"

**Correção:**
- Substitua por equivalentes diretos em português.
- Aplique a regra de compressão: se a expressão tem 5+ palavras e cabe em 1-2, comprima.
- Aplique o Teste da tradução reversa: se a expressão parece traduzida do inglês corporativo, troque-a pelo equivalente que o brasileiro realmente fala.

### B9. Transições mecânicas e estrutura de parágrafo idêntica

Id Jev: `ptbr_transicao_mecanica`. O formato de parágrafo no nível da composição está em [padroes-composicao.md](padroes-composicao.md#colapso-estrutural) (Colapso estrutural).

Todo parágrafo abre com conectivo, num ritmo mecânico. É o equivalente brasileiro de "Furthermore" e "Moreover". Humanos variam: às vezes transição, às vezes abertura direta, pergunta ou exemplo. Repetir "Além disso... Nesse sentido... Diante disso..." a cada parágrafo é assinatura de IA.

**Gatilhos:** "Além disso", "Nesse sentido", "Diante disso", "Em contrapartida", "Por outro lado", "No entanto", "Dessa forma", "Sendo assim", "Nessa perspectiva", "À vista disso"

**Antes (IA):**
> O mercado de SaaS B2B no Brasil cresceu 40% em 2025. **Além disso**, a entrada de novos players internacionais acirrou a competição. **Nesse sentido**, startups brasileiras precisam diferenciação clara. **Diante disso**, estratégias de nicho ganham relevância. **Em contrapartida**, o aumento de competição também valida o mercado. **Dessa forma**, empresas que encontrarem seu posicionamento tendem a prosperar.

**Depois (humano):**
> O mercado de SaaS B2B no Brasil cresceu 40% em 2025. A entrada de novos concorrentes internacionais acirrou a competição. Por isso, startups brasileiras precisam de diferenciação clara, e estratégias de nicho ganham relevância. Ao mesmo tempo, o aumento da competição também valida o mercado. Empresas que encontrarem seu posicionamento tendem a prosperar.

**Evite em PT-BR:**
- "Além disso" como abertura de mais de 1 parágrafo no mesmo texto
- "Nesse sentido" sem referência clara ao "sentido"
- "Diante disso" / "Diante do exposto" (dissertação de ENEM)
- "Em contrapartida" quando não há real contrapartida
- "Por outro lado" quando não há dois lados claros
- "Dessa forma" / "Sendo assim" como conclusão automática
- Qualquer padrão de [conectivo] + [afirmação] repetido 3+ vezes seguidas

**Alternativas:**
- Comece com o conteúdo direto, sem transição: "Startups brasileiras precisam se diferenciar."
- Use pergunta retórica apenas se ela não mudar a modalidade e combinar com o perfil de voz.
- Use fragmento com conteúdo existente: "Resultado: estratégias de nicho ganham relevância."
- Use exemplo concreto somente quando ele já estiver no texto-fonte.
- Use contraste implícito (sem "por outro lado"): "Só que mais competição também valida o mercado."
- Continue com "E", "Mas", "Só que" ou "Agora", escolhendo apenas o conectivo que preserve a relação original.

**Estrutura de parágrafo idêntica:**
- Não repita em todo parágrafo a sequência frase-tópico, explicação, exemplo, transição.
- Comece alguns parágrafos com pergunta e outros com afirmação direta.
- Deixe alguns parágrafos com uma frase só. Deixe alguns terminarem sem transição.
- Em reescrita, reordene apenas as proposições existentes.

### B10. Purismo linguístico

Id Jev: `ptbr_purismo_linguistico`. A lista de estrangeirismos preservados e a regra de ouro estão em [SKILL.md](../SKILL.md), seção Estrangeirismos preservados.

Forçar a tradução de termo naturalizado é um dos sinais mais claros de IA em PT-BR tech. "Vamos reduzir o churn" é a forma natural. "Vamos reduzir a rotatividade de clientes" soa como livro técnico de 2003.

**Gatilhos:** "retroalimentação" (feedback), "implantação" (deploy), "rotatividade de clientes" (churn), "corrida/iteração" (sprint), "fluxo de trabalho" (workflow), "partes interessadas" (stakeholders), "entregáveis" (deliverables), "plataforma de dados" (data lake)

**Antes (IA):**
> A equipe realizou a implantação do novo microsserviço e obteve retroalimentação positiva das partes interessadas. A rotatividade de clientes diminuiu após a iteração focada em experiência do usuário. O fluxo de trabalho foi otimizado para entregar os entregáveis dentro do prazo da corrida.

**Depois (humano):**
> A equipe fez o deploy do novo microsserviço e recebeu feedback positivo dos stakeholders. O churn diminuiu após a sprint focada em experiência do usuário. O workflow foi otimizado para entregar os deliverables dentro do prazo da sprint.

**Evite em PT-BR a tradução, quando o termo inglês já é padrão no mercado:**
- "retroalimentação" em vez de "feedback"
- "implantação" em vez de "deploy" (contexto tech)
- "rotatividade de clientes" em vez de "churn"
- "corrida" ou "iteração" em vez de "sprint"
- "partes interessadas" em vez de "stakeholders"
- "entregáveis" em vez de "deliverables"
- "fluxo de trabalho" em vez de "workflow"
- "computação em nuvem" em vez de "cloud" (contexto dev)
- "aprendizado de máquina" em vez de "machine learning" (contexto tech)
- "cadeia de suprimentos" em vez de "supply chain" (contexto startup/ops)

**Alternativas:**
- Use o termo em inglês como o brasileiro usa: "feedback", "deploy", "churn", "sprint"
- Se o usuário pedir explicação para público não técnico, use o termo + explicação sem acrescentar consequência: "churn (perda de clientes)"
- Mantenha consistência: se usou "deploy" uma vez, não alterne com "implantação"
- Preserve a terminologia do texto-fonte. Adapte-a apenas quando o perfil de voz ou o público exigirem e houver equivalente sem perda de precisão

### B11. Colocação pronominal artificial

O modelo usa ênclise (verbo + pronome) e até mesóclise onde o brasileiro usa próclise (pronome + verbo). Na escrita real, a próclise domina em quase todos os contextos. Ênclise excessiva soa como manual de gramática de Portugal.

**Gatilhos:** "Apresento-lhe", "Trata-se de", "Faz-se necessário", "Encontra-se disponível", "Realizou-se", "Dar-se-á", "Enviar-lhe-ei", "Diga-se de passagem", "Permite-nos afirmar"

**Antes (IA):**
> O sistema permite-nos monitorar métricas em tempo real. Trata-se de uma solução que integra-se facilmente ao stack existente. Encontra-se disponível para todos os planos. Enviar-lhe-emos o relatório até sexta.

**Depois (humano):**
> O sistema nos permite monitorar métricas em tempo real. É uma solução que se integra facilmente ao stack existente. Está disponível para todos os planos. Nós lhe enviaremos o relatório até sexta.

**Evite em PT-BR:**
- "Permite-nos" (quando "nos permite" é mais natural)
- "Trata-se de" em excesso (quando "é" resolve)
- "Encontra-se" (quando "está" ou "fica" resolve)
- "Integra-se" no início ou meio de frase (quando "se integra" soa melhor)
- Qualquer mesóclise fora de texto jurídico ou literário intencional ("dar-se-á", "enviar-lhe-ei")
- Ênclise após sujeito explícito: "O usuário cadastra-se" → "O usuário se cadastra"

**Alternativas:**
- "Permite-nos" → "nos permite"; "deixa a gente" somente em perfil informal já autorizado
- "Trata-se de" → "É" / "Isso é"
- "Encontra-se disponível" → "Está disponível"; "Tá disponível" somente em perfil informal
- "Realizou-se a migração" → "A migração foi realizada", sem inventar quem a realizou
- "Dar-se-á início" → "Terá início" / "Vai começar", preservando o tempo verbal
- "Faz-se necessário" → "Precisa" / "É necessário"

**Nota:**
- A ênclise é legítima após vírgula, no início absoluto de frase e em imperativos ("Diga-me", "Faça-o").
- O problema é a ênclise em posições onde o brasileiro coloca o pronome antes do verbo.

### B12. Voz passiva analítica

A passiva analítica (ser + particípio) vem do inglês, onde é mais frequente. Em PT-BR natural, prefira a voz ativa ou a passiva sintética (com "se"). Sequências de 3+ frases em passiva soam como tradução automática de release notes em inglês.

**Gatilhos:** "foi realizado por", "foi implementado pela equipe", "será desenvolvido pelo time", "foi identificado que", "é considerado como", "foi constatado que", "foram obtidos resultados", "foi tomada a decisão"

**Antes (IA):**
> O relatório foi finalizado pela equipe de dados. A análise foi conduzida utilizando metodologia ágil. Foram identificados 3 gargalos principais. A decisão foi tomada de priorizar o módulo de pagamentos. Os testes foram realizados em ambiente de staging.

**Depois (humano):**
> A equipe de dados finalizou o relatório. Na análise, conduzida com metodologia ágil, foram identificados 3 gargalos principais. Decidiu-se priorizar o módulo de pagamentos. Os testes foram realizados em ambiente de staging.

**Evite em PT-BR:**
- "O relatório foi finalizado pela equipe" → "A equipe finalizou o relatório" / "A equipe concluiu o relatório"
- "Foi identificado que" → "Identificou-se que"; nomeie o agente apenas se a fonte o informar
- "A decisão foi tomada" → "Decidiu-se"; use "A equipe decidiu" somente se esse agente constar da fonte
- "Foram obtidos resultados positivos" → "Houve resultados positivos"
- "É considerado como referência" → "É referência"
- 3+ frases consecutivas em voz passiva
- "Está sendo feito", "foi constatado que", "é considerado como" (equivalentes de "is being done," "was found to be," "are considered to be.")

**Alternativas:**
- Use voz ativa quando o sujeito estiver explícito: "A equipe entregou" em vez de "Foi entregue pela equipe"
- Use passiva sintética (com "se"): "Identificaram-se 3 bugs"
- Use indeterminação do sujeito somente quando a fonte também não identifica o agente.
- Use inversão simples: "Concluiu-se o relatório" em vez de "O relatório foi concluído"

**Nota:**
- A passiva é legítima quando o agente é desconhecido ou irrelevante ("O servidor foi invadido").
- A passiva é legítima em gêneros formais (jurídico, acadêmico, normativo).
- O problema é usá-la quando existe um sujeito claro que deveria estar agindo.
- Nunca invente um agente para eliminar a passiva.
- Sinalize 3 ou mais passivas consecutivas.

## Lista rápida de verificação

|#|Padrão|Teste rápido|
|---|---|---|
|1|Gerundismo|Tem "vou estar + gerúndio"?|
|2|Conectivos arcaicos|Tem "ademais", "outrossim", "destarte" fora de contexto jurídico?|
|3|Abertura ENEM|Começa com "Em um mundo cada vez mais..."?|
|4|Ressalva burocrática|Tem "Vale ressaltar que" ou "Cumpre salientar"?|
|5|Formalidade deslocada|Tem "No que tange a" num e-mail de startup?|
|6|Oficialês|Tem "Venho por meio deste" fora de ofício?|
|7|Evitação de verbos simples|"É" virou "constitui"? "Tem" virou "há"?|
|8|Expressões infladas|Tem "contribui significativamente" sem número?|
|9|Transições mecânicas|Todo parágrafo começa com conectivo?|
|10|Purismo linguístico|Traduziu "feedback", "deploy", "churn"?|
|11|Colocação pronominal artificial|Tem "permite-nos", "trata-se de", mesóclise?|
|12|Voz passiva analítica|3+ frases com "foi X pelo Y" em sequência?|

- Se 3+ padrões aparecem no mesmo texto: alta probabilidade de geração por IA.

## Contexto de calibração

Estes padrões são calibrados para texto profissional brasileiro nas áreas de:
- Tecnologia (dev, produto, infra)
- Startups e scale-ups
- Marketing digital
- Fintech e SaaS
- Comunicação corporativa moderna

- Aceite alguns destes padrões onde o gênero exige formalidade: petição judicial, artigo acadêmico publicado, comunicação diplomática.
- Considere o **perfil de voz** ativo antes de sinalizar.
