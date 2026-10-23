# IMPLEMENT: Bot Access Control

- Use this file for scanner category `botAccessControl` (`robotsTxtAiRules`, `contentSignals`, `webBotAuth`) and for the GEO rules on AI training crawler redirects and crawler access.
- Use Cloudflare [AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/) to manage AI bot rules (`robotsTxtAiRules`) and Content Signals (`contentSignals`) from the dashboard, without editing robots.txt manually.
- Load [../SKILL.md](../SKILL.md) for the Check Index, levels, and output gates.
- Load [scan-api.md](scan-api.md) for the full scan contract and status values.
- Load the prompt template of each check from [fix-prompts.md](fix-prompts.md).
- Apply [Crawler Policy in GEO Mode](#crawler-policy-in-geo-mode) to `robotsTxtAiRules` and `contentSignals` when the task is GEO.

## Validate Procedure

- Send this request after each change. Replace `YOUR-SITE.com` with the target site.

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

- Read the status at the JSON path in the table below.
- Expect `"pass"` for `robotsTxtAiRules` and `contentSignals`.
- Treat `webBotAuth` as informational. A neutral result does not affect the score.
- Re-scan before any fix when a status is `unableToCheck`.

|Check|JSON path|Pass criteria|
|-------|-----------|---------------|
|`robotsTxtAiRules`|`checks.botAccessControl.robotsTxtAiRules.status`|robots.txt contains `User-agent` entries for known AI bots (GPTBot, Claude-Web, Google-Extended, etc.)|
|`contentSignals`|`checks.botAccessControl.contentSignals.status`|robots.txt contains `Content-Signal` directives with ai-train/search/ai-input|
|`webBotAuth`|`checks.botAccessControl.webBotAuth.status`|`/.well-known/http-message-signatures-directory` exists with valid JWKS (informational — neutral does not affect score)|

## robotsTxtAiRules

- Add explicit `User-agent` entries in robots.txt per [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309) for AI-specific bots: `GPTBot`, `OAI-SearchBot`, `Claude-Web`, `Google-Extended`, `Amazonbot`, `anthropic-ai`, `Bytespider`, `CCBot`, `Applebot-Extended`
- Set `Allow` and/or `Disallow` rules matching your content policy.
- Never rely on a wildcard `User-agent: *` block alone. Explicit AI bot entries are required.
- Let the site owner choose allow or disallow for each bot.
- Check that `checks.botAccessControl.robotsTxtAiRules.status` is `"pass"`.

## contentSignals

- Declare AI content usage preferences in robots.txt using [Content Signals](https://contentsignals.org/) ([IETF draft](https://datatracker.ietf.org/doc/draft-romm-aipref-contentsignals/)).
- Add `Content-Signal` directives to your robots.txt under the relevant `User-agent` block.
- Declare preferences for `ai-train`, `search`, and `ai-input`, as in this example:

```
Content-Signal: ai-train=no, search=yes, ai-input=no
```

- Let the site owner choose the values. The example shows the format only.
- Check that `checks.botAccessControl.contentSignals.status` is `"pass"`.

## webBotAuth

- Use Web Bot Auth so your site can identify itself when it sends bot or agent requests, per the [IETF WebBotAuth WG](https://datatracker.ietf.org/wg/webbotauth/about/).
- Publish a JWKS (JSON Web Key Set) at `/.well-known/http-message-signatures-directory` with at least one public key for signature verification.
- Sign requests sent by your bot or agent so receiving sites can verify them.
- Include `Signature-Agent` and `Signature-Input` headers on those signed requests.
- Use [Web Bot Auth on Cloudflare](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/) for built-in verification of bot request signatures.
- Check that `checks.botAccessControl.webBotAuth.status` is `"pass"`.

## AI Training Crawler Redirects

- Apply this rule in GEO step 4.5. No scanner check covers it.
- Identify AI training crawlers (GPTBot, Google-Extended, etc.)
- Redirect them away from deprecated/outdated content to current versions.
- Keep archives open: humans still access archives; LLMs only see accurate content. This prevents outdated recommendations in AI responses.
- See [robotsTxtAiRules](#robotstxtairules) for the full bot name list.
- Load [geo.md](geo.md) for the full 4.5 workflow.

## Crawler Policy in GEO Mode

- Confirm `robots.txt` allows AI crawlers (do not block Perplexity, ChatGPT, etc.) before delivering GEO output.
- Flag `ai-input=no` and any block on AI search or answer bots as a citation risk.
- Keep the owner policy in SCAN and IMPLEMENT mode.
- Keep the training crawler redirect rule above; it is compatible with this policy.
- Load [geo.md](geo.md) step 5 for the single copy of this rule.
