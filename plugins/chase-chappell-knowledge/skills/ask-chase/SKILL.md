---
name: ask-chase
description: "Route a Chase Chappell question to the right skill. Use when the user says /chase, ask Chase, which skill, or the ask is ambiguous. Do NOT teach a classroom lesson (teach-chase). Do NOT teardown a brand (break-down-brand). Do NOT invent doctrine."
argument-hint: "Question"
---

# Ask Chase

Pick **one** skill. Then run it. Knowledge is in `${CLAUDE_PLUGIN_ROOT}/knowledge/` — skills point, they do not own facts.

| They want | Skill |
|---|---|
| Teach me / classroom / guess then job | `teach-chase` |
| Teardown **this brand** like his Shorts | `break-down-brand` |
| My account is stuck; they paste numbers | `diagnose-ad-account` |
| Andromeda / Hub / Euka / matchback / CAPI | `andromeda-stack` |
| 4-campaign, scale %, 33%, what ads to make | `run-facebook-ads` |
| CVR / PDP / drawer / site speed / first-load | `shopify-cro` |
| TikTok Shop army / affiliates / GPM | `tiktok-shop-army` |
| Email / SMS / Klaviyo / cart flow | `email-sms` |
| Why subscriptions / L1 L2 L3 / LTV | `subscription-ltv` |
| Claude + Meta MCP / AI UGC / Higgsfield | `ai-creative-stack` |
| 5 levels / villain / Hims quiz desire | `positioning` |

Ambiguous → one clarifying question, then route. Python reverse-string → **no** Chase skill.
