# Agent access

Goal: agents operate every service through its API or CLI. The owner never clicks through a dashboard to complete a task.

## Why a one-time bootstrap is unavoidable

No service lets software grant itself access to an account. The owner creates each account once and mints one scoped token per service. After that, agents do everything else: create repos and projects, add domains and DNS records, create Sentry and PostHog projects, add uptime monitors, run database migrations.

Run `bin/doctor` to see what the current environment can reach. On 2026-10-13 the Claude Code cloud environment could reach only GitHub, and only for repos attached to the session.

## Human-only actions (the complete list)

1. Create an account (accepting terms, identity, 2FA).
2. Payments and plan changes.
3. Minting, rotating and revoking tokens.
4. Changing a domain's nameservers at Namecheap, once. Namecheap's API only accepts requests from whitelisted fixed IPs, which cloud agents don't have. After the move, DNS lives in Cloudflare, whose API agents can use.

Anything else that an agent says needs a dashboard is a gap to fix: find the API, CLI or Terraform provider for it.

## Bootstrap (one time, about 20 minutes)

For each service, create the token, save it in 1Password (vault **Dev**), then add it to the Claude Code environment: environment menu in the session title bar → **Edit** → **Network secrets** (or environment variables) with the variable name below, and add the hosts under **Network access → Allowed domains**. New sessions pick both up.

| Service | Create the token at | Permissions | Variable | Allowed domains |
|---|---|---|---|---|
| GitHub | github.com → Settings → Developer settings → Fine-grained tokens | Resource owner `jaablesa`, All repositories. Administration, Contents, Pull requests, Workflows, Secrets, Actions: Read and write | `GH_ADMIN_TOKEN` | (already allowed) |
| Vercel | vercel.com → Account Settings → Tokens | Scope: team "Jose's projects" | `VERCEL_TOKEN` | `api.vercel.com`, `vercel.com` |
| Cloudflare | dash.cloudflare.com → My Profile → API Tokens → Create custom token | Account: Zone Edit (to add the domain). Zone (all zones): DNS Edit, Zone Read, Zone Settings Edit | `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID` | `api.cloudflare.com` |
| Sentry | Settings → Developer Settings → Custom Integrations → New internal integration | Project: Admin, Organization: Read, Release: Admin | `SENTRY_AUTH_TOKEN`, `SENTRY_ORG` | `sentry.io`, `*.sentry.io` |
| PostHog | Settings → Personal API keys | Organization and Project: Write | `POSTHOG_PERSONAL_API_KEY` | `eu.posthog.com`, `eu.i.posthog.com` |
| Better Stack | Uptime → Settings → API tokens | Team token | `BETTERSTACK_API_TOKEN` | `uptime.betterstack.com` |
| Supabase | supabase.com/dashboard/account/tokens | Personal access token | `SUPABASE_ACCESS_TOKEN` | `api.supabase.com`, `*.supabase.co` |
| npm registry, Terraform | none | none | none | `registry.terraform.io`, `releases.hashicorp.com`, `github.com` (provider downloads) |

Give each token an expiry (90 days) and let the weekly review warn before they expire.

## What agents do after the bootstrap

| Task | How |
|---|---|
| Create a repo from a template | `GH_TOKEN=$GH_ADMIN_TOKEN gh repo create jaablesa/<name> --private --template jaablesa/template-vite` |
| Deploy a project and add its subdomain | Vercel API / CLI with `VERCEL_TOKEN` |
| DNS records | Cloudflare API with `CLOUDFLARE_API_TOKEN` |
| Error tracking and analytics for a new project | Sentry and PostHog APIs |
| Uptime monitor | Better Stack API |
| Database and migrations | `supabase` CLI with `SUPABASE_ACCESS_TOKEN` |
| Set a project's environment variables | Vercel API, values read from the environment, never pasted in chat |

Never paste a token into a chat, a commit, a log or an issue.
