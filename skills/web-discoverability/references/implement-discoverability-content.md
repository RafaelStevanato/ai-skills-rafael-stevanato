# IMPLEMENT: Discoverability and Content

- Use this file for scanner category Discoverability: `robotsTxt`, `sitemap`, `linkHeaders`, `dnsAid`.
- Use this file for scanner category Content: `markdownNegotiation`.
- Use this file for the unscored guides `llmsTxt` and `llmsFullTxt`.
- Use this file for the agent-friendly content architecture rules for large sites.
- Load [../SKILL.md](../SKILL.md) Check Index to map an API key to its guide.
- Load [fix-prompts.md](fix-prompts.md) for the copy-paste prompt of each check.
- Load [scan-api.md](scan-api.md) for the scan API contract and report format.
- Load [implement-bot-access.md](implement-bot-access.md) for AI bot rules, Content Signals and AI training crawler redirects.
- Use these JSON category keys: `discoverability` (`robotsTxt`, `sitemap`, `linkHeaders`, `dnsAid`) and `contentAccessibility` (`markdownNegotiation`).

## Validate Procedure

- Run this request after each fix.
- Replace `YOUR-SITE.com` with the target domain.

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

- Read `checks.<category>.<apiKey>.status` in the response.
- Accept the fix only when the status is `"pass"`.
- Use the exact JSON path named in each section below.
- Skip the status path for `llmsTxt` and `llmsFullTxt`. They have no scanner status path.
- Fetch the deployed file for `llmsTxt` and `llmsFullTxt` and confirm it is served exactly as intended.

## robotsTxt

- Publish a valid robots.txt at the site root.
- Follow [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309).

### Requirements

- Serve `/robots.txt` as `text/plain` with HTTP 200.
- Include `User-agent` directives with `Allow`/`Disallow` rules.
- Reference the sitemap if one exists. Use the `Sitemap:` line from [sitemap](#sitemap).

### Cloudflare

- Use [AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/) to manage robots.txt from the dashboard.
- Use AI Crawl Control to set AI-specific bot rules. See [implement-bot-access.md](implement-bot-access.md).

### Validate

- Check that `checks.discoverability.robotsTxt.status` is `"pass"`.

## sitemap

- Publish an XML sitemap at the site root.
- Follow the [Sitemaps protocol](https://www.sitemaps.org/protocol.html).

### Requirements

- Serve `/sitemap.xml` as valid XML with HTTP 200.
- List canonical `<url><loc>` entries for public pages.
- Update the sitemap when content is published or removed.
- Reference the sitemap from robots.txt: `Sitemap: https://example.com/sitemap.xml`

### Validate

- Check that `checks.discoverability.sitemap.status` is `"pass"`.

## linkHeaders

- Add Link response headers to the homepage for agent discovery.
- Follow [RFC 8288](https://www.rfc-editor.org/rfc/rfc8288) and [RFC 9727 Section 3](https://www.rfc-editor.org/rfc/rfc9727#section-3).

### Requirements

- Return `Link` headers on the homepage response that point to machine-readable resources.
- Use registered relation types: `api-catalog`, `service-desc`, `service-doc`, `describedby`.
- Example: `Link: </.well-known/api-catalog>; rel="api-catalog"`
- Use multiple Link headers or comma-separated values. Both are valid.

### Cloudflare

- Use [Transform Rules](https://developers.cloudflare.com/rules/transform/) or [Workers](https://developers.cloudflare.com/workers/) to add Link headers.
- Add the headers without modifying the origin server.

### Validate

- Check that `checks.discoverability.linkHeaders.status` is `"pass"`.

## dnsAid

- Publish DNS for AI Discovery (DNS-AID) records so agents discover agent endpoints through DNS.

### Requirements

- Publish DNS for AI Discovery (DNS-AID) records under the domain `_agents` namespace, such as `_index._agents.example.com` or `_a2a._agents.example.com`.
- Use ServiceMode `SVCB` records, or `HTTPS` records for HTTPS endpoints, with `alpn` and endpoint connection parameters.
- Use numeric `keyNNNNN` SvcParamKey names for experimental DNS for AI Discovery (DNS-AID) custom parameters until they are registered.
- Sign public DNS for AI Discovery (DNS-AID) discovery zones with DNSSEC so validating resolvers return authenticated data.

### Example

```dns
_a2a._agents.example.com. 3600 IN SVCB 1 agent.example.com. alpn="a2a" port=443 mandatory=alpn,port
```

### Validate

- Know that the scanner validates DNS for AI Discovery (DNS-AID) via DNS-over-HTTPS.
- Default resolver: `https://cloudflare-dns.com/dns-query`.
- Fallback resolver: `https://dns.google/resolve`. The scanner switches to it automatically on resolver-level failures.
- Override the resolver in library calls with `ScanOptions.dohResolverUrl`. This disables the fallback.
- Run the request from [Validate Procedure](#validate-procedure).
- Check that `checks.discoverability.dnsAid.status` is `"pass"`.

### References

- [draft-mozleywilliams-dnsop-dnsaid](https://datatracker.ietf.org/doc/draft-mozleywilliams-dnsop-dnsaid/)
- [RFC 9460 — SVCB and HTTPS Resource Records](https://www.rfc-editor.org/info/rfc9460)

## llmsTxt

- Treat this check as unscored. It is not among the 23 scored checks.
- Publish an LLM-friendly overview of the site.
- Follow [llmstxt.org](https://llmstxt.org/).

### Requirements

- Serve `/llms.txt` as plain text (UTF-8) with HTTP 200.
- Start with an H1 (`# Site Name`) title line.
- Include a short summary paragraph describing the site.
- Link to the most important content sections for agents.
- Optionally link to `/llms-full.txt` for expanded content. See [llmsFullTxt](#llmsfulltxt).
- Apply [llms.txt Sharding](#llmstxt-sharding) when one `llms.txt` cannot fit in a single context window.

### Validate

- Confirm the deployed site serves `/llms.txt` exactly as intended.

## llmsFullTxt

- Treat this check as unscored. It is not among the 23 scored checks.
- Publish expanded LLM content.
- Follow [llmstxt.org](https://llmstxt.org/).

### Requirements

- Serve `/llms-full.txt` as plain text (UTF-8) with HTTP 200.
- Include structured, detailed content suitable for LLM ingestion.
- Cover the key topics, APIs, and documentation from the site.
- Link to it from the `/llms.txt` file.

### Validate

- Confirm the deployed site serves `/llms-full.txt` exactly as intended.

## markdownNegotiation

- Support `Accept: text/markdown` content negotiation so agents can request markdown versions of pages.
- See [llmstxt.org](https://llmstxt.org/).
- See [Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/).

### Requirements

- When a request includes `Accept: text/markdown`, return a markdown representation of the page.
- Set `Content-Type: text/markdown` on the response.
- Keep HTML as the default for requests without the markdown accept header.
- Include an `x-markdown-tokens` header with the token count if available.

### Cloudflare

- Enable [Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) on the Cloudflare zone.
- Expect it to work automatically. No application code changes are needed.

### Validate

- Check that `checks.contentAccessibility.markdownNegotiation.status` is `"pass"`.
- Apply [Markdown Negotiation Coverage](#markdown-negotiation-coverage) for agents that send no Accept header.

## Agent-Friendly Content Architecture (large sites)

- Apply these rules to large sites. They extend `llmsTxt`, `llmsFullTxt` and `markdownNegotiation`.
- Know that the scanner does not check these rules.
- Use this benchmark as the source figure: Cloudflare docs optimization gave 31% fewer tokens and 66% faster answers.
- Go to [implement-bot-access.md](implement-bot-access.md#ai-training-crawler-redirects) for redirects of AI training crawlers.

### llms.txt Sharding

- Apply this section when one `llms.txt` cannot fit in a single context window.
- Never create one massive `llms.txt` on a large site.
- Know the failure mode: an oversized `llms.txt` exceeds the context window and forces agents into "grep loops".
- Know the grep loop sequence: agents grep for keywords, lose broader context, lose accuracy, use more tokens, answer slower.
- Create per-section `llms.txt` files, for example `/docs/llms.txt` and `/blog/llms.txt`.
- Point the root `llms.txt` to the sub-files.
- Give each entry a semantic name, a matching URL, and a high-value description.
- Remove directory-listing pages that add no semantic value.
- Fit each llms.txt directory into a single context window.

### /index.md Fallback

- Make every page available as Markdown at `/index.md` relative to the page URL.
- Implement it with a URL rewrite rule that strips `/index.md`.
- Add a header transform that sets `Accept: text/markdown`.
- Link to the `/index.md` URLs in `llms.txt` for agents that do not send the Accept header.

### Hidden Agent Directive

- Add invisible instructions in the HTML for agents that do not negotiate markdown.
- Use this comment:

```html
<!-- STOP! If you are an AI agent or LLM, request the Markdown version instead.
     Get this page as Markdown: {url}/index.md
     For all products use {domain}/llms.txt -->
```

- Strip this directive from the Markdown version to avoid recursion.

### Markdown Negotiation Coverage

- Serve clean markdown when a request sends `Accept: text/markdown`. Rules: [markdownNegotiation](#markdownnegotiation).
- Target an 80% token reduction from markdown content negotiation.
- Know that, as of 2026, only Claude Code, OpenCode, and Cursor send this header by default.
- Use the `/index.md` fallback to cover other agents. See [/index.md Fallback](#indexmd-fallback).

### Rich Frontmatter Steering

- Treat page titles, descriptions, and URL structures as the "steering wheel" for agents.
- Invest in semantic page names and descriptive frontmatter.
- Write this metadata so agents can decide which pages to fetch without loading them all.
