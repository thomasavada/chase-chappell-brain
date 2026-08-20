# Chase Chappell Brain

Unofficial teaching plugin for [Chase Chappell](https://www.youtube.com/@ChaseChappell). Same shape as Avada **Joy brain**: knowledge lives next to skills; the agent **reads the file** instead of guessing.

**Start here:** `/teach-chase` — taught like [this video](https://youtu.be/42uhZYnyEXU?t=936): one metric combo, you guess, then one job.

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

Run that from another directory (absolute path) if you want the real test — skills must work *outside* this repo.

| Ask | Expected |
|---|---|
| `/teach-chase facebook ads` | Scenario (e.g. flat sales + high ROAS), you guess, then the t=9:36 job |
| *"Why do brands need subscriptions?"* | `subscription-ltv` |
| *"Write a Python reverse-string function"* | **no** Chase skill fires |

```
/plugin list
```

## Skills

| Skill | Owns |
|---|---|
| **`teach-chase`** | **Default.** Multi-session teacher. Slash: `/teach-chase` |
| `ask-chase` | Which skill fits |
| `chase-chappell-brain` | Index — which note to Read |
| `diagnose-ad-account` | Metric → one job |
| `run-facebook-ads` | 4-campaign, scale, AOV floor |
| `andromeda-stack` | Indexing, Hub, Euka, matchback |
| `33-percent-creative` | Unique formats in one ad set |
| `tiktok-shop-army` | Affiliates, GPM, request rate |
| `subscription-ltv` | Why one-time sales cap you |
| `brand-stories` | Roster + head-to-heads |
| `hims-diagnostic` | Quiz, sell desire |
| `positioning` | 5 levels, villain |
| `ai-creative-stack` | Claude + Meta Ads MCP |

**Knowledge (Obsidian):** open `plugins/chase-chappell-knowledge/knowledge/` as a vault.

**Graph:** `graphify-out/graph.html`.

Student files land in `learners/` (gitignored). `/teach-chase` always grills a mission first.

## Layout (Joy brain format)

| Path | What |
|---|---|
| [`docs/install-claude-code.md`](docs/install-claude-code.md) | Claude plugin install |
| [`CLAUDE.md`](CLAUDE.md) | invariants |
| [`shared/RESOLVER.md`](shared/RESOLVER.md) | which task reads what |
| `plugins/chase-chappell-knowledge/` | plugin — **`/teach-chase` first**, then doctrine skills + knowledge |
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
