# Integração com TypeSafe Jev

## Regras de uso

- Use Jev só quando o usuário pedir avaliação externa e Jev já estiver disponível.
- Nunca instale serviços, escolha provedores pagos nem delegue automaticamente.
- Calcule pontuação só quando solicitada. Ela é julgamento editorial subjetivo.
- Nenhuma decisão do avaliador supera uma violação semântica detectada.
- Os limites de tentativas, a proveniência e a trava semântica de [SKILL.md](../SKILL.md) valem aqui.

## O que é o Jev

Jev é o modelo flagship da TypeSafe AI: o primeiro **System One Model**. Ele não gera texto: classifica, pontua e decide, com probabilidades calibradas (quando diz 70%, é 70% mesmo).

- Latência: 70-500ms para dezenas de perguntas paralelas.
- Custo: $0.042/M tokens de entrada, output grátis.
- ~50-100x mais barato que avaliação via GPT-4.

## Quando usar Jev ou avaliação LLM

Use Jev para diagnóstico, verificação e scoring. A reescrita continua com o LLM.

|Aspecto|Avaliação LLM|Avaliação Jev|
|---------|---------------|---------------|
|Consistência|Varia entre chamadas|Determinístico|
|Calibração|P(70%) ≠ 70% real|P(70%) = 70% real|
|Custo|~$0.01-0.05/avaliação|~$0.0001-0.0002/avaliação|
|Latência|1-5s|70-500ms|
|Output|Texto (precisa parsing)|Estruturado nativo|

Prefira avaliação LLM quando:

- Textos muito curtos (<50 palavras)
- `modo_direto` com pressa
- Debug/desenvolvimento (mais fácil inspecionar reasoning)
- Jev não disponível no harness

## Protocolo de descoberta

Nunca assuma que Jev está disponível. Rode este protocolo antes de usá-lo.

### Resumo

```
1. Verificar MCP tools disponíveis no harness
   → Se existir tool "jev_eval" ou similar → usar

2. Verificar se harness usa OpenRouter
   → Se sim, solicitar modelo `typesafe/jev-latest`

3. Verificar slots auxiliares (Hermes, Devin)
   → Se slot approval/custom configurado com Jev → usar

4. Fallback → avaliação inline via LLM atual
```

### Ordem de prioridade

```
1. MCP Tool `jev_eval` já configurado no harness
   ↓ (não encontrado)
2. Modelo `typesafe/jev-latest` via OpenRouter
   ↓ (não disponível)
3. Modelo `jev-latest` em slot auxiliar (Hermes, Devin)
   ↓ (não configurado)
4. Fallback: avaliação inline via LLM atual do harness
```

### Passo 1: verificar MCP tools

```
Pergunte ao harness: "Quais MCP tools estão disponíveis?"

Se existir tool com nome contendo "jev" ou "typesafe":
  → Usar essa tool para avaliação
  → Pular para execução
```

### Passo 2: verificar OpenRouter

```
Se o harness usa OpenRouter como provider:
  → Verificar se `typesafe/jev-latest` está no catálogo
  → Se sim, solicitar esse modelo para chamadas de avaliação
```

### Passo 3: verificar slots auxiliares (Hermes, Devin)

```
Em Hermes Agent:
  → Verificar se slot `approval` está configurado com Jev
  → Se sim, usar esse slot para avaliação

Em Devin:
  → Verificar se existe subagent profile com model: jev-latest
  → Se sim, delegar avaliação para esse subagent
```

### Passo 4: fallback para LLM

```
Se nenhuma opção Jev disponível:
  → Executar avaliação inline usando o LLM atual
  → Usar os mesmos critérios, mas via prompt engineering
```

## Instruções por harness

|Harness|Como detectar Jev|
|---------|-------------------|
|**Claude Code**|Verificar MCP em `.claude/mcp.json` → tool `jev_eval`|
|**Cursor**|Verificar se OpenRouter é provider → modelo `typesafe/jev-latest`|
|**Devin**|Verificar `agents/*.md` → profile com `model: typesafe/jev-latest`|
|**Hermes**|Verificar `config.yaml` → `auxiliary.approval.model`|
|**Kiro/Copilot/Cline**|Verificar MCP servers ou lista de modelos disponíveis|
|**Aider/OpenCode**|Verificar providers configurados|

### Claude Code

```markdown
## Descoberta de Jev

1. Verificar MCP: execute `mcp list` ou consulte .claude/mcp.json
2. Se `jev-eval` MCP server configurado → usar tool `jev_avaliar`
3. Se não → avaliação inline via Claude
```

### Cursor

```markdown
## Descoberta de Jev

1. Verificar se OpenRouter está configurado como provider
2. Se sim, solicitar modelo `typesafe/jev-latest` para avaliação
3. Se não → avaliação inline via modelo atual
```

### Devin

```markdown
## Descoberta de Jev

1. Verificar custom subagent profiles em agents/
2. Se existir profile com `model: typesafe/jev-latest`:
   → Delegar avaliação: "avalie usando subagent jev-eval"
3. Se não → avaliação inline
```

### Hermes Agent

```markdown
## Descoberta de Jev

1. Verificar config.yaml → auxiliary.approval
2. Se configurado com `model: typesafe/jev-latest`:
   → Avaliação usará slot approval automaticamente
3. Se não → avaliação inline via modelo principal
```

### Kiro / Copilot / Cline / Aider

```markdown
## Descoberta de Jev

1. Verificar MCP servers configurados
2. Verificar se provider suporta modelo Jev
3. Fallback → avaliação inline
```

## Mapeamento de passos para Jev

|Passo|Primitivo Jev|Perguntas|
|-------|---------------|-----------|
|**Passo 2** (Diagnóstico)|Noul|57 perguntas binárias (padrões de IA)|
|**Passo 6** (Falso positivo)|Noul|2 perguntas (marca humana, gênero formal)|
|**Passo 7** (Verificação)|Noul|4 perguntas (TRAVA FACTUAL, argumento, modalidade, primeira pessoa)|
|**Passo 8** (Avaliação)|Score|4 dimensões ponderadas|

## Formato das perguntas

Use o banco [assets/jev_questions.json](../assets/jev_questions.json). Nunca o modifique. Ele já está no formato que a API Jev espera: monte os requests direto dele.

Contagem real: 67 perguntas, sendo 63 Noul (57 de diagnóstico, 2 de falso positivo, 4 de verificação) e 4 Score. O `metadata` do JSON declara 52 Noul; ignore esse valor.

### Diagnóstico (57 perguntas Noul)

Cada padrão de IA mapeia para uma pergunta binária (P(sim) entre 0-1):

|Categoria|Qtd|Exemplo|
|-----------|-----|---------|
|Composição|9|"O texto anuncia o que vai dizer, diz, e depois resume?"|
|Tom|14|"O texto usa elogios genéricos como 'Ótima pergunta!'?"|
|Linguagem|9|"O texto abusa de vocabulário pomposo típico de IA?"|
|Conteúdo|7|"O texto transforma fatos mundanos em revolução?"|
|Estilo|10|"O texto usa travessão excessivamente como aparte?"|
|PT-BR|8|"O texto usa gerundismo corporativo?"|

### Verificação (4 perguntas Noul)

|Verificação|Crítico|Pergunta|
|-------------|---------|----------|
|TRAVA FACTUAL|✓|"Algum fato foi alterado, adicionado ou removido?"|
|Argumento|✓|"O argumento e posição do autor foram preservados?"|
|Modalidade||"A modalidade foi preservada?"|
|Primeira pessoa||"Opinião ou primeira pessoa foram adicionados?"|

### Avaliação (4 perguntas Score)

|Dimensão|Peso|Níveis|
|----------|------|--------|
|Remoção de padrões|35%|5 níveis (0-20 a 81-100)|
|Naturalidade|30%|5 níveis|
|Consistência de voz|20%|5 níveis|
|Legibilidade|15%|5 níveis|

Se uma pergunta do JSON divergir de uma regra de prosa, vale a regra mais rígida da prosa. Exemplos: `estilo_negrito_excessivo` (mais de 5 trechos em negrito) contra [padroes-estilo.md](padroes-estilo.md), que não define cota; `estilo_travessao_excessivo` (mais de 2 por parágrafo ou 5 por texto) contra [SKILL.md](../SKILL.md), que manda substituir todo aparte.

## Estrutura de request e response

### Request

```json
{
  "state": {
    "texto_fonte": "O texto original...",
    "texto_reescrito": "A candidata..."
  },
  "model": "jev-latest",
  "questions": {
    "composicao_resumos_fractais": {
      "type": "noul",
      "instructions": "O texto anuncia o que vai dizer, diz, e depois resume?",
      "labels": {
        "yes": "Contém resumos fractais",
        "no": "Fluxo direto"
      }
    },
    "score_naturalidade": {
      "type": "score",
      "instructions": "O texto_reescrito soa natural?",
      "levels": ["Muito artificial (0-20)", "...", "Muito natural (81-100)"]
    }
  }
}
```

### Response

```json
{
  "answers": {
    "composicao_resumos_fractais": {
      "type": "noul",
      "noul": 0.23
    },
    "score_naturalidade": {
      "type": "score",
      "score": 3.2,
      "probabilities": {"0": 0.02, "1": 0.05, "2": 0.15, "3": 0.48, "4": 0.30},
      "confidence": 0.78
    }
  },
  "usage": {"input_tokens": 1523, "output_tokens": 0}
}
```

## Interpretação dos resultados

**Noul** (diagnóstico e verificação):

- **P(sim) ≥ 0.5**: padrão detectado / violação detectada.
- **P(sim) < 0.5**: padrão ausente / verificação passou.

**Score** (avaliação):

- Audite nos dois sentidos antes de avaliar estilo. Qualquer violação invalida a candidata.
- **Pontuação final** = Σ(dimensão × peso), somente quando solicitada ou quando houver `limiar`. Sem pontuação, `limiar`, `pontuacao` e `convergiu` ficam `null`.
- **Convergiu**: pontuação ≥ limiar (padrão: 80).

**Decisões:**

|Resultado|Ação|
|-----------|------|
|TRAVA FACTUAL violada|Descartar candidata, retornar texto_fonte|
|Argumento alterado|Descartar candidata|
|Pontuação < limiar|Iterar ou retornar melhor_resultado|
|Pontuação ≥ limiar e trava semântica intacta|Convergiu, retornar candidata|

## Referências externas

- [TypeSafe AI Docs](https://docs.typesafe.ai)
- [Jev API Reference](https://docs.typesafe.ai/api)
- [OpenRouter - Jev](https://openrouter.ai/typesafe/jev-latest)
