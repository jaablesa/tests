import "@fontsource/bungee";
import "@fontsource/jetbrains-mono/400.css";
import "@fontsource/jetbrains-mono/600.css";
import "./style.css";
import { start } from "./scene.js";
import { startTelemetry, track } from "./telemetry";

void startTelemetry();
start({ onTravel: ({ city, language }) => track("city_visited", { city, language }) });
