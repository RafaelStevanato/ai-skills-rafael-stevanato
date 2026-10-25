---
name: gemini
description: Gera ou edita imagem com o Nano Banana (modelos de imagem do Gemini, do Google) a partir do Claude Code no Windows, pela API REST do Google AI Studio, lendo a chave da variável GEMINI_API_KEY. Traz o script pronto, então não precisa investigar endpoint, ID de modelo, formato do corpo nem SDK. Use sempre que o pedido citar Nano Banana, Nano Banana Pro, Nano Banana 2, Gemini imagem, gemini-image, "gera no Gemini", "imagem pelo Google", AI Studio imagem, ou pedir foto, thumbnail, capa, banner, mockup, ilustração, infográfico ou edição feitos pelo modelo de imagem do Google, inclusive editar ou variar uma imagem existente usando-a como referência. Pedido que cita GPT Image, OpenAI ou Codex vai para a skill gpt-image.
---

# Nano Banana (Gemini) pela API do Google AI Studio

## Caminho fixo
- Use só o script desta skill: `scripts/gerar-imagem.mjs`.
- Não use SDK do Google, `curl` nem outro script para gerar imagem.
- Não use Imagen (`imagen-*`): a Google desligou esses modelos.
- Não procure a chave nem peça que o usuário a cole no chat. O script lê `GEMINI_API_KEY` do processo e, se estiver vazia, da variável de usuário do Windows.
- Nunca escreva a chave em prompt, comando, log ou arquivo.
- Se o pedido citar GPT Image, OpenAI ou Codex, use a skill `gpt-image`.

## Passo a passo
1. Grave o prompt num arquivo UTF-8 ao lado da saída: `<nome>.prompt.txt`.
2. Rode com a ferramenta Bash, em segundo plano (`run_in_background: true`):
   `node "<pasta desta skill>/scripts/gerar-imagem.mjs" "<nome>.prompt.txt" "<nome>.png" [referencia1.png ...]`
3. Espere o aviso de fim (de segundos a alguns minutos). Não fique lendo o log.
4. Leia o código de saída:
   - `0`: gerou. A última linha é o caminho final. A extensão vira `.jpg` ou `.webp` se a API devolver esse formato.
   - `1`: falhou. Veja o fim do log: status HTTP e mensagem da API, ou o motivo do bloqueio e o texto do modelo.
   - `2`: uso errado (argumento, prompt ou referência faltando, extensão inválida, sem `GEMINI_API_KEY`).
   - `3`: limite, cota ou crédito da API (HTTP 429 ou 402). A última linha diz quando volta. Diga ao usuário e pare.
5. Abra a imagem com Read e confira assunto, texto e proporção.
6. Corrija uma coisa por vez no prompt e gere de novo com nome versionado (`<nome>-v2.png`).

## Prompt
Use só as linhas que ajudam:
```text
Use case: <photorealistic-natural | product-mockup | ui-mockup | infographic-diagram | ads-marketing | logo-brand | illustration-story | stylized-concept>
Asset type: <onde a imagem vai ser usada>
Primary request: <pedido principal>
Input images: <Imagem 1: papel; Imagem 2: papel>
Subject: <assunto>
Style/medium: <foto, ilustração, 3D>
Composition/framing: <enquadramento e ângulo, ex.: plano aberto, câmera baixa>
Lighting/mood: <luz e clima>
Color palette: <cores>
Text (verbatim): "<texto exato>"
Constraints: <o que manter>
Avoid: <o que evitar>
```
- Não escreva a proporção no prompt. Use a variável `GEMINI_IMAGE_PROPORCAO` (veja "Modelo e tamanho").
- Escreva o prompt em português (pt-BR) ou inglês. Os dois idiomas têm bom desempenho.
- Para texto na imagem, decida o texto antes e copie entre aspas, letra por letra.
- Descreva o que quer, não o que não quer ("rua deserta", não "sem carros"). Use `Avoid` só para o que não tem inverso.
- O modelo não gera fundo transparente. Peça fundo liso de uma cor e recorte depois.
- Preserve os termos literais do usuário entre aspas.

## Editar ou variar uma imagem
- Passe a imagem como referência no fim do comando (`.png`, `.jpg`, `.jpeg` ou `.webp`).
- A primeira referência é a "Imagem 1" do prompt.
- Escreva no prompt: "Edite a Imagem 1: mude só X; mantenha Y igual."
- Deixe `GEMINI_IMAGE_PROPORCAO` vazia: sem ela, a saída segue a proporção da referência.
- Para iterar, passe a saída anterior como "Imagem 1" e descreva só a mudança.
- Use no máximo 14 referências. O padrão segura bem 4 pessoas e 10 objetos. O Pro segura 5 pessoas e 6 objetos.
- Nunca sobrescreva o original. Salve como `<nome>-editado.png`.

## Várias imagens
- Rode uma chamada por imagem, cada uma com saída própria. O script grava só a primeira imagem da resposta.
- Rode no máximo 2 em paralelo, para não estourar a cota por minuto da chave.

## Modelo e tamanho
- O padrão é `gemini-nano-banana-2.1` (Nano Banana 2.1, linha flash: rápido e barato).
- Use o Pro (`gemini-3-pro-image`, Nano Banana Pro) para texto legível na imagem, infográfico e qualidade máxima.
- O padrão também renderiza texto curto. Se o texto sair errado, repita no Pro.
- Preço por imagem em out/2026: padrão US$ 0,0336 (1K), 0,0504 (2K), 0,113 (4K). Pro US$ 0,134 (1K e 2K), 0,24 (4K).
- O Pro custa mais: cerca de 4 vezes o padrão em 1K. Use o Pro só quando o caso pedir.
- Troque o modelo só numa tarefa: `GEMINI_IMAGE_MODELO=gemini-3-pro-image node ...`.
- Defina a proporção: `GEMINI_IMAGE_PROPORCAO=16:9`. Sem a variável, o modelo decide (ou segue a referência). Sem referência, sai 1:1.
- Defina o tamanho: `GEMINI_IMAGE_TAMANHO=2K`. Sem a variável, sai 1K. Escreva o K maiúsculo.
- Padrão: proporções 1:1, 1:4, 1:8, 2:3, 3:2, 3:4, 4:1, 4:3, 4:5, 5:4, 8:1, 9:16, 16:9, 21:9. Tamanhos 1K, 2K, 4K.
- Pro: proporções 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9. Tamanhos 1K, 2K, 4K.
- `gemini-3.1-flash-lite-image`: o mais rápido, só 1K, fraco com várias referências.
- `gemini-3.1-flash-image`: obsoleto desde out/2026, aceita também o tamanho 512.
- `gemini-2.5-flash-image`: legado, sem faixas de tamanho. O script ignora `GEMINI_IMAGE_TAMANHO` nele.
- Os IDs mudam. Se a API disser que o modelo não existe, confira `https://ai.google.dev/gemini-api/docs/models`.

## Se falhar
- Código 2 com "GEMINI_API_KEY não encontrada": peça ao usuário para rodar `setx GEMINI_API_KEY "sua-chave"` num terminal. A chave sai do Google AI Studio. O app não precisa reiniciar.
- Código 3 (HTTP 429): diga quando volta e pare. A cota diária zera à meia-noite do horário do Pacífico.
- Código 3 com "prepayment credits are depleted" (HTTP 402): os créditos pré-pagos acabaram e não voltam sozinhos. Peça ao usuário para adicionar créditos ou ligar a recarga automática no Google AI Studio.
- Código 3 sem horário e com a mensagem citando cota ou plano: a chave provavelmente está sem faturamento, porque os modelos de imagem não têm camada gratuita. Peça ao usuário para vincular uma conta de faturamento do Google Cloud ao projeto da chave.
- Código 1 com "API key not valid": a chave está errada ou revogada. Peça ao usuário para conferir `GEMINI_API_KEY`.
- Código 1 com `blockReason` ou `finishReason` (`SAFETY`, `PROHIBITED_CONTENT`, `IMAGE_SAFETY`, `IMAGE_PROHIBITED_CONTENT`, `IMAGE_OTHER`, `NO_IMAGE`): o filtro do Google bloqueou o pedido. Tire do prompt o trecho sensível e rode mais uma vez. Se bloquear de novo, diga o motivo ao usuário e pare.
- Código 1 com texto do modelo e sem imagem: o modelo respondeu em texto. Comece o prompt com "Gere uma imagem de ..." e rode de novo.
- Código 1 com HTTP 500 ou 503: o serviço está sobrecarregado. Espere 1 minuto e rode mais uma vez.
- Código 1 com HTTP 404 e "models/...": o ID do modelo não existe mais. Veja "Modelo e tamanho".
- Código 1 com "não respondeu em 5 minutos": rode mais uma vez. Se repetir, baixe o tamanho.

## Entrega
- Diga o caminho final da imagem, o modelo usado e o arquivo do prompt usado.
