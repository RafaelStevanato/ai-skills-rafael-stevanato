---
name: web-discoverability
description: >-
  Make sites and content discoverable by AI agents, LLM answer engines and Substack readers. SCAN (agent ready, isitagentready, agent-ready score): audit a domain with the Cloudflare Is It Agent Ready scanner (API or MCP scan_site), report level 0-5, generate copy-paste fix prompts. IMPLEMENT: guides for robots.txt, sitemap.xml, Link headers RFC 8288, DNS-AID, llms.txt, llms-full.txt, markdown for agents (Accept: text/markdown), AI bot rules, Content Signals, Web Bot Auth, API Catalog RFC 9727, OAuth OIDC RFC 8414, OAuth Protected Resource RFC 9728, auth.md, MCP Server Card SEP-1649, A2A Agent Card, agent skills index, WebMCP, ARD ai-catalog, Poppy, x402, MPP, UCP, ACP, AP2. GEO: generative engine optimization, AEO, AI SEO, LLM citation rate, AI visibility, optimize for ChatGPT, Perplexity, Google AI Overview, roundup pages, FAQPage schema, community signals. NEWSLETTER: Substack post formatting, SEO title, slug, meta description, Notes, polls, Chat, recommendations, monetization, free-to-paid conversion.
license: "Apache-2.0 (GEO and Substack material, ft.ia.br); Cloudflare scanner material (isitagentready.com), license not stated in source"
metadata:
  author: "Cloudflare / isitagentready.com; ft.ia.br"
  version: "1.0"
  source-agent-ready: "https://isitagentready.com (scanner skill v3.2, 2026-10-18)"
  source-geo: "https://github.com/fabricioctelles/skills (GEO skill v1.1, 2026-03-05, Apache 2.0)"
  source-substack: "https://github.com/fabricioctelles/skills (Substack skill v1.1, 2026-03-05, Apache 2.0)"
  merged-from: "agent-ready-cloudflare, geo-optimization, substack-expert"
  consolidated: "2026-10-23 ASD-STE100 rewrite"
---
> **⚠️ EXECUTION DIRECTIVE (INPUT vs. OUTPUT SEPARATION):**
> The rules in this skill use strict ASD-STE100 controlled language solely for zero-ambiguity parsing and token efficiency.
> - **NEVER copy this telegraphic or robotic style into human-facing outputs.**
> - Apply 80% ASD-STE100 in final outputs ONLY when explaining dense technical concepts.

# Web Discoverability

Scope: scan, fix and optimize web properties for AI agents ("Is It Agent Ready?" scanner), LLM citation (GEO) and Substack.

## Mode Router

Select one mode per request. Load only the files that the mode needs (see Reference Index).

- **SCAN**: scan a domain, agent ready, isitagentready, AI agent scan, agent readiness, agent-ready score, improve agent readiness, make a site usable by AI agents, check agent protocol support (MCP, robots.txt, Link headers), debug missing agent-readiness checks, get fix instructions, compare agent readiness across sites.
  Default: SCAN: Core Flow, Steps 1-5.
- **IMPLEMENT**: named check, fix a failing check, agent discovery, RFC 9727, RFC 8288, RFC 9728, SEP-1649, WebMCP, ARD, ai-catalog, x402, UCP, ACP, or any other check in the Check Index.
  Default: find the check in Check Index, open the guide anchor.
- **GEO**: GEO, AEO, AI SEO, LLM optimization, citation rate, AI visibility, optimize for ChatGPT, roundup pages, audit pages for AI discoverability.
  Default: Full GEO Audit (menu option 1).
- **NEWSLETTER**: Substack, newsletter, post SEO, Notes, polls, paid conversion.
  Default: goals `format` + `seo`, output language = user language.

- Chain SCAN into IMPLEMENT: for each check with status `fail`, load the matching `implement-*.md` file.
- Run SCAN first when the user asks to improve agent readiness and names no check.

## SCAN: Core Flow

Run these steps every time SCAN mode starts.

### Step 1: Get the domain

If the user gave no domain, ask:

> Which domain do you want to scan on isitagentready.com?

### Step 2: Scan via API

```bash
curl -s -X POST 'https://isitagentready.com/api/scan' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
  -H 'Referer: https://isitagentready.com/' \
  -H 'Origin: https://isitagentready.com' \
  -d '{"url":"https://DOMAIN/","enabledChecks":["robotsTxt","sitemap","linkHeaders","dnsAid","markdownNegotiation","robotsTxtAiRules","contentSignals","webBotAuth","apiCatalog","oauthDiscovery","oauthProtectedResource","authMd","mcpServerCard","a2aAgentCard","agentSkills","webMcp","ard","personalAgentProtocol","x402","mpp","ucp","acp","ap2"]}'
```

- Replace `DOMAIN` with the target domain.
- Send the `User-Agent`, `Referer` and `Origin` headers on every request (Cloudflare protection).
- Remove a key from `enabledChecks` to skip that check.

### Step 3: Generate the Markdown report

- Build the report from the report template in [references/scan-api.md](references/scan-api.md).
- Add a Summary table (5 categories, `{passed}/{total}` each) and a Details list (per check: status icon, name, API `message`).
- Add a "How to Implement" section (Step 4).
- End with Next Level: `nextLevel.target`, `nextLevel.name`, `nextLevel.requirements[].description`.

### Step 4: Generate "How to Implement" prompts

- Write one prompt block per check with `status: "fail"` or `status: "neutral"`.
- Take Goal, Fix, Skill URL and Docs from the template in [references/fix-prompts.md](references/fix-prompts.md). Take Issue from `checks.{category}.{check}.message`.
- Omit the Skill line for `ap2`. Its template has no Skill URL.
- Format each prompt as a fenced code block for a coding agent, per the block format in [references/scan-api.md](references/scan-api.md).
- Rebuild every prompt from the templates. The API returns a prompt only for `nextLevel`.
- Write no prompt for status `unableToCheck`. Re-scan before any fix.

### Step 5: Deliver

- Present the full Markdown report. Save it to the requested path on request.

Usage example:

```
You: "Scan example.com for agent readiness"

Agent: Scans via API → generates Markdown report → includes fix prompts for every failure
```

## Levels

Level | Name | Requirements
-------|------|-------------
0 | Not Ready | Fewer than 2 of: robots.txt, sitemap, Link headers
1 | Basic Web Presence | Pass 2 of 3: robots.txt, sitemap, link headers
2 | Bot-Aware | Level 1 + both: AI bot rules AND Content Signals in robots.txt
3 | Agent-Readable | Level 2 + markdown content negotiation
4 | Agent-Integrated | Level 3 + 1 of 4: MCP Server Card, A2A Agent Card, Agent Skills, API Catalog
5 | Agent-Native | Level 4 + 2 of 3: Web Bot Auth, all integrations, auth metadata (OAuth or Auth.md)

## Priority Order

Implement missing checks in this order for maximum impact:

1. `robots.txt` + `sitemap.xml` → Level 1
2. `Content Signals` in robots.txt → Level 2
3. `Markdown for Agents` + `Link headers` → toward Level 3
4. `MCP Server Card` + `Agent Skills Index` → toward Level 4
5. `OAuth discovery` + `API Catalog` → full agent interoperability

## Check Index

- Count 23 scored checks: 4 + 1 + 3 + 10 + 5.
- Build the validate path as `checks.<category key>.<API key>.status`. Pass means `"pass"`.
- Treat `llmsTxt` and `llmsFullTxt` as unscored: not in `enabledChecks`, no scanner status.

### Discoverability (4 checks), category key `discoverability`

Check | Pass criteria | Links
-------|---------------|-------
robots.txt `robotsTxt` | Returns 200 with `text/plain` containing at least one `User-agent` directive | [guide](references/implement-discoverability-content.md#robotstxt) [prompt](references/fix-prompts.md#robotstxt)
sitemap.xml `sitemap` | `/sitemap.xml` returns valid XML, or `Sitemap` directive found in robots.txt | [guide](references/implement-discoverability-content.md#sitemap) [prompt](references/fix-prompts.md#sitemap)
Link headers `linkHeaders` | Homepage includes `Link` headers with agent-useful relations (`service-desc`, `api-catalog`, etc.) | [guide](references/implement-discoverability-content.md#linkheaders) [prompt](references/fix-prompts.md#linkheaders)
DNS-AID `dnsAid` | SVCB/HTTPS records found under `_agents` namespace via DNS-over-HTTPS (Cloudflare → Google fallback) | [guide](references/implement-discoverability-content.md#dnsaid) [prompt](references/fix-prompts.md#dnsaid)

### Content (1 check), category key `contentAccessibility`

Check | Pass criteria | Links
-------|---------------|-------
Markdown for Agents `markdownNegotiation` | `Accept: text/markdown` returns `Content-Type: text/markdown` | [guide](references/implement-discoverability-content.md#markdownnegotiation) [prompt](references/fix-prompts.md#markdownnegotiation)

### Bot Access Control (3 checks), category key `botAccessControl`

Check | Pass criteria | Links
-------|---------------|-------
AI bot rules `robotsTxtAiRules` | robots.txt contains `User-agent` entries for known AI bots (GPTBot, Claude-Web, Google-Extended, etc.) | [guide](references/implement-bot-access.md#robotstxtairules) [prompt](references/fix-prompts.md#robotstxtairules)
Content Signals `contentSignals` | robots.txt contains `Content-Signal` directives with ai-train/search/ai-input | [guide](references/implement-bot-access.md#contentsignals) [prompt](references/fix-prompts.md#contentsignals)
Web Bot Auth `webBotAuth` | `/.well-known/http-message-signatures-directory` exists with valid JWKS (informational — neutral does not affect score) | [guide](references/implement-bot-access.md#webbotauth) [prompt](references/fix-prompts.md#webbotauth)

### API, Auth, MCP & Skill Discovery (10 checks), category key `discovery`

Check | Pass criteria | Links
-------|---------------|-------
API Catalog `apiCatalog` | `/.well-known/api-catalog` returns valid `linkset+json` with API entries | [guide](references/implement-api-auth-mcp.md#apicatalog) [prompt](references/fix-prompts.md#apicatalog)
OAuth/OIDC `oauthDiscovery` | `/.well-known/openid-configuration` or `oauth-authorization-server` with valid OAuth metadata | [guide](references/implement-api-auth-mcp.md#oauthdiscovery) [prompt](references/fix-prompts.md#oauthdiscovery)
OAuth Protected Resource `oauthProtectedResource` | `/.well-known/oauth-protected-resource` with `resource` and `authorization_servers` | [guide](references/implement-api-auth-mcp.md#oauthprotectedresource) [prompt](references/fix-prompts.md#oauthprotectedresource)
Auth.md `authMd` | `/auth.md` exists with valid H1 heading containing "auth.md"; optionally PRM + AS metadata | [guide](references/implement-api-auth-mcp.md#authmd) [prompt](references/fix-prompts.md#authmd)
MCP Server Card `mcpServerCard` | Valid card at `/.well-known/mcp/server-card.json`, `server-cards.json`, or `mcp.json` with `serverInfo.name` | [guide](references/implement-api-auth-mcp.md#mcpservercard) [prompt](references/fix-prompts.md#mcpservercard)
A2A Agent Card `a2aAgentCard` | `/.well-known/agent-card.json` with `name`, `version`, and `supportedInterfaces` | [guide](references/implement-api-auth-mcp.md#a2aagentcard) [prompt](references/fix-prompts.md#a2aagentcard)
Agent Skills Index `agentSkills` | `/.well-known/agent-skills/index.json` with valid `skills` array (legacy `/.well-known/skills/` also accepted) | [guide](references/implement-api-auth-mcp.md#agentskills) [prompt](references/fix-prompts.md#agentskills)
WebMCP `webMcp` | Page exposes MCP tools via `navigator.modelContext.provideContext()` | [guide](references/implement-api-auth-mcp.md#webmcp) [prompt](references/fix-prompts.md#webmcp)
ARD `ard` | `/.well-known/ai-catalog.json` with `specVersion`, `host`, and non-empty `entries` | [guide](references/implement-api-auth-mcp.md#ard) [prompt](references/fix-prompts.md#ard)
Personal Agent Protocol (Poppy) `personalAgentProtocol` | `/.well-known/poppy.json` (draft 0.1) with valid `organization`/`domain` and interfaces; when auth is declared, a matching OAuth issuer whose metadata lists the domain in `poppy_domains` (informational — does not affect level or score) | [guide](references/implement-api-auth-mcp.md#personalagentprotocol) [prompt](references/fix-prompts.md#personalagentprotocol)

### Commerce, optional (5 checks, scored only if e-commerce signals detected), category key `commerce`

Check | Pass criteria | Links
-------|---------------|-------
x402 `x402` | API routes return HTTP 402 with valid x402 payment headers | [guide](references/implement-commerce.md#x402) [prompt](references/fix-prompts.md#x402)
MPP `mpp` | `/openapi.json` with `x-payment-info` extensions on payable operations (Machine Payment Protocol) | [guide](references/implement-commerce.md#mpp) [prompt](references/fix-prompts.md#mpp)
UCP `ucp` | `/.well-known/ucp` with `protocol_version` and `services` | [guide](references/implement-commerce.md#ucp) [prompt](references/fix-prompts.md#ucp)
ACP `acp` | `/.well-known/acp.json` with `protocol.name`, `api_base_url`, `transports`, `capabilities.services` | [guide](references/implement-commerce.md#acp) [prompt](references/fix-prompts.md#acp)
AP2 `ap2` | A2A Agent Card includes AP2 extension with role information | [guide](references/implement-commerce.md#ap2) [prompt](references/fix-prompts.md#ap2)

### Unscored guides

Check | Pass criteria | Links
-------|---------------|-------
llms.txt `llmsTxt` | Deployed site serves `/llms.txt` as plain text (UTF-8), HTTP 200, H1 title first, short summary paragraph, links to the main content sections | [guide](references/implement-discoverability-content.md#llmstxt) [prompt](references/fix-prompts.md#llmstxt)
llms-full.txt `llmsFullTxt` | Deployed site serves `/llms-full.txt` as plain text (UTF-8) with HTTP 200 and `/llms.txt` links to it | [guide](references/implement-discoverability-content.md#llmsfulltxt) [prompt](references/fix-prompts.md#llmsfulltxt)

## IMPLEMENT: Core Rules

- Find the check in Check Index. Load only the `implement-*.md` file that holds the guide anchor, then the prompt anchor in [references/fix-prompts.md](references/fix-prompts.md) for Goal, Fix and Docs.
- Apply the stricter rule when a guide, a template and the scanner disagree. Each guide records its case:
  - OAuth Protected Resource: `scopes_supported`; `authMd` adds `bearer_methods_supported` with `header`.
  - OAuth discovery: `grant_types_supported` and `response_types_supported`.
  - API Catalog: `status` next to `service-desc` and `service-doc`.
  - MCP Server Card: `/.well-known/mcp/server-card.json` (the scanner also accepts `server-cards.json` and `mcp.json`).
  - Agent Skills: `/.well-known/agent-skills/index.json`, never the legacy `/.well-known/skills/` path.
  - Batch scans: the full `User-Agent` string from the Step 2 curl block.
- Implement checks in Priority Order when the user names no check.

## GEO: Core Rules

- Measure the Citation Rate baseline before any edit. Present the Quick Actions menu in [references/geo.md](references/geo.md) first.
- Hand off step 4.5 to [references/implement-discoverability-content.md](references/implement-discoverability-content.md#agent-friendly-content-architecture-large-sites) and [references/implement-bot-access.md](references/implement-bot-access.md#ai-training-crawler-redirects).

## NEWSLETTER: Core Rules

- Resolve `topic`, `goal` and `language` with the Parameters table in [references/newsletter.md](references/newsletter.md).
- Follow the workflow in [references/newsletter.md](references/newsletter.md).

## Cross-Mode Conflict Rules

- GEO crawler access vs Bot Access policy:
  - GEO mode: robots.txt must not block AI crawlers (Perplexity, ChatGPT). Flag `ai-input=no` and any block on AI search or answer bots as citation risks.
  - SCAN and IMPLEMENT mode: keep the owner policy. Example: `Content-Signal: ai-train=no, search=yes, ai-input=no`.
- llms.txt sizing: publish one `/llms.txt` by default. Apply the GEO sharding rule (per-section `llms.txt` files) when one file cannot fit a single context window.
- WebMCP API: the scanner pass criterion names `navigator.modelContext.provideContext()`. The webMcp guide states `navigator.modelContext.registerTool()` per tool with an `AbortController` signal. Keep the template unchanged. Flag the mismatch to the user. Re-scan to confirm.

## Output Gates

- SCAN: Check that the report lists every category with `{passed}/{total}`, one prompt per `fail` or `neutral` check, and a Next Level section.
- IMPLEMENT: Re-run SCAN Step 2. Check that the validate path is `"pass"`. For `llmsTxt` and `llmsFullTxt`, fetch the deployed file.
- GEO: Check all 9 items of the Quality Checklist in [references/geo.md](references/geo.md).
- NEWSLETTER: Check all 8 items of the Quality Checklist in [references/newsletter.md](references/newsletter.md).

## Reference Index

Load a file only when its condition holds:

- [references/scan-api.md](references/scan-api.md): SCAN mode: templates, API contract, MCP server, response schema, batch scanning.
- [references/fix-prompts.md](references/fix-prompts.md): a check fails and needs its fix prompt (25 templates).
- [references/implement-discoverability-content.md](references/implement-discoverability-content.md): implement a `discoverability` or `contentAccessibility` check, `llmsTxt`, `llmsFullTxt` or GEO content architecture.
- [references/implement-bot-access.md](references/implement-bot-access.md): implement a `botAccessControl` check or AI training crawler redirects.
- [references/implement-api-auth-mcp.md](references/implement-api-auth-mcp.md): implement a `discovery` check (API, auth, MCP, skills, ARD, Poppy).
- [references/implement-commerce.md](references/implement-commerce.md): implement a `commerce` check (x402, mpp, ucp, acp, ap2).
- [references/geo.md](references/geo.md): GEO mode: menu, workflow, authority rule, checklist.
- [references/newsletter.md](references/newsletter.md): NEWSLETTER mode: workflow, formatting, SEO metadata, subject lines, checklist.
