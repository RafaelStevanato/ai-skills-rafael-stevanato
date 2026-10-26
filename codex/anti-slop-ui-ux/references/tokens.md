# Tokens and base-library overrides

Change every value below before the first screen.

## Values

- Set `--radius` on purpose (`0.25rem` technical, `0.375rem` balanced, `0.5rem` soft). Never ship the shadcn default `0.625rem`.
- Tint neutrals toward the brand hue `H` with chroma `0.003` to `0.012`. Never ship the achromatic `oklch(L 0 0)` set.
- Light: background near `oklch(0.985 0.004 H)`, foreground near `oklch(0.2 0.01 H)`. Dark: background near `oklch(0.16 0.006 H)`, foreground near `oklch(0.95 0.005 H)`.
- Rebalance dark mode surface by surface. Never invert the light theme. Lower border opacity in dark mode: borders read heavier there.
- Set `--primary` to the brand color in OKLCH. Keep the default near-black `oklch(0.205 0 0)` only on a monochrome brief.
- Derive `--ring` from `--primary`.
- Choose the typeface on purpose. Write the reason in a comment beside the font token. Never inherit the init font silently.
- Map tokens in `@theme inline` (Tailwind v4) or `theme.extend` (v3), so components can use `bg-background`, `text-muted-foreground`, `border-border` and `bg-primary`.

## Component sources

- Edit the copied sources in `components/ui/*`: remove the Card shadow (classic style) or `ring-1 ring-foreground/10` (nova style), match Card padding to PRE-FLIGHT `density`, put control heights on one scale (`h-8` compact, `h-9` default, `h-10` comfortable).

## Gotchas

- Tinted neutrals often push `muted-foreground` below 4.5:1. Measure after tinting.
- `npx shadcn add <component> --overwrite` resets customized `components/ui/*` files. Diff after every add and re-apply the overrides.
- shadcn defaults change between releases (Base UI and the nova style became default in 2026). Read `components.json` and the current `globals.css` before you override. Check https://ui.shadcn.com/docs/theming when unsure.

## Done

- Done when every value above is set or tagged `// BRIEF:`, and text contrast passes after tinting.
