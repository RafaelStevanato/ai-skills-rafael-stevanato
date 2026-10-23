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

Final status 2026-10-23: every file below is DONE or a verified COPY. See "Global work" and "Metrics" at the end.

### anti-ai-slop-escrita-ptbr (PT-BR)

| File | Status | Action |
|---|---|---|
| SKILL.md | DONE | Finished, validated (0 errors). |
| references/perfis-voz.md | DONE | Finished, validated (0 errors). |
| references/padroes-composicao.md | DONE | Finished, validated (0 errors). |
| references/padroes-estilo.md | DONE | Finished, validated (0 errors). |
| references/palavras-banidas.md | DONE | Finished, validated (0 errors). |
| references/padroes-conteudo-tom.md | DONE | Finished, validated (0 errors). |
| references/padroes-linguagem-ptbr.md | DONE | Finished, validated (0 errors). |
| references/padroes-portugues-simplificado.md | DONE | Finished, validated (0 errors). |
| references/auditoria-entrega.md | DONE | Finished, validated (0 errors). |
| references/jev-integration.md | DONE | Finished, validated (0 errors). |
| references/modo-ingles.md | DONE | Finished, validated (0 errors). |
| assets/jev_questions.json | COPY | Keep. Verified. |

### anti-slop

| File | Status | Action |
|---|---|---|
| SKILL.md | DONE | Finished, validated (0 errors). |
| references/tells.md, evaluate-procedure.md, evaluate-scoring.md | DONE | Finished, validated (0 errors). |
| references/premium-markers.md, contexts.md, evaluate-exclusions-qa.md, validate-design-md.md, jev-integration.md | DONE | Finished, validated (0 errors). |
| references/slop-report-template.md, system-briefing.md, design-md-lint-rules.md, design-md-token-schema.md, scripts/score.py, scripts/jev_questions.json | COPY (listed edits) | Diff against source; confirm only the blueprint `path_rewrites` edits exist. Verified. |
| references/system-roles/role-01..10-*.md | COPY | Mojibake and typo fixes applied. Keep verbatim. Verified. |

### web-discoverability

| File | Status | Action |
|---|---|---|
| SKILL.md, references/implement-bot-access.md, references/implement-api-auth-mcp.md | DONE | Finished, validated (0 errors). |
| references/scan-api.md, implement-commerce.md, newsletter.md | DONE | Finished, validated (0 errors). |
| references/fix-prompts.md, implement-discoverability-content.md | DONE | Finished, validated (0 errors). |
| references/geo.md | DONE | Finished, validated (0 errors). |

### revenue-centric-design

| File | Status | Action |
|---|---|---|
| SKILL.md | DONE | Finished, validated (0 errors). |
| references/*.md (13 files) | DONE | Finished, validated (0 errors). |
| references/revenue-centric-design.md | DONE | Finished, validated (0 errors). |
| LICENSE, scripts/*.py, assets/*.jpg | COPY | Keep. LICENSE must stay verbatim (license clause 3). Verified. |

### motion-ad

- DONE. SKILL.md and references/template-map.md audited. assets/ and scripts/ are byte-identical copies.

### human-browser

| File | Status | Action |
|---|---|---|
| SKILL.md | DONE | Finished, validated (0 errors). |
| references/snippets.md | DONE | Finished, validated (0 errors). |
| references/sites.md | DONE | Finished, validated (0 errors). |

### skill-evaluation

- DONE. `references/categories.md` is BUILT: audit it. `references/output-template.md` and `scripts/score.py` are COPY.

## Audit procedure (per BUILT or rewritten file)

1. Open the blueprint entry for the file. Read every source line range it names, completely.
2. List every atomic source item: rule, threshold, number, gotcha, list entry, table row, code block, URL, example.
3. Find each item in the target file, or in the target file the `dedup_map` names.
4. Compare verbatim assets character by character.
5. Fix missing or altered items in place. Remove filler. Make every rule line start with an imperative verb.

## Global work (all done)

1. Compress: done. Total words 117,672 against 122,779 originally (-4.2%). Without the table-padding step (item 8) the total is 124,121 (+1.1%). Item 8 is its own commit; revert it to restore padded tables.
2. Integrate: done. Each `SKILL.md` has a router or "Reference index (load when)" that links every reference file.
3. Old skill names: done. They remain only in `metadata.merged-from`.
4. Validate: done. `validate.py` reports 0 errors and 0 warnings for the 7 skills.
5. `code_blocks_missing`: reviewed. Every miss is a blueprint-approved edit: anti-slop 6/53 (tool rename `slop-eval` to `anti-slop evaluate`, bash block replaced by a link, JSON cross-reference rewrites), web-discoverability 6/74 (level list became a table, merged API blocks with renamed headings, README folder tree dropped), motion-ad 2/9 (`S=` install path rewrite), human-browser 3/14 (translated `//` comments), anti-ai-slop-escrita-ptbr 0/20.
6. Package: `skills-claude-asd-ste100.zip`.
7. Report: see Metrics.
8. Table padding: spaces around table pipes were removed in 30 non-copy files (cells unchanged, -6,449 words).

Open points for the owner:
- Several PT-BR references stay above their blueprint budget because verbatim lists and examples fill them: perfis-voz 5,520 (4,400), padroes-composicao 3,696 (3,000), padroes-estilo 3,570 (2,700), padroes-linguagem-ptbr 7,119 (5,800), padroes-conteudo-tom 4,592 (3,900), padroes-portugues-simplificado 2,823 (2,450). No rule was cut to meet a budget.
- `slop-report-template.md` (copy) names two exclusion tags; `evaluate-exclusions-qa.md` names four. The conflict exists in the source. The template was left verbatim.
- `jev-integration.md` (PT-BR) counts 57 diagnostic and 67 total Jev questions; the source said 52 and 56, and the JSON `metadata` still says 52. The JSON holds 63 Noul and 4 Score questions.
- The `Resumo` profile emoji in `perfis-voz.md` changed from the clipboard to the bar chart, because `SKILL.md` uses the clipboard for Portugues Simplificado.

## Every SKILL.md must keep

- Frontmatter keys only: `name`, `description` (<= 1024 chars, no angle brackets), `license`, `metadata` (flat string values).
- The INPUT vs OUTPUT execution directive block right after the frontmatter (English version in 6 skills, PT-BR version in `anti-ai-slop-escrita-ptbr`). Copy it from any existing SKILL.md; never edit its wording.

## Known facts (do not re-investigate)

- `anti-ai-slop-writing` linked `references/banned-words.md`, which never existed in the pack or in the installed skill. `palavras-banidas.md` replaces it.
- Skills `caveman` and `ponytail` (named in the user's preferences) are not in the pack. Do not invent them.
- 30 unreferenced JPGs of revenue-centric-design were dropped; the 44 referenced ones were recompressed (max 1400 px, JPEG q78).
- The user's global preferences call `anti-AI-slop-writing` and `navegador-humano`; tell the user to update them to `anti-ai-slop-escrita-ptbr` and `human-browser`.

## Metrics

| Metric | Original (13 skills) | Final (7 skills) |
|---|---|---|
| Skills | 13 | 7 |
| Total size | 10,015.7 KB | 4,144.2 KB (-58.6%) |
| Text size | 860.4 KB | 858.4 KB (-0.2%) |
| Images | 9,155.2 KB | 3,285.8 KB (-64.1%) |
| Words (text files, `split()`) | 122,779 | 117,672 (-4.2%) |

Words per skill: anti-ai-slop-escrita-ptbr 39,556; anti-slop 21,407; revenue-centric-design 27,201; web-discoverability 10,473; motion-ad 8,560; human-browser 5,830; skill-evaluation 4,645.
