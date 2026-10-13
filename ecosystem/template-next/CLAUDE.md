@AGENTS.md

# Project conventions

Started from `jaablesa/template-next`. The reasoning behind every tool choice lives in `jaablesa/stack`.

- Next.js 16 with App Router, React Compiler and Cache Components. Read the guides bundled in `node_modules/next/dist/docs/` before using an API; this version differs from older Next.js (for example, middleware is now `src/proxy.ts`).
- Package manager: pnpm. Node 22. Before pushing, run `pnpm lint && pnpm build` (CI runs the same).
- Lint and format with Biome only (`pnpm fix`). Do not add ESLint or Prettier.
- Styling: Tailwind CSS v4. Fonts: the `geist` package (self-hosted, so builds need no network).
- Data and login: Supabase. Use `@/lib/supabase/server` in Server Components and Actions, `@/lib/supabase/client` in Client Components. Schema changes are SQL migrations in `supabase/migrations/`, never edits in the dashboard. Every table gets row-level security.
- Telemetry: Sentry starts in `src/instrumentation*.ts`; product events go through `track()` in `@/lib/analytics`, snake_case and past tense.
- Secrets never go in the repo. Never put the Supabase secret key in a `NEXT_PUBLIC_` variable.
