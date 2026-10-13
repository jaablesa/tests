# stack

How I build and ship things. One place for every tool decision, why it was made, the alternative, and when to switch.

- [`environment.html`](environment.html): the visual guide to all of this, with remaining setup steps. Reviewed weekly.
- [`DECISIONS.md`](DECISIONS.md): every layer of the stack, with its reasoning and alternative.
- [`docs/new-project.md`](docs/new-project.md): from idea to a live URL with errors, analytics and uptime checks.
- [`docs/agent-access.md`](docs/agent-access.md): how agents get access to every service, and the short list of things only a human does.
- [`bin/doctor`](bin/doctor): checks which services an agent can reach from the current environment.
- [`docs/domain.md`](docs/domain.md): one-time domain and DNS setup.
- [`docs/accounts.md`](docs/accounts.md): every service account, what it's for, and where its keys live.
- [`AGENTS.md`](AGENTS.md): the same rules, written for any coding agent (Claude Code, Codex, Cursor, Copilot…).

## The shape of it

```
codelessbridge.com (Cloudflare DNS)
├── hello.codelessbridge.com     → Vercel ← jaablesa/hello-world   (from template-vite)
├── <demo>.codelessbridge.com    → Vercel ← jaablesa/<demo>        (from template-vite)
└── <product>.codelessbridge.com → Vercel ← jaablesa/<product>     (from template-next)
                                         ├── Supabase  (data, login, storage)
                                         ├── Sentry    (errors)
                                         ├── PostHog   (analytics)
                                         └── Better Stack (uptime + status page)
```

Each project is its own repo, started from one of two templates. GitHub stores code; it never serves anything public.
