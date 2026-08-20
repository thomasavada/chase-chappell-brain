# Install — Grok

Grok reads the same `.claude-plugin/marketplace.json` as Claude Code. No extra `.grok-plugin/` copy — three version numbers is three chances to ship a mismatch.

After install, `/teach-chase` and `/break-down-brand` work from **any directory**, not only this repo.

## 1. Add the marketplace

```bash
grok plugin marketplace add thomasavada/chase-chappell-brain
```

GitHub shorthand, a full `https://github.com/thomasavada/chase-chappell-brain.git` URL, or a local clone path all work.

## 2. Install and trust

```bash
grok plugin install chase-chappell-knowledge --trust
```

`--trust` is required the first time: without it Grok prints the source and stops. This plugin has no hooks or MCP servers; trust only means “load the skills.”

Grok plugins stay **off until enabled**. If `/teach-chase` is missing after install:

```bash
grok plugin enable chase-chappell-knowledge
```

Or add the name to `~/.grok/config.toml`:

```toml
[plugins]
enabled = ["cmux-workflow", "chase-chappell-knowledge"]
```

Start a **new** Grok session (or press `r` in the Plugins tab). This session will not see a plugin installed mid-chat.

## 3. Check it loaded

```bash
grok plugin list
grok plugin details chase-chappell-knowledge
```

You should see `1 skill dir(s), 1 command dir(s)`. Then, from **any other directory**:

```
/teach-chase facebook ads
/break-down-brand Hims
```

Grok must **Read** a file under `knowledge/` — not answer from memory.

| Ask | Expected |
|---|---|
| `/break-down-brand Hims` | Hook + unique ads + army + rival from `Brand atlas.md` |
| `/teach-chase` *teach me important meta ads metrics* | High CPM first — *quickest way to lower it?* |
| *"Write a Python function to reverse a string"* | **no** Chase skill fires |

## Update

```bash
grok plugin marketplace update chase-chappell
grok plugin update chase-chappell-knowledge
```

Runtime detects updates by **`version`**, not by commit. If a skill changed and you see nothing new, the publisher forgot to bump `plugin.json`.

## Try without a marketplace (one machine)

Already cloned the repo?

```bash
grok plugin install /absolute/path/to/chase-chappell-brain/plugins/chase-chappell-knowledge --trust
grok plugin enable chase-chappell-knowledge
```

That copies the plugin into `~/.grok/` (user scope, auto-trusted). It will **not** auto-update with git pull — use the marketplace path for that.

## Knowledge path

Skills Read `${CLAUDE_PLUGIN_ROOT}/knowledge/…`. Grok sets that alias to the same value as `GROK_PLUGIN_ROOT`. Do not rewrite the skills to `GROK_PLUGIN_ROOT` only — Claude Code would then miss them.
