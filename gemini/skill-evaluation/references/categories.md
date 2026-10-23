# Skill Categories Reference

Sources:
- [Lessons from building Claude Code: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills) — Anthropic, Jun 2026 (origin of the nine categories, which apply to any agent's skills)
- [Best practices for skill creators](https://agentskills.io/skill-creation/best-practices) — Agent Skills spec, which Antigravity skills follow
- [Agent skills](https://antigravity.google/docs/skills/) — Google Antigravity docs

- Assign the target skill to exactly one category below, using the [Classification Decision Tree](#classification-decision-tree).
- Use the category to select conditional criteria 15-18 in [SKILL.md](../SKILL.md). Match slugs byte-exact.

## 1. `library-and-api-reference`

Explains how to use an internal or public library, CLI, or SDK that the model struggles with. Often includes reference code snippets and gotchas lists.

**Signals:** Has API endpoint docs, CLI command reference, code examples, "how to call X" patterns.

**Examples:** billing-lib, internal-platform-cli, sandbox-proxy

## 2. `product-verification`

Tests or verifies that code works. Often paired with Playwright, tmux, or other external tools.

**Signals:** Has test scripts, assertion patterns, Playwright/Cypress flows, "verify that X" instructions.

**Examples:** signup-flow-driver, checkout-verifier, tmux-cli-driver

## 3. `data-fetching-and-analysis`

Connects to data and monitoring stacks. Includes libraries that fetch data with credentials, dashboard IDs, and common query patterns.

**Signals:** Has database queries, dashboard references, metric/event schemas, "how to find X in our data" patterns.

**Examples:** funnel-query, cohort-compare, grafana, datadog

## 4. `business-process-automation`

Automates repetitive workflows into one command. Usually simple instructions, but may depend on other skills or MCPs. Save results in log files for consistency.

**Signals:** Has "do this weekly/daily" patterns, aggregates from multiple sources, posts to Slack/channels, formats structured output.

**Examples:** standup-post, create-ticket, weekly-recap

## 5. `code-scaffolding-and-templates`

Generates framework boilerplate for a specific function. May combine with composable scripts. Suits natural-language requirements beyond pure code.

**Signals:** Has templates, "new X" generators, boilerplate structures, asset files to copy.

**Examples:** new-workflow, new-migration, create-app

## 6. `code-quality-and-review`

Enforces code quality and helps review code. May use deterministic scripts for robustness and run as hooks or in GitHub Actions.

**Signals:** Has style rules, review checklists, linting patterns, "reject if X" logic, adversarial review patterns.

**Examples:** adversarial-review, code-style, testing-practices

## 7. `ci-cd-and-deployment`

Helps fetch, push, and deploy code. May reference other skills to collect data.

**Signals:** Has deploy commands, build pipelines, PR management, rollout/rollback logic, environment configs.

**Examples:** babysit-pr, deploy-service, cherry-pick-prod

## 8. `runbooks`

Takes a symptom (alert, error, Slack thread) and walks through a multi-tool investigation. Produces a structured report.

**Signals:** Has symptom→tool→diagnosis flows, "if you see X check Y" decision trees, report templates.

**Examples:** service-debugging, oncall-runner, log-correlator

## 9. `infrastructure-operations`

Performs routine maintenance and ops, some involving destructive actions with guardrails. Makes best practices easier to follow in critical operations.

**Signals:** Has cleanup/orphan detection, cost investigation, dependency approval, confirmation gates for destructive actions.

**Examples:** resource-orphans, dependency-management, cost-investigation

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

If a skill spans multiple categories, pick the one that describes its **primary action**: what the user gets when they invoke the skill.
