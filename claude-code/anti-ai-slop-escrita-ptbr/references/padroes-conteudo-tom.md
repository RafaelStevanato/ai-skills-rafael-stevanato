# Padrões de conteúdo e tom

## Regras de uso

- Carregue no Passo 3 quando a categoria Conteúdo ou Tom estiver marcada.
- Cumpra a TRAVA FACTUAL de [SKILL.md](../SKILL.md), seção Proteções obrigatórias. Trate o "Antes" como universo factual fechado.
- No "Depois", preserve proposições, entidades, números, datas, fontes, causalidade, modalidade e registro.
- Corte muletas, reorganize e simplifique. Nunca crie experiência pessoal, número, fonte, causa, opinião ou certeza.
- Nunca preencha lacuna com exemplo, dado, fonte ou experiência pessoal. Preserve a alegação ou a dúvida e aponte a lacuna no relatório.
- Corte, qualifique ou corrija somente com autorização do usuário.
- Ajuste ao perfil de voz ativo. Os "Depois" usam registro neutro.
  - Perfil formal: preserve qualificações, atribuições e impessoalidade funcional.
  - Perfil informal: use coloquialidade só se o usuário a pedir ou o original a tiver.
  - Nunca invente primeira pessoa para produzir "voz".
- Consulte o Passo 6 de [SKILL.md](../SKILL.md) antes de marcar qualquer padrão (guarda de falso positivo).
- O código sob cada título é o id Jev do padrão ([jev-integration.md](jev-integration.md)).
- Não copie para texto novo o travessão de aparte que alguns exemplos trazem ([padroes-estilo.md](padroes-estilo.md)).

## Parte A: conteúdo

### A1. Ênfase indevida em significância, legado e tendências

`conteudo_enfase_indevida`

**Gatilhos:** representa um marco, é um testemunho de, papel fundamental/crucial/vital, ressalta a importância, reflete uma tendência mais ampla, simbolizando o/a, contribuindo para o/a, preparando o terreno para, moldando o futuro de, cenário em constante evolução, ponto de inflexão, marca indelével, profundamente enraizado, redefine o paradigma

**Problema:** fato mundano vira revolução. Um CRUD vira "um marco na transformação digital". Um pivô de startup vira "um ponto de inflexão no ecossistema de inovação".

**Antes:**
> O Nubank representa um marco fundamental na transformação do cenário financeiro brasileiro, moldando ativamente o futuro das fintechs na América Latina e preparando o terreno para uma nova era de inclusão bancária digital.

**Depois:**
> O Nubank tem papel central na transformação do setor financeiro brasileiro. A empresa influencia o desenvolvimento das fintechs na América Latina e contribui para a inclusão bancária digital.

**Evitar:**
- "representa um marco na evolução de..."
- "moldando o futuro do ecossistema de..."
- "em um cenário em constante transformação"

**Sinais:**
- superlativo absoluto sem quantificação ("maior", "melhor", "sem precedentes", "inédito")
- verbo de transformação grandiosa ("redefinir", "moldar", "preparar o terreno")
- "ponto de inflexão" sem dizer o que muda depois

**Correção:**
- Troque superlativo por dado somente se o dado estiver na entrada. Sem dado, preserve a força da avaliação e aponte a lacuna.
- Troque verbo grandioso por verbo de ação já descrito no original. Sem ação descrita, use formulação direta sem criar evento.
- Aplique o "Teste do jornalista": se um repórter perguntaria "como assim?", o termo é vazio.
- Veja B10.

### A2. Ênfase forçada em notabilidade e cobertura de mídia

`conteudo_notabilidade_forcada`

**Gatilhos:** amplamente reconhecido, coberto pelos principais veículos, destaque na mídia especializada, presença ativa nas redes sociais, segundo especialistas do setor, referência no mercado

**Antes:**
> A empresa foi destaque na Exame, Valor Econômico, TechCrunch e Bloomberg. Amplamente reconhecida como referência no mercado de SaaS B2B brasileiro, mantém presença ativa nas redes sociais com mais de 200 mil seguidores.

**Depois:**
> A empresa apareceu na Exame, no Valor Econômico, no TechCrunch e na Bloomberg. É amplamente reconhecida no mercado brasileiro de SaaS B2B e soma mais de 200 mil seguidores nas redes sociais.

**Evitar:**
- "amplamente reconhecido(a) como referência em..."
- "destaque nos principais veículos do setor"
- "mantém presença ativa nas redes com X seguidores"

**Sinais:**
- veículos ou prêmios citados como prova de importância, sem dizer o que foi dito nem por que importa
- lista de veículos sem matéria específica (data, título, link)
- "Presença ativa nas redes" sem métrica (seguidores, engajamento)
- prêmio ou ranking sem fonte verificável

**Correção:**
- Se a entrada trouxer fonte, data ou link, preserve e cite só esses elementos.
- Sem fonte, preserve a alegação e sua atribuição e aponte a lacuna.
- Aplique o "Teste de verificabilidade": se o leitor não checa em 30 segundos, a informação é puffery.

### A3. Análises superficiais com gerúndio ou particípio

`conteudo_gerundio_analise`

Técnica canônica: [padroes-linguagem-ptbr.md](padroes-linguagem-ptbr.md), B1.

**Gatilhos:** ressaltando a importância de, demonstrando o compromisso com, refletindo a tendência de, contribuindo para o fortalecimento de, evidenciando o potencial de, impulsionando a inovação, fomentando o crescimento, consolidando sua posição como

**Antes:**
> A RD Station lançou integração nativa com WhatsApp Business, demonstrando seu compromisso com a inovação no marketing digital brasileiro e consolidando sua posição como líder no segmento, impulsionando a transformação digital das PMEs.

**Depois:**
> A RD Station lançou integração nativa com WhatsApp Business. O lançamento demonstra seu compromisso com a inovação no marketing digital brasileiro, consolida sua posição de liderança no segmento e impulsiona a transformação digital das PMEs.

**Evitar:**
- "demonstrando o compromisso da empresa com..."
- "consolidando sua posição como líder em..."
- "contribuindo para o fortalecimento do ecossistema"

**Sinais:**
- frase que termina em gerúndio como conclusão de análise
- "verbo composto + gerúndio" em sequência ("vem demonstrando", "vai estar consolidando")
- gerúndio como adjetivo ("inovando", "transformando", "impulsionando")

**Correção:**
- Converta a oração gerundial em oração finita com sujeito claro: "demonstrando compromisso" → "o lançamento demonstra o compromisso".
- Corte o gerúndio puramente decorativo: "impulsionando a transformação" → (nada; a frase principal já diz).
- Aplique o "Teste do podcast": se a frase em voz alta soa como narração de vídeo institucional, o gerúndio é excessivo.

### A4. Linguagem promocional e de propaganda

`conteudo_linguagem_promocional`

**Gatilhos:** solução inovadora, experiência única, ecossistema robusto, revolucionário, disruptivo, estado da arte, de ponta, excelência, sinergia, empoderar, potencializar, alavancar, impulsionar, viabilizar, transformador, game-changer, seamless (usado em PT)

**Problema:** o texto soa como copy de página de produto: tudo é "inovador", "revolucionário" e "de ponta".

**Antes:**
> A plataforma oferece uma solução inovadora e disruptiva que empodera equipes de produto a potencializarem seus resultados, entregando uma experiência seamless e de estado da arte para alavancar a transformação digital das organizações.

**Depois:**
> A plataforma oferece uma solução inovadora e disruptiva. Ela dá às equipes de produto meios para melhorar seus resultados, oferece uma experiência integrada e de alto nível e apoia a transformação digital das organizações.

**Evitar:**
- "solução inovadora e disruptiva que empodera..."
- "experiência única de ponta/estado da arte"
- "potencializar/alavancar a transformação digital"

**Sinais:**
- 2 ou mais buzzwords na mesma frase ("solução inovadora e disruptiva de ponta")
- adjetivos autocontraditórios ("seamless mas robusto", "simples mas poderoso")
- texto que serviria de copy para qualquer produto sem mudança

**Correção:**
- Reduza adjetivo decorativo sem apagar alegação substantiva. Sem evidência na entrada, qualifique a alegação como descrição da empresa ou do texto.
- Troque adjetivo por dado ou comparação somente se já estiver na entrada. Sem evidência, preserve a avaliação e aponte a lacuna.
- Aplique o "Teste do pitch deck": se a frase cabe em qualquer slide de qualquer startup, é genérica demais.
- Corte o tom de torcida corporativa (B5).

### A5. Atribuições vagas e weasel words

`conteudo_atribuicao_vaga`

**Gatilhos:** segundo especialistas, de acordo com analistas do setor, estudos apontam que, o mercado reconhece, é amplamente considerado, pesquisas indicam, fontes do setor afirmam, observadores notam que

**Problema:** autoridade genérica que não existe. Pergunte: quais especialistas? Qual estudo, de que ano, com que metodologia?

**Antes:**
> Segundo especialistas do setor, o modelo de negócios da empresa representa uma evolução significativa. Analistas de mercado reconhecem que a abordagem tem potencial para redefinir o segmento de healthtechs no Brasil.

**Depois:**
> Especialistas do setor não identificados consideram o modelo de negócios uma evolução significativa. Analistas também não identificados avaliam que a abordagem pode redefinir o segmento de healthtechs no Brasil.

**Evitar:**
- "segundo especialistas do setor..."
- "analistas de mercado reconhecem que..."
- "estudos/pesquisas apontam/indicam que..."

**Sinais:**
- quantificador vago: "muitos especialistas", "diversos estudos", "alguns analistas"
- referência sem data: "pesquisas recentes mostram..."
- afirmação controversa ou específica sem fonte

**Correção:**
- Se a fonte estiver na entrada, preserve autor, ano, título e link.
- Sem fonte, mantenha a atribuição como não identificada e aponte a lacuna.
- Nunca converta atribuição vaga em opinião ou experiência pessoal do revisor.
- Aplique o "Teste da fonte": se 2 minutos de busca não acham a fonte, a atribuição é weasel.
- Em texto novo, use nome, empresa e data reais no lugar de "um grande banco" ou "pesquisas mostram". Use-os somente se constarem do material do usuário.

### A6. Conclusões formulaicas sobre desafios e perspectivas futuras

`conteudo_conclusao_formulaica`

Veja também B5.

**Gatilhos:** apesar dos desafios, não obstante as dificuldades, o futuro é promissor, perspectivas animadoras, em um contexto de constante evolução, seguir crescendo, continuar inovando, trilhar um caminho de sucesso, superar obstáculos, rumo a um futuro, desafios e oportunidades

**Problema:** seção "Desafios e Perspectivas" sem conteúdo concreto. Lista problemas genéricos e conclui que "apesar disso, o futuro é promissor".

**Antes:**
> Apesar dos desafios inerentes ao mercado brasileiro — como a complexidade tributária e a concorrência acirrada — a startup segue trilhando um caminho de crescimento sustentável. Com perspectivas animadoras e um time comprometido com a inovação, a empresa está bem posicionada para continuar liderando a transformação do setor.

**Depois:**
> A startup enfrenta a complexidade tributária e a concorrência acirrada, mas mantém uma trajetória de crescimento sustentável. Suas perspectivas são animadoras, o time é comprometido com a inovação e a empresa está bem posicionada para continuar liderando a transformação do setor.

**Evitar:**
- "apesar dos desafios, o futuro é promissor"
- "a empresa segue bem posicionada para continuar..."
- "trilhando um caminho de crescimento sustentável"

**Sinais:**
- fórmula "Apesar de X, o futuro é Y", com X genérico e Y otimista
- "perspectivas animadoras" sem dizer o que anima
- conclusão que serviria a QUALQUER empresa do setor

**Correção:**
- Use previsão, prazo ou plano somente se já estiverem na entrada. Senão, nomeie só os desafios existentes e aponte a ausência de evidência.
- Se o original expressa incerteza, preserve-a sem criar cenário, consequência ou plano alternativo.
- Aplique o "Teste do horóscopo": se a conclusão caberia no horóscopo de qualquer signo, é genérica demais.

### A7. Fonte inventada (referência específica que não existe)

`conteudo_fonte_inventada`

**Gatilhos:** referência com autor e ano que não bate, DOI que não resolve, ISBN inválido, link quebrado, número de página inventado, citação atribuída a quem nunca a disse

**Problema:** distinto de A5. A fonte é **específica e falsa**, não vaga ("especialistas dizem"): sobrenome, ano, página e periódico não existem. A Wikipédia usa este sinal para eliminação rápida de artigo gerado por IA. É o único vício da lista que fabrica evidência.

**Antes:**
> Segundo Almeida (2019, p. 84), a adoção de metodologias ágeis reduziu em 37% o tempo de entrega em empresas brasileiras de médio porte. O estudo, publicado na *Revista Brasileira de Gestão de Projetos*, acompanhou 240 organizações ao longo de dois anos.

**Depois:**
> [⚠️ VERIFICAR FONTE] Segundo Almeida (2019, p. 84), a adoção de metodologias ágeis reduziu em 37% o tempo de entrega em empresas brasileiras de médio porte.
>
> Nota ao usuário: a referência Almeida (2019) e o periódico citado não foram confirmados. Se a fonte não existir, retirar também o número de 37%, que depende só dela.

**Evitar:**
- Reescrever a citação trocando o nome do autor ou o ano por outro que "soe mais certo"
- "Melhorar" a referência completando periódico, página ou DOI ausentes
- Converter a citação falsa em atribuição vaga ("segundo pesquisas") para disfarçar o problema

**Sinais:**
- referência completa em texto que não cita fonte em nenhum outro lugar
- ano, volume e página impecáveis com conteúdo genérico
- periódico plausível, mas com termos genéricos ("Revista Brasileira de Gestão de X")
- número preciso (37%, 2,4x, 240 organizações) apoiado em uma única fonte não verificável

**Correção:**
- **Não conserte.** Marque para verificação do usuário e mantenha o texto.
- Se a afirmação depende só daquela fonte, sinalize que ela sai junto se a fonte não se confirmar.
- Sem como checar, diga que não houve verificação. Nunca apresente ausência de checagem como checagem.
- Registre sempre no relatório, inclusive em `modo_direto`: este padrão é exceção à preservação silenciosa.
- Em texto novo, nunca invente dado, estudo, estatística, referência nem citação. Parafraseie com atribuição ou omita.
- Em texto novo, nunca crie número aproximado. Use "cerca de" ou "aproximadamente" somente se o número da fonte já for aproximado.

## Parte B: tom

### B1. Tom servil

`tom_servil`

**Gatilhos:** "Ótima pergunta!", "Com certeza!", "Excelente observação!", "Espero ter ajudado!", "Fico feliz em ajudar!", "Obrigado por compartilhar!"

**Problema:** elogio genérico ao interlocutor antes da resposta.

**Antes:**
> Ótima pergunta! O deploy contínuo com GitHub Actions é realmente uma abordagem fascinante. Com certeza posso te ajudar com isso! Vamos lá: primeiro, você precisa configurar o fluxo de trabalho em YAML...

**Depois:**
> Para configurar deploy contínuo com GitHub Actions, comece pelo fluxo de trabalho em YAML.

**Evitar:**
- "Ótima pergunta!" / "Excelente ponto!"
- "Com certeza!" / "Absolutamente!"
- "Espero ter ajudado!" / "Fico feliz em contribuir!"

### B2. Avisos sobre limite de conhecimento

`tom_aviso_limite`

**Gatilhos:** "Até onde sei...", "Com base nas informações disponíveis...", "Até minha última atualização...", "Não posso confirmar com certeza, mas...", "De acordo com minhas informações limitadas..."

**Problema:** a fórmula sobre "última atualização" expõe a natureza de máquina. O defeito está na fórmula, não na cautela. Preserve incerteza, limitação temporal e necessidade de confirmação que fazem parte do conteúdo.

**Antes:**
> Até onde sei, o Next.js 15 introduziu Server Actions como recurso estável. No entanto, informações mais recentes podem ter alterado esse cenário. Com base nas informações disponíveis até minha última atualização, a recomendação é usar App Router.

**Depois:**
> As informações disponíveis indicam que o Next.js 15 tornou Server Actions estável e recomendam o App Router. Isso pode ter mudado; confirme antes de aplicar.

**Correção segura:** retire a autorreferência do assistente. Não transforme hipótese em fato, recomendação em obrigação nem informação possivelmente desatualizada em certeza atual.

**Evitar:**
- "Até minha última atualização..."
- "Com base nas informações disponíveis..."
- "Não tenho informações suficientes para afirmar com certeza, mas..."

### B3. Comunicação colaborativa residual

`tom_colaborativo_residual`

**Gatilhos:** "Aqui está um exemplo...", "Posso te ajudar com...", "Vou te mostrar como...", "Segue abaixo...", "Fique à vontade para perguntar mais!"

**Problema:** vestígio de interação assistente-usuário. Parece resposta de suporte, não texto autoral.

**Antes:**
> Aqui está um exemplo de como implementar autenticação com JWT no Express. Vou te mostrar passo a passo como configurar o middleware. Fique à vontade para adaptar conforme suas necessidades!

**Depois:**
> A seguir, a configuração passo a passo do middleware de autenticação com JWT no Express.

**Evitar:**
- "Aqui está um..." / "Segue abaixo..."
- "Posso te ajudar com..." / "Vou te mostrar..."
- "Fique à vontade para..." / "Não hesite em perguntar!"

### B4. Cautela excessiva e gangorra de ressalvas

`tom_cautela_excessiva`

**Gatilhos:** "Pode-se argumentar que...", "É possível que...", "Talvez seja o caso de...", "Alguns especialistas sugerem...", "Aparentemente...", "De certa forma..."

**Problema:** qualificadores acumulados escondem a proposição principal. Na gangorra, a frase afirma e neutraliza com contraponto de peso igual. Remova só a redundância. Não aumente a certeza, não apague exceções e não converta atribuição vaga em opinião do autor.

**Antes:**
> Pode-se argumentar que microsserviços nem sempre são a melhor escolha para startups em estágio inicial. Alguns especialistas sugerem que, em determinados contextos, uma arquitetura monolítica pode ser potencialmente mais adequada para equipes menores.

**Depois:**
> Há o argumento de que microsserviços nem sempre são a melhor escolha para startups em estágio inicial. Alguns especialistas sugerem que, em certos contextos, uma arquitetura monolítica pode ser mais adequada para equipes menores.

**Correção segura:** mantenha verbos modais como "pode" e "parece" quando expressam incerteza real. Se a atribuição não estiver identificada, sinalize a lacuna em vez de assumir a afirmação como própria.

**Regra por modo:**
- Em reescrita, mantenha a modalidade da fonte. Nunca tome posição que o autor não tomou.
- Em `modo_criacao`, escolha um lado e declare-o com clareza, somente se o material do usuário sustentar a posição.
- Em `modo_criacao`, use qualificador só para incerteza real, nunca por hábito.
- Em `modo_criacao`, reconheça o contraponto em no máximo 1 frase, sem peso igual.

**Evitar:**
- "Pode-se argumentar que..." / "É possível que..."
- "Em determinados contextos..." / "Potencialmente..."
- "Alguns especialistas sugerem..." / "De certa forma..."

### B5. Conclusões genéricas positivas e tom de animador corporativo

`tom_conclusao_generica`

Veja também A4, A6 e, em padroes-composicao.md, [Conclusão sinalizada](padroes-composicao.md#conclusão-sinalizada) e [Apesar dos desafios](padroes-composicao.md#apesar-dos-desafios).

**Gatilhos:** "O futuro é promissor", "Tempos empolgantes", "As possibilidades são infinitas", "O potencial é ilimitado", "Estamos apenas no começo", "O melhor ainda está por vir"

**Problema:** encerramento vazio que repete otimismo sem desenvolver o argumento. O texto pode terminar quando o conteúdo termina. Não acrescente posição, provocação nem previsão.

**Antes:**
> O futuro da inteligência artificial no marketing digital é promissor. Estamos vivendo tempos empolgantes, e as possibilidades são verdadeiramente infinitas para profissionais que souberem se adaptar a essa nova realidade.

**Depois:**
> A inteligência artificial pode ampliar as possibilidades no marketing digital para profissionais que se adaptarem. O texto vê esse futuro com otimismo.

**Evitar:**
- "O futuro é promissor" / "Tempos empolgantes nos aguardam"
- "As possibilidades são infinitas" / "O potencial é ilimitado"
- "Estamos apenas no começo dessa jornada"

**Tom de animador corporativo (torcida, palestra motivacional):**
- Proíba esse tom em qualquer texto.
- Em `modo_criacao`, escreva com a experiência do material do usuário, inclusive as partes frustrantes.
- Nunca invente atrito nem vivência para evitar o tom de torcida.

### B6. Frases de enchimento

`tom_enchimento`

Técnica canônica: [padroes-linguagem-ptbr.md](padroes-linguagem-ptbr.md), B4.

**Gatilhos:** "É importante destacar que", "Vale ressaltar que", "Cabe mencionar que", "Convém observar que", "Não se pode ignorar o fato de que", "É fundamental compreender que"

**Problema:** muletas sem informação, usadas antes do ponto. Remova a chamada de atenção e preserve a proposição. Não acrescente justificativa, exemplo nem grau de certeza.

**Antes:**
> É importante destacar que o uso de TypeScript em projetos React tem crescido significativamente. Vale ressaltar que essa tendência reflete a busca por maior segurança de tipos. Cabe mencionar que empresas como Vercel e Stripe já adotaram TypeScript como padrão.

**Depois:**
> O uso de TypeScript em projetos React tem crescido significativamente, e essa tendência reflete a busca por mais segurança de tipos. Vercel e Stripe já adotaram TypeScript como padrão.

**Evitar:**
- "É importante destacar que" / "Vale ressaltar que"
- "Cabe mencionar que" / "Convém observar que"
- "Não se pode ignorar o fato de que" / "É fundamental compreender que"

### B7. Falso suspense ("Eis a questão")

`tom_falso_suspense`

Veja [Dois-pontos](padroes-estilo.md#dois-pontos).

**Gatilhos:** "Eis a questão:", "O ponto central é:", "Mas aqui está o detalhe:", "A grande sacada é:", "O plot twist é:", "E aqui mora o perigo:"

**Problema:** promete revelação dramática antes de um ponto banal e entrega obviedade. Não anuncie que vai dizer algo interessante; diga.

**Antes:**
> Muitas startups investem em growth hacking sem ter product-market fit. Elas contratam profissionais de growth, gastam com anúncios e otimizam funis. Mas eis a questão: sem um produto que as pessoas realmente querem, nenhuma tática de crescimento vai funcionar.

**Depois:**
> Muitas startups investem em growth hacking antes de ter product-market fit: contratam profissionais de growth, gastam com anúncios e otimizam funis. Sem um produto que as pessoas realmente queiram, nenhuma dessas táticas vai funcionar.

**Evitar:**
- "Eis a questão:" / "Eis o ponto:"
- "Mas aqui está o detalhe:" / "A grande sacada é:"
- "E aqui mora o perigo:" / "O plot twist é:"

### B8. Vulnerabilidade falsa e abertura "Como [cargo], eu..."

`tom_vulnerabilidade_falsa`

**Gatilhos:** "Sendo honesto aqui...", "Confesso que...", "Vou ser vulnerável:", "Não vou mentir:", "Se eu for sincero...", "Admito que..."

**Problema:** autoconsciência performática anuncia a vulnerabilidade antes do conteúdo. Remova o ritual. Não dramatize o relato nem invente episódio, consequência ou aprendizado.

**Antes:**
> Confesso que, como desenvolvedor, nem sempre segui boas práticas. Sendo honesto aqui: houve momentos em que priorizei velocidade sobre qualidade. E sim, admito que isso me ensinou lições valiosas sobre a importância do código limpo.

**Depois:**
> Como desenvolvedor, nem sempre segui boas práticas: houve momentos em que priorizei velocidade sobre qualidade. Isso me ensinou a importância do código limpo.

**Variação por perfil:**
- Mantenha a primeira pessoa somente porque ela existe no original.
- Perfil formal: "Em alguns momentos, priorizei..." basta.
- Perfil informal: a oralidade pode aumentar; os acontecimentos, não.

**Abertura com cargo:**
- Gatilhos: "Como [cargo], eu...", "Na qualidade de [cargo]...". Pessoas reais dizem a coisa sem anunciar credencial.
- Em `modo_criacao`, não abra com credencial.
- Em reescrita, mova a credencial para fora da abertura sem apagá-la (TRAVA FACTUAL).
- O "Depois" acima mantém "Como desenvolvedor" porque modela só a remoção do ritual.

**Evitar:**
- "Confesso que..." / "Sendo honesto aqui..."
- "Vou ser vulnerável:" / "Não vou mentir:"
- "Admito que isso me ensinou lições valiosas"

### B9. "A verdade é simples"

`tom_verdade_simples`

**Gatilhos:** "A verdade é simples:", "A realidade é mais simples do que parece", "No fundo, tudo se resume a...", "A resposta é surpreendentemente direta:", "Na prática, é menos complicado do que parece"

**Problema:** declara obviedade sem provar e finge simplificar algo complexo. Exponha direto a proposição já presente. Não crie demonstração, recomendação nem opinião para convencer mais.

**Antes:**
> Muitos fundadores se perdem em métodos de priorização complexos, matrizes RICE e metodologias ágeis elaboradas. Mas a verdade é simples: o que importa é conversar com seus usuários e construir o que eles precisam.

**Depois:**
> Muitos fundadores se perdem em métodos de priorização, matrizes RICE e metodologias ágeis. O ponto defendido é conversar com os usuários e construir o que eles precisam.

**Evitar:**
- "A verdade é simples:" / "A realidade é mais simples do que parece"
- "No fundo, tudo se resume a..." / "A resposta é surpreendentemente direta:"
- "É menos complicado do que você imagina"

### B10. Inflação grandiosa de importância

`tom_inflacao_grandiosa`

Veja também A1.

**Gatilhos:** "Isso vai redefinir fundamentalmente...", "Uma mudança de paradigma", "Revolucionário", "Transformar completamente", "O jogo mudou para sempre", "Nunca mais será o mesmo"

**Problema:** expressões dramáticas redundantes dão importância máxima a tudo. Simplifique a formulação. Não enfraqueça a tese, não troque previsão por dúvida e não insira contraponto que o autor não apresentou.

**Antes:**
> O surgimento de agentes de IA autônomos representa uma mudança de paradigma que vai redefinir fundamentalmente a forma como desenvolvemos software. Estamos testemunhando uma revolução que transformará completamente a indústria de tecnologia como a conhecemos.

**Depois:**
> Agentes autônomos de inteligência artificial vão mudar profundamente o desenvolvimento de software e a indústria de tecnologia.

**Evitar:**
- "Mudança de paradigma" / "Redefinir fundamentalmente"
- "Revolução" / "Transformar completamente"
- "O jogo mudou para sempre" / "Nunca mais será o mesmo"

### B11. Anúncio de explicação ("Vamos analisar")

`tom_anuncio_explicacao`

**Gatilhos:** "Vamos analisar:", "Vamos destrinchar:", "Vamos entender passo a passo:", "Vamos explorar cada aspecto:", "Vamos mergulhar nesse assunto:", "Quebrando em partes:"

**Problema:** voz pedagógica condescendente, que guia o leitor quando o contexto pede exposição direta. Remova o anúncio e comece pelo conteúdo que já existe. Se o "Antes" não trouxer a explicação, não a complete.

**Antes:**
> Vamos analisar os três pilares de uma estratégia de conteúdo eficaz. Primeiro, vamos explorar a pesquisa de palavras-chave. Em seguida, vamos mergulhar na criação de grupos temáticos. Por fim, vamos entender como medir resultados.

**Depois:**
> Uma estratégia de conteúdo eficaz reúne três pilares: pesquisa de palavras-chave, criação de grupos temáticos e medição de resultados.

**Evitar:**
- "Vamos analisar:" / "Vamos destrinchar:"
- "Vamos explorar cada aspecto:" / "Vamos mergulhar nesse assunto:"
- "Vamos entender passo a passo:" / "Quebrando em partes:"

### B12. Rótulos conceituais inventados

`tom_rotulo_inventado`

**Gatilhos:** "o paradoxo da [X]", "a armadilha da [X]", "o deficit de [X]", "a falácia do [X]", "o efeito [X]", "a síndrome de [X]"

**Problema:** termo composto inventado e apresentado como conceito estabelecido ("o paradoxo da supervisão", "a armadilha da aceleração"). Nomeie o fenômeno com cautela ou reconheça que o autor cunha o termo.

**Antes:**
> Muitas empresas caem no que podemos chamar de "paradoxo da automação" — quanto mais automatizam, mais dependem de intervenção humana para lidar com os casos excepcionais. Esse "déficit de supervisão escalável" é o verdadeiro gargalo da transformação digital.

**Depois:**
> Quanto mais essas empresas automatizam, mais dependem de intervenção humana nos casos excepcionais. O texto apresenta essa dificuldade de supervisão como gargalo da transformação digital.

**Evitar:**
- "O paradoxo da [X]" / "A armadilha da [X]"
- "O deficit de [X]" / "A falácia do [X]"
- "O que podemos chamar de..." (seguido de termo inventado)

### B13. "Imagine um mundo onde..." e marcador de hipótese

`tom_imagine_mundo`

**Gatilhos:** "Imagine um mundo onde...", "Imagine se...", "Pense num cenário em que...", "E se eu te dissesse que...", "Visualize um futuro onde...", "Feche os olhos e imagine..."

**Problema:** abertura futurista clichê. Exponha a hipótese direto. Não adicione produtos atuais, dados nem limitações ausentes do texto de origem.

**Antes:**
> Imagine um mundo onde todo desenvolvedor tem um assistente de IA que entende perfeitamente o contexto da sua base de código. Imagine se cada pull request fosse revisada instantaneamente com retorno preciso e acionável. Esse mundo não está tão distante quanto você pensa.

**Depois:**
> Um assistente de inteligência artificial que entenda todo o contexto do código e revise cada pull request imediatamente, com retorno preciso, ainda é uma possibilidade futura. O texto sustenta que ela pode estar próxima.

**Evitar:**
- "Imagine um mundo onde..." / "Imagine se..."
- "E se eu te dissesse que..." / "Visualize um futuro onde..."
- "Esse mundo não está tão distante" / "O futuro já chegou"

**Marcador de hipótese:**
- Marque hipótese com "Suponha que" ou "Por hipótese".
- Nunca abra com "Imagine um mundo onde" nem com "Imagine se".
- Nunca apresente hipótese como fato. Nunca invente anedota. Prefira vagueza honesta a especificidade fabricada.
- A amostra "Imagine que você pediu um delivery" do perfil Didático permanece válida ([perfis-voz.md](perfis-voz.md)).

### B14. Máxima de camiseta

`tom_maxima_camiseta`

**Gatilhos:** "X é a linguagem de Y", "X é a moeda de Y", "X é a arquitetura de Y", "X não é ferramenta, é espelho", "X vira uma armadilha", "no fim das contas, tudo é X"

**Problema:** afirmação comum vira aforismo que informa menos que a versão direta. O aforismo apaga o sujeito, o contexto e a condição em que a afirmação vale.

**Antes:**
> Simetria é a linguagem da confiança. Eficiência vira armadilha quando o time esquece a camada humana.

**Depois:**
> Layout simétrico costuma parecer mais previsível para o usuário. Times podem otimizar demais o fluxo e perder de vista como as pessoas usam o produto.

**Evitar:**
- "Dados são o novo petróleo" e variações de "X é o novo Y"
- "Cultura come estratégia no café da manhã" reciclado para qualquer par de substantivos
- "Não é sobre X, é sobre Y" no fecho de parágrafo
- Substantivo abstrato como sujeito de verbo de ação ("a confiança constrói", "a inovação exige")

**Sinais:**
- frase que funcionaria igual com outros dois substantivos no lugar
- sem sujeito concreto, prazo, condição ou exceção
- isolada no fim de parágrafo ou de seção, como fecho
- sua retirada não muda o que o texto informa

**Correção:**
- Pergunte "quem faz o quê, em que condição?" e escreva a resposta no lugar do aforismo.
- Recupere a modalidade que a máxima apagou. A afirmação real quase sempre é "costuma", "em geral" ou "quando X", não uma lei.
- Se a máxima é do autor e o perfil de voz é autoral (Crônica, Post de rede social), preserve-a. Nesse registro o aforismo é escolha estilística, não vício. Veja o Passo 6 de [SKILL.md](../SKILL.md).
- Não troque uma máxima por outra mais sóbria. Troque pela afirmação específica.
