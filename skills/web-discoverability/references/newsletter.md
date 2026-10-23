# NEWSLETTER Reference (Substack)

Load this file in NEWSLETTER mode.
Return to [SKILL.md](../SKILL.md) for the mode router.

## Parameters

| Parameter     | Description                                            | Default                          |
|---------------|--------------------------------------------------------|----------------------------------|
| `topic`       | Subject or draft content to work with                  | Infer from the conversation      |
| `goal`        | Primary objective: `format`, `seo`, `growth`, `monetize` | `format` + `seo` if unspecified |
| `language`    | Output language                                        | Match the user's message language |

## 1. Clarify Scope

- Identify which goals apply: formatting, SEO, growth, monetization.
- Confirm the topic.
- Produce SEO metadata and a formatted structure outline simultaneously when the request is ambiguous.

## 2. Visual Formatting

- Structure content with `Heading 1`, `Heading 2`, and `Heading 3` to improve readability and facilitate search-engine crawling.
- Apply the centering technique in [Text Centering](#text-centering).
- Apply the rules in the subsections below.

### Text Centering

- Note: the Substack minimalist editor has no standard center-align button for regular body text.
- Select the text to center.
- Click "Insert Quote".
- Choose "Pull Quote".
- Use this method to highlight key phrases or statistics.
- Expect the Pull Quote to create a visual break.

### Content Hierarchy

- Use **Heading 1** through **Heading 3** to create a clear, scannable structure.
- Keep paragraphs short: 3–5 sentences max.
- Check readability in both email and web views.
- Use **Bold**, *Italics*, ~~Strikethrough~~, and hyperlinks to guide the reader's eye and improve scannability.
- Use bullet points, numbered lists, and dividers to break up long sections.

### Quotes

- Use **Block Quote** to attribute long excerpts from external sources.
- Use **Pull Quote** to emphasize a key phrase or statistic.
- Expect a Pull Quote to render centered and visually distinct.

### Visuals and Media

- Insert images, GIFs, or charts to break up heavy text.
- Choose the image width by the visual weight needed: **standard**, **wide**, or **full**.
- Always add a **caption** to every image.
- Always add **alt text** to every image. See the Image Alt Text rule in [3. SEO Metadata](#3-seo-metadata).
- Know the purpose: alt text serves accessibility and organic SEO simultaneously.

### Interactive Engagement Tools

- Insert native engagement tools at natural breakpoints in the post.
- Use **native buttons**: "Subscribe", "Share your post", "Leave a comment".
- Use **custom buttons**: insert any URL to drive a specific reader action (e.g., download, survey, external link).
- Use **polls** as a passive engagement and retention mechanism.
- Know the limit: polls are exclusive to paying subscribers.
- Count a poll as the required engagement element only in content for paying subscribers.
- Use a button or a comment prompt as the required engagement element in all other content.

## 3. SEO Metadata

Produce the following fields for every post.

- **Title**
  - Write 40–60 characters.
  - Use clear modifiers, keywords, and authority signals (e.g., "Tested", "Complete Guide").
  - Include the primary keyword.
  - Avoid vague or clickbait phrasing.
- **URL Slug**
  - Use 3–5 main keywords only.
  - Ban auto-generated numbers.
  - Ban dates, to keep the post evergreen.
  - Example: `/substack-seo-strategy`.
- **Meta Description**
  - Write 155–160 characters.
  - Include the primary keyword.
  - Include an implicit call to action.
- **Image Alt Text**
  - Describe the image for accessibility.
  - Incorporate article keywords organically.
  - Add alt text to every image.

Consult the worked example in [SEO Output Example](#seo-output-example).

### SEO Output Example

#### Input

> "Create SEO definitions for an article about how digital nomads can choose the best smartwatches."

#### Output

| Field            | Value                                                                                                      | Notes                                                        |
|------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| **Title**        | The 5 Best Smartwatches for Digital Nomads in 2025                                                         | Utility trigger, audience specification, timeliness signal   |
| **Meta Description** | Discover the essential smartwatch features for trails and global travel. Read the complete guide for Digital Nomads and choose your gear. | 155–160 chars, includes keyword and implicit CTA             |
| **URL Slug**     | `/smartwatches-digital-nomads`                                                                             | 3–5 keywords, no dates, evergreen-friendly                   |

#### SEO Rules Applied

- Title is 50 characters (within the 40–60 char target for maximum CTR).
- Slug contains no auto-generated numbers or filler words.
- Meta description closes with an action-oriented phrase without being a hard sell.

#### Auditor Note

- Know the gap: the example Meta Description has 137 characters, not 155–160.
- Enforce the 155–160 character rule in all new output.
- Never copy the 137-character length of the example.

## Email Subject Line Rules

- Keep subject lines under 50 characters to prevent truncation on mobile.
- Ban ALL CAPS.
- Ban excessive exclamation marks.
- Ban spam-trigger phrases like "Buy Now" or "Act Now".
- Test deliverability: check spam scores before sending to the full list.

## 4. Growth

- **Substack Notes**
  - Publish short snippets derived from the post to Notes immediately after publishing.
  - Leave authentic comments on related publications to build name recognition.
- **Recommendations rotation**
  - Review Analytics monthly to identify which partner newsletters drive inbound traffic.
  - Rotate recommended partners every 30–60 days to maintain reciprocal growth.

## 5. Monetization (Free to Paid)

- **Tease & Convert**
  - Publish the core article freely.
  - Gate a utility bonus (template, spreadsheet, prompt set, audio) behind the paywall.
  - Prove value before asking for payment.
  - Never cut the paywall mid-sentence.
- **VIP outreach**
  - In the Dashboard, filter subscribers by engagement score (4–5 stars).
  - Send a targeted direct message.
  - Offer a special rate or an exclusive invite to the paid tier.
- **Welcome email**
  - Customize the automated welcome email.
  - Introduce the author.
  - Set publishing cadence expectations.
  - Link to the three best existing articles.
  - Never leave the platform default.
- **Homepage taxonomy**
  - Group posts into Tags (equivalent to newspaper sections).
  - Add the Tags to the navigation bar via *Website Themes* for advanced content discovery.

## Quality Checklist

Check each item before delivering output.

- [ ] Write a title of 40–60 characters that contains the primary keyword.
- [ ] Write a URL slug of 3–5 words with no numbers and no dates.
- [ ] Write a meta description of 155–160 characters with a keyword and an implicit CTA.
- [ ] Add alt text to all images.
- [ ] Keep the subject line (if applicable) under 50 characters and free of spam triggers.
- [ ] Include at least one native engagement element (button, poll, or comment prompt). Count a poll only for paying-subscriber content.
- [ ] Place the paywall by the Tease & Convert model (not a mid-sentence cut).
- [ ] Recommend welcome email customization if the post is the first in a new publication.
