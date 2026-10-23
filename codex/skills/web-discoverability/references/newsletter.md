# NEWSLETTER Reference (Substack)

## Parameters

|Parameter|Description|Default|
|---------------|--------------------------------------------------------|----------------------------------|
|`topic`|Subject or draft content to work with|Infer from the conversation|
|`goal`|Primary objective: `format`, `seo`, `growth`, `monetize`|`format` + `seo` if unspecified|
|`language`|Output language|Match the user's message language|

## 1. Clarify Scope

- Identify the goals that apply: formatting, SEO, growth, monetization. Confirm the topic.
- When the request is ambiguous, produce SEO metadata and a formatted structure outline together.

## 2. Visual Formatting

### Text Centering

- The Substack minimalist editor has no standard center-align button for regular body text. To center text: select it, click "Insert Quote", then choose "Pull Quote".
- Use this method to highlight key phrases or statistics. The Pull Quote creates a visual break.

### Content Hierarchy

- Structure content with **Heading 1**, **Heading 2**, and **Heading 3** for a clear, scannable structure that improves readability and search-engine crawling.
- Keep paragraphs to 3–5 sentences max. Check readability in both email and web views.
- Use **Bold**, *Italics*, ~~Strikethrough~~, and hyperlinks to guide the reader's eye and improve scannability. Use bullet points, numbered lists, and dividers to break up long sections.

### Quotes

- Use **Block Quote** to attribute long excerpts from external sources.
- Use **Pull Quote** to emphasize a key phrase or statistic. It renders centered and visually distinct.

### Visuals and Media

- Insert images, GIFs, or charts to break up heavy text.
- Choose the image width by the visual weight needed: **standard**, **wide**, or **full**.
- Always add a **caption** and **alt text** to every image (rules: [3. SEO Metadata](#3-seo-metadata)).

### Interactive Engagement Tools

- Insert native engagement tools at natural breakpoints in the post. **Native buttons**: "Subscribe", "Share your post", "Leave a comment". **Custom buttons**: any URL, to drive a specific reader action (e.g., download, survey, external link).
- **Polls**: passive engagement and retention. Polls are exclusive to paying subscribers.
- Count a poll as the required engagement element only in paying-subscriber content. Otherwise use a button or comment prompt.

## 3. SEO Metadata

Produce these fields for every post.

- **Title**: write 40–60 characters. Use clear modifiers, keywords, and authority signals (e.g., "Tested", "Complete Guide"). Include the primary keyword. Avoid vague or clickbait phrasing.
- **URL Slug**: use 3–5 main keywords only. Ban auto-generated numbers and dates, to keep the post evergreen. Example: `/substack-seo-strategy`.
- **Meta Description**: write 155–160 characters. Include the primary keyword and an implicit call to action.
- **Image Alt Text**: add it to every image. Describe the image for accessibility and incorporate article keywords organically. It serves accessibility and organic SEO simultaneously.

See [SEO Output Example](#seo-output-example).

### SEO Output Example

#### Input

> "Create SEO definitions for an article about how digital nomads can choose the best smartwatches."

#### Output

|Field|Value|Notes|
|------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
|**Title**|The 5 Best Smartwatches for Digital Nomads in 2025|Utility trigger, audience specification, timeliness signal|
|**Meta Description**|Discover the essential smartwatch features for trails and global travel. Read the complete guide for Digital Nomads and choose your gear.|155–160 chars, includes keyword and implicit CTA|
|**URL Slug**|`/smartwatches-digital-nomads`|3–5 keywords, no dates, evergreen-friendly|

#### SEO Rules Applied

- Title is 50 characters (within the 40–60 char target for maximum CTR).
- Slug contains no auto-generated numbers or filler words.
- Meta description closes with an action-oriented phrase without being a hard sell.

#### Auditor Note

- The example Meta Description has 137 characters, not 155–160. Enforce 155–160 in all new output.

## Email Subject Line Rules

- Keep subject lines under 50 characters to prevent truncation on mobile.
- Ban ALL CAPS, excessive exclamation marks, and spam-trigger phrases like "Buy Now" or "Act Now".
- Check spam scores before sending to the full list.

## 4. Growth

- **Substack Notes**: publish short snippets derived from the post to Notes immediately after publishing. Leave authentic comments on related publications to build name recognition.
- **Recommendations rotation**: review Analytics monthly to identify which partner newsletters drive inbound traffic. Rotate recommended partners every 30–60 days to maintain reciprocal growth.

## 5. Monetization (Free to Paid)

- **Tease & Convert**: publish the core article freely. Gate a utility bonus (template, spreadsheet, prompt set, audio) behind the paywall. Prove value before asking for payment. Never cut the paywall mid-sentence.
- **VIP outreach**: in the Dashboard, filter subscribers by engagement score (4–5 stars). Send a targeted direct message with a special rate or an exclusive invite to the paid tier.
- **Welcome email**: customize the automated welcome email. Introduce the author, set publishing cadence expectations, and link to the three best existing articles. Never leave the platform default.
- **Homepage taxonomy**: group posts into Tags (equivalent to newspaper sections). Add the Tags to the navigation bar via *Website Themes* for advanced content discovery.

## Quality Checklist

Check each item before delivering output.

- Title: 40–60 characters, with the primary keyword.
- URL slug: 3–5 words, no numbers, no dates.
- Meta description: 155–160 characters, with a keyword and an implicit CTA.
- Alt text on all images.
- Subject line (if applicable): under 50 characters, no spam triggers.
- At least one native engagement element (button, poll, or comment prompt). Count a poll only for paying-subscriber content.
- Paywall placement follows Tease & Convert (no mid-sentence cut).
- Recommend welcome email customization if the post is the first in a new publication.
