# Skill Categories Reference

Sources:
- [Lessons from building Claude Code: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills) — Anthropic, Jun 2026
- [Best practices for skill creators](https://agentskills.io/skill-creation/best-practices) — Agent Skills spec
- [Extend Claude with skills](https://code.claude.com/docs/en/skills) — Claude Code docs

---

Assign the target skill to exactly one of the 9 categories below:

- Use the [Classification Decision Tree](#classification-decision-tree) to pick the category.
- Use the category to decide which conditional criteria (15-18) apply in [SKILL.md](../SKILL.md).
- Match each category slug byte-exact. The conditional table in [SKILL.md](../SKILL.md) uses the same slugs.

---

## 1. `library-and-api-reference`

- Classify as `library-and-api-reference` when the skill explains how to correctly use a library, CLI, or SDK.
- Expect internal or public libraries that the model struggles with.
- Expect reference code snippets and gotchas lists.

**Signals:** Has API endpoint docs, CLI command reference, code examples, "how to call X" patterns.

**Examples:** billing-lib, internal-platform-cli, sandbox-proxy

---

## 2. `product-verification`

- Classify as `product-verification` when the skill describes how to test or verify that code is working.
- Expect pairing with Playwright, tmux, or other external tools.

**Signals:** Has test scripts, assertion patterns, Playwright/Cypress flows, "verify that X" instructions.

**Examples:** signup-flow-driver, checkout-verifier, tmux-cli-driver

---

## 3. `data-fetching-and-analysis`

- Classify as `data-fetching-and-analysis` when the skill connects to data and monitoring stacks.
- Expect libraries that fetch data with credentials.
- Expect dashboard IDs.
- Expect common query patterns.

**Signals:** Has database queries, dashboard references, metric/event schemas, "how to find X in our data" patterns.

**Examples:** funnel-query, cohort-compare, grafana, datadog

---

## 4. `business-process-automation`

- Classify as `business-process-automation` when the skill automates repetitive workflows into one command.
- Expect simple instructions.
- Allow dependencies on other skills or MCPs.
- Save results in log files to keep results consistent.

**Signals:** Has "do this weekly/daily" patterns, aggregates from multiple sources, posts to Slack/channels, formats structured output.

**Examples:** standup-post, create-ticket, weekly-recap

---

## 5. `code-scaffolding-and-templates`

- Classify as `code-scaffolding-and-templates` when the skill generates framework boilerplates for a specific function.
- Allow combination with composable scripts.
- Expect natural-language requirements beyond pure code in the scaffolding.

**Signals:** Has templates, "new X" generators, boilerplate structures, asset files to copy.

**Examples:** new-workflow, new-migration, create-app

---

## 6. `code-quality-and-review`

- Classify as `code-quality-and-review` when the skill enforces code quality and helps review code.
- Allow deterministic scripts for robustness.
- Allow runs as hooks or in GitHub Actions.

**Signals:** Has style rules, review checklists, linting patterns, "reject if X" logic, adversarial review patterns.

**Examples:** adversarial-review, code-style, testing-practices

---

## 7. `ci-cd-and-deployment`

- Classify as `ci-cd-and-deployment` when the skill helps fetch, push, and deploy code.
- Allow references to other skills to collect data.

**Signals:** Has deploy commands, build pipelines, PR management, rollout/rollback logic, environment configs.

**Examples:** babysit-pr, deploy-service, cherry-pick-prod

---

## 8. `runbooks`

- Classify as `runbooks` when the skill takes a symptom (alert, error, Slack thread) and walks through a multi-tool investigation.
- Expect a structured report as output.

**Signals:** Has symptom→tool→diagnosis flows, "if you see X check Y" decision trees, report templates.

**Examples:** service-debugging, oncall-runner, log-correlator

---

## 9. `infrastructure-operations`

- Classify as `infrastructure-operations` when the skill performs routine maintenance and ops.
- Expect some destructive actions with guardrails.
- Expect the skill to make it easier to follow best practices in critical operations.

**Signals:** Has cleanup/orphan detection, cost investigation, dependency approval, confirmation gates for destructive actions.

**Examples:** resource-orphans, dependency-management, cost-investigation

---

## Classification Decision Tree

Ask the questions in order.

1. Does it primarily teach how to **call an API/CLI/SDK**? → `library-and-api-reference`
2. Does it **verify** that something works (test, assert, validate)? → `product-verification`
3. Does it **query data** from monitoring/analytics/databases? → `data-fetching-and-analysis`
4. Does it **automate a repeating team process** (standup, report, ticket)? → `business-process-automation`
5. Does it **generate new code/files** from templates? → `code-scaffolding-and-templates`
6. Does it **review/lint/enforce quality** on existing code? → `code-quality-and-review`
7. Does it **build/deploy/ship** code to environments? → `ci-cd-and-deployment`
8. Does it **diagnose problems** from symptoms to structured findings? → `runbooks`
9. Does it perform **infrastructure maintenance/cleanup** with guardrails? → `infrastructure-operations`

If a skill spans multiple categories, pick the one that describes its **primary action**.

Define **primary action** as what the user gets when they invoke the skill.
