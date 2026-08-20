# Chase Chappell Brain

Unofficial teaching plugin for [Chase Chappell](https://www.youtube.com/@ChaseChappell). Same shape as Avada **Joy brain**: knowledge lives next to **one skill**; the agent **reads the file** instead of guessing.

**The skill:** `/teach-chase` — like [this video](https://youtu.be/42uhZYnyEXU?t=936): one metric combo, you guess, then one job.

**Not affiliated.** Numbers are *claimed*. Watch the originals. Not financial advice.

## Install (Claude Code)

Cloning this repo does **not** install the plugin. Full guide: [`docs/install-claude-code.md`](docs/install-claude-code.md).

```
/plugin marketplace add https://github.com/thomasavada/chase-chappell-brain.git
/plugin install chase-chappell-knowledge@chase-chappell
```

Then, from **any folder**:

```
/teach-chase facebook ads
```

> **The `.git` suffix is required** on the marketplace URL. Without it Claude Code HTTP-GETs a file instead of `git clone`.

**Codex:** [`docs/install-codex.md`](docs/install-codex.md).

### One session, no install

```bash
claude --plugin-dir ./plugins/chase-chappell-knowledge
```

Run that from another directory (absolute path) if you want the real test — the skill must work *outside* this repo.

| Ask | Expected |
|---|---|
| `/teach-chase facebook ads` or *teach me important meta ads metrics* | High CPM first (*quickest way to lower it?*) — not a Shopify-numbers quiz |
| *My sales are flat but ROAS is high* | Then the four numbers, then t=9:36 |
| *"Why do brands need subscriptions?"* | `teach-chase` → `Three levels of purchase.md` |
| *"Write a Python reverse-string function"* | **no** Chase skill fires |

```
/plugin list
```

## What ships

**The notes are markdown** (that is the brain). Graphify did **not** replace them — `graphify-out/` is only a map of wikilinks between these files.

Browse on GitHub: [`plugins/chase-chappell-knowledge/knowledge/`](plugins/chase-chappell-knowledge/knowledge/)

| Path | What |
|---|---|
| [`knowledge/index.md`](plugins/chase-chappell-knowledge/knowledge/index.md) | Hub |
| [`foundations/playbook.md`](plugins/chase-chappell-knowledge/knowledge/foundations/playbook.md) | Full synthesis |
| [`foundations/glossary.md`](plugins/chase-chappell-knowledge/knowledge/foundations/glossary.md) | Terms |
| [`concepts/`](plugins/chase-chappell-knowledge/knowledge/concepts/) | Doctrine (diagnosis tree, Andromeda, 33% rule, LTV, …) |
| [`sources/`](plugins/chase-chappell-knowledge/knowledge/sources/) | 26 long-form cards + Watch links |
| [`brands/`](plugins/chase-chappell-knowledge/knowledge/brands/) | Shorts atlas + 233-clip catalog |

Obsidian: **Open folder as vault** → `plugins/chase-chappell-knowledge/knowledge/`.

**One skill:** `teach-chase` (slash `/teach-chase`). It **Reads** those `.md` files and teaches like [t=9:36](https://youtu.be/42uhZYnyEXU?t=936).

**Graph (optional):** [`graphify-out/graph.html`](graphify-out/graph.html) — 46 nodes / 153 EXTRACTED edges from the same markdown. Query layer, not the content.

Student files land in `learners/` (gitignored). `/teach-chase` always grills a mission first.

## Layout (Joy brain format)

| Path | What |
|---|---|
| [`docs/install-claude-code.md`](docs/install-claude-code.md) | Claude plugin install |
| [`CLAUDE.md`](CLAUDE.md) | invariants |
| [`shared/RESOLVER.md`](shared/RESOLVER.md) | which topic reads which note |
| `plugins/chase-chappell-knowledge/` | plugin — **`teach-chase`** + `knowledge/` |
| `scripts/check-parity.mjs` | Claude↔Codex drift gate |

```
node scripts/check-parity.mjs
```

## Doctrine in one screen

1. Ads own **CPM + CTR** only.
2. **AOV floor $35.**
3. **33% rule** — unique formats in one ad set.
4. Andromeda retrieval needs matchback **≥ 8–10**.
5. Subscription is L3 — lose on order 1 to outbid.
6. Ad count is the scoreboard.

Primary: [If you watch one Facebook Ad video](https://youtu.be/42uhZYnyEXU).
