# Padrões de composição

Fonte dos tropos: [tropes.fyi](https://tropes.fyi/directory).
Fonte da ablação semântica: The Register (fev 2026).

## Regras de uso

- Use este arquivo no Passo 3 de [SKILL.md](../SKILL.md) quando a categoria Composição estiver marcada.
- Trate composição como a forma de montar o texto, nunca como o que o texto diz.
- Altere a composição. Nunca altere o conteúdo.
- Aplique a TRAVA FACTUAL de [SKILL.md](../SKILL.md) (seção Proteções obrigatórias).
- Trate o texto "Antes" como universo factual fechado.
- Preserve no "Depois" proposições, entidades, números, datas, fontes, causalidade, modalidade e registro.
- Nunca introduza analogia, exemplo, dado, experiência, opinião ou detalhe ausente da entrada.
- Quando uma lacuna impedir a concretização, mantenha a generalidade.
- Aponte a lacuna no relatório (veja [auditoria-entrega.md](auditoria-entrega.md)).
- Restaure conteúdo apagado somente a partir de uma versão-fonte fornecida pelo usuário.
- Nunca reconstrua conteúdo apagado por inferência.
- Leia "Antes (IA)" como o defeito e "Depois (humano)" como a forma corrigida.
- Use os ids Jev do campo "Id Jev" de cada tropo com [jev_questions.json](../assets/jev_questions.json) e [jev-integration.md](jev-integration.md).
- Observe que "Documentação da versão anterior" e os 3 padrões de ablação semântica não têm id Jev.
- Consulte [palavras-banidas.md](palavras-banidas.md) para o vocabulário banido em PT-BR.

Estrutura de cada padrão:

- Problema: o que marcar no texto.
- Antes (IA) e Depois (humano): um par de exemplo.
- Evitar em PT-BR ou Restaurar: lista literal de formas.
- Sinais de detecção: o que verificar.
- Técnicas de correção: o que fazer.

---

## Tropos de composição

### Resumos fractais

Id Jev: `composicao_resumos_fractais`

**Problema:**
- Marque o texto que anuncia o que vai dizer, diz, e depois resume o que disse.
- Verifique se o ciclo se repete em cada seção, subseção e parágrafo.
- Trate o ciclo como recursão infinita de meta-comentário.

**Antes (IA):**
> Nesta seção, vamos explorar como a inteligência artificial está transformando o setor financeiro. Veremos três aspectos principais: automação de processos, análise preditiva e atendimento ao cliente.
>
> [... 3 parágrafos ...]
>
> Como vimos nesta seção, a inteligência artificial está transformando o setor financeiro por meio da automação de processos, da análise preditiva e do atendimento ao cliente. Na próxima seção, abordaremos os desafios dessa transformação.

**Depois (humano):**
> A inteligência artificial transforma o setor financeiro por meio da automação de processos, da análise preditiva e do atendimento ao cliente. A seção seguinte examina os desafios dessa transformação.

**Evitar em PT-BR:**
- "Nesta seção, veremos..."
- "Como vimos anteriormente..."
- "A seguir, abordaremos..."
- "Conforme mencionado na seção anterior..."
- "Para resumir o que foi discutido..."

**Sinais de detecção:**
- Marque recursividade de meta-nível: cada seção tem introdução → desenvolvimento → mini-conclusão, e cada parágrafo dentro da seção também tem essa estrutura.
- Procure palavras-chave de meta-comentário: "como discutido", "retomando", "para recapitular", "em resumo desta seção".
- Marque conectivos de transição entre subseções que referenciam o próprio texto ("No tópico anterior vimos...").
- Marque seções com a mesma estrutura interna e o mesmo comprimento (regra completa em [Colapso estrutural](#colapso-estrutural)).

**Técnicas de correção:**
- Reescreva eliminando a recursão.
- Escreva UMA conclusão do texto, no final.
- Não coloque mini-conclusões nas subseções.
- Converta meta-comentário em afirmação direta: "Como vimos nesta seção, a IA transforma o setor" → "A IA transforma o setor de três formas".
- Se o texto tem 3+ subseções com mini-conclusões, funda as subseções em um único bloco com fluxo contínuo.
- Não repita a mesma estrutura de seção em todo o texto; varie o comprimento das seções (regra completa em [Colapso estrutural](#colapso-estrutural)).

---

### Metáfora morta

Id Jev: `composicao_metafora_morta`

**Problema:**
- Marque a metáfora encontrada no início e repetida ad nauseam como espinha do texto.
- Exemplo de excesso: "ecossistema" aparece 30 vezes.
- Exemplo de excesso: "jornada" aparece em cada parágrafo.
- Trate a metáfora repetida como ruído, sem poder expressivo.

**Antes (IA):**
> O ecossistema de startups brasileiro está amadurecendo. Nesse ecossistema, os players precisam se adaptar. O ecossistema exige novas competências. Para sobreviver neste ecossistema, empreendedores devem construir redes sólidas. O futuro do ecossistema depende de políticas públicas que fomentem a inovação dentro do próprio ecossistema.

**Depois (humano):**
> O ecossistema de startups brasileiro está amadurecendo. Esse processo exige que seus participantes desenvolvam novas competências e que os empreendedores construam redes sólidas. O futuro do setor também depende de políticas públicas de incentivo à inovação.

**Evitar em PT-BR:**
- Repetir "ecossistema", "jornada", "cenário", "panorama" ou "paisagem" mais de 2x num texto
- Usar a mesma metáfora-base em mais de 3 parágrafos seguidos
- Forçar coerência metafórica artificial ("nessa jornada... o próximo passo da jornada... ao longo da jornada...")

**Sinais de detecção:**
- Conte a repetição da mesma palavra-metafórica: mais de 2 no texto inteiro; mais de 1 por parágrafo.
- Marque metáfora semanticamente vazia no contexto ("ecossistema" para qualquer coisa que tenha mais de duas partes).
- Marque metáfora que não suporta raciocínio: o autor usa "jornada" mas não desenvolve nenhuma etapa da jornada.

**Técnicas de correção:**
- Crie um **mapa metafórico**: liste todas as metáforas usadas.
- Se houver sobreposição semântica (ex: "ecossistema", "cenário", "paisagem" no mesmo texto), escolha UMA e elimine as demais.
- Substitua metáfora genérica por formulação direta baseada nas proposições existentes.
- Use imagem concreta somente se ela já estiver na entrada ou for apresentada, com autorização, como hipótese explícita.
- Quando a metáfora não serve a um argumento real, corte e vá direto ao ponto.

---

### Empilhamento de analogias históricas

Id Jev: `composicao_analogias_historicas`

**Problema:**
- Marque a lista de 5 empresas ou revoluções históricas em sequência para dar "peso" ao argumento.
- Verifique se alguma analogia é desenvolvida o bastante para provar algo.
- Trate a lista sem desenvolvimento como preenchimento, mesmo que pareça erudição.

**Antes (IA):**
> Assim como a revolução industrial transformou a manufatura, como a eletricidade mudou a infraestrutura urbana, como a internet redefiniu a comunicação, como o iPhone revolucionou a computação móvel, e como o Netflix disruputou a mídia — a inteligência artificial generativa está prestes a transformar fundamentalmente o modo como trabalhamos.

**Depois (humano):**
> A revolução industrial transformou a manufatura; a eletricidade, a infraestrutura urbana; a internet, a comunicação; o iPhone, a computação móvel; e a Netflix, a mídia. Da mesma forma, a inteligência artificial generativa está prestes a transformar fundamentalmente o modo como trabalhamos.

**Evitar em PT-BR:**
- "Assim como [empresa/revolução 1], como [empresa/revolução 2], como [empresa/revolução 3]..."
- "Da mesma forma que a revolução industrial..."
- "Se olharmos para a história — do rádio à TV, da TV à internet, da internet ao mobile —"
- Listar mais de 2 analogias históricas sem desenvolver nenhuma

**Sinais de detecção:**
- Marque sequências de 3+ analogias com a mesma estrutura sintática (coordenação com "como" ou "assim como").
- Marque analogias que terminam em conclusão genérica idêntica ("...está transformando fundamentalmente o modo como trabalhamos").
- Marque analogias sem especificidade temporal (não diz quando a revolução industrial aconteceu, quanto durou, qual setor).

**Técnicas de correção:**
- Condense analogias repetitivas sem apagar proposições distintas.
- Descarte apenas a analogia decorativa que não acrescenta conteúdo ao argumento.
- Desenvolva especificidade temporal ou causal somente com dados já presentes na entrada.
- Se a analogia não tiver sustentação, qualifique-a como comparação do autor ou aponte a lacuna no relatório.
- Nunca ancore a analogia com dados externos inventados.

---

### Diluição de ponto único

Id Jev: `composicao_diluicao_ponto`

**Problema:**
- Marque o texto que tem UM argumento e o reformula 10 vezes com conectivos diferentes.
- Exemplo de escala: 4000 palavras para o que caberia em 400.
- Marque parágrafos que dizem a mesma coisa com palavras diferentes.

**Antes (IA):**
> A transformação digital é essencial para a competitividade empresarial. De fato, empresas que não adotarem tecnologias digitais correm o risco de ficar para trás. Nesse sentido, a digitalização dos processos se torna uma prioridade estratégica. Além disso, a modernização tecnológica permite que organizações se adaptem com mais agilidade. Por outro lado, empresas que resistem à mudança digital enfrentam desafios crescentes de eficiência. Diante disso, fica claro que a transformação digital não é mais uma opção — é uma necessidade.

**Depois (humano):**
> A transformação digital é essencial para a competitividade. Empresas que não adotam tecnologias digitais podem perder competitividade e enfrentar problemas de eficiência. Por isso, digitalizar processos e modernizar a tecnologia são necessidades estratégicas para aumentar a agilidade e a capacidade de adaptação.

**Evitar em PT-BR:**
- Parágrafo que começa com "De fato," seguido da repetição da mesma ideia
- "Nesse sentido," introduzindo a mesma ideia de novo
- "Em outras palavras," (literalmente admitindo que vai repetir)
- "Isso significa que..." (reformulação disfarçada)
- Texto com mais de 3 parágrafos onde cada um pode ser resumido pela mesma frase

**Sinais de detecção:**
- Marque parágrafos com a mesma informação expressa em palavras diferentes (sinonímia redundante).
- Marque conectivos de reformulação: "em outras palavras", "ou seja", "isso significa que", "dito de outro modo".
- Marque texto com TTR (Type-Token Ratio) artificialmente baixo: muita repetição lexical com sinônimos.

**Técnicas de correção:**
- Aplique o **algoritmo de compressão**: identifique o núcleo proposicional de cada parágrafo.
- Se dois parágrafos compartilham o mesmo núcleo, funda os dois em um.
- Elimine conectivos de reformulação.
- Aplique a "regra de 3": trate como provavelmente fraco o argumento que precisa de 3 reformulações para ser entendido.

---

### Conclusão sinalizada

Id Jev: `composicao_conclusao_sinalizada`

**Problema:**
- Marque marcadores explícitos que telegrafam "aqui acaba".
- Trate o anúncio de que o texto vai terminar como quebra do impacto do final.

**Antes (IA):**
> Em conclusão, a inteligência artificial generativa representa uma oportunidade transformadora para o mercado brasileiro. Em suma, as empresas que souberem aproveitar esse potencial estarão melhor posicionadas para o futuro. Para finalizar, é importante ressaltar que o equilíbrio entre inovação e responsabilidade será determinante para o sucesso dessa jornada.

**Depois (humano):**
> A inteligência artificial generativa é uma oportunidade transformadora para o mercado brasileiro. As empresas que aproveitarem esse potencial estarão mais bem posicionadas, e o equilíbrio entre inovação e responsabilidade será determinante para o sucesso.

**Evitar em PT-BR:**
- "Em conclusão,"
- "Em suma,"
- "Para finalizar,"
- "Concluindo,"
- "Portanto, podemos afirmar que..."
- "Diante do exposto,"
- "À luz do que foi apresentado,"

**Sinais de detecção:**
- Marque marcadores explícitos de encerramento em sequência ("Em conclusão... Para finalizar...").
- Marque conclusões que apenas repetem o que já foi dito sem acrescentar ideia nova.
- Marque parágrafo final com tom otimista genérico ("o futuro é promissor").

**Técnicas de correção:**
- Escolha o fechamento apenas entre materiais já presentes no texto.
- Escolha entre os 4 tipos de fechamento abaixo.
  1. **Virada reflexiva:** converta uma dúvida já existente em pergunta.
  2. **Detalhe concreto:** reutilize dado já fornecido na entrada.
  3. **Contradição:** preserve limite ou tensão já expresso pelo autor.
  4. **Silêncio:** retire o marcador e simplesmente encerre.
- No Silêncio, deixe o parágrafo terminar abruptamente.
- Não acrescente resumo nem transição a todo parágrafo; às vezes, pare.
- Se a conclusão começa com "Em conclusão", corte as 3 primeiras palavras e verifique se o resto sobrevive.
- Para fechamentos otimistas genéricos e o tom de "cheerleading", veja [padroes-conteudo-tom.md](padroes-conteudo-tom.md) (B5).

---

### Apesar dos desafios

Id Jev: `composicao_apesar_desafios`

**Problema:**
- Marque a fórmula rígida de "acknowledge→dismiss" (reconhecer→descartar).
- Marque o problema reconhecido e descartado de imediato com otimismo vazio.
- Verifique se o "desafio" ameaça a tese; se nunca ameaça, não há tensão real.

**Antes (IA):**
> Apesar dos desafios regulatórios, a adoção de IA no setor de saúde segue em ritmo acelerado. Embora existam preocupações legítimas sobre privacidade de dados, as oportunidades superam amplamente os riscos. Mesmo com as limitações atuais de infraestrutura, o potencial transformador da tecnologia é inegável.

**Depois (humano):**
> A adoção de IA no setor de saúde avança em ritmo acelerado. Há preocupações com a privacidade de dados e limitações de infraestrutura; ainda assim, as oportunidades superam amplamente os riscos, e o potencial transformador da tecnologia é inegável.

**Evitar em PT-BR:**
- "Apesar dos desafios, [coisa positiva]"
- "Embora existam preocupações legítimas, as oportunidades superam..."
- "Mesmo com as limitações, o potencial é..."
- "Não obstante os obstáculos, o caminho é promissor"
- "Reconhecendo os riscos, mas focando nas possibilidades..."

**Sinais de detecção:**
- Marque a estrutura "reconhece → descarta" em 1-2 frases.
- Marque adjetivos que neutralizam o problema: "desafios legítimos", "limitações atuais", "obstáculos naturais".
- Marque o "desafio" que nunca tem consequência concreta e permanece abstrato.

**Técnicas de correção:**
- Explicite custo, risco ou consequência somente quando esses elementos já estiverem na entrada.
- Se não estiverem na entrada, mantenha o desafio nos termos originais e aponte a lacuna no relatório.
- Se o original já expressar uma tensão, **não a descarte**.
- Preserve o dado, a dúvida sobre a fonte e a decisão em aberto.
- Nunca crie nenhum desses elementos.
- Aplique o "teste de consequência": se o desafio não tiver custo, risco ou contrapartida explícita na entrada, não invente um.
- Sem consequência explícita, mantenha a formulação geral ou aponte a lacuna no relatório.

---

### Listicle disfarçado de prosa

Id Jev: `composicao_listicle_disfarçado`

**Problema:**
- Marque a lista numerada que finge ser parágrafo corrido.
- Marque itens que começam com "O primeiro aspecto...", "O segundo ponto...", "O terceiro elemento...".
- Verifique a ausência de fluxo: o texto é enumeração com pontuação de prosa.

**Antes (IA):**
> O primeiro aspecto a considerar é a escalabilidade da solução. O segundo ponto relevante diz respeito à integração com sistemas legados. O terceiro elemento fundamental é a experiência do usuário final. O quarto fator a ser levado em conta é o custo total de propriedade. Por fim, o quinto aspecto envolve a governança de dados.

**Depois (humano):**
> A solução deve ser avaliada por cinco aspectos: escalabilidade, integração com sistemas legados, experiência do usuário, custo total de propriedade e governança de dados.

**Evitar em PT-BR:**
- "O primeiro aspecto..."
- "O segundo ponto..."
- "O terceiro elemento..."
- "O quarto fator..."
- "Por fim, o quinto..."
- Qualquer sequência ordinal disfarçada de argumentação

**Sinais de detecção:**
- Marque sequência ordinal implícita: "Primeiro... Depois... Em seguida... Por fim...".
- Marque frases com estrutura sintática idêntica (mesmo comprimento, mesma ordem de constituintes).
- Marque texto que pode ser reformatado como lista numerada sem perder sentido.

**Técnicas de correção:**
- Se o conteúdo merece lista, **formate como lista real**.
- Se o conteúdo não merece lista, **reorganize como raciocínio causal**: causa → efeito → consequência.
- Nunca crie relação causal que a entrada não expressa.
- Quebre a simetria sintática sem mudar o registro nem acrescentar fragmentos que não estejam no texto.
- Reordene os itens somente quando a nova ordem preservar relações lógicas e ênfase do original.

---

### Eco do título

Id Jev: `composicao_eco_titulo`

**Problema:**
- Marque a frase curta isolada que repete o título logo abaixo dele, antes de o conteúdo começar.
- Verifique se o parágrafo só reafirma o cabeçalho que o leitor acabou de ler.

**Antes (IA):**
> ## Desempenho
>
> Velocidade importa.
>
> Quando a página demora a carregar, o usuário desiste antes da primeira interação.

**Depois (humano):**
> ## Desempenho
>
> Quando a página demora a carregar, o usuário desiste antes da primeira interação.

**Evitar em PT-BR:**
- Parágrafo de uma linha logo após o título que apenas reformula o título
- "A segurança é fundamental." sob o título "## Segurança"
- "Vamos falar sobre X." sob o título "## X"

**Sinais de detecção:**
- Remova a frase e verifique: se o texto sobrevive sem perda, é eco.
- Marque o substantivo do título repetido como sujeito da primeira frase.
- Marque o padrão repetido em todas as seções do documento.

**Técnicas de correção:**
- Corte a frase de eco e comece pela informação.
- Se a frase carrega algo além do título, funda-a com o parágrafo seguinte em vez de deixá-la isolada.
- Não substitua o eco por uma frase de abertura nova.
- Comece a seção direto no conteúdo.

---

### Alternativa falsa rejeitada

Id Jev: `composicao_alternativa_falsa`

**Palavras/expressões gatilho:** uma opção tentadora seria, poderíamos pensar em, uma abordagem óbvia seria, você pode achar que... mas, seria fácil apenas, alguns sugeririam, à primeira vista pode parecer que

**Problema:**
- Marque a opção que ninguém consideraria, descartada em meia frase, sem retorno ao assunto.
- Trate o caso, em geral, como resto de rascunho: o modelo encena uma deliberação que não aconteceu.
- Não confunda com comparação legítima de alternativas.
- Espere comparação legítima como conteúdo de documento de arquitetura, tutorial e texto argumentativo.

**Antes (IA):**
> Os tokens de sessão são rotacionados a cada 24 horas. Uma opção tentadora seria fazer a rotação reiniciando o serviço de autenticação por cron, mas isso derrubaria todas as sessões ativas. A rotação acontece em memória e os clientes renovam sozinhos.

**Depois (humano):**
> Os tokens de sessão são rotacionados a cada 24 horas, em memória, e os clientes renovam sozinhos.

**Evitar em PT-BR:**
- "Uma opção tentadora seria X, mas..." seguido de silêncio sobre X
- "Seria fácil apenas fazer Y, porém..." quando Y nunca esteve em jogo
- Sequência de rejeições curtas e desconexas no mesmo parágrafo

**Sinais de detecção:**
- Marque a alternativa que aparece uma única vez, só para ser descartada.
- Marque a rejeição que ocupa menos espaço do que a opção rejeitada mereceria se fosse real.
- Pergunte de cada frase: que informação nova ela traz?
- Se a resposta for "registra uma edição antiga", é este padrão.

**Técnicas de correção:**
- Remova a opção falsa e mantenha apenas a restrição real que ela escondia.
- Quando várias rejeições se acumulam, reescreva o parágrafo em volta do ponto principal.
- Preserve a alternativa quando o texto nomeia quem a propôs.
- Preserve a alternativa quando ela é retomada depois.
- Preserve a alternativa quando o gênero exige o levantamento de opções.

---

### Documentação da versão anterior

Sem id Jev.

**Problema:**
- Descreva o comportamento atual em documentação, comentário de código e texto de referência.
- Marque a explicação do presente em contraste com um passado que o leitor não conhece.
- Trate esse contraste como transformação de referência em changelog.

**Antes (IA):**
> Esta função foi criada para substituir a abordagem anterior, que percorria todos os itens da lista e custava O(n²) em coleções grandes.

**Depois (humano):**
> Esta função usa um hash map para busca em O(1).

**Evitar em PT-BR:**
- "Diferentemente da versão anterior..."
- "Substitui o antigo método X, que..."
- "Antes era necessário Y; agora basta Z" fora de guia de migração

**Sinais de detecção:**
- Marque o texto que explica o que o sistema **não** faz mais antes de dizer o que ele faz.
- Marque menção a implementação antiga que não aparece em nenhum outro lugar da documentação.
- Marque comentário de código que narra a história do arquivo em vez do estado atual.

**Técnicas de correção:**
- Reescreva a partir do comportamento atual, sem referência ao anterior.
- Preserve o histórico quando o documento **é** sobre mudança: changelog, nota de versão, guia de migração, post-mortem, ADR.
- Não apague o contraste quando ele explica uma decisão que o leitor precisa entender para não repetir o erro.
- Nesse caso, mova o contraste para uma nota separada.

---

## Ablação semântica

Regras de definição:

- Defina ablação semântica como a remoção de informação de alta entropia (os trechos únicos, específicos, surpreendentes).
- Defina a substituição como troca por sequências genéricas de alta probabilidade.
- Identifique a ablação quando a IA "melhora" um texto.
- Trate o resultado como "JPEG de pensamento": parece coerente, mas perdeu a densidade original.
- Preserve o que ainda existe no texto, além de remover padrões ruins.
- Restaure conteúdo apagado somente com uma versão-fonte fornecida pelo usuário.
- Sem versão-fonte, nunca reconstrua por inferência.

---

### Limpeza metafórica

Sem id Jev.

**Problema:**
- Marque metáforas originais, imagens viscerais e comparações inesperadas tratadas como "ruído".
- Marque a troca delas por clichês seguros.
- Trate a troca como metáforas vivas que viram metáforas mortas.
- Verifique o desaparecimento da especificidade sensorial.

**Antes (IA):**
> O mercado de trabalho está passando por uma profunda transformação. As empresas estão navegando em águas turbulentas e buscando se adaptar ao novo cenário. É preciso abraçar a mudança e trilhar novos caminhos para alcançar o sucesso.

**Depois (humano):**
> O mercado de trabalho passa por uma transformação profunda. As empresas enfrentam instabilidade, buscam adaptação e precisam mudar para alcançar o sucesso.

**Restaurar:**
- Metáforas sensoriais (visuais, táteis, sonoras) que já estejam na entrada ou em uma versão-fonte fornecida
- Comparações concretas que já façam parte do material autorizado
- Imagens e reações presentes no original, sem criar desconforto ou surpresa por conta própria
- Especificidade: em vez de "cenário", descrever apenas o que a entrada já informa; se não houver detalhe, usar formulação direta e apontar a lacuna no relatório

**Sinais de detecção:**
- Marque metáforas substituídas por **clichês corporativos** ("ponto de inflexão", "navegar as complexidades").
- Marque perda de especificidade sensorial: texto que antes tinha cor/luz/cheiro e agora tem só conceito.
- Marque metáforas que poderiam ser aplicadas a QUALQUER assunto ("transformação profunda", "novo capítulo").

**Técnicas de correção:**
- Aplique a **escala de concretude**: classifique cada imagem de 1 a 5 (1 = abstrata, 5 = sensorial).
- Se a média do texto for < 2, simplifique a abstração com o material existente.
- Nesse caso, aponte a falta de concretude no relatório.
- Substitua clichês por formulação direta.
- Use referência cultural brasileira apenas se ela já estiver na entrada ou for autorizada como hipótese explícita.
- Aplique o "teste do bar": se a metáfora não funcionaria numa conversa de bar, ela é genérica demais.

---

### Achatamento lexical

Sem id Jev.

**Problema:**
- Marque jargão preciso e terminologia de domínio substituídos por termos genéricos "acessíveis".
- Reconheça o efeito: token de 1-em-10.000 vira token de 1-em-100.
- Verifique a perda de densidade informacional: o texto diz menos com mais palavras.

**Antes (IA):**
> A empresa implementou uma solução de análise de dados que permite monitorar indicadores de desempenho e tomar decisões mais informadas. A ferramenta oferece visualizações intuitivas que ajudam a equipe a entender melhor os resultados.

**Depois (humano):**
> A empresa implementou uma solução de análise de dados para monitorar indicadores de desempenho, apoiar decisões mais informadas e visualizar resultados. As visualizações ajudam a equipe a compreender melhor esses resultados.

**Restaurar:**
- Nomes próprios de ferramentas, frameworks e metodologias que já estejam na entrada ou em uma versão-fonte fornecida
- Métricas e siglas de domínio já presentes no material autorizado
- Verbos técnicos precisos que já estejam na entrada ou em uma versão-fonte fornecida; sem essa base, preservar a ação genérica
- Dados concretos já fornecidos: preservar números, porcentagens e intervalos temporais; se estiverem ausentes, não criá-los

**Sinais de detecção:**
- Marque substituição de jargão técnico por sinônimos genéricos ("ORM" → "ferramenta de mapeamento objeto-relacional" → "solução de banco de dados").
- Marque perda de siglas do domínio (substitui "SaaS" por "software como serviço", depois por "plataforma digital").
- Marque texto que soa como tradução de material introdutório para público leigo, mesmo quando o público é técnico.

**Técnicas de correção:**
- Aplique o **mapeamento de domínio**: identifique o campo (dev, marketing, jurídico).
- Preserve o vocabulário técnico existente.
- Nunca infira ferramenta, métrica ou sigla ausente.
- Se o texto generalizou demais, reintroduza sigla ou termo somente a partir de uma versão-fonte fornecida.
- Sem versão-fonte, aponte a perda de precisão no relatório.
- Aplique o "teste de precisão": se um especialista do domínio lê e diz "isso tá vago", o texto perdeu densidade.

---

### Colapso estrutural

Sem id Jev.

**Problema:**
- Marque raciocínio complexo, não linear e cheio de voltas forçado no molde previsível de baixa perplexidade: introdução → 3 pontos → conclusão.
- Marque digressões eliminadas.
- Marque contradições "resolvidas".
- Marque nuance transformada em item de lista.

**Antes (IA):**
> A adoção de metodologias ágeis no Brasil apresenta três benefícios principais. Em primeiro lugar, aumenta a produtividade das equipes. Em segundo lugar, melhora a qualidade das entregas. Em terceiro lugar, promove uma cultura de melhoria contínua. Dessa forma, as empresas que adotam práticas ágeis tendem a obter melhores resultados.

**Depois (humano):**
> No Brasil, a adoção de metodologias ágeis aumenta a produtividade das equipes, melhora a qualidade das entregas e promove uma cultura de melhoria contínua. Por isso, as empresas que adotam essas práticas tendem a obter resultados melhores.

**Restaurar:**
- Digressões produtivas que já estejam na entrada ou em uma versão-fonte fornecida
- Contradições internas efetivamente expressas pelo autor
- Qualificações, exceções e dúvidas presentes no material autorizado
- Perguntas sem resposta somente quando preservarem uma dúvida já existente
- Estrutura que surpreende: começar por contra-argumento ou detalhe já existente, sem alterar a ênfase do autor

**Sinais de detecção:**
- Marque estrutura perfeitamente simétrica: parágrafos com 3-4 frases cada, todos com a mesma ordem (tópico → desenvolvimento → conclusão).
- Marque ausência de digressões, parênteses ou tangentes.
- Marque texto que parece ter sido gerado por outline rígido sem desvios.
- Marque parágrafos com a mesma forma em série: tópico → explicação → exemplo → transição.
- Marque seções com estrutura paralela e comprimento parecido.

**Técnicas de correção:**
- Reposicione uma tangente já existente sem criar comentário ou argumento novo.
- Use parênteses apenas para material lateral já presente no texto.
- Quebre a simetria por divisão ou combinação de frases existentes, preservando o registro.
- Varie a estrutura somente quando isso não alterar ênfase, modalidade ou voz do original.

**Forma dos parágrafos e das seções:**
- Proíba parágrafos com a mesma estrutura em sequência.
- Quebre a sequência tópico → explicação → exemplo → transição.
- Deixe alguns parágrafos terem uma só frase.
- Deixe alguns parágrafos terminarem sem transição e sem resumo.
- Em [modo_criacao](../SKILL.md#escrita-do-zero-modo_criacao), abra alguns parágrafos com pergunta e outros com afirmação direta.
- Em reescrita, varie a forma só por divisão ou combinação de frases existentes.
- Em reescrita, nunca transforme afirmação em pergunta quando isso mudar a modalidade do original.
- Proíba estrutura paralela entre seções.
- Dê tratamento diferente a pontos diferentes.
- Varie o comprimento das seções.
- Em reescrita, varie o comprimento só por fusão ou corte de meta-comentário; nunca acrescente conteúdo.
- Para transições mecânicas entre parágrafos, veja [padroes-linguagem-ptbr.md](padroes-linguagem-ptbr.md) (B9).
