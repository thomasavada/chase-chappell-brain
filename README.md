# Chase Chappell Brain

Unofficial teaching plugin for [Chase Chappell](https://www.youtube.com/@ChaseChappell). Same shape as Avada **Joy brain**: knowledge lives next to skills; the agent **reads the file** instead of guessing.

| Command | Job |
|---|---|
| `/chase` | Router — which skill |
| `/teach-chase` | Classroom like [t=9:36](https://youtu.be/42uhZYnyEXU?t=936): one combo, you guess, one job |
| `/break-down-brand Hims` | Teardown: Chase's system + **live** Ads Library / site / rival |
| `/diagnose-ad-account` | Stuck account → one combo, one job |
| `/andromeda-stack` | Matchback → Hub → Euka → 33% fill |
| `/run-facebook-ads` | 4-campaign + 33% + $35 AOV |
| `/shopify-cro` | ATC / reach checkout / complete checkout |
| `/tiktok-shop-army` | Listing, request rate, GPM, army |
| `/email-sms` | Owned come-back loop |
| `/subscription-ltv` | L1 / L2 / L3 |
| `/ai-creative-stack` | Claude + Meta MCP (no CBO publish) |
| `/positioning` | 5 levels, villain, Hims desire |

**Not affiliated.** Numbers are *claimed*. Watch the originals. Not financial advice.

## Install

Works in **Claude Code**, **Codex**, and **Grok** — one repo. Claude and Grok both read `.claude-plugin/`; Codex reads `.agents/plugins/`. Cloning does **not** install the skills.

```
# Claude Code
/plugin marketplace add https://github.com/thomasavada/chase-chappell-brain.git
/plugin install chase-chappell-knowledge@chase-chappell
```

```bash
# Codex
codex plugin marketplace add thomasavada/chase-chappell-brain
codex plugin add chase-chappell-knowledge@chase-chappell
```

```bash
# Grok
grok plugin marketplace add thomasavada/chase-chappell-brain
grok plugin install chase-chappell-knowledge --trust
grok plugin enable chase-chappell-knowledge
```

Then, from **any folder**:

```
/chase
/teach-chase facebook ads
/break-down-brand Hims
/andromeda-stack
```

Full guides: [`docs/install-claude-code.md`](docs/install-claude-code.md) · [`docs/install-codex.md`](docs/install-codex.md) · [`docs/install-grok.md`](docs/install-grok.md).

> **Claude Code:** the `.git` suffix is required on the marketplace URL. Without it Claude HTTP-GETs a file instead of `git clone`.
>
> **Grok:** plugins stay off until `enable` (or `[plugins].enabled` in `~/.grok/config.toml`). Start a new session after install.

### One session, no install

```bash
claude --plugin-dir ./plugins/chase-chappell-knowledge
codex --plugin-dir ./plugins/chase-chappell-knowledge
grok plugin install ./plugins/chase-chappell-knowledge --trust
```

Run those from another directory (absolute path) if you want the real test — the skill must work *outside* this repo.

| Ask | Expected |
|---|---|
| `/teach-chase facebook ads` or *teach me important meta ads metrics* | High CPM first (*quickest way to lower it?*) — not a Shopify-numbers quiz |
| `/break-down-brand Hims` | Chase hook + **two-column** proof (his claimed vs live Ads Library / filing) |
| *My sales are flat but ROAS is high* | Then the four numbers, then t=9:36 |
| *"Write a Python reverse-string function"* | **no** Chase skill fires |

Check: Claude `/plugin list` · Codex `codex plugin list` · Grok `grok plugin list`.

## What ships

**The notes are markdown** (that is the brain). Graphify did **not** replace them — `graphify-out/` is only a map of wikilinks between these files.

Browse on GitHub: [`plugins/chase-chappell-knowledge/knowledge/`](plugins/chase-chappell-knowledge/knowledge/)

| Path | What |
|---|---|
| [`knowledge/index.md`](plugins/chase-chappell-knowledge/knowledge/index.md) | Hub |
| [`foundations/playbook.md`](plugins/chase-chappell-knowledge/knowledge/foundations/playbook.md) | Full synthesis |
| [`foundations/glossary.md`](plugins/chase-chappell-knowledge/knowledge/foundations/glossary.md) | Terms |
| [`concepts/`](plugins/chase-chappell-knowledge/knowledge/concepts/) | Doctrine (diagnosis tree, Andromeda, 33% rule, LTV, …) |
| [`sources/`](plugins/chase-chappell-knowledge/knowledge/sources/) | 31 long-form cards + Watch links |
| [`brands/`](plugins/chase-chappell-knowledge/knowledge/brands/) | Shorts atlas + 233-clip catalog |

Obsidian: **Open folder as vault** → `plugins/chase-chappell-knowledge/knowledge/`.

**Skills:** classroom `teach-chase` · teardown `break-down-brand` · router `ask-chase` · apply: `diagnose-ad-account`, `andromeda-stack`, `run-facebook-ads`, `shopify-cro`, `tiktok-shop-army`, `email-sms`, `subscription-ltv`, `ai-creative-stack`, `positioning`. Skills **Read** those `.md` files. Doctrine is not copied into skills.

**Graph (optional):** [`graphify-out/graph.html`](graphify-out/graph.html) — 46 nodes / 153 EXTRACTED edges from the same markdown. Query layer, not the content.

Student files land in `learners/` (gitignored). `/teach-chase` always grills a mission first.

## Layout (Joy brain format)

| Path | What |
|---|---|
| [`docs/install-claude-code.md`](docs/install-claude-code.md) | Claude Code |
| [`docs/install-codex.md`](docs/install-codex.md) | Codex |
| [`docs/install-grok.md`](docs/install-grok.md) | Grok |
| [`CLAUDE.md`](CLAUDE.md) | invariants |
| [`shared/RESOLVER.md`](shared/RESOLVER.md) | which topic reads which note |
| `plugins/chase-chappell-knowledge/` | plugin — `teach-chase` + `break-down-brand` + `knowledge/` |
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
