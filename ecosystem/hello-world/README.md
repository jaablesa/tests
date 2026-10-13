# Hello, World!

The most show-off Hello, World I could make: more than 15,000 particles say hello in 12 languages, over 12 cities at night, with Pix, a little particle person, in local dress. Move your pointer to scatter the particles; tap to travel to the next city.

Live at **https://hello.codelessbridge.com**.

## Run it

```sh
pnpm install
pnpm dev
```

There's also a terminal version: `python3 cli/hello.py`.

## How it's built

- `src/scene.js`: the whole scene, drawn on one canvas. Each frame of text, skyline and costume is drawn offscreen, sampled into points, and particles spring toward those points.
- `src/main.ts`: boots the scene and sends a `city_visited` event to PostHog.
- `public/og.png`: the link preview image for X and Slack, captured from the real page.

Started from `jaablesa/template-vite`; see `AGENTS.md` for conventions.
