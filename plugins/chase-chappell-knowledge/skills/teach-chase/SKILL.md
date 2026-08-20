---
name: teach-chase
description: "Teach a Chase Chappell topic over multiple sessions using this repo as a stateful classroom. Use when the user says teach me, /teach-chase, I want to learn Facebook ads, Andromeda, TikTok Shop, subscriptions, or brand stories. Ground every lesson in knowledge/ plus YouTube. Do NOT invent doctrine from training data."
disable-model-invocation: true
argument-hint: "What would you like to learn?"
---

# Teach Chase

Adapted from [Matt Pocock `/teach`](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md). Knowledge source is **this plugin**, not the web.

## Workspace

Treat **cwd** as the student workspace. Prefer `./learners/` if this repo was cloned (that folder is gitignored). Files:

- `MISSION.md` — why they want this. Format: [MISSION-FORMAT.md](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/teach/MISSION-FORMAT.md)
- `RESOURCES.md` — start from `${CLAUDE_PLUGIN_ROOT}/knowledge/sources/Source index.md` and the matching concept note. Add Watch URLs only.
- `learning-records/*.md` — `0001-slug.md` when they *demonstrate* understanding
- `lessons/*.html` — one short self-contained lesson per session
- `NOTES.md` — how they like to be taught

## First turn

If `MISSION.md` is missing or vague, **grill the mission** (Matt grilling: numbered questions + your recommended answer, wait). Do not teach yet.

Concrete over abstract: "I spend $5K/mo on Meta and ROAS dies when I scale" beats "learn Facebook ads."

## Every lesson

1. If repo `graphify-out/graph.json` exists, `graphify query` the topic, then Read the cited knowledge files.
2. Otherwise Read the file in `chase-chappell-brain` quick-lookup.
3. Reach for the matching model-invoked skill (`diagnose-ad-account`, `run-facebook-ads`, …).
4. Teach **one** tightly scoped thing in their zone of proximal development (from `learning-records`).
5. Write `lessons/NNNN-slug.html` — short, Tufte-plain, one win. Cite **one primary YouTube**. Equal-length quiz answers.
6. Link the knowledge note. Remind them to ask follow-ups.

Do not paste the whole playbook. Do not write transcripts.

## Knowledge / skills / wisdom

- Knowledge: `knowledge/` + the Watch URL on the source card
- Skills: interactive quiz or a real-world checklist (break-even ROAS, 4-campaign, 33% grid)
- Wisdom: send them to the video comments / brand Ads Library, not to invented communities

## Completion of a session

User can do the one job the lesson named. A learning record exists only if they showed they got it — coverage is not learning.
