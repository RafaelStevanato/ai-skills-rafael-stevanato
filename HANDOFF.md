# HANDOFF: finish the ASD-STE100 skill pack

Read this file fully before you act. It is the only context you get.

## Mission

- Finish the consolidation of 13 Claude skills into 7 skills under `skills/`.
- Rewrite every rule file in ASD-STE100 controlled language: 1 rule per line, imperative verb first, zero filler.
- Preserve verbatim: banned word/phrase lists, substitution tables, code blocks, commands, JSON/YAML, templates, URLs, numbers, few-shot examples (right vs wrong / antes vs depois).
- Lose zero technical rules. Keep the stricter rule on conflicts (each blueprint lists the resolutions).
- Write all skills in English, except `anti-ai-slop-escrita-ptbr`: write it 100% in PT-BR (English allowed only as quoted data).
- Deliver `skills-claude-asd-ste100.zip` (one folder per skill, `SKILL.md` at each folder root) and a before/after metrics table.

## Repository map

- `skills/<name>/`: the 7 target skills (work here).
- `_handoff/source/<old-skill>/`: original text sources, read-only. Images are not copied here; the 44 kept images are already in `skills/revenue-centric-design/assets/`.
- `_handoff/blueprints/<target>.json`: architect plan per target skill. Use `target_files[].sources` (source file + line ranges), `outline`, `critical_assets`, `dedup_map`, `conflicts`, `path_rewrites`, `drop_list`, `frontmatter_description_draft`.
- `_handoff/tools/validate.py`: pack validator. Run: `python3 -I _handoff/tools/validate.py _handoff/source skills`.
- `_handoff/tools/metrics.py`: size and word metrics. Run: `python3 -I _handoff/tools/metrics.py skills`.
- `_handoff/tools/build-workflow.js` and `slice.py`: the original build automation. Edit their absolute `/tmp/...` paths before reuse, or work file by file by hand.

## Target skills (old -> new)

| New skill | Merged from |
|---|---|
| `anti-ai-slop-escrita-ptbr` | anti-ai-slop-writing + humanizar |
| `anti-slop` | anti-slop + slop-eval + ultimate-design-system-master + design-md-validator |
| `web-discoverability` | agent-ready-cloudflare + geo-optimization + substack-expert |
| `revenue-centric-design` | revenue-centric-design |
| `motion-ad` | motion-ad |
| `human-browser` | navegador-humano (translated PT -> EN) |
| `skill-evaluation` | skill-evaluation |

## Status legend

- DONE: rewritten and audited against sources.
- BUILT: rewritten, not audited. Audit it.
- PLACEHOLDER: original content copied unchanged, with a `PENDING` / `PENDENTE` banner on line 1. Rewrite it from the blueprint, then delete the banner.
- COPY: byte-identical or listed-edit copy. Do not rewrite.

## Per-file status

### anti-ai-slop-escrita-ptbr (PT-BR)

| File | Status | Action |
|---|---|---|
| SKILL.md | DONE | Cut to <= 500 lines (now 502). |
| references/perfis-voz.md | BUILT | Audit. |
| references/padroes-composicao.md | BUILT | Audit. |
| references/padroes-estilo.md | BUILT | Audit. |
| references/palavras-banidas.md | DONE (new) | Researched PT-BR banned-word checklist written by the orchestrator. Keep. Optional: proofread for false positives. |
| references/padroes-conteudo-tom.md | PLACEHOLDER | Merge-rewrite padroes-conteudo + padroes-tom per blueprint. |
| references/padroes-linguagem-ptbr.md | PLACEHOLDER | Merge-rewrite padroes-linguagem + padroes-exclusivos-pt-br per blueprint. |
| references/padroes-portugues-simplificado.md | PLACEHOLDER | Rewrite per blueprint. |
| references/auditoria-entrega.md | PLACEHOLDER | Merge-rewrite material-autoral + humanizar SKILL.md L524-537, L646-802, L814-831. |
| references/jev-integration.md | PLACEHOLDER | Rewrite; delete the `scripts/jev_eval.py` line (file never existed). |
| references/modo-ingles.md | PLACEHOLDER (English) | Rewrite as PT-BR instructions for English-language texts. Keep the English banned items and English examples verbatim as quoted data. Blueprint entry: `references/vocabulario-banido.md` (renamed; its section A now lives in palavras-banidas.md). |
| assets/jev_questions.json | COPY | Keep. |

### anti-slop

| File | Status | Action |
|---|---|---|
| SKILL.md | DONE | Keep. |
| references/tells.md, evaluate-procedure.md, evaluate-scoring.md | BUILT (audit interrupted) | Audit. |
| references/premium-markers.md, contexts.md, evaluate-exclusions-qa.md, validate-design-md.md, jev-integration.md | BUILT | Audit. |
| references/slop-report-template.md, system-briefing.md, design-md-lint-rules.md, design-md-token-schema.md, scripts/score.py, scripts/jev_questions.json | COPY (listed edits) | Diff against source; confirm only the blueprint `path_rewrites` edits exist. |
| references/system-roles/role-01..10-*.md | COPY | Mojibake and typo fixes applied. Keep verbatim. |

### web-discoverability

| File | Status | Action |
|---|---|---|
| SKILL.md, references/implement-bot-access.md, references/implement-api-auth-mcp.md | DONE | Keep. |
| references/scan-api.md, implement-commerce.md, newsletter.md | BUILT (audit interrupted) | Audit. |
| references/fix-prompts.md, implement-discoverability-content.md | BUILT | Audit. |
| references/geo.md | PLACEHOLDER | Merge-rewrite geo-optimization SKILL.md + guiding-principles per blueprint. |

### revenue-centric-design

| File | Status | Action |
|---|---|---|
| SKILL.md | DONE | Keep. |
| references/*.md (13 files) | BUILT | Audit. `metrics-and-experimentation.md` and `product-strategy-and-features.md` builds were cut off: check them against source end to end. |
| references/revenue-centric-design.md | PLACEHOLDER | Rewrite per blueprint. |
| LICENSE, scripts/*.py, assets/*.jpg | COPY | Keep. LICENSE must stay verbatim (license clause 3). |

### motion-ad

- DONE. SKILL.md and references/template-map.md audited. assets/ and scripts/ are byte-identical copies.

### human-browser

| File | Status | Action |
|---|---|---|
| SKILL.md | DONE | Keep. |
| references/snippets.md | BUILT | Audit. Keep every code block byte-identical (Portuguese identifiers and regexes are functional). |
| references/sites.md | PLACEHOLDER (Portuguese) | Translate prose to English ASD-STE100; keep code and URLs verbatim. |

### skill-evaluation

- DONE. `references/categories.md` is BUILT: audit it. `references/output-template.md` and `scripts/score.py` are COPY.

## Audit procedure (per BUILT or rewritten file)

1. Open the blueprint entry for the file. Read every source line range it names, completely.
2. List every atomic source item: rule, threshold, number, gotcha, list entry, table row, code block, URL, example.
3. Find each item in the target file, or in the target file the `dedup_map` names.
4. Compare verbatim assets character by character.
5. Fix missing or altered items in place. Remove filler. Make every rule line start with an imperative verb.

## Global pending work (after the per-file work)

1. Compress. The pack now has MORE words than the original (see metrics). Cut repetition, field-label overhead, and duplicate rules until the word count drops below baseline. Never cut verbatim assets.
2. Integrate. Check that every `SKILL.md` router links every reference file with a one-line "load when" condition.
3. Clean old skill names in prose. Keep them only in `metadata.merged-from`.
4. Validate. `validate.py` must report 0 errors. Known false positive: `human-browser/references/snippets.md` regex parsed as a link.
5. Review `code_blocks_missing` in the validator output: anti-slop 6/53, web-discoverability 6/74, motion-ad 2/9, human-browser 3/14, anti-ai-slop-escrita-ptbr 1/20. Restore each block or confirm a blueprint-approved edit.
6. Package. Zip the 7 folders under `skills/` into `skills-claude-asd-ste100.zip`.
7. Report. Fill the metrics table below with the final numbers.

## Every SKILL.md must keep

- Frontmatter keys only: `name`, `description` (<= 1024 chars, no angle brackets), `license`, `metadata` (flat string values).
- The INPUT vs OUTPUT execution directive block right after the frontmatter (English version in 6 skills, PT-BR version in `anti-ai-slop-escrita-ptbr`). Copy it from any existing SKILL.md; never edit its wording.

## Known facts (do not re-investigate)

- `anti-ai-slop-writing` linked `references/banned-words.md`, which never existed in the pack or in the installed skill. `palavras-banidas.md` replaces it.
- Skills `caveman` and `ponytail` (named in the user's preferences) are not in the pack. Do not invent them.
- 30 unreferenced JPGs of revenue-centric-design were dropped; the 44 referenced ones were recompressed (max 1400 px, JPEG q78).
- The user's global preferences call `anti-AI-slop-writing` and `navegador-humano`; tell the user to update them to `anti-ai-slop-escrita-ptbr` and `human-browser`.

## Metrics

| Metric | Original (13 skills) | Now (7 skills, partial) | Final |
|---|---|---|---|
| Skills | 13 | 7 | |
| Total size | 10,015.7 KB | 4,267.5 KB (-57.4%) | |
| Text size | 860.4 KB | 981.7 KB | |
| Images | 9,155.2 KB | 3,285.8 KB | |
| Words (text files, `split()`) | 122,779 | 145,572 (+18.6%) | |
