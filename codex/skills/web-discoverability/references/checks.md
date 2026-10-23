# Agent-readiness checks: levels, priority and index

Contents: Levels · Priority order · Check index (Discoverability, Content, Bot Access Control, API/Auth/MCP/Skill Discovery, Commerce, Unscored) · Where guides and the scanner disagree

## Levels

| Level | Name | Requirements |
|---|---|---|
| 0 | Not Ready | Fewer than 2 of: robots.txt, sitemap, Link headers |
| 1 | Basic Web Presence | Pass 2 of 3: robots.txt, sitemap, link headers |
| 2 | Bot-Aware | Level 1 + both: AI bot rules AND Content Signals in robots.txt |
| 3 | Agent-Readable | Level 2 + markdown content negotiation |
| 4 | Agent-Integrated | Level 3 + 1 of 4: MCP Server Card, A2A Agent Card, Agent Skills, API Catalog |
| 5 | Agent-Native | Level 4 + 2 of 3: Web Bot Auth, all integrations, auth metadata (OAuth or Auth.md) |

## Priority order

When the user names no check, implement missing checks in this order:

1. `robots.txt` + `sitemap.xml` → Level 1
2. `Content Signals` in robots.txt → Level 2
3. `Markdown for Agents` + `Link headers` → toward Level 3
4. `MCP Server Card` + `Agent Skills Index` → toward Level 4
5. `OAuth discovery` + `API Catalog` → full agent interoperability

## Check index

There are 23 scored checks (4 + 1 + 3 + 10 + 5). The validate path is `checks.<category key>.<API key>.status`; pass means `"pass"`. `llmsTxt` and `llmsFullTxt` are unscored: they are not in `enabledChecks` and have no scanner status.

### Discoverability (4 checks), category key `discoverability`

| Check | Pass criteria | Links |
|---|---|---|
| robots.txt `robotsTxt` | Returns 200 with `text/plain` containing at least one `User-agent` directive | [guide](implement-discoverability-content.md#robotstxt) [prompt](fix-prompts.md#robotstxt) |
| sitemap.xml `sitemap` | `/sitemap.xml` returns valid XML, or `Sitemap` directive found in robots.txt | [guide](implement-discoverability-content.md#sitemap) [prompt](fix-prompts.md#sitemap) |
| Link headers `linkHeaders` | Homepage includes `Link` headers with agent-useful relations (`service-desc`, `api-catalog`, etc.) | [guide](implement-discoverability-content.md#linkheaders) [prompt](fix-prompts.md#linkheaders) |
| DNS-AID `dnsAid` | SVCB/HTTPS records found under `_agents` namespace via DNS-over-HTTPS (Cloudflare → Google fallback) | [guide](implement-discoverability-content.md#dnsaid) [prompt](fix-prompts.md#dnsaid) |

### Content (1 check), category key `contentAccessibility`

| Check | Pass criteria | Links |
|---|---|---|
| Markdown for Agents `markdownNegotiation` | `Accept: text/markdown` returns `Content-Type: text/markdown` | [guide](implement-discoverability-content.md#markdownnegotiation) [prompt](fix-prompts.md#markdownnegotiation) |

### Bot Access Control (3 checks), category key `botAccessControl`

| Check | Pass criteria | Links |
|---|---|---|
| AI bot rules `robotsTxtAiRules` | robots.txt contains `User-agent` entries for known AI bots (GPTBot, Claude-Web, Google-Extended, etc.) | [guide](implement-bot-access.md#robotstxtairules) [prompt](fix-prompts.md#robotstxtairules) |
| Content Signals `contentSignals` | robots.txt contains `Content-Signal` directives with ai-train/search/ai-input | [guide](implement-bot-access.md#contentsignals) [prompt](fix-prompts.md#contentsignals) |
| Web Bot Auth `webBotAuth` | `/.well-known/http-message-signatures-directory` exists with valid JWKS (informational — neutral does not affect score) | [guide](implement-bot-access.md#webbotauth) [prompt](fix-prompts.md#webbotauth) |

### API, Auth, MCP & Skill Discovery (10 checks), category key `discovery`

| Check | Pass criteria | Links |
|---|---|---|
| API Catalog `apiCatalog` | `/.well-known/api-catalog` returns valid `linkset+json` with API entries | [guide](implement-api-auth-mcp.md#apicatalog) [prompt](fix-prompts.md#apicatalog) |
| OAuth/OIDC `oauthDiscovery` | `/.well-known/openid-configuration` or `oauth-authorization-server` with valid OAuth metadata | [guide](implement-api-auth-mcp.md#oauthdiscovery) [prompt](fix-prompts.md#oauthdiscovery) |
| OAuth Protected Resource `oauthProtectedResource` | `/.well-known/oauth-protected-resource` with `resource` and `authorization_servers` | [guide](implement-api-auth-mcp.md#oauthprotectedresource) [prompt](fix-prompts.md#oauthprotectedresource) |
| Auth.md `authMd` | `/auth.md` exists with valid H1 heading containing "auth.md"; optionally PRM + AS metadata | [guide](implement-api-auth-mcp.md#authmd) [prompt](fix-prompts.md#authmd) |
| MCP Server Card `mcpServerCard` | Valid card at `/.well-known/mcp/server-card.json`, `server-cards.json`, or `mcp.json` with `serverInfo.name` | [guide](implement-api-auth-mcp.md#mcpservercard) [prompt](fix-prompts.md#mcpservercard) |
| A2A Agent Card `a2aAgentCard` | `/.well-known/agent-card.json` with `name`, `version`, and `supportedInterfaces` | [guide](implement-api-auth-mcp.md#a2aagentcard) [prompt](fix-prompts.md#a2aagentcard) |
| Agent Skills Index `agentSkills` | `/.well-known/agent-skills/index.json` with valid `skills` array (legacy `/.well-known/skills/` also accepted) | [guide](implement-api-auth-mcp.md#agentskills) [prompt](fix-prompts.md#agentskills) |
| WebMCP `webMcp` | Page exposes MCP tools via `navigator.modelContext.provideContext()` | [guide](implement-api-auth-mcp.md#webmcp) [prompt](fix-prompts.md#webmcp) |
| ARD `ard` | `/.well-known/ai-catalog.json` with `specVersion`, `host`, and non-empty `entries` | [guide](implement-api-auth-mcp.md#ard) [prompt](fix-prompts.md#ard) |
| Personal Agent Protocol (Poppy) `personalAgentProtocol` | `/.well-known/poppy.json` (draft 0.1) with valid `organization`/`domain` and interfaces; when auth is declared, a matching OAuth issuer whose metadata lists the domain in `poppy_domains` (informational — does not affect level or score) | [guide](implement-api-auth-mcp.md#personalagentprotocol) [prompt](fix-prompts.md#personalagentprotocol) |

### Commerce, optional (5 checks, scored only if e-commerce signals detected), category key `commerce`

| Check | Pass criteria | Links |
|---|---|---|
| x402 `x402` | API routes return HTTP 402 with valid x402 payment headers | [guide](implement-commerce.md#x402) [prompt](fix-prompts.md#x402) |
| MPP `mpp` | `/openapi.json` with `x-payment-info` extensions on payable operations (Machine Payment Protocol) | [guide](implement-commerce.md#mpp) [prompt](fix-prompts.md#mpp) |
| UCP `ucp` | `/.well-known/ucp` with `protocol_version` and `services` | [guide](implement-commerce.md#ucp) [prompt](fix-prompts.md#ucp) |
| ACP `acp` | `/.well-known/acp.json` with `protocol.name`, `api_base_url`, `transports`, `capabilities.services` | [guide](implement-commerce.md#acp) [prompt](fix-prompts.md#acp) |
| AP2 `ap2` | A2A Agent Card includes AP2 extension with role information | [guide](implement-commerce.md#ap2) [prompt](fix-prompts.md#ap2) |

### Unscored guides

| Check | Pass criteria | Links |
|---|---|---|
| llms.txt `llmsTxt` | Deployed site serves `/llms.txt` as plain text (UTF-8), HTTP 200, H1 title first, short summary paragraph, links to the main content sections | [guide](implement-discoverability-content.md#llmstxt) [prompt](fix-prompts.md#llmstxt) |
| llms-full.txt `llmsFullTxt` | Deployed site serves `/llms-full.txt` as plain text (UTF-8) with HTTP 200 and `/llms.txt` links to it | [guide](implement-discoverability-content.md#llmsfulltxt) [prompt](fix-prompts.md#llmsfulltxt) |

## Where guides and the scanner disagree

Apply the stricter requirement. Each guide records its case:

- OAuth Protected Resource: include `scopes_supported`; `authMd` adds `bearer_methods_supported` with `header`.
- OAuth discovery: include `grant_types_supported` and `response_types_supported`.
- API Catalog: include `status` next to `service-desc` and `service-doc`.
- MCP Server Card: publish at `/.well-known/mcp/server-card.json` (the scanner also accepts `server-cards.json` and `mcp.json`).
- Agent Skills: publish at `/.well-known/agent-skills/index.json`, not the legacy `/.well-known/skills/` path.
- Batch scans: send the full `User-Agent` string from the scan request in SKILL.md.
