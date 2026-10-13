# stack

How I build and ship things. One place for every tool decision, why it was made, the alternative, and when to switch.

- [`DECISIONS.md`](DECISIONS.md): every layer of the stack, with its reasoning and alternative.
- [`docs/new-project.md`](docs/new-project.md): from idea to a live URL with errors, analytics and uptime checks.
- [`docs/domain.md`](docs/domain.md): one-time domain and DNS setup.
- [`docs/accounts.md`](docs/accounts.md): every service account, what it's for, and where its keys live.
- [`CLAUDE.md`](CLAUDE.md): the same rules, written for coding agents.

## The shape of it

```
yourdomain.com (Cloudflare DNS)
├── hello.yourdomain.com    → Vercel ← jaablesa/hello-world   (from template-vite)
├── <demo>.yourdomain.com   → Vercel ← jaablesa/<demo>        (from template-vite)
└── <product>.yourdomain.com → Vercel ← jaablesa/<product>    (from template-next)
                                         ├── Supabase  (data, login, storage)
                                         ├── Sentry    (errors)
                                         ├── PostHog   (analytics)
                                         └── Better Stack (uptime + status page)
```

Each project is its own repo, started from one of two templates. GitHub stores code; it never serves anything public.
