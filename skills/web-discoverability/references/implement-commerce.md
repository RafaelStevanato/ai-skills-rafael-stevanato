# IMPLEMENT: Commerce (Optional)

- Use this file for the optional scanner category Commerce (5 checks).
- Read each result under the JSON key `checks.commerce.<apiKey>`.
- Use these API keys: `x402`, `mpp`, `ucp`, `acp`, `ap2`.
- Load the copy-paste prompt for each check from [fix-prompts.md](fix-prompts.md).
- Load the scan contract and status values from [scan-api.md](scan-api.md).
- Return to [SKILL.md](../SKILL.md) for the mode router and the Check Index.

## Scoring Rule

- Treat the Commerce category as optional.
- Score the 5 Commerce checks only if the scanner detects e-commerce signals.
- Read `isCommerce` and `commerceSignals` in the scan response to see the detection result.
- Expect the values below when the scanner detects no e-commerce signals (fragment of the sample response).

```json
  "isCommerce": false,
  "commerceSignals": [],
```

- Use the pass criteria below.

| Check | API Key | Pass criteria |
|-------|---------|---------------|
| x402 | `x402` | API routes return HTTP 402 with valid x402 payment headers |
| MPP | `mpp` | `/openapi.json` with `x-payment-info` extensions on payable operations (Machine Payment Protocol) |
| UCP | `ucp` | `/.well-known/ucp` with `protocol_version` and `services` |
| ACP | `acp` | `/.well-known/acp.json` with `protocol.name`, `api_base_url`, `transports`, `capabilities.services` |
| AP2 | `ap2` | A2A Agent Card includes AP2 extension with role information |

## Validate Procedure

- Run the scan request below after each Commerce change.
- Use the same request for every check in this file.

```http
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

- Replace `https://YOUR-SITE.com` with the target site URL.
- Read the status of one check at `checks.commerce.<apiKey>.status`.
- Treat `"pass"` as the success value.
- Use the exact `Check that ...` line in each section below.
- Note: no source gives a status path for `ap2`. Infer `checks.commerce.ap2.status` from the category pattern and confirm it in the scan response.

## x402

- Support agent-native HTTP payments with the [x402 protocol](https://x402.org).
- Read the [docs](https://docs.x402.org).
- Read the [GitHub](https://github.com/coinbase/x402) repository.
- Add x402 payment middleware to your API routes.
- Use `@x402/express`, `@x402/hono`, or `@x402/next` middleware.
- Configure a facilitator URL.
- Configure a wallet address.
- Return HTTP 402 with payment requirements on protected routes.
- Expect agents to fulfill the payment requirements automatically.
- Check that `checks.commerce.x402.status` is `"pass"`.

## mpp

- Publish an OpenAPI document with MPP payment discovery metadata.
- Goal: AI agents discover your payable endpoints via the [Machine Payment Protocol](https://mpp.dev) ([spec](https://paymentauth.org/draft-payment-discovery-00.txt)).
- Serve `/openapi.json` at the site root with HTTP 200.
- Include `x-payment-info` extensions on payable operations.
- Declare `intent` in each `x-payment-info`. Allowed values: `charge`, `session`.
- Declare `method` in each `x-payment-info`. Allowed values: `tempo`, `stripe`, `lightning`, `card`.
- Declare `amount` in each `x-payment-info`.
- Optionally include `currency`.
- Optionally include `description`.
- Optionally include top-level `x-service-info` with categories.
- Use the example below as the base.

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
- References:
  - [Machine Payment Protocol](https://mpp.dev)
  - [Payment Discovery Spec](https://paymentauth.org/draft-payment-discovery-00.txt)

## ucp

- Enable content payments via the Universal Commerce Protocol per the [UCP Specification](https://ucp.dev/specification/overview/).
- Serve JSON at `/.well-known/ucp` with HTTP 200.
- Include `protocol_version`.
- Include `services`.
- Include `capabilities`.
- Include `endpoints`.
- Include all 4 fields. The scanner pass criterion names only `protocol_version` and `services`.
- Ensure referenced spec URLs and schemas are reachable.
- Check that `checks.commerce.ucp.status` is `"pass"`.

## acp

- Publish an ACP discovery document so AI agents discover your [Agentic Commerce Protocol](https://agenticcommerce.dev) implementation.
- Serve JSON at `/.well-known/acp.json` with HTTP 200.
- Include `protocol.name` set to `"acp"`.
- Include `protocol.version`.
- Include `api_base_url` as an absolute HTTP(S) URL.
- Include `transports` as a non-empty array of supported transport types.
- Include `capabilities.services` as a non-empty array of offered services.
- Check that `checks.commerce.acp.status` is `"pass"`.

## ap2

- Declare AP2 support in your A2A Agent Card for agent payments.
- Add the AP2 extension to your A2A Agent Card at `/.well-known/agent-card.json`.
- Set your role in the AP2 extension (merchant, shopper, etc.).
- Goal: agents discover your payment capabilities.
- Publish the A2A Agent Card first. See [a2aAgentCard](implement-api-auth-mcp.md#a2aagentcard).
- Read the docs at https://ap2-protocol.org/.
- Copy the fix prompt from [fix-prompts.md](fix-prompts.md#ap2).
- Expect no Skill line in the `ap2` fix prompt. No `ap2` sub-skill and no Skill URL exist.
- Validate with the `ap2` note in the Validate Procedure.
