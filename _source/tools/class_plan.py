# -*- coding: utf-8 -*-
"""Writes CLASS-PLAN.md at the repo root from the kit: the day, blocks, minutes, demos and tasks."""
import os, sys
SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(SRC, "kit"))
import content as C, content_demos as CD
def mins(span):
    a, z = span.split("-"); return (int(z[:2]) * 60 + int(z[3:])) - (int(a[:2]) * 60 + int(a[3:]))
out = [f"# Class plan · {C.TITLE}", "", f"{C.BRAND} · {C.DATES} · {C.HOURS} · {C.VENUE}", "", "Generated from the kit by `_source/tools/class_plan.py`. Do not edit by hand.", ""]
for d, D in C.DAYS.items():
    out += [f"## Day {d} · {D['title']}", "", f"**Claim:** {D['claim']}", "", f"**Integration moment:** {D['artifact']}", "", "| Time | Min | Block | Inside |", "|---|---|---|---|"]
    tot = 0
    for t, n, w in D["blocks"]:
        m = mins(t); tot += m; out.append(f"| {t} | {m} | {n} | {w or 'break'} |")
    out += [f"| | **{tot}** | **Total** | |", "", "### Demos and tasks", "", "| Card | Title | Minutes | Solo or pairs | Files | Deliverable | Finished early? |", "|---|---|---|---|---|---|---|"]
    for k, v in CD.DEMOS.items():
        if v["day"] != d: continue
        h = v.get("hands_on")
        out.append(f"| {v['card']} | {v['title']} | {v.get('minutes', '') if h else 'demo'} | {v.get('solo', '') if h else ''} | {', '.join(v.get('files', [])) or 'none'} | {v.get('deliverable', '') if h else ''} | {' '.join(v.get('stretch', [])) if h else ''} |")
    out += ["", f"Hands-on minutes: {sum(v['minutes'] for v in CD.DEMOS.values() if v.get('hands_on') and v['day'] == d)}. No points: a one-day session.", ""]
out += ["## Survey", "", "- No MAP test in this session (Aya's decision, 24 Nov 2026).",
        f"- Final survey: {C.FORMS['survey']['when']} · {C.FORMS['survey']['url']}", ""]
open(os.path.join(os.path.dirname(SRC), "CLASS-PLAN.md"), "w", encoding="utf-8").write("\n".join(out))
print("CLASS-PLAN.md written")
