# Chase Chappell Brain

Unofficial teaching plugin for [Chase Chappell](https://www.youtube.com/@ChaseChappell) (Ads Mastery). Same shape as Avada **Joy brain**: knowledge lives next to skills, the agent **reads the file** instead of guessing.

**Not affiliated.** Numbers are *claimed*. Watch the originals. Not financial advice.

## What ships

| Skill | Owns |
|---|---|
| `chase-chappell-brain` | Index — which note to read |
| `teach-chase` | Matt Pocock-style teacher, grounded in this corpus |
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

**Knowledge:** `plugins/chase-chappell-knowledge/knowledge/` (open that folder in Obsidian).

**Graph:** `graphify-out/graph.html` — query before answering.

## Try it

```bash
git clone https://github.com/thomasavada/chase-chappell-brain
claude --plugin-dir ./plugins/chase-chappell-knowledge
```

Then: *"Teach me how to run Facebook ads"* or *"Why do brands need subscriptions?"*

Obsidian: **Open folder as vault** → `plugins/chase-chappell-knowledge/knowledge`.

Student files land in `learners/` (gitignored). `/teach-chase` grills a mission first.

## Layout (Joy brain format)

| Path | What |
|---|---|
| [`CLAUDE.md`](CLAUDE.md) | invariants |
| [`shared/RESOLVER.md`](shared/RESOLVER.md) | which task reads what |
| `plugins/chase-chappell-knowledge/` | plugin — skills + knowledge |
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
