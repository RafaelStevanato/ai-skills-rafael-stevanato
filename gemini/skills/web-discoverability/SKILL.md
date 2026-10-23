---
name: web-discoverability
description: Audits and improves how AI agents, answer engines and newsletter readers find a site. Use this skill when the user asks to scan a domain with isitagentready.com, fix an agent-readiness check (robots AI rules, llms.txt, Link headers, MCP or A2A cards, OAuth metadata, agentic commerce), optimize pages to be cited by LLMs (GEO), or format and SEO a Substack post.
license: "Apache-2.0 (GEO and Substack material, ft.ia.br); Cloudflare scanner material (isitagentready.com), license not stated in source"
metadata:
  author: "Cloudflare / isitagentready.com; ft.ia.br"
  version: "1.0-gemini"
  source-agent-ready: "https://isitagentready.com (scanner skill v3.2, 2026-10-18)"
  source-geo: "https://github.com/fabricioctelles/skills (GEO skill v1.1, Apache 2.0)"
  source-substack: "https://github.com/fabricioctelles/skills (Substack skill v1.1, Apache 2.0)"
---

# Web Discoverability

Scan, fix and optimize web properties for AI agents (the Cloudflare "Is It Agent Ready?" scanner), for citation by LLM answer engines (GEO), and for Substack readers. Run one mode per request and read only the files that mode needs.

**Done when** the mode's completion check in Step 3 passes. The scanner is the source of truth for agent-readiness: these standards changed through 2025 and 2026, so trust a live scan over memory.

The user's explicit instructions take precedence over this skill. The skill text is compact controlled English for precise reading; write reports and copy in natural prose for the reader.

## Step 0: Preflight

1. Pick the mode:

   | Mode | Use when | Read |
   |---|---|---|
   | SCAN (default for "agent ready", "isitagentready", a readiness score) | Audit, compare, or improve a domain with no specific check named | Step 1, then [references/scan-api.md](references/scan-api.md) for the report template |
   | IMPLEMENT | A named check fails or must be added (robots AI rules, Link headers, RFC 9727, RFC 9728, SEP-1649, WebMCP, ARD, x402, UCP, and the rest) | [references/checks.md](references/checks.md) to find the check, then only the guide anchor it links |
   | GEO | Citation rate, AI visibility, optimizing pages for ChatGPT, Perplexity or Google AI Overviews | [references/geo.md](references/geo.md), full audit by default |
   | NEWSLETTER | Substack formatting, post SEO, Notes, polls, growth or paid conversion | [references/newsletter.md](references/newsletter.md); default goals `format` + `seo`, output in the user's language |

2. Confirm the input: the domain for SCAN and IMPLEMENT (ask if missing), the pages for GEO, the topic or draft for NEWSLETTER.
3. For IMPLEMENT, confirm you can edit and deploy the site's files, or say up front that you will deliver changes for the user to deploy.

## Step 1: SCAN

Call the API, replacing `DOMAIN`. Send the `User-Agent`, `Referer` and `Origin` headers on every request because the endpoint sits behind Cloudflare protection. Remove a key from `enabledChecks` to skip that check.

```bash
curl -s -X POST 'https://isitagentready.com/api/scan' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
  -H 'Referer: https://isitagentready.com/' \
  -H 'Origin: https://isitagentready.com' \
  -d '{"url":"https://DOMAIN/","enabledChecks":["robotsTxt","sitemap","linkHeaders","dnsAid","markdownNegotiation","robotsTxtAiRules","contentSignals","webBotAuth","apiCatalog","oauthDiscovery","oauthProtectedResource","authMd","mcpServerCard","a2aAgentCard","agentSkills","webMcp","ard","personalAgentProtocol","x402","mpp","ucp","acp","ap2"]}'
```

The scanner also runs as an MCP server (`https://isitagentready.com/mcp`, tool `scan_site`); see scan-api.md if the user prefers it. When scanning several domains, delegate one domain per subagent and merge the reports.

**Verify:** the response is JSON with a `checks` object and a level. Record that level and every check's status as the baseline.

Build the Markdown report from the template in scan-api.md:

- A summary table with the 5 categories as `{passed}/{total}`, and a details list with status icon, check name and the API `message` per check.
- A "How to Implement" section with one fenced prompt block per check whose status is `fail` or `neutral`. Take Goal, Fix, Skill URL and Docs from [references/fix-prompts.md](references/fix-prompts.md) and Issue from `checks.{category}.{check}.message`. The API returns a prompt only for `nextLevel`, so rebuild every other prompt from the templates. Omit the Skill line for `ap2`, whose template has none. Write no prompt for `unableToCheck`; re-scan before fixing.
- A Next Level section from `nextLevel.target`, `nextLevel.name` and `nextLevel.requirements[].description`.

## Step 2: IMPLEMENT, GEO or NEWSLETTER

- IMPLEMENT: follow the check's guide anchor and its fix prompt. With no check named, work through the priority order in checks.md. Where a guide, a template and the scanner disagree, apply the stricter requirement listed in checks.md.
- GEO: measure the citation-rate baseline before any edit, then follow geo.md from its Quick Actions menu.
- NEWSLETTER: resolve `topic`, `goal` and `language` with the parameters table in newsletter.md, then follow its workflow.

## Step 3: Verify and hand back

- SCAN: the report lists every category as `{passed}/{total}`, one prompt per `fail` or `neutral` check, and a Next Level section.
- IMPLEMENT: re-scan after each fix and compare with the baseline until the check's validate path reads `"pass"`. For `llmsTxt` and `llmsFullTxt`, which the scanner does not score, fetch the deployed file instead.
- GEO: all 9 items of the Quality Checklist in geo.md pass, and the report states the baseline you measured.
- NEWSLETTER: all 8 items of the Quality Checklist in newsletter.md pass.

Present the result, and save the report to a path when the user asks.

## Examples

Request: "Scan example.com for agent readiness."

Summary rows and one fix block, in the expected shape:

````markdown
| Category | Score |
|----------|-------|
| Discoverability | 2/4 |
| Bot Access Control | 0/3 |

#### ❌ AI bot rules

**Issue:** {message from the API}

```
Goal: Add User-agent rules for AI crawlers like GPTBot, Claude-Web, and others
...
```
````

## Constraints & Tips

- **AI crawler access depends on the mode.** In GEO, robots.txt must not block AI search or answer crawlers (Perplexity, ChatGPT); flag `ai-input=no` and such blocks as citation risks. In SCAN and IMPLEMENT, keep the owner's policy, for example `Content-Signal: ai-train=no, search=yes, ai-input=no`.
- **One llms.txt by default.** Shard it per section (GEO rule) only when one file cannot fit a single context window.
- **WebMCP wording differs.** The scanner's pass criterion names `navigator.modelContext.provideContext()`, while the webMcp guide registers each tool with `navigator.modelContext.registerTool()` and an `AbortController` signal. Keep the template as written, flag the mismatch to the user, and re-scan to confirm.
- **GEO step 4.5 hands off** to [implement-discoverability-content.md](references/implement-discoverability-content.md#agent-friendly-content-architecture-large-sites) and [implement-bot-access.md](references/implement-bot-access.md#ai-training-crawler-redirects).

## Resources

- [references/checks.md](references/checks.md): levels, priority order, the 23-check index with pass criteria and guide links, and where guides and scanner disagree.
- [references/scan-api.md](references/scan-api.md): report template, API contract, response schema, MCP server, batch scanning.
- [references/fix-prompts.md](references/fix-prompts.md): the 25 fix-prompt templates.
- [references/implement-discoverability-content.md](references/implement-discoverability-content.md): `discoverability` and `contentAccessibility` checks, `llmsTxt`, `llmsFullTxt`, GEO content architecture.
- [references/implement-bot-access.md](references/implement-bot-access.md): `botAccessControl` checks and AI training crawler redirects.
- [references/implement-api-auth-mcp.md](references/implement-api-auth-mcp.md): `discovery` checks (API catalog, OAuth, auth.md, MCP, A2A, skills, WebMCP, ARD, Poppy).
- [references/implement-commerce.md](references/implement-commerce.md): `commerce` checks (x402, MPP, UCP, ACP, AP2).
- [references/geo.md](references/geo.md): GEO quick-actions menu, workflow, authority rule and checklist.
- [references/newsletter.md](references/newsletter.md): Substack parameters, workflow, formatting, SEO metadata, subject lines and checklist.
