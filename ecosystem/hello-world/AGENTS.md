# Project conventions

Started from `jaablesa/template-vite`. The reasoning behind every tool choice lives in `jaablesa/stack`.

- Package manager: pnpm. Node 22.
- Before pushing, run `pnpm check && pnpm build`. CI runs exactly these two.
- Lint and format with Biome only (`pnpm fix` applies fixes). Do not add ESLint or Prettier.
- Telemetry goes through `src/telemetry.ts`. Never import `@sentry/browser` or `posthog-js` elsewhere: keeping them lazy keeps the first load tiny.
- Product events use `track("noun_verb", {...})`, snake_case, past tense: `city_visited`, `signup_completed`.
- Secrets never go in the repo. Local: `.env.local`. Production: Vercel environment variables, with 1Password as the source of truth.
- Hosting is Vercel. Every PR gets a preview URL; `main` is production.
