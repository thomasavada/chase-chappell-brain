---
name: chase-chappell-brain
description: "Chase Chappell ecom teaching brain: Meta/Facebook ads, Andromeda, 33 percent creative rule, TikTok Shop armies, subscriptions/LTV, brand stories, Hims diagnostic, villain marketing, AI creative stack. Use when the user asks about Chase Chappell, how to run Facebook ads, why an ad account is stuck, TikTok Shop affiliates, why brands need subscriptions, or which brands Chase mentioned. Also use when they want to be taught a topic from this corpus. Do NOT use for Avada/Joy product work or for cloning a CAPI pixel app."
---

# Chase Chappell product brain

Knowledge lives in `${CLAUDE_PLUGIN_ROOT}/knowledge/`.

## STOP — mandatory read protocol

**Before writing a sentence, Read the file named in the tables.** This skill is an index. Answering from the index (or from memory of Chase videos) is the failure this skill exists to prevent.

1. Read the mapped file with the Read tool
2. Cite at least one specific fact (a number, a named rule, a Watch URL)
3. Tag scale/ad-count/GMV as **claimed**
4. If the area is empty, say so

If `graphify-out/graph.json` exists at the repo root, prefer `graphify query "<question>"` first, then Read the cited notes.

## Skill map

| Question | Skill |
|---|---|
| Teach me X over multiple sessions | `teach-chase` |
| Which skill should I use | `ask-chase` (same map) |
| CPM/CTR/CVR/ROAS/returning looks wrong | `diagnose-ad-account` |
| How do I run / scale Facebook ads | `run-facebook-ads` |
| Andromeda, matchback, Hub, Euka | `andromeda-stack` |
| What creatives / 33% / 2027 | `33-percent-creative` |
| TikTok Shop, affiliates, GPM | `tiktok-shop-army` |
| Why subscriptions / LTV | `subscription-ltv` |
| Brands Chase named, David vs Prima | `brand-stories` |
| Hims quiz / diagnostic | `hims-diagnostic` |
| 5 levels, villain, positioning | `positioning` |
| Claude MCP, AI ads | `ai-creative-stack` |

## Directory map

| Directory | Contents |
|---|---|
| `foundations/` | [[playbook]], [[glossary]] |
| `concepts/` | One doctrine note per idea |
| `sources/` | 26 long-form cards + Watch |
| `brands/` | Atlas + 233 Shorts catalog |

## Quick lookup

| Question | Read |
|---|---|
| Whole picture | `foundations/playbook.md` |
| Terms | `foundations/glossary.md` |
| Ads dying / which metric | `concepts/Metric diagnosis tree.md` |
| Campaign structure | `concepts/4-campaign method.md` |
| Why AOV $35 | `concepts/Break-even ROAS and AOV floor.md` |
| Why sub | `concepts/Three levels of purchase.md` |
| Andromeda | `concepts/Andromeda stack.md` |
| Unique formats | `concepts/33 percent rule.md` |
| TTS | `concepts/TikTok Shop army.md` |
| Brand roster | `brands/Brand atlas.md` |
| A specific video | `sources/` + [[Source index]] |

## Known gaps — say so

- No raw transcripts (copyright). Send them to YouTube.
- No private ad accounts, Avada, Joy, or WeTracked notes.
- Chase figures are marketing claims.
- Shorts older than 2025-08-21 are not in the catalog.
