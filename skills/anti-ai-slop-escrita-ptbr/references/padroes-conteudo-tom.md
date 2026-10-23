> PENDENTE: reescrita ASD-STE100. Conteúdo original copiado sem alteração de `humanizar/references/padroes-conteudo.md, padroes-tom.md`. Ver `HANDOFF.md` na raiz do repositório.

# Padrões de Conteúdo

Padrões onde a IA infla importância, fabrica autoridade ou encerra textos com fórmulas previsíveis. São fáceis de detectar porque soam como comunicado de assessoria de imprensa — ninguém fala assim.

> **TRAVA FACTUAL neste arquivo:** tratar o texto "Antes" como universo factual fechado. No "Depois", preservar proposições, entidades, números, datas, fontes, causalidade, modalidade e registro. Não preencher lacunas com exemplos, dados, fontes ou experiência pessoal. Quando faltar sustentação, preservar a alegação e apontar a lacuna no relatório; só cortar, qualificar ou corrigir com autorização do usuário.

---

### 1. Ênfase indevida em significância, legado e tendências

**Palavras/expressões gatilho:** representa um marco, é um testemunho de, papel fundamental/crucial/vital, ressalta a importância, reflete uma tendência mais ampla, simbolizando o/a, contribuindo para o/a, preparando o terreno para, moldando o futuro de, cenário em constante evolução, ponto de inflexão, marca indelével, profundamente enraizado, redefine o paradigma

**Problema:** A IA transforma qualquer fato mundano numa revolução. Um CRUD vira "um marco na transformação digital". Um pivô de startup vira "um ponto de inflexão no ecossistema de inovação". Nenhum ser humano escreve assim sobre coisas normais.

**Antes (IA):**
> O Nubank representa um marco fundamental na transformação do cenário financeiro brasileiro, moldando ativamente o futuro das fintechs na América Latina e preparando o terreno para uma nova era de inclusão bancária digital.

**Depois (humano):**
> O Nubank tem papel central na transformação do setor financeiro brasileiro. A empresa influencia o desenvolvimento das fintechs na América Latina e contribui para a inclusão bancária digital.

**Evitar em PT-BR:**
- "representa um marco na evolução de..."
- "moldando o futuro do ecossistema de..."
- "em um cenário em constante transformação"

**Sinais adicionais de detecção:**
- Superlativos absolutos sem quantificação ("maior", "melhor", "sem precedentes", "inédito")
- Verbos de transformação grandiosa ("redefinir", "moldar", "preparar o terreno")
- Texto que descreve qualquer coisa como "ponto de inflexão" sem dizer o que muda depois

**Técnicas avançadas de correção:**
- Converter superlativos em **dados concretos somente quando o dado já estiver na entrada**. Sem dado, preservar a força da avaliação e registrar a falta de sustentação no relatório
- Substituir verbos grandiosos por **verbos de ação já descritos no original**. Se o original não informar a ação, usar formulação direta que preserve a alegação sem criar evento novo
- "Teste do jornalista" — se um repórter leria a frase e perguntaria "como assim?", o termo é vazio

---

### 2. Ênfase forçada em notabilidade e cobertura de mídia

**Palavras/expressões gatilho:** amplamente reconhecido, coberto pelos principais veículos, destaque na mídia especializada, presença ativa nas redes sociais, segundo especialistas do setor, referência no mercado

**Problema:** A IA lista veículos e prêmios como prova de importância, sem dizer o que foi dito ou por que importa. Vira um Lattes turbinado — impressiona no vácuo mas não informa nada.

**Antes (IA):**
> A empresa foi destaque na Exame, Valor Econômico, TechCrunch e Bloomberg. Amplamente reconhecida como referência no mercado de SaaS B2B brasileiro, mantém presença ativa nas redes sociais com mais de 200 mil seguidores.

**Depois (humano):**
> A empresa apareceu na Exame, no Valor Econômico, no TechCrunch e na Bloomberg. É amplamente reconhecida no mercado brasileiro de SaaS B2B e soma mais de 200 mil seguidores nas redes sociais.

**Evitar em PT-BR:**
- "amplamente reconhecido(a) como referência em..."
- "destaque nos principais veículos do setor"
- "mantém presença ativa nas redes com X seguidores"

**Sinais adicionais de detecção:**
- Listagem de veículos sem citação de matéria específica (data, título, link)
- "Presença ativa nas redes" sem métrica (seguidores, engajamento)
- Menção a prêmios ou rankings sem fonte verificável

**Técnicas avançadas de correção:**
- Se a entrada já trouxer fonte, data ou link → preservar e citar esses mesmos elementos, sem completar o que estiver ausente
- Se não houver fonte → preservar a alegação e sua atribuição, apontando a lacuna no relatório; só cortar ou qualificar com autorização
- "Teste de verificabilidade" — se o leitor não pode checar em 30 segundos, a informação é puffery

---

### 3. Análises superficiais com gerúndio/particípio

**Palavras/expressões gatilho:** ressaltando a importância de, demonstrando o compromisso com, refletindo a tendência de, contribuindo para o fortalecimento de, evidenciando o potencial de, impulsionando a inovação, fomentando o crescimento, consolidando sua posição como

**Problema:** A IA gruda frases com gerúndio no final das sentenças pra parecer que está analisando algo, mas não está. É firula sintática — enche linguiça sem adicionar informação. Tipo aquele estagiário que escreve 3 páginas pra dizer "funcionou".

**Antes (IA):**
> A RD Station lançou integração nativa com WhatsApp Business, demonstrando seu compromisso com a inovação no marketing digital brasileiro e consolidando sua posição como líder no segmento, impulsionando a transformação digital das PMEs.

**Depois (humano):**
> A RD Station lançou integração nativa com WhatsApp Business. O lançamento demonstra seu compromisso com a inovação no marketing digital brasileiro, consolida sua posição de liderança no segmento e impulsiona a transformação digital das PMEs.

**Evitar em PT-BR:**
- "demonstrando o compromisso da empresa com..."
- "consolidando sua posição como líder em..."
- "contribuindo para o fortalecimento do ecossistema"

**Sinais adicionais de detecção:**
- Frases que terminam com gerúndio como se fosse conclusão de análise
- Construções "verbo composto + gerúndio" em sequência ("vem demonstrando", "vai estar consolidando")
- Gerúndio usado como adjetivo ("inovando", "transformando", "impulsionando")

**Técnicas avançadas de correção:**
- Converter a oração gerundial em **oração finita** com sujeito claro, preservando a alegação: "demonstrando compromisso" → "o lançamento demonstra o compromisso"
- Se o gerúndio é puramente decorativo, **cortar**: "impulsionando a transformação" → (nada — a frase principal já diz)
- "Teste do podcast" — ler a frase em voz alta; se soa como narração de vídeo institucional, o gerúndio é excessivo

---

### 4. Linguagem promocional e de propaganda

**Palavras/expressões gatilho:** solução inovadora, experiência única, ecossistema robusto, revolucionário, disruptivo, estado da arte, de ponta, excelência, sinergia, empoderar, potencializar, alavancar, impulsionar, viabilizar, transformador, game-changer, seamless (usado em PT)

**Problema:** A IA escreve como copywriter de página de produto. Tudo é "inovador", "revolucionário" e "de ponta". Nenhuma pessoa normal descreve o próprio trabalho assim — soa como pitch deck desesperado pra anjo investidor.

**Antes (IA):**
> A plataforma oferece uma solução inovadora e disruptiva que empodera equipes de produto a potencializarem seus resultados, entregando uma experiência seamless e de estado da arte para alavancar a transformação digital das organizações.

**Depois (humano):**
> A plataforma oferece uma solução inovadora e disruptiva. Ela dá às equipes de produto meios para melhorar seus resultados, oferece uma experiência integrada e de alto nível e apoia a transformação digital das organizações.

**Evitar em PT-BR:**
- "solução inovadora e disruptiva que empodera..."
- "experiência única de ponta/estado da arte"
- "potencializar/alavancar a transformação digital"

**Sinais adicionais de detecção:**
- Combinação de 2+ buzzwords na mesma frase ("solução inovadora e disruptiva de ponta")
- Adjetivos que são autocontraditórios ("seamless mas robusto", "simples mas poderoso")
- Texto que poderia ser usado como copy de qualquer produto sem mudar nada

**Técnicas avançadas de correção:**
- Reduzir adjetivos puramente decorativos sem apagar uma alegação substantiva. Quando a alegação não tiver evidência na entrada, qualificá-la como descrição da empresa ou do texto
- Substituir adjetivos por **dados ou comparações somente quando esses elementos já estiverem na entrada**. Sem evidência, preservar a avaliação e apontar a lacuna no relatório
- "Teste do pitch deck" — se a frase apareceria em qualquer slide de qualquer startup, ela é genérica demais

---

### 5. Atribuições vagas e weasel words

**Palavras/expressões gatilho:** segundo especialistas, de acordo com analistas do setor, estudos apontam que, o mercado reconhece, é amplamente considerado, pesquisas indicam, fontes do setor afirmam, observadores notam que

**Problema:** A IA atribui afirmações a autoridades genéricas que não existem. "Especialistas dizem" — quais? "Estudos apontam" — qual estudo, de que ano, com que metodologia? É a versão corporativa de "meu primo falou".

**Antes (IA):**
> Segundo especialistas do setor, o modelo de negócios da empresa representa uma evolução significativa. Analistas de mercado reconhecem que a abordagem tem potencial para redefinir o segmento de healthtechs no Brasil.

**Depois (humano):**
> Especialistas do setor não identificados consideram o modelo de negócios uma evolução significativa. Analistas também não identificados avaliam que a abordagem pode redefinir o segmento de healthtechs no Brasil.

**Evitar em PT-BR:**
- "segundo especialistas do setor..."
- "analistas de mercado reconhecem que..."
- "estudos/pesquisas apontam/indicam que..."

**Sinais adicionais de detecção:**
- Quantificadores vagos: "muitos especialistas", "diversos estudos", "alguns analistas"
- Referências sem data: "pesquisas recentes mostram..."
- Ausência de fonte quando a afirmação é controversa ou específica

**Técnicas avançadas de correção:**
- Se a fonte já estiver na entrada → preservá-la com os mesmos autor, ano, título e link
- Se a fonte não estiver na entrada → manter a atribuição como não identificada e registrar a lacuna no relatório; só cortar ou qualificar com autorização
- Não converter atribuição vaga em opinião ou experiência pessoal do revisor
- "Teste da fonte" — se você não consegue encontrar a fonte em 2 minutos de busca, a atribuição é weasel

---

### 6. Conclusões formulaicas sobre desafios e perspectivas futuras

**Palavras/expressões gatilho:** apesar dos desafios, não obstante as dificuldades, o futuro é promissor, perspectivas animadoras, em um contexto de constante evolução, seguir crescendo, continuar inovando, trilhar um caminho de sucesso, superar obstáculos, rumo a um futuro, desafios e oportunidades

**Problema:** A IA encerra textos com uma seção "Desafios e Perspectivas" que não diz nada concreto. Primeiro lista problemas genéricos, depois diz que "apesar disso, o futuro é promissor". É o equivalente textual de shrug seguido de thumbs up.

**Antes (IA):**
> Apesar dos desafios inerentes ao mercado brasileiro — como a complexidade tributária e a concorrência acirrada — a startup segue trilhando um caminho de crescimento sustentável. Com perspectivas animadoras e um time comprometido com a inovação, a empresa está bem posicionada para continuar liderando a transformação do setor.

**Depois (humano):**
> A startup enfrenta a complexidade tributária e a concorrência acirrada, mas mantém uma trajetória de crescimento sustentável. Suas perspectivas são animadoras, o time é comprometido com a inovação e a empresa está bem posicionada para continuar liderando a transformação do setor.

**Evitar em PT-BR:**
- "apesar dos desafios, o futuro é promissor"
- "a empresa segue bem posicionada para continuar..."
- "trilhando um caminho de crescimento sustentável"

**Sinais adicionais de detecção:**
- Fórmula "Apesar de X, o futuro é Y" onde X é genérico e Y é otimista
- Uso de "perspectivas animadoras" sem dizer o que anima
- A conclusão poderia ser aplicada a QUALQUER empresa do setor

**Técnicas avançadas de correção:**
- Usar previsão, prazo ou plano somente quando esses elementos já estiverem na entrada. Se faltarem, nomear apenas os desafios existentes e apontar a ausência de evidência no relatório
- Se o original expressar incerteza, preservá-la sem criar cenário, consequência ou plano alternativo
- "Teste do horóscopo" — se a conclusão poderia aparecer no horóscopo de qualquer signo, ela é genérica demais

---

### 7. Fonte inventada (referência específica que não existe)

**Palavras/expressões gatilho:** referência com autor e ano que não bate, DOI que não resolve, ISBN inválido, link quebrado, número de página inventado, citação atribuída a quem nunca a disse

**Problema:** Distinto do padrão 5. Lá a fonte é vaga ("especialistas dizem"); aqui ela é **específica e falsa**. O modelo produz uma referência com todos os elementos de uma citação real — sobrenome, ano, página, periódico — e nada disso existe. É o sinal que a Wikipédia usa para eliminação rápida de artigo gerado por IA, porque é o único vício da lista que fabrica evidência em vez de apenas inflar linguagem.

**Antes (IA):**
> Segundo Almeida (2019, p. 84), a adoção de metodologias ágeis reduziu em 37% o tempo de entrega em empresas brasileiras de médio porte. O estudo, publicado na *Revista Brasileira de Gestão de Projetos*, acompanhou 240 organizações ao longo de dois anos.

**Depois (humano):**
> [⚠️ VERIFICAR FONTE] Segundo Almeida (2019, p. 84), a adoção de metodologias ágeis reduziu em 37% o tempo de entrega em empresas brasileiras de médio porte.
>
> Nota ao usuário: a referência Almeida (2019) e o periódico citado não foram confirmados. Se a fonte não existir, retirar também o número de 37%, que depende só dela.

**Evitar em PT-BR:**
- Reescrever a citação trocando o nome do autor ou o ano por outro que "soe mais certo"
- "Melhorar" a referência completando periódico, página ou DOI ausentes
- Converter a citação falsa em atribuição vaga ("segundo pesquisas") para disfarçar o problema

**Sinais adicionais de detecção:**
- Referência muito completa em texto que não cita fonte em nenhum outro lugar
- Ano, volume e página com formatação impecável e conteúdo genérico
- Periódico com nome plausível mas composto de termos genéricos ("Revista Brasileira de Gestão de X")
- Número preciso (37%, 2,4x, 240 organizações) sustentado por uma única fonte não verificável

**Técnicas avançadas de correção:**
- **Não consertar.** Marcar para verificação do usuário e manter o texto como está
- Se a afirmação depende exclusivamente daquela fonte, sinalizar que ela sai junto caso a fonte não se confirme
- Quando não houver como checar, dizer explicitamente que não houve verificação — nunca apresentar ausência de checagem como checagem
- Este padrão é exceção à regra geral de preservação silenciosa: sempre registrá-lo no relatório, inclusive em `modo_direto`


# Padrões de Tom — Detecção e Correção

Padrões que denunciam tom artificial, servil ou performático em texto PT-BR. Cada padrão inclui gatilhos, exemplos brasileiros (tecnologia, startups, marketing e desenvolvimento) e alternativas editoriais.

> **Preservação obrigatória:** em cada par “Antes/Depois”, o texto “Antes” é a única fonte de fatos, argumento, modalidade e posição autoral. A correção pode cortar muletas, reorganizar e simplificar, mas não pode criar experiência pessoal, número, fonte, causa, opinião ou certeza. Se faltar sustentação, preserve a dúvida ou aponte a lacuna.
>
> **Ajuste ao perfil:** os exemplos “Depois” usam registro neutro. Em perfil formal, preserve qualificações, atribuições e impessoalidade funcional; em perfil informal, use coloquialidade somente quando solicitada ou já presente; em nenhum perfil invente primeira pessoa para produzir “voz”.

---

### 1. Tom servil / bajulador

**Palavras/expressões gatilho:** "Ótima pergunta!", "Com certeza!", "Excelente observação!", "Espero ter ajudado!", "Fico feliz em ajudar!", "Obrigado por compartilhar!"

**Problema:** Elogios genéricos ao interlocutor antes de responder. Ninguém fala assim em texto profissional brasileiro — é marca registrada de chatbot tentando agradar.

**Antes (IA):**
> Ótima pergunta! O deploy contínuo com GitHub Actions é realmente uma abordagem fascinante. Com certeza posso te ajudar com isso! Vamos lá: primeiro, você precisa configurar o fluxo de trabalho em YAML...

**Depois (humano):**
> Para configurar deploy contínuo com GitHub Actions, comece pelo fluxo de trabalho em YAML.

**Evitar em PT-BR:**
- "Ótima pergunta!" / "Excelente ponto!"
- "Com certeza!" / "Absolutamente!"
- "Espero ter ajudado!" / "Fico feliz em contribuir!"

---

### 2. Avisos sobre limite de conhecimento

**Palavras/expressões gatilho:** "Até onde sei...", "Com base nas informações disponíveis...", "Até minha última atualização...", "Não posso confirmar com certeza, mas...", "De acordo com minhas informações limitadas..."

**Problema:** Expõe a natureza de máquina do autor com fórmulas sobre “última atualização”. O defeito está na fórmula, não na cautela: incerteza, limitação temporal e necessidade de confirmação devem ser preservadas quando fazem parte do conteúdo.

**Antes (IA):**
> Até onde sei, o Next.js 15 introduziu Server Actions como recurso estável. No entanto, informações mais recentes podem ter alterado esse cenário. Com base nas informações disponíveis até minha última atualização, a recomendação é usar App Router.

**Depois (humano):**
> As informações disponíveis indicam que o Next.js 15 tornou Server Actions estável e recomendam o App Router. Isso pode ter mudado; confirme antes de aplicar.

**Correção segura:** retirar a autorreferência do assistente sem transformar hipótese em fato, recomendação em obrigação ou informação possivelmente desatualizada em certeza atual.

**Evitar em PT-BR:**
- "Até minha última atualização..."
- "Com base nas informações disponíveis..."
- "Não tenho informações suficientes para afirmar com certeza, mas..."

---

### 3. Comunicação Colaborativa Residual

**Palavras/expressões gatilho:** "Aqui está um exemplo...", "Posso te ajudar com...", "Vou te mostrar como...", "Segue abaixo...", "Fique à vontade para perguntar mais!"

**Problema:** O texto conserva vestígios de interação assistente-usuário. Parece resposta de suporte, não texto autoral. Quando publicado como artigo ou post, denuncia imediatamente a origem.

**Antes (IA):**
> Aqui está um exemplo de como implementar autenticação com JWT no Express. Vou te mostrar passo a passo como configurar o middleware. Fique à vontade para adaptar conforme suas necessidades!

**Depois (humano):**
> A seguir, a configuração passo a passo do middleware de autenticação com JWT no Express.

**Evitar em PT-BR:**
- "Aqui está um..." / "Segue abaixo..."
- "Posso te ajudar com..." / "Vou te mostrar..."
- "Fique à vontade para..." / "Não hesite em perguntar!"

---

### 4. Cautela excessiva

**Palavras/expressões gatilho:** "Pode-se argumentar que...", "É possível que...", "Talvez seja o caso de...", "Alguns especialistas sugerem...", "Aparentemente...", "De certa forma..."

**Problema:** O acúmulo de qualificadores pode esconder a proposição principal. A correção remove apenas redundância; não aumenta a certeza, não apaga exceções e não converte atribuição vaga em opinião do autor.

**Antes (IA):**
> Pode-se argumentar que microsserviços nem sempre são a melhor escolha para startups em estágio inicial. Alguns especialistas sugerem que, em determinados contextos, uma arquitetura monolítica pode ser potencialmente mais adequada para equipes menores.

**Depois (humano):**
> Há o argumento de que microsserviços nem sempre são a melhor escolha para startups em estágio inicial. Alguns especialistas sugerem que, em certos contextos, uma arquitetura monolítica pode ser mais adequada para equipes menores.

**Correção segura:** mantenha verbos modais como “pode” e “parece” quando expressam incerteza real. Se a atribuição não estiver identificada, sinalize a lacuna em vez de assumir a afirmação como própria.

**Evitar em PT-BR:**
- "Pode-se argumentar que..." / "É possível que..."
- "Em determinados contextos..." / "Potencialmente..."
- "Alguns especialistas sugerem..." / "De certa forma..."

---

### 5. Conclusões Genéricas Positivas

**Palavras/expressões gatilho:** "O futuro é promissor", "Tempos empolgantes", "As possibilidades são infinitas", "O potencial é ilimitado", "Estamos apenas no começo", "O melhor ainda está por vir"

**Problema:** Encerramento vazio que repete otimismo sem desenvolver o argumento. A saída pode terminar quando o conteúdo termina; não precisa acrescentar posição, provocação ou previsão.

**Antes (IA):**
> O futuro da inteligência artificial no marketing digital é promissor. Estamos vivendo tempos empolgantes, e as possibilidades são verdadeiramente infinitas para profissionais que souberem se adaptar a essa nova realidade.

**Depois (humano):**
> A inteligência artificial pode ampliar as possibilidades no marketing digital para profissionais que se adaptarem. O texto vê esse futuro com otimismo.

**Evitar em PT-BR:**
- "O futuro é promissor" / "Tempos empolgantes nos aguardam"
- "As possibilidades são infinitas" / "O potencial é ilimitado"
- "Estamos apenas no começo dessa jornada"

---

### 6. Frases de Enchimento

**Palavras/expressões gatilho:** "É importante destacar que", "Vale ressaltar que", "Cabe mencionar que", "Convém observar que", "Não se pode ignorar o fato de que", "É fundamental compreender que"

**Problema:** Adicionam zero informação. São muletas usadas antes de chegar ao ponto. A correção remove a chamada de atenção e preserva a proposição, sem acrescentar justificativa, exemplo ou grau de certeza.

**Antes (IA):**
> É importante destacar que o uso de TypeScript em projetos React tem crescido significativamente. Vale ressaltar que essa tendência reflete a busca por maior segurança de tipos. Cabe mencionar que empresas como Vercel e Stripe já adotaram TypeScript como padrão.

**Depois (humano):**
> O uso de TypeScript em projetos React tem crescido significativamente, e essa tendência reflete a busca por mais segurança de tipos. Vercel e Stripe já adotaram TypeScript como padrão.

**Evitar em PT-BR:**
- "É importante destacar que" / "Vale ressaltar que"
- "Cabe mencionar que" / "Convém observar que"
- "Não se pode ignorar o fato de que" / "É fundamental compreender que"

---

### 7. Falso suspense (“Eis a questão”)

**Palavras/expressões gatilho:** "Eis a questão:", "O ponto central é:", "Mas aqui está o detalhe:", "A grande sacada é:", "O plot twist é:", "E aqui mora o perigo:"

**Problema:** Cria falso suspense antes de um ponto banal. Promete revelação dramática e entrega obviedade. Humanos não anunciam que vão dizer algo interessante — simplesmente dizem.

**Antes (IA):**
> Muitas startups investem em growth hacking sem ter product-market fit. Elas contratam profissionais de growth, gastam com anúncios e otimizam funis. Mas eis a questão: sem um produto que as pessoas realmente querem, nenhuma tática de crescimento vai funcionar.

**Depois (humano):**
> Muitas startups investem em growth hacking antes de ter product-market fit: contratam profissionais de growth, gastam com anúncios e otimizam funis. Sem um produto que as pessoas realmente queiram, nenhuma dessas táticas vai funcionar.

**Evitar em PT-BR:**
- "Eis a questão:" / "Eis o ponto:"
- "Mas aqui está o detalhe:" / "A grande sacada é:"
- "E aqui mora o perigo:" / "O plot twist é:"

---

### 8. Vulnerabilidade Falsa

**Palavras/expressões gatilho:** "Sendo honesto aqui...", "Confesso que...", "Vou ser vulnerável:", "Não vou mentir:", "Se eu for sincero...", "Admito que..."

**Problema:** Autoconsciência performática que anuncia a vulnerabilidade antes de apresentar o conteúdo. Remover esse ritual não autoriza tornar o relato mais dramático nem inventar episódio, consequência ou aprendizado.

**Antes (IA):**
> Confesso que, como desenvolvedor, nem sempre segui boas práticas. Sendo honesto aqui: houve momentos em que priorizei velocidade sobre qualidade. E sim, admito que isso me ensinou lições valiosas sobre a importância do código limpo.

**Depois (humano):**
> Como desenvolvedor, nem sempre segui boas práticas: houve momentos em que priorizei velocidade sobre qualidade. Isso me ensinou a importância do código limpo.

**Variação por perfil:** mantenha a primeira pessoa apenas porque ela existe no original. Em perfil formal, “Em alguns momentos, priorizei...” é suficiente; em perfil informal, a oralidade pode aumentar, mas os acontecimentos não.

**Evitar em PT-BR:**
- "Confesso que..." / "Sendo honesto aqui..."
- "Vou ser vulnerável:" / "Não vou mentir:"
- "Admito que isso me ensinou lições valiosas"

---

### 9. "A Verdade É Simples"

**Palavras/expressões gatilho:** "A verdade é simples:", "A realidade é mais simples do que parece", "No fundo, tudo se resume a...", "A resposta é surpreendentemente direta:", "Na prática, é menos complicado do que parece"

**Problema:** Declara obviedade sem provar. Finge simplificar algo complexo, mas apenas repete a superfície. A correção expõe diretamente a proposição já presente; não cria demonstração, recomendação ou opinião para torná-la mais convincente.

**Antes (IA):**
> Muitos fundadores se perdem em métodos de priorização complexos, matrizes RICE e metodologias ágeis elaboradas. Mas a verdade é simples: o que importa é conversar com seus usuários e construir o que eles precisam.

**Depois (humano):**
> Muitos fundadores se perdem em métodos de priorização, matrizes RICE e metodologias ágeis. O ponto defendido é conversar com os usuários e construir o que eles precisam.

**Evitar em PT-BR:**
- "A verdade é simples:" / "A realidade é mais simples do que parece"
- "No fundo, tudo se resume a..." / "A resposta é surpreendentemente direta:"
- "É menos complicado do que você imagina"

---

### 10. Inflação grandiosa de importância

**Palavras/expressões gatilho:** "Isso vai redefinir fundamentalmente...", "Uma mudança de paradigma", "Revolucionário", "Transformar completamente", "O jogo mudou para sempre", "Nunca mais será o mesmo"

**Problema:** Tudo recebe importância máxima por meio de expressões dramáticas redundantes. A correção simplifica a formulação sem enfraquecer a tese, trocar previsão por dúvida ou inserir contraponto que o autor não apresentou.

**Antes (IA):**
> O surgimento de agentes de IA autônomos representa uma mudança de paradigma que vai redefinir fundamentalmente a forma como desenvolvemos software. Estamos testemunhando uma revolução que transformará completamente a indústria de tecnologia como a conhecemos.

**Depois (humano):**
> Agentes autônomos de inteligência artificial vão mudar profundamente o desenvolvimento de software e a indústria de tecnologia.

**Evitar em PT-BR:**
- "Mudança de paradigma" / "Redefinir fundamentalmente"
- "Revolução" / "Transformar completamente"
- "O jogo mudou para sempre" / "Nunca mais será o mesmo"

---

### 11. Anúncio de explicação (“Vamos analisar”)

**Palavras/expressões gatilho:** "Vamos analisar:", "Vamos destrinchar:", "Vamos entender passo a passo:", "Vamos explorar cada aspecto:", "Vamos mergulhar nesse assunto:", "Quebrando em partes:"

**Problema:** Voz pedagógica condescendente. Pressupõe que o leitor precisa ser guiado quando o contexto pede exposição direta. Remova o anúncio e comece pelo conteúdo que já existe; se o “Antes” não trouxer a explicação, não a complete.

**Antes (IA):**
> Vamos analisar os três pilares de uma estratégia de conteúdo eficaz. Primeiro, vamos explorar a pesquisa de palavras-chave. Em seguida, vamos mergulhar na criação de grupos temáticos. Por fim, vamos entender como medir resultados.

**Depois (humano):**
> Uma estratégia de conteúdo eficaz reúne três pilares: pesquisa de palavras-chave, criação de grupos temáticos e medição de resultados.

**Evitar em PT-BR:**
- "Vamos analisar:" / "Vamos destrinchar:"
- "Vamos explorar cada aspecto:" / "Vamos mergulhar nesse assunto:"
- "Vamos entender passo a passo:" / "Quebrando em partes:"

---

### 12. Rótulos Conceituais Inventados

**Palavras/expressões gatilho:** "o paradoxo da [X]", "a armadilha da [X]", "o deficit de [X]", "a falácia do [X]", "o efeito [X]", "a síndrome de [X]"

**Problema:** Inventar termos compostos e apresentá-los como conceitos estabelecidos. IA cria rótulos pseudo-acadêmicos para parecer profunda ("o paradoxo da supervisão", "a armadilha da aceleração"). Humanos nomeiam fenômenos com cautela — ou reconhecem que estão cunhando um termo.

**Antes (IA):**
> Muitas empresas caem no que podemos chamar de "paradoxo da automação" — quanto mais automatizam, mais dependem de intervenção humana para lidar com os casos excepcionais. Esse "déficit de supervisão escalável" é o verdadeiro gargalo da transformação digital.

**Depois (humano):**
> Quanto mais essas empresas automatizam, mais dependem de intervenção humana nos casos excepcionais. O texto apresenta essa dificuldade de supervisão como gargalo da transformação digital.

**Evitar em PT-BR:**
- "O paradoxo da [X]" / "A armadilha da [X]"
- "O deficit de [X]" / "A falácia do [X]"
- "O que podemos chamar de..." (seguido de termo inventado)

---

### 13. "Imagine um Mundo Onde..."

**Palavras/expressões gatilho:** "Imagine um mundo onde...", "Imagine se...", "Pense num cenário em que...", "E se eu te dissesse que...", "Visualize um futuro onde...", "Feche os olhos e imagine..."

**Problema:** Convite futurista clichê que serve de abertura genérica. A correção deve expor a hipótese diretamente, sem adicionar produtos atuais, dados ou limitações que não estejam no texto de origem.

**Antes (IA):**
> Imagine um mundo onde todo desenvolvedor tem um assistente de IA que entende perfeitamente o contexto da sua base de código. Imagine se cada pull request fosse revisada instantaneamente com retorno preciso e acionável. Esse mundo não está tão distante quanto você pensa.

**Depois (humano):**
> Um assistente de inteligência artificial que entenda todo o contexto do código e revise cada pull request imediatamente, com retorno preciso, ainda é uma possibilidade futura. O texto sustenta que ela pode estar próxima.

**Evitar em PT-BR:**
- "Imagine um mundo onde..." / "Imagine se..."
- "E se eu te dissesse que..." / "Visualize um futuro onde..."
- "Esse mundo não está tão distante" / "O futuro já chegou"

---

### 14. Máxima de camiseta

**Palavras/expressões gatilho:** "X é a linguagem de Y", "X é a moeda de Y", "X é a arquitetura de Y", "X não é ferramenta, é espelho", "X vira uma armadilha", "no fim das contas, tudo é X"

**Problema:** Uma afirmação comum é convertida em frase de efeito com cara de aforismo. A estrutura promete profundidade e entrega menos informação que a versão direta — o aforismo apaga o sujeito, o contexto e a condição em que a afirmação vale. É o inverso do trabalho de precisão: em vez de nomear o que acontece, produz uma frase estampável.

**Antes (IA):**
> Simetria é a linguagem da confiança. Eficiência vira armadilha quando o time esquece a camada humana.

**Depois (humano):**
> Layout simétrico costuma parecer mais previsível para o usuário. Times podem otimizar demais o fluxo e perder de vista como as pessoas usam o produto.

**Evitar em PT-BR:**
- "Dados são o novo petróleo" e variações de "X é o novo Y"
- "Cultura come estratégia no café da manhã" reciclado para qualquer par de substantivos
- "Não é sobre X, é sobre Y" no fecho de parágrafo
- Substantivo abstrato como sujeito de verbo de ação ("a confiança constrói", "a inovação exige")

**Sinais adicionais de detecção:**
- A frase funcionaria igual com outros dois substantivos no lugar
- Não há sujeito concreto, prazo, condição ou exceção
- Aparece isolada no fim de parágrafo ou de seção, como fecho
- Retirar a frase não muda o que o texto informa

**Técnicas avançadas de correção:**
- Perguntar "quem faz o quê, em que condição?" e escrever a resposta no lugar do aforismo
- Recuperar a modalidade que a máxima apagou: quase sempre a afirmação real é "costuma", "em geral", "quando X", não uma lei
- Se a máxima é do autor e o perfil de voz é autoral (Crônica, Post de Rede Social), preservá-la: neste registro o aforismo é escolha estilística, não vício. Ver a guarda de falso positivo no SKILL.md
- Não substituir uma máxima por outra mais sóbria; substituir pela afirmação específica
