# -*- coding: utf-8 -*-
"""The 8 fictional sample files for Claude in Layers (Misbah Charity Society).
    python3 gen_files.py OUTDIR        (the kit keeps them in ../files; the site copies them unchanged)
Names never change once built: participants download them."""
import sys, os, io, zipfile, datetime as dt
import openpyxl
from openpyxl.styles import Font, PatternFill
from docx import Document
from docx.shared import Pt
import data as D
from data import kwd
from content_demos import FILE_REPORT, FILE_DON, FILE_POST, FILE_BRIEF, FILE_BRAND, FILE_INBOX, FILE_SKILL, FILE_RECEIPTS, SKILL_STEPS

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "files")
os.makedirs(OUT, exist_ok=True)
FIXED = dt.datetime(2026, 11, 24, 9, 0, 0)

from reportlab.lib.pagesizes import A4, A5
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
SS = getSampleStyleSheet()
NAVY = colors.HexColor("#1B2A41"); TEAL = colors.HexColor("#0F6E6E")
H = ParagraphStyle("H", parent=SS["Heading2"], fontName="Helvetica-Bold", fontSize=13, spaceAfter=8, textColor=NAVY)
B = ParagraphStyle("B", parent=SS["BodyText"], fontName="Helvetica", fontSize=10.5, leading=15, spaceAfter=7)
T = ParagraphStyle("T", parent=SS["Title"], fontName="Helvetica-Bold", fontSize=18, textColor=NAVY)
def grid(rows, widths, head=True):
    st = [("FONT", (0, 0), (-1, -1), "Helvetica", 9.5), ("GRID", (0, 0), (-1, -1), 0.5, colors.grey), ("VALIGN", (0, 0), (-1, -1), "TOP")]
    if head: st += [("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 9.5), ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E3F0EF"))]
    return Table(rows, colWidths=[w * mm for w in widths], style=TableStyle(st))

def pdf(path, title, pages, header):
    story = []
    for i, p in enumerate(pages):
        story += p
        if i < len(pages) - 1: story.append(PageBreak())
    n = len(pages)
    def deco(c, d):
        c.saveState(); c.setFont("Helvetica", 8.5); c.setFillColor(colors.HexColor("#555555"))
        c.drawString(20 * mm, 287 * mm, header); c.drawRightString(190 * mm, 287 * mm, f"Page {d.page} of {n}")
        c.drawString(20 * mm, 12 * mm, D.FICTION); c.restoreState()
    SimpleDocTemplate(path, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm, topMargin=22 * mm, bottomMargin=20 * mm,
                      title=title, author="CODED", subject="Fictional training file", creator="CODED", invariant=1).build(story, onFirstPage=deco, onLaterPages=deco)

def doc(name, title, blocks):
    d = Document()
    st = d.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(11)
    d.add_heading(title, 1)
    for kind, val in blocks:
        if kind == "p": d.add_paragraph(val)
        elif kind == "b": d.add_paragraph(val, style="List Bullet")
        elif kind == "n": d.add_paragraph(val, style="List Number")
        elif kind == "h": d.add_heading(val, 2)
        elif kind == "t":
            t = d.add_table(rows=0, cols=len(val[0])); t.style = "Table Grid"
            for r in val:
                cells = t.add_row().cells
                for c, v in zip(cells, r): c.text = str(v)
    d.add_paragraph(D.FICTION).runs[0].italic = True
    cp = d.core_properties; cp.author = "CODED"; cp.title = title; cp.created = FIXED; cp.modified = FIXED; cp.last_modified_by = "CODED"
    d.save(os.path.join(OUT, name))

KIT_ROWS = [["Item", "Unit cost (KWD)", "Per family", "Cost per family (KWD)"]] + [[i, f"{c:.3f}", str(q), f"{c * q:.3f}"] for i, c, q in D.KIT] + \
           [["Delivery", f"{D.DELIVERY_COST:.3f}", "1", f"{D.DELIVERY_COST:.3f}"], ["Total per family", "", "", f"{D.PER_FAMILY:.3f}"]]

# ------------------------------------------------------------------ 1 · the winter campaign report (the source: Task 1.1, 1.4, Demo 1.3)
pdf(os.path.join(OUT, FILE_REPORT), "Winter Warmth 2026: campaign report (fictional)", [
    [Paragraph(f"{D.ORG}", B), Paragraph("Winter Warmth 2026: campaign report", T), Paragraph(f"Status at 24 November 2026 · Prepared by {D.HESSA}", B), Spacer(1, 6),
     Paragraph("1. Summary", H),
     Paragraph(f"Winter Warmth gives one warm home kit to each registered family for the winter. The campaign runs from {D.PERIOD}.", B),
     Paragraph(f"<b>Families registered: {D.FAMILIES:,}</b>, in four districts: Jahra, Farwaniya, Sabah Al-Salem and Kuwait City.", B),
     Paragraph(f"Budget: {kwd(D.BUDGET)}. Planned cost: {kwd(D.CAMPAIGN_COST)} (page {D.PAGE_KIT}).", B),
     Paragraph(f"Volunteers: {D.VOLUNTEERS} confirmed. Each kit is delivered by hand at one of three community halls.", B),
     Paragraph("2. Goals", H),
     Paragraph("Every registered family receives its kit before the coldest weeks of January. Every donor receives a thank-you letter and a receipt within 3 working days.", B)],
    [Paragraph("3. Delivery plan", H),
     Paragraph(f"<b>Deliveries start on {D.DELIVERY_START} 2026</b> and end on {D.DELIVERY_END}, from 08:00 to 13:00 on working days.", B),
     grid([["Center", "Days", "Families"]] + [[c, d, str(n)] for c, d, n in D.HALLS] + [["Total", "", f"{D.FAMILIES:,}"]], [70, 55, 30]),
     Spacer(1, 8),
     Paragraph("Each family books a time slot by phone. Volunteers check the family's booking number, not their name, at the door.", B),
     Paragraph("Heaters arrive from the supplier before the first delivery day. Blankets, jackets and food baskets are packed at the Farwaniya hall.", B)],
    [Paragraph("4. The kit and the budget", H),
     Paragraph("One kit for one family:", B),
     grid(KIT_ROWS, [62, 34, 26, 44]), Spacer(1, 8),
     Paragraph(f"{D.FAMILIES:,} families × {kwd(D.PER_FAMILY)} = <b>{kwd(D.CAMPAIGN_COST)}</b>. Budget {kwd(D.BUDGET)}. Left: {kwd(D.LEFT)}.", B),
     Paragraph("Any change to the number of families needs the General Manager's approval, because the budget has little room.", B)],
    [Paragraph("5. Rules for volunteers and media", H),
     Paragraph(f"<b>{D.PHOTO_RULE}</b>", B),
     Paragraph("Take photos of kits, halls and volunteers only, with their permission.", B),
     Paragraph("Never share a family's address, phone number, civil ID or case details outside the case team.", B),
     Paragraph("Every public post uses one number from this report, and ends with the donation link.", B),
     Paragraph("6. Contacts", H),
     Paragraph(f"Programs: {D.HESSA} · Marketing: {D.NOURA} · Accounts: {D.FAHAD} · Media: {D.BADER}", B)],
], f"{D.ORG} · Winter Warmth 2026 · campaign report")

# ------------------------------------------------------------------ 2 · donations, 1 to 24 November (month to date), with the planted duplicate
wb = openpyxl.Workbook(); ws = wb.active; ws.title = "Donations"
ws.append(["Date", "Receipt", "Donor ID", "Channel", "Campaign", "Amount (KWD)"])
for c in ws[1]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="1B2A41")
for r in D.DON_EXPORT:
    ws.append([dt.date(*r["date"]), r["receipt"], r["donor"], r["channel"], r["campaign"], r["amount"]])
for row in ws.iter_rows(min_row=2):
    row[0].number_format = "dd/mm/yyyy"; row[5].number_format = "#,##0.000"
for col, w in zip("ABCDEF", (12, 15, 11, 18, 22, 15)): ws.column_dimensions[col].width = w
ws.freeze_panes = "A2"
cs = wb.create_sheet("Control totals")
cs.append([f"Control totals · donations 1 to {D.DON_LAST} November 2026 (month to date)"]); cs["A1"].font = Font(bold=True)
cs.append(["Checked by the accounts team against the bank and KNET statements."]); cs.append([])
cs.append(["Campaign", "Total (KWD)"])
for c in cs[4]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="1B2A41")
for k in D.CAMPAIGNS: cs.append([k, D.CONTROL[k]])
cs.append(["All campaigns", D.TOTAL_CONTROL]); cs.cell(cs.max_row, 1).font = Font(bold=True)
for row in cs.iter_rows(min_row=5): row[1].number_format = "#,##0.000"
cs.column_dimensions["A"].width = 26; cs.column_dimensions["B"].width = 16
ns = wb.create_sheet("Notes")
for line in [f"Donations for November 2026, month to date: 1 to {D.DON_LAST} November.", "One row = one receipt. Donor IDs only; names are kept in the donor system, never in this file.",
             "Campaign codes: " + ", ".join(f"{v} = {k}" for k, v in D.CODES.items()) + ".", D.FICTION]: ns.append([line])
ns.column_dimensions["A"].width = 100
wb.properties.creator = "CODED"; wb.properties.created = FIXED; wb.properties.modified = FIXED; wb.properties.lastModifiedBy = "CODED"
wb.save(os.path.join(OUT, FILE_DON))

# ------------------------------------------------------------------ 3 · the post screenshot with 2 planted errors (Task 1.1)
from PIL import Image, ImageDraw, ImageFont
FD = "/usr/share/fonts/truetype/dejavu/"
def F(sz, bold=False):
    try: return ImageFont.truetype(FD + ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"), sz)
    except OSError: return ImageFont.load_default()
W_, H_ = 900, 1280
im = Image.new("RGB", (W_, H_), "#FFFFFF"); dr = ImageDraw.Draw(im)
dr.rectangle([0, 0, W_, 90], fill="#F4F4F4")
dr.ellipse([24, 18, 78, 72], fill="#0F6E6E"); dr.text((51, 45), "M", font=F(26, True), fill="#E9D8B4", anchor="mm")
dr.text((96, 28), "misbah.charity", font=F(26, True), fill="#1B2A41"); dr.text((96, 60), "Draft post · not published", font=F(18), fill="#888888")
dr.rectangle([0, 90, W_, 690], fill="#0F6E6E")
dr.polygon([(400, 200), (500, 200), (530, 240), (370, 240)], fill="#E9D8B4"); dr.rounded_rectangle([385, 240, 515, 410], 18, outline="#E9D8B4", width=10)
dr.ellipse([430, 285, 470, 365], fill="#F2C879"); dr.rectangle([370, 410, 530, 430], fill="#E9D8B4"); dr.arc([420, 150, 480, 210], 180, 360, fill="#E9D8B4", width=8)
dr.text((W_ // 2, 500), "WINTER WARMTH 2026", font=F(52, True), fill="#FFFFFF", anchor="mm")
dr.text((W_ // 2, 565), "One warm home kit for every family", font=F(30), fill="#E9D8B4", anchor="mm")
dr.text((W_ // 2, 640), "Misbah Charity Society", font=F(24), fill="#FFFFFF", anchor="mm")
dr.text((24, 712), "♡  ○  ➤", font=F(34), fill="#1B2A41")
cap = ["misbah.charity  Winter is here, and so are we.",
       f"Deliveries start {D.DELIVERY_START_WRONG}!",
       f"Together we will warm {D.FAMILIES_WRONG:,} families",
       "across Kuwait this winter.",
       f"One kit costs {kwd(D.PER_FAMILY)}. Give a kit:",
       f"{D.LINK}",
       "#MisbahWinter"]
y = 780
for i, line in enumerate(cap):
    dr.text((24, y), line, font=F(29, i == 0), fill="#1B2A41" if i < 5 else "#0F6E6E"); y += 48
dr.rectangle([0, H_ - 70, W_, H_], fill="#FFF4D6"); dr.text((W_ // 2, H_ - 35), "DRAFT · fictional training file · Misbah Charity Society is not real", font=F(20, True), fill="#7A5A00", anchor="mm")
im.save(os.path.join(OUT, FILE_POST), optimize=True)

# ------------------------------------------------------------------ 4 · the campaign brief (Project knowledge, Task 1.4 A, 3.1, 4.1)
doc(FILE_BRIEF, "Winter Warmth 2026 · campaign brief", [
    ("p", f"Owner: {D.NOURA}. Status: approved by the General Manager, 2 November 2026."),
    ("h", "Goal"), ("p", f"One warm home kit for each of the {D.FAMILIES:,} registered families, delivered by hand between {D.DELIVERY_START} and {D.DELIVERY_END}."),
    ("h", "Who we talk to"), ("b", "Donors in Kuwait: individuals, families and companies."), ("b", "Volunteers: students and young professionals."), ("b", "Families: through the case team only, never in public posts."),
    ("h", "Key messages"), ("b", f"{kwd(D.PER_FAMILY)} warms one home for the winter."), ("b", f"{D.VOLUNTEERS} volunteers deliver every kit by hand."), ("b", "Every family is received with dignity: no faces, no names."),
    ("h", "The kit"), ("t", KIT_ROWS),
    ("p", f"Budget: {kwd(D.BUDGET)}. {D.FAMILIES:,} families cost {kwd(D.CAMPAIGN_COST)}."),
    ("h", "Channels and timeline"), ("b", "Instagram: one post a day in the delivery weeks."), ("b", "WhatsApp broadcast to donors: every Sunday."), ("b", "Newsletter: 1 December and 20 December."),
    ("b", f"Deliveries: {D.DELIVERY_START} to {D.DELIVERY_END}, at the {', '.join(D.CENTERS[:2])} and {D.CENTERS[2]}."),
    ("h", "The donation link"), ("p", D.LINK),
])

# ------------------------------------------------------------------ 5 · the brand guide (Project knowledge)
doc(FILE_BRAND, "Misbah Charity Society · brand guide", [
    ("p", "How we sound and look in every post, letter and design."),
    ("h", "Voice"), *[("b", x) for x in D.VOICE],
    ("h", "Rules"), *[("n", x) for x in D.BRAND_RULES],
    ("h", "Colors"), ("t", [["Name", "Hex"]] + [list(c) for c in D.COLORS]),
    ("h", "Sign-off"), ("p", "With thanks, Misbah Charity Society"),
    ("h", "Words we use"), ("t", [["Use", "Instead of"], ["families", "the poor, the needy"], ["supporters, donors", "sponsors"], ["a warm home kit", "aid package"], ["volunteers", "workers"]]),
])

# ------------------------------------------------------------------ 6 · the inbox and Sunday's calendar (Demo 2.1, Task 2.1 fallback)
pdf(os.path.join(OUT, FILE_INBOX), "Inbox and calendar export (fictional)", [
    [Paragraph("Inbox and calendar export", T), Paragraph(f"Hessa's work account · exported Wednesday 25 November 2026, 17:00 · {D.ORG}", B), Spacer(1, 6),
     Paragraph(f"Calendar: {D.BRIEF_DAY}", H),
     grid([["Time", "Meeting", "Who", "Notes"]] + [[t, Paragraph(m, B), Paragraph(w, B), ""] for t, m, w, _p in D.MEETINGS], [24, 52, 52, 42]),
     Paragraph("Inbox: the 8 newest emails", H),
     grid([["Received", "From", "Subject"]] + [[r, Paragraph(f, B), Paragraph(s, B)] for f, s, r, _g, _n in D.EMAILS], [30, 60, 80])],
    [Paragraph("The emails in full", H)] + [x for f, s, r, g, _n in D.EMAILS for x in (Paragraph(f"<b>{s}</b> · {f} · {r}", B), Paragraph(g, B), Spacer(1, 4))],
], f"{D.ORG} · inbox and calendar export")

# ------------------------------------------------------------------ 7 · the starter skill (Task 3.2)
SKILL_MD = f"""---
name: donor-thank-you
description: Write a thank-you letter to a {D.ORG} donor. Use when someone asks for a donor thank-you letter or a receipt letter.
---

# Donor thank-you letter

Write one letter per donor, under 120 words, in the Misbah voice: warm, respectful and clear.

{D.FICTION}

## Steps
""" + "\n".join(f"{i}. {s}" for i, s in enumerate(SKILL_STEPS, 1)) + f"""

## Rules
- Never name a family or describe a family's situation.
- Use only the amount, campaign and receipt number you are given. If one is missing, ask for it.
- One winter kit costs {kwd(D.PER_FAMILY)}. Round the number of kits down and say "about".

## Example

Dear supporter,

Thank you for your gift of KWD 100.000 to Winter Warmth. It pays for about two winter kits: blankets, a heater,
food and children's jackets for two families. Your kindness keeps a home warm this winter.

Receipt: {D.EXAMPLE_GIFT["receipt"]}

With thanks,
Misbah Charity Society

See template.md for the layout.
"""
TEMPLATE_MD = """# Letter layout

Dear {name or "supporter"},

Thank you for your gift of {amount in KWD, three decimals} to {campaign}. {What it paid for, in one sentence.}
{One warm line of thanks.}

Receipt: {receipt number}

With thanks,
Misbah Charity Society
"""
def zwrite(path, members):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in members:
            zi = zipfile.ZipInfo(name, date_time=(2026, 11, 24, 9, 0, 0)); zi.compress_type = zipfile.ZIP_DEFLATED; zi.external_attr = 0o644 << 16
            z.writestr(zi, data)
zwrite(os.path.join(OUT, FILE_SKILL), [("donor-thank-you/SKILL.md", SKILL_MD), ("donor-thank-you/template.md", TEMPLATE_MD)])

# ------------------------------------------------------------------ 8 · the receipts folder: 14 receipts and 1 copy (Demo 1.2, Task 1.2)
def receipt_pdf(r):
    n, sup, what, qty, unit, code = r
    buf = io.BytesIO()
    story = [Paragraph(sup, T), Paragraph("Tax invoice and receipt", B), Spacer(1, 4),
             grid([["Receipt no.", D.rc_no(n)], ["Date", D.RC_DATES[n]], ["Billed to", D.ORG], ["Campaign code", code or ""]], [40, 70], head=False), Spacer(1, 8),
             grid([["Item", "Quantity", "Unit (KWD)", "Total (KWD)"], [what, f"{qty:,}", f"{unit:,.3f}", f"{qty * unit:,.3f}"]], [52, 22, 24, 26]), Spacer(1, 8),
             Paragraph(f"<b>Paid: {kwd(D.rc_amount(r))}</b> by bank transfer.", B), Paragraph(D.FICTION, B)]
    SimpleDocTemplate(buf, pagesize=A5, leftMargin=12 * mm, rightMargin=12 * mm, topMargin=14 * mm, bottomMargin=12 * mm,
                      title=f"Receipt {D.rc_no(n)}", author="CODED", creator="CODED", invariant=1).build(story)
    return buf.getvalue()
members = []
for r in D.RECEIPTS:
    data_ = receipt_pdf(r)
    members.append((f"misbah-receipts-nov-2026/{D.rc_file(r[0])}", data_))
    if r[0] == D.DUP_RECEIPT_NO: members.append((f"misbah-receipts-nov-2026/{D.rc_file(r[0], True)}", data_))
members.append(("misbah-receipts-nov-2026/README.txt", f"Receipts from the Winter Warmth deliveries and other campaigns, November 2026.\nCampaign codes: " + ", ".join(f"{v} = {k}" for k, v in D.CODES.items()) + f".\n{D.FICTION}\n"))
zwrite(os.path.join(OUT, FILE_RECEIPTS), sorted(members))

for f in sorted(os.listdir(OUT)): print(f"{os.path.getsize(os.path.join(OUT, f)):>8}  {f}")
