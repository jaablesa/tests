# template-vite

Starter for demos, toys and interactive pages. For products with accounts or a database, use `template-next`.

## What's included

| | |
|---|---|
| Build | Vite + TypeScript (strict) |
| Quality | Biome for lint and format, GitHub Actions CI on every PR |
| Errors | Sentry, with source maps uploaded at build time and never served publicly |
| Analytics | PostHog, `track()` helper |
| Hosting | Vercel config with security and cache headers |
| Dependencies | Renovate: weekly, dev-tool minors and patches merge themselves |
| Link previews | Open Graph and X card tags in `index.html` |

Sentry and PostHog only download when their keys are set, so a demo without keys ships about 1.5 KB of JavaScript.

## Start a new project

Follow the runbook in `jaablesa/stack` (`docs/new-project.md`). The short version:

1. On GitHub, **Use this template** → new private repo.
2. `pnpm install && pnpm dev`
3. Import the repo in Vercel, add the environment variables from `.env.example`, and add the subdomain.
