# template-next

Starter for products: anything with accounts, a database, or server logic. For demos and toys, use `template-vite`.

## What's included

| | |
|---|---|
| Framework | Next.js 16 (App Router, React Compiler, Cache Components), TypeScript, Tailwind CSS v4 |
| Data and login | Supabase: browser and server clients, plus session refresh in `src/proxy.ts`. All of it stays inactive until keys are set. |
| Quality | Biome, GitHub Actions CI on every PR |
| Errors | Sentry on client, server and edge, with source-map upload and an ad-blocker-safe `/monitoring` tunnel |
| Analytics | PostHog, `track()` helper |
| Hosting | Vercel (no config needed), security headers in `next.config.ts` |
| Dependencies | Renovate: weekly, dev-tool minors and patches merge themselves |

## Start a new project

Follow `docs/new-project.md` in `jaablesa/stack`. The short version:

1. On GitHub, **Use this template** → new private repo.
2. `pnpm install && cp .env.example .env.local && pnpm dev`
3. Create a Supabase project, then `pnpm dlx supabase link` and `pnpm dlx supabase db push` for migrations.
4. Import the repo in Vercel, add the environment variables, and add the subdomain.

## When Supabase is the wrong fit

See "Data: Supabase, or Neon + Clerk" in `jaablesa/stack/DECISIONS.md`. The Supabase code is limited to `src/lib/supabase/` and `src/proxy.ts`, so it's easy to swap.
