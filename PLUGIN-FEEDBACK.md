# Feedback for the coded-workshop-builder plugin

Found while building a **one-day** workshop (Claude in Layers, 24 Nov 2026). None of these was fixed in the engine; each has a kit-side workaround.

1. **`wk.FORM_DAY` default on one day.** `{FIRST: ["pre"], LAST: ["post", "survey"]}` collapses to `{1: ["post", "survey"]}` when `FIRST == LAST`, so the pre-MAP slide disappears. Workaround: the kit sets `FORM_DAY = {1: ["pre", "post", "survey"]}`. Suggested fix: merge the lists when the first and last day are the same.
2. **"all 1 days".** `pages.topbar()` and `pages.both()` write "all 1 days" / "All 1 days" on page headers, the 404 page and the card pages when `NDAYS == 1`. Suggested fix: "the workshop" for one day.
3. **Survey payloads on one day.** `surveys.py` writes "at the start of Day 1 and at the end of Day 1", "1 days" in the descriptions and "The length and pace of the 1 days". It also leaves out `q_ai` and `q_safe`, names the first two can-do items `q_can1`/`q_can2` instead of `q_4`/`q_5`, has no "workshop" wording option, has no NUM entry above 10 ("12 questions" with no word), and omits the newest intro line "It is not graded: it shows us how much you learned in the program." Workaround: `_source/tools/finalize_surveys.py`.
4. **`MAP_LEDE` default** says "the same on Day 1 and Day 1" on one day. Workaround: the kit sets `MAP_LEDE`.
5. **Opener labels are fixed text.** `widgets.showcase()` hardcodes "Weak prompt", "Strong prompt", "Weak result", "Strong result" and the scorecard heads "Weak / Strong". A layers or setup comparison (not a prompting lesson) cannot rename them. Workaround: kit CSS. Suggested fix: optional `labels` in `SHOWCASE`.
6. **Task notes say "each pair".** `deck.task()` defaults the note to "Ask each pair what they found so far." even when the task is solo. Workaround: the kit passes its own note. Suggested fix: use the task's `solo` field.
