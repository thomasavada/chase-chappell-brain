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
| `/teach-chase facebook ads` | Scenario (e.g. flat sales + high ROAS), you guess, then the t=9:36 job |
| *"Why do brands need subscriptions?"* | `teach-chase` → `Three levels of purchase.md` |
| *"Write a Python reverse-string function"* | **no** Chase skill fires |

```
/plugin list
```

## What ships

**One skill:** `teach-chase` (slash `/teach-chase`). Everything else is notes in `knowledge/` — Andromeda, 33% rule, TTS, subscriptions, brand atlas — taught through that classroom, not as extra skills.

**Knowledge (Obsidian):** open `plugins/chase-chappell-knowledge/knowledge/` as a vault.

**Graph:** `graphify-out/graph.html`.

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
