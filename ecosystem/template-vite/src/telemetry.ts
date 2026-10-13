// Sentry and PostHog load in their own chunks, after first paint, and only when their keys are set.
// With no keys (local dev, forks) nothing is downloaded and nothing is sent anywhere.
type PostHog = typeof import("posthog-js").default;
let posthog: PostHog | undefined;

export async function startTelemetry(): Promise<void> {
  const { VITE_SENTRY_DSN, VITE_POSTHOG_KEY, VITE_POSTHOG_HOST, MODE } = import.meta.env;

  if (VITE_SENTRY_DSN) {
    const Sentry = await import("@sentry/browser");
    Sentry.init({
      dsn: VITE_SENTRY_DSN,
      environment: MODE,
      integrations: [Sentry.browserTracingIntegration()],
      tracesSampleRate: 0.1,
    });
  }

  if (VITE_POSTHOG_KEY) {
    posthog = (await import("posthog-js")).default;
    posthog.init(VITE_POSTHOG_KEY, {
      api_host: VITE_POSTHOG_HOST || "https://eu.i.posthog.com",
      person_profiles: "identified_only",
    });
  }
}

export function track(event: string, properties?: Record<string, unknown>): void {
  posthog?.capture(event, properties);
}
