#!/usr/bin/env node
// Catches drift that `claude plugin validate` and `claude plugin tag` cannot see.
//
// starlink-brain's ADR-0001 says it plainly: `tag --dry-run` catches version drift
// between plugin.json and the marketplace entry, but "does NOT catch drift between
// the Claude and Codex copies -- that remains human discipline". This replaces that.
//
// ADR-0003: a plain-scalar description containing `: ` breaks the frontmatter; the
// runtime then loads the file with EMPTY metadata and reports nothing.
//
// Measured 2026-08-13: `claude plugin validate --strict` DOES catch the already-broken
// case, with an excellent message ("At runtime this skill loads with empty metadata").
// So the ADR-0003 hard-fail here is a second net, not the only one. What this script
// catches that validate does NOT:
//   1. drift between the Claude and Codex manifests (ADR-0001: nothing catches it)
//   2. plugin.json vs marketplace entry version drift => the catalog lies
//   3. an unquoted description that CURRENTLY still parses -- validate sees nothing
//      wrong, but it is one `: ` away from dying silently. Warning level.
//
// Run: node scripts/check-parity.mjs   (exit 1 on error)

import { readFileSync, existsSync, readdirSync, statSync } from "node:fs";
import { join, relative } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(fileURLToPath(new URL(".", import.meta.url)), "..");
const errors = [];
const warnings = [];

const fail = (m) => errors.push(m);
const warn = (m) => warnings.push(m);
const readJson = (p) => JSON.parse(readFileSync(p, "utf8"));
const rel = (p) => relative(ROOT, p);

// --- 1. Both marketplaces must list the same plugin set ---------------------
const claudeMarketPath = join(ROOT, ".claude-plugin/marketplace.json");
const codexMarketPath = join(ROOT, ".agents/plugins/marketplace.json");

for (const p of [claudeMarketPath, codexMarketPath]) {
  if (!existsSync(p)) {
    fail(`missing manifest: ${rel(p)}`);
  }
}
if (errors.length) {
  report();
}

const claudeMarket = readJson(claudeMarketPath);
const codexMarket = readJson(codexMarketPath);

if (claudeMarket.name !== codexMarket.name) {
  fail(
    `marketplace name drift: Claude "${claudeMarket.name}" vs Codex "${codexMarket.name}"`,
  );
}

const claudeNames = (claudeMarket.plugins ?? []).map((p) => p.name).sort();
const codexNames = (codexMarket.plugins ?? []).map((p) => p.name).sort();

for (const n of claudeNames) {
  if (!codexNames.includes(n)) fail(`plugin "${n}" is in Claude, missing from Codex`);
}
for (const n of codexNames) {
  if (!claudeNames.includes(n)) fail(`plugin "${n}" is in Codex, missing from Claude`);
}

// --- 2. Per plugin: both plugin.json must agree, and match the marketplace ---
for (const entry of claudeMarket.plugins ?? []) {
  const dir = join(ROOT, entry.source.replace(/^\.\//, ""));
  const claudePluginPath = join(dir, ".claude-plugin/plugin.json");
  const codexPluginPath = join(dir, ".codex-plugin/plugin.json");

  if (!existsSync(claudePluginPath)) {
    fail(`${entry.name}: missing ${rel(claudePluginPath)}`);
    continue;
  }
  if (!existsSync(codexPluginPath)) {
    fail(`${entry.name}: missing ${rel(codexPluginPath)}`);
    continue;
  }

  const a = readJson(claudePluginPath);
  const b = readJson(codexPluginPath);

  for (const field of ["name", "version", "description"]) {
    if (JSON.stringify(a[field]) !== JSON.stringify(b[field])) {
      fail(
        `${entry.name}: "${field}" differs between .claude-plugin and .codex-plugin\n` +
          `      claude: ${JSON.stringify(a[field])}\n` +
          `      codex : ${JSON.stringify(b[field])}`,
      );
    }
  }

  // Invariant #4 -- validate --strict catches it too, but failing early is cheaper
  for (const [label, obj, path] of [
    ["claude", a, claudePluginPath],
    ["codex", b, codexPluginPath],
  ]) {
    if (!obj.author?.name) fail(`${entry.name}: ${rel(path)} is missing author.name`);
  }

  // plugin.json wins at install => drift makes the CATALOG LIE, it does not break installs
  if (a.version !== entry.version) {
    fail(
      `${entry.name}: version drift -- plugin.json "${a.version}" vs ` +
        `.claude-plugin/marketplace.json "${entry.version}". ` +
        `The runtime uses plugin.json, so the catalog is lying.`,
    );
  }
}

// --- 3. ADR-0003 -- every frontmatter description must be quoted ------------
function walk(dir, out = []) {
  if (!existsSync(dir)) return out;
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walk(p, out);
    else if (name.endsWith(".md")) out.push(p);
  }
  return out;
}

for (const file of walk(join(ROOT, "plugins"))) {
  const text = readFileSync(file, "utf8");
  if (!text.startsWith("---\n")) continue; // no frontmatter, skip
  const end = text.indexOf("\n---", 4);
  if (end === -1) {
    fail(`${rel(file)}: frontmatter opened but never closed`);
    continue;
  }
  const fm = text.slice(4, end);

  for (const key of ["description", "argument-hint"]) {
    const line = fm.split("\n").find((l) => l.startsWith(`${key}:`));
    if (!line) continue;
    const value = line.slice(key.length + 1).trim();
    if (!value) continue;
    const quoted = /^["']/.test(value);
    if (!quoted) {
      const rest = fm.slice(fm.indexOf(line) + line.length);
      const continued = /^\n\s+\S/.test(rest);
      const risky = value.includes(": ") || value.startsWith("[") || continued;
      const msg =
        `${rel(file)}: "${key}" is an unquoted plain scalar` +
        (risky ? " AND contains parser-breaking structure" : "");
      // Already contains `: ` or opens `[` => already broken. Otherwise => one char away.
      risky ? fail(msg) : warn(msg + " (not broken yet, but fragile -- ADR-0003)");
    }
  }
}

function report() {
  for (const w of warnings) console.log(`  ⚠ ${w}`);
  for (const e of errors) console.log(`  ✖ ${e}`);
  if (errors.length) {
    console.log(`\n✖ ${errors.length} parity error(s).`);
    process.exit(1);
  }
  console.log(
    warnings.length
      ? `\n✔ Parity clean (${warnings.length} warning(s)).`
      : "✔ Parity clean.",
  );
  process.exit(0);
}

report();
