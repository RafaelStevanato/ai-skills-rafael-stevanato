# IMPLEMENT: API, Auth, MCP and Skill Discovery

Contents: Validate Procedure · apiCatalog · oauthDiscovery · oauthProtectedResource · authMd · mcpServerCard · a2aAgentCard · agentSkills · webMcp · ard · personalAgentProtocol

- Use this file for the 10 checks of this category. API keys: `apiCatalog`, `oauthDiscovery`, `oauthProtectedResource`, `authMd`, `mcpServerCard`, `a2aAgentCard`, `agentSkills`, `webMcp`, `ard`, `personalAgentProtocol`.
- Load prompts from [fix-prompts.md](fix-prompts.md), the scan contract and status values from [scan-api.md](scan-api.md), and the Check Index from [checks.md](checks.md).

## Validate Procedure

- Run this scan request after each change.

```http
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

- Replace `https://YOUR-SITE.com` with the target URL.
- Read each check at `checks.discovery.<apiKey>.status`. The success value is `"pass"`.

## apiCatalog

- Publish an API catalog for automated discovery per [RFC 9727](https://www.rfc-editor.org/rfc/rfc9727).
- Serve `/.well-known/api-catalog` with `Content-Type: application/linkset+json` and HTTP 200.
- Include a `linkset` array with entries for each API.
- Give each entry an `anchor` URL and the link relations `service-desc` (OpenAPI spec), `service-doc` (docs), and `status` (health endpoint; optional in the source guide, required here).
- See [RFC 9727 Appendix A](https://www.rfc-editor.org/rfc/rfc9727#appendix-A) for examples.
- Check that `checks.discovery.apiCatalog.status` is `"pass"`.

## oauthDiscovery

- Publish OAuth or OpenID Connect discovery metadata for agent authentication.
- Follow [OpenID Connect Discovery](http://openid.net/specs/openid-connect-discovery-1_0.html) and [RFC 8414](https://www.rfc-editor.org/rfc/rfc8414).
- Serve JSON at `/.well-known/openid-configuration` (OIDC) or `/.well-known/oauth-authorization-server` (OAuth 2.0).
- Include `issuer`, `authorization_endpoint`, `token_endpoint`, `jwks_uri`, and both `grant_types_supported` and `response_types_supported` (the fix prompt template names only the first).
- Cloudflare: use [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/identity/) as identity provider, or use Workers to proxy discovery metadata.
- Check that `checks.discovery.oauthDiscovery.status` is `"pass"`.

## oauthProtectedResource

- Publish OAuth Protected Resource Metadata per [RFC 9728](https://www.rfc-editor.org/rfc/rfc9728).
- Serve JSON at `/.well-known/oauth-protected-resource` with HTTP 200.
- Include `resource` (your resource identifier URL) and `authorization_servers` (array of OAuth/OIDC issuer URLs).
- Include `scopes_supported`: optional in the source guide, required by `authMd`.
- Optionally return `WWW-Authenticate` with `resource_metadata` on 401 responses.
- Cloudflare: use [Workers](https://developers.cloudflare.com/workers/) to serve the metadata endpoint and [Access](https://developers.cloudflare.com/cloudflare-one/) as the authorization server.
- Check that `checks.discovery.oauthProtectedResource.status` is `"pass"`.

## authMd

- Use this guide when the `authMd` check fails or when you add Auth.md to an API or application.
- Serve `/auth.md` from the service root as Markdown with an H1 heading that contains `auth.md` (for example, `# auth.md` or `# Example auth.md`).
- Prefer publishing OAuth Protected Resource Metadata at `/.well-known/oauth-protected-resource` for the resource server.
- Include `resource`, `authorization_servers`, `scopes_supported`, and `bearer_methods_supported` with `header` in the PRM document. This is stricter than [oauthProtectedResource](#oauthprotectedresource).
- Publish OAuth Authorization Server metadata at each advertised authorization server's `/.well-known/oauth-authorization-server` URL.
- Include a valid `issuer` in Authorization Server metadata that matches the issuer advertised in PRM.
- Add an `agent_auth` block with `skill`, `register_uri`, and at least one complete registration method when Authorization Server metadata is available.
- If OAuth metadata is not available, keep `/auth.md` self-contained. In it:
  - identify the agent audience;
  - document registration or provisioning endpoint(s);
  - list supported method(s);
  - explain credential use.
- Never probe `POST /agent/auth` during passive scans. Registration can create accounts, send email, or issue credentials.
- Use public discovery documents as the safe source of truth.
- Check that `checks.discovery.authMd.status` is `"pass"`.
- References:
  - [Auth.md Specification](https://auth-md.com)
  - [RFC 9728 — OAuth Protected Resource Metadata](https://www.rfc-editor.org/rfc/rfc9728)
  - [RFC 8414 — OAuth Authorization Server Metadata](https://www.rfc-editor.org/rfc/rfc8414)

### Flow Metadata

- Publish the metadata for each flow you support.
- **ID-JAG**: include `identity_types_supported: ["identity_assertion"]`, `identity_assertion.assertion_types_supported` with `urn:ietf:params:oauth:token-type:id-jag`, and credential types.
- **ID-JAG**: include `revocation_uri` and the revocation event in `events_supported` when supported. Scanners may warn when they are omitted; detection does not require them.
- **Verified email**: include `identity_assertion.assertion_types_supported` with `verified_email`, credential types, and `claim_uri`.
- **Anonymous**: include `identity_types_supported: ["anonymous"]`, `anonymous.credential_types_supported`, and `claim_uri`.

## mcpServerCard

- Publish an MCP Server Card for agent discovery per [SEP-1649](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2127).
- Serve JSON at `/.well-known/mcp/server-card.json` with HTTP 200.
- Include `serverInfo` with `name` and `version`, a transport `endpoint` URL (e.g., `/mcp` for Streamable HTTP), and the `capabilities` (tools, resources, prompts) the server supports.
- Do not rely on `server-cards.json` or `mcp.json`. The scanner also accepts them.
- Cloudflare: use the [Agents SDK](https://developers.cloudflare.com/agents/) and [Workers](https://developers.cloudflare.com/workers/) to build and deploy MCP servers with server card support.
- Check that `checks.discovery.mcpServerCard.status` is `"pass"`.

## a2aAgentCard

- Publish an A2A Agent Card for agent-to-agent discovery per the [A2A Protocol Specification](https://a2a-protocol.org/latest/specification/).
- Serve JSON at `/.well-known/agent-card.json` with HTTP 200.
- Include `name`, `version`, `description`, and `supportedInterfaces` with service URL and transport protocol.
- List `capabilities` and `skills` (each with `id`, `name`, `description`).
- See [Agent Discovery](https://a2a-protocol.org/latest/topics/agent-discovery/) for the full schema.
- Cloudflare: use the [Agents SDK](https://developers.cloudflare.com/agents/) to build A2A-compatible agents on Workers.
- Check that `checks.discovery.a2aAgentCard.status` is `"pass"`.

## agentSkills

- Publish a skills discovery document per the [Agent Skills Discovery RFC](https://github.com/cloudflare/agent-skills-discovery-rfc) v0.2.0.
- Serve JSON at `/.well-known/agent-skills/index.json` with HTTP 200.
- Include a `$schema` field set to `https://schemas.agentskills.io/discovery/0.2.0/schema.json`.
- Include a `skills` array with these five fields per entry:
  - `name`: skill identifier (lowercase alphanumeric + hyphens)
  - `type`: `"skill-md"` (single SKILL.md) or `"archive"` (bundled archive)
  - `description`: brief description of what the skill does
  - `url`: URL to the skill artifact (SKILL.md file or archive)
  - `digest`: SHA-256 hash of the artifact (`sha256:{hex}`)
- Never publish only to the legacy path `/.well-known/skills/`. The scanner also accepts it.
- Check that `checks.discovery.agentSkills.status` is `"pass"`.

## webMcp

- Expose site tools to AI agents via the browser using the [WebMCP API](https://webmachinelearning.github.io/webmcp/) ([Chrome blog](https://developer.chrome.com/blog/webmcp-epp)).
- Call `navigator.modelContext.registerTool()` for each tool you want to expose.
- Give each tool `name`, `description`, `inputSchema` (JSON Schema), and an `execute` callback.
- Expose key site actions as tools (search, navigation, data retrieval).
- Use an `AbortController` signal to unregister tools.
- Ensure the script runs on page load. The scanner detects the API by loading the page in a browser.
- Flag this mismatch to the user: the scanner pass criterion and the [fix prompt template](fix-prompts.md#webmcp) name `navigator.modelContext.provideContext()`, not `registerTool()`. Do not edit it.
- Check that `checks.discovery.webMcp.status` is `"pass"`.

## ard

- Publish a capability manifest so agents can discover your MCP servers, A2A agents, skills and API tools, per the [ARD spec](https://agenticresourcediscovery.org/) and the [ai-catalog](https://github.com/Agent-Card/ai-catalog) data model.
- The ARD spec is a v0.9 draft. The scanner validates structure only and reports non-conformant identifiers and media types without failing the check.
- `specVersion` refers to the ai-catalog data model, not the ARD spec version, so the example reads `1.0`. The scanner requires only a non-empty string.
- Serve `/.well-known/ai-catalog.json` from the origin root with `Content-Type: application/json`, HTTP 200, and `Access-Control-Allow-Origin: *`.
- Include a `specVersion` string, a non-empty `entries` array, and a `host` object with `displayName` and a stable `identifier`.
- Give each entry an `identifier`, a `displayName`, and a `type` media type.
- Give each entry **exactly one** of `url` or `data`. Never both, never neither (spec §3.4).
- Use `urn:air:<your-fqdn>:<namespace>:<name>` for entry identifiers.
- Add 2-5 `representativeQueries` per entry so registries can build semantic embeddings.

```json
{
  "specVersion": "1.0",
  "host": {
    "displayName": "Example Systems",
    "identifier": "did:web:example.com"
  },
  "entries": [
    {
      "identifier": "urn:air:example.com:server:weather",
      "displayName": "Weather Telemetry Server",
      "type": "application/mcp-server-card+json",
      "url": "https://example.com/mcp/weather.json",
      "representativeQueries": [
        "what is the wind speed in Chicago",
        "get the 5-day forecast for Seattle"
      ]
    }
  ]
}
```

- Check that `checks.discovery.ard.status` is `"pass"`.

### Additional Discovery Mechanisms

- Use the well-known path as the primary mechanism, or any mechanism below to point agents at a manifest hosted elsewhere (spec §6.1). The scanner reports which mechanisms you publish.
- **robots.txt**: add an `Agentmap: https://example.com/ai-catalog.json` directive
- **HTML**: add `<link rel="ai-catalog" href="/.well-known/ai-catalog.json">` to `<head>`
- **DNS**: publish a `_catalog._agents.example.com` TXT record containing `url=https://example.com/.well-known/ai-catalog.json`
- **DNS**: publish a `_search._agents.example.com` SRV record to advertise a semantic search endpoint (reported only; the scanner never queries it)

## personalAgentProtocol

- Publish public discovery metadata for the [Personal Agent Protocol draft 0.1](https://personalagentprotocol.org/docs/spec#3-discovery) at `/.well-known/poppy.json`, and validate its OAuth issuer binding.
- Treat this check as informational. It does not affect level or score.
- Expect the draft to change before version 1.0.

### Website-Only Discovery

- Serve JSON at `https://YOUR-DOMAIN/.well-known/poppy.json`:

```json
{
  "protocol_version": "0.1",
  "organization": { "name": "Example Company", "domain": "example.com" },
  "web": {}
}
```

- Replace the example name and domain with your own.
- Match the domain to the hostname of the requested well-known URL, ignoring leading `www.`.
- Allow HTTPS redirects to a hosting provider, but never let its hostname replace your organization domain.
- Return JSON, not your SPA's HTML fallback.
- Unknown fields and optional extensions are allowed.

### Session-Enabled Interfaces

- Declare only interfaces backed by working implementations:
  - `agent.protocols` entries with `type` and HTTPS `endpoint`
  - `apis` entries with `type`, HTTPS `url`, and `description`
  - `web.browser_session_endpoint` for browser sessions
- Set `auth.issuer` for agent/API declarations and browser-session endpoints.
- Publish RFC 8414 metadata at the issuer with these fields:
  - `issuer` exactly matching `auth.issuer`;
  - `poppy_domains` containing `organization.domain`;
  - HTTPS `token_endpoint` and `revocation_endpoint`;
  - `authorization_endpoint` when `auth.direct` is declared;
  - `device_authorization_endpoint` when `auth.device` is declared.
- For issuer `https://auth.example.com/tenant`, publish metadata at `https://auth.example.com/.well-known/oauth-authorization-server/tenant`.
- Put scope arrays in direct, device, and mediated sign-in declarations.
- Describe the endpoint and credential fields in mediated sign-in. Never put actual credentials or secrets in discovery metadata.
- A pass confirms public discovery and issuer binding only, not functioning sessions, sign-in, API authorization, or conversations.

### Verify

- Scan your site and read `details.issuerValidation` under `checks.discovery.personalAgentProtocol`. Expect `verified`, `notRequired`, `unverified`, `invalid`, or `notChecked`.
- Use the audit evidence to diagnose invalid fields, redirects, and issuer/domain mismatches.
- Network failures and unsupported major versions return `unableToCheck` while retaining available discovery evidence.
