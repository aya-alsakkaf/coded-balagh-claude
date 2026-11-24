# Claude in Layers · CODED × Al-Balagh Al-Mubeen

The workshop site for a one-day, hands-on Claude session: **Thursday 26 November 2026, 09:00-13:00, Legacy room, CODED campus**.
Four layers of Claude (chat and artifacts, connectors, memory, Projects and Skills, Cowork, plugins and schedules), ending with one AI employee per participant.
Fictional practice organization: Misbah Charity Society.

Live: https://coded-balagh-claude.vercel.app

## Pages

| Address | Page | Who |
|---|---|---|
| `/` → `/coded-balagh-claude` | Workshop home | Everyone |
| `/day1` → `/coded-balagh-claude-day-1` | The day: run of show, files, survey QR code | Everyone |
| `/slides1` → `/coded-balagh-claude-day-1-deck` | The deck (66 slides, no notes) | Everyone |
| `/coded-balagh-claude-prompt-sheet-day-1` | Every prompt, with COPY | Everyone |
| `/coded-balagh-claude-lab-day-1` | Browser lab: check the dashboard | Everyone |
| `/coded-balagh-claude-cheat-sheet`, `-safe-use-card`, `-take-home-guide` | Take-aways | Everyone |
| `/survey` | Short link to the final survey in the portal | Everyone |
| `/staff` | Lesson plan, deck with notes, facilitator kit, runbook, backups, answer key, lab key | Password |

## Build and deploy

```
bash _source/build/build.sh          # sample files, deck, pages, staff pages, config, survey payloads, validator (PROBLEMS: 0)
python3 _source/tools/finalize_surveys.py
python3 _source/tools/class_plan.py
git push                             # main deploys production on Vercel
```

The staff pages need `STAFF_PASSWORD` in Vercel → Project → Settings → Environment Variables (Production), then a redeploy.

## Survey (CODED portal)

No MAP test in this session (Aya's decision, 24 Nov 2026).

- Final survey (12:50): https://platform.joincoded.com/sv/coded-al-balagh-al-mubeen-claude-in-layers-final-satisfaction-survey

See `CLAUDE.md` for the rules and decisions, `CLASS-PLAN.md` for the plan, `CHANGELOG.md` for changes.
