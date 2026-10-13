# New project runbook

From idea to a live URL with errors, analytics and uptime checks in about 15 minutes.

## 1. Pick the template

- **Demo, toy, landing page, anything that runs only in the browser** → `jaablesa/template-vite`
- **Accounts, database, server logic, payments** → `jaablesa/template-next` (Supabase by default; see `DECISIONS.md` for when to choose Neon + Clerk)

## 2. Create the repo

On GitHub, open the template and choose **Use this template → Create a new repository**, private, named after the project.

```sh
git clone git@github.com:jaablesa/<name>.git && cd <name>
pnpm install
cp .env.example .env.local
pnpm dev
```

Update the name, title, description and Open Graph tags (`index.html` or `src/app/layout.tsx`).

## 3. Services (skip any the project doesn't need yet)

| Service | Create | Copy into 1Password, then Vercel |
|---|---|---|
| Sentry | New project (Browser JavaScript or Next.js) | DSN → `VITE_SENTRY_DSN` / `NEXT_PUBLIC_SENTRY_DSN`; `SENTRY_ORG`, `SENTRY_PROJECT`; org auth token → `SENTRY_AUTH_TOKEN` |
| PostHog | New project in the EU cloud | Project API key → `VITE_POSTHOG_KEY` / `NEXT_PUBLIC_POSTHOG_KEY` |
| Supabase (Next only) | New project, same region as Vercel | URL + publishable key → `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY` |

## 4. Deploy on Vercel

1. **Add New → Project**, import the repo. The framework is detected automatically.
2. Paste the environment variables for **Production** and **Preview**.
3. **Settings → Domains → Add** `<name>.yourdomain.com`. Vercel shows a CNAME target.
4. In Cloudflare DNS, add that CNAME record with the proxy **off** (grey cloud), so Vercel can issue the certificate.

From now on, `main` is production and every PR gets its own preview URL.

## 5. Watch it

- Better Stack: add a monitor for `https://<name>.yourdomain.com` and add it to the status page.
- Renovate: install the Renovate GitHub App on the new repo (or give it access to all repos once).
- Share the link and check the preview card with the X and LinkedIn card validators.

## Done means

- [ ] Live on its own subdomain over HTTPS
- [ ] CI green on `main`
- [ ] A test error shows up in Sentry with a readable stack trace
- [ ] A pageview shows up in PostHog
- [ ] An uptime monitor is on
