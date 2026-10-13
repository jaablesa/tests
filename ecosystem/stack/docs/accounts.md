# Accounts

Every service, what it's for, and where its credentials live. All credentials are stored in the 1Password vault **Dev**.

| Service | Used for | Plan to start | Credentials in 1Password |
|---|---|---|---|
| Cloudflare | Domain, DNS | Free | Login + 2FA |
| GitHub | Code, CI | Free | Login + 2FA |
| Vercel | Hosting | Hobby, then Pro for commercial projects | Login; per-project env vars sourced from the items below |
| Sentry | Errors | Developer (free) | One item per project: DSN, org, project; one org auth token |
| PostHog | Analytics | Free (EU cloud) | One item per project: project API key |
| Better Stack | Uptime, status page | Free | Login |
| Supabase | Data, login, storage | Free (2 projects), then Pro | One item per project: URL, publishable key, secret key, database password |
| Renovate | Dependency PRs | Free GitHub App | None |

Vercel's Hobby plan is for non-commercial use. Move to Pro before anything earns money.
