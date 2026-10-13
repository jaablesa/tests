import posthog from "posthog-js";

/** Product events: snake_case, past tense, e.g. track("signup_completed", { plan: "free" }). */
export function track(event: string, properties?: Record<string, unknown>): void {
  if (process.env.NEXT_PUBLIC_POSTHOG_KEY) posthog.capture(event, properties);
}
