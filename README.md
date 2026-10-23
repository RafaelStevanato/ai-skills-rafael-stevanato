# claude-skills-rafael-stevanato

Pacote de 7 skills (consolidadas a partir de 13), mantido em uma versão por agente. As regras usam linguagem controlada ASD-STE100 para leitura precisa pelo modelo (input), e a saída se adapta ao leitor (output).

| Pasta | Agente e modelo | Estado |
|---|---|---|
| [`claude-code/`](claude-code/) | Claude Code | Pronta. Histórico da consolidação em [claude-code/HANDOFF.md](claude-code/HANDOFF.md) |
| [`codex/`](codex/) | ChatGPT Codex (GPT-6) | Pronta. O que mudou e como instalar em [codex/README.md](codex/README.md) |
| [`gemini/`](gemini/) | Gemini 4 Argon (Google Antigravity) | Pronta. O que mudou e como instalar em [gemini/README.md](gemini/README.md) |

## Skills

| Skill | O que faz |
|---|---|
| `anti-ai-slop-escrita-ptbr` | Escreve e revisa texto em PT-BR (e inglês) sem marcas de IA, com trava factual |
| `anti-slop` | Design de UI sem cara de IA: build, design system, lint de DESIGN.md e Slop Index |
| `human-browser` | Navegação web com poucas ações, armadilhas testadas e paradas seguras |
| `motion-ad` | Anúncio em vídeo de 15 s (MP4) a partir da landing page do produto |
| `revenue-centric-design` | 134 princípios de conversão, retenção e monetização para SaaS |
| `skill-evaluation` | Nota, trigger eval e diagnóstico de uma skill |
| `web-discoverability` | Prontidão para agentes de IA, GEO e SEO de Substack |

## Instalação

- Claude Code: copie `claude-code/skills/<nome>` para `~/.claude/skills/<nome>`.
- Codex: copie `codex/skills/<nome>` para `~/.agents/skills/<nome>` (ou `<repo>/.agents/skills/<nome>`).
- Gemini (Antigravity): copie `gemini/skills/<nome>` para `~/.gemini/config/skills/<nome>` (ou `<workspace>/.agents/skills/<nome>`).
