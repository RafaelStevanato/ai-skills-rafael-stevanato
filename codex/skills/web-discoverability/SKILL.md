---
name: web-discoverability
description: Make a site findable and usable by AI agents and answer engines. Use to scan a domain with isitagentready.com, implement agent-discovery standards (robots AI rules, llms.txt, Link headers, MCP or A2A cards, OAuth metadata, agentic commerce), optimize pages for LLM citations (GEO), or format and SEO a Substack post.
license: "Apache-2.0 (GEO and Substack material, ft.ia.br); Cloudflare scanner material (isitagentready.com), license not stated in source"
metadata:
  author: "Cloudflare / isitagentready.com; ft.ia.br"
  version: "1.0-codex"
  source-agent-ready: "https://isitagentready.com (scanner skill v3.2, 2026-10-18)"
  source-geo: "https://github.com/fabricioctelles/skills (GEO skill v1.1, Apache 2.0)"
  source-substack: "https://github.com/fabricioctelles/skills (Substack skill v1.1, Apache 2.0)"
---

# Web Discoverability

Scan, fix and optimize web properties for AI agents (the Cloudflare "Is It Agent Ready?" scanner), for citation by LLM answer engines (GEO), and for Substack readers. Pick one mode per request and read only the files that mode needs.

The user's explicit instructions take precedence over this skill. The skill text is compact controlled English for precise reading; write reports and copy in natural prose for the reader.

## Modes

| Mode | Use when | Start with |
|---|---|---|
| SCAN (default for "agent ready", "isitagentready", readiness score) | The user wants a domain audited, compared, or improved with no specific check named | The scan below, then [references/scan-api.md](references/scan-api.md) for the report template |
| IMPLEMENT | A named check fails or must be added (robots AI rules, Link headers, RFC 9727, RFC 9728, SEP-1649, WebMCP, ARD, x402, UCP, and the rest) | [references/checks.md](references/checks.md) to find the check, then only the guide anchor it links |
| GEO | Citation rate, AI visibility, optimizing pages for ChatGPT, Perplexity or Google AI Overviews | [references/geo.md](references/geo.md), full audit by default |
| NEWSLETTER | Substack formatting, post SEO, Notes, polls, growth or paid conversion | [references/newsletter.md](references/newsletter.md); default goals `format` + `seo`, output in the user's language |

After a scan, IMPLEMENT each check whose status is `fail`. When the user asks to improve readiness but names no check, scan first and then follow the priority order in checks.md.

## SCAN

If the user gave no domain, ask which domain to scan. Then call the API, replacing `DOMAIN`. Send the `User-Agent`, `Referer` and `Origin` headers on every request because the endpoint sits behind Cloudflare protection. Remove a key from `enabledChecks` to skip that check.

```bash
curl -s -X POST 'https://isitagentready.com/api/scan' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
  -H 'Referer: https://isitagentready.com/' \
  -H 'Origin: https://isitagentready.com' \
  -d '{"url":"https://DOMAIN/","enabledChecks":["robotsTxt","sitemap","linkHeaders","dnsAid","markdownNegotiation","robotsTxtAiRules","contentSignals","webBotAuth","apiCatalog","oauthDiscovery","oauthProtectedResource","authMd","mcpServerCard","a2aAgentCard","agentSkills","webMcp","ard","personalAgentProtocol","x402","mpp","ucp","acp","ap2"]}'
```

The scanner also runs as an MCP server (`https://isitagentready.com/mcp`, tool `scan_site`); see scan-api.md if the user prefers it.

Build the Markdown report from the template in scan-api.md:

- A summary table with the 5 categories as `{passed}/{total}`, and a details list with status icon, check name and the API `message` per check.
- A "How to Implement" section with one fenced prompt block per check whose status is `fail` or `neutral`. Take Goal, Fix, Skill URL and Docs from [references/fix-prompts.md](references/fix-prompts.md) and Issue from `checks.{category}.{check}.message`. The API returns a prompt only for `nextLevel`, so rebuild every other prompt from the templates. Omit the Skill line for `ap2`, whose template has none. Write no prompt for `unableToCheck`; re-scan before fixing.
- A Next Level section from `nextLevel.target`, `nextLevel.name` and `nextLevel.requirements[].description`.

Present the full report, and save it to a path when the user asks.

## Cross-mode conflicts

- AI crawler access: in GEO mode, robots.txt must not block AI search or answer crawlers (Perplexity, ChatGPT); flag `ai-input=no` and such blocks as citation risks. In SCAN and IMPLEMENT, keep the owner's policy, for example `Content-Signal: ai-train=no, search=yes, ai-input=no`.
- llms.txt size: publish one `/llms.txt` by default. Shard it per section (GEO rule) only when one file cannot fit a single context window.
- WebMCP: the scanner's pass criterion names `navigator.modelContext.provideContext()`, while the webMcp guide registers each tool with `navigator.modelContext.registerTool()` and an `AbortController` signal. Keep the template as written, flag the mismatch to the user, and re-scan to confirm.
- GEO step 4.5 hands off to [implement-discoverability-content.md](references/implement-discoverability-content.md#agent-friendly-content-architecture-large-sites) and [implement-bot-access.md](references/implement-bot-access.md#ai-training-crawler-redirects).

## Done when

- SCAN: the report lists every category as `{passed}/{total}`, one prompt per `fail` or `neutral` check, and a Next Level section.
- IMPLEMENT: a re-scan shows `"pass"` on the check's validate path. For `llmsTxt` and `llmsFullTxt`, which the scanner does not score, fetch the deployed file instead.
- GEO: the citation-rate baseline was measured before any edit, and all 9 items of the Quality Checklist in geo.md pass.
- NEWSLETTER: all 8 items of the Quality Checklist in newsletter.md pass.

## References

- [references/checks.md](references/checks.md): levels, priority order, the 23-check index with pass criteria and guide links, and where guides and scanner disagree.
- [references/scan-api.md](references/scan-api.md): report template, API contract, response schema, MCP server, batch scanning.
- [references/fix-prompts.md](references/fix-prompts.md): the 25 fix-prompt templates.
- [references/implement-discoverability-content.md](references/implement-discoverability-content.md): `discoverability` and `contentAccessibility` checks, `llmsTxt`, `llmsFullTxt`, GEO content architecture.
- [references/implement-bot-access.md](references/implement-bot-access.md): `botAccessControl` checks and AI training crawler redirects.
- [references/implement-api-auth-mcp.md](references/implement-api-auth-mcp.md): `discovery` checks (API catalog, OAuth, auth.md, MCP, A2A, skills, WebMCP, ARD, Poppy).
- [references/implement-commerce.md](references/implement-commerce.md): `commerce` checks (x402, MPP, UCP, ACP, AP2).
- [references/geo.md](references/geo.md): GEO quick-actions menu, workflow, authority rule and checklist.
- [references/newsletter.md](references/newsletter.md): Substack parameters, workflow, formatting, SEO metadata, subject lines and checklist.
