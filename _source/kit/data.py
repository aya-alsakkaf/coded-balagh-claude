# -*- coding: utf-8 -*-
"""Every fictional name, date and number for Claude in Layers (Misbah Charity Society).
Change numbers here only: slides, prompts, files, answer keys and backups all read this file."""
import random

ORG = "Misbah Charity Society"
SHORT = "Misbah"
ORG_AR = "جمعية المصباح الخيرية"
LINK = "misbah-charity.example/give"
FICTION = "Fictional training file. Misbah Charity Society and every name, number and organization in it are made up."

def kwd(x): return f"KWD {x:,.3f}"

# ------------------------------------------------------------------ people (first names and team only)
HESSA = "Hessa (Programs)"
NOURA = "Noura (Marketing)"
FAHAD = "Fahad (Accounts)"
BADER = "Bader (Media production)"
DANA = "Dana (Design)"

# ------------------------------------------------------------------ the winter campaign (report, brief, calculator)
CAMPAIGN = "Winter Warmth 2026"
PERIOD = "1 November to 31 December 2026"
FAMILIES = 1020
FAMILIES_WRONG = 1200                                  # planted in the post screenshot
DELIVERY_START = "Sunday 6 December"
DELIVERY_START_WRONG = "Thursday 3 December"           # planted in the post screenshot
DELIVERY_END = "Thursday 17 December"
CENTERS = ["Jahra community hall", "Farwaniya community hall", "Sabah Al-Salem community hall"]
VOLUNTEERS = 64
# delivery days per hall (working days, Sunday to Thursday) and families per hall
HALLS = [(CENTERS[0], "6 to 10 December", 340), (CENTERS[1], "6 to 10 December", 380), (CENTERS[2], "13 to 17 December", 300)]
assert sum(n for _c, _d, n in HALLS) == FAMILIES
BUDGET = 48000.0
# the kit for one family: (item, unit cost KWD, quantity per family)
KIT = [("Blanket", 4.750, 2), ("Heater", 13.500, 1), ("Food basket", 9.250, 1), ("Child's winter jacket", 6.500, 2)]
DELIVERY_COST = 1.250                                  # per family
PER_FAMILY = round(sum(c * q for _i, c, q in KIT) + DELIVERY_COST, 3)      # 46.500
CAMPAIGN_COST = round(PER_FAMILY * FAMILIES, 3)                             # 47,430.000
LEFT = round(BUDGET - CAMPAIGN_COST, 3)                                     # 570.000
# report pages (the page that holds each fact)
PAGE_FAMILIES, PAGE_DELIVERY, PAGE_KIT, PAGE_RULES = 1, 2, 3, 4
POST_ERRORS = [("Delivery start", f"Deliveries start {DELIVERY_START_WRONG}", f"Deliveries start {DELIVERY_START} (page {PAGE_DELIVERY})"),
               ("Families", f"{FAMILIES_WRONG:,} families", f"{FAMILIES:,} families (page {PAGE_FAMILIES})")]
PHOTO_RULE = "Never show a child's face. Never name a family."

# ------------------------------------------------------------------ donations, 1 to 24 November 2026 (month to date)
CAMPAIGNS = ["Winter Warmth", "Ramadan Iftar 2027", "Orphan Sponsorship", "Water Wells"]
CODES = {"Winter Warmth": "WW", "Ramadan Iftar 2027": "RI", "Orphan Sponsorship": "OS", "Water Wells": "WL"}
CHANNELS = ["KNET online", "Bank transfer", "Collection box", "Office cash desk"]
DON_LAST = 24                                          # month to date: 1 to 24 November
DUP_RECEIPT = "R-2026-11408"                           # planted: this receipt appears twice
DUP_AMOUNT = 2500.0
DUP_CAMPAIGN = "Winter Warmth"
THANKS = {"donor": "D-1043", "receipt": "R-2026-11487", "amount": 150.0, "campaign": "Winter Warmth"}   # the skill test case

def _donations():
    rnd = random.Random(2611)
    amounts = [5, 10, 10, 20, 20, 25, 25, 50, 50, 50, 75, 100, 100, 150, 200, 250, 500]
    wts = {"Winter Warmth": 46, "Ramadan Iftar 2027": 18, "Orphan Sponsorship": 22, "Water Wells": 14}
    rows = []
    n = 239
    for i in range(n):
        rec = f"R-2026-{11300 + i}"
        day = 1 + (i * DON_LAST) // n
        camp = rnd.choices(CAMPAIGNS, weights=[wts[c] for c in CAMPAIGNS])[0]
        ch = rnd.choices(CHANNELS, weights=[50, 22, 16, 12])[0]
        amt = float(rnd.choice(amounts))
        donor = f"D-{1001 + rnd.randrange(180)}"
        rows.append({"date": (2026, 11, day), "receipt": rec, "donor": donor, "channel": ch, "campaign": camp, "amount": amt})
    for r in rows:
        if r["receipt"] == DUP_RECEIPT: r.update(campaign=DUP_CAMPAIGN, channel="Bank transfer", amount=DUP_AMOUNT, donor="D-1077")
        if r["receipt"] == THANKS["receipt"]: r.update(campaign=THANKS["campaign"], channel="KNET online", amount=THANKS["amount"], donor=THANKS["donor"])
    return rows
DON_TRUE = _donations()                                # 239 unique receipts
_dup = next(r for r in DON_TRUE if r["receipt"] == DUP_RECEIPT)
_at = DON_TRUE.index(_dup)
DON_EXPORT = DON_TRUE[:_at + 1] + [dict(_dup)] + DON_TRUE[_at + 1:]      # 240 rows: the duplicate sits right after the original
DON_ROWS = len(DON_EXPORT)
DUP_SHEET_ROWS = (_at + 2, _at + 3)                    # Excel rows (header is row 1)
def _tot(rows, key):
    out = {}
    for r in rows: out[r[key]] = round(out.get(r[key], 0) + r["amount"], 3)
    return out
CONTROL = {c: _tot(DON_TRUE, "campaign").get(c, 0.0) for c in CAMPAIGNS}          # the Control totals sheet
EXPORT = {c: _tot(DON_EXPORT, "campaign").get(c, 0.0) for c in CAMPAIGNS}         # what code on the export gives
BY_CHANNEL = {c: _tot(DON_TRUE, "channel").get(c, 0.0) for c in CHANNELS}
BY_CHANNEL_EXPORT = {c: _tot(DON_EXPORT, "channel").get(c, 0.0) for c in CHANNELS}   # what a dashboard on the export shows
EXPORT_ROWS = {c: sum(1 for r in DON_EXPORT if r["campaign"] == c) for c in CAMPAIGNS}
TOTAL_CONTROL = round(sum(CONTROL.values()), 3)
TOTAL_EXPORT = round(sum(EXPORT.values()), 3)
DIFF = round(TOTAL_EXPORT - TOTAL_CONTROL, 3)          # 2,500.000
TOP_CAMPAIGN = max(CONTROL, key=CONTROL.get)
DUP_DAY = _dup["date"][2]                              # the day of the duplicated bank transfer (lab hint)
# one real past letter from the export (the example in the starter skill and in Demo 3.2): a Winter Warmth gift of KWD 100.000
EXAMPLE_GIFT = next(r for r in DON_TRUE if r["campaign"] == "Winter Warmth" and r["amount"] == 100.0 and r["receipt"] not in (DUP_RECEIPT, THANKS["receipt"]))

# ------------------------------------------------------------------ the inbox and calendar for Sunday 29 November (Demo 2.1, Task 2.1 fallback)
BRIEF_DAY = "Sunday 29 November 2026"
MEETINGS = [("09:00-09:45", "Weekly delivery check-in", "Hessa, Fahad, Bader", "The heater delay: 120 of 300 heaters arrive Tuesday 1 December"),
            ("11:00-11:30", "Call with Al-Rayyan Heaters Co.", "Salem (account manager), Hessa", "Confirm the new date in writing; ask for the rest of the order"),
            ("13:00-14:00", "Board update preparation", "General Manager, Fahad", "Donations to 24 November and the budget slide, due Monday 12:00")]
EMAILS = [  # (from, subject, received, gist, needs a reply)
    ("Salem, Al-Rayyan Heaters Co.", "Heater order WW-H-300: delivery change", "Wed 25 Nov, 16:10",
     "Only 120 of the 300 heaters can arrive on Tuesday 1 December. The other 180 arrive on Sunday 6 December, the first delivery day.", True),
    ("Maha, volunteer coordinator", "Volunteers for the delivery days", "Wed 25 Nov, 14:02",
     "64 volunteers confirmed. Jahra still needs 10 more drivers for 6 to 10 December.", True),
    ("Board secretary", "Board pack: donations and budget", "Wed 25 Nov, 11:45",
     "Please send the donations total to 24 November and one budget slide by Monday 30 November, 12:00.", True),
    ("Donor D-1043", "Receipt for my donation", "Tue 24 Nov, 20:31",
     f"Asks for a thank-you letter for receipt {THANKS['receipt']}: KWD 150.000 to Winter Warmth.", True),
    ("Sabah Al-Salem community hall", "Booking confirmed", "Tue 24 Nov, 10:15",
     "The hall is booked from 6 to 17 December, 08:00 to 13:00.", False),
    ("Photographer (freelance)", "Photos at the delivery days", "Mon 23 Nov, 18:40",
     "Asks if he can photograph families as they receive their kits.", True),
    ("Newsletter tool", "Your annual plan renews on 1 December", "Mon 23 Nov, 09:00",
     "The plan renews automatically for KWD 96.000.", False),
    ("Noura, Marketing", "Ramadan Iftar 2027: first planning meeting", "Sun 22 Nov, 13:20",
     "Proposes Wednesday 2 December, 10:00 for the first planning meeting.", False),
]
URGENT = EMAILS[0]

# ------------------------------------------------------------------ the receipts folder (Demo 4.1, Task 4.1): (no., supplier, what, qty, unit, campaign code or "")
RECEIPTS = [
    (1, "Sadu Textiles", "Blankets", 400, 4.750, "WW"),
    (2, "Al-Rayyan Heaters Co.", "Heaters", 180, 13.500, "WW"),
    (3, "Fresh Basket Foods", "Food baskets", 250, 9.250, "WW"),
    (4, "Little Coats Trading", "Children's winter jackets", 300, 6.500, "WW"),
    (5, "Swift Vans Rental", "Van rental, days", 6, 45.000, "WW"),
    (6, "Print Point", "Flyers", 2000, 0.035, "WW"),
    (7, "Sadu Textiles", "Blankets", 250, 4.750, "WW"),
    (8, "Al-Rayyan Heaters Co.", "Heaters", 120, 13.500, "WW"),
    (9, "Fresh Basket Foods", "Food baskets", 100, 9.250, ""),          # planted: no campaign code
    (10, "Bright Steps School Supplies", "School bags", 60, 7.250, "OS"),
    (11, "Aqua Drill Services", "Well site survey, deposit", 1, 1500.000, "WL"),
    (12, "Iftar Kitchen Co.", "Menu tasting, deposit", 1, 150.000, "RI"),
    (13, "Swift Vans Rental", "Van rental, days", 4, 45.000, "WW"),
    (14, "Print Point", "Roll-up banners", 3, 22.500, "WW"),
]
DUP_RECEIPT_NO = 4                                    # planted: receipt 04 is in the folder twice
NO_CODE_NO = 9
def rc_no(n): return f"MS-RC-{1100 + n}"
def rc_file(n, copy=False): return f"misbah-receipt-{n:02d}{'-copy' if copy else ''}.pdf"
def rc_amount(r): return round(r[3] * r[4], 3)
RC_DATES = {n: f"{1 + (n * 2) % 24:02d}/11/2026" for n in range(1, 15)}
RC_TOTAL = {code: round(sum(rc_amount(r) for r in RECEIPTS if r[5] == code), 3) for code in ("WW", "RI", "OS", "WL")}
RC_NOCODE = rc_amount(RECEIPTS[NO_CODE_NO - 1])
RC_DUP = rc_amount(RECEIPTS[DUP_RECEIPT_NO - 1])
RC_ALL = round(sum(rc_amount(r) for r in RECEIPTS), 3)
CODE_NAME = {v: k for k, v in CODES.items()}

# ------------------------------------------------------------------ the brand guide (Project knowledge)
VOICE = ["Warm, respectful and clear. Short sentences.", "Say \"families\" and \"neighbors\", never \"the poor\" or \"the needy\".",
         "Thank donors for what their gift did, not for the amount alone.", "English first, then Arabic, in every post."]
BRAND_RULES = [PHOTO_RULE, f"Every post ends with the donation link: {LINK}.", "Use one number per post, and check it against the campaign report.",
               "Hashtags: #MisbahWinter and #دفء_المصباح."]
COLORS = [("Lamp teal", "#0F6E6E"), ("Warm sand", "#E9D8B4"), ("Night blue", "#1B2A41")]
