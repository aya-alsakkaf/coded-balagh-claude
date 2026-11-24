# CLAUDE.md · Claude in Layers (CODED × Al-Balagh Al-Mubeen)

One-day client session, Thursday 26 November 2026, 09:00-13:00, Legacy room, CODED campus. Trainer: Aya.
Built with the CODED workshop builder on its engine. The approved handoff is `_source/HANDOFF.md`; the outline is `_source/OUTLINE.md`.

## How this repo works

- `_source/build/` is the engine. **Never edit it** (one logged exception: decision 18). `_source/kit/` is this workshop's kit: edit only the kit, then rebuild.
- Build and check: `bash _source/build/build.sh` (must end with `PROBLEMS: 0`). `public/` is generated: never hand-edit it.
- Survey payload: `python3 _source/tools/finalize_surveys.py` writes the one-day wording of the final survey into `_source/surveys/ready/final.json`.
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
8. **MAP:** none. Aya removed the MAP test on 24 Nov 2026 ("No need for a map test. Omit it"). The kit sets `MAP = []`; the PRE and POST portal drafts were deleted with her confirmation. The 10-minute slots went to a setup check (09:00-09:10), Task 1.1 (15 min), Task 4.2 (20 min) and show and tell (7 min).
9. **Final survey:** full form, client version (q_dept, no NPS), "workshop" wording, with q_ai and q_safe.
10. **Cohort:** none exists in the portal for this session; the surveys are not linked to one.
11. **Portal:** folder "Claude in Layers · Al-Balagh Al-Mubeen (Nov 26)" (9d0ed253-6ffa-4591-aa6b-3c95f22972ec). Final survey 402362fa-61c5-43f2-9eb2-3b15ff667498 (the only survey). The intro screen, closing screen and colors stay the portal default, the same as the model surveys.
12. **Engine on one day:** `FORM_DAY = {1: ["survey"]}`; the hub and page headers say "all 1 days" (engine wording, logged in PLUGIN-FEEDBACK.md); the final survey wording is fixed in `_source/tools/finalize_surveys.py`.
13. **Kit additions:** the live calculator on slide 19 (`abcalc`) is kit HTML, CSS and JS (`build_deck.py`: `CALC_HTML`, `EXTRA_CSS`, `EXTRA_JS`).
14. **Slack:** the team message goes in the thread of Yousif's outline.
15. **Opener labels:** the engine's opener names its windows "Weak prompt / Strong prompt". This client left over prompting, so the kit relabels them "Plain chat / In the Project" with CSS in `build_deck.py` (`EXTRA_CSS`). Logged in PLUGIN-FEEDBACK.md #5.
16. **Task 2.1 accounts:** only an account Al-Balagh approved for Claude connects Gmail; everyone else uses `misbah-inbox-and-calendar.pdf`. Yousif confirms the approved accounts before Thursday.
17. **QA round 1 (6.9/10, fail)** led to the changes listed at the end of `_source/HANDOFF.md`. The portal drafts were updated under decision 1.
18. **Engine change (24 Nov 2026, approved by Aya):** the engine had no way to leave out the MAP test. Aya chose a small engine change: `wk.HAS_MAP` (false when `MAP = []`) makes the hub survey heading, the staff index, lesson plan, facilitator kit and answer keys, `surveys.py` and `validate_site.py` skip the MAP. Hub hooks `map_eyebrow` and `map_title` added. Nothing else in the engine changed. Logged in PLUGIN-FEEDBACK.md #7.
19. **Survey slide:** the closing QR slide is kit HTML (`SURVEY_LEAD` and `#c6survey` CSS in `build_deck.py`), built on the engine's `timer_slide`.
