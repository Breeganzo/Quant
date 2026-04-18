import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const siteRoot = path.resolve(__dirname, "..");
const repoRoot = path.resolve(siteRoot, "..");
const publicRoot = path.join(siteRoot, "public");

const copyTargets = ["curriculum", "references", "templates", "README.md"];
const staleTargets = ["docs"];

for (const target of staleTargets) {
  fs.rmSync(path.join(publicRoot, target), { recursive: true, force: true });
}

for (const target of copyTargets) {
  const src = path.join(repoRoot, target);
  const dest = path.join(publicRoot, target);
  fs.rmSync(dest, { recursive: true, force: true });
  fs.cpSync(src, dest, { recursive: true });
}

console.log("Synced curriculum, references, templates, and README into site/public");
