import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react";

function normalizeBasePath(input) {
  const raw = (input || "").trim() || "/Quant_Practise/";
  const withLeadingSlash = raw.startsWith("/") ? raw : `/${raw}`;
  return withLeadingSlash.endsWith("/") ? withLeadingSlash : `${withLeadingSlash}/`;
}

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "");
  return {
    plugins: [react()],
    base: normalizeBasePath(env.VITE_SITE_BASE),
    build: {
      outDir: "../docs",
      emptyOutDir: true,
    },
  };
});
