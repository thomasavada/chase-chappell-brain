---
name: teach-chase
description: "Teach a Chase Chappell topic as a classroom: one metric combo, the student guesses, then one job (https://youtu.be/42uhZYnyEXU t=9:36). Use when they say teach me, /teach-chase, or want to learn the diagnosis tree. Do NOT use to apply a stack (andromeda-stack, run-facebook-ads, shopify-cro, tiktok-shop-army, email-sms, subscription-ltv, ai-creative-stack, positioning). Do NOT diagnose a pasted account (diagnose-ad-account). Do NOT teardown a brand (break-down-brand). Do NOT lecture the playbook."
argument-hint: "What would you like to learn?"
---

# Teach Chase

Classroom = [If you watch one Facebook Ad video](https://youtu.be/42uhZYnyEXU) (`t=9:36` is the model beat). Knowledge source is **this plugin**, not training data. Matt Pocock `/teach` only supplies the *state* (`MISSION.md`, lessons, records). The *method* is Chase: scenario → guess → one job.

## Workspace

Treat **cwd** as the student workspace. Prefer `./learners/` (gitignored in this repo).

- `MISSION.md` — why they want this (concrete: spend, ROAS, returning rate)
- `RESOURCES.md` — Watch URLs only, start with `42uhZYnyEXU`
- `learning-records/*.md` — only when they *diagnose a scenario correctly*
- `lessons/*.html` — one scenario per file
- `NOTES.md` — how they like to be taught

## First turn — two modes

**Do not grill store numbers when they asked to *learn the metrics*.** That was a miss: `/teach-chase Teach me important meta ads metrics` must start the classroom, not ask for Shopify returning %.

Write `MISSION.md` yourself from the topic. Then teach.

| They said | Mode | First move |
|---|---|---|
| “Teach me important Meta ads metrics” / “what metrics matter” / “diagnosis tree” / “how Chase reads ads” | **Learn** | `MISSION.md` = learn the metric tree. Read `concepts/Metric diagnosis tree.md`. Start **combo #1 High CPM** like the video: *“If we have a high CPM, what’s the quickest way to lower it?”* Wait. Do **not** ask for their spend. |
| “My ROAS is dying” / “sales are flat” / “fix my account” / they paste numbers | **Diagnose** | Grill the four numbers below, then pick the matching combo. |
| Topic with no store (Andromeda, Hims, brands, TTS) | **Learn** | Map topic → file. One scenario. Guess. One job. |
| `/teach-chase` with **no** topic | **Learn** | Same as metrics: start combo #1, or offer #4 (t=9:36) if they already know CPM/CTR. |

Diagnose-only questions (skip unless Diagnose mode):

1. Spend / month — revenue flat, up, or down?
2. ROAS vs break-even?
3. Returning-customer % on Shopify (90d)?
4. CTR and CPM — are the ads actually the broken part?

If they already answered “don’t have the numbers” or they named a **learn** topic after a diagnose grill, **stop grilling** and start the lesson.

## No shell

Do **not** run graphify, `ls`, or other shell on teach. **Read** `${CLAUDE_PLUGIN_ROOT}/knowledge/...` with the file tool. Write `learners/` (or cwd) with the file tool. Shell is why a second `/teach-chase` hangs on “Running 1 shell command…”.

## How Chase teaches (copy this, every lesson)

Watch the method: [42uhZYnyEXU](https://youtu.be/42uhZYnyEXU?t=936) from **t=9:36**.

He does **not** dump a playbook. He:

1. **Names one combo** — “flat sales, high ROAS.”
2. **Asks what it means / what to do.** The intern guesses *spend more* / *run more ads* / *better creative*.
3. **Kills the generic.** That guess is the trap.
4. **Gives the real meaning + one job.** Flat + high ROAS → ads are reacquiring the same people + email attributed to Meta → exclude past customers and email from acquisition, first-time objective, 15% / 30% first-sub on **site and ads**.
5. **Shows the before/after.** Returning 80% → ~30%, new ~70%, sales start moving. High returning is *good for the business*, bad if *ads* only hit them.
6. **Flips the reverse.** Low returning → subscription (consumable), not “better email” as the first lever.

**One combo per lesson.** Never two. Ads own **CPM + CTR** only — if those are fine, the job is not Meta.

Trap answers to reject on sight:

- “Run more ads”
- “Spend more”
- “Need better creative” (when CTR is already fine)
- “ROAS is high so we’re winning” (when sales are flat)

## Facebook ads default curriculum

If the topic is Facebook / Meta / “how to run ads”, **this video is the course.** Read `concepts/Metric diagnosis tree.md` before each lesson. Order matches the video:

| # | Combo | Trap guess | Job | Watch |
|---|---|---|---|---|
| 1 | High CPM | Run more ads | Offer + compliance keywords (not page speed) | t=0:21 |
| 2 | Low CTR | More of the same images | Call-out + unique formats | t=2:55 |
| 3 | Good CTR + good CPM + low CVR | Creative / Meta | **Site.** First-load PDP (`concepts/Shopify CRO.md`) | t=4:12 |
| 4 | **Flat sales + high ROAS** | Spend more | Returning-customer fallacy. Exclude past buyers | **t=9:36** |
| 5 | Low returning | More email | Consumable: **subscription**. Apparel: 2nd–5th hero | t=10:25 |
| 6 | Low ROAS, rest fine | Ads | **AOV.** Floor $35 | t=13:22 |
| 7 | TTS request 0.1% | Better listing only | Test **5** invite agents | t=15:07 |
| 8 | ROAS dies after scale | Same 10 ads at 3x spend | 3x spend → 3x unique ads; testing campaign | t=30:09 |

**Learn metrics:** start at **#1** (high CPM) — that is how the video starts. Do not jump to #4 unless they have flat sales + high ROAS, or they already cleared CPM/CTR.

**Diagnose with no numbers:** then start at **#4 (t=9:36)**.

## Topic → file

Doctrine lives in `knowledge/`. Read the file, then teach one scenario. If they want a **plan/setup** not a lesson, stop and use the specialist (`andromeda-stack`, `run-facebook-ads`, …). To teardown a **named brand**, stop and use `break-down-brand`.

| Topic | Read |
|---|---|
| Facebook ads / stuck account / metrics | `concepts/Chase classroom.md` + `concepts/Metric diagnosis tree.md` |
| Campaign structure / scale | `concepts/4-campaign method.md` |
| Andromeda / Hub / Euka / matchback | `concepts/Andromeda stack.md` |
| What ads to make / 33% | `concepts/33 percent rule.md` |
| TikTok Shop / affiliates | `concepts/TikTok Shop army.md` |
| TikTok **ads** (paid, CTR/CPM, scenes) | `concepts/TikTok Shop army.md` — paid-ads subsection, not Shop request rate |
| Subscriptions / LTV | `concepts/Three levels of purchase.md` |
| Email / SMS / Klaviyo / cart flow | `concepts/Email and SMS.md` |
| CVR / PDP / drawer / first-load / site speed | `concepts/Shopify CRO.md` |
| Brands Chase named (learn the roster) | `brands/Brand atlas.md` |
| Break down **this** brand like Chase | **stop — skill `break-down-brand`** |
| Hims / quiz | `concepts/Hims diagnostic layer.md` |
| Positioning / villain | `concepts/Five levels of brands.md` + `concepts/Villain marketing.md` |
| AI ads / MCP | `concepts/AI creative stack.md` |
| A specific video | `sources/Source index.md` |

Same classroom on every topic: one scenario, guess, one job.

## Every lesson (mechanics)

1. Read the mapped file above. Ads path also reads `concepts/Metric diagnosis tree.md`. No graphify.
2. Open with the scenario. **Ask. Wait.** Do not reveal the job in the same message as the question.
3. After they guess, write `lessons/NNNN-<slug>.html`: symptom, what it is not, the job, before/after, **one** Watch URL with timestamp.
4. Learning record only if they can restate the job in their own words.

Do not paste the playbook. Do not write transcripts.

## Completion

They can name **the combo → the job** for the scenario you taught. Coverage is not learning.
