# ai-skills-rafael-stevanato

Pacote de 11 skills (7 consolidadas a partir de 13, mais a `turnitout-ptbr`, a `gpt-image`, a `gemini` e a `anti-slop-ui-ux`), em uma versão por agente. As regras usam linguagem controlada ASD-STE100 para leitura precisa pelo modelo (input), e a saída se adapta ao leitor (output).

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
| `anti-slop-ui-ux` | Regras de engenharia para telas de produto: hierarquia plana, cor só por token, shadcn/Radix/Tailwind e portão PRE-FLIGHT + SELF-CHECK |
| `gemini` | Gera e edita imagem com o Nano Banana pela API do Google AI Studio (`GEMINI_API_KEY`). Só Claude Code |
| `gpt-image` | Gera e edita imagem com o GPT Image 2 pelo Codex CLI do app Codex, com a conta ChatGPT e sem chave de API. Só Claude Code |
| `human-browser` | Navegação web com poucas ações, armadilhas testadas e paradas seguras |
| `motion-ad` | Anúncio em vídeo de 15 s (MP4) a partir da landing page do produto |
| `revenue-centric-design` | 134 princípios de conversão, retenção e monetização para SaaS |
| `skill-evaluation` | Nota, trigger eval e diagnóstico de uma skill |
| `turnitout-ptbr` | Filtro PT-BR de texto e comentários de código: script determinístico contra conectivos de IA, clichês de tradução, travessão e caracteres invisíveis |
| `web-discoverability` | Prontidão para agentes de IA, GEO e SEO de Substack |

No Claude Code, ative o hook da `turnitout-ptbr` com `python scripts/install_hooks.py`, dentro da pasta da skill.

A `gpt-image` e a `gemini` existem só em `claude-code/`: a skill `gemini` é a de imagem do Claude Code, não a pasta `gemini/` do Antigravity. Para a `gemini`, grave a chave antes com `setx GEMINI_API_KEY "sua-chave"`.
