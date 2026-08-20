# Install — Codex

Marketplace catalog for Codex is `.agents/plugins/marketplace.json`. Same plugin folder as Claude and Grok: `plugins/chase-chappell-knowledge`.

After install, `teach-chase` and `break-down-brand` work from **any directory**.

## 1. Add the marketplace

```bash
codex plugin marketplace add thomasavada/chase-chappell-brain
```

Local clone instead of GitHub:

```bash
codex plugin marketplace add /absolute/path/to/chase-chappell-brain
```

## 2. Install the plugin

```bash
codex plugin add chase-chappell-knowledge@chase-chappell
```

(`add`, not `install` — that is the Codex verb.) If the marketplace name differs on your Codex build, `codex plugin marketplace list` prints the name to put after `@`.

## 3. Check it loaded

```bash
codex plugin list
```

Then, from **any other directory**, ask to **teach** Facebook ads or **break down Hims**. Codex should load `teach-chase` / `break-down-brand` and Read `knowledge/` — not answer from memory.

Slash commands (`/teach-chase`) are host-dependent on Codex. If they do not appear, invoke the skill by name; it is the same file.

## Update

Codex has **no auto-update**. Refresh by hand:

```bash
codex plugin marketplace upgrade chase-chappell
```

## One session, no marketplace

```bash
codex --plugin-dir ./plugins/chase-chappell-knowledge
```

The real test is from another directory, with an absolute `--plugin-dir`.
