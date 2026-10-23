# Fix Prompt Templates

## Usage Rules

- Use these templates for the web UI "How to implement — paste into your coding agent" prompts in Step 4 of the SCAN flow ([scan-api.md](scan-api.md)).
- Rebuild the prompt of every failing check from its template. The API returns only the `nextLevel` prompt.
- Copy each code block exactly, including the remote `Skill: https://isitagentready.com/...` line. Replace only `{issue}` with the `message` from the API response.
- Open the IMPLEMENT reference through the `Guide:` link under each block.
- Omit the `Skill:` line for ap2. No local `ap2/` folder exists. Cover AP2 through the parent prompt and the A2A Agent Card extension.
- Treat llmsTxt and llmsFullTxt as unscored (outside the 23 scanner checks).

## robotsTxt

```
Goal: Publish /robots.txt with clear crawl rules

Issue: {issue}

Fix: Create /robots.txt at the site root with explicit User-agent directives and allow/disallow rules for key paths. Ensure it is plain text and returns 200.

Skill: https://isitagentready.com/.well-known/agent-skills/robots-txt/SKILL.md

Docs: https://www.rfc-editor.org/rfc/rfc9309
```

Guide: [robotsTxt](implement-discoverability-content.md#robotstxt)

## sitemap

```
Goal: Publish /sitemap.xml with canonical URLs

Issue: {issue}

Fix: Generate /sitemap.xml listing canonical URLs, keep it updated on publish, and reference it from /robots.txt.

Skill: https://isitagentready.com/.well-known/agent-skills/sitemap/SKILL.md

Docs: https://www.sitemaps.org/protocol.html
```

Guide: [sitemap](implement-discoverability-content.md#sitemap)

## linkHeaders

```
Goal: Include Link response headers for agent discovery (RFC 8288)

Issue: {issue}

Fix: Add Link response headers to your homepage that point agents to useful resources. For example: Link: </.well-known/api-catalog>; rel="api-catalog" to advertise your API catalog, or Link: </docs/api>; rel="service-doc" for API documentation. See RFC 8288 for the Link header format and IANA Link Relations for registered relation types.

Skill: https://isitagentready.com/.well-known/agent-skills/link-headers/SKILL.md

Docs: https://www.rfc-editor.org/rfc/rfc8288, https://www.rfc-editor.org/rfc/rfc9727#section-3
```

Guide: [linkHeaders](implement-discoverability-content.md#linkheaders)

## markdownNegotiation

```
Goal: Return HTML responses as markdown when agents request it

Issue: {issue}

Fix: Enable Markdown for Agents so requests with Accept: text/markdown return a markdown version of your HTML response while HTML stays the default for browsers. Confirm the response uses Content-Type: text/markdown (and x-markdown-tokens if available).

Skill: https://isitagentready.com/.well-known/agent-skills/markdown-negotiation/SKILL.md

Docs: https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/
```

Guide: [markdownNegotiation](implement-discoverability-content.md#markdownnegotiation)

## robotsTxtAiRules

```
Goal: Add User-agent rules for AI crawlers like GPTBot, Claude-Web, and others

Issue: {issue}

Fix: Add explicit User-agent entries for AI crawlers (GPTBot, OAI-SearchBot, Claude-Web, Google-Extended) with allow/disallow rules that match your policy.

Skill: https://isitagentready.com/.well-known/agent-skills/ai-rules/SKILL.md

Docs: https://www.rfc-editor.org/rfc/rfc9309, https://developers.cloudflare.com/ai-crawl-control/
```

Guide: [robotsTxtAiRules](implement-bot-access.md#robotstxtairules)

## contentSignals

```
Goal: Declare AI content usage preferences with Content Signals in robots.txt

Issue: {issue}

Fix: Add Content-Signal directives to your robots.txt declaring preferences for ai-train, search, and ai-input. For example:
Content-Signal: ai-train=no, search=yes, ai-input=no

Skill: https://isitagentready.com/.well-known/agent-skills/content-signals/SKILL.md

Docs: https://contentsignals.org/, https://datatracker.ietf.org/doc/draft-romm-aipref-contentsignals/
```

Guide: [contentSignals](implement-bot-access.md#contentsignals)

## webBotAuth

```
Goal: Let your site identify itself as a bot with Web Bot Auth

Issue: {issue}

Fix: Publish a JWKS at /.well-known/http-message-signatures-directory so your site can identify itself when it sends bot or agent requests. Receiving sites can use it to verify those signed requests.

Skill: https://isitagentready.com/.well-known/agent-skills/web-bot-auth/SKILL.md

Docs: https://datatracker.ietf.org/wg/webbotauth/about/, https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/
```

Guide: [webBotAuth](implement-bot-access.md#webbotauth)

## apiCatalog

```
Goal: Publish an API catalog for automated API discovery (RFC 9727)

Issue: {issue}

Fix: Create /.well-known/api-catalog returning application/linkset+json with a "linkset" array. Each entry should include an "anchor" URL for the API and link relations for service-desc (OpenAPI spec), service-doc (documentation), and status (health endpoint). See RFC 9727 Appendix A for examples.

Skill: https://isitagentready.com/.well-known/agent-skills/api-catalog/SKILL.md

Docs: https://www.rfc-editor.org/rfc/rfc9727, https://www.rfc-editor.org/rfc/rfc9264
```

Guide: [apiCatalog](implement-api-auth-mcp.md#apicatalog)

## oauthDiscovery

```
Goal: Publish OAuth/OIDC discovery metadata so agents can authenticate with your APIs

Issue: {issue}

Fix: If your site has protected APIs, publish /.well-known/openid-configuration (for OpenID Connect) or /.well-known/oauth-authorization-server (for pure OAuth 2.0) with your issuer, authorization_endpoint, token_endpoint, jwks_uri, and grant_types_supported. This allows AI agents to programmatically discover how to authenticate.

Skill: https://isitagentready.com/.well-known/agent-skills/oauth-discovery/SKILL.md

Docs: http://openid.net/specs/openid-connect-discovery-1_0.html, https://www.rfc-editor.org/rfc/rfc8414
```

Guide: [oauthDiscovery](implement-api-auth-mcp.md#oauthdiscovery)

## oauthProtectedResource

```
Goal: Publish OAuth Protected Resource Metadata so agents can discover how to authenticate

Issue: {issue}

Fix: Publish /.well-known/oauth-protected-resource with your resource identifier, authorization_servers (list of OAuth/OIDC issuer URLs that can issue tokens for this resource), and scopes_supported. This tells agents how to obtain access tokens for your protected APIs.

Skill: https://isitagentready.com/.well-known/agent-skills/oauth-protected-resource/SKILL.md

Docs: https://www.rfc-editor.org/rfc/rfc9728
```

Guide: [oauthProtectedResource](implement-api-auth-mcp.md#oauthprotectedresource)

## mcpServerCard

```
Goal: Publish an MCP Server Card for agent discovery

Issue: {issue}

Fix: Serve an MCP Server Card (SEP-1649) at /.well-known/mcp/server-card.json with serverInfo (name, version), transport endpoint, and capabilities. The schema is being standardized at https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2127

Skill: https://isitagentready.com/.well-known/agent-skills/mcp-server-card/SKILL.md

Docs: https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2127
```

Guide: [mcpServerCard](implement-api-auth-mcp.md#mcpservercard)

## agentSkills

```
Goal: Publish an agent skills discovery index

Issue: {issue}

Fix: Publish a skills discovery index at /.well-known/agent-skills/index.json (per the Agent Skills Discovery RFC v0.2.0). Include a $schema field, and a skills array where each entry has name, type, description, url, and a sha256 digest.

Skill: https://isitagentready.com/.well-known/agent-skills/agent-skills/SKILL.md

Docs: https://github.com/cloudflare/agent-skills-discovery-rfc, https://agentskills.io/
```

Guide: [agentSkills](implement-api-auth-mcp.md#agentskills)

## webMcp

```
Goal: Support WebMCP to expose site tools to AI agents via the browser

Issue: {issue}

Fix: Implement the WebMCP API by calling navigator.modelContext.provideContext() with tool definitions that expose your site's key actions to AI agents. Each tool needs a name, description, inputSchema (JSON Schema), and an execute callback function.

Skill: https://isitagentready.com/.well-known/agent-skills/webmcp/SKILL.md

Docs: https://webmachinelearning.github.io/webmcp/, https://developer.chrome.com/blog/webmcp-epp
```

Guide: [webMcp](implement-api-auth-mcp.md#webmcp)

## ard

```
Goal: Publish an ARD capability manifest at /.well-known/ai-catalog.json

Issue: {issue}

Fix: Serve /.well-known/ai-catalog.json with Content-Type application/json, HTTP 200, and Access-Control-Allow-Origin: *. Include specVersion, a host object (displayName + identifier), and a non-empty entries array. Each entry needs identifier, displayName, type, exactly one of url or data, and 2-5 representativeQueries. Use urn:air:<fqdn>:<namespace>:<name> for entry identifiers.

Skill: https://isitagentready.com/.well-known/agent-skills/ard/SKILL.md

Docs: https://agenticresourcediscovery.org/, https://github.com/Agent-Card/ai-catalog
```

Guide: [ard](implement-api-auth-mcp.md#ard)

## personalAgentProtocol

```
Goal: Publish Personal Agent Protocol (Poppy) discovery at /.well-known/poppy.json

Issue: {issue}

Fix: Publish the manifest and any required RFC 8414 metadata. Website-only declarations can use web: {} without auth. When agent protocols, APIs, or a browser session endpoint are declared, set auth.issuer and publish issuer metadata with a matching issuer, poppy_domains containing organization.domain, and HTTPS token_endpoint and revocation_endpoint. Informational: does not affect level or score.

Skill: https://isitagentready.com/.well-known/agent-skills/personal-agent-protocol/SKILL.md

Docs: https://personalagentprotocol.org/docs/spec#3-discovery
```

Guide: [personalAgentProtocol](implement-api-auth-mcp.md#personalagentprotocol)

## x402

```
Goal: Support x402 protocol for agent-native HTTP payments

Issue: {issue}

Fix: Add x402 payment middleware to your API routes to enable AI agents to pay for access via HTTP. Use @x402/express, @x402/hono, or @x402/next middleware with a facilitator URL and wallet address. Protected routes will return HTTP 402 with payment requirements that agents can fulfill automatically.

Skill: https://isitagentready.com/.well-known/agent-skills/x402/SKILL.md

Docs: https://x402.org, https://github.com/coinbase/x402, https://docs.x402.org
```

Guide: [x402](implement-commerce.md#x402)

## ucp

```
Goal: Enable content payments via Universal Commerce Protocol

Issue: {issue}

Fix: Serve /.well-known/ucp with protocol version, services, capabilities, and endpoints, and ensure spec URLs and schemas are reachable.

Skill: https://isitagentready.com/.well-known/agent-skills/ucp/SKILL.md

Docs: https://ucp.dev/specification/overview/
```

Guide: [ucp](implement-commerce.md#ucp)

## acp

```
Goal: Publish ACP discovery metadata so agents can discover your commerce API

Issue: {issue}

Fix: Serve /.well-known/acp.json at the origin root with protocol.name "acp", protocol.version, api_base_url, supported transports, and capabilities.services so agents can discover your ACP implementation without creating a checkout session first.

Skill: https://isitagentready.com/.well-known/agent-skills/acp/SKILL.md

Docs: https://agenticcommerce.dev, https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/pull/137
```

Guide: [acp](implement-commerce.md#acp)

## a2aAgentCard

```
Goal: Publish an A2A Agent Card for agent-to-agent discovery

Issue: {issue}

Fix: Serve JSON at /.well-known/agent-card.json with name, version, description, supportedInterfaces (service URL and transport), capabilities, and skills (each with id, name, description). See the A2A Protocol Specification for the full schema.

Skill: https://isitagentready.com/.well-known/agent-skills/a2a-agent-card/SKILL.md

Docs: https://a2a-protocol.org/latest/specification/, https://a2a-protocol.org/latest/topics/agent-discovery/
```

Guide: [a2aAgentCard](implement-api-auth-mcp.md#a2aagentcard)

## dnsAid

```
Goal: Publish DNS for AI Discovery (DNS-AID) records for DNS-based agent discovery

Issue: {issue}

Fix: Publish SVCB or HTTPS records under your domain's _agents namespace (e.g. _a2a._agents.example.com or _index._agents.example.com). Use alpn and port SvcParamKeys with mandatory=alpn,port. Use numeric keyNNNNN names for experimental custom parameters until registered. Sign zones with DNSSEC.

Skill: https://isitagentready.com/.well-known/agent-skills/dns-aid/SKILL.md

Docs: https://datatracker.ietf.org/doc/draft-mozleywilliams-dnsop-dnsaid/, https://www.rfc-editor.org/info/rfc9460
```

Guide: [dnsAid](implement-discoverability-content.md#dnsaid)

## authMd

```
Goal: Publish Auth.md agent registration discovery metadata

Issue: {issue}

Fix: Serve /auth.md from the site root as Markdown with an H1 heading containing "auth.md". Include OAuth Protected Resource Metadata at /.well-known/oauth-protected-resource and Authorization Server metadata. Add an agent_auth block with skill, register_uri, and registration methods. If OAuth is not available, keep /auth.md self-contained with audience, registration endpoints, and credential use.

Skill: https://isitagentready.com/.well-known/agent-skills/auth-md/SKILL.md

Docs: https://auth-md.com
```

Guide: [authMd](implement-api-auth-mcp.md#authmd)

## mpp

```
Goal: Support MPP (Machine Payment Protocol) for agent-native HTTP payments

Issue: {issue}

Fix: Serve /openapi.json at the site root with HTTP 200. Include x-payment-info extensions on payable operations declaring intent (charge or session), method (tempo, stripe, lightning, card), and amount. Optionally include currency, description, and top-level x-service-info with categories.

Skill: https://isitagentready.com/.well-known/agent-skills/mpp/SKILL.md

Docs: https://mpp.dev, https://paymentauth.org/draft-payment-discovery-00.txt
```

Guide: [mpp](implement-commerce.md#mpp)

## llmsTxt

```
Goal: Publish an LLM-friendly overview at /llms.txt

Issue: {issue}

Fix: Serve /llms.txt as plain text (UTF-8) with HTTP 200. Start with an H1 title line, include a short summary paragraph, and link to the most important content sections for agents. Optionally link to /llms-full.txt for expanded content.

Skill: https://isitagentready.com/.well-known/agent-skills/llms-txt/SKILL.md

Docs: https://llmstxt.org/
```

Guide: [llmsTxt](implement-discoverability-content.md#llmstxt)

## llmsFullTxt

```
Goal: Publish expanded LLM content at /llms-full.txt

Issue: {issue}

Fix: Serve /llms-full.txt as plain text (UTF-8) with HTTP 200. Include structured, detailed content suitable for LLM ingestion covering key topics, APIs, and documentation. Link to it from your /llms.txt file.

Skill: https://isitagentready.com/.well-known/agent-skills/llms-full-txt/SKILL.md

Docs: https://llmstxt.org/
```

Guide: [llmsFullTxt](implement-discoverability-content.md#llmsfulltxt)

## ap2

```
Goal: Declare AP2 support in your A2A Agent Card for agent payments

Issue: {issue}

Fix: Add AP2 extension to your A2A Agent Card at /.well-known/agent-card.json with your role (merchant, shopper, etc.) so agents can discover your payment capabilities.

Docs: https://ap2-protocol.org/
```

Guide: [ap2](implement-commerce.md#ap2)
