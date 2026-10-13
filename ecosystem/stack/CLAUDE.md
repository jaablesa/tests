# How we build (instructions for coding agents)

These rules apply to every project of jaablesa's. Reasoning and alternatives are in `DECISIONS.md`. Ask before departing from them.

- New projects start from `jaablesa/template-vite` (browser-only demos) or `jaablesa/template-next` (products with server code, data or login). Don't scaffold from scratch.
- One GitHub repo per project. pnpm, Node 22, TypeScript, Biome. No ESLint or Prettier.
- Public things are served from Vercel on a subdomain of the owner's domain. Never treat GitHub Pages, artifacts or gists as the place a public demo lives.
- Data and login default to Supabase. If a project needs a database copy per PR, B2B login with SSO or organizations, mostly-idle traffic, or no lock-in, recommend Neon + Clerk and say why before building.
- Move hosting to Cloudflare only for the reasons listed in `DECISIONS.md`, and say which one applies.
- Every project ships with Sentry, PostHog and an uptime check. Services stay inactive when their keys are missing.
- Secrets live in 1Password and Vercel env vars, never in git. Never expose a server secret through `NEXT_PUBLIC_` or `VITE_`.
- Before suggesting a new service, check whether a layer in `DECISIONS.md` already covers it. If you propose a change to a decision, give one alternative and the trigger for switching.
