# -*- coding: utf-8 -*-
"""Single source of truth for the program shape: the day, blocks, outcomes, cards, MAP test and survey words.
Claude in Layers · CODED × Al-Balagh Al-Mubeen · one-day client session, Thu 26 Nov 2026 (approved handoff, 24 Nov 2026)."""
import data as D
from data import kwd

TITLE = "Claude in Layers"
SUBTITLE = "From chat to your first AI employee"
CODE = "balagh-claude"
BRAND = "CODED × Al-Balagh Al-Mubeen"
TOOL_MODE = "ai"
CLIENT = None                          # the logo has not arrived yet: CODED theme, the client named in text (handoff decision 9)
DATES = "Thursday 26 November 2026"
DAYDATE = {1: "Thursday 26 Nov"}
HOURS = "09:00-13:00"
VENUE = "CODED campus, Legacy room"
TOOL = "Claude"
TOOLS = "Claude: chat, web search, files, artifacts, connectors, memory, Projects, Skills, plugins, Cowork and scheduled tasks"
NDAYS = 1
AUDIENCE = "Al-Balagh Al-Mubeen staff who already use Claude, including the General Manager"
SAMPLE_NOTE = "All sample files are fictional, made for training. Misbah Charity Society is not a real organization."
THRU = "Claude drafts. You check. You approve what goes out."
STORY = "Everything today uses Misbah Charity Society, a fictional Kuwaiti charity in the middle of its winter campaign. One coffee break and a Dhuhr prayer break."

SOURCES = {
 "cowork": ("Get started with Claude Cowork (Claude Help Center)", "https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork"),
 "skills": ("Use skills in Claude (Claude Help Center)", "https://support.claude.com/en/articles/12512180-use-skills-in-claude"),
 "plugins": ("Use plugins in Claude (Claude Help Center)", "https://support.claude.com/en/articles/13837440-use-plugins-in-claude"),
 "pluginspage": ("Manage plugins, skills, and connectors from one Plugins page (Claude Help Center)", "https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page"),
 "google": ("Use Google Workspace connectors (Claude Help Center)", "https://support.claude.com/en/articles/10166901-use-google-workspace-connectors"),
 "artifacts": ("What are artifacts and how do I use them? (Claude Help Center)", "https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them"),
 "schedule": ("Schedule recurring tasks in Claude Cowork (Claude Help Center)", "https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork"),
 "memory": ("Use Claude's chat search and memory (Claude Help Center)", "https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context"),
 "academy": ("Introduction to Claude Cowork (Claude Academy)", "https://academy.claude.com/courses/introduction-to-claude-cowork/getting-set-up"),
}

# the five outcomes (handoff section 2): MAP confidence items and the final survey "I can" items
OUTCOMES = ["I can choose between Claude's trained knowledge and web search, and give Claude PDFs, spreadsheets and screenshots to work from.",
            "I can turn a spreadsheet or an idea into an artifact, such as a dashboard, a calculator or a short deck, and share it.",
            "I can connect my email and calendar to Claude and keep every send and change under my approval.",
            "I can teach Claude once with memory, instructions, a Project and a Skill, and find ready-made skills and plugins.",
            "I can explain what Cowork and scheduled tasks do, and set up an AI employee for one role at my organization."]

DAYS = {
1: {"title": "From chat to your first AI employee", "claim": "Each layer you switch on does more of the work. You stay the manager.",
    "sub": "Four layers of Claude, seven hands-on tasks, and one AI employee for a role at your organization by 12:40.",
    "brief": "The day starts with one request and two setups. Then you work up the layers: chat and artifacts, connectors, memory, Projects and Skills, then Cowork, plugins and schedules. You end by hiring one AI employee for Misbah: a producer, a marketer, a designer or an accountant.",
    "artifact": "One AI employee for one Misbah role, built from every layer of the morning",
    "blocks": [("09:00-09:05", "Welcome and sign-in check", "Claude open and signed in; the desktop app installed"),
               ("09:05-09:15", "Pre-MAP test", "10 minutes. Scan the QR code. It also checks your phone"),
               ("09:15-09:25", "Opener: one request, two setups", "The roadmap: Claude in four layers"),
               ("09:25-09:45", "Layer 1 · Chat: ask, attach, speak", "Web search, files, voice · Task 1.1"),
               ("09:45-10:15", "Layer 1 · Artifacts: from an answer to a tool", "Calculator, dashboard, deck, doc, game · Task 1.3"),
               ("10:15-10:25", "Break", ""),
               ("10:25-10:55", "Layer 2 · Connectors: your email and calendar", "Gmail, Google Calendar, approvals, safe use · Task 2.1"),
               ("10:55-11:15", "Layer 3 · Memory, instructions and Projects", "Where to teach Claude what · Task 3.1"),
               ("11:15-11:40", "Layer 3 · Skills: teach Claude a task once", "Create, upload, find, use with / · Task 3.2"),
               ("11:40-11:55", "Dhuhr prayer break", ""),
               ("11:55-12:15", "Layer 4 · Cowork, plugins and scheduled tasks", "Hand Claude a folder; role plugins; scheduled tasks · Task 4.1"),
               ("12:15-12:40", "Integration · Hire your first AI employee", "Producer, marketer, designer or accountant · Task 4.2"),
               ("12:40-12:55", "Post-MAP test, then the final survey", "Two QR codes · 15 minutes"),
               ("12:55-13:00", "Wrap and close", "Keep exploring on your own")],
    "outcomes": ["Choose between <b>trained knowledge and web search</b>, and give Claude files to work from.",
                 "Turn a spreadsheet or an idea into an <b>artifact</b> you can share.",
                 "Connect <b>email and calendar</b>, with every send under your approval.",
                 "Teach Claude once with <b>memory, instructions, a Project and a Skill</b>, and find ready-made skills and plugins.",
                 "Explain <b>Cowork and scheduled tasks</b>, and set up <b>one AI employee</b> for a role."]},
}

# minutes inside each session (lesson plan): consecutive, and they fill the session
SEGMENTS = {1: [
 ("09:15-09:25", "Opener", [("09:15", 1, "Story: the General Manager's question"), ("09:16", 6, "Demo 1.0: one request, two setups"), ("09:22", 1, "Outcomes and today's map"), ("09:23", 2, "The four layers")]),
 ("09:25-09:45", "Layer 1 · Chat", [("09:25", 1, "Story: the donor's pledge"), ("09:26", 2, "A library book and today's newspaper"), ("09:28", 2, "Next-word widget"), ("09:30", 3, "Demo 1.1: web search"), ("09:33", 1, "Files and voice"), ("09:34", 1, "Two quick checks"), ("09:35", 10, "Task 1.1")]),
 ("09:45-10:15", "Layer 1 · Artifacts", [("09:45", 1, "Story: the board meets Wednesday"), ("09:46", 2, "Artifact"), ("09:48", 2, "Six artifacts"), ("09:50", 3, "Demo 1.2: the calculator"), ("09:53", 4, "Demo 1.3: the dashboard"), ("09:57", 1, "Edit, check, share"), ("09:58", 1, "Quick check"), ("09:59", 15, "Task 1.3"), ("10:14", 1, "Two artifacts on the screen")]),
 ("10:25-10:55", "Layer 2 · Connectors", [("10:25", 1, "Story: 40 unread emails"), ("10:26", 1, "A visitor badge"), ("10:27", 1, "Connector"), ("10:28", 3, "Demo 2.1: Sunday's brief"), ("10:31", 2, "You decide: modes and permissions"), ("10:33", 4, "Safe-use sort"), ("10:37", 1, "Quick check"), ("10:38", 15, "Task 2.1"), ("10:53", 2, "What you caught")]),
 ("10:55-11:15", "Layer 3 · Memory, instructions and Projects", [("10:55", 1, "Story: the same three paragraphs"), ("10:56", 3, "Four places to teach Claude"), ("10:59", 1, "Project"), ("11:00", 3, "Demo 3.1: the campaign Project"), ("11:03", 1, "Quick check"), ("11:04", 8, "Task 3.1"), ("11:12", 3, "Memory: what Claude keeps, and a quick check")]),
 ("11:15-11:40", "Layer 3 · Skills", [("11:15", 1, "Story: 30 letters a week"), ("11:16", 1, "A recipe card"), ("11:17", 1, "Skill"), ("11:18", 2, "Inside a skill"), ("11:20", 3, "Demo 3.2: create a skill"), ("11:23", 2, "Find skills"), ("11:25", 1, "Quick check"), ("11:26", 12, "Task 3.2"), ("11:38", 2, "One letter read aloud")]),
 ("11:55-12:15", "Layer 4 · Cowork, plugins and schedules", [("11:55", 1, "Story: a morning of receipts"), ("11:56", 1, "Cowork"), ("11:57", 3, "Demo 4.1: the receipts folder"), ("12:00", 1, "Plugins"), ("12:01", 1, "Quick check: plugins"), ("12:02", 1, "Scheduled tasks"), ("12:03", 2, "Two quick checks"), ("12:05", 8, "Task 4.1"), ("12:13", 2, "The flags you found")]),
 ("12:15-12:40", "Integration · Your first AI employee", [("12:15", 1, "Story: the General Manager's four roles"), ("12:16", 2, "Hire it like a person"), ("12:18", 2, "Four AI employees"), ("12:20", 3, "Demo 4.2: the AI accountant"), ("12:23", 14, "Task 4.2"), ("12:37", 3, "Show and tell")]),
 ("12:40-12:55", "Post-MAP and survey", [("12:40", 10, "Post-MAP test"), ("12:50", 5, "Final survey")]),
 ("12:55-13:00", "Wrap and close", [("12:55", 2, "Wrap: what you built"), ("12:57", 2, "Keep exploring"), ("12:59", 1, "Close")]),
]}

# ------------------------------------------------------------------ next-word widget: trained knowledge is a prediction
LLM_TREE = {
 "start": {"prompt": "One US dollar is worth about", "opts": [["0.30", 33], ["0.31", 26], ["0.29", 15], ["three", 9], ["the", 8], ["one", 5], ["seven", 1]]},
 "0.30": [["Kuwaiti", 62], ["KWD", 24], ["dinars", 12], ["apples", 1]],
 "0.31": [["Kuwaiti", 60], ["KWD", 26], ["dinars", 12], ["apples", 1]],
 "0.29": [["Kuwaiti", 58], ["KWD", 28], ["dinars", 12], ["apples", 1]],
 "three": [["hundred", 70], ["tenths", 18], ["fils", 10], ["moons", 1]],
 "the": [["same", 44], ["rate", 30], ["price", 24], ["sun", 1]],
 "one": [["third", 52], ["quarter", 26], ["dinar", 20], ["planet", 1]],
 "seven": [["dinars", 50], ["fils", 30], ["rials", 18], ["stars", 1]],
 "_2": [["dinars", 50], ["KWD", 30], ["fils", 18], ["stars", 1]],
 "Kuwaiti": [["dinars.", 84], ["dinar.", 10], ["fils.", 5], ["camels.", 1]],
 "KWD": [["today.", 44], ["in 2025.", 30], ["on average.", 24], ["forever.", 1]],
 "dinars": [["today.", 44], ["in 2025.", 30], ["on average.", 24], ["forever.", 1]],
 "hundred": [["fils.", 82], ["dinars.", 12], ["rials.", 5], ["stars.", 1]],
 "_3": [["today.", 44], ["in 2025.", 30], ["on average.", 24], ["forever.", 1]],
}
LLM = {"tree": LLM_TREE, "foot": "Percentages are illustrative. This is not a real exchange rate."}

# ------------------------------------------------------------------ the five checks before you approve (hub habit band, cheat sheet)
CHECKS = [("The source", "Every fact traces back to a file, a page, an email or a link."),
          ("The numbers", "Check one total against its source before you share."),
          ("The people", "No donor or family names, no faces, no civil IDs."),
          ("The actions", "Sends, new events and payments wait for your approval."),
          ("The place", "Work data only in an account your organization approved.")]

# ------------------------------------------------------------------ safe-use card
SAFE = [("green", "Green: go ahead", "Public or fictional data, and your own drafting.", ["Rewrite a public campaign post", "Practice on the Misbah files", "Explain a Claude feature"]),
        ("amber", "Amber: approved account, approvals on", "Internal work only in an account your organization approved. Remove names first. Keep approvals on.", ["Search your work inbox for supplier emails", "Totals by campaign with donor IDs, no names", "Replies saved as drafts"]),
        ("red", "Red: never in an AI tool", "Personal data of donors or families, case files, civil IDs, bank details. Any send or payment without a person.", ["The donor list with phone numbers", "A family's case file", "Civil IDs or bank details", "Emails sent to donors with no approval"])]
RISKS = [("Wrong facts", "Claude predicts words. A neat answer can be wrong.", "Check every number, date and name against the source."),
         ("Data leaving", "A personal account is not your organization's approved tool.", "Sort the task first: green, amber or red. Follow your policy."),
         ("Actions without you", "Connectors and Cowork can send, create and delete.", "Work in Manual mode. Approve each send, event and file change.")]
SORT_LABELS = {"green": "Green · go ahead", "amber": "Amber · approved account", "red": "Red · never"}

# ------------------------------------------------------------------ cheat sheet and take-home guide (handoff section 5)
CHEAT = [("Part 1 · The four layers", "Claude in layers", "Switch on what the task needs.",
          [("1 · Chat", "Questions, files, voice", "Ask it to search the web (older layout: + › Web search); + › Add files", "One question, one file."),
           ("1 · Artifacts", "Something you put in front of people", "Ask for it, or Output in the message box", "A tool or page you will use again."),
           ("2 · Connectors", "Claude reads your apps with your sign-in", "+ menu: Connectors", "Email, calendar, Drive."),
           ("3 · Teach once", "Memory, instructions, Projects, Skills", "Settings › Your Claude; Projects; + or /", "Anything you would type twice."),
           ("4 · Cowork and schedules", "Claude works through a task, on a time you set", "Cowork; Scheduled › New task, or ask in a chat", "Tasks with steps and files, every week.")],
          "Start at layer 1. Add a layer when the task needs it."),
         ("Part 2 · Six artifacts", "Ask for a tool, not a paragraph", "Name the artifact and the source in the first line.",
          [("Calculator", "A cost or pricing calculator", "Build an artifact: a cost calculator from the attached brief.", "Inputs change the result."),
           ("Dashboard", "Charts from a spreadsheet", "Build an artifact: a dashboard from the attached file, with the row count and total.", "Check one total first."),
           ("Chart and summary", "One chart, three lines", "Make one chart of donations by campaign and three summary lines.", "One idea per chart."),
           ("Slide deck", "Slides you can export", "Make a 5-slide deck for the board from the attached report.", "Exports to PowerPoint or PDF."),
           ("Document", "A doc you edit and share", "Write the volunteer guide as a doc.", "Edit it in place."),
           ("Game or quiz", "A small interactive tool", "Build a 6-question quiz for new volunteers from the report.", "Good for training.")],
          "Artifacts start private. You choose who sees them."),
         ("Part 3 · Where to teach Claude what", "Teach once, in the right place", "Four places, four jobs.",
          [("Memory", "Facts from your chats", "Settings › Your Claude (or Settings › Memory)", "View, edit or delete any item."),
           ("Instructions for Claude", "How you like answers, in every chat", "Settings › Your Claude › Instructions", "Two or three lines."),
           ("Project", "One area of work: rules and files", "Projects › New project", "One campaign, one role."),
           ("Skill", "One method, loaded when the task comes up", "Use: + or /. Make: ask Claude, or upload a .zip (Plugins page › Add; older: Customize › Skills › +)", "The description decides when it runs.")],
          "Who you are: memory. How you like it: instructions. One area: a Project. One method: a Skill."),
         ("Part 4 · The AI employee recipe", "Hire it like a person", "Seven parts, one role.",
          [("Job", "Project instructions", "You are Misbah's AI accountant. Your jobs: ...", "End with the approval rule."),
           ("Binder", "Knowledge files", "The donations file, the receipts", "Only what the role needs."),
           ("Procedures", "Skills", "donor-thank-you", "One skill per repeated method."),
           ("Keys", "Connectors", "Google Drive; Gmail to read", "Read first. Act with approval."),
           ("Starter kit", "A plugin", "Finance, Marketing, Productivity", "Install, then make it yours."),
           ("Shift", "A scheduled task", "Every Thursday at 08:00", "Only after you ran it by hand."),
           ("Manager", "You", "Approve sends, events and payments", "Nothing goes out without you.")],
          "Claude drafts. You check. You approve what goes out.")]
CHEAT_TABLES = [("Settings paths: the new layout and the older one", ["What", "New layout", "Older layout"],
                 [("Instructions for Claude", "Settings › Your Claude › Instructions", "Settings › Account › Instructions for Claude"),
                  ("Memory", "Settings › Your Claude › Your memory", "Settings › Memory"),
                  ("Skills, connectors, plugins", "Plugins, in the sidebar", "Customize, in the sidebar"),
                  ("Files and artifacts switch", "Settings › Capabilities › Create and edit files", "Settings › Capabilities › Code execution and file creation"),
                  ("Start a Cowork task", "Ask in any chat (the new Claude experience)", "Select Cowork in the message box")])]
CHEAT_LEDE = "The four layers, six artifacts to ask for, where to teach Claude what, the AI employee recipe, and the settings paths. On one page."
CHEAT_META = [("list", "4 parts and a table"), ("check", "New and older menus"), ("shield", "Fictional data")]
GUIDE_INTRO = "Keep going on your own, one layer at a time. Start with green tasks. Your organization's AI and data policy comes first."
GUIDE = [("Your first week", ["Build one artifact you will use again: a calculator, a dashboard or a short deck. Check one number before you share it.",
                              "Connect Gmail and Google Calendar only in an account your organization approved for Claude. Ask for Sunday's brief, read only. Keep every send as a draft.",
                              "Create one Project for your main area of work, with its rules and two files."]),
         ("Your first month", ["Turn one method you repeat every week into a Skill. Test it, then share it: from the skill on Team and Enterprise plans, or send the .zip.",
                               "Add one plugin for your role from the Plugins page, and change one of its skills to fit your work.",
                               "Schedule one weekly task you have already run and checked by hand.",
                               "Hire one AI employee per role: producer, marketer, designer, accountant. Each one drafts; a person approves."]),
         ("Keep exploring", ["The Claude Help Center (support.claude.com) explains every feature, step by step.",
                             "Claude Academy (academy.claude.com) has free short courses, including Introduction to Claude Cowork.",
                             "The Plugins page lists ready-made skills, connectors and plugins. Search there before you build.",
                             "Claude Code is the next layer: Claude builds tools and small apps with you."])]
GUIDE_HABIT = "Claude drafts. You check. You approve what goes out. Your organization's AI and data policy comes first."
GUIDE_META = [("home", "Your own work, safely"), ("list", "First week, first month"), ("shield", "Policy first")]

# ------------------------------------------------------------------ MAP test: the same 12 questions before and after (approved handoff, section 6)
CONFIDENCE = OUTCOMES
_Q = lambda q, o, a, topic, where: {"q": q, "o": o, "a": a, "day": 1, "topic": topic, "where": where}
MAP = [
 _Q("Fahad asks Claude for today's USD to KWD rate. Web search is off. What is Claude's answer based on?",
    ["What it learned in training, which may be old", "The live rate, which Claude checks with the banks", "The Central Bank of Kuwait site, read on its own", "A quick search Claude runs in the background"], 0, "Trained knowledge and web search", "Layer 1 · next-word widget and Demo 1.1"),
 _Q(f"Hessa needs total donations by campaign from a {D.DON_ROWS}-row Excel file. Which request gives the most reliable numbers?",
    ["Paste the first 50 rows into the chat and ask for totals", "Send a screenshot of the sheet and ask for totals", "Attach the file and ask Claude to calculate with code", "Describe the columns in words and ask for an estimate"], 2, "Files", "Layer 1 · files and voice, Task 1.1"),
 _Q("Noura wants a winter-kit cost calculator that volunteers can open again next week. What should she ask Claude for?",
    ["A long answer that explains the formula step by step", "An artifact: a small calculator she can share", "A memory entry that stores the unit costs", "A scheduled task that sends her the costs daily"], 1, "Artifacts", "Layer 1 · Artifacts, Demo 1.2"),
 _Q(f"Claude's receipts table shows Winter Warmth KWD {D.RC_DUP:,.0f} above the supplier invoices. What do you do first?",
    ["Ask Claude to recalculate until the totals match", "Change the table by hand to match the invoices", "Send it to Fahad with a note that it is a draft", "Look for a receipt that is counted twice"], 3, "Check before you share", "Layer 1 · Demo 1.3 check; Layer 4 · Task 4.1 flags"),
 _Q("Hessa asks Claude to forward the heater email to the board secretary through the Gmail connector. She works in Manual mode. What happens before it is forwarded?",
    ["Nothing: Claude forwards it as soon as it is ready", "Claude forwards it, because forwarding is read-only", "Claude asks her to approve the forward first", "Claude saves a draft and she forwards it in Gmail"], 2, "Connectors and approvals", "Layer 2 · you decide"),
 _Q("Hessa plans the delivery days with Claude, in an account her organization approved. Which file must she keep out of the chat?",
    ["The booking times for the three community halls", "The list of families with their civil IDs and addresses", "The heater order from the supplier, with its prices", "The campaign brief with the kit and the budget"], 1, "Safe use", "Layer 2 · safe-use sort and card"),
 _Q("Noura's Ramadan Iftar 2027 chats all need the menu rules and the venue list, but her other work does not. Where do they go?",
    ["In a Ramadan Iftar Project, as its knowledge", "In a pinned chat that she goes back to each time", "In her personal settings, so every chat starts with them", "In the first message of each chat, pasted by hand"], 0, "Projects", "Layer 3 · four places to teach Claude"),
 _Q("Fahad writes donor thank-you letters every week with the same five steps. What makes Claude follow those steps when the task comes up?",
    ["A Skill with the steps, an example and a template", "A longer prompt saved in a file on his desktop", "A connector to the shared drive that holds old letters", "A memory entry that says he writes letters weekly"], 0, "Skills", "Layer 3 · Skills"),
 _Q("Noura wants Claude ready for marketing work in one step, with commands such as /campaign-plan. What does she add?",
    ["A new Project named Marketing, with no files yet", "A connector to Instagram from the + menu", "Longer Instructions for Claude in Settings", "The Marketing plugin from the Plugins page"], 3, "Plugins", "Layer 4 · plugins"),
 _Q("Which task fits Cowork better than a normal chat?",
    ["Explaining the meaning of one word in a post", "Sorting 15 receipt files into one Excel table", "Checking the date in one short email from Salem", "Translating one sentence of a post into Arabic"], 1, "Cowork", "Layer 4 · Cowork, Demo 4.1"),
 _Q("You want a donations summary every Sunday at 08:00, even when your laptop is off. What do you set up?",
    ["A memory entry that says “every Sunday at 08:00”", "A Skill named weekly-summary with the steps", "A pinned chat that you open each Sunday", "A scheduled task in Claude for Sunday 08:00"], 3, "Scheduled tasks", "Layer 4 · scheduled tasks"),
 _Q("You set up an AI accountant for Misbah. Which part should stay with a person?",
    ["Reading the receipts in the Google Drive folder", "Sorting the November donations by campaign", "Approving any payment or email that goes out", "Drafting the weekly three-line note"], 2, "AI employees", "Integration · the recipe"),
]
MAP_KEY = " · ".join(f"{i} {'abcd'[q['a']]}" for i, q in enumerate(MAP, 1))
MAP_MIN = 10
MAP_LEDE = {"before": f"{len(MAP)} questions. You take the same test again at 12:40. Not graded. It measures what this morning changes. Phone only: no notes, no search, no AI.",
            "after": f"The same {len(MAP)} questions as this morning. Not graded. Phone only: no notes, no search, no AI. Then scan the second code for the final survey."}

# ------------------------------------------------------------------ the approved slide plan (the validator checks the deck against it)
SLIDES = {1: 66}

# ------------------------------------------------------------------ MAP tests and the final survey (CODED portal; links filled after publishing)
PORTAL = "https://platform.joincoded.com/sv/"
_SL = {"pre": "coded-al-balagh-al-mubeen-claude-in-layers-map-test-pre-day-1",
       "post": "coded-al-balagh-al-mubeen-claude-in-layers-map-test-post-day-1",
       "survey": "coded-al-balagh-al-mubeen-claude-in-layers-final-satisfaction-survey"}
FORMS = {
    "pre":    {"name": "Pre-MAP test", "when": "Day 1 · Thu 26 Nov · 09:05", "slug": _SL["pre"], "url": PORTAL + _SL["pre"], "id": "6bc37002-4c02-4aa4-9c79-64be5b9213ee"},
    "post":   {"name": "Post-MAP test", "when": "Day 1 · Thu 26 Nov · 12:40", "slug": _SL["post"], "url": PORTAL + _SL["post"], "id": "2c1bce62-400a-45aa-b391-05ec7d7b232a"},
    "survey": {"name": "Final satisfaction survey", "when": "Day 1 · Thu 26 Nov · 12:50", "slug": _SL["survey"], "url": PORTAL + _SL["survey"], "id": "402362fa-61c5-43f2-9eb2-3b15ff667498"},
}
FORM_DAY = {1: ["pre", "post", "survey"]}            # one day: the morning test, the closing test and the survey

# ------------------------------------------------------------------ the workshop home (hub)
DAYS[1].update({"cat": "Four layers", "icon": "flask", "tag": "chat · connectors · skills · cowork",
                "bullets": ["Chat and artifacts: web search, files, a calculator and a dashboard", "Connectors, memory, Projects and Skills", "Cowork, plugins, scheduled tasks and your first AI employee"]})
HUB = {
    "headline": ["Claude in Layers", "from chat to your first AI employee"],
    "sub": "A hands-on morning for Al-Balagh Al-Mubeen. Switch on Claude one layer at a time: chat and artifacts, connectors, memory, Projects and Skills, then Cowork, plugins and schedules. End with an AI employee for a real role. You check everything it gives you.",
    "meta": "Claude",
    "program_title": "One morning, four layers, one AI employee.",
    "program_lead": "One fictional Kuwaiti charity, Misbah Charity Society, carries the whole morning: its winter campaign report, donations, inbox and receipts. Every file is made up, so you can practice safely. Bring your laptop with the Claude desktop app and your paid Claude account.",
    "habit_eyebrow": "How the morning runs", "habit_title": "Claude drafts. You check.",
    "habit_text": "Claude drafts. You check. You approve what goes out. Run the five checks before anything leaves Claude:", "habit_list": CHECKS,
    "files_title": "One charity. One story all morning.",
    "takeaway_text": "The cheat sheet: the four layers, six artifacts, where to teach Claude what, the AI employee recipe and the settings paths. The take-home guide says what to do in your first week and your first month. Every prompt from the morning is on the prompt sheet with a COPY button.",
    "map_text": f"{len(MAP)} questions, at 09:05 and again at 12:40. Not graded. It measures what this morning changes. Phone only, no AI. The final survey comes right after the second test.",
    "about": "Claude in Layers is a CODED Professionals session for Al-Balagh Al-Mubeen.",
    "day_tool_note": "Use Claude in the desktop app or at claude.ai, signed in with your own paid account.",
    "stats": [(4, "layers"), (None, "slides"), (7, "hands-on tasks"), (9, "in-slide demos"), (8, "sample files"), (12, "MAP questions")],
}
SHEET = {"howto": ["<b>Watch the trainer first.</b> Then find the same card here.", "<b>Download the file</b> on the card. In Claude, attach it with the + button.",
                   "Click <b>COPY</b>, paste the prompt into Claude, then press <code>Enter</code>.", "<b>Check the answer</b> against the file before you trust it: numbers, dates, names and actions."],
         "note": "<b>Answers vary.</b> Claude may word things differently from the trainer's screen. That is normal, and it is why we check. Use only the fictional files here, or green tasks from your own work."}
TASK_FALLBACK_LINE = "Claude slow, or a feature missing on your account? Continue from the backup."
REWRITE_LABEL = "Examples"

# ------------------------------------------------------------------ the safe-use card
CARD = {"lede": "<b>Before you connect an app or paste anything, sort the task.</b> Your organization's AI and data policy always comes first.",
        "meta": [("shield", "Green, amber, red"), ("check", "Three risks"), ("pin", "Policy first")],
        "cards": SAFE, "risks_title": "Three risks, three habits", "risks_head": ["Risk", "What it looks like", "The habit"], "risks": RISKS,
        "policy_title": "Your organization's policy comes first",
        "policy": ["Ask your General Manager or IT which AI accounts and connectors your organization approves.", "If there is no approved account for work data, amber becomes red.",
                   "Donor and family data stays red, in any account.", "When you are not sure, treat the task as red and ask first."]}

# ------------------------------------------------------------------ trainer pages
LESSON_INTRO = f"CODED Professionals client session for Al-Balagh Al-Mubeen Charity. {AUDIENCE}; they know prompting and asked for Claude's features in depth. No prompting lesson. Story: Misbah Charity Society (fictional)."
RUNBOOK_PREFLIGHT = ["Presenting laptop: Claude desktop app updated, signed in to a paid account. The message box shows Cowork (or the new Claude experience).",
                     "Settings › Capabilities: Create and edit files is on (skills and artifacts need it). Web search is on (older layout; the new Claude experience has no toggle).",
                     "The day before: upload misbah-donor-thanks-skill.zip from the Plugins page, note the exact button labels for Task 3.2, then delete the skill again. If the new page refuses a skill .zip, teach the fallback: create the skill with Claude (Demo 3.2).",
                     "Run the Demo 1.2 calculator prompt once with the campaign brief and keep the real artifact open, to show next to the slide.",
                     "The CODED training Google account is connected to Gmail and Google Calendar, with the fictional inbox and Sunday 29 November's calendar loaded for Demo 2.1.",
                     "The Misbah Winter Campaign Project exists with the Task 3.1 instructions, the brand guide and the brief (the opener uses it). No donor-thank-you skill on the laptop: it is uploaded live on the find-skills slide. The receipts folder is unzipped on the desktop.",
                     "All 8 sample files are on the laptop and on a USB stick. Open this runbook, the backups and the answer key on your own screen.",
                     "Test the projector with the deck at full screen (F). Step through one player and press R to reset it. Check the calculator slide responds."]
FACILITATOR = [
 ("open", "Before the session", "confirm by Wednesday 25 November", [("ul", [
    "Send the joining note through Yousif: bring a charged laptop with the Claude desktop app installed and signed in to a paid Claude plan (Pro, Max or Team).",
    "Ask Yousif to confirm with Al-Balagh which Claude accounts are approved for work email. Only approved accounts connect Gmail in Task 2.1; everyone else uses the fictional inbox file. On a Team plan, an owner must also turn on: the Google connectors; code execution and file creation, and Skills (Organization settings › Plugins & skills); and web search (Organization settings › Capabilities).",
    "This room left AI Essentials because of too much prompting. Do not teach prompting. Every block is a Claude feature, shown, then done.",
    "The three portal surveys are not linked to a cohort (there is none for this session). Ops can link one later."])]),
 ("room", "Room and laptops", "pre-flight", [("ol", [
    "Legacy room. Three to six people: one table facing the screen; everyone works solo.",
    "Wi-Fi name and password on the board before 08:45.",
    "09:00: every laptop opens Claude and signs in. The pre-MAP QR at 09:05 is also the phone check.",
    "Print one safe-use card and one cheat sheet per person.",
    "The General Manager is in the room. Ask him which role he wants his first AI employee for before Task 4.2."])]),
 ("failplan", "If something fails", "Plan A, B, C", [("table", [["What fails", "Plan B", "Plan C"],
    ["Claude is slow or busy", "Keep talking. Use the prompt player slide.", "Show the backup result."],
    ["A feature is missing on an account (Cowork, plugins, schedules)", "Pair with the trainer's laptop for that task.", "Show the player and the backup; give the steps for later."],
    ["Gmail will not connect (admin settings)", "Use misbah-inbox-and-calendar.pdf in the chat.", "Trainer demo on the training account."],
    ["File upload fails", "Try again in a new chat.", "Trainer demo; participants read the backup."],
    ["No internet", "Phone hotspot.", "The decks, backups and files work offline."]])]),
]

# ------------------------------------------------------------------ the browser lab: one page; answers only in the staff lab key
LABS = {
 1: {"title": "Check the dashboard before the board sees it", "intro": "Work through the steps after Task 1.3, or at home. Your done marks stay in this browser.",
     "steps": [
        {"title": "Open the donations file", "do": ["Download misbah-donations-nov-2026.xlsx and open it in Excel.", "Find the Donations sheet and the Control totals sheet."],
         "hint": "The Control totals sheet holds the totals the accounts team checked.", "check": {"kind": "note", "label": "How many donation rows does the Donations sheet have?"},
         "answer": [("p", f"The Donations sheet has {D.DON_ROWS} rows, 1 to {D.DON_LAST} November. The Control totals sheet has one total per campaign.")]},
        {"title": "Compare the campaign totals", "do": ["Add up each campaign with a PivotTable, or ask Claude with code.", "Compare each total with the Control totals sheet."],
         "hint": "Only one campaign is different.", "check": {"kind": "flag", "label": "Type the campaign whose total is too high", "answer": "Winter Warmth"},
         "answer": [("p", f"Winter Warmth is {kwd(D.DIFF)} too high: {kwd(D.EXPORT['Winter Warmth'])} in the export against {kwd(D.CONTROL['Winter Warmth'])} on the Control totals sheet.")]},
        {"title": "Find the row behind it", "do": ["Sort the Donations sheet by receipt number.", "Look for a receipt number that appears twice."],
         "hint": f"Look at the large bank transfers on {D.DUP_DAY} November.", "check": {"kind": "flag", "label": "Type the receipt number that appears twice", "answer": D.DUP_RECEIPT},
         "answer": [("p", f"Receipt {D.DUP_RECEIPT} ({kwd(D.DUP_AMOUNT)}, bank transfer, Winter Warmth) is on sheet rows {D.DUP_SHEET_ROWS[0]} and {D.DUP_SHEET_ROWS[1]}. Count it once.")]},
     ]},
}

# ------------------------------------------------------------------ the portal survey words (surveys.py); the folder id is set when the folder is made
SURVEY = {
 "program": "CODED × Al-Balagh Al-Mubeen", "program_ar": "Claude في طبقات", "client": "Al-Balagh Al-Mubeen Charity",
 "subtitle": {"en": "CODED × Al-Balagh Al-Mubeen", "ar": "CODED × جمعية البلاغ المبين"},
 "folder": "9d0ed253-6ffa-4591-aa6b-3c95f22972ec", "name_prefix": "CODED × Al-Balagh Al-Mubeen", "note": "", "test_min": 10, "cohort": "",
 "day_ar": {1: "من المحادثة إلى أول موظف ذكاء اصطناعي"},
 "confidence_ar": ["أستطيع الاختيار بين معرفة Claude المدرَّبة والبحث في الويب، وأن أعطي Claude ملفات PDF وجداول ولقطات شاشة ليعمل منها.",
                   "أستطيع تحويل جدول بيانات أو فكرة إلى Artifact، مثل لوحة بيانات أو حاسبة أو عرض قصير، ومشاركته.",
                   "أستطيع ربط بريدي الإلكتروني وتقويمي بـ Claude، مع إبقاء كل إرسال وتغيير بموافقتي.",
                   "أستطيع تعليم Claude مرة واحدة عبر الذاكرة والتعليمات والمشروع (Project) والمهارة (Skill)، وأن أجد مهارات وإضافات جاهزة.",
                   "أستطيع شرح ما يفعله Cowork والمهام المجدولة، وإعداد موظف ذكاء اصطناعي لدور واحد في مؤسستي."],
 "map_ar": [
  ("يسأل فهد Claude عن سعر صرف الدولار الأمريكي مقابل الدينار الكويتي اليوم، والبحث في الويب متوقف. على ماذا تعتمد إجابة Claude؟",
   ["على ما تعلّمه أثناء التدريب، وقد يكون قديماً", "على السعر المباشر الذي يتحقق منه Claude لدى البنوك", "على موقع بنك الكويت المركزي، يقرؤه من تلقاء نفسه", "على بحث سريع يجريه Claude في الخلفية"]),
  (f"تحتاج حصة إلى إجمالي التبرعات لكل حملة من ملف Excel فيه {D.DON_ROWS} صفاً. أي طلب يعطي أدق الأرقام؟",
   ["لصق أول 50 صفاً في المحادثة وطلب الإجماليات", "إرسال لقطة شاشة للورقة وطلب الإجماليات", "إرفاق الملف وطلب الحساب من Claude باستخدام الكود", "وصف الأعمدة بالكلمات وطلب تقدير"]),
  ("تريد نورة حاسبة لتكلفة حقيبة الشتاء يفتحها المتطوعون مرة أخرى الأسبوع القادم. ماذا تطلب من Claude؟",
   ["إجابة طويلة تشرح المعادلة خطوة بخطوة", "عنصر Artifact: حاسبة صغيرة يمكنها مشاركتها", "إدخالاً في الذاكرة يحفظ تكاليف الوحدات", "مهمة مجدولة ترسل لها التكاليف يومياً"]),
  (f"يُظهر جدول الإيصالات الذي أعدّه Claude أن حملة Winter Warmth أعلى بمقدار {D.RC_DUP:,.0f} دينار من فواتير الموردين. ماذا تفعل أولاً؟",
   ["أطلب من Claude إعادة الحساب حتى تتطابق الإجماليات", "أعدّل الجدول يدوياً ليطابق الفواتير", "أرسله إلى فهد مع ملاحظة أنه مسودة", "أبحث عن إيصال محسوب مرتين"]),
  ("تطلب حصة من Claude إعادة توجيه رسالة الدفايات إلى سكرتير مجلس الإدارة عبر موصل Gmail، وهي تعمل في الوضع اليدوي (Manual). ماذا يحدث قبل إعادة التوجيه؟",
   ["لا شيء: يعيد Claude توجيهها فور جاهزيتها", "يعيد Claude توجيهها، لأن إعادة التوجيه للقراءة فقط", "يطلب منها Claude الموافقة على إعادة التوجيه أولاً", "يحفظ Claude مسودة وتعيد هي توجيهها من Gmail"]),
  ("تخطط حصة لأيام التوزيع مع Claude، في حساب وافقت عليه مؤسستها. أي ملف يجب أن تُبقيه خارج المحادثة؟",
   ["مواعيد حجز القاعات المجتمعية الثلاث", "قائمة الأسر بأرقامها المدنية وعناوينها", "طلب الدفايات من المورّد، مع أسعاره", "موجز الحملة بمحتويات الحقيبة والميزانية"]),
  ("كل محادثات نورة عن حملة Ramadan Iftar 2027 تحتاج قواعد قائمة الطعام وقائمة القاعات، لكن عملها الآخر لا يحتاجها. أين تضعها؟",
   ["في مشروع (Project) لحملة Ramadan Iftar، كملفات معرفة", "في محادثة مثبّتة تعود إليها كل مرة", "في إعداداتها الشخصية، لتبدأ بها كل محادثة", "في أول رسالة من كل محادثة، بلصقها يدوياً"]),
  ("يكتب فهد رسائل شكر للمتبرعين كل أسبوع بالخطوات الخمس نفسها. ما الذي يجعل Claude يتبع هذه الخطوات عندما تأتي المهمة؟",
   ["مهارة (Skill) فيها الخطوات ومثال وقالب", "طلب أطول محفوظ في ملف على سطح المكتب", "موصل إلى المجلد المشترك الذي يضم الرسائل القديمة", "إدخال في الذاكرة يقول إنه يكتب رسائل كل أسبوع"]),
  ("تريد نورة تجهيز Claude لأعمال التسويق بخطوة واحدة، مع أوامر جاهزة مثل /campaign-plan. ماذا تضيف؟",
   ["مشروعاً جديداً باسم Marketing، دون ملفات بعد", "موصلاً إلى Instagram من قائمة +", "تعليمات أطول لـ Claude في الإعدادات", "إضافة Marketing من صفحة Plugins"]),
  ("أي مهمة تناسب Cowork أكثر من المحادثة العادية؟",
   ["شرح معنى كلمة واحدة في منشور", "فرز 15 ملف إيصال في جدول Excel واحد", "التحقق من التاريخ في رسالة قصيرة واحدة من سالم", "ترجمة جملة واحدة من منشور إلى العربية"]),
  ("تريد ملخصاً للتبرعات كل يوم أحد الساعة 08:00، حتى وحاسوبك مغلق. ماذا تُعدّ؟",
   ["إدخالاً في الذاكرة يقول «كل أحد الساعة 08:00»", "مهارة (Skill) باسم weekly-summary فيها الخطوات", "محادثة مثبّتة تفتحها كل أحد", "مهمة مجدولة في Claude ليوم الأحد الساعة 08:00"]),
  ("أعددت محاسباً بالذكاء الاصطناعي لجمعية المصباح. أي جزء يجب أن يبقى مع شخص؟",
   ["قراءة الإيصالات في مجلد Google Drive", "فرز تبرعات نوفمبر حسب الحملة", "الموافقة على أي دفعة أو رسالة تخرج", "كتابة مسودة الملاحظة الأسبوعية من ثلاثة أسطر"]),
 ],
 "hands_on": ("The hands-on parts, such as the seven tasks, the Misbah sample files and the prompt sheet, helped me apply what I learned.",
              "ساعدتني الأجزاء التطبيقية، مثل المهام السبع وملفات المصباح التجريبية وورقة الأوامر، على تطبيق ما تعلّمته."),
 "materials": ("The workshop website, the cheat sheet, the safe-use card and the take-home guide were clear and useful.",
               "كانت مواد ورشة العمل (الموقع وورقة المراجعة السريعة وبطاقة الاستخدام الآمن ودليل ما بعد ورشة العمل) واضحةً ومفيدة."),
 "logistics": ("The venue, the timing and access to Claude worked well for me.", "كان المكان والتوقيت وإمكانية الوصول إلى Claude مناسباً لي."),
 "relevance": ("The content was high quality and relevant to my work at Al-Balagh Al-Mubeen.", "كان المحتوى عالي الجودة وذا صلة بعملي في جمعية البلاغ المبين."),
}
