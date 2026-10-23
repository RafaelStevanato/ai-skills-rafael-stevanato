# IMPLEMENT: API, Auth, MCP and Skill Discovery

- Use this file for the scanner category API, Auth, MCP and Skill Discovery (10 checks).
- Read each result under the JSON key `checks.discovery.<apiKey>`.
- Use these API keys: `apiCatalog`, `oauthDiscovery`, `oauthProtectedResource`, `authMd`, `mcpServerCard`, `a2aAgentCard`, `agentSkills`, `webMcp`, `ard`, `personalAgentProtocol`.
- Load the copy-paste prompt for each check from [fix-prompts.md](fix-prompts.md).
- Load the scan contract and status values from [scan-api.md](scan-api.md).
- Return to [SKILL.md](../SKILL.md) for the mode router and the Check Index.

## Validate Procedure

- Run the scan request below after each change.
- Use the same request for every check in this file.

```http
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

- Replace `https://YOUR-SITE.com` with the target site URL.
- Read the status of one check at `checks.discovery.<apiKey>.status`.
- Treat `"pass"` as the success value.
- Use the exact `Check that ...` line in each section below.
- Treat `personalAgentProtocol` as informational. It does not affect level or score.

## apiCatalog

- Publish an API catalog for automated discovery per [RFC 9727](https://www.rfc-editor.org/rfc/rfc9727).
- Serve `/.well-known/api-catalog` with `Content-Type: application/linkset+json` and HTTP 200.
- Include a `linkset` array with entries for each API.
- Give each entry an `anchor` URL.
- Give each entry the link relation `service-desc` (OpenAPI spec).
- Give each entry the link relation `service-doc` (docs).
- Give each entry the link relation `status` (health endpoint).
- Include `status` even though the source guide marks it optional. The fix prompt template lists it.
- See [RFC 9727 Appendix A](https://www.rfc-editor.org/rfc/rfc9727#appendix-A) for examples.
- Check that `checks.discovery.apiCatalog.status` is `"pass"`.

## oauthDiscovery

- Publish OAuth or OpenID Connect discovery metadata so agents can authenticate with your APIs.
- Follow [OpenID Connect Discovery](http://openid.net/specs/openid-connect-discovery-1_0.html) and [RFC 8414](https://www.rfc-editor.org/rfc/rfc8414).
- Serve JSON at `/.well-known/openid-configuration` (OIDC) or `/.well-known/oauth-authorization-server` (OAuth 2.0).
- Include `issuer`, `authorization_endpoint`, `token_endpoint`, `jwks_uri`.
- List `grant_types_supported`.
- List `response_types_supported`.
- Include both list fields. The fix prompt template names only `grant_types_supported`.
- Cloudflare option: use [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/identity/) as identity provider.
- Cloudflare option: use Workers to proxy discovery metadata.
- Check that `checks.discovery.oauthDiscovery.status` is `"pass"`.

## oauthProtectedResource

- Publish OAuth Protected Resource Metadata so agents can discover how to authenticate per [RFC 9728](https://www.rfc-editor.org/rfc/rfc9728).
- Serve JSON at `/.well-known/oauth-protected-resource` with HTTP 200.
- Include `resource` (your resource identifier URL).
- Include `authorization_servers` (array of OAuth/OIDC issuer URLs).
- Include `scopes_supported`.
- Include `scopes_supported` even though the source guide marks it optional. The fix prompt template lists it, and `authMd` requires it.
- Optionally return `WWW-Authenticate` with `resource_metadata` on 401 responses.
- Cloudflare option: use [Workers](https://developers.cloudflare.com/workers/) to serve the metadata endpoint.
- Cloudflare option: use [Access](https://developers.cloudflare.com/cloudflare-one/) as the authorization server.
- Check that `checks.discovery.oauthProtectedResource.status` is `"pass"`.

## authMd

- Use this guide when the scanner reports the `authMd` check as failing.
- Use this guide when you add the Auth.md standard to an API or application.
- Publish Auth.md support for agent registration.
- Serve `/auth.md` from the service root as Markdown with an H1 heading that contains `auth.md` (for example, `# auth.md` or `# Example auth.md`).
- Prefer publishing OAuth Protected Resource Metadata at `/.well-known/oauth-protected-resource` for the resource server.
- Include `resource`, `authorization_servers`, `scopes_supported`, and `bearer_methods_supported` with `header` in the PRM document.
- Require `scopes_supported` and `bearer_methods_supported` with `header` here. This is stricter than [oauthProtectedResource](#oauthprotectedresource).
- Publish OAuth Authorization Server metadata at each advertised authorization server's `/.well-known/oauth-authorization-server` URL.
- Include a valid `issuer` in Authorization Server metadata and ensure it matches the issuer advertised in PRM.
- Add an `agent_auth` block with `skill`, `register_uri`, and at least one complete registration method when Authorization Server metadata is available.
- If OAuth metadata is not available, keep `/auth.md` self-contained.
- In a self-contained `/auth.md`, identify the agent audience.
- In a self-contained `/auth.md`, document registration or provisioning endpoint(s).
- In a self-contained `/auth.md`, list supported method(s).
- In a self-contained `/auth.md`, explain credential use.
- Never probe `POST /agent/auth` during passive scans.
- Registration can create accounts, send email, or issue credentials.
- Use public discovery documents as the safe source of truth.
- Check that `checks.discovery.authMd.status` is `"pass"`.
- Use these references:
  - [Auth.md Specification](https://auth-md.com)
  - [RFC 9728 — OAuth Protected Resource Metadata](https://www.rfc-editor.org/rfc/rfc9728)
  - [RFC 8414 — OAuth Authorization Server Metadata](https://www.rfc-editor.org/rfc/rfc8414)

### Flow Metadata

- Publish the metadata that matches each flow you support.
- **ID-JAG**: include `identity_types_supported: ["identity_assertion"]`, `identity_assertion.assertion_types_supported` with `urn:ietf:params:oauth:token-type:id-jag`, and credential types.
- **ID-JAG**: include `revocation_uri` and the revocation event in `events_supported` when supported.
- Scanners may warn when `revocation_uri` and the revocation event are omitted. They are not required for detection.
- **Verified email**: include `identity_assertion.assertion_types_supported` with `verified_email`, credential types, and `claim_uri`.
- **Anonymous**: include `identity_types_supported: ["anonymous"]`, `anonymous.credential_types_supported`, and `claim_uri`.

## mcpServerCard

- Publish an MCP Server Card for agent discovery per [SEP-1649](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2127).
- Serve JSON at `/.well-known/mcp/server-card.json` with HTTP 200.
- Include `serverInfo` with `name` and `version`.
- Include a transport `endpoint` URL (e.g., `/mcp` for Streamable HTTP).
- List `capabilities` (tools, resources, prompts) the server supports.
- Implement the card at `/.well-known/mcp/server-card.json`.
- Note that the scanner also accepts `server-cards.json` or `mcp.json` as the card location.
- Do not rely on the alternate names. Use the `server-card.json` path.
- Cloudflare option: use the [Agents SDK](https://developers.cloudflare.com/agents/) and [Workers](https://developers.cloudflare.com/workers/) to build and deploy MCP servers with server card support.
- Check that `checks.discovery.mcpServerCard.status` is `"pass"`.

## a2aAgentCard

- Publish an A2A Agent Card for agent-to-agent discovery per the [A2A Protocol Specification](https://a2a-protocol.org/latest/specification/).
- Serve JSON at `/.well-known/agent-card.json` with HTTP 200.
- Include `name`, `version`, and `description`.
- Include `supportedInterfaces` with service URL and transport protocol.
- List `capabilities` and `skills` (each with `id`, `name`, `description`).
- See [Agent Discovery](https://a2a-protocol.org/latest/topics/agent-discovery/) for the full schema.
- Cloudflare option: use the [Agents SDK](https://developers.cloudflare.com/agents/) to build A2A-compatible agents on Workers.
- Check that `checks.discovery.a2aAgentCard.status` is `"pass"`.

## agentSkills

- Publish a skills discovery document per the [Agent Skills Discovery RFC](https://github.com/cloudflare/agent-skills-discovery-rfc) v0.2.0.
- Serve JSON at `/.well-known/agent-skills/index.json` with HTTP 200.
- Include a `$schema` field set to `https://schemas.agentskills.io/discovery/0.2.0/schema.json`.
- Include a `skills` array.
- Give each `skills` entry these five fields:
  - `name`: skill identifier (lowercase alphanumeric + hyphens)
  - `type`: `"skill-md"` (single SKILL.md) or `"archive"` (bundled archive)
  - `description`: brief description of what the skill does
  - `url`: URL to the skill artifact (SKILL.md file or archive)
  - `digest`: SHA-256 hash of the artifact (`sha256:{hex}`)
- Implement the new path `/.well-known/agent-skills/index.json`.
- Note that the scanner also accepts the legacy path `/.well-known/skills/`.
- Never publish only to the legacy path.
- Check that `checks.discovery.agentSkills.status` is `"pass"`.

## webMcp

- Expose site tools to AI agents via the browser using the [WebMCP API](https://webmachinelearning.github.io/webmcp/) ([Chrome blog](https://developer.chrome.com/blog/webmcp-epp)).
- Call `navigator.modelContext.registerTool()` for each tool you want to expose.
- Give each tool `name`, `description`, `inputSchema` (JSON Schema), and an `execute` callback.
- Expose your site's key actions as tools (search, navigation, data retrieval).
- Use an `AbortController` signal to unregister tools when no longer needed.
- Ensure the script runs on page load. The scanner detects the API by loading the page in a browser.
- Note that the scanner pass criterion names `navigator.modelContext.provideContext()`.
- Note that the fix prompt template in [fix-prompts.md](fix-prompts.md#webmcp) also names `provideContext()`.
- Keep each source wording as written. Do not edit the fix prompt template.
- Flag this API mismatch (`registerTool()` vs `provideContext()`) to the user.
- Check that `checks.discovery.webMcp.status` is `"pass"`.

## ard

- Publish a capability manifest so agents can discover your MCP servers, A2A agents, skills and API tools.
- Follow the [ARD spec](https://agenticresourcediscovery.org/) and the [ai-catalog](https://github.com/Agent-Card/ai-catalog) data model.
- Note that the ARD spec is a v0.9 draft.
- Note that the scanner validates structure only.
- Note that the scanner reports non-conformant identifiers and media types without failing the check.
- Note that `specVersion` refers to the ai-catalog data model, not the ARD spec version. This is why the example below reads `1.0`.
- Note that the scanner only requires `specVersion` to be a non-empty string.
- Serve `/.well-known/ai-catalog.json` from the origin root with `Content-Type: application/json`, HTTP 200, and `Access-Control-Allow-Origin: *`.
- Include a `specVersion` string and a non-empty `entries` array.
- Add a `host` object with `displayName` and a stable `identifier`.
- Give each entry an `identifier`, a `displayName`, and a `type` media type.
- Give each entry **exactly one** of `url` or `data`. Never both, never neither (spec §3.4).
- Use `urn:air:<your-fqdn>:<namespace>:<name>` for entry identifiers.
- Add 2-5 `representativeQueries` per entry so registries can build semantic embeddings.

Example:

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

- Use the well-known path as the primary mechanism.
- Use any mechanism below to point agents at a manifest hosted elsewhere (spec §6.1).
- Expect the scanner to report which mechanisms you publish.
- **robots.txt**: add an `Agentmap: https://example.com/ai-catalog.json` directive
- **HTML**: add `<link rel="ai-catalog" href="/.well-known/ai-catalog.json">` to `<head>`
- **DNS**: publish a `_catalog._agents.example.com` TXT record containing `url=https://example.com/.well-known/ai-catalog.json`
- **DNS**: publish a `_search._agents.example.com` SRV record to advertise a semantic search endpoint (reported only; the scanner never queries it)

## personalAgentProtocol

- Publish public discovery metadata for the [Personal Agent Protocol draft 0.1](https://personalagentprotocol.org/docs/spec#3-discovery).
- Publish `/.well-known/poppy.json` (draft 0.1) and validate its OAuth issuer binding.
- Treat this check as informational. It does not affect readiness levels or percentage scores.
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

- Replace the example organization with your actual name and domain.
- Match the domain to the hostname of the requested well-known URL, ignoring leading `www.`.
- HTTPS redirects to a hosting provider are allowed.
- Never let the hosting provider's hostname replace your organization domain.
- Return JSON, not your SPA's HTML fallback.
- Unknown fields and optional extensions are allowed.

### Session-Enabled Interfaces

- Declare the interfaces you actually implement.
- Use `agent.protocols` entries with `type` and HTTPS `endpoint`.
- Use `apis` entries with `type`, HTTPS `url`, and `description`.
- Use `web.browser_session_endpoint` for browser sessions.
- Set `auth.issuer` for agent/API declarations and browser-session endpoints.
- Publish RFC 8414 metadata at the issuer with these fields:
  - `issuer` exactly matching `auth.issuer`;
  - `poppy_domains` containing `organization.domain`;
  - HTTPS `token_endpoint` and `revocation_endpoint`;
  - `authorization_endpoint` when `auth.direct` is declared;
  - `device_authorization_endpoint` when `auth.device` is declared.
- For issuer `https://auth.example.com/tenant`, publish metadata at `https://auth.example.com/.well-known/oauth-authorization-server/tenant`.
- Put scope arrays in direct, device, and mediated sign-in declarations.
- Describe the endpoint and credential fields in mediated sign-in.
- Never put actual credentials or secrets in discovery metadata.
- Publish only capabilities backed by working implementations.
- Note that a pass confirms public discovery and issuer binding only.
- Note that a pass does not confirm functioning sessions, sign-in, API authorization, or conversations.

### Verify

- Scan your site and inspect `checks.discovery.personalAgentProtocol`.
- Read `details.issuerValidation`.
- Expect one of these `issuerValidation` values: `verified`, `notRequired`, `unverified`, `invalid`, or `notChecked`.
- Use the audit evidence to diagnose invalid fields, redirects, and issuer/domain mismatches.
- Network failures and unsupported major versions return `unableToCheck` while retaining available discovery evidence.
