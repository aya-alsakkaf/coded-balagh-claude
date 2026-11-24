# CLAUDE.md · Claude in Layers (CODED × Al-Balagh Al-Mubeen)

One-day client session, Thursday 26 November 2026, 09:00-13:00, Legacy room, CODED campus. Trainer: Aya.
Built with the CODED workshop builder on its engine. The approved handoff is `_source/HANDOFF.md`; the outline is `_source/OUTLINE.md`.

## How this repo works

- `_source/build/` is the engine. **Never edit it.** `_source/kit/` is this workshop's kit: edit only the kit, then rebuild.
- Build and check: `bash _source/build/build.sh` (must end with `PROBLEMS: 0`). `public/` is generated: never hand-edit it.
- Survey payloads: `python3 _source/tools/finalize_surveys.py` writes the one-day wording into `_source/surveys/ready/`.
- Class plan: `python3 _source/tools/class_plan.py` regenerates `CLASS-PLAN.md`.
- A push to `main` deploys production on Vercel (project `coded-balagh-claude`).

## Rules

- The site carries the kit word for word. Change wording in the kit, never in `public/`.
- Plain English for Gulf ESL readers, American spelling, no em dashes, KWD for money. English only on the site and decks; only the portal surveys are bilingual.
- Fictional data only: Misbah Charity Society. **Never put Al-Balagh Al-Mubeen's name on fake data.**
- Participant pages give hints, never answers. Answers live in `/staff`, `_source/` and the portal descriptions.
- The whole site is noindex. `/staff` is locked by `middleware.js` with `STAFF_PASSWORD` (set in Vercel; never in the repo or in Slack).
- Sample file names never change once published.
- No prompting lesson: this client left AI Essentials over too much prompting.

## Decisions

1. **Approval (24 Nov 2026):** Aya approved the handoff with "Approve, ship when checks pass". This also confirmed creating and updating the three portal survey drafts.
2. **Accounts:** attendees use their own paid Claude plan (Pro, Max or Team) with the Claude desktop app (approval answer).
3. **Email:** Gmail and Google Calendar connectors (approval answer).
4. **Theme:** CODED theme for now; Aya will send Al-Balagh's logo. When it arrives: add it to `_source/kit/`, set `CLIENT = {"name": "Al-Balagh Al-Mubeen Charity", "short": "Al-Balagh", "primary": <logo color>, "logo": <file>}`, rebuild, check contrast, push.
5. **Scope:** Yousif's Slack message (24 Nov) is the outline; Ali Taqi's four layers are the order. Claude Code gets one line in the close only.
6. **Product facts** checked on the Claude Help Center on 24 Nov 2026: Customize renamed Plugins (general 9 Nov); one Plugins page for skills, connectors and plugins; skills on all plans (need "Create and edit files"); plugins, Cowork and scheduled tasks on paid plans; the new Claude experience merges chat and Cowork; Gmail send, reply and forward ask first outside Auto mode; Google Calendar can create events; artifacts start private; Cowork modes Manual, Auto, Skip. Slides give the new menu name first and the older name in brackets.
7. **Timing:** coffee break 10:15-10:25; Dhuhr break 11:40-11:55 (Dhuhr about 11:36 in Kuwait City on 26 Nov), never inside a task.
8. **MAP:** one day, PRE at 09:05 and POST at 12:40, 12 questions, no Part 3. Key: 1 a · 2 c · 3 b · 4 d · 5 c · 6 b · 7 a · 8 a · 9 d · 10 b · 11 d · 12 c.
9. **Final survey:** full form, client version (q_dept, no NPS), "workshop" wording, with q_ai and q_safe.
10. **Cohort:** none exists in the portal for this session; the surveys are not linked to one.
11. **Portal:** folder "Claude in Layers · Al-Balagh Al-Mubeen (Nov 26)" (9d0ed253-6ffa-4591-aa6b-3c95f22972ec). PRE 6bc37002-4c02-4aa4-9c79-64be5b9213ee, POST 2c1bce62-400a-45aa-b391-05ec7d7b232a, final 402362fa-61c5-43f2-9eb2-3b15ff667498. The intro screen, closing screen and colors stay the portal default, the same as the model surveys.
12. **Engine on one day:** `FORM_DAY = {1: ["pre", "post", "survey"]}`; the hub and page headers say "all 1 days" (engine wording, logged in PLUGIN-FEEDBACK.md); the survey wording is fixed in `_source/tools/finalize_surveys.py`.
13. **Kit additions:** the live calculator on slide 18 is kit HTML, CSS and JS (`build_deck.py`: `CALC_HTML`, `EXTRA_CSS`, `EXTRA_JS`).
14. **Slack:** the team message goes in the thread of Yousif's outline.
15. **Opener labels:** the engine's opener names its windows "Weak prompt / Strong prompt". This client left over prompting, so the kit relabels them "Plain chat / In the Project" with CSS in `build_deck.py` (`EXTRA_CSS`). Logged in PLUGIN-FEEDBACK.md #5.
16. **Task 2.1 accounts:** only an account Al-Balagh approved for Claude connects Gmail; everyone else uses `misbah-inbox-and-calendar.pdf`. Yousif confirms the approved accounts before Thursday.
17. **QA round 1 (6.9/10, fail)** led to the changes listed at the end of `_source/HANDOFF.md`. The portal drafts were updated under decision 1.
