# GEO Reference (Generative Engine Optimization)

Load this file in GEO mode.
Return to [SKILL.md](../SKILL.md) for the mode router.

## Quick Actions Menu

Present these options at the start of the interaction:

1. **Full GEO Audit**: Analyze the current page. Deliver a score and a prioritized roadmap.
2. **Roundup Page Builder**: Create a comparison page optimized for LLMs.
3. **Terminology Optimizer**: Generate new titles, metas, and headings aligned with LLM searches.
4. **FAQ + Schema Generator**: Create a complete FAQ set with schema markup.
5. **Community Signal Booster**: Structure a strategy to generate reviews on Product Hunt and Reddit.
6. **Citation Rate Test Kit**: Create 50 ready-made prompts for visibility measurement.
7. **FULL PACKAGE**: Execute all of the above as a complete optimization package using Multi Agents.

Default to option 1 (Full GEO Audit) when the user requests no specific action.
Execute the steps below according to the selected action or user need.

## 1. Measurement and Tracking

- Begin by evaluating the current state of AI visibility. AI visibility is measurable: treat it like SEO.
- Create an initial set of 50–100 real prompts. Test them against ChatGPT, Google AI Overview, Perplexity, and Grok.
- Define the main metric: **Citation Rate** (% of LLM responses that cite the brand or product).

## 2. Terminology Alignment

- Map how people actually query LLMs. Do not rely solely on Google keyword patterns.
- Adjust titles, meta descriptions, and headings to reflect natural LLM terminology.
- Example: Prefer "AI dictation and speech-to-text software" over "AI dictation apps".

## 3. Page Format and Structure

- Recommend and create the formats that LLMs value most. Prioritize **Roundup / Comparison pages** (for example, "The best [category] in 2026").
- Include these elements in each optimized page:
  - Title aligned with LLM terminology.
  - 8–12 products with authentic community reviews.
  - Comparison table.
  - Complete FAQPage schema.
  - "What the community is saying" section (embed or cite Product Hunt and Reddit content).
- Do not produce purely self-promotional listicles. LLMs detect and deprioritize them.

## 4. Community Signals

- Encourage real reviews and discussions on Product Hunt, Reddit, and Quora. They are the strongest trust signals for LLMs.
- Embed or cite community content directly on the page to strengthen trust signals.

## 4.5 Agent-Friendly Content Architecture (pointer)

- Source figure: Cloudflare docs optimization gave 31% fewer tokens and 66% faster answers.
- Load [implement-discoverability-content.md](implement-discoverability-content.md#agent-friendly-content-architecture-large-sites) for the llms.txt, `/index.md`, hidden directive, markdown negotiation and frontmatter rules.
- Load [implement-bot-access.md](implement-bot-access.md#ai-training-crawler-redirects) for the redirect rules for AI training crawlers.

## 5. Technical and Structured Data

- Add JSON-LD with FAQPage schema.
- Add Product schema where applicable.
- Keep traditional SEO and structured data as the foundation: JSON-LD schemas remain essential for LLM retrieval.
- Confirm `robots.txt` allows AI crawlers. Do not block Perplexity, ChatGPT, and similar crawlers.
- Flag `ai-input=no` and any block on AI search or answer bots as citation risks. See [implement-bot-access.md](implement-bot-access.md#crawler-policy-in-geo-mode).

## 6. Continuous Monitoring

- Run tests every week, or after each model update.
- Adjust terminology and add community content when models change. Model updates change citation patterns.

## Authority Rule

- Build one high-signal, well-structured page. It outperforms dozens of thin or weak pages. Authority beats volume.

## Quality Checklist

Verify each item before delivering any output:

- [ ] Citation Rate baseline is defined, or a test kit has been created.
- [ ] Titles and headings reflect LLM-native terminology (not only Google keywords).
- [ ] Page structure includes a comparison table and FAQPage schema.
- [ ] Community signals (Product Hunt, Reddit) are referenced or embedded.
- [ ] `robots.txt` does not block major AI crawlers.
- [ ] JSON-LD schemas are present and valid.
- [ ] Monitoring cadence is defined (weekly or post-model-update).
- [ ] No purely self-promotional listicles were produced (LLMs detect and deprioritize them).
- [ ] Bot-blocking risks have been flagged (for example, Perplexity has temporarily blocked some platforms).

## Source

Insights come from X posts and the Product Hunt 2026 case study. The case study showed measurable gains in LLM citation rates through community signal integration and terminology alignment.
