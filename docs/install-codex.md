# Install — Codex

Marketplace catalog for Codex is `.agents/plugins/marketplace.json`. Same plugin as Claude: `plugins/chase-chappell-knowledge`.

```
# from this repo, one session
codex --plugin-dir ./plugins/chase-chappell-knowledge
```

Then ask to **teach** Facebook ads. The skill is `teach-chase`.

If your Codex build uses `npx skills`:

```
npx skills@latest add thomasavada/chase-chappell-brain
```

Pick `teach-chase` first.
