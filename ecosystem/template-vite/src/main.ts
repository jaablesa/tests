import "./style.css";
import { startTelemetry, track } from "./telemetry";

void startTelemetry();

const button = document.querySelector<HTMLButtonElement>("#hello");
button?.addEventListener("click", () => {
  track("hello_clicked");
  button.textContent = "Hello again!";
});
