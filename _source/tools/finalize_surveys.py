# -*- coding: utf-8 -*-
"""One-day wording for the final survey payload written by the engine's surveys.py (it assumes several days).
No MAP test in this session (Aya, 24 Nov 2026), so there is no PRE or POST payload.
Reads _source/surveys/final.json, writes _source/surveys/ready/final.json. Logged in PLUGIN-FEEDBACK.md.
Changes: "workshop" wording, q_4/q_5 for the first two can-do items, and q_ai / q_safe (surveys.md section 9)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(SRC, "kit"))
import content as C
IN = os.path.join(SRC, "surveys"); OUT = os.path.join(IN, "ready"); os.makedirs(OUT, exist_ok=True)
L = lambda en, ar: {"en": en, "ar": ar}
FOLDER = C.SURVEY["folder"]
W = [("The program met my expectations as a learning experience.", "The workshop met my expectations as a learning experience.", "لبّى البرنامج توقعاتي كتجربة تعليمية.", "لبّت ورشة العمل توقعاتي كتجربة تعليمية."),
     ("I am satisfied with the program overall.", "I am satisfied with the workshop overall.", "أنا راضٍ عن البرنامج بشكل عام.", "أنا راضٍ عن ورشة العمل بشكل عام."),
     ("I will use what I learned, and the tools from the program, in my work.", "I will use what I learned, and the tools from the workshop, in my work.", "سأطبّق ما تعلّمته والأدوات التي حصلت عليها في البرنامج في عملي.", "سأطبّق ما تعلّمته والأدوات التي حصلت عليها في ورشة العمل في عملي."),
     ("The instructor delivered the program effectively, and the teaching style was clear and easy to follow.", "The instructor delivered the workshop effectively, and the teaching style was clear and easy to follow.", "قدّم المدرّب البرنامج بفعالية، وكان أسلوب التدريس واضحاً وسهل المتابعة.", "قدّم المدرّب ورشة العمل بفعالية، وكان أسلوب التدريس واضحاً وسهل المتابعة."),
     ("I would recommend this program to a colleague.", "I would recommend this workshop to a colleague.", "أنصح زملائي بهذا البرنامج.", "أنصح زملائي بورشة العمل هذه."),
     ("What would you change or add to make the program better?", "What would you change or add to make the workshop better?", "ما الذي تقترح تغييره أو إضافته لتحسين البرنامج؟", "ما الذي تقترح تغييره أو إضافته لتحسين ورشة العمل؟")]
def fix_final(p):
    qs = []
    for q in p["questions"]:
        for en0, en1, ar0, ar1 in W:
            if q["label"]["en"] == en0: q["label"] = L(en1, ar1)
        if q["id"] == "q_7": q["label"] = L("The instructor was knowledgeable, professional and available to help me.", "كان المدرّب متمكناً ومحترفاً ومتاحاً لمساعدتي.")
        if q["id"] == "q_pace": q["label"] = L("The length and pace of the workshop were right for me.", "كانت مدة ورشة العمل ووتيرتها مناسبة لي.")
        if q["id"] == "q_12": q["label"] = L("Which part of the workshop was most useful to you, and why?", "ما الجزء الأكثر فائدة لك في ورشة العمل، ولماذا؟")
        if q["id"] == "q_can1": q["id"] = "q_4"
        if q["id"] == "q_can2": q["id"] = "q_5"
        if q["id"] == "q_10":
            sc = q["scaleConfig"]
            qs.append({"id": "q_ai", "type": "scale", "label": L("I check Claude's numbers and sentences before I use them.", "أتحقق من أرقام Claude وعباراته قبل أن أستخدمها."), "required": True, "sectionId": "s_learn", "scaleConfig": sc})
            qs.append({"id": "q_safe", "type": "scale", "label": L("I know which data must never go into Claude.", "أعرف البيانات التي لا يجوز إدخالها إلى Claude أبداً."), "required": True, "sectionId": "s_learn", "scaleConfig": sc})
        qs.append(q)
    for i, q in enumerate(qs): q["order"] = i
    p["questions"] = qs
    p["description"] = (f"End-of-workshop satisfaction survey for the CODED Professionals client session \"{C.TITLE}\" for Al-Balagh Al-Mubeen Charity, one day ({C.DATES}, {C.HOURS}, {C.VENUE}). "
                        "Taken at the end of the session (12:50), about 5 minutes. There is no MAP test in this session. The same 6-point agreement scale as other CODED programs (1 = Strongly disagree ... 6 = Strongly agree). Bilingual EN/AR.")
    p["folderId"] = FOLDER
    return p

for name, fn in (("final", fix_final),):
    p = fn(json.load(open(os.path.join(IN, name + ".json"), encoding="utf-8")))
    t = json.dumps(p, ensure_ascii=False, indent=1)
    assert "—" not in t and "program" not in json.dumps([q["label"] for q in p["questions"]]).lower().replace("cowork", "") or name != "final", name
    assert "1 days" not in t and "Day 1 and at the end of Day 1" not in t, name
    open(os.path.join(OUT, name + ".json"), "w", encoding="utf-8").write(t)
    print(name, len(p["questions"]), "questions")
