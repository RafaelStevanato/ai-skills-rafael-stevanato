# SCAN Reference

- Load this file in SCAN mode.
- Read the mode router, levels and check index in [SKILL.md](../SKILL.md).
- Read the prompt templates for every check in [fix-prompts.md](fix-prompts.md).
- Read the fix guides in [implement-discoverability-content.md](implement-discoverability-content.md), [implement-bot-access.md](implement-bot-access.md), [implement-api-auth-mcp.md](implement-api-auth-mcp.md) and [implement-commerce.md](implement-commerce.md).

## Scan Procedure (Steps 1-5 detail)

Run SCAN for these requests:

- Checking whether a site supports agent protocols (MCP, robots.txt, Link headers, etc.)
- Debugging why a site is missing specific agent-readiness checks
- Getting actionable fix instructions to improve a site's agent readiness
- Comparing agent readiness across multiple sites

Run the 5 steps in order every time.

### Step 1: Get the domain

- Ask for the domain when the user gives none.
- Ask this question verbatim:

> Which domain do you want to scan on isitagentready.com?

### Step 2: Scan via API

- Run the scan `curl` from the SCAN Core Flow in [SKILL.md](../SKILL.md).
- Replace `DOMAIN` with the target domain.
- Send the 3 required headers. See [API Endpoint and Required Headers](#api-endpoint-and-required-headers).
- Pass the `enabledChecks` list from [Request Body and Parameters](#request-body-and-parameters).
- Scan 23 checks across 5 categories.
- Ignore the legacy "22 standards" figure.

### Step 3: Generate the Markdown report

- Use the API response to build the report.
- Follow the structure in [Report Template](#report-template).

### Step 4: Generate "How to Implement" prompts

- Generate a prompt block for every check with `status: "fail"` or `status: "neutral"`.
- Take the templates from [fix-prompts.md](fix-prompts.md).
- Build each prompt from 4 parts:
  1. The **Goal** and **Fix** from the template (static per check).
  2. The **Issue** from the API response (`checks.{category}.{check}.message`).
  3. The **Skill URL** pointing to the sub-skill.
  4. The **Docs** links to the relevant RFCs/specs.
- Format each prompt as a fenced code block the user can copy-paste into a coding agent.
- Use the block in [Fix Prompt Block Template](#fix-prompt-block-template).
- Omit the Skill line for `ap2`. No ap2 sub-skill exists.
- Generate no prompt for `unableToCheck`. Re-scan before any fix.

### Step 5: Deliver

- Present the full Markdown report to the user.
- Write the report to the requested path when the user asks to save it.

## Report Template

- Fill `{domain}`, `{level}`, `{levelName}`, `{scannedAt}`, `{passed}`, `{total}` and `{message}` from the API response.
- Use ✅ for `pass`, ❌ for `fail` and ⬜ for `neutral` on each check line.
- Write one check line per check in each category.
- Repeat the category section for every category.
- Insert one prompt block per failing check under "How to Implement".
- Fill the "Next Level" block from `nextLevel`.
- Use these category totals: Discoverability 4, Content 1, Bot Access Control 3, API/Auth/MCP/Skill Discovery 10, Commerce 5.
- Count Commerce checks only when the scanner detects e-commerce signals.

```markdown
# Agent Ready Scan — {domain}

> **Score:** Level {level} — {levelName}
> **Scanned:** {scannedAt}
> **Link:** [View online](https://isitagentready.com/{domain})

## Summary

| Category | Score |
|----------|-------|
| Discoverability | {passed}/{total} |
| Content | {passed}/{total} |
| Bot Access Control | {passed}/{total} |
| API, Auth, MCP & Skill Discovery | {passed}/{total} |
| Commerce (Optional) | {passed}/{total} |

## Details

### Discoverability ({passed}/{total})

- ✅ **robots.txt** — {message}
- ❌ **sitemap.xml** — {message}
  (... for each check ...)

### (... repeat for each category ...)

## 🔧 How to Implement — Agent Prompts

(... one block per failing check, see Step 4 ...)

## Next Level

**Level {nextLevel.target} — {nextLevel.name}**

To reach the next level, implement:
- {nextLevel.requirements[].description}
```

## Fix Prompt Block Template

- Replace `{check name}`, `{message from API}`, `{goal from template}`, `{fix from template}`, `{skill-folder}` and `{docs URLs from template}`.
- Keep the 4-backtick outer fence in the report. The inner fence holds the copy-paste prompt.
- Keep the Skill line as the remote URL.
- Keep the Reference link as the remote URL. Local sub-skill paths do not exist for report readers.

````markdown
#### ❌ {check name}

**Issue:** {message from API}

```
Goal: {goal from template}

Issue: {message from API}

Fix: {fix from template}

Skill: https://isitagentready.com/.well-known/agent-skills/{skill-folder}/SKILL.md

Docs: {docs URLs from template}
```

> 📖 Reference: [{skill-folder}/SKILL.md](https://isitagentready.com/.well-known/agent-skills/{skill-folder}/SKILL.md)
````

## Fix Prompt Field Legend

- Give every failing check a prompt block.
- Write the block so the user can copy-paste it into any coding agent (Cursor, Copilot, Claude, etc.).
- Match the format of the isitagentready.com web UI.
- Replace the `{issue}` placeholder with the actual message from the API response.
- Take the templates for all checks from [fix-prompts.md](fix-prompts.md).

```
Goal: <what the check expects>
Issue: <what was found (dynamic from scan)>
Fix: <step-by-step implementation>
Skill: <URL to the detailed SKILL.md>
Docs: <links to RFCs and specs>
```

## API Endpoint and Required Headers

- Send a POST request with a JSON body.
- Send all 3 headers on every request.
- Send the full `User-Agent` string. Cloudflare protection requires it.

Endpoint:

```
POST https://isitagentready.com/api/scan
Content-Type: application/json
```

Required headers (Cloudflare protection):

```
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36
Referer: https://isitagentready.com/
Origin: https://isitagentready.com
```

## Request Body and Parameters

```json
{
  "url": "https://example.com/",
  "enabledChecks": [
    "robotsTxt", "sitemap", "linkHeaders", "dnsAid",
    "markdownNegotiation",
    "robotsTxtAiRules", "contentSignals", "webBotAuth",
    "apiCatalog", "oauthDiscovery", "oauthProtectedResource", "authMd",
    "mcpServerCard", "a2aAgentCard", "agentSkills", "webMcp", "ard",
    "personalAgentProtocol",
    "x402", "mpp", "ucp", "acp", "ap2"
  ]
}
```

- Treat all checks as optional. Pass only the ones you want to run.
- Set `"format": "agent"` to get a markdown response with fix instructions instead of JSON (useful for piping directly to an LLM).

Minimal request with the `format` parameter:

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://example.com", "format": "agent"}
```

Parameters:

- `url` (required): The URL to scan. Must be a valid HTTP or HTTPS URL.
- `format` (optional): Set to `"agent"` for a markdown response with fix instructions, or `"json"` (default) for structured data.

## Quick-Start Requests

Scan a single domain:

```bash
curl -s -X POST 'https://isitagentready.com/api/scan' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
  -H 'Referer: https://isitagentready.com/' \
  -H 'Origin: https://isitagentready.com' \
  -d '{"url":"https://example.com/"}'
```

Get a markdown report (for LLMs):

```bash
curl -s -X POST 'https://isitagentready.com/api/scan' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
  -H 'Referer: https://isitagentready.com/' \
  -H 'Origin: https://isitagentready.com' \
  -d '{"url":"https://example.com/","format":"agent"}'
```

## MCP Server

- Use the MCP server as an alternative to the HTTP API.
- Connect the agent to this endpoint (Streamable HTTP transport):

```
https://isitagentready.com/mcp
```

- Call the `scan_site` tool with a `url` parameter.
- Pass these arguments: `{"url": "https://example.com"}`.

## Response Structure

```json
{
  "url": "https://example.com",
  "scannedAt": "2026-04-18T13:10:58.788Z",
  "level": 1,
  "levelName": "Basic Web Presence",
  "isCommerce": false,
  "commerceSignals": [],
  "nextLevel": {
    "target": 2,
    "name": "Bot-Aware",
    "requirements": [
      {
        "check": "contentSignals",
        "description": "...",
        "shortPrompt": "...",
        "prompt": "Full implementation prompt...",
        "specUrls": ["https://..."],
        "skillUrl": "https://isitagentready.com/.well-known/agent-skills/.../SKILL.md"
      }
    ]
  },
  "checks": {
    "<category>": {
      "<checkKey>": {
        "status": "pass|fail|neutral",
        "message": "Human-readable conclusion",
        "durationMs": 42,
        "evidence": [
          {
            "action": "fetch|parse|conclude",
            "label": "GET /robots.txt",
            "request": { "url": "...", "method": "GET" },
            "response": {
              "status": 200,
              "headers": { "content-type": "..." },
              "bodyPreview": "..."
            },
            "finding": {
              "outcome": "positive|negative|neutral",
              "summary": "..."
            }
          }
        ]
      }
    }
  }
}
```

Concrete example of the response shape:

```json
{
  "url": "https://example.com",
  "scannedAt": "2026-04-18T13:10:58.788Z",
  "level": 1,
  "levelName": "Basic Web Presence",
  "isCommerce": false,
  "checks": {
    "discoverability": {
      "robotsTxt": {
        "status": "pass",
        "message": "robots.txt exists with valid format",
        "evidence": [ ... ],
        "durationMs": 42
      }
    }
  },
  "nextLevel": {
    "target": 2,
    "name": "Bot-Aware",
    "requirements": [
      {
        "check": "contentSignals",
        "description": "...",
        "prompt": "...",
        "skillUrl": "...",
        "specUrls": ["..."]
      }
    ]
  }
}
```

Evidence values:

| Field | Allowed values |
|-------|----------------|
| `evidence[].action` | `fetch`, `parse`, `conclude` |
| `evidence[].finding.outcome` | `positive`, `negative`, `neutral` |

## Category Keys

- Read one check at `checks.<category>.<checkKey>`.
- Validate a fix: re-scan, then check that `checks.<category>.<checkKey>.status` is `"pass"`.

| JSON category key | Report category | Check keys |
|-------------------|-----------------|------------|
| `discoverability` | Discoverability | `robotsTxt`, `sitemap`, `linkHeaders`, `dnsAid` |
| `contentAccessibility` | Content | `markdownNegotiation` |
| `botAccessControl` | Bot Access Control | `robotsTxtAiRules`, `contentSignals`, `webBotAuth` |
| `discovery` | API, Auth, MCP & Skill Discovery | `apiCatalog`, `oauthDiscovery`, `oauthProtectedResource`, `authMd`, `mcpServerCard`, `a2aAgentCard`, `agentSkills`, `webMcp`, `ard`, `personalAgentProtocol` |
| `commerce` | Commerce (Optional) | `x402`, `mpp`, `ucp`, `acp`, `ap2` |

- Treat `commerce` as the key for `ap2`. It is inferred from the category. No source gives a validate path for `ap2`.
- Example path: `checks.discovery.personalAgentProtocol`.

## Status Values

| Status | Icon | Meaning |
|--------|------|---------|
| `pass` | ✅ | Check passed |
| `fail` | ❌ | Action needed |
| `neutral` | ⬜ | Not applicable / informational |
| `unableToCheck` | none defined | Network failure or unsupported major version. Available discovery evidence is retained |

- Read the 4 values as the union of all sources. Some sources list only 3 values.
- Treat `neutral` on `webBotAuth` as informational. It does not affect the score.
- Treat `personalAgentProtocol` as informational. It does not affect level or score.
- Generate prompts only for `fail` and `neutral`. `unableToCheck` gets no prompt.
- Re-scan before any fix when a check returns `unableToCheck`.
- Read `checks.discovery.personalAgentProtocol.details.issuerValidation` for the issuer result.
- Expect one of these `issuerValidation` values: `verified`, `notRequired`, `unverified`, `invalid`, `notChecked`.
- Use the audit evidence to diagnose invalid fields, redirects, and issuer/domain mismatches.

## Interpreting Results (JSON and Agent formats)

### JSON format

Read these fields:

- `level`: Integer 0-5 indicating overall readiness
- `levelName`: Human-readable level name (e.g., "Agent-Readable")
- `checks`: Object with 5 categories, each containing individual check results
- `nextLevel`: What's needed to reach the next level
- Each check has `status` and a `message`. See [Status Values](#status-values) for the allowed values.
- `isCommerce` and `commerceSignals`: E-commerce detection. Commerce checks count only when e-commerce signals are detected.

Read the level scale (levels 0-5 and their requirements) in [SKILL.md](../SKILL.md).

### Agent format

- Set `"format": "agent"` to get a markdown document.
- Expect these items in the document:
  - The site's current score (e.g., "3/5 Agent-Readable")
  - All failing checks with descriptions and fix instructions
  - If all checks pass, a confirmation message

## Web UI vs API

| Feature | API | Web UI |
|---------|-----|--------|
| Score & Level | ✅ | ✅ |
| Check status + message | ✅ | ✅ |
| Evidence (audit details) | ✅ Full | ✅ Same |
| "How to implement" prompts | ⚠️ Only `nextLevel` (1 prompt) | ✅ All failing checks |
| Skill URLs | ⚠️ Only `nextLevel` | ✅ All checks |

- Rebuild all prompts from the templates in [fix-prompts.md](fix-prompts.md). The API returns only the `nextLevel` prompt.
- Reconstruct the web-quality prompts from API data.

## Batch Scanning

- Add a 2-second delay between requests.
- Write results incrementally to avoid data loss.
- Set `timeout=90` on each request.
- Substitute the full `User-Agent` string from [API Endpoint and Required Headers](#api-endpoint-and-required-headers) for the truncated value in the code below.
- Define `domains` before you run the loop. Replace `# process data...` with real result handling.

Variant A: all 23 checks, result handling left open.

```python
import json, time, urllib.request

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 ...",
    "Referer": "https://isitagentready.com/",
    "Origin": "https://isitagentready.com"
}
CHECKS = ["robotsTxt","sitemap","linkHeaders","dnsAid","markdownNegotiation",
          "robotsTxtAiRules","contentSignals","webBotAuth","apiCatalog",
          "oauthDiscovery","oauthProtectedResource","authMd","mcpServerCard",
          "a2aAgentCard","agentSkills","webMcp","ard","personalAgentProtocol",
          "x402","mpp","ucp","acp","ap2"]

for domain in domains:
    body = json.dumps({"url": f"https://{domain}/", "enabledChecks": CHECKS}).encode()
    req = urllib.request.Request("https://isitagentready.com/api/scan",
                                data=body, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = json.loads(resp.read())
    # process data...
    time.sleep(2)
```

Variant B: url-only request, prints the level per domain.

```python
import json, time, urllib.request

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 ...",
    "Referer": "https://isitagentready.com/",
    "Origin": "https://isitagentready.com"
}

domains = ["example.com", "another.com", "third.com"]

for domain in domains:
    body = json.dumps({"url": f"https://{domain}/"}).encode()
    req = urllib.request.Request(
        "https://isitagentready.com/api/scan",
        data=body, headers=HEADERS
    )
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = json.loads(resp.read())
    
    level = data["level"]
    name = data["levelName"]
    print(f"{domain}: Level {level} — {name}")
    time.sleep(2)
```

## isitagentready.com Own Endpoints

- Use these endpoints of the scanner itself as live references.

| Endpoint | Content |
|----------|---------|
| `/.well-known/api-catalog` | RFC 9727 linkset with scan API and MCP server entries |
| `/.well-known/mcp/server-card.json` | MCP Server Card (Streamable HTTP transport) |
| `/.well-known/mcp.json` | Same MCP Server Card (alternate path) |
| `/.well-known/agent-skills/index.json` | 25 skills in Agent Skills Discovery v0.2.0 format |
| `/llms.txt` | LLM-friendly overview of the scanner |
| `/llms-full.txt` | Full documentation — canonical reference for all 23 checks, pass criteria, and level system |
| `/api/health` | Health check (`{"status":"ok"}`) |
| `/mcp` | Streamable HTTP MCP server with `scan_site` tool |

The API Catalog links the scan API to:

- its documentation (`/llms-full.txt`)
- its service description (`/.well-known/mcp/server-card.json`)
- its health endpoint (`/api/health`)

## Example Output

- Use this example as a format reference only.
- It is illustrative output from an earlier check set. The denominators are stale.
- Current totals are 4, 1, 3, 10 and 5. The Commerce row is missing in the example.
- A site at Level 1 produces a report like this:

````markdown
# Agent Ready Scan — example.com

> **Score:** Level 1 — Basic Web Presence
> **Scanned:** 2026-04-18T13:10:58Z
> **Link:** [View online](https://isitagentready.com/example.com)

## Summary

| Category                          | Score |
|-----------------------------------|-------|
| Discoverability                   | 2/3   |
| Content                           | 0/1   |
| Bot Access Control                | 1/3   |
| API, Auth, MCP & Skill Discovery  | 0/7   |

## Details

### Discoverability (2/3)

- ✅ **robots.txt** — robots.txt exists with valid format
- ✅ **sitemap.xml** — sitemap.xml exists with valid structure
- ❌ **Link headers** — No Link headers found on homepage

### Content (0/1)

- ❌ **Markdown for Agents** — Site does not support Markdown for Agents

(... more categories ...)

## 🔧 How to Implement — Agent Prompts

#### ❌ Link headers

**Issue:** No Link headers found on homepage

```
Goal: Include Link response headers for agent discovery (RFC 8288)

Issue: No Link headers found on homepage

Fix: Add Link response headers to your homepage that point agents to useful
resources. For example: Link: </.well-known/api-catalog>; rel="api-catalog"

Skill: https://isitagentready.com/.well-known/agent-skills/link-headers/SKILL.md

Docs: https://www.rfc-editor.org/rfc/rfc8288
```

> 📖 Reference: [link-headers/SKILL.md](https://isitagentready.com/.well-known/agent-skills/link-headers/SKILL.md)

(... one block per failing check ...)

## Next Level

**Level 2 — Bot-Aware**

To reach the next level, implement:
- Content Signals in robots.txt
````

## Sources

| Resource | URL |
|----------|-----|
| Scanner | https://isitagentready.com |
| API endpoint | `POST https://isitagentready.com/api/scan` |
| MCP server | `https://isitagentready.com/mcp` |
| API Catalog | https://isitagentready.com/.well-known/api-catalog |
| Agent Skills Index | https://isitagentready.com/.well-known/agent-skills/index.json |
| MCP Server Card | https://isitagentready.com/.well-known/mcp/server-card.json |
| Full docs (llms-full.txt) | https://isitagentready.com/llms-full.txt |
| Cloudflare Agents | https://developers.cloudflare.com/agents/ |
| MCP Protocol | https://modelcontextprotocol.io/ |
| Content Signals | https://contentsignals.org/ |
| Agent Skills Discovery | https://github.com/cloudflare/agent-skills-discovery-rfc |
