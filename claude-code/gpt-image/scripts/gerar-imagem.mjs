// Gera uma imagem pelo GPT Image 2 do Codex CLI (app Codex da Microsoft Store, conta ChatGPT), sem chave de API.
// Uso: node gerar-imagem.mjs <prompt.txt> <saida.png> [referencia ...]
// As referências vão anexadas na ordem: a primeira é a "Imagem 1" do prompt.
// Códigos: 0 gerou (a última linha é o caminho), 1 falhou, 2 uso errado, 3 limite de uso do Codex (a última linha diz quando volta).
import { spawn, spawnSync } from 'node:child_process'
import { existsSync, mkdirSync, readFileSync } from 'node:fs'
import { dirname, join, resolve } from 'node:path'

const [promptFile, outputArg, ...referenceArgs] = process.argv.slice(2)
if (!promptFile || !outputArg) {
  console.error('Uso: node gerar-imagem.mjs <prompt.txt> <saida.png> [referencia ...]')
  process.exit(2)
}
if (!existsSync(promptFile)) {
  console.error(`Prompt não encontrado: ${promptFile}`)
  process.exit(2)
}
const output = resolve(outputArg)
const references = referenceArgs.map((path) => resolve(path))
const missing = references.find((path) => !existsSync(path))
if (missing) {
  console.error(`Referência não encontrada: ${missing}`)
  process.exit(2)
}

// motivo: o codex.exe não fica no PATH e a pasta do app muda a cada atualização.
const install = process.env.CODEX_BIN ? '' : spawnSync('powershell', ['-NoProfile', '-Command', "(Get-AppxPackage -Name 'OpenAI.Codex*').InstallLocation"], { encoding: 'utf8' }).stdout.trim()
const codex = process.env.CODEX_BIN || (install && join(install, 'app', 'resources', 'codex.exe'))
if (!existsSync(codex)) {
  console.error('Codex CLI não encontrado: instale o app Codex da Microsoft Store e entre com a conta ChatGPT.')
  process.exit(1)
}

const request = [
  'Gere uma única imagem com a ferramenta de geração de imagem embutida (GPT Image), em qualidade alta, usando exatamente o prompt abaixo.',
  'Não use scripts/image_gen.py nem chave de API.',
  ...(references.length ? [`As ${references.length} imagem(ns) anexada(s) são as referências do prompt, na ordem: a primeira é a Imagem 1.`] : []),
  `Quando terminar, copie o PNG gerado para ${output} e não mexa em mais nenhum arquivo. Responda só com o caminho final.`,
  '',
  '# Prompt da imagem',
  readFileSync(promptFile, 'utf8').trim(),
].join('\n')

// motivo: o config.toml do Codex está em esforço ultra; imagem roda em alto, salvo GPT_IMAGE_ESFORCO.
const effort = process.env.GPT_IMAGE_ESFORCO || 'high'
mkdirSync(dirname(output), { recursive: true })
// motivo: o sandbox só deixa o Codex escrever na pasta da saída.
const args = ['exec', '--skip-git-repo-check', '-s', 'workspace-write', '-C', dirname(output), '-c', `model_reasoning_effort="${effort}"`, ...references.flatMap((path) => ['-i', path]), '--', '-']
// motivo: pedido pela entrada padrão, porque aspas num argumento longo quebram no PowerShell 5.1.
const child = spawn(codex, args, { stdio: ['pipe', 'pipe', 'pipe'] })
let tail = ''
// motivo: o aviso de limite de uso sai no meio de um log longo, então o fim do log fica guardado.
for (const [from, to] of [[child.stdout, process.stdout], [child.stderr, process.stderr]]) from.on('data', (chunk) => { to.write(chunk); tail = `${tail}${chunk}`.slice(-20000) })
child.stdin.end(request)
const status = await new Promise((done) => { child.on('error', () => done(-1)); child.on('close', done) })
if (status !== 0 || !existsSync(output)) {
  const limit = tail.split(/\r?\n/).reverse().find((line) => /usage limit|rate limit|limite de uso/i.test(line))
  if (limit) {
    const when = limit.match(/try again (?:at|in) ([^.!\n]+)/i)?.[1] ?? limit.match(/\b\d{1,2}:\d{2}(?:\s?[AP]M)?\b/i)?.[0]
    console.error(`Limite de uso do Codex: volta ${when ? `em "${when.trim()}"` : 'em horário que o Codex não informou'} (aviso dele: ${limit.trim().slice(0, 200)})`)
    process.exit(3)
  }
  console.error(`A imagem não foi gerada (código ${status}).`)
  process.exit(1)
}
console.log(output)
