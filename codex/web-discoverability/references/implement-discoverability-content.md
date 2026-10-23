# IMPLEMENT: Discoverability and Content

- Use this file for `robotsTxt`, `sitemap`, `linkHeaders`, `dnsAid` (JSON category `discoverability`), `markdownNegotiation` (JSON category `contentAccessibility`), unscored `llmsTxt` and `llmsFullTxt`, and the large-site content rules.
- Map an API key to its guide with the Check Index in [checks.md](checks.md). Get the prompt of a check from [fix-prompts.md](fix-prompts.md).

## Validate Procedure

- Run this request after each fix. Replace `YOUR-SITE.com` with the target domain.

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

- Read `checks.<category>.<apiKey>.status` in the response. Use the exact JSON path named in each section.
- Accept the fix only when the status is `"pass"`.
- `llmsTxt` and `llmsFullTxt` have no scanner status path. Fetch the deployed file instead and confirm it is served exactly as intended.

## robotsTxt

- Publish a valid robots.txt at the site root per [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309). Serve `/robots.txt` as `text/plain` with HTTP 200.
- Include `User-agent` directives with `Allow`/`Disallow` rules.
- Reference the sitemap if one exists, with the `Sitemap:` line from [sitemap](#sitemap).
- On Cloudflare, manage robots.txt and AI-specific bot rules from the dashboard with [AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/). See [implement-bot-access.md](implement-bot-access.md).
- Validate: `checks.discoverability.robotsTxt.status` is `"pass"`.

## sitemap

- Publish an XML sitemap at the site root per the [Sitemaps protocol](https://www.sitemaps.org/protocol.html). Serve `/sitemap.xml` as valid XML with HTTP 200.
- List canonical `<url><loc>` entries for public pages.
- Update the sitemap when content is published or removed.
- Reference the sitemap from robots.txt: `Sitemap: https://example.com/sitemap.xml`
- Validate: `checks.discoverability.sitemap.status` is `"pass"`.

## linkHeaders

- Add Link response headers to the homepage per [RFC 8288](https://www.rfc-editor.org/rfc/rfc8288) and [RFC 9727 Section 3](https://www.rfc-editor.org/rfc/rfc9727#section-3).
- Point the `Link` headers to machine-readable resources.
- Use registered relation types: `api-catalog`, `service-desc`, `service-doc`, `describedby`.
- Example: `Link: </.well-known/api-catalog>; rel="api-catalog"`
- Allow multiple Link headers or comma-separated values.
- On Cloudflare, add the headers with [Transform Rules](https://developers.cloudflare.com/rules/transform/) or [Workers](https://developers.cloudflare.com/workers/). Do not modify the origin server.
- Validate: `checks.discoverability.linkHeaders.status` is `"pass"`.

## dnsAid

- Publish DNS for AI Discovery (DNS-AID) records so agents discover agent endpoints through DNS.
- Use the domain `_agents` namespace, such as `_index._agents.example.com` or `_a2a._agents.example.com`.
- Use ServiceMode `SVCB` records, or `HTTPS` records for HTTPS endpoints, with `alpn` and endpoint connection parameters.
- Use numeric `keyNNNNN` SvcParamKey names for experimental custom parameters until they are registered.
- Sign public DNS-AID discovery zones with DNSSEC so validating resolvers return authenticated data.

```dns
_a2a._agents.example.com. 3600 IN SVCB 1 agent.example.com. alpn="a2a" port=443 mandatory=alpn,port
```

- The scanner validates DNS-AID via DNS-over-HTTPS. Default resolver: `https://cloudflare-dns.com/dns-query`.
- Fallback resolver: `https://dns.google/resolve`. The scanner switches to it automatically on resolver-level failures.
- Override the resolver in library calls with `ScanOptions.dohResolverUrl`. This disables the fallback.
- Validate: `checks.discoverability.dnsAid.status` is `"pass"`.
- References: [draft-mozleywilliams-dnsop-dnsaid](https://datatracker.ietf.org/doc/draft-mozleywilliams-dnsop-dnsaid/), [RFC 9460 — SVCB and HTTPS Resource Records](https://www.rfc-editor.org/info/rfc9460).

## llmsTxt

- Treat this guide as unscored (not among the 23 scored checks).
- Publish an LLM-friendly overview of the site per [llmstxt.org](https://llmstxt.org/). Serve `/llms.txt` as plain text (UTF-8) with HTTP 200.
- Start with an H1 (`# Site Name`) title line.
- Include a short summary paragraph describing the site. Link to the most important content sections for agents.
- Optionally link to `/llms-full.txt` for expanded content. See [llmsFullTxt](#llmsfulltxt).
- Apply [llms.txt Sharding](#llmstxt-sharding) on large sites.
- Validate: fetch `/llms.txt` from the deployed site.

## llmsFullTxt

- Treat this guide as unscored (not among the 23 scored checks).
- Publish expanded LLM content per [llmstxt.org](https://llmstxt.org/). Serve `/llms-full.txt` as plain text (UTF-8) with HTTP 200.
- Include structured, detailed content suitable for LLM ingestion. Cover the key topics, APIs, and documentation from the site.
- Link to it from the `/llms.txt` file.
- Validate: fetch `/llms-full.txt` from the deployed site.

## markdownNegotiation

- Support `Accept: text/markdown` content negotiation so agents can request markdown versions of pages. See [llmstxt.org](https://llmstxt.org/).
- When a request includes `Accept: text/markdown`, return a markdown representation of the page.
- Set `Content-Type: text/markdown` on the response.
- Keep HTML as the default for requests without the markdown accept header.
- Include an `x-markdown-tokens` header with the token count if available.
- On Cloudflare, enable [Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) on the zone. No code changes are needed.
- Validate: `checks.contentAccessibility.markdownNegotiation.status` is `"pass"`.
- Apply [Markdown Negotiation Coverage](#markdown-negotiation-coverage) for agents that send no Accept header.

## Agent-Friendly Content Architecture (large sites)

- Apply these rules to large sites. They extend `llmsTxt`, `llmsFullTxt` and `markdownNegotiation`. The scanner does not check them.
- Benchmark: Cloudflare docs optimization gave 31% fewer tokens and 66% faster answers.
- For AI training crawler redirects, see [implement-bot-access.md](implement-bot-access.md#ai-training-crawler-redirects).

### llms.txt Sharding

- Apply this section when one `llms.txt` cannot fit in a single context window.
- Never create one massive `llms.txt` on a large site. It exceeds the context window and forces agents into "grep loops".
- Grep loop: agents grep for keywords, lose broader context, lose accuracy, use more tokens, answer slower.
- Create per-section `llms.txt` files, for example `/docs/llms.txt` and `/blog/llms.txt`.
- Point the root `llms.txt` to the sub-files.
- Give each entry a semantic name, a matching URL, and a high-value description.
- Remove directory-listing pages that add no semantic value.
- Fit each llms.txt directory into a single context window.

### /index.md Fallback

- Make every page available as Markdown at `/index.md` relative to the page URL.
- Implement it with a URL rewrite rule that strips `/index.md` and a header transform that sets `Accept: text/markdown`.
- Link to the `/index.md` URLs in `llms.txt` for agents that do not send the Accept header.

### Hidden Agent Directive

- Add this invisible comment to the HTML for agents that do not negotiate markdown:

```html
<!-- STOP! If you are an AI agent or LLM, request the Markdown version instead.
     Get this page as Markdown: {url}/index.md
     For all products use {domain}/llms.txt -->
```

- Strip this directive from the Markdown version to avoid recursion.

### Markdown Negotiation Coverage

- Serve clean markdown for `Accept: text/markdown` requests per [markdownNegotiation](#markdownnegotiation).
- Target an 80% token reduction from markdown content negotiation.
- As of 2026, only Claude Code, OpenCode, and Cursor send this header by default.
- Use the `/index.md` fallback to cover other agents. See [/index.md Fallback](#indexmd-fallback).

### Rich Frontmatter Steering

- Treat page titles, descriptions, and URL structures as the "steering wheel" for agents.
- Invest in semantic page names and descriptive frontmatter.
- Write this metadata so agents choose which pages to fetch without loading them all.
