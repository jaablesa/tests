# Decisions

Every layer, the pick, why, the alternative, and the signal that means it's time to switch. Revisit a row only when its "switch when" happens; don't re-litigate the rest.

## Principles

1. **Foundation once, extras per project.** Domain, code, hosting and monitoring are set up once. Data, login, email and storage are added only when a project needs them.
2. **Nothing public is served from GitHub, artifacts or a laptop.** Every public URL is on our own domain, behind Vercel or Cloudflare.
3. **Every project is observable from its first deploy.** Errors, analytics and uptime come with the template.
4. **Services stay inactive without keys.** Templates run locally and in forks with zero accounts.
5. **Prefer portable over clever.** Postgres, standard web APIs, and SQL migrations in git.

## Foundation

| Layer | Pick | Why | Alternative | Switch when |
|---|---|---|---|---|
| Domain and DNS | **Cloudflare** | Registration at cost, the fastest DNS, free DDoS protection and SSL, and the door to Workers and R2 later | Porkbun (registrar) with DNS elsewhere | Cloudflare's registrar doesn't support a TLD you want |
| Code | **One GitHub repo per project** | Clean ownership and history; any project can be open-sourced or handed off alone | One monorepo (pnpm + Turborepo) | You're copying the same code between more than three projects every month |
| Project starters | **Two templates**: `template-vite` (demos), `template-next` (products) | Demos stay tiny and fast; products get server code, data and login | One Next.js template for everything | Maintaining two templates costs more than demos gain from being light |
| Hosting (default) | **Vercel** | Deploys on push, preview URL on every PR, built-in preview images and domains, already connected | Cloudflare Pages/Workers | See "When to move to Cloudflare" below |
| Long-running servers | **Fly.io**, only when needed | Real VMs, WebSockets, background workers, regions near users | Railway | You want point-and-click simplicity over control |
| Errors | **Sentry** | The standard: stack traces with source maps, releases, alerting | Highlight.io | You want errors and session replay in one open-source tool |
| Analytics | **PostHog** (EU cloud) | Product analytics, feature flags, A/B tests and session replay in one generous free tier | Plausible | You only need page views, privacy-first with no cookie banner |
| Uptime and status page | **Better Stack** | Checks every live URL, alerts by phone or email, and gives a public status page | UptimeRobot | Free and basic is enough |
| Secrets | **1Password**, synced into Vercel env vars | One source of truth you already trust; nothing secret in git | Doppler | Secrets need syncing to several platforms automatically |
| Lint and format | **Biome** | One fast tool replaces ESLint and Prettier; same config in every repo | ESLint + Prettier | You need a plugin that only ESLint has |
| Dependency updates | **Renovate** | Weekly batches; dev-tool minors and patches merge themselves when CI passes | Dependabot | You want zero setup and don't mind a noisier PR stream |
| CI | **GitHub Actions** | Runs lint and build on every PR, next to the code | None needed; Vercel's build is the fallback check | n/a |

## Per project

| Need | Pick | Why | Alternative |
|---|---|---|---|
| Demo framework | **Vite + TypeScript** | No framework weight; a demo ships a few KB | Astro, for content-heavy demos and landing pages |
| Product framework | **Next.js** | Best Vercel integration; server code, data and SEO in one place | Astro + islands, for mostly-static sites |
| Styling (products) | **Tailwind CSS** | Fast to write, consistent, and coding agents write it well | CSS Modules, which `template-vite` already uses (plain CSS) |
| Data, login, storage | **Supabase** (default) | Postgres, login, storage and realtime in one place; row-level security; SQL migrations in git | **Neon + Clerk**, see below |
| File storage at scale | Supabase Storage, then **Cloudflare R2** | R2 has no download (egress) fees | Vercel Blob for tiny projects |
| Email | **Resend** | Clean API, React email templates | Postmark, when delivery of important emails like password resets matters most |
| Payments | **Stripe** | The default for a reason | Lemon Squeezy, if you want it to handle sales tax as merchant of record |

## Data: Supabase, or Neon + Clerk

Supabase is the default. Recommend **Neon + Clerk** instead when a project has one of these:

- **A database copy per PR.** Neon creates a branch of the database for every preview deployment in seconds. Supabase branching exists but is heavier and costs more.
- **Polished or B2B login out of the box.** Clerk ships organizations, roles, SSO/SAML, user management screens and bot protection without building them.
- **Login that must outlive the database choice.** With Clerk, users aren't tied to one Postgres provider.
- **Bursty or mostly idle traffic.** Neon scales to zero and wakes per request; Supabase projects run (and on paid plans bill) continuously.
- **Lock-in concerns.** Neon is plain Postgres, while Supabase couples data, login, storage and APIs.

Stay on Supabase when the project wants realtime, file storage and login in one bill, or row-level security driven by the logged-in user.

## When to move a project to Cloudflare

Vercel stays the default. Move a project (or part of it) to Cloudflare Pages/Workers when:

- Bandwidth or function invocations make the Vercel bill grow faster than the product.
- You need Durable Objects, Queues, or compute in every region by default.
- The project is mostly static assets with heavy traffic (Cloudflare has no bandwidth fees).
- The project needs R2 or Cloudflare's other tools to be fast and sit close together.
