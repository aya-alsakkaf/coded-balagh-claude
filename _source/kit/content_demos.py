# -*- coding: utf-8 -*-
"""Every demo and hands-on task of Claude in Layers: prompts, expected results, backups, answer keys and prompt-player data.
Numbers come from data.py, so the deck, prompt sheet, runbook, backups and answer key always match."""
import data as D
from data import kwd

FILE_REPORT = "misbah-winter-campaign-report.pdf"
FILE_DON = "misbah-donations-nov-2026.xlsx"
FILE_POST = "misbah-post-screenshot.png"
FILE_BRIEF = "misbah-campaign-brief.docx"
FILE_BRAND = "misbah-brand-guide.docx"
FILE_INBOX = "misbah-inbox-and-calendar.pdf"
FILE_SKILL = "misbah-donor-thanks-skill.zip"
FILE_RECEIPTS = "misbah-receipts-nov-2026.zip"
ALL_FILES = [FILE_REPORT, FILE_DON, FILE_POST, FILE_BRIEF, FILE_BRAND, FILE_INBOX, FILE_SKILL, FILE_RECEIPTS]

# prompt sheet sections: sec -> (day, name)
BLOCK = {1: (1, "Opener"), 2: (1, "Layer 1 · Chat: ask, attach, speak"), 3: (1, "Layer 1 · Artifacts"), 4: (1, "Layer 2 · Connectors"),
         5: (1, "Layer 3 · Memory, instructions and Projects"), 6: (1, "Layer 3 · Skills"), 7: (1, "Layer 4 · Cowork, plugins and schedules"),
         8: (1, "Integration · Your first AI employee")}

DEMOS = {}
def demo(did, **kw):
    kw.setdefault("stretch", []); kw.setdefault("stretch_prompts", []); kw.setdefault("files", [])
    kw["card"] = ("Task " if kw.get("hands_on") else "Demo ") + kw["skill"]
    DEMOS[did] = kw
def tbl(head, rows): return ("table", [head] + [list(r) for r in rows])
def joined(parts): return " ".join(v for _k, v in parts)
CAMP_ROWS = [(c, str(D.EXPORT_ROWS[c]), kwd(D.EXPORT[c])) for c in D.CAMPAIGNS]

# ===================================================================== the layered request (the opener and Demo 3.1)
WEAK_POST = "Write a post for our winter campaign."
# the right-hand window: the same words, sent inside the campaign Project. The parts show what the Project already holds.
POST_PARTS = [["Same request", WEAK_POST],
              ["Project", "Sent inside the Misbah Winter Campaign Project."],
              ["Instructions", "Already in the Project: our voice, English then Arabic, one checked number, end with the link."],
              ["Knowledge", "Already in the Project: the brand guide and the campaign brief."]]
WEAK_ANSWER = [f"This winter, {D.FAMILIES:,} families need warmth. Only {kwd(D.PER_FAMILY)} buys a winter kit, and {D.VOLUNTEERS} volunteers deliver them.",
               f"Help the needy stay warm. Donate now: {D.LINK}"]
STRONG_POST = [f"This winter, {D.FAMILIES:,} families get a warm home kit, delivered by hand.", "(The same message in Arabic.)",
               f"#MisbahWinter and our Arabic hashtag. Give a kit: {D.LINK}"]

# ===================================================================== OPENER
demo("d10", day=1, skill="1.0", sec=1, title="One request, two setups", tool="Claude", files=[FILE_BRIEF], kind="showcase",
 setup=["[T] Before the session: build the Misbah Winter Campaign Project from Task 3.1 (its instructions, the brand guide and the brief).",
        "[T] Open two windows: a plain new chat, and a new chat inside the Project. Attach the campaign brief in both.",
        "[T] Type the same request in both. Compare the two posts against the brand guide."],
 prompts=[("Plain chat, brief attached", WEAK_POST), ("Inside the campaign Project, brief attached", WEAK_POST)],
 expected=f"Plain chat: the brief's facts, but three numbers, English only, no hashtags and the word “the needy”, which the brand guide does not allow. Inside the Project: one number ({D.FAMILIES:,} families), English then Arabic, both hashtags, and the link {D.LINK} at the end.",
 say="Same tool, same request. The only thing I changed is what Claude already knows and can reach.",
 point="The layers decide the answer. You still check it.",
 backup=[("h", "Plain chat: typical result"), ("p", "“" + " ".join(WEAK_ANSWER) + "”"),
         ("h", "Inside the Project: typical result"), ("ul", STRONG_POST)],
 fallback="Play the opener in the deck; it shows both results.",
 hint="Compare both posts with the brand guide: how many numbers, which languages, which words?")

# ===================================================================== LAYER 1 · CHAT
RATE = [["Web search", "Search the web."],
        ["Ask", "A US donor pledged USD 5,000 to our winter campaign. What is that in KWD at today's rate?"],
        ["Source", "Use the Central Bank of Kuwait or another official source, and give me the link."],
        ["Format", "One line: the rate, the date of the rate, and the KWD amount to three decimals."]]
demo("d11", day=1, skill="1.1", sec=2, title="Trained knowledge, then web search", tool="Claude · web search", files=[], kind="player",
 setup=["Ask the first question: it tells Claude not to search. Note the rate and whether a date or a source is given.", "Ask again with the full prompt, which asks Claude to search the web. (Older layout: turn on Web search in the + menu first. The new Claude experience has no toggle.)"],
 prompts=[("Web search off", "Do not search the web. A US donor pledged USD 5,000 to our winter campaign. What is that in KWD?"), ("Web search on", joined(RATE))],
 expected="Off: an approximate rate from training, often with a note that it may be out of date, and no source. On: today's rate with its date, a link to the source, and the KWD amount calculated from that rate.",
 say="Without web search, Claude answers from what it learned. With it, Claude reads today's pages and shows you where the number came from.",
 point="Current facts need web search and a source you can open.",
 backup=[("h", "What changes when web search is on"), tbl(["", "Web search off", "Web search on"], [("Rate", "From training, may be old", "Today's rate, with its date"), ("Source", "None", "A link you can open"), ("KWD amount", "An estimate", "Calculated from the quoted rate")])],
 fallback="Show the backup table. Rates change daily, so never put a rate on the slide as fact.",
 hint="Does the answer give a date for the rate and a link? If not, it came from training.",
 player={"parts": RATE, "table": [["", "Web search off", "Web search on"], ["Rate", "From training, may be old", "Today's rate, with its date"], ["Source", "None shown", "A link you can open"], ["KWD amount", "An estimate", "Calculated from the quoted rate"]],
         "best": 2, "reco": ["<b>Trained knowledge</b> stops on a date. It does not know today.", "<b>Web search</b> reads current pages and shows its sources.", "<b>Your check:</b> open the link and compare the number."],
         "control": "Open the source link and check the rate before you use the amount."})

demo("t11", day=1, skill="1.1", sec=2, title="One chat, the web and three files", tool="Claude · web search and files", files=[FILE_REPORT, FILE_DON, FILE_POST], kind="task", hands_on=True, minutes=10, solo="on your own",
 setup=["Run prompt 1 (older layout: turn on Web search in the + menu first). Open the link it gives.",
        "Attach the report (PDF), the donations file (Excel) and the post (PNG). Run prompts 2 to 4.", "Check the page Claude gives for each error in the post."],
 prompts=[("1 · The web", "Search the web: a US donor pledged USD 5,000. What is that in KWD today? Give the rate, its date and the link."),
          ("2 · The PDF", "From the attached report: how many families are registered, and when do deliveries start? Give the page."),
          ("3 · The Excel file", "Use code on the attached donations file: total donations by campaign in KWD, and the rows used."),
          ("4 · The screenshot", "Compare the attached post with the report. List every fact that does not match, with the page.")],
 expected="Web: today's rate with its date and a link to the source, and the KWD amount. Files: two errors in the post: " + "; ".join(f"{a.lower()}: the post says “{b}”, the report says {c}" for a, b, c in D.POST_ERRORS) + ".",
 say="The PDF is the source. The screenshot is a draft. Claude reads both; you decide which one is right.",
 point="Attach the source, not a summary of it. Check the page it gives.",
 backup=[("h", "The two errors in the post"), tbl(["Fact", "The post says", "The report says"], D.POST_ERRORS)],
 answer=[("h", "The two planted errors"), tbl(["Fact", "The post says", "The report says"], D.POST_ERRORS),
         ("h", "Donations by campaign (from the export, 1 to 24 November)"), tbl(["Campaign", "Rows", "Total"], CAMP_ROWS),
         ("note", f"The families figure ({D.FAMILIES:,}) is on pages 1 to 3, so accept any of them; page {D.PAGE_FAMILIES} is the registration count. Also accept extra findings against the rules on page {D.PAGE_RULES}: the post uses two numbers (one is allowed), and it ends with a hashtag, not the donation link."),
         ("h", "Prompt 1: the web"), ("p", "No fixed answer: rates change every day. Accept any rate that comes with its date and a link to an official or bank source, and a KWD amount that matches that rate."),
         ("note", f"The export total is {kwd(D.TOTAL_EXPORT)} from {D.DON_ROWS} rows. Task 1.3 finds why it is {kwd(D.DIFF)} above the Control totals sheet.")],
 deliverable="The KWD amount with the rate's date and link, and the 2 errors in the post with their pages.",
 fallback="If the PNG does not upload, the trainer shows misbah-post-screenshot.png on the screen; attach only the PDF.",
 hint="A rate with no date or link came from training. The post has 2 errors: a date and a number.",
 stretch=["Open the Claude app on your phone. Ask the PDF question by voice: tap the voice mode icon (the sound wave), not the microphone."])

# ===================================================================== LAYER 1 · ARTIFACTS
demo("d12", day=1, skill="1.2", sec=3, title="The winter-kit cost calculator", tool="Claude · artifact", files=[FILE_BRIEF], kind="demo",
 setup=["[T] Use the calculator on the slide. Change the families to 1,200, then back to 1,020.", "[T] Untick the heater to show how the cost per family changes."],
 prompts=[("Ask for the calculator", f"Build an artifact: a winter-kit cost calculator from the attached campaign brief. Inputs: the number of families and the items in one kit. Show the cost per family, the total in KWD and the gap to the budget of {kwd(D.BUDGET)}.")],
 expected=f"Cost per family {kwd(D.PER_FAMILY)}; {D.FAMILIES:,} families cost {kwd(D.CAMPAIGN_COST)}, which leaves {kwd(D.LEFT)} of the budget. At {D.FAMILIES_WRONG:,} families the cost is {kwd(D.PER_FAMILY * D.FAMILIES_WRONG)}, over the budget.",
 say="This is what Claude gives you when you ask for a tool instead of an answer. Volunteers can open it again next week.",
 point="Ask for a tool, not a paragraph.",
 backup=[("h", "The numbers the calculator must show"), tbl(["Item", "Unit cost", "Per family", "Line total"], [(i, f"{c:.3f}", str(q), f"{c * q:.3f}") for i, c, q in D.KIT] + [("Delivery", f"{D.DELIVERY_COST:.3f}", "1", f"{D.DELIVERY_COST:.3f}"), ("<b>Per family</b>", "", "", f"<b>{D.PER_FAMILY:.3f}</b>")])],
 fallback="If the slide calculator does not respond, press R to reload the slide; the numbers are on the backup.",
 hint=f"Cost per family {kwd(D.PER_FAMILY)}. Multiply by the families and compare with the budget.")

DASH = [["Output", "Build an artifact: a dashboard I can share with the board."],
        ["Source", f"Use code on the attached donations file, 1 to {D.DON_LAST} November 2026."],
        ["Show", "Donations by campaign and by channel, one chart each, then three lines of summary."],
        ["Check", "Show the number of rows and the total, so I can match them to the Control totals sheet."]]
demo("d13", day=1, skill="1.3", sec=3, title="A donations dashboard from the Excel file", tool="Claude · artifact", files=[FILE_DON], kind="player",
 setup=["Attach misbah-donations-nov-2026.xlsx to a new chat.", "Paste the prompt below. Compare the total with the Control totals sheet in the same file."],
 prompts=[("Dashboard", joined(DASH))],
 expected=f"Two charts and three summary lines. Rows: {D.DON_ROWS}; total {kwd(D.TOTAL_EXPORT)}. The Control totals sheet says {kwd(D.TOTAL_CONTROL)}: {kwd(D.DIFF)} more in Winter Warmth.",
 say="The chart looks finished. The check line is what tells you it is not ready yet.",
 point="An artifact is only as right as its source. Check one total before you share.",
 backup=[("h", "Typical result (calculated on the export as it is)"), tbl(["Campaign", "Rows", "Total"], CAMP_ROWS + [("<b>All</b>", f"<b>{D.DON_ROWS}</b>", f"<b>{kwd(D.TOTAL_EXPORT)}</b>")]),
         ("h", "By channel (the export as it is)"), tbl(["Channel", "Total"], [(c, kwd(v)) for c, v in D.BY_CHANNEL_EXPORT.items()]),
         ("note", f"Bank transfer includes the duplicate receipt {D.DUP_RECEIPT} ({kwd(D.DUP_AMOUNT)}). Counted once, it is {kwd(D.BY_CHANNEL['Bank transfer'])}.")],
 fallback="Show the backup table. If file upload fails, the trainer runs it on the presenting laptop.",
 hint="Compare the dashboard total with the Control totals sheet.",
 player={"parts": DASH, "table": [["Campaign", "Rows", "Total (KWD)"]] + [[c, str(D.EXPORT_ROWS[c]), f"{D.EXPORT[c]:,.3f}"] for c in D.CAMPAIGNS], "best": 2,
         "reco": [f"<b>Largest:</b> {D.TOP_CAMPAIGN}, then Ramadan Iftar 2027.", f"<b>Check line:</b> {D.DON_ROWS} rows, {kwd(D.TOTAL_EXPORT)}.",
                  f"<b>Control totals sheet:</b> {kwd(D.TOTAL_CONTROL)}. Find the {kwd(D.DIFF)} before the board sees it."],
         "control": "The totals do not match. Find the difference before you share."})

ART_PROMPTS = [("A · Calculator · brief", "Build a cost calculator artifact from the attached brief, with the budget gap."),
               ("B · Dashboard · donations", "Build a dashboard artifact from the attached file: by campaign, with the total."),
               ("C · Quiz game · report", "Build a 6-question quiz game artifact for new volunteers from the attached report."),
               ("D · Board deck · report", "Make a 5-slide board deck from the attached report: goal, families, kit, budget."),
               ("E · Document · report", "Write a one-page volunteer guide as a doc from the attached report.")]
demo("t13", day=1, skill="1.3", sec=3, title="Build one artifact for Misbah", tool="Claude · artifacts", files=[FILE_BRIEF, FILE_DON, FILE_REPORT], kind="task", hands_on=True, minutes=15, solo="on your own",
 setup=["Choose A to E. Attach its file and paste its prompt.", "Ask for one change. Then check one number against the file.",
        "Open Share and copy the link (private is fine)."],
 prompts=ART_PROMPTS,
 expected=f"A: {kwd(D.PER_FAMILY)} per family, {kwd(D.CAMPAIGN_COST)} for {D.FAMILIES:,} families. B: {D.DON_ROWS} rows and {kwd(D.TOTAL_EXPORT)}, {kwd(D.DIFF)} above the Control totals because receipt {D.DUP_RECEIPT} is in the file twice. C: questions that match the report. D: five slides with the report's numbers. E: a doc you edit in place, with deliveries from {D.DELIVERY_START} to {D.DELIVERY_END}.",
 say="Pick the one you would really use next week.",
 point="Name the artifact and the source in the first line. Check one number. Then share.",
 backup=[("h", "The number to check for each choice"), tbl(["Choice", "Check this number", "Where"], [("A Calculator", kwd(D.CAMPAIGN_COST), "Campaign brief, the kit table and budget"), ("B Dashboard", kwd(D.TOTAL_CONTROL), "Control totals sheet"),
                                                                                              ("C Quiz game", f"{D.FAMILIES:,} families", f"Report, page {D.PAGE_FAMILIES}"), ("D Board deck", kwd(D.BUDGET), f"Report, page {D.PAGE_KIT}"), ("E Document", f"Deliveries start {D.DELIVERY_START}", f"Report, page {D.PAGE_DELIVERY}")])],
 answer=[("h", "What a finished artifact shows"), ("ul", ["It opens beside the chat and works: inputs change the result, the slides open, or the doc can be edited in place.", "One number was checked against the file.", "It has a share link (private is fine)."]),
         ("h", "Choice B: why the total is too high"), ("p", f"Receipt {D.DUP_RECEIPT} ({kwd(D.DUP_AMOUNT)}, {D.DUP_CAMPAIGN}) is in the export twice, on sheet rows {D.DUP_SHEET_ROWS[0]} and {D.DUP_SHEET_ROWS[1]}. Without it, the total is {kwd(D.TOTAL_CONTROL)}, the same as the Control totals sheet."),
         ("h", "Correct totals by campaign"), tbl(["Campaign", "Total"], [(c, kwd(v)) for c, v in D.CONTROL.items()])],
 deliverable="One working artifact, one number checked against its file, and its share link.",
 fallback="If artifacts do not open, check Settings › Capabilities: Create and edit files must be on.",
 hint="A total that is too high often hides a row counted twice.",
 stretch=["Build a second artifact from another choice, or add an “Ask Claude” box inside your artifact."],
 stretch_prompts=[("Claude inside", "Add a box to this artifact where a volunteer can ask Claude a question about the campaign. Use only the report for the answers.")])

# ===================================================================== LAYER 2 · CONNECTORS
BRIEF = [["Connectors", "Gmail and Google Calendar are on, from the + menu."],
         ["Ask", f"Brief me for {D.BRIEF_DAY.rsplit(' ', 1)[0]}: each meeting, who attends, and the latest email about it."],
         ["Limit", "Read only. Draft a reply to anything urgent, but do not send it."],
         ["Format", "A table: time, meeting, what to prepare, the email to answer."]]
demo("d21", day=1, skill="2.1", sec=4, title="Sunday's brief from email and calendar", tool="Claude · Gmail and Google Calendar", files=[FILE_INBOX], kind="player",
 setup=["Watch only: the trainer runs this on the CODED training account. You connect an approved account, or use the fictional inbox file, in Task 2.1.",
        "[T] Click + › Connectors, turn on Gmail and Google Calendar, paste the prompt, then check one meeting and one email against the source."],
 prompts=[("Sunday's brief", joined(BRIEF[1:]))],
 expected=f"Three meetings on {D.BRIEF_DAY}, with the heater delay as the urgent item. One draft reply to Salem, saved, not sent.",
 say="Claude reads the inbox and the calendar with your sign-in. It drafts. Sending stays with you.",
 point="Connect once. Read freely. Approve every action.",
 backup=[("h", f"Typical brief for {D.BRIEF_DAY}"), tbl(["Time", "Meeting", "Who", "Prepare"], D.MEETINGS),
         ("h", "Emails that need a reply"), ("ul", [f"{a}: {b}" for a, b, _c, _g, need in D.EMAILS if need])],
 fallback="Use the CODED training Google account. If it fails, attach misbah-inbox-and-calendar.pdf and show the backup.",
 hint="Check the meeting time in the calendar and the heater numbers in the email.",
 player={"parts": BRIEF, "table": [["Time", "Meeting", "Prepare"]] + [[t, m, p] for t, m, _w, p in D.MEETINGS], "best": 2,
         "reco": ["<b>Urgent:</b> the heater delay. A reply is drafted and waits for you.", "<b>Board pack:</b> donations to 24 November and one budget slide by Monday 12:00.", "<b>Not sent:</b> Claude asks before it sends, replies or forwards."],
         "control": "Read the draft, check the numbers in the email, then decide to send."})

SORT = [("Rewrite a public post about the winter campaign", "green"), ("Practice on the fictional Misbah files", "green"),
        ("Search your work inbox for the heater emails, in your organization's approved account", "amber"), ("Draft a reply to a supplier and save it as a draft for you", "amber"),
        ("Upload the donor list with names, phone numbers and amounts", "red"), ("Paste a family's case file with civil ID and income", "red"),
        ("Let Claude send emails to donors without your approval", "red"), ("Summarize a public news article about the weather this winter", "green")]
demo("t21", day=1, skill="2.1", sec=4, title="Connect your email and calendar, then get Sunday's brief", tool="Claude · Gmail and Google Calendar", files=[FILE_INBOX], kind="task", hands_on=True, minutes=15, solo="on your own",
 setup=["Connect only an account your organization approved for Claude. No approval, or donor or family emails in it? Attach misbah-inbox-and-calendar.pdf instead.",
        "Approved: + › Connectors, turn on Gmail and Calendar, sign in. Set the mode to Manual. Run the brief for your next working day, read only.",
        "Ask for one draft reply. Do not send it.", "Check two facts in the brief against the email or the calendar itself."],
 prompts=[("The brief", "Brief me for my next working day: each meeting, who attends, and the latest email about it. Read only. A table: time, meeting, what to prepare, the email to answer."),
          ("One draft", "Draft a short reply to the most urgent email in the brief. Save it as a draft. Do not send it.")],
 expected="A brief table for the next working day, one draft saved (not sent), and two facts checked. With the fallback file: the three meetings on Sunday 29 November and a draft to Salem about the heaters.",
 say="Amber needs an approved account. Without one, the fictional inbox teaches the same thing. Nothing leaves your account without you.",
 point="Connect once. Read freely. Approve every action.",
 backup=[("h", "Fallback file: the brief for Sunday 29 November"), tbl(["Time", "Meeting", "Who", "Prepare"], D.MEETINGS),
         ("h", "A good draft to Salem"), ("p", "“Dear Salem, thank you for the update on order WW-H-300. Please confirm in writing that 120 heaters arrive on Tuesday 1 December and the other 180 on Sunday 6 December. Our deliveries to families start that day. Best regards, Hessa, Misbah Charity Society.”")],
 answer=[("h", "What to check in each participant's work"), ("ul", ["The account is one the organization approved, or the participant used the fictional file.", "Gmail and Google Calendar are connected and turned on in the chat (approved accounts only).", "The brief is a table for the next working day.", "One draft is saved and was not sent.", "Two facts were checked against the source email or event."]),
         ("h", "If an account cannot connect"), ("p", "On Team and Enterprise plans an owner must turn the Google connectors on first, and Google Workspace admins may need to trust Claude. Use the fallback file and note it for their IT team.")],
 deliverable="Your brief table, one draft reply (not sent), and two facts checked against the source.",
 fallback="If the account is not approved or cannot connect, use misbah-inbox-and-calendar.pdf. Show the backup brief at the end.",
 hint="Look for the email that changes a date or a number. That is the urgent one.",
 stretch=["Ask Claude to find a free 30-minute slot next week for the Ramadan Iftar 2027 planning meeting. Approve the event only if it is real."],
 stretch_prompts=[("A free slot", "Find a free 30-minute slot next week for the Ramadan Iftar 2027 planning meeting. Propose the event, but wait for my approval before you create it.")])

# ===================================================================== LAYER 3 · MEMORY, INSTRUCTIONS, PROJECTS
PROJ = [["Project", "Create a Project named Misbah Winter Campaign."],
        ["Instructions", f"You write for Misbah Charity Society. Follow the brand guide in this Project. English, then Arabic. One checked number per post, and both hashtags. {D.PHOTO_RULE} Every post ends with {D.LINK}."],
        ["Knowledge", f"Add {FILE_BRAND} and {FILE_BRIEF} to the Project."],
        ["Ask", "Write three Instagram captions for the delivery week."]]
INSTR = PROJ[1][1]
demo("d31", day=1, skill="3.1", sec=5, title="The Misbah Winter Campaign Project", tool="Claude · Projects", files=[FILE_BRAND, FILE_BRIEF], kind="player",
 setup=["Open Projects and create Misbah Winter Campaign.", "Paste the instructions below. Add the brand guide and the brief to the Project knowledge.", "Start a chat in the Project and ask for three captions."],
 prompts=[("Project instructions", INSTR), ("First chat in the Project", PROJ[3][1])],
 expected=f"Three short captions, English then Arabic, each with one checked number ({D.FAMILIES:,} families, {D.VOLUNTEERS} volunteers or {kwd(D.PER_FAMILY)} per kit), both hashtags, no faces or family names, each ending with {D.LINK}.",
 say="Write the rules once. Every chat in this Project starts with them and with the two files.",
 point="One Project per area of work: one campaign, one role.",
 backup=[("h", "What the Project holds"), tbl(["Part", "What goes in it", "Misbah example"], [("Name", "One area of work", "Misbah Winter Campaign"), ("Instructions", "The rules for every chat", "Voice, languages, photo rule, the link"), ("Knowledge", "Files Claude uses every time", f"{FILE_BRAND}, {FILE_BRIEF}"), ("Chats", "Each new request", "Three captions for the delivery week")])],
 fallback="Show the backup table and build the Project live on the presenting laptop.",
 hint="Does every caption end with the link and follow the photo rule?",
 player={"parts": PROJ, "table": [["Caption", "One number", "Ends with the link"], ["Day 1: the first kits leave", f"{D.FAMILIES:,} families", "Yes"], ["Day 4: volunteers at the halls", f"{D.VOLUNTEERS} volunteers", "Yes"], ["Last day: thank you", f"{kwd(D.PER_FAMILY)} per kit", "Yes"]], "best": 2,
         "reco": ["<b>Brand voice:</b> warm and clear, English then Arabic.", "<b>Rules kept:</b> no faces, no family names.", "<b>Next chat:</b> the rules and files are already there."],
         "control": "Check each number against the brief before you post."})

demo("t31", day=1, skill="3.1", sec=5, title="Set your instructions and build the campaign Project", tool="Claude · Projects", files=[FILE_BRAND, FILE_BRIEF], kind="task", hands_on=True, minutes=8, solo="on your own",
 setup=["Settings › Your Claude › Instructions (older layout: Settings › Account): add two lines about how you like answers.",
        "Create a Project named Misbah Winter Campaign. Paste the Project instructions below.", "Add the brand guide and the campaign brief to the Project knowledge.",
        "Start a chat in the Project and run the request. Check one caption against the brand guide."],
 prompts=[("Instructions for Claude (example)", "Reply in English first, then Arabic. Use short sentences and tables when you compare things."), ("Project instructions", INSTR), ("First chat in the Project", PROJ[3][1])],
 expected="A Project with instructions and two knowledge files; three captions that follow the brand guide; personal instructions saved.",
 say="Who you are and how you like answers: your instructions. The rules for one area of work: a Project.",
 point="Teach Claude once, in the right place.",
 backup=[("h", "Typical captions (each one: English, then the same in Arabic, then the hashtags and the link)"),
         ("ul", [f"Today the first kits leave our halls: {D.FAMILIES:,} families, one warm winter. (Arabic line) #MisbahWinter and the Arabic hashtag. {D.LINK}",
                 f"{D.VOLUNTEERS} volunteers deliver every kit by hand. Thank you for making it possible. (Arabic line) #MisbahWinter and the Arabic hashtag. {D.LINK}",
                 f"One kit warms one home: {kwd(D.PER_FAMILY)}. Give a kit today. (Arabic line) #MisbahWinter and the Arabic hashtag. {D.LINK}"])],
 answer=[("h", "What to check"), ("ul", ["Instructions for Claude has two lines.", "The Project has the instructions and both files.", "Each caption: English then Arabic, one number that matches the brief, both hashtags, no faces or family names, and the link at the end."])],
 deliverable="A Project with instructions and two files, and one caption checked against the brand guide.",
 fallback="If Projects are slow, build the instructions in a normal chat first, then move them into the Project.",
 hint="One number each, checked against the brief. English, then Arabic. The link comes last.",
 stretch=["Open Settings › Your Claude (older layout: Settings › Memory). Read what Claude remembers about you. Edit or delete one item."])

# ===================================================================== LAYER 3 · SKILLS
SKILL_STEPS = ["Greet the donor by name, or “Dear supporter” if there is no name.", "Name the campaign and the amount in KWD with three decimals.",
               f"Say what the gift paid for (one winter kit = {kwd(D.PER_FAMILY)}).", "Add one warm line of thanks.", "End with the receipt number and the Misbah sign-off."]
MAKE = [["Ask", "Help me create a skill for donor thank-you letters."],
        ["Method", "Five steps: greeting, campaign and amount in KWD, what it paid for, a line of thanks, the receipt number. Under 120 words."],
        ["Example", f"Here is one good letter: “Dear supporter, thank you for your gift of {kwd(D.EXAMPLE_GIFT['amount'])} to Winter Warmth. It pays for about two winter kits. Receipt: {D.EXAMPLE_GIFT['receipt']}. With thanks, Misbah Charity Society.” Copy its tone, not its numbers."],
        ["Save", "Package it as a skill named donor-thank-you. I will test it with /."]]
demo("d32", day=1, skill="3.2", sec=6, title="Create the donor thank-you skill with Claude", tool="Claude · Skills", files=[], kind="player",
 setup=["Check Settings › Capabilities: Create and edit files is on.", "In a new chat, paste the prompt below and answer Claude's questions.", "Watch only: do not save this skill. You install the starter skill, which has the same name, in Task 3.2."],
 prompts=[("Create the skill", joined(MAKE))],
 expected="Claude asks one or two questions, then offers a skill with a name, a description of when to use it, the five steps and an example. Saved, it shows in the / menu.",
 say="A skill is a method you write once. Claude reads its description and uses it when the task comes up.",
 point="A Project is where. A Skill is how.",
 backup=[("h", "Inside donor-thank-you/SKILL.md"), tbl(["Part", "What it says"], [("name", "donor-thank-you"), ("description", "Write a thank-you letter to a Misbah donor. Use when someone asks for a donor thank-you or receipt letter."), ("steps", " · ".join(SKILL_STEPS)), ("example", "One good letter, under 120 words")])],
 fallback="Upload the starter skill (misbah-donor-thanks-skill.zip) instead and test it.",
 hint="Look for the description: it decides when Claude uses the skill.",
 player={"parts": MAKE, "table": [["Part of the skill", "What it holds"], ["Name", "donor-thank-you"], ["Description", "When to use it: a donor thank-you or receipt letter"], ["Steps", "The five steps, in order"], ["Example", "One good letter"]], "best": 1,
         "reco": ["<b>Use it:</b> type / and choose donor-thank-you.", "<b>Share it:</b> on Team and Enterprise plans, share it from the skill; otherwise send the .zip.", "<b>Edit it:</b> change a step any time; every letter after that follows it."],
         "control": "Test the skill on one letter and check all five parts."})

demo("t32", day=1, skill="3.2", sec=6, title="Install the starter skill, test it, make it yours", tool="Claude · Skills", files=[FILE_SKILL], kind="task", hands_on=True, minutes=12, solo="on your own",
 setup=["Upload the .zip (do not unzip it). Older layout: Customize › Skills › + › Create skill › Upload a skill. Plugins page: Add › Upload.", "Start a new chat. Type / and choose donor-thank-you, then paste the test request.",
        "Check the letter: all five parts, under 120 words.", "Make it yours: ask Claude to change one step, then test again."],
 prompts=[("Test the skill", f"Write a thank-you letter for donor {D.THANKS['donor']}: {kwd(D.THANKS['amount'])} to {D.THANKS['campaign']}, receipt {D.THANKS['receipt']}."),
          ("Change one step", "Update the donor-thank-you skill: add the delivery start date, Sunday 6 December, after the line about what the gift paid for.")],
 expected=f"A letter under 120 words with all five parts: greeting, {D.THANKS['campaign']} and {kwd(D.THANKS['amount'])}, what it paid for (about three winter kits), one line of thanks, receipt {D.THANKS['receipt']} and the sign-off.",
 say="Test it once, then change it. That is how a skill becomes yours.",
 point="Search first. Build only what is missing.",
 backup=[("h", "A good test letter"), ("p", f"“Dear supporter, thank you for your gift of {kwd(D.THANKS['amount'])} to {D.THANKS['campaign']}. It pays for about three winter kits: blankets, a heater, food and children's jackets for three families. Your kindness keeps a home warm this winter. Receipt: {D.THANKS['receipt']}. With thanks, Misbah Charity Society.”")],
 answer=[("h", "The five parts to check"), ("ol", SKILL_STEPS), ("note", f"{kwd(D.THANKS['amount'])} ÷ {kwd(D.PER_FAMILY)} is 3.2 kits, so “about three winter kits” is right.")],
 deliverable="A working skill and one tested letter with all five parts.",
 fallback="If the upload is missing or refuses the .zip, turn on Create and edit files in Settings › Capabilities, or create the skill with Claude as in Demo 3.2.",
 hint="The receipt number is the step people forget. Check it first.",
 stretch=["Open the Plugins page (Customize on some accounts), filter by skills and add one skill you would use at work."])

# ===================================================================== LAYER 4 · COWORK, PLUGINS, SCHEDULES
COWORK = [["Folder", "The misbah-receipts-nov-2026 folder: 15 receipt files and a README."],
          ["Task", "Read every receipt. Build an Excel table: date, supplier, campaign code, amount in KWD. Add totals by campaign."],
          ["Flag", "List any receipt with no campaign code, and any receipt that is in the folder twice."],
          ["Mode", "Manual: ask me before you create or delete any file."]]
RC_TABLE = [[D.CODE_NAME[c] + f" ({c})", kwd(D.RC_TOTAL[c])] for c in ("WW", "RI", "OS", "WL")]
demo("d41", day=1, skill="4.1", sec=7, title="Hand Cowork the receipts folder", tool="Claude · Cowork", files=[FILE_RECEIPTS], kind="player",
 setup=["Unzip misbah-receipts-nov-2026.zip into a folder.", "Start a Cowork task: select Cowork in the message box (in the new Claude experience, ask in the chat). Add the folder, or attach the files on the web.", "Set the mode to Manual. Paste the task and approve each step."],
 prompts=[("The task", joined(COWORK[1:]))],
 expected=f"An Excel file of the 14 receipts with a total for each campaign; the largest is Winter Warmth. Two flags: receipt {D.NO_CODE_NO:02d} has no campaign code, and receipt {D.DUP_RECEIPT_NO:02d} is in the folder twice.",
 say="Chat answers a question. Cowork works through a task with steps and files, and asks you before risky steps.",
 point="Chat for questions. Cowork for tasks with steps and files.",
 backup=[("h", "Totals by campaign (14 receipts, the copy counted once)"), tbl(["Campaign", "Total"], RC_TABLE + [["Receipt 09, no code", kwd(D.RC_NOCODE)], ["<b>All receipts</b>", f"<b>{kwd(D.RC_ALL)}</b>"]]),
         ("h", "Flags"), ("ul", [f"Receipt {D.NO_CODE_NO:02d}: food baskets, {kwd(D.RC_NOCODE)}, no campaign code. Ask Fahad which campaign.", f"Receipt {D.DUP_RECEIPT_NO:02d}: in the folder twice ({D.rc_file(4)} and {D.rc_file(4, True)}). Count it once."])],
 fallback="Show the backup. If Cowork is not on the account, run the same task in chat with the 15 files attached.",
 hint="Count the receipts: 15 receipt files (and a README), 14 different receipts.",
 player={"parts": COWORK, "table": [["Campaign", "Total"]] + RC_TABLE, "best": 1,
         "reco": ["<b>Flag 1:</b> one receipt has no campaign code.", "<b>Flag 2:</b> one receipt is in the folder twice. Counted once.", "<b>Made:</b> one Excel file in the folder, after your approval."],
         "control": "Decide the campaign for the receipt with no code before the report goes to the board."})

demo("t41", day=1, skill="4.1", sec=7, title="Hand Cowork a folder", tool="Claude · Cowork", files=[FILE_RECEIPTS], kind="task", hands_on=True, minutes=8, solo="on your own",
 setup=["Unzip misbah-receipts-nov-2026.zip on your laptop.", "Start a Cowork task in the Claude desktop app and add the folder. Choose Manual mode.",
        "Paste the task. Approve each step you agree with.", "Open the Excel file. Check the two flags against the receipts."],
 prompts=[("The task", joined(COWORK[1:]))],
 expected=f"An Excel table of 14 receipts with totals by campaign (Winter Warmth {kwd(D.RC_TOTAL['WW'])}), receipt {D.NO_CODE_NO:02d} flagged for no campaign code and receipt {D.DUP_RECEIPT_NO:02d} flagged as a duplicate.",
 say="Hand over the task, stay in Manual mode, and approve the steps you agree with.",
 point="Chat for questions. Cowork for tasks with steps and files.",
 backup=[("h", "Totals by campaign"), tbl(["Campaign", "Total"], RC_TABLE)],
 answer=[("h", "The two flags"), ("ul", [f"Receipt {D.NO_CODE_NO:02d} ({D.rc_no(D.NO_CODE_NO)}): Fresh Basket Foods, 100 food baskets, {kwd(D.RC_NOCODE)}, no campaign code.", f"Receipt {D.DUP_RECEIPT_NO:02d} ({D.rc_no(D.DUP_RECEIPT_NO)}): Little Coats Trading, {kwd(D.RC_DUP)}, in the folder twice; count it once."]),
         ("h", "Totals (the copy counted once, receipt 09 on its own line)"), tbl(["Campaign", "Total"], RC_TABLE + [["No code (receipt 09)", kwd(D.RC_NOCODE)]])],
 deliverable="The Excel table and the 2 flags, checked against the receipts.",
 fallback="If Cowork is not on the account, attach the 15 files to a chat and run the same task there.",
 hint="One receipt has no campaign code. One receipt is in the folder twice.",
 stretch=["In an account your organization approved, put the unzipped folder on Google Drive and turn on Google Drive in + › Connectors. Then schedule the job for every Thursday at 08:00: Scheduled › New task, or ask in the chat. Or add the Finance plugin."],
 stretch_prompts=[("Schedule it", "Schedule a task for every Thursday at 08:00. Read the new receipts in our Misbah receipts folder on Google Drive, update the table by campaign, and list any receipt with no campaign code or a duplicate. Ask me before you change any file.")])

# ===================================================================== INTEGRATION · YOUR FIRST AI EMPLOYEE
def job(role, jobs, files, rules=f"{D.PHOTO_RULE} Never send, publish or pay: draft only and wait for my approval."):
    return f"You are Misbah Charity Society's AI {role}. Your jobs: {jobs} Use the files in this Project. End every answer with what you checked and what I must check. Rules: {rules}"
ROLES = [("Producer", "write 60-second video scripts and shot lists for our campaigns, and a weekly content plan.", FILE_BRIEF,
          "Write a 60-second video script and shot list for the first delivery day."),
         ("Marketer", "plan campaign posts, write captions in our brand voice, and draft the newsletter.", f"{FILE_BRIEF}, {FILE_BRAND}",
          "Plan five posts for the delivery week, one checked number in each."),
         ("Designer", "design posts and posters as artifacts in our brand colors, and check text against the brand guide.", FILE_BRAND,
          "Design one Instagram post for the first delivery day, as an artifact."),
         ("Accountant", "check donations and receipts, total them by campaign, flag problems, and write a three-line note.", f"{FILE_DON}, the receipts table from Task 4.1",
          "Total donations by campaign, flag any duplicate, and write a three-line note.")]
ROLE_LABEL = {"Producer": "brief · Marketing plugin", "Marketer": "brief, brand guide · Marketing plugin", "Designer": "brand guide · Marketing plugin", "Accountant": "donations, Task 4.1 table · Finance plugin"}
ACC = [["Project", "Misbah AI Accountant: its job description, the donations file and the receipts table from Task 4.1."],
       ["Skills", "The Finance plugin for reconciliation; the donor thank-you skill for letters."],
       ["Connectors", "Google Drive for the receipts folder; Gmail to read only."],
       ["Schedule", "Every Thursday at 08:00: the receipts table and a three-line note. Wait for my approval before anything is sent."]]
demo("d42", day=1, skill="4.2", sec=8, title="The AI accountant, hired", tool="Claude · Project, plugin, schedule", files=[FILE_DON], kind="player",
 setup=["Create a Project for the role. Paste its job description below.", "Add the role's files. Add the plugin or skill it needs.", "Give it the first job. Check the result. Then schedule the weekly job."],
 prompts=[(f"Job description · AI {r}", job(r.lower(), j, f)) for r, j, f, _first in ROLES],
 expected=f"The accountant Project returns donations by campaign ({kwd(D.TOTAL_CONTROL)} after the duplicate {D.DUP_RECEIPT} is removed), flags the duplicate, and writes a three-line note. The weekly task is scheduled for Thursday 08:00.",
 say="An AI employee is the same layers, set up for one job. You stay the manager.",
 point="Same recipe, four jobs. You approve what goes out.",
 backup=[("h", "The accountant's first weekly note"), ("ul", [f"Donations 1 to 24 November: {kwd(D.TOTAL_CONTROL)} after one duplicate receipt ({D.DUP_RECEIPT}) was removed.", f"{D.TOP_CAMPAIGN} leads with {kwd(D.CONTROL[D.TOP_CAMPAIGN])}.", f"Action: confirm the campaign for receipt {D.NO_CODE_NO:02d} ({kwd(D.RC_NOCODE)}) before the board pack."])],
 fallback="Show the backup note. Build the Project live if the room has time.",
 hint="Every job description ends with a rule: draft only, wait for approval.",
 player={"parts": ACC, "table": [["Weekly output", "From", "Who approves"], ["Donations by campaign", FILE_DON, "Fahad"], ["Receipts table and flags", "the receipts folder", "Fahad"], ["Three-line note", "both files", "General Manager"]], "best": 2,
         "reco": ["<b>Job:</b> Project instructions. <b>Binder:</b> its files.", "<b>Procedures:</b> skills and the plugin. <b>Keys:</b> connectors.", "<b>Shift:</b> Thursday 08:00. <b>Manager:</b> you."],
         "control": "Nothing is sent or paid until a person approves it."})

demo("t42", day=1, skill="4.2", sec=8, title="Hire one AI employee", tool="Claude · Projects, skills, plugins", files=[FILE_BRIEF, FILE_BRAND, FILE_DON], kind="task", hands_on=True, minutes=14, solo="on your own",
 setup=["Choose a role. Create a Project named for it, for example Misbah AI Accountant.", "Paste its job description (Demo 4.2 on your prompt sheet) and add its files.",
        "Add the role's plugin from the Plugins page. Run the first job below.", "Check one fact. Write the employee card: role, tools, schedule, approvals."],
 prompts=[(f"{r} · {ROLE_LABEL[r]}", first) for r, _j, _f, first in ROLES],
 expected="One working AI employee Project with a job description, its files and one skill or plugin; a first output with one fact checked; an employee card.",
 say="Same recipe, four jobs. Which job would save your team the most time?",
 point="Hire it like a person: a job, a binder, procedures, keys, a shift and a manager.",
 backup=[("h", "The four role cards (also on the slide and the prompt sheet)"), tbl(["Role", "Files and plugin", "First job"], [(r, ROLE_LABEL[r], first) for r, _j, _f, first in ROLES])],
 answer=[("h", "What a finished AI employee has"), ("ul", ["A Project with the role's job description (with the approval rule).", "The role's files in the Project knowledge.", "The role's plugin added (Marketing, or Finance for the accountant), and one of its commands or skills used.", "A first output with one fact checked.", "An employee card: role, tools, schedule, what a person approves."]),
         ("h", "The first job, for each role"), tbl(["Role", "First job", "Check"], [("Producer", ROLES[0][3], "The script uses the delivery start date and shows no faces"), ("Marketer", ROLES[1][3], f"Each post ends with {D.LINK}"), ("Designer", ROLES[2][3], "The colors match the brand guide"), ("Accountant", ROLES[3][3], f"{kwd(D.TOTAL_CONTROL)} and the duplicate {D.DUP_RECEIPT}; also accept receipt {D.DUP_RECEIPT_NO:02d} in the folder twice and receipt {D.NO_CODE_NO:02d} with no code")])],
 deliverable="A working AI employee Project, its first output checked, and its employee card.",
 fallback="Anyone short of time builds the accountant from the demo and runs its first job.",
 hint="The job description must end with the approval rule.",
 stretch=["Add the role's weekly job as a scheduled task (Scheduled › New task, or ask in the chat), set to wait for your approval."],
 stretch_prompts=[("Weekly job", "Schedule a task on this role's shift from the Four AI employees slide. Do its weekly job with the latest files in this Project. Save the result as a draft and wait for my approval.")])

# ===================================================================== the opener (weak and strong)
SHOWCASE = {
 "eyebrow": "Opener · the same request", "title": "Same tool. Same request. <span class=\"hl\">Two setups.</span>", "tool": "Claude", "file": FILE_BRIEF,
 "weak": WEAK_POST,
 "weak_answer": WEAK_ANSWER,
 "weak_flags": ["Three numbers", "Says “the needy”", "English only"],
 "parts": POST_PARTS,
 "table": [["Brand rule", "Plain chat", "In the Project"], ["One number", "Three", f"One: {D.FAMILIES:,} families"], ["Languages", "English only", "English, then Arabic"], ["Hashtags", "None", "Both"]],
 "strong_answer": [f"<b>This winter, {D.FAMILIES:,} families</b> get a warm home kit, delivered by hand.", "<i>(The same message in Arabic.)</i>", f"#MisbahWinter and our Arabic hashtag. <b>Give a kit:</b> {D.LINK}"],
 "strong_flags": ["Brand voice", "One checked number", "Both languages"],
 "score": [["Follows the brand guide?", "No", "Yes"], ["Numbers to check", "Three", "One"], ["Ready to post?", "Rewrite it", "After one check"]],
 "punch": "The layers decide the answer.", "punch_sub": "Same tool, same request, same file. What changed is what Claude already knows.",
}

AI_DEMOS = [k for k, v in DEMOS.items() if v.get("kind") in ("player", "showcase")]
