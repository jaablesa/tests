# Domain setup (one time)

Goal: `codelessbridge.com` uses Cloudflare DNS, and each project is a subdomain pointing at Vercel.

## Before you touch DNS

`codelessbridge.com` is already the website on your GitHub profile, so something may be live on it, and email may run through it too.

1. Write down what serves `codelessbridge.com` and `www` today (the hosting platform) and whether you receive email at the domain.
2. Log in to the current registrar and export or screenshot every DNS record.
3. Only then switch nameservers. Cloudflare imports records automatically, but compare them against your list, especially MX, SPF/DKIM TXT and any verification records.

## Move DNS to Cloudflare

1. In Cloudflare: **Add a domain** → enter `codelessbridge.com` → Free plan. Cloudflare imports the existing DNS records; check that MX (email) and TXT records came across.
2. Cloudflare shows two nameservers. At your current registrar, replace the nameservers with those two.
3. Wait for Cloudflare to show **Active** (minutes to a few hours). Nothing goes down during the switch if the imported records are complete.
4. Optional, later: transfer the registration itself to Cloudflare Registrar for at-cost renewals.

## Settings to turn on

- **SSL/TLS → Overview**: Full (strict).
- **SSL/TLS → Edge Certificates**: Always Use HTTPS on.
- **DNS**: records pointing at Vercel stay **DNS only** (grey cloud). Vercel already has a CDN and needs to issue its own certificates.

## Apex domain

Point `codelessbridge.com` and `www` at whatever you want as your home page (a portfolio project on Vercel, for example). Add both in that Vercel project's Domains settings and copy the records it asks for.
