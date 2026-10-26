---
name: anti-slop-ui-ux
description: 'Load on every frontend UI or UX coding task, together with anti-slop: building, editing, refactoring or reviewing pages, screens, components, tables, forms, dashboards, settings, navigation, tabs, Tailwind classes, CSS, shadcn/ui, design tokens or design system setup, including Portuguese requests (tela, componente, página, refatoração visual, interface com cara de IA). Supplies product-UI engineering rules: flat hierarchy instead of cards, one primary action per viewport, quiet table rows, token-only color, customized shadcn/Radix/Tailwind defaults, the 18 Laws of UX as component constraints, restrained motion, and a PRE-FLIGHT plus SELF-CHECK gate. anti-slop keeps brand signature, landing-page art direction and Slop Index scoring.'
metadata:
  version: "1.1.0"
  date: "2026-10-24"
  category: "design"
  sources: "lawsofux.com; w3.org/WAI/WCAG22/Understanding/target-size-minimum.html; github.com/emilkowalski/skills; ui.shadcn.com/docs/theming; tailwindcss.com/docs/colors; linear.app/now/behind-the-latest-design-refresh; refactoringui.com"
---

> **⚠️ EXECUTION DIRECTIVE (INPUT vs. OUTPUT SEPARATION):**
> The rules in this skill use strict ASD-STE100 controlled language solely for zero-ambiguity parsing and token efficiency.
> - **NEVER copy this telegraphic or robotic style into human-facing outputs.**
> - Apply 80% ASD-STE100 in final outputs ONLY when explaining dense technical concepts.

# Anti-Slop UI/UX

## Scope

- Apply to every file that renders UI: `.tsx`, `.jsx`, `.vue`, `.svelte`, `.astro`, `.html`, `.css`, Tailwind config, `components/ui/*`.
- Obey explicit user or brief direction over every rule here. Tag the line `// BRIEF: <direction>`.
- Read the existing tokens and components first (`globals.css`, `tailwind.config.*`, `components/ui/`). Extend them. Never fork a parallel set.
- Defer brand signature, landing-page art direction and Slop Index scoring to `anti-slop`. Run both skills on landing pages.
- Defer prose rewriting to `anti-ai-slop-escrita-ptbr`.

## Leading words

Use these terms in reasoning and reports.

- **flat-first**: build hierarchy with space, weight and color before any box, border or shadow.
- **box test**: delete a card, border, ring or divider. If the grouping still reads, keep it deleted.
- **one primary**: exactly one accent-filled element per viewport.
- **token-only**: components consume semantic tokens. Raw palette classes (`bg-zinc-100`, `text-gray-500`) and hex values live only in the token file.
- **quiet rows**: rows show data. Row actions live in one menu.
- **mock-first**: typed fixtures cover every state before any schema, endpoint or fetch.
- **instant on repeat**: never animate an action the user repeats many times per session.

## Workflow

### 1. PRE-FLIGHT

Write this one line before the first line of UI code:

```
PRE-FLIGHT: goal=<the one task this screen serves> | primary=<the one primary action> | top20=<2-3 actions that get prime space> | density=<compact|default|comfortable> | structure=<flat | N cards: reason each> | nav=<sidebar | underline tabs | segmented | none>
```

- Fill every field before you code.
- Allow a card for one of three reasons only: a floating surface (dialog, popover, menu, toast), a draggable or selectable object, a peer-grid item that is itself the click target.
- Done when the line exists, `primary` names one element, and each card carries one allowed reason.

### 2. Mock-first data (new screens)

- Put typed fixtures in one file next to the feature (`<feature>.mock.ts`). Shape them like the planned API response.
- Use realistic domain values: plausible names, prices, dates, IDs. Never `Lorem ipsum`, `John Doe`, `Item 1`, `$99`.
- Add edge rows: a 60-character name, a zero, a 7-digit number, a missing optional field, an error.
- Render every state from fixtures: loading, empty, error, partial, success, overflow.
- Write no schema, migration, endpoint or real fetch until the user approves the UI.
- Done when each state renders from fixtures with zero network calls.

### 3. Build

- Derive components from the domain and the task, never from a template. Name them by domain noun or task (`InvoiceRow`, `UsageMeter`, `InviteMemberForm`), never by shape (`FeatureCard`, `StatCard`, `InfoBox`).
- Apply every rule in sections A to J.

### 4. SELF-CHECK

- Run the Self-Check section before you end any turn that created or edited a frontend file.
- Done when both scans show zero untagged hits and every checklist line is true.

### Refactor or review branch

- Run the Self-Check scans on the existing files first. Record the hits.
- Write PRE-FLIGHT for the screen as it must become.
- Fix in this order: structure (cards, borders), actions and density, color, tokens, copy, motion.
- Skip step 2 when real data already flows.
- Done when the Self-Check passes on every touched file.

## A. Hierarchy and layout (flat-first)

- Place page content directly on the page background. Never wrap a page section, a single form or a settings group in a card.
- Never nest a card in a card, a bordered box in a bordered box, or a shadow in a shadow.
- Replace a KPI card row with a flat stats strip: muted label above, large value below, `gap-x-12` between items, no box, no icon tile.
- Separate groups with space first, background shift second (`bg-muted/40`), hairline border last.
- Use the 4 px spacing scale only (Tailwind default steps). Never use arbitrary values such as `p-[13px]`.
- Proximity: make the space between groups at least 2× the space inside a group, and the space between sections at least 2× the space between groups (`gap-2`, then `gap-6`, then `gap-12`). [Proximity]
- Build emphasis with weight and color, not size alone. Use at most 3 text colors (`text-foreground`, `text-muted-foreground`, one tertiary) and 2 weights. [Refactoring UI]
- Keep app headings modest: page `<h1>` at `text-xl` to `text-2xl font-semibold tracking-tight`, section `<h2>` at `text-sm` to `text-base font-medium`.
- De-emphasize competitors before you emphasize the focus. Mute secondary text and icons first.
- Drop labels the value already explains (`ana@kovir.com` needs no "Email:"). In key-value pairs, mute the label and emphasize the value. [Refactoring UI]
- Never put gray text on a colored background. Use a lighter or darker step of that background's hue.
- Right-align numbers in table columns. Never center text longer than 2 lines.
- Align mixed font sizes on one line with `items-baseline`, not `items-center`.
- Size inline icons to the line height (`size-4` with `text-sm`, `size-5` with `text-base`). Align them optically: nudge with `translate-y-px` when the glyph reads off-center.
- Limit reading text to `max-w-prose` (65ch). Never exceed 75ch. Never constrain tables or app shells with it.
- Occam: between two layouts that solve the task, ship the one with fewer DOM nodes, borders, surface colors and radii. Delete every wrapper `div` with no layout job. [Occam's Razor]
- Prägnanz: use one radius scale, one border style and one shadow style per product. Never mix radii in one component. [Prägnanz]

## B. Borders and dividers (box test)

- Remove the border under page and section headings.
- Remove borders between sidebar sections. Use `gap-6` and a muted group label.
- Remove the border and card around charts. Put the chart on the page background, its title above.
- Remove vertical cell borders in tables. Use one row-separator system: hairline `divide-y divide-border/60` or a hover background, never both.
- Keep visible boundaries on inputs, selects and checkboxes at 3:1 contrast against the background (WCAG 1.4.11).
- Keep at most one structural divider between app chrome regions (sidebar | main). Prefer a background shift.
- Never darken a border to fix weak hierarchy. Fix spacing and weight instead.

## C. Actions and data density (quiet rows)

- Show at most 1 visible action per row. Put the rest in one `⋯` dropdown menu per row, mirrored in a right-click context menu where the stack has one.
- Never place loose icon buttons per row (eye + copy + edit + trash). Make the value the control: click the ID badge to copy it, reveal a masked secret from the row menu.
- Reveal hover actions on `focus-within` too, and keep the `⋯` trigger always visible on coarse pointers. Hover-only actions are invisible to touch and keyboard users.
- Cap tables at 3 to 4 columns that `goal` needs. Move the rest to the row detail view (sheet, drawer or page).
- Expose only the fields that `goal` needs. Remove metric columns and stat tiles that change no decision on this page.
- Hick: show at most 3 actions in a toolbar. Move the rest to an overflow menu. Put advanced options behind one disclosure. [Hick]
- Serial position: put the most-used item first and the next most important last in menus, lists and nav. Put destructive items last, after a separator, in `text-destructive`. [Serial Position]
- Pareto: give the `top20` actions the prime area (content start, primary button, keyboard shortcut) and full state polish. Put the other 80% in menus and settings. [Pareto]
- Miller: chunk long values: phone `(11) 98765-4321`, CEP `01310-100`, card `4242 4242 4242 4242`, CPF `123.456.789-09`, keys `sk_live_••••4f2a`. Group menu and nav items in blocks of 5 to 7 under a muted label. [Miller]

## D. Color and focus (one primary)

- Apply one primary: the only `variant="default"` (filled) button in the viewport. Use `outline` or `secondary` for secondary actions, `ghost` or `link` for tertiary. [Hick, Von Restorff]
- Use one accent hue. Spend it on the primary button, focus ring, selected state and links only.
- Map every non-neutral color on screen to one meaning: accent = primary or selected, destructive = error or irreversible, warning = needs attention, success = done. Make every other color neutral.
- Render badges neutral by default (`bg-muted text-muted-foreground`). Color a badge only when it encodes a state the user acts on.
- Never color-code tabs, cards, categories or icon tiles in rainbow hues.
- Use soft status styles: tinted text on a 10 to 15% tint background. Reserve solid fills for the one primary and for destructive confirm buttons.
- Check the screen in grayscale first. Hierarchy must read with color removed. Add the accent after.

## E. Navigation and tabs

- Jakob: follow known conventions. Global nav in a left sidebar (apps) or top bar (sites). Logo top-left links home. Workspace or project switcher at the top of the sidebar. Account and settings in the user menu. Search and commands on `Ctrl+K`/`⌘K`. Breadcrumbs past 2 levels of depth. [Jakob]
- Never use inset or pill tabs (shadcn `TabsList` default: `bg-muted p-[3px]`) for page or route navigation.
- Use underline tabs for sub-pages of one entity: shadcn `<TabsList variant="line">`, or a `<nav>` of links with an active underline.
- Build route navigation from links (`<a>`/`<Link>` with `aria-current="page"`), not `role="tablist"`. Give each tab a URL. Tabs components break the back button, deep links and middle-click.
- Restrict inset or segmented tabs to local view state inside one component: Preview/Code, Monthly/Yearly, List/Grid.

## F. Copy

- Delete subtitles that restate the heading ("Settings" + "Manage your settings", "Equipe" + "Gerencie os membros da sua equipe"). Keep a subtitle only when it adds a fact the heading lacks: a scope, a consequence, a real count.
- Never add a description line under every section or card.
- Write CTAs as verb + object ("Create invoice", "Invite member", "Exportar CSV"). Never "Get started", "Learn more", "Submit", "Click here", "Saiba mais", "Começar", "Enviar".
- Match each button label to the title of the screen it opens.
- Never invent metrics or social proof ("10x faster", "99.9% uptime", "Trusted by 10,000+ teams"). Use real data or omit it.
- Write error messages as cause + fix ("Card declined. Use another card or contact your bank.").
- Use sentence case on labels, buttons and headings. Never Title Case Every Word. Never UPPERCASE labels.
- Write empty states as one line + one action.

## G. Tokens (token-only)

- Read [references/tokens.md](references/tokens.md) before you set up or change tokens, `globals.css`, `tailwind.config.*` or `components/ui/*`, and whenever the project still ships shadcn/ui `init` defaults (`--radius: 0.625rem`, achromatic `oklch(L 0 0)` neutrals).

## H. Banned AI tells

- Ban Tailwind `indigo-*`, `violet-*` and `purple-*` as accent unless the brand hue is one of them (`// BRIEF:`).
- Ban two-stop gradients on buttons, text and heroes: `bg-gradient-to-*` (v3), `bg-linear-to-*` (v4), `bg-clip-text text-transparent`.
- Ban `#000`, `#fff`, `oklch(0 0 0)` and `oklch(1 0 0)` as surface or text colors.
- Ban decorative bento grids: mixed-span grids whose cells carry no distinct function.
- Ban colored left-border accent cards (`border-l-4 border-<color>`).
- Ban blob SVGs and blurred background orbs (`blur-3xl` circles).
- Ban glassmorphism (`backdrop-blur`) unless the surface floats over moving or complex content.
- Ban uppercase pills and eyebrows above section titles (`text-xs uppercase tracking-wider` kickers).
- Ban emojis as UI icons (🚀 ✨ ⚡ 🎯 🔥 💡). Use one icon library at one stroke width.
- Put `tabular-nums` on every number that changes or aligns: prices, metrics, table cells, timers, counters, dates in columns.

## I. Motion (instant on repeat)

- Ban `transition-all` and `transition: all`. Name the properties: `transition-[opacity,transform]`, `transition-colors`.
- Keep UI motion between 120 and 250 ms: press 120 to 160 ms, tooltip or small popover 125 to 200 ms, dropdown, modal and drawer 150 to 250 ms.
- Ease enter and exit with ease-out, `cubic-bezier(0.23, 1, 0.32, 1)`. Ease on-screen movement with ease-in-out, `cubic-bezier(0.77, 0, 0.175, 1)`. Never use ease-in.
- Animate `transform` and `opacity` only. Never animate `width`, `height`, `top`, `left` or `margin`.
- Render instantly, with no animation: keyboard navigation, command palette open and close, list filtering, search results, tab switches.
- Scale popovers and menus from their trigger: `transform-origin: var(--radix-dropdown-menu-content-transform-origin)` (Radix) or `var(--transform-origin)` (Base UI). Keep modals centered.
- Start scale-in at `0.95` to `0.97` with opacity 0. Never start at `scale-0`.
- Give buttons press feedback: `active:scale-[0.97]`.
- Honor `prefers-reduced-motion`: drop movement, keep opacity and color changes (`motion-reduce:transform-none`).
- Ban decorative loops (`animate-bounce`, `animate-ping` outside live status), hover `scale-105` on cards, and scroll-triggered fade-ups. Show content on first paint.

## J. Feedback, input and flow

- Fitts: make touch targets at least 44×44 px (`min-h-11 min-w-11` on coarse pointers) and pointer targets at least 24×24 px (WCAG 2.5.8). Grow the hit area with padding or `before:absolute before:-inset-2`, not the visual size. [Fitts]
- Fitts: put the primary action at the end of the reading path: last in a form, rightmost in a dialog footer, in a sticky bottom bar on mobile. [Fitts]
- Doherty: answer every input within 400 ms. Apply mutations optimistically, reconcile with the server, roll back and show a retry toast on failure. [Doherty]
- Doherty: show a skeleton with the final layout's dimensions for loads over 300 ms. Never block the whole screen with a spinner. Keep stale data visible during refetch.
- Doherty: show the pending state on the clicked button within 100 ms. Block double submits.
- Postel: accept loose input. Strip spaces, dashes, dots, parentheses and currency symbols on parse. Accept paste. Trim. Compare emails case-insensitively. [Postel]
- Postel: store the canonical value, show the formatted value. Format on blur. Never block typing, paste, autofill or the caret with a hard mask.
- Postel: set `type`, `inputMode` and `autoComplete` on every field (`inputMode="numeric"` for CEP and CPF, `autoComplete="email"`).
- Tesler: absorb complexity in code. Fill the address from the CEP, infer currency and date format from locale, generate slugs from titles, preselect the most common option, remember the last choice. Never ask for data the system can derive. [Tesler]
- Parkinson: compress flows. Prefer inline edit over an edit page. Prefer a one-click action with an undo toast over a confirm dialog. [Parkinson]
- Parkinson: use a confirm dialog only for irreversible destructive actions. Use type-to-confirm only for high-stakes deletes.
- Parkinson: use a multi-step wizard only when later steps depend on earlier answers. Otherwise use one page.
- Zeigarnik: show progress on multi-step work ("Step 2 of 4" plus a bar). Persist drafts. Keep a setup checklist visible until complete, then remove it. [Zeigarnik]
- Peak-End: polish the core value moment and the final state. Name the result and offer the next action ("Invoice #1042 sent to Ana · View invoice"). Never a bare "Success!". [Peak-End]
- Uniform connectedness: join the steps of one flow with a visible track in steppers. Attach controls that act as one unit (input + button with `rounded-r-none`, segmented controls). Group them with a shared background, not a card. [Uniform Connectedness]
- Similarity: same look, same behavior. Give static badges no hover, no `cursor-pointer`, no shadow. Render clickable badges as `<button>` with hover and focus states. Keep one icon per action across all screens. [Similarity]
- Keep a `focus-visible` ring on every interactive element (`focus-visible:ring-2 focus-visible:ring-ring`). Never remove an outline without a replacement.
- Measure text contrast after any color change: 4.5:1 for body text, 3:1 for large text (WCAG 2.2 AA).

## Gotchas

- Deleting cards without adding space leaves content floating. After each box-test deletion, apply the Proximity rule and add a heading if the group lost its name.
- `tabular-nums` does nothing when the font lacks the `tnum` feature. Check the font.
- The scans flag legitimate brand choices. Tag them `// BRIEF:` instead of contorting the code.

## Self-Check

Run before you end any turn that created or edited a frontend file. Validate silently. Fix every hit, then run again.

1. Run the tells scan with the Grep tool on every changed frontend file, CSS included:

```
transition-all|transition:\s*all|bg-gradient-to-|bg-linear-to-|bg-clip-text|(indigo|violet|purple)-\d{2,3}|#(000000|ffffff|FFFFFF|000|fff|FFF)\b|oklch\((0|1) 0 0\)|--radius:\s*0\.625rem|border-l-[48]\b|backdrop-blur|animate-bounce|hover:scale-1\d\d|\p{Emoji_Presentation}|\x{FE0F}|Lorem ipsum|Manage your|Gerencie (seus|suas|os|as)|Get started|Learn more|Saiba mais
```

2. Run the token-only scan on component files only, never on the token file:

```
\b(bg|text|border|ring|fill|stroke|from|via|to|divide|outline)-(slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose|white|black)\b
```

3. Keep a hit only with a `// BRIEF:` or `// WHY:` comment on the same line. Fix all other hits.
4. Confirm every line below. Print only `SELF-CHECK: pass` or the failed lines.

- [ ] PRE-FLIGHT written; every card carries an allowed reason.
- [ ] Mock-first: every state renders from fixtures; no backend code before approval.
- [ ] Flat-first: no nested boxes; Proximity spacing steps hold; at most 3 text colors and 2 weights.
- [ ] Box test: no border under headings, between sidebar sections or around charts; input boundaries at 3:1.
- [ ] Quiet rows: at most 1 visible row action, 4 table columns, 3 toolbar actions.
- [ ] One primary: one filled button per viewport; every non-neutral color maps to a meaning.
- [ ] Route navigation uses links with URLs; inset tabs hold local state only.
- [ ] No restating subtitles; every CTA is verb + object; no invented metrics.
- [ ] Token-only: radius, neutrals, primary, ring and font customized; contrast measured.
- [ ] `tabular-nums` on every changing or aligned number.
- [ ] Instant on repeat: named properties, 120 to 250 ms, ease-out, reduced motion honored.
- [ ] Targets at least 24 px pointer and 44 px touch; focus rings visible; optimistic mutations roll back; inputs accept loose formats.
