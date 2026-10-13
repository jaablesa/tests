<!-- BEGIN:nextjs-agent-rules -->

## This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` (resolved from this file's directory; in monorepos the `next` package may not be visible from the repo root) before writing any code. Heed deprecation notices.

This block is written and re-added by `next dev` — verify at `node_modules/next/dist/server/lib/generate-agent-files.js`. Removing it from a diff only re-creates the uncommitted change; committing it with your work keeps the tree clean.

<!-- END:nextjs-agent-rules -->

# Project conventions

Started from `jaablesa/template-next`. The reasoning behind every tool choice lives in `jaablesa/stack`.

- Next.js 16 with App Router, React Compiler and Cache Components. Read the guides bundled in `node_modules/next/dist/docs/` before using an API; this version differs from older Next.js (for example, middleware is now `src/proxy.ts`).
- Package manager: pnpm. Node 22. Before pushing, run `pnpm lint && pnpm build` (CI runs the same).
- Lint and format with Biome only (`pnpm fix`). Do not add ESLint or Prettier.
- Styling: Tailwind CSS v4. Fonts: the `geist` package (self-hosted, so builds need no network).
- Data and login: Supabase. Use `@/lib/supabase/server` in Server Components and Actions, `@/lib/supabase/client` in Client Components. Schema changes are SQL migrations in `supabase/migrations/`, never edits in the dashboard. Every table gets row-level security.
- Telemetry: Sentry starts in `src/instrumentation*.ts`; product events go through `track()` in `@/lib/analytics`, snake_case and past tense.
- Secrets never go in the repo. Never put the Supabase secret key in a `NEXT_PUBLIC_` variable.
