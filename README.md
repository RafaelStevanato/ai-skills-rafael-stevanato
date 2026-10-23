# claude-skills-rafael-stevanato

Pacote de 7 skills (consolidadas a partir de 13), em uma versão por agente. As regras usam linguagem controlada ASD-STE100 para leitura precisa pelo modelo (input), e a saída se adapta ao leitor (output).

Cada pasta de plataforma contém só as pastas das skills: arraste-as para a pasta de skills do agente.

| Pasta | Agente | Arraste para |
|---|---|---|
| `claude-code/` | Claude Code | `~/.claude/skills/` |
| `codex/` | ChatGPT Codex (GPT-6) | `~/.agents/skills/` (ou `<repo>/.agents/skills/`) |
| `gemini/` | Google Antigravity (Gemini 4 Argon) | `~/.gemini/config/skills/` (ou `<workspace>/.agents/skills/`) |

No Windows, `~` é `C:\Users\<você>`.

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
