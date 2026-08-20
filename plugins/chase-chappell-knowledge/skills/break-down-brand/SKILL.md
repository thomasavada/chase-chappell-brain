---
name: break-down-brand
description: "Break down a DTC/ecom brand the way Chase Chappell does: hook line (not the SKU), unique ad volume, creator army, TTS vs Meta, funnel, brand level, nearest rival. Always combine Chase's lens with live research (Ads Library, site, filings). Use when the user says break down a brand like Chase, teardown Hims, why Gruns beat Bloom, analyse Medicube, or paste a brand URL. Do NOT use to teach Meta metrics (that is teach-chase). Do NOT invent Chase quotes or unaudited scale."
argument-hint: "Brand name or URL"
---

# Break down a brand like Chase

Two sources. **Both required.** Chase is the lens. Live research is today's evidence.

Knowledge: `${CLAUDE_PLUGIN_ROOT}/knowledge/`. Template: `concepts/Brand breakdown.md`. Roster: `brands/Brand atlas.md`.

Filling the table from the atlas only is a fail. Dumping a site visit without Chase's system/hook is also a fail.

## STOP

1. **Read** `concepts/Brand breakdown.md` (the skeleton + three levers).
2. **Read** `brands/Brand atlas.md`. If the brand is in the table or a head-to-head, keep *his* hook and Watch. Treat his scale/ad-count as **claimed, dated** — not current.
3. If it is Hims / David / Bloom / a named long-form, also Read that concept or `sources/` card.
4. Then **research today** (required, even when the atlas has a row):

| Fetch | Where |
|---|---|
| Funnel / offer / quiz / sub default / AOV | Brand site + consult/PDP. Browser if the page is JS-walled. |
| Unique **active** Meta ads + formats | [Ads Library](https://www.facebook.com/ads/library/) — search the Page, country US, Active. Count unique creatives, not variants of one ID if the UI groups them. Date it. |
| Rival unique ads | Same Ads Library search for the nearest competitor. **Volume = verdict.** |
| Army | TikTok Shop / affiliate count if shoppable; else Meta Hub/collab vs face-only celebrity. |
| Scale | Official filing or press **beats** Chase claimed when they disagree. Tag both. |

`web_search` + `open_page` / browser. Ads Library and most storefronts are JS-walled — open them. No graphify. Do not skip this step because “Chase already covered it.”

If Ads Library is login-walled or the count is not on the page, say **unverified today** and keep Chase's claimed number in the Chase column. Do not invent a count.

## Do

One page. Chase-short energy: hook first, then proof.

```
# {Brand} — Chase-style breakdown

Hook: They're not a {category} brand. They're a {system}.
      (Chase's line if he named it. Else write one in his voice and say he didn't cover this.)

| Slot | Chase (claimed) | Live · {YYYY-MM-DD} |
| Scale | atlas / source | filing or press |
| Ads | atlas unique count | Ads Library unique active + formats |
| Army | atlas | TTS / Hub / face-only, live |
| Funnel | if he named it | what the site does now |
| Level | L1–L5 | same, unless live evidence moved it |
| Rival | his head-to-head | who has more unique ads *today* |
| Monday job | — | one system to copy, from the *live* gap |
| Watch | his youtu.be | Ads Library URL |
```

Rules:

- **Volume = verdict.** Rival row without two live (or explicitly unverified) ad counts is incomplete.
- **Sell the problem / desire**, not the bottle (Hims, Mars Men).
- Tag every dollar and ad-count **claimed** unless you fetched it this run (then say the date).
- Chase's hook can stay even when live numbers moved. The point of research is to see whether the *system* is still true.
- Do not teach a lesson. Do not grill MISSION.md. That is `teach-chase`.

## Completion

The user can repeat the hook line, say whether live ads still match Chase's volume call, and name the Monday job.
