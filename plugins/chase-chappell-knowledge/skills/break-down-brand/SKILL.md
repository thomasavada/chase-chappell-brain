---
name: break-down-brand
description: "Break down a DTC/ecom brand the way Chase Chappell does in his Shorts and Hims/David videos: hook line (not the SKU), unique ad volume, creator army, TTS vs Meta, funnel, brand level, nearest rival. Use when the user says break down a brand like Chase, teardown Hims, why Gruns beat Bloom, analyse Medicube, or paste a brand URL. Do NOT use to teach Meta metrics (that is teach-chase). Do NOT invent Chase quotes or unaudited scale."
argument-hint: "Brand name or URL"
---

# Break down a brand like Chase

Knowledge: `${CLAUDE_PLUGIN_ROOT}/knowledge/`. Template: `concepts/Brand breakdown.md`. Roster: `brands/Brand atlas.md`.

## STOP

1. **Read** `concepts/Brand breakdown.md` (the skeleton).
2. **Read** `brands/Brand atlas.md`. If the brand is in the table or a head-to-head, use *his* hook and Watch link.
3. If it is Hims / David / Bloom / a named long-form, also Read that concept or `sources/` card.
4. No shell. No graphify.

## Do

Fill **every row** of the skeleton. One page. Chase-short energy: hook first, then proof.

```
# {Brand} — Chase-style breakdown

Hook: They're not a {category} brand. They're a {system}.

| Slot | Call |
| Scale | {claimed} |
| Ads | {unique count + formats} |
| Army | {TTS / Hub / face-only} |
| Funnel | {quiz / sub / first-box / AOV} |
| Level | L1–L5 |
| Rival | {who} — volume verdict |
| Monday job | {one system to copy} |
| Watch | {youtu.be from atlas or Ads Library} |
```

Rules:

- **Volume = verdict.** If you name a rival, compare unique ads, not vibes.
- **Sell the problem / desire**, not the bottle (Hims, Mars Men).
- Tag every dollar and ad-count **claimed** unless you fetched a live Ads Library count (then say the date).
- If the brand is **not** in the atlas: still run the template from public ads/site. Say “Chase didn’t cover this.” Do not fake a Chase take.
- Do not teach a lesson. Do not grill MISSION.md. That is `teach-chase`.

## Completion

The user can repeat the hook line and the Monday job. If they ask “teach me to do this,” hand off to `/teach-chase`.
