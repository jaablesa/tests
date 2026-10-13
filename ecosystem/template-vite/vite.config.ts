import { sentryVitePlugin } from "@sentry/vite-plugin";
import { defineConfig } from "vite";

// Source maps are built, uploaded to Sentry, then deleted so they never ship publicly.
// The upload only runs when SENTRY_AUTH_TOKEN is set (in Vercel), so local builds stay offline.
const sentry = process.env.SENTRY_AUTH_TOKEN
  ? sentryVitePlugin({
      org: process.env.SENTRY_ORG,
      project: process.env.SENTRY_PROJECT,
      authToken: process.env.SENTRY_AUTH_TOKEN,
      sourcemaps: { filesToDeleteAfterUpload: ["dist/**/*.map"] },
    })
  : [];

export default defineConfig({
  build: { sourcemap: true },
  plugins: [sentry],
});
