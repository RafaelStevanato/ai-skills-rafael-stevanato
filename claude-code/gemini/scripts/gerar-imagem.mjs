// Gera ou edita uma imagem pelo Nano Banana (modelos de imagem do Gemini) na API REST do Google AI Studio, com a chave de GEMINI_API_KEY.
// Uso: node gerar-imagem.mjs <prompt.txt> <saida.png> [referencia ...]
// As referências vão depois do texto, na ordem: a primeira é a "Imagem 1" do prompt. Aceita .png, .jpg, .jpeg e .webp.
// Ajustes por variável de ambiente: GEMINI_IMAGE_MODELO (ID do modelo), GEMINI_IMAGE_PROPORCAO (ex.: 16:9) e GEMINI_IMAGE_TAMANHO (ex.: 2K).
// Códigos: 0 gerou (a última linha é o caminho), 1 falhou, 2 uso errado, 3 limite, cota ou crédito da API (a última linha diz quando volta).
import { spawnSync } from 'node:child_process'
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs'
import { dirname, extname, join, parse, resolve } from 'node:path'

const mimeByExtension = { '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp' }

// motivo: process.exit() depois de um fetch derruba o Node no Windows (assert do libuv e código de saída errado), então main devolve o código e o processo termina sozinho.
async function main() {
  const [promptFile, outputArg, ...referenceArgs] = process.argv.slice(2)
  if (!promptFile || !outputArg) {
    console.error('Uso: node gerar-imagem.mjs <prompt.txt> <saida.png> [referencia ...]')
    return 2
  }
  if (!existsSync(promptFile)) {
    console.error(`Prompt não encontrado: ${promptFile}`)
    return 2
  }
  const prompt = readFileSync(promptFile, 'utf8').trim()
  if (!prompt) {
    console.error(`Prompt vazio: ${promptFile}`)
    return 2
  }
  const output = resolve(outputArg)
  const references = referenceArgs.map((path) => resolve(path))
  const missing = references.find((path) => !existsSync(path))
  if (missing) {
    console.error(`Referência não encontrada: ${missing}`)
    return 2
  }
  const unsupported = references.find((path) => !mimeByExtension[extname(path).toLowerCase()])
  if (unsupported) {
    console.error(`Referência com extensão não aceita (use .png, .jpg, .jpeg ou .webp): ${unsupported}`)
    return 2
  }

  // motivo: o setx grava a variável só no registro e não chega a processos já abertos, então ler a variável de usuário evita reiniciar o app.
  const key = (process.env.GEMINI_API_KEY ?? '').trim() || (spawnSync('powershell', ['-NoProfile', '-Command', "[Environment]::GetEnvironmentVariable('GEMINI_API_KEY','User')"], { encoding: 'utf8' }).stdout ?? '').trim()
  if (!key) {
    console.error('GEMINI_API_KEY não encontrada: rode setx GEMINI_API_KEY "sua-chave" num terminal.')
    return 2
  }
  // motivo: a chave não pode ir para o log, e a API às vezes ecoa trechos do pedido (até a imagem em base64) na mensagem de erro.
  const say = (text) => console.error(String(text).replaceAll(key, '***').slice(0, 1500))

  const model = process.env.GEMINI_IMAGE_MODELO?.trim() || 'gemini-nano-banana-2.1'
  const aspectRatio = process.env.GEMINI_IMAGE_PROPORCAO?.trim() || undefined
  let imageSize = process.env.GEMINI_IMAGE_TAMANHO?.trim().toUpperCase() || undefined
  // motivo: o gemini-2.5-flash-image tem uma resolução só por proporção, e a doc manda apenas aspectRatio nele.
  if (imageSize && model.includes('2.5-flash-image')) {
    console.error(`Aviso: o ${model} não aceita GEMINI_IMAGE_TAMANHO, então o tamanho foi ignorado.`)
    imageSize = undefined
  }
  const generationConfig = { responseModalities: ['IMAGE'] }
  if (aspectRatio || imageSize) generationConfig.imageConfig = { aspectRatio, imageSize }
  const inputParts = [{ text: prompt }, ...references.map((path) => ({ inline_data: { mime_type: mimeByExtension[extname(path).toLowerCase()], data: readFileSync(path).toString('base64') } }))]

  let status
  let raw
  try {
    const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`, {
      method: 'POST',
      headers: { 'x-goog-api-key': key, 'content-type': 'application/json' },
      body: JSON.stringify({ contents: [{ parts: inputParts }], generationConfig }),
      signal: AbortSignal.timeout(5 * 60 * 1000),
    })
    status = response.status
    raw = await response.text()
  } catch (error) {
    say(error.name === 'TimeoutError' ? 'A API não respondeu em 5 minutos.' : `Falha de rede ao chamar a API: ${error.cause?.code ?? error.message}`)
    return 1
  }
  // motivo: erro de proxy ou de gateway pode vir em HTML, e aí a mensagem é o texto cru.
  let data = {}
  try { data = JSON.parse(raw) ?? {} } catch {}

  if (status < 200 || status > 299) {
    const error = data.error
    const detail = `HTTP ${status}${error?.status ? ` ${error.status}` : ''}: ${error?.message ?? raw}`
    if (status === 429 || status === 402 || error?.status === 'RESOURCE_EXHAUSTED') {
      say(`Limite, cota ou crédito do Gemini (${detail})`)
      const wait = parseFloat(error?.details?.find((item) => item['@type']?.endsWith('RetryInfo'))?.retryDelay)
      let when = 'A API não informou quando volta (a cota diária zera à meia-noite do horário do Pacífico).'
      if (wait > 0) when = `Volta em cerca de ${Math.ceil(wait)} s (por volta das ${new Date(Date.now() + wait * 1000).toLocaleTimeString('pt-BR')}).`
      else if (status === 402) when = 'Não volta sozinho: os créditos pré-pagos acabaram. Adicione créditos ou ligue a recarga automática no Google AI Studio.'
      console.error(when)
      return 3
    }
    say(`Erro da API (${detail})`)
    return 1
  }

  const candidate = data.candidates?.[0]
  const outputParts = candidate?.content?.parts ?? []
  // motivo: com o thinking ligado a resposta pode trazer imagens de rascunho marcadas com thought, e o arquivo tem que ser a imagem final.
  const image = outputParts.find((part) => part.inlineData?.mimeType?.startsWith('image/') && !part.thought)?.inlineData
  if (!image) {
    const reasons = [data.promptFeedback?.blockReason && `promptFeedback.blockReason=${data.promptFeedback.blockReason}`, candidate?.finishReason && `finishReason=${candidate.finishReason}`, candidate?.finishMessage && `finishMessage=${candidate.finishMessage}`].filter(Boolean)
    const text = outputParts.filter((part) => part.text && !part.thought).map((part) => part.text).join('\n')
    say(`A API respondeu sem imagem (HTTP ${status})${reasons.length ? `: ${reasons.join(', ')}` : ''}`)
    if (text) say(`Texto do modelo: ${text}`)
    return 1
  }

  const mimeType = image.mimeType.toLowerCase()
  const extensions = { 'image/png': ['.png'], 'image/jpeg': ['.jpg', '.jpeg'], 'image/webp': ['.webp'] }[mimeType] ?? [`.${mimeType.split('/')[1]}`]
  // motivo: o modelo escolhe o formato (PNG ou JPEG), e arquivo com extensão que não bate com os bytes não abre em alguns programas.
  const final = extensions.includes(extname(output).toLowerCase()) ? output : join(dirname(output), parse(output).name + extensions[0])
  mkdirSync(dirname(final), { recursive: true })
  writeFileSync(final, Buffer.from(image.data, 'base64'))
  if (final !== output) console.error(`Aviso: a API devolveu ${mimeType}, então a extensão virou ${extensions[0]}.`)
  console.log(final)
  return 0
}

process.exitCode = await main()
