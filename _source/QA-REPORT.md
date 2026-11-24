# QA report · Claude in Layers (balagh-claude)

## Round 1 · 6.9 / 10 · FAIL (Content coherence 1.0, Tasks and demos 4.0, MAP tests 6.5, Language 8.0, Decks 9.0)

Levels 1 to 4: run by the builder with `validate_site.py` (PROBLEMS: 0), `qa.cjs pages` (0), `qa.cjs decks` (0), a presenter walk of the deck
(every player, the opener and the next-word widget step to the end and fit 1440 × 810), the card sort, and each QR code decoded on its own.
Levels 5 to 8: run by a fresh agent that did not see the build.

| Dimension | Score |
|---|---|
| Files, links and config | 10.0 |
| Pages | 9.75 |
| Decks | 9.0 |
| Interactivity | 10.0 |
| Content coherence | 1.0 |
| Tasks and demos | 4.0 |
| MAP tests | 6.5 |
| Final survey | 9.75 |
| Language and data safety | 8.0 |

### Findings

Pages
- Nit · every page header and pill · "all 1 days" (engine wording on one day) · no kit hook; logged in PLUGIN-FEEDBACK.md #2

Decks
- Concerning · slide 4 `o_ws` · the opener labels read "Weak prompt / Strong prompt / Weak result / Strong result": a prompting frame on a layers comparison, against decision 5 · relabel "Plain chat / Layers on" from the kit

Content coherence
- Concerning · `o_ws` scorecard · "Follows the brand guide? Yes", but the layered post is English only, has two numbers and no Arabic hashtag · rewrite the post and the d10 backup
- Concerning · staff backup Demo 1.3 · "By channel (Control totals)" uses de-duplicated figures under an export-as-is table · compute from the export and label it
- Concerning · outline 1.3f "document" · no demo or task option · add option E to Task 1.3
- Concerning · lesson plan 11:12 "Memory" · 3 minutes with no slide, note or check · add a memory slide with a check
- Concerning · `l4plug` · "44 skills" for Small business · verify and fix or drop the count
- Concerning · Task 3.2 and `skfind` · "+ › Create skill" path · verify and use the Help Center path
- Concerning · `ablist` note · sharing options per plan out of date · verify and replace
- Nit · Layer 4 · no quick check on Cowork · cover Cowork in `l4chk`
- Nit · `l4plug` note · plugins and connectors · verify wording
- Nit · `l4sched` · "your laptop can be off" vs local-folder tasks · add the condition
- Nit · slide 5 · outcome 4 differs from OUTCOMES · align
- Nit · `l4story` vs inbox · board deadline differs · one deadline
- Nit · misbah-inbox-and-calendar.pdf · export time after the session · move to 25 Nov
- Nit · task notes · "Ask each pair" on solo tasks · "each person"
- Nit · `l3pp` · "64 volunteers in Jahra" · 64 is all halls

Tasks and demos
- Concerning · Task 4.2 · role cards only on staff pages · put them on the prompt sheet and the slide
- Concerning · Demo 3.2 · "one good letter" is never given · put the letter in the prompt
- Concerning · Demo 1.0 · "social post skill" and Drive delivery plan do not exist · use layers that exist, add to pre-flight
- Concerning · backup Task 3.1 captions · English only, three numbers · rewrite
- Concerning · Task 1.1 · web search demonstrated but never practiced · add it to the task
- Nit · key Task 1.1 · accept pages 1 to 3, the one-number rule
- Nit · backup Task 1.3 · Choice A source is the brief · fix
- Nit · Demo 4.1 hint · 16 files with README · fix
- Nit · lab step 3 hint · does not narrow · fix

MAP tests
- Concerning · Q1 to Q12 · keyed answer longest by characters in 8 of 12 · balance to 3 or fewer
- Concerning · Q6 · options copied from the sort cards, recall stem · rewrite as a work moment
- Nit · Q4, Q7 · distractors copy quick-check options · new distractors
- Nit · Q9 · recall · work moment
- Nit · Q10 · "14 receipt files" · 15
- Nit · Q8 d · not believable · replace
- Nit · ready payloads · brandingTitle without the colon · match the portal

Final survey
- Nit · q_7 · "instructor and facilitators" · one instructor

Language and data safety
- Concerning · Task 2.1 · connects a real work inbox with no approval gate · approved account or the fictional PDF
- Nit · `l4term`, Demo 4.1 setup · "just" · remove
- Nit · Task 4.2 step 2 · unclear Project name · fix

## Round 2 · 8.4 / 10 · FAIL (Content coherence 4.25, Tasks and demos 7.75, Language 8.5)

| Dimension | Score |
|---|---|
| Files, links and config | 10.0 |
| Pages | 9.75 |
| Decks | 10.0 |
| Interactivity | 10.0 |
| Content coherence | 4.25 |
| Tasks and demos | 7.75 |
| MAP tests | 9.75 |
| Final survey | 10.0 |
| Language and data safety | 8.5 |

Levels 1 to 4 re-run after the round 1 fixes: validator 0, pages 0, decks 0, presenter walk clean (opener relabeled, 63 slides fit).
Levels 5 to 8 by a second fresh agent. Findings (all fixed in the kit, see the end of HANDOFF.md):
- Concerning · Task 1.1, Demo 1.1, cheat sheet · "+ menu: Web search" (new experience has no toggle) · both layouts
- Concerning · `l4sched`, cheat sheet, extras · "/schedule" not documented · Scheduled › New task, or a chat
- Concerning · Task 3.2, `skfind`, cheat sheet · "Plugins page › Skills" tab does not exist · both layouts, live upload, runbook check
- Concerning · Task 4.2 · no participant adds a plugin · plugin step and key
- Concerning · Task 4.2 accountant · .zip cannot be added to a chat or Project · Task 4.1 table
- Concerning · take-home guide, `w1` · Gmail without the approved-account condition · added
- Nits · `l4plug` Discover tab · block line without "doc" · outcome 4 wording · board date · "week's receipts" · memory check key · no schedule check · Task 1.1 key (hashtag ending) · Task 4.2 key (receipts 04 and 09) · Demo 3.2 upload path · Demo 4.1 flags on the public slide · Task 1.1 fallback · MAP Q5 repeats the quick check · "all 1 days" (engine) · skill .zip without the fiction line

## Round 3 · 9.3 / 10 · FAIL (Content coherence 8.25, Tasks and demos 8.0)

| Dimension | Score |
|---|---|
| Files, links and config | 10.0 |
| Pages | 9.75 |
| Decks | 10.0 |
| Interactivity | 10.0 |
| Content coherence | 8.25 |
| Tasks and demos | 8.0 |
| MAP tests | 9.5 |
| Final survey | 10.0 |
| Language and data safety | 9.5 |

Levels 1 to 4 after the round 2 fixes: validator 0, pages 0, decks 0, walk clean (64 slides). Levels 5 to 8 by a third fresh agent:
- Concerning · `l4schk`, `l4sched` note · "cannot open a folder on a laptop" (a laptop folder works while the laptop is awake) · stem now says laptop closed; note corrected
- Concerning · runbook, Demo 3.2, `skfind` · donor-thank-you would already exist on the presenting laptop · delete the test upload, do not save in Demo 3.2, upload once live
- Nits fixed · plugin quick check added (`l4pchk`) · skill sharing per plan · "one hands-on task each" · Demo 1.2 shown as kit HTML plus a real artifact · Task 4.2 extra uses each role's shift · Task 4.1 extra puts the folder on Drive first · Team owner settings in the joining note · 35-word sentence split
- Nits accepted · MAP Q4 and Q7 stems echo two quick checks (new options; a third portal rewrite not worth the risk two days out) · "all 1 days" (engine, PLUGIN-FEEDBACK #2)

## Round 4 · 9.5 / 10 · FAIL (Language and data safety 8.5)

| Dimension | Score |
|---|---|
| Files, links and config | 10.0 |
| Pages | 10.0 (the engine Nit is counted under Language) |
| Decks | 10.0 |
| Interactivity | 10.0 |
| Content coherence | 9.25 |
| Tasks and demos | 9.25 |
| MAP tests | 9.25 |
| Final survey | 10.0 |
| Language and data safety | 8.5 |

Levels 1 to 4 after the round 3 fixes: validator 0, pages 0, decks 0, walk clean (65 slides). Levels 5 to 8 by a fourth fresh agent; all product facts and every sample-file number verified.
- Concerning · prompt sheet Demo 2.1 card · Gmail connect steps with no approved-account condition, before the sort · card is watch-only (trainer account)
- Nits fixed · `l2chk` stem · files concept check (`l1fchk`) · report hall days · job descriptions end with the approval rule · Demo 3.2 "do not save" · Task 2.1 Manual mode · MAP Q4, Q5, Q7 · Task 4.1 extra approved account
- Nit accepted · "all 1 days" (engine, PLUGIN-FEEDBACK #2)

## Round 5 · about 9.45 / 10 · FAIL (Content coherence 8.25)

The last allowed round. No Blocking finding; every other dimension at 9.0 or more. Levels 1 to 4 after the round 4 fixes: validator 0, pages 0, decks 0, walk clean (66 slides). Levels 5 to 8 by a fifth fresh agent.
- Concerning · `l4plug` note · said a plugin connects its connectors for you; the plugin docs say each bundled connector still has to be connected · note now says: open the plugin's Connectors tab and connect each one with your own account
- Nits fixed · `l1fchk` echoed MAP Q2 and voice mode had no check: now a voice check, plus a 30-second voice demo in the `l1files` note · `w1` label "Between you, you caught" · `aeshow` timing for more than three people · `aetable` Designer shift is now a schedule (Wednesday 09:00) · Task 3.1 and Task 4.2 steps point to the prompt sheet, not "below" · day-before skill upload and inbox loading moved from the preflight list to Facilitator "Before the session" · receipt PDF unit prices with thousands separators · MAP Q4 money with three decimals (both portal drafts updated) · Task 2.1 and Demo 3.2 hints shortened
- Nit accepted · "all 1 days" (engine, PLUGIN-FEEDBACK #2)

After the fixes: validator 0 (Task 3.1 steps shortened to fit 1440 × 810), pages 0, decks 0. Not re-audited: by the QA rule, round 5 was the last round, so the build is not shipped without Aya's decision.
