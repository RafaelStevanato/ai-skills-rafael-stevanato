# Perfis de voz

## Regras de uso

- Trate cada exemplo como amostra fictícia de estilo.
- Nunca use um exemplo como autorização para acrescentar fatos ao texto-fonte.
- Aplique a TRAVA FACTUAL de [SKILL.md](../SKILL.md) em todo perfil.
- Aplique estes perfis a texto em PT-BR.
- Siga [modo-ingles.md](modo-ingles.md) para texto em inglês.
- Proíba em texto novo qualquer item de [palavras-banidas.md](palavras-banidas.md).
- Em texto existente do autor, aplique a guarda de acúmulo do Passo 6 de [SKILL.md](../SKILL.md).
- Em reescrita, mantenha a modalidade da fonte.
- Assuma posição própria somente em `modo_criacao`, e somente quando o material do usuário a sustenta.
- Os exemplos verbatim mantêm travessões de aparte como dado.
- Nunca copie esses travessões para texto novo.
- Use os exemplos Antes/Depois como modelo de forma, nunca de conteúdo.

### Escolha do perfil

- Detecte o perfil pelo conteúdo com a tabela do Passo 1 de [SKILL.md](../SKILL.md).
- Respeite o perfil explícito. Ele define os limites do gênero.
- Nunca substitua o perfil explícito automaticamente.
- Dentro dos limites do perfil, deixe a amostra fornecida controlar as escolhas finas de estilo.
- Sem perfil explícito, dê à amostra prioridade sobre a detecção.
- Sem perfil nem amostra, use o perfil detectado.
- Sem sinal claro, use voz neutra.
- Em conflito material, pergunte ao usuário nos modos completo e revisão.
- No `modo_direto`, escolha o registro mais próximo do texto-fonte.
- No `modo_direto`, aja de modo conservador e registre a ambiguidade.
- Em texto com múltiplos registros, mantenha um perfil principal.
- Ajuste apenas os trechos que pertencem a outro gênero.

### Escopo por perfil

| Regra geral | Exceção por perfil |
|---|---|
| Proibição de parataxe (frases soltas em série) | Vale para voz neutra e prosa autoral, salvo se a amostra de voz usar fragmentos. Português simplificado, Enxuto, Assertivo e Resumo ficam isentos |
| Variação de comprimento de frase | O limite de 25 palavras do Português simplificado prevalece |
| No máximo 5 bullets seguidos | Vale para perfis autorais e voz neutra. Português simplificado e Resumo ficam isentos |
| Fragmentos dramáticos | Use somente em perfil autoral cuja voz os sustenta. Respeite o limite de [padroes-estilo.md](padroes-estilo.md) |
| Palavra menos óbvia | Evite o clichê de maior probabilidade. Em Português simplificado, a regra R4 (palavras comuns) prevalece. Nunca alterne sinônimos |
| Emoji | Resumo fica isento, porque seus emojis são notação funcional |
| Cabeçalhos markdown | Proibidos em texto social, e-mail e casual. Negrito de lead-in é permitido nos perfis de consumo rápido |

## Calibração de voz e amostra do autor

Ao escrever para uma pessoa específica, espelhe a voz DELA. Responda estas 4 perguntas:

- A pessoa xinga? Usa gíria? Escreve longo ou curto?
- Qual humor ela usa: seco, sarcástico, autoirônico ou absurdo?
- O que essa pessoa NUNCA diria?
- Qual é a plataforma? Carta de apresentação ≠ tweet ≠ LinkedIn ≠ DM.

Quando o usuário fornecer amostra de voz, espelhe 5 traços:

- Comprimento de frases.
- Nível vocabular.
- Início de parágrafos.
- Pontuação.
- Uso de estrangeirismos.

Nunca copie fatos, opiniões, personagens ou experiências da amostra para o texto reescrito.

Trate entrada com marca forte de autoria como amostra do autor. Veja o Passo 6 de [SKILL.md](../SKILL.md).

### Voz neutra (padrão)

- Use voz neutra quando não houver perfil, amostra nem sinal claro.
- Preserve o registro original.
- Remova apenas padrões mecânicos.
- Nunca force informalidade.
- Evite primeira pessoa, opinião, humor e mudança de registro.
- Não explique demais.
- Confie no leitor.
- Comece frase com "E" ou "Mas" apenas de vez em quando, e só se mantiver a relação lógica.
- Use formas como pra, tá e né somente em perfil informal ou quando o texto-fonte as contém.
- Conflito resolvido: a diretriz de origem em inglês pedia "direto, levemente informal, com contrações" como padrão. Esta skill adota voz neutra.
- Para contrações em inglês, siga [modo-ingles.md](modo-ingles.md).

## Perfis autorais e de gênero

### Crônica

- Use tom de cronista brasileiro.
- Use coloquialidade controlada, ironia e observação do cotidiano transformada em reflexão.
- Misture registros alto e baixo.
- Feche com virada reflexiva.
- Aplique este perfil somente quando o texto-fonte ou o pedido forem autorais.
- Nunca trate este perfil como padrão universal.

**Características:**
- Combine "a gente" com mais-que-perfeito simples.
- Use fragmentos de frase como pausa dramática.
- Use humor seco e autoironia somente quando já pertencem à voz ou foram pedidos.
- Mantenha posição autoral explícita. Nunca crie opinião nova.
- Use perguntas retóricas que ficam sem resposta.

**Exemplo:**
> Todo mundo conhece aquele colega que automatizou o próprio trabalho e não contou pra ninguém. Ficou meses fingindo que digitava. Pois é. Agora a empresa inteira virou esse colega — só que usando ChatGPT em vez de scripts em Python. A diferença é que ninguém tá fingindo. E aí fica a dúvida: eficiência ou preguiça? Sei lá. Provavelmente os dois.

### Jornalístico

- Use tom de reportagem da Folha ou Piauí.
- Escreva com clareza máxima e dados concretos.
- Corte firula.

**Características:**
- Escreva na ordem sujeito + verbo + complemento.
- Use números e datas quando presentes no texto-fonte.
- Atribua somente às fontes existentes no texto-fonte.
- Proíba adjetivos avaliativos.
- Proíba primeira pessoa, exceto em coluna assinada.

**Exemplo:**
> A empresa demitiu 40 pessoas da área de atendimento em maio. Dois ex-funcionários atribuíram os cortes à substituição por chatbots. A assessoria não comentou. A área tinha 120 pessoas no início do ano.

### Acadêmico

- Escreva formal, mas não burocrático.
- Use rigor terminológico. Proíba oficialês.

**Características:**
- Use vocabulário preciso de domínio.
- Use qualificações legítimas. Nunca use ressalvas vazias.
- Preserve com exatidão autores e estudos citados na fonte.
- Evite os clichês "faz-se necessário", "cumpre salientar", "no âmbito de".

**Exemplo:**
> A convergência para um registro médio pode ser examinada pela variação lexical em textos submetidos a ciclos sucessivos de refinamento. Nesse contexto, a ablação semântica não acrescenta falsidade; reduz a especificidade.

### Corporativo informal

- Use em e-mail de startup e Slack profissional.
- Escreva direto e leve.
- Proíba gerundismo.

**Características:**
- Use frases curtas e diretas.
- Use "a gente" em vez de "nós" quando cabe.
- Use verbos de ação no lugar de locução verbal.
- Use estrangeirismos naturais (deploy, sprint, feedback).

**Exemplo:**
> Pessoal, atualizando: o hotfix foi deployado ontem à noite, já tá em prod. O bug de duplicação parou desde as 23h. Vou monitorar mais 48h e, se zerar, fechamos a issue. Me pingam se aparecer algo.

### Post de rede social

- Use em LinkedIn ou Twitter BR.
- Escreva curto e opinativo.
- Abra com gancho na primeira linha.

**Características:**
- Faça da primeira frase o gancho.
- Escreva parágrafos de 1-2 linhas.
- Mantenha posição autoral clara. Nunca crie opinião nova.
- Use "eu" somente quando a fonte já usa primeira pessoa ou o usuário pede.
- Use chamada para ação sutil ou nenhuma.

**Exemplo:**
> Eu demiti o ChatGPT do meu fluxo de escrita.
>
> Não porque é ruim. Porque tudo que eu publicava soava igual a todo mundo.
>
> Voltei a escrever na mão. Demora 3x mais. Mas as pessoas respondem agora.
>
> Eficiência sem voz não é vantagem. É invisibilidade.

### Mensagem de WhatsApp

- Use oralidade máxima.
- Permita fluxo de consciência.

**Características:**
- Aceite frases incompletas.
- Use abreviações naturais (vc, tb, mto).
- Aceite gírias regionais.
- Dispense a norma culta.

**Exemplo:**
> cara tu viu o que o time de dados fez?
>
> meteram um modelo em prod sem avisar ninguém
>
> aí começou a mandar e-mail errado pra cliente
>
> mó treta

### Jurídico / oficialesco

- Use em petições, pareceres e notificações.
- Escreva em registro formal.
- Use os tiques do gênero somente de forma deliberada.
- Os tiques deliberados soam mais autênticos que a imitação genérica da IA.

**Características:**
- Estruture em preâmbulo → fatos → fundamentos → pedido.
- Use clichês do gênero de forma controlada ("data venia", "ante o exposto", "é cediço que").
- Cite artigos, súmulas e jurisprudência.
- Use voz ativa quando possível para evitar burocratês vazio.

**Sinais de IA nesse registro:**
- Marque excesso de "cumpre salientar", "faz-se mister", "no âmbito desta análise".
- Marque citações genéricas sem número de artigo ou lei.
- Marque parágrafos perfeitamente simétricos (3-4 frases idênticas).

**Exemplo (IA → Humano):**
> *IA*: "Nos termos do art. 14 do CDC, cumpre salientar que a responsabilidade do fornecedor é objetiva no caso em tela."
>
> *Humano*: "O art. 14 do CDC estabelece a responsabilidade objetiva do fornecedor neste caso."

**O que preservar (não é sinal de IA):**
- Preserve seções em CAPS ("DOS FATOS", "DO DIREITO", "DOS PEDIDOS"). É formatação esperada em petições.
- Preserve a numeração de itens em pedidos e fundamentos.
- Preserve a citação de artigos com número de lei e data (Art. 14, CDC; Súmula 362/STJ).
- Preserve a estrutura preâmbulo → fatos → fundamentos → pedido. É o gênero, não molde de IA.

**Sinal de revisão nesse registro:**
- Marque atribuição vaga como "conforme entendimento consolidado".
- Se a fonte não trouxer artigo, súmula ou precedente específico, aponte a lacuna.
- Nunca crie a referência.

### Didático / explicador

- Use em textos de edtech, apostilas, tutoriais e documentação técnica amigável.

**Características:**
- Siga o padrão pergunta → explicação → exemplo concreto → reforço.
- Use vocabulário acessível, mas preciso. Nunca infantilize.
- Use exemplos específicos já presentes na fonte ou fornecidos pelo usuário.
- Use transições explícitas: "Então", "Agora", "Vamos ver na prática".

**Sinais de IA nesse registro:**
- Marque exemplos genéricos e artificiais.
- Marque tom enciclopédico sem interação com o leitor.
- Marque "Neste capítulo, abordaremos X, Y e Z" como molde vazio.

**Exemplo:**
> Vamos direto ao ponto: *callback* é uma função que você passa como argumento pra outra função, pra ela te "chamar de volta" quando terminar. Parece complicado, mas é só isso. Imagine que você pediu um delivery: em vez de ficar ligando a cada 5 minutos pra saber se chegou, você deixa seu número e o entregador te avisa quando estiver na porta. Seu número é o callback.

**Hipóteses em texto novo:**
- A amostra acima usa "Imagine que você pediu um delivery". Ela fica como dado verbatim.
- Marque hipóteses com "Suponha que" ou "Por hipótese".
- Nunca abra com "Imagine um mundo onde" nem com "Imagine se".

### Português simplificado

- Escreva texto acessível para público amplo.
- Baseie-se nas operações do PorSimples (NILC/USP) e nas técnicas da Lei 15.263/2025 (Política Nacional de Linguagem Simples).
- Simplifique a forma. Nunca infantilize o raciocínio.
- Consulte [padroes-portugues-simplificado.md](padroes-portugues-simplificado.md) para operações, tabelas lexicais, métricas e regras R1-R15.

**Quando usar:**
- Use em documentação técnica para público não-especialista.
- Use em comunicação institucional e governamental.
- Use em manuais de produto, FAQs e onboarding de usuários.
- Use em textos para públicos com letramento funcional variado.
- Use quando o usuário pedir "simplificar", "linguagem simples", "mais claro", "acessível".

**Características:**
- Escreva frases curtas em ordem direta (SVO). Meta: 13-18 palavras. Máximo: 25.
- Escreva uma ideia por frase.
- Use vocabulário comum. Explique termo técnico na primeira ocorrência.
- Use voz ativa. Use passiva apenas quando o agente for irrelevante ou desconhecido.
- Use listas e estrutura visual para 3+ itens em sequência.
- Use conectivos explícitos e simples ("porque", "por isso", "então", "mas").
- Proíba orações intercaladas longas. Apostos com mais de 5 palavras viram frase nova.
- Use repetição deliberada para clareza. Nunca force sinônimos variados.

**O que NÃO fazer:**
- Nunca elimine raciocínio complexo. Simplifique a forma, não o conteúdo.
- Nunca remova terminologia de domínio. Explique, não substitua.
- Nunca transforme toda prosa em lista de bullets indiscriminadamente.
- Nunca adicione exemplos fictícios para "ajudar". Use apenas os da fonte.
- Nunca reduza modalidade: "pode causar" não vira "causa".

**Exemplo:**
> *Antes:* "A implementação de políticas públicas que visem à mitigação dos impactos socioeconômicos decorrentes da automação de processos produtivos configura-se como desafio premente para gestores em todas as esferas do poder público."
>
> *Depois:* "A automação muda como as pessoas trabalham. Isso traz problemas sociais e econômicos. Os governos precisam criar políticas para reduzir esses problemas. Esse é um desafio urgente em todas as esferas — federal, estadual e municipal."

## Perfis de consumo rápido

- Aplique esta seção aos perfis Assertivo, Enxuto e Resumo.
- Otimize para consumo (absorção rápida pelo leitor), não para autoria (texto que alguém vai assinar).
- Em perfil autoral, preserve voz e estilo.
- Em perfil de consumo, priorize a transferência eficiente de informação.
- Aplique a TRAVA FACTUAL de [SKILL.md](../SKILL.md). Veja [Brevidade por compressão](#brevidade-por-compressão).

### Quando usar cada perfil

| Perfil | Público | Formato típico | Otimiza para |
|---|---|---|---|
| ➡️ **Assertivo** | Tomador de decisão, leitor com atenção fragmentada | E-mail, Slack, briefing, resposta técnica | Escaneabilidade: quem lê só o bold entende |
| 🔹 **Enxuto** | Dev em flow, operador em troubleshooting | Terminal, chat técnico, instrução | Densidade máxima: uma linha quando basta |
| 📊 **Resumo** | Gestor, equipe em standup, stakeholder | Status update, notas de reunião, sprint review | Legibilidade: board de estado, não parágrafo |

**Regra de seleção rápida:**
- Leitor precisa **agir** → Enxuto
- Leitor precisa **decidir** → Assertivo
- Leitor precisa **acompanhar** → Resumo

### Assertivo

- Use tom assertivo para leitor que precisa de sinal, não de conversa.
- Corte toda frase que não justifique seu lugar.

**Quando usar:**
- Use em respostas a perguntas objetivas em Slack, e-mail ou documento.
- Use em briefings de decisão onde o leitor quer a resposta, não a jornada.
- Use em comunicação técnica para público com atenção fragmentada.
- Use quando o usuário pedir "direto ao ponto", "sem enrolação" ou "resumo executivo".

**Características:**
- Escreva a resposta completa na primeira frase. Quem lê só ela entende o essencial.
- Escreva parágrafos de 1-3 frases, uma ideia por bloco.
- Use negrito em termos-chave, números e decisões. Quem escaneia o bold pega o ponto.
- Proíba preâmbulo, reafirmação da pergunta e resumo no final.
- Mantenha tom caloroso, mas econômico: amigo perspicaz, não manual frio.
- Proíba filler: nada de "Ótima pergunta", "Com certeza", "Na verdade".
- Escreva avisos e ressalvas em linha própria. Nunca os enterre.
- Converta instrução em ação. Quando o trecho manda fazer algo, comece a frase pelo verbo e pelo alvo (comando, caminho, arquivo). Nunca comece pela justificativa.

**TRAVA FACTUAL neste perfil:** comprima a forma, nunca o conteúdo. Corte elaboração, **nunca** warning. Veja [Brevidade por compressão](#brevidade-por-compressão).

**Sinais de IA nesse registro:**
- Marque negrito em *toda* palavra-chave (decoração, não hierarquia).
- Marque preâmbulo disfarçado: "Para responder isso, precisamos considerar..."
- Marque resumo no final repetindo o que já foi dito.
- Marque ressalvas genéricas em vez de risco concreto.
- Marque tom seco demais. Direto não é grosseiro.

**Exemplo (IA → Humano):**
> *IA*: "Para responder à sua pergunta sobre qual banco de dados utilizar, é importante considerar diversos fatores. PostgreSQL é uma excelente opção para aplicações que necessitam de relacionamentos complexos. Por outro lado, MongoDB pode ser mais adequado para cenários específicos. Em resumo, a escolha depende das suas necessidades."
>
> *Humano*: "**Use PostgreSQL.** App social é todo relacionamentos (amigos, follows, likes), e Postgres lida nativamente. Correto para ~90% de apps sociais novos.
>
> **MongoDB só se:** você tem dados sem schema que mudam toda semana, ou volume de escrita que justifique o trade-off.
>
> **Armadilha comum:** começar com Mongo achando que é mais flexível e depois gastar meses migrando quando precisar de JOIN."

**Aviso sobre o exemplo:**
- O Humano acima acrescenta "amigos, follows, likes" e "~90%", que o IA não traz.
- Use o exemplo como modelo de forma.
- Nunca acrescente fato, número ou estatística ausente da fonte em saída real.

**O que preservar (não é sinal de IA):**
- Preserve negrito em hierarquia de escaneabilidade (títulos de ponto, números, decisão).
- Preserve frases muito curtas em série quando cada uma carrega uma ideia distinta.
- Preserve tom direto sem ser rude. Economia não é frieza.
- Preserve setas (→) quando indicam fluxo ou consequência, não decoração.

### Enxuto

- Entregue sinal máximo e zero conforto.
- Use modo heads-down para quem quer fato, não conversa.
- Use quando o leitor está no meio de uma tarefa e precisa da resposta sem atrito.

**Quando usar:**
- Use em respostas durante coding/debugging (o leitor está em flow).
- Use em instruções de terminal, comandos e troubleshooting.
- Use em confirmações de ação ("faz X" → resposta confirma que fez).
- Use quando o usuário pedir "curto", "só o necessário" ou responder com monossílabos.

**Características:**
- Escreva a resposta completa na linha 1, em uma sentença.
- Proíba calor, hedge e transição.
- Use imperativo quando cabe: "Use", "Rode", "Corte".
- Escreva um ponto por linha quando uma linha basta.
- Escreva números exatos. Nunca arredonde.
- Escreva risco ou incerteza em linha própria, direta.
- Quando a tarefa for "faça X", confirme em uma linha e faça. Nunca narre o que vai fazer.

**TRAVA FACTUAL neste perfil:** curto não elimina warning. Se a omissão faz o leitor agir errado, mantenha o trecho, mesmo que quebre a brevidade. Veja [Brevidade por compressão](#brevidade-por-compressão).

**Sinais de IA nesse registro:**
- Marque explicação não solicitada ("Isso funciona porque...").
- Marque qualquer forma de "espero que ajude".
- Marque narração da própria ação ("Vou agora verificar o arquivo...").
- Marque ressalva genérica sem risco concreto.
- Marque parágrafo onde caberia uma linha.
- Marque dramatização de erro: "Ops", "Infelizmente", "Parece que algo deu errado". Descreva o erro por causa e correção, nada mais.
- Marque idiomatismo onde cabe a ação literal ("colocar em pauta", "alinhar expectativas", "dar um norte"). Neste perfil ele custa um passo de decodificação que o leitor não tem.

**Exemplo (IA → Humano):**
> *IA*: "Para corrigir esse erro, você precisará verificar o arquivo de configuração. O problema parece estar relacionado à variável de ambiente que não foi definida corretamente. Recomendo que você abra o arquivo .env e verifique se a chave DATABASE_URL está presente. Espero que isso ajude a resolver o problema."
>
> *Humano*: "Falta `DATABASE_URL` no `.env`. Adicione a linha e reinicie o server."

**Aviso sobre o exemplo:**
- O Humano acima acrescenta "reinicie o server", que o IA não traz.
- Use o exemplo como modelo de forma.
- Nunca acrescente instrução ausente da fonte em saída real.

**O que preservar (não é sinal de IA):**
- Preserve imperativo seco. É o registro, não grosseria.
- Preserve a ausência de "por favor" ou "obrigado" em contexto técnico.
- Preserve resposta de uma linha quando uma linha basta.
- Preserve comando sem explicação quando a explicação não foi pedida.

### Resumo

- Escreva board de status para escanear, não parágrafo para ler.
- Informe o que mudou, o que está travado e o que precisa de decisão.
- Otimize para legibilidade, não para brevidade.

**Quando usar:**
- Use em standups, status updates e notas de reunião.
- Use em relatórios de progresso e sprint reviews.
- Use em qualquer contexto onde o leitor pergunta "como está X?".
- Use quando o usuário pedir "resumo de status", "update rápido" ou "onde estamos".

**Características:**
- Abra com **TL;DR** de uma linha carregando resultado e bloqueio principal.
- Mostre o estado como checklist visual:
  - ✅ feito
  - 🟡 em andamento
  - ⬜ não iniciado
  - ❔ desconhecido
  - 🔴 bloqueio/risco
- Escreva linhas curtas, uma ideia cada. Nunca escreva paredes de texto.
- Termine com ação clara ou pick-one.
- Escreva prazo em unidade concreta quando a fonte fornece: "3 dias úteis", "até 4ª", "~2 semanas".
- Nunca converta prazo ausente em estimativa. Sem prazo na fonte, marque o item ❔.

**TRAVA FACTUAL neste perfil:**
- Nunca invente status.
- Se o estado de um item é desconhecido, marque ❔ e diga o que resolveria.
- Checklist inventada é pior que checklist incompleta.
- Prazo inventado é status inventado. Vale a mesma regra.

**Estrutura do perfil Resumo:**

```markdown
**TL;DR:** [Uma linha com resultado + bloqueio principal]

**[Categoria]:**
✅ **Item 1:** status
🟡 **Item 2:** status
⬜ **Item 3:** status

🔴 **Bloqueio:** [Descrição do impedimento]

**Sua vez:**
1. Opção 1
2. Opção 2
3. Opção 3
```

**Regras da estrutura:**
- Escreva o TL;DR de modo que se sustente sozinho. Quem lê só ele entende o essencial.
- Escreva um item por linha. Negrite o assunto.
- Escreva o bloqueio sempre em linha própria com 🔴.
- Escreva "Sua vez" com opções numeradas, para o leitor escolher por número.
- Nunca invente status. Se desconhecido, marque ❔.

**Sinais de IA nesse registro:**
- Marque status inventado (item que não estava na fonte).
- Marque TL;DR que não se sustenta sozinho.
- Marque parágrafo corrido onde cabia checklist.
- Marque emoji decorativo (🚀💡🎯) sem função de status.
- Marque "Conforme alinhado" ou "dando seguimento" como filler.

**Exemplo (IA → Humano):**
> *IA*: "Com relação ao andamento do projeto de contratação, gostaria de informar que recebemos 20 candidatos até o momento. Destes, 5 foram triados e 2 entrevistas estão agendadas. Ainda não fizemos nenhuma oferta. Vale ressaltar que temos um candidato forte que pode estar considerando outras oportunidades, o que demanda atenção especial da equipe."
>
> *Humano*: "**TL;DR:** Pipeline saudável no topo, linha de chegada travada. Candidato forte escorregando.
>
> **Funil:**
> ✅ **Candidatos:** 20 recebidos
> ✅ **Triagem:** 5 de 20
> 🟡 **Entrevistas:** 2 agendadas, não realizadas
> ⬜ **Oferta:** não rascunhada
>
> 🔴 **Bloqueio:** Candidato forte com outras propostas — janela de ~5 dias.
>
> **Sua vez:**
> 1. Fast-track o candidato forte (decisão até 4ª)
> 2. Rodar as 2 entrevistas esta semana
> 3. Rascunhar oferta agora para não travar depois"

**Aviso sobre o exemplo:**
- O Humano acima acrescenta "janela de ~5 dias" e "(decisão até 4ª)", que o IA não traz.
- Use o exemplo como modelo de forma.
- Nunca acrescente prazo ausente da fonte em saída real.

**O que preservar (não é sinal de IA):**
- Preserve emojis de status (✅🟡⬜❔🔴). São notação funcional, não decoração.
- Preserve lista com mais de 5 itens quando o status exige.
- Preserve a repetição em "Sua vez" do item que já apareceu no status. A redundância é proposital (ver → decidir).
- Preserve a estrutura de board mesmo em texto corrido no canal original.

### Regras comuns

- Aplique estas regras a **Assertivo**, **Enxuto** e **Resumo**.
- Nunca as aplique aos perfis autorais.

**Quatro restrições do leitor:**
1. O que não está na tela foi esquecido. Nunca escreva "tendo em vista o que foi dito acima".
2. Entender não é executar. Texto que explica bem e não diz o que fazer falhou.
3. Começar é o passo caro. Faça da primeira ação algo pequeno e óbvio.
4. Prazo vago não registra. "Em breve" e "algumas semanas" chegam iguais.

Em caso de dúvida sobre uma escolha de forma, decida pelo que reduz o custo de agir.

**Passo a passo vira lista numerada:**
- Converta sequência de duas ou mais ações executáveis em lista numerada.
- Escreva uma ação por item.
- Nunca repita "e então" no mesmo item.
- Marque prosa corrida com passos embutidos como sinal de IA nestes perfis.

**Fechamento é ação, não recapitulação:**
- Mantenha a proibição de resumo final.
- Se o texto-fonte deixa algo em aberto, nomeie na última linha **uma** ação concreta que o leitor faz agora.
- Nunca recapitule o que já foi dito. Recapitular é ruído.
- Apontar o próximo passo é a entrega.
- Se a fonte não deixa nada em aberto, termine na última informação.

**Assunto secundário sai do meio:**
- Nunca transforme o segundo tema do texto-fonte em parêntese, "vale mencionar" ou digressão no meio do primeiro.
- Termine o primeiro assunto.
- Depois escreva o segundo em bloco próprio ou como pergunta ao final.
- Nunca descarte o assunto. A TRAVA FACTUAL vale aqui.
- A regra é de posição, não de corte.

**Cláusula de escape (os três perfis):**
- Se o usuário pedir profundidade ("explica de verdade", "por quê", "detalha"), desligue a compressão.
- Entregue o contexto inteiro.
- Mantenha o registro: sem preâmbulo, sem fecho cortês, corpo do tamanho que o assunto exigir.

### Formatação

#### Marcadores: → vs - vs *

| Contexto | Marcador | Exemplo |
|---|---|---|
| Fluxo ou consequência | → | `→ Resultado: deploy bem-sucedido` |
| Lista comum sem hierarquia | - | `- Item 1` |
| Ênfase em lista | * com negrito | `* **Ponto crítico:** descrição` |

- Use `→` apenas para indicar resultado, consequência ou próximo passo.
- Use `-` para listas simples.
- Nunca misture `→` e `-` no mesmo bloco. É sinal de inconsistência.

#### Negrito: funcional vs decorativo

| Uso | Exemplo | Veredicto |
|---|---|---|
| Lead-in de ponto | **Use PostgreSQL.** App social é... | ✅ Funcional |
| Termo-chave de decisão | ...correto para **~90% de apps** | ✅ Funcional |
| Número crítico | Timeout de **30s** | ✅ Funcional |
| Aviso/warning | **Armadilha comum:** | ✅ Funcional |
| Substantivo comum | A **plataforma** oferece **integração**... | ❌ Decorativo |
| Toda palavra importante | **PostgreSQL** é **bom** para **apps** | ❌ Decorativo |

- Use negrito para marcar hierarquia de escaneabilidade.
- Garanta que quem lê só o bold entende a resposta completa, a decisão principal e qualquer aviso.
- Se remover o negrito não prejudica a compreensão rápida, trate-o como decorativo e remova-o.
- Consulte a regra canônica na seção Negrito excessivo de [padroes-estilo.md](padroes-estilo.md).

#### Emojis: estado vs decoração

| Emoji | Função | Perfil |
|---|---|---|
| ✅ | Feito/concluído | 📊 Resumo |
| 🟡 | Em andamento | 📊 Resumo |
| ⬜ | Não iniciado | 📊 Resumo |
| ❔ | Desconhecido | 📊 Resumo |
| 🔴 | Bloqueio/risco | 📊 Resumo |
| 🚀💡🎯✨ | Decoração | ❌ Nenhum |

- Use emojis de estado como notação funcional. Cada um indica um status específico.
- Proíba emojis decorativos (🚀💡🎯). Eles não têm função comunicativa.
- Marque emoji decorativo como sinal de IA em qualquer perfil.
- Consulte a regra geral na seção Emojis decorativos de [padroes-estilo.md](padroes-estilo.md).

### Regras de corte

#### O que SEMPRE cortar

| Padrão | Exemplo | Por que cortar |
|---|---|---|
| Preâmbulo | "Para responder à sua pergunta..." | Atrasa a resposta |
| Reafirmação da pergunta | "Você perguntou sobre bancos de dados..." | Redundante |
| Filler openers | "Ótima pergunta!", "Com certeza!" | Zero informação |
| Resumo final | "Em resumo, PostgreSQL é a melhor opção" | Repete o que já foi dito |
| Narração de ação | "Vou agora verificar o arquivo..." | Fazer, não narrar |
| Transições mecânicas | "Além disso", "Por outro lado", "Nesse sentido" | Padding |
| Ressalva genérica | "É importante considerar diversos fatores" | Não diz nada |
| Despedida | "Espero que isso ajude!" | Filler |
| Dramatização de erro | "Ops", "Infelizmente", "Parece que algo deu errado" | Erro se descreve por causa e correção |
| Idiomatismo (só 🔹 Enxuto) | "Colocar em pauta", "alinhar expectativas", "dar um norte" | Custa um passo de decodificação |

#### O que reposicionar (não cortar)

- Mude o lugar da informação. Nunca elimine a informação.
- A TRAVA FACTUAL vale integralmente.

| Situação na fonte | O que fazer |
|---|---|
| Duas ou mais ações executáveis em prosa corrida | Lista numerada, uma ação por item, sem "e então" duas vezes no mesmo item |
| Algo em aberto ao final | Última linha nomeia **uma** ação concreta que o leitor faz agora, nunca recapitulação |
| Nada em aberto ao final | Texto termina na última informação, sem fecho |
| Segundo assunto no meio do primeiro | Termina o primeiro, depois o segundo em bloco próprio ou pergunta ao final |

- Não confunda reposicionar com cortar.
- Corte a recapitulação e inclua a próxima ação.
- Mude a posição do assunto secundário. Nunca o apague.

#### O que NUNCA cortar

| Elemento | Por que preservar |
|---|---|
| Warning/aviso | Omissão pode causar erro do leitor |
| Número exato | "~30s" não é igual a "alguns segundos" |
| Condição de escopo | "Apenas para workspaces < 14 dias" não vira "para workspaces" |
| Modalidade | "Pode causar" não vira "causa" |
| Fonte/atribuição | Quem disse ou de onde veio |
| Exceção mencionada | Restrição faz parte do fato |

**Regra mestre:** se omitir o trecho faz o leitor agir errado, mantenha o trecho, mesmo que quebre a brevidade.

### Padrões que continuam e padrões suspensos

#### Padrões de IA que CONTINUAM se aplicando

- Aplique estes padrões também em modo conciso.
- Eles denunciam texto de IA.

| Padrão | Descrição | Referência |
|---|---|---|
| Conclusão sinalizada | "Em conclusão", "Em resumo" no final | [padroes-composicao.md](padroes-composicao.md) |
| Metáfora morta | "Ecossistema", "jornada", "cenário" repetidos | [padroes-composicao.md](padroes-composicao.md) |
| Ressalva vazia | "É importante considerar" sem dizer o quê | [padroes-conteudo-tom.md](padroes-conteudo-tom.md) |
| Vocabulário genérico | "Impacto", "contexto", "solução" sem especificidade | [padroes-linguagem-ptbr.md](padroes-linguagem-ptbr.md) |
| Autorreferência | "Como assistente de IA..." | [padroes-conteudo-tom.md](padroes-conteudo-tom.md) |

#### Padrões SUSPENSOS nestes perfis

| Padrão | Suspenso em | Justificativa |
|---|---|---|
| Negrito excessivo | ➡️ Assertivo, 🔹 Enxuto | Negrito em lead-in é hierarquia, não decoração |
| Fragmentos curtos | 🔹 Enxuto | Uma linha é o formato, não fragmento dramático |
| Decoração Unicode (→) | ➡️ Assertivo | Seta indica fluxo/consequência, não decora |
| Emoji em cada item | 📊 Resumo | Emojis de estado são notação funcional |
| Listicle disfarçado | 📊 Resumo | Lista É o formato declarado, não disfarce |

### Brevidade por compressão

- Comprima a forma, nunca o conteúdo.
- Se o original tem 5 proposições, a reescrita tem as mesmas 5, em menos palavras.
- Corte molduras e transições.
- Preserve toda proposição, relação causal, número, qualificação de escopo e aviso.
- Quando um trecho protegido conflitar com a brevidade, a brevidade cede.

```
CORRETO:
  Original (50 palavras) → Reescrita (25 palavras)
  Mesmas 5 proposições, metade das palavras
  
ERRADO:
  Original (50 palavras) → Reescrita (25 palavras)
  3 proposições, 2 foram cortadas
```

**Regra "Cortar elaboração, nunca warning":**

```python
para cada trecho do original:
    se trecho é warning/aviso:
        manter integralmente
    se trecho é número/threshold:
        manter exato
    se trecho é condição de escopo:
        manter completo
    se trecho é elaboração/exemplo:
        comprimir ou cortar
    se trecho é transição/filler:
        cortar
```

- Rode a verificação específica de brevidade (6 itens) do Passo 7 em [auditoria-entrega.md](auditoria-entrega.md).

### Exemplos com contagem de palavras

- Use os rótulos de contagem como ordem de grandeza.
- Contagem real por espaços: Assertivo 69 para 52; Enxuto 55 para 11; Resumo 52 para 62.

**Aviso sobre os exemplos:**
- Os Depois acrescentam fatos que o Antes não traz, entre eles "amigos, follows, likes", "~90%", "reinicie o server" e "janela de ~5 dias".
- Use os exemplos como modelo de forma, nunca de conteúdo.
- Nunca acrescente fato, número ou prazo ausente da fonte em saída real.

#### Exemplo do perfil Assertivo

**Contexto:** Resposta sobre escolha de banco de dados

**Antes (IA — 87 palavras):**
> Para responder à sua pergunta sobre qual banco de dados utilizar para seu novo aplicativo social, é importante considerar diversos fatores relevantes. PostgreSQL é uma excelente opção para aplicações que necessitam de relacionamentos complexos entre entidades. Por outro lado, MongoDB pode ser mais adequado para cenários específicos onde a flexibilidade de schema é prioritária. Em resumo, a escolha final depende das suas necessidades específicas e do contexto do projeto.

**Depois (Assertivo — 52 palavras):**
> **Use PostgreSQL.** App social é todo relacionamentos (amigos, follows, likes), e Postgres lida nativamente. Correto para ~90% de apps sociais novos.
>
> **MongoDB só se:** dados sem schema que mudam toda semana, ou volume de escrita que justifique o trade-off.
>
> **Armadilha comum:** começar com Mongo e gastar meses migrando quando precisar de JOIN.

#### Exemplo do perfil Enxuto

**Contexto:** Troubleshooting de erro

**Antes (IA — 54 palavras):**
> Para corrigir esse erro que você está enfrentando, você precisará verificar o arquivo de configuração do seu projeto. O problema parece estar relacionado à variável de ambiente que não foi definida corretamente. Recomendo que você abra o arquivo .env e verifique se a chave DATABASE_URL está presente. Espero que isso ajude a resolver o problema.

**Depois (Enxuto — 12 palavras):**
> Falta `DATABASE_URL` no `.env`. Adicione a linha e reinicie o server.

#### Exemplo do perfil Resumo

**Contexto:** Status de processo de contratação

**Antes (IA — 62 palavras):**
> Com relação ao andamento do projeto de contratação, gostaria de informar que recebemos 20 candidatos até o momento. Destes, 5 foram triados e 2 entrevistas estão agendadas. Ainda não fizemos nenhuma oferta. Vale ressaltar que temos um candidato forte que pode estar considerando outras oportunidades, o que demanda atenção especial da equipe.

**Depois (Resumo — 58 palavras, mas escaneável):**
> **TL;DR:** Pipeline saudável no topo, linha de chegada travada. Candidato forte escorregando.
>
> **Funil:**
> ✅ **Candidatos:** 20 recebidos
> ✅ **Triagem:** 5 de 20
> 🟡 **Entrevistas:** 2 agendadas, não realizadas
> ⬜ **Oferta:** não rascunhada
>
> 🔴 **Bloqueio:** Candidato forte com outras propostas — janela de ~5 dias.
>
> **Sua vez:**
> 1. Fast-track o candidato forte
> 2. Rodar as 2 entrevistas esta semana
> 3. Rascunhar oferta agora

### Perfis de consumo vs perfis autorais

| Aspecto | Perfis Autorais | Perfis de Consumo |
|---|---|---|
| **Foco** | Voz, estilo, autenticidade | Transferência eficiente de informação |
| **Público** | Leitor que vai ler tudo | Leitor que vai escanear |
| **Formatação** | Mínima, a serviço da voz | Estruturada para navegação |
| **Negrito** | Evitar excesso | Usar para hierarquia |
| **Listas** | Quando natural | Quando facilita consumo |
| **Tom** | Varia por perfil | Consistentemente direto |
| **Exemplos** | Crônica, Jornalístico, Acadêmico | Assertivo, Enxuto, Resumo |
| **Pergunta-guia** | "Como o autor diria isso?" | "O que o leitor precisa saber?" |

### Checklist de consumo rápido

Rode esta checklist antes de entregar texto em perfil de consumo rápido:

- [ ] Verifique se a primeira frase carrega a resposta/decisão principal.
- [ ] Verifique se quem lê só o bold entende o essencial.
- [ ] Verifique se nenhum warning/aviso foi cortado.
- [ ] Verifique se números e thresholds estão exatos.
- [ ] Verifique se as condições de escopo estão completas.
- [ ] Verifique que não há filler (preâmbulo, despedida, "espero que ajude").
- [ ] Verifique se cada emoji tem função (estado) ou é decoração.
- [ ] Verifique se o negrito marca hierarquia ou decora substantivos.
- [ ] Verifique se o TL;DR se sustenta sozinho (perfil Resumo).
- [ ] Verifique se nenhum status foi inventado (perfil Resumo).
- [ ] Verifique se o prazo está em unidade concreta, sem estimar prazo ausente (perfil Resumo).
- [ ] Verifique se o passo a passo está em lista numerada, uma ação por item.
- [ ] Verifique se o fecho é ação concreta ou fim seco, nunca recapitulação.
- [ ] Verifique se o assunto secundário está fora do meio do primeiro.

## Aplicação da voz por perfil

- Aplique somente os recursos permitidos pelo perfil ativo.

| Perfil | Aplicar | Evitar |
|---|---|---|
| Voz neutra | Clareza, ritmo natural e transições discretas | Primeira pessoa, opinião, humor ou mudança de registro |
| Crônica | Ritmo irregular e ironia já sustentada pela fonte ou pedida pelo usuário | Inventar lembrança, sentimento ou observação pessoal |
| Jornalístico | Ordem direta, atribuição precisa e linguagem sóbria | Adjetivação avaliativa, primeira pessoa e fontes novas |
| Acadêmico | Terminologia de domínio e qualificações necessárias | Novas referências, certezas maiores que as da fonte e coloquialidade gratuita |
| Corporativo Informal | Frases diretas, leveza e estrangeirismos naturais do domínio | Criar status, prazo, promessa, chamada para ação ou experiência pessoal |
| Post de Rede Social | Gancho baseado na tese existente e parágrafos curtos | Criar opinião, história pessoal ou chamada para ação ausente |
| WhatsApp | Oralidade compatível com o canal e abreviações naturais | Alterar compromisso, data, destinatário ou grau de certeza |
| Jurídico | Formalidade controlada, estrutura e termos do gênero | Criar artigo, súmula, precedente, fato ou fundamento |
| Didático | Ordem clara e explicação acessível | Criar analogia, personagem, dado ou exemplo não fornecido |
| Português Simplificado | SVO, frases ≤25 palavras, vocabulário comum, listas para 3+ itens e termos técnicos explicados | Eliminar conteúdo, reduzir modalidade, inventar exemplo ou remover terminologia de domínio |
| Assertivo | Primeira frase como resposta completa, negrito em hierarquia, parágrafos curtos, avisos em linha própria | Preâmbulo, resumo final, filler openers, negrito decorativo, explicar o que não foi perguntado |
| Enxuto | Linha 1 = resposta, imperativo, números exatos, uma linha quando basta | Narrar ação, explicar sem pedido, ressalva genérica, "espero que ajude", parágrafo onde cabe linha |
| Resumo | TL;DR, checklist de status (✅🟡⬜🔴), bloqueio em destaque, opções numeradas em "Sua vez" | Inventar status, emoji decorativo, parágrafo corrido, TL;DR que não se sustenta sozinho |

- Quando o usuário fornecer amostra de voz, espelhe comprimento de frases, nível vocabular, início de parágrafos, pontuação e uso de estrangeirismos.
- Nunca copie fatos, opiniões, personagens ou experiências da amostra para o texto reescrito.
