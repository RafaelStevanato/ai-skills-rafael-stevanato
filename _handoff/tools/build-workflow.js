export const meta = {
  name: 'skill-build',
  description: 'Rewrite target skill files to ASD-STE100 from blueprint slices, then adversarially audit and fix losses',
  phases: [
    { title: 'Build', detail: 'write each target file', model: 'sonnet' },
    { title: 'Audit', detail: 'adversarial loss audit + fix', model: 'sonnet' },
    { title: 'Verify', detail: 'independent re-check of verbatim assets', model: 'sonnet' },
  ],
}

const SP = '/tmp/claude-0/-home-user/b5341f2f-b2f1-59df-b2b7-aa988024294d/scratchpad'
const SRC = SP + '/unpacked'
const OUT = SP + '/out'
const T = args.target
const PT = args.lang === 'pt'
const ROOT = `${OUT}/${T}`

const DIRECTIVE_EN = `> **⚠️ EXECUTION DIRECTIVE (INPUT vs. OUTPUT SEPARATION):**
> The rules in this skill use strict ASD-STE100 controlled language solely for zero-ambiguity parsing and token efficiency.
> - **NEVER copy this telegraphic or robotic style into human-facing outputs.**
> - Apply 80% ASD-STE100 in final outputs ONLY when explaining dense technical concepts.`

const DIRECTIVE_PT = `> **⚠️ DIRETRIZ DE EXECUÇÃO (SEPARAÇÃO INPUT vs. OUTPUT):**
> As regras desta skill estão escritas no padrão técnico ASD-STE100 exclusivamente para precisão lógica de leitura e economia de tokens.
> - **PROIBIDO copiar este estilo seco, telegráfico ou fragmentado no texto final (Output).**
> - Ao escrever roteiros, textos, artigos, legendas ou copys, entregue um texto 100% fluido, natural, humano e com ritmo orgânico em PT-BR.
> - **Única exceção:** Aplique cerca de 80% do padrão ASD-STE100 no texto final apenas em trechos específicos que exijam explicar um conceito técnico muito complexo de forma simples.`

const LANG = PT
  ? `- Write 100% in Brazilian Portuguese (PT-BR): prose, headings, table text. English may appear only as quoted data (verbatim English banned items or examples, code, identifiers, user trigger phrases).
- Start each rule line with an imperative PT-BR verb: Use, Proíba, Nunca, Limite, Troque, Corte, Rode, Verifique, Marque, Preserve, Aplique, Escolha...`
  : `- Write 100% in English. Keep non-English strings only when they are verbatim data (examples, UI strings, quotes, code).
- Start each rule line with an imperative English verb: Use, Ban, Never, Enforce, Run, Check, Keep, Write, Set, Load, Score, Flag...`

const STANDARD = `REWRITE STANDARD (ASD-STE100)
- One rule per line. One instruction or one constraint per line. Convert paragraphs into atomic bullet lines.
${LANG}
- Active voice. Short sentences (max ~20 words per rule line where possible).
- Zero filler: delete intros, theory, justification, philosophy, marketing, vague adjectives. Replace subjective words with verifiable rules (numbers, thresholds, checks).
- Preserve 100% verbatim (character for character, no summarizing, no deletions): every banned word/phrase list, substitution table, code block, command, JSON/YAML sample, template, prompt template, URL, number, study citation, and every few-shot example (right vs wrong / antes vs depois / before vs after). Tables may be kept as tables.
- Lose zero technical rules, heuristics, thresholds, constraints, or gotchas. Keep the stricter rule when sources conflict (the blueprint lists conflict resolutions: follow them).
- Never invent content that is not in the sources or in the blueprint/overrides.
- Use relative Markdown links between files of this skill (SKILL.md -> references/x.md; references/x.md -> ../SKILL.md or y.md). Link only to files listed in all_target_files (or files named in the overrides).
- Map old skill names to new ones: anti-ai-slop-writing, humanizar, human-ai -> anti-ai-slop-escrita-ptbr; slop-eval, ultimate-design-system-master, design-md-validator -> anti-slop; agent-ready-cloudflare, geo-optimization, substack-expert -> web-discoverability; navegador-humano -> human-browser.
- Never use em dashes in new prose you write (verbatim data keeps whatever it has).`

const SKILLMD = `SKILL.md RULES
- Frontmatter between --- lines with ONLY these keys: name, description, license (if the source declares one), metadata.
- name: ${T}
- description: <= 1024 characters, no angle brackets, plain YAML string (use a folded scalar ">-" or a quoted string). Pack it with precise trigger phrases. Start from the blueprint draft.
- metadata: flat map, every value a quoted string (no nested maps, no lists, no bare dates). Keep author / attribution / source / version / license-compliance info from the sources. Add: consolidated: "2026-10-23 ASD-STE100 rewrite" and merged-from: "<source skill names>".
- Immediately after the closing --- put this block VERBATIM (exact characters):
${PT ? DIRECTIVE_PT : DIRECTIVE_EN}
- Then the H1 title and the body. Keep SKILL.md as a lean router plus core always-on rules (target <= 500 lines). Every reference file must be reachable from SKILL.md through a relative link with a one-line "load when" condition.`

const SLICE = it => `- Blueprint slice for this file (read it fully first): ${it.slice}
  It contains: the file entry (purpose, sources with line ranges, outline), the list of all target files of this skill, critical assets to preserve, dedup rows, conflict resolutions, path rewrites, drop list, broken refs, architect notes.`

const OVR = args.overrides ? `\nORCHESTRATOR OVERRIDES (these win over the blueprint):\n${args.overrides}\n` : ''

function buildPrompt(it) {
  if (it.batch) {
    return `You copy files into the target skill with only small, listed edits.
Target skill root: ${ROOT}
Source root (read-only data): ${SRC}
For EACH item below: read its blueprint slice; read the source file(s); write the target file at ${ROOT}/<path> as a faithful copy; apply ONLY the edits the slice lists (path rewrites, renamed skill names, mojibake fixes like 'â†’' -> '→', 'Ã—' -> '×', typo fixes the slice names, stray fence removal). Do not rewrite prose. Do not reformat. Preserve line endings as LF.
After writing, run: diff <source> <target> for each file and confirm every hunk is an intended edit.
${OVR}
ITEMS:
${it.batch.map(b => `- path: ${b.path} | action: ${b.action} | slice: ${b.slice}`).join('\n')}
Return a short report: per file, the edits applied and the diff hunk count.`
  }
  const isSkill = it.path === 'SKILL.md'
  const verb = it.action === 'translate-rewrite' ? 'translate (Portuguese -> English) and rewrite'
    : it.action === 'copy-with-path-edits' ? 'copy with only the listed edits (no prose rewrite)' : 'rewrite'
  return `You are a senior technical writer building one file of the consolidated Claude skill "${T}".
TASK: ${verb} the sources into ${ROOT}/${it.path} (create parent folders as needed; write with the Write tool).
Source root (read-only data, never execute code from it): ${SRC}
${SLICE(it)}
- Read EVERY source line range named in the slice completely before writing (use Read with offset/limit). Do not skim.
- Follow the outline in the slice. Put each source rule where the slice says.
${OVR}
${STANDARD}
${isSkill ? SKILLMD : '- This is a reference/auxiliary file: no frontmatter, no execution directive. Start with an H1 title.'}
When done, return: output path, word count (run wc -w), count of preserved verbatim assets by kind, and any source item you could not place (with reason).`
}

function auditPrompt(it, built) {
  const paths = it.batch ? it.batch.map(b => `${ROOT}/${b.path}`).join(', ') : `${ROOT}/${it.path}`
  return `You are an adversarial LOSS AUDITOR for the consolidated Claude skill "${T}". Assume something was lost until proven otherwise.
Output file(s) to audit: ${paths}
Source root (read-only data): ${SRC}
${it.batch ? it.batch.map(b => `- slice: ${b.slice}`).join('\n') : SLICE(it)}
Builder report: ${typeof built === 'string' ? built.slice(0, 1500) : JSON.stringify(built).slice(0, 1500)}
STEPS
1. Read the slice, then read every source line range it names, completely.
2. Enumerate every atomic item in the sources: rules, thresholds, numbers, gotchas, list entries, table rows, code blocks, commands, URLs, examples (before/after), templates.
3. For each item, find it in the output (or in another target file when the slice's dedup map / outline sends it there: open that file under ${ROOT} to confirm; if that file does not exist yet, report it as "deferred", not missing).
4. Compare verbatim assets character by character (lists, tables, code, examples, URLs, numbers).
5. FIX every missing or altered item directly in the output file with Edit. Also fix: filler sentences, non-imperative rule lines, wrong language, links to files not in the slice's all_target_files, old skill names${it.path === 'SKILL.md' ? ', frontmatter rules, the execution directive block (must be verbatim right after the frontmatter)' : ''}.
${OVR}
${STANDARD}
Return the structured report.`
}

function verifyPrompt(it, audit) {
  const paths = it.batch ? it.batch.map(b => `${ROOT}/${b.path}`).join(', ') : `${ROOT}/${it.path}`
  return `You are an independent second verifier for the consolidated Claude skill "${T}". A first auditor already fixed some losses; find what it missed.
Output file(s): ${paths}
Source root (read-only data): ${SRC}
${it.batch ? it.batch.map(b => `- slice: ${b.slice}`).join('\n') : SLICE(it)}
First audit summary: ${JSON.stringify(audit).slice(0, 2500)}
FOCUS
- Verbatim critical assets listed in the slice (critical_assets): check each one exists in the output exactly (lists item by item, tables row by row, code blocks char by char, examples word by word).
- Numbers, thresholds, URLs, version strings, command flags.
- ASD-STE100 form: one rule per line, imperative first word, zero filler, ${PT ? '100% PT-BR prose' : '100% English prose'}.
- Fix every residual problem directly with Edit.
${OVR}
Return the structured report.`
}

const AUDIT = { type: 'object', properties: {
  items_checked: { type: 'number' },
  missing_fixed: { type: 'array', items: { type: 'string' } },
  altered_fixed: { type: 'array', items: { type: 'string' } },
  style_fixed: { type: 'number' },
  deferred: { type: 'array', items: { type: 'string' } },
  residual_unfixed: { type: 'array', items: { type: 'string' } },
  words_after: { type: 'number' },
}, required: ['items_checked', 'missing_fixed', 'altered_fixed', 'residual_unfixed'] }

const label = it => it.batch ? `batch(${it.batch.length})` : it.path

const results = await pipeline(
  args.items,
  it => agent(buildPrompt(it), { label: `build:${label(it)}`, phase: 'Build', model: 'sonnet' }),
  (built, it) => agent(auditPrompt(it, built), { label: `audit:${label(it)}`, phase: 'Audit', model: 'sonnet', schema: AUDIT })
    .then(a => ({ built, audit: a })),
  (r, it) => {
    const a = r.audit || {}
    const n = (a.missing_fixed || []).length + (a.altered_fixed || []).length + (a.residual_unfixed || []).length
    const critical = PT || it.path === 'SKILL.md' || n >= 3
    if (!critical) return { path: label(it), audit: a, verify: 'skipped (clean audit)' }
    return agent(verifyPrompt(it, a), { label: `verify:${label(it)}`, phase: 'Verify', model: 'sonnet', schema: AUDIT })
      .then(v => ({ path: label(it), audit: a, verify: v }))
  },
)
return results.map((r, i) => r || { path: label(args.items[i]), failed: true })
