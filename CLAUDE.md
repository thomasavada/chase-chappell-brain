# chase-chappell-brain

Marketplace plugin: unofficial **Chase Chappell** teaching corpus (Meta ads, TikTok Shop, brand stories). Works from **any directory**, not only inside this repo.

Channel: https://www.youtube.com/@ChaseChappell — **not affiliated**.

## Three runtimes, two manifests

| Runtime | Reads |
|---|---|
| **Claude Code** | `.claude-plugin/` |
| **Codex** | `.agents/plugins/` + `.codex-plugin/` |
| **Grok** | `.claude-plugin/` (same files as Claude) |

## Structure

| Path | What |
|---|---|
| `.claude-plugin/marketplace.json` | catalog — Claude **and Grok** |
| `.agents/plugins/marketplace.json` | catalog — Codex |
| `plugins/chase-chappell-knowledge/` | skills + `knowledge/` |
| `shared/RESOLVER.md` | which task reads what first |
| `graphify-out/` | committed knowledge graph |
| `learners/` | gitignored student workspace |

**Install (Claude Code):** [`docs/install-claude-code.md`](docs/install-claude-code.md) — `/plugin marketplace add` then `/plugin install chase-chappell-knowledge@chase-chappell`. The plugin ships **one skill:** **`/teach-chase`**.

**Content is markdown** in `plugins/chase-chappell-knowledge/knowledge/` (playbook, concepts, 26 source cards, brand atlas). Open that folder as an **Obsidian vault**. `graphify-out/` is only a wikilink map of those files.

## Invariants

1. Marketplace is named `chase-chappell`.
2. A registry change touches **both** `marketplace.json` files. A plugin change touches **both** `plugin.json` files.
3. A skill change bumps `version` in **all four** places.
4. Every `plugin.json` needs `author`.
5. Every frontmatter `description` is a **quoted YAML scalar**.
6. **Distil, never copy transcripts.** YouTube is the primary. Two copies of doctrine (skill + knowledge) is a bug — skills point, knowledge owns.
7. No binaries over 1 MB.

## Boundaries

| This brain | Not this brain |
|---|---|
| Chase doctrine, Watch links, brand roster | Raw transcripts |
| How to *teach* Facebook ads | Live ad-account spend / MCP publish |
| Claimed figures, labelled claimed | Avada, Joy, WeTracked, OpenShop |

## Publishing

1. Bump version in both `plugin.json` and both `marketplace.json`
2. `node scripts/check-parity.mjs`
3. `claude plugin validate ./plugins/chase-chappell-knowledge --strict` and `claude plugin validate . --strict` if those CLIs exist
4. Commit, push
