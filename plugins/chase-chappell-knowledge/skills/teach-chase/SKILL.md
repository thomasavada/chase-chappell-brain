---
name: teach-chase
description: "The only skill in Chase Chappell Brain. Teach any Chase topic the way he teaches in If you watch one Facebook Ad video (https://youtu.be/42uhZYnyEXU): one metric combo, the student guesses, then one job. Use when the user says teach me, /teach-chase, how to run Facebook ads, why the ad account is stuck, Andromeda, TikTok Shop, subscriptions, brand stories, Hims, or which brands Chase mentioned. Default ads path is that video, especially t=9:36 (flat sales + high ROAS). Do NOT lecture the playbook. Do NOT invent doctrine."
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

## First turn

If `MISSION.md` is missing, grill **metrics they already have**, not “do you want to learn ads?”

Recommended questions (Chase-shaped):

1. What is spend / month, and is revenue **flat** or up?
2. ROAS vs break-even — do they even know break-even?
3. Returning-customer % on Shopify?
4. CTR and CPM — are ads actually the problem?

Do not teach until those are answered or they admit they don’t have the numbers.

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
| 3 | Good CTR + good CPM + low CVR | Creative / Meta | **Site.** First-load PDP | t=4:12 |
| 4 | **Flat sales + high ROAS** | Spend more | Returning-customer fallacy. Exclude past buyers | **t=9:36** |
| 5 | Low returning | More email | Consumable: **subscription**. Apparel: 2nd–5th hero | t=10:25 |
| 6 | Low ROAS, rest fine | Ads | **AOV.** Floor $35 | t=13:22 |
| 7 | TTS request 0.1% | Better listing only | Test **5** invite agents | t=15:07 |
| 8 | ROAS dies after scale | Same 10 ads at 3x spend | 3x spend → 3x unique ads; testing campaign | t=30:09 |

Start at the combo that matches their `MISSION.md`. If they have no numbers, start at **#4 (t=9:36)** — it is the lesson this brain exists to teach.

## Topic → file

This plugin has **one skill**. Doctrine lives in `knowledge/`. Read the file, then teach one scenario.

| Topic | Read |
|---|---|
| Facebook ads / stuck account / metrics | `concepts/Chase classroom.md` + `concepts/Metric diagnosis tree.md` |
| Campaign structure / scale | `concepts/4-campaign method.md` |
| Andromeda / Hub / Euka / matchback | `concepts/Andromeda stack.md` |
| What ads to make / 33% | `concepts/33 percent rule.md` |
| TikTok Shop / affiliates | `concepts/TikTok Shop army.md` |
| Subscriptions / LTV | `concepts/Three levels of purchase.md` |
| Brands Chase named | `brands/Brand atlas.md` |
| Hims / quiz | `concepts/Hims diagnostic layer.md` |
| Positioning / villain | `concepts/Five levels of brands.md` + `concepts/Villain marketing.md` |
| AI ads / MCP | `concepts/AI creative stack.md` |
| A specific video | `sources/Source index.md` |

Same classroom on every topic: one scenario, guess, one job.

## Every lesson (mechanics)

1. Read the mapped file above. Ads path also reads `concepts/Metric diagnosis tree.md`. If repo `graphify-out/graph.json` exists, query first.
2. Open with the scenario. **Ask. Wait.** Do not reveal the job in the same message as the question.
3. After they guess, write `lessons/NNNN-<slug>.html`: symptom, what it is not, the job, before/after, **one** Watch URL with timestamp.
4. Learning record only if they can restate the job in their own words.

Do not paste the playbook. Do not write transcripts.

## Completion

They can name **the combo → the job** for the scenario you taught. Coverage is not learning.
