# IMPLEMENT: Commerce (Optional)

- Use this file for the optional scanner category Commerce (5 checks).
- API keys: `x402`, `mpp`, `ucp`, `acp`, `ap2`.
- Load prompts from [fix-prompts.md](fix-prompts.md), the scan contract and status values from [scan-api.md](scan-api.md), and the mode router and Check Index from [SKILL.md](../SKILL.md).

## Scoring Rule

- Treat the Commerce category as optional: score its 5 checks only if the scanner detects e-commerce signals.
- Read `isCommerce` and `commerceSignals` in the scan response to see the detection result.
- Expect the values below when the scanner detects no e-commerce signals (sample response fragment).

```json
  "isCommerce": false,
  "commerceSignals": [],
```

- Use these pass criteria:

|Check|API Key|Pass criteria|
|-------|---------|---------------|
|x402|`x402`|API routes return HTTP 402 with valid x402 payment headers|
|MPP|`mpp`|`/openapi.json` with `x-payment-info` extensions on payable operations (Machine Payment Protocol)|
|UCP|`ucp`|`/.well-known/ucp` with `protocol_version` and `services`|
|ACP|`acp`|`/.well-known/acp.json` with `protocol.name`, `api_base_url`, `transports`, `capabilities.services`|
|AP2|`ap2`|A2A Agent Card includes AP2 extension with role information|

## Validate Procedure

- Run this scan request after each Commerce change.

```http
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

- Replace `https://YOUR-SITE.com` with the target site URL.
- Read each check at `checks.commerce.<apiKey>.status`. The success value is `"pass"`.
- No source gives a status path for `ap2`. Infer `checks.commerce.ap2.status` from the category pattern and confirm it in the scan response.

## x402

- Support agent-native HTTP payments with the [x402 protocol](https://x402.org) ([docs](https://docs.x402.org), [GitHub](https://github.com/coinbase/x402)).
- Add x402 payment middleware to your API routes. Use `@x402/express`, `@x402/hono`, or `@x402/next`.
- Configure a facilitator URL and a wallet address.
- Return HTTP 402 with payment requirements on protected routes. Agents fulfill them automatically.
- Check that `checks.commerce.x402.status` is `"pass"`.

## mpp

- Publish an OpenAPI document with MPP payment discovery metadata so AI agents discover your payable endpoints via the [Machine Payment Protocol](https://mpp.dev) ([Payment Discovery Spec](https://paymentauth.org/draft-payment-discovery-00.txt)).
- Serve `/openapi.json` at the site root with HTTP 200.
- Include `x-payment-info` extensions on payable operations.
- Declare in each `x-payment-info`: `intent` (`charge` or `session`), `method` (`tempo`, `stripe`, `lightning`, `card`), and `amount`.
- Optionally include `currency`, `description`, and top-level `x-service-info` with categories.
- Use this example as the base:

```json
{
  "openapi": "3.1.0",
  "info": { "title": "My API", "version": "1.0" },
  "paths": {
    "/api/generate": {
      "post": {
        "x-payment-info": {
          "intent": "charge",
          "method": "stripe",
          "amount": "0.01",
          "currency": "USD",
          "description": "Generate content"
        }
      }
    }
  }
}
```

- Check that `checks.commerce.mpp.status` is `"pass"`.

## ucp

- Enable content payments via the Universal Commerce Protocol per the [UCP Specification](https://ucp.dev/specification/overview/).
- Serve JSON at `/.well-known/ucp` with HTTP 200.
- Include `protocol_version`, `services`, `capabilities`, and `endpoints`. Include all 4 fields, although the scanner pass criterion names only `protocol_version` and `services`.
- Ensure referenced spec URLs and schemas are reachable.
- Check that `checks.commerce.ucp.status` is `"pass"`.

## acp

- Publish an ACP discovery document so AI agents discover your [Agentic Commerce Protocol](https://agenticcommerce.dev) implementation.
- Serve JSON at `/.well-known/acp.json` with HTTP 200.
- Include `protocol.name` set to `"acp"` and `protocol.version`.
- Include `api_base_url` as an absolute HTTP(S) URL.
- Include `transports` as a non-empty array of supported transport types.
- Include `capabilities.services` as a non-empty array of offered services.
- Check that `checks.commerce.acp.status` is `"pass"`.

## ap2

- Declare AP2 support in your A2A Agent Card for agent payments.
- Publish the A2A Agent Card first. See [a2aAgentCard](implement-api-auth-mcp.md#a2aagentcard).
- Add the AP2 extension to your A2A Agent Card at `/.well-known/agent-card.json`. Set your role in it (merchant, shopper, etc.).
- Read the docs at https://ap2-protocol.org/
- Copy the fix prompt from [fix-prompts.md](fix-prompts.md#ap2). It has no Skill line: no `ap2` sub-skill and no Skill URL exist.
