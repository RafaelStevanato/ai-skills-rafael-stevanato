---
name: gpt-image
description: Gera ou edita imagem com o GPT Image 2 (OpenAI) a partir do Claude Code no Windows, pelo Codex CLI que vem dentro do app Codex da Microsoft Store, usando a conta ChatGPT e sem chave de API. Traz o script pronto, então não precisa investigar caminho, PATH, flags nem API. Use sempre que o pedido citar GPT Image, GPT Image 2, gpt-image-2, "gera no GPT", "imagem pelo Codex", imagegen, ou pedir foto, ícone 3D, thumbnail, capa, banner, mockup, ilustração, textura ou fundo transparente feitos pelo modelo de imagem da OpenAI, inclusive editar ou variar uma imagem existente usando-a como referência.
---

# GPT Image 2 pelo Codex CLI

## Caminho fixo
- Use só o script desta skill: `scripts/gerar-imagem.mjs`.
- Não procure `codex` no PATH. O script acha o `codex.exe` do app sozinho.
- Não use `OPENAI_API_KEY`, SDK da OpenAI nem `scripts/image_gen.py` do Codex.
- Não chame `codex exec` direto para imagem.

## Passo a passo
1. Grave o prompt num arquivo UTF-8 ao lado da saída: `<nome>.prompt.txt`.
2. Rode com a ferramenta Bash, em segundo plano (`run_in_background: true`):
   `node "<pasta desta skill>/scripts/gerar-imagem.mjs" "<nome>.prompt.txt" "<nome>.png" [referencia1.png ...]`
3. Espere o aviso de fim (cerca de 40 s a 2 min). Não fique lendo o log.
4. Leia o código de saída:
   - `0`: gerou. A última linha é o caminho do PNG.
   - `1`: falhou. Veja o fim do log.
   - `2`: uso errado (prompt ou referência não existe).
   - `3`: limite de uso do Codex. Diga ao usuário quando volta e pare.
5. Abra o PNG com Read e confira assunto, texto e proporção.
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
Composition/framing: <proporção e enquadramento, ex.: 1536x1024 paisagem>
Lighting/mood: <luz e clima>
Color palette: <cores>
Text (verbatim): "<texto exato>"
Constraints: <o que manter>
Avoid: <o que evitar>
```
- Escreva a proporção no prompt. O script não tem flag de tamanho.
- Para fundo transparente, escreva "fundo transparente (PNG com alfa)".
- Para texto na imagem, copie o texto entre aspas, letra por letra.
- Preserve os termos literais do usuário entre aspas.

## Editar ou variar uma imagem
- Passe a imagem como referência no fim do comando.
- A primeira referência é a "Imagem 1" do prompt.
- Escreva no prompt: "Edite a Imagem 1: mude só X; mantenha Y igual."
- Nunca sobrescreva o original. Salve como `<nome>-editado.png`.

## Várias imagens
- Rode uma chamada por imagem, cada uma com saída própria.
- Rode no máximo 2 em paralelo, para não estourar o limite do Codex.

## Esforço
- O padrão é esforço alto (`high`).
- Para subir só numa tarefa, prefixe o comando: `GPT_IMAGE_ESFORCO=xhigh node ...`.

## Se falhar
- Código 1 sem PNG na saída: pegue o PNG mais novo em `~/.codex/generated_images/*/` e copie para a saída.
- "Codex CLI não encontrado": peça ao usuário para abrir o app Codex e entrar com a conta ChatGPT.
- Outro caminho do `codex.exe`: defina `CODEX_BIN=<caminho>` antes do comando.

## Entrega
- Diga o caminho final do PNG e o arquivo do prompt usado.
