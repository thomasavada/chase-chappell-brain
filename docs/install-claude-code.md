# Install — Claude Code

This repo is a **plugin marketplace**, not a folder Claude auto-loads. Cloning it does **not** install the skills. Claude Code only auto-loads `.claude/skills/` inside a project. Ours live under `plugins/chase-chappell-knowledge/skills/` in marketplace format, so you must add the marketplace, then install.

Codex and Grok: [`install-codex.md`](install-codex.md) · [`install-grok.md`](install-grok.md).

After install: **`/teach-chase`** (classroom) or **`/break-down-brand Hims`** (teardown).

## 1. Add the marketplace

In a Claude Code session:

```
/plugin marketplace add https://github.com/thomasavada/chase-chappell-brain.git
```

**The `.git` suffix is required.** Without it, Claude Code treats the URL as a *file* to HTTP GET instead of `git clone`.

## 2. Install the plugin

```
/plugin install chase-chappell-knowledge@chase-chappell
```

Turn on **Enable auto-update** in `/plugin` so new skills arrive next session.

## 3. Check it loaded

```
/plugin list
```

You should see `chase-chappell-knowledge` from marketplace `chase-chappell`.

Then, **from any other directory** (not this repo):

```
/teach-chase facebook ads
```

Claude must load skill `teach-chase`, grill a mission, and **Read** a file under `knowledge/` — not answer from memory. That is the whole point of a brain: it works outside the repo.

| Ask | Expected |
|---|---|
| `/break-down-brand Hims` | Chase hook + live Ads Library / site / rival (two-column). Not atlas-only. |
| `/teach-chase` *teach me important meta ads metrics* | High CPM first — *quickest way to lower it?* — **not** a Shopify numbers quiz |
| *My sales are flat, ROAS is high* | Then grill spend / returning % / CTR+CPM, then t=9:36 |
| *"Why do brands need subscriptions?"* | `teach-chase` → `Three levels of purchase.md` |
| *"Which brands did Chase mention?"* | `teach-chase` → `Brand atlas.md` |
| *"Write a Python function to reverse a string"* | **no** Chase skill fires |

## Update

```
/plugin marketplace update chase-chappell
```

Runtime detects updates by **`version`**, not by commit. If a skill changed and you see nothing new, the publisher forgot to bump `plugin.json`.

## Try without installing (one session)

Already cloned the repo? Load the plugin for **this session only** — no marketplace, no leftover install:

```bash
claude --plugin-dir ./plugins/chase-chappell-knowledge
```

The real test is from **another directory**:

```bash
cd ~/some-other-project
claude --plugin-dir ~/Documents/chase-chappell-brain/plugins/chase-chappell-knowledge
```

Then `/teach-chase`.

Plugin skills are namespaced `chase-chappell-knowledge:teach-chase`. A copy in `~/.claude/skills` would show up *without* the prefix and will drift — delete the personal copy once the plugin works.

## Obsidian (the markdown)

The doctrine is **markdown**, not the graph JSON.

Open folder as vault:

`plugins/chase-chappell-knowledge/knowledge`

Start at `index.md`. Graph (optional map of those notes): repo `graphify-out/graph.html`.
