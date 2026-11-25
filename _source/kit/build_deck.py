# -*- coding: utf-8 -*-
"""The slides of Claude in Layers (one day): the kit's slide source. The engine's deck.py renders every call.
One helper call is one slide. Every note is written as N(...) parts and never repeats the slide text.
The engine adds the close slide from CLOSE."""
from deck import *
import wk
import content as C
import content_demos as CD
import data as D
from data import kwd

SECTIONS = {1: [("Opening", "g-mark", ["open"]), ("Layer 1", "g-code", ["l1", "l1c", "l1b"]), ("Layer 2", "g-frame", ["l2"]),
                ("Layer 3", "g-code", ["l3", "l3b"]), ("Layer 4", "g-impact", ["l5"]), ("Close", "g-progress", ["c6", "close"])]}
FLOW = {1: (["Chat", "Cowork", "Artifacts", "Connectors", "Projects", "Skills", "AI employee"], {"l1": 0, "l1c": 1, "l1b": 2, "l2": 3, "l3": 4, "l3b": 5, "l5": 6})}
COVER_NOTES = {1: N(do="Welcome. Introduce yourself and CODED in one minute. Name the reason for today: Claude's features, in depth, with your hands on the keys.",
                    more=["Housekeeping: coffee at 10:30, Dhuhr break at 11:40. Prayer room and toilets.",
                          "Sign-in check: Claude desktop app open and signed in on every laptop. Help anyone who is still on the free plan or the web only."],
                    say="This morning is about Claude, not about prompting. You already write good prompts.",
                    silent="ask the General Manager which feature he most wants to see working today.")}
OUTCOMES_NOTES = {1: N(do="Read the outcomes quickly. Ask which one each person came for.", expect="Most pick the AI employee or the connectors.",
                       say="Five things you will do yourself before 13:00, on fictional files.", silent="say which one you would pick for their team, and why.")}
ROAD = {1: {"title": "One charity. <span class=\"hl\">Four layers. One morning.</span>",
            "n": N(do="Point to the four layers on the map and the two breaks. The cup button starts the break clock.",
                   say="This is the roadmap for the whole morning. Nothing on it is about prompting.", silent="ask which block they expect to use first at work.")}}
CLOSE = {1: {"big": "Claude drafts. <span class=\"hl\">You approve.</span>", "next": "Thank you, Al-Balagh Al-Mubeen. One layer at a time, starting this week.",
             "n": N(do="Thank the room. Point to the take-home guide and the cheat sheet on the site.", more=["Ask the General Manager for one line of feedback before he leaves."],
                    say="Pick one layer you will switch on at work this week.")}}

# ------------------------------------------------------------------ the artifact on the calculator slide (Demo 1.3): a working tool, built from data.py
def _calc_html():
    rows = "".join(f'<tr data-u="{c}"><td><label><input type="checkbox" checked> {i}</label></td><td>{c:.3f}</td>'
                   f'<td><input class="mc-q" type="number" min="0" max="9" value="{q}" aria-label="{i} per family"></td><td class="mc-line">{c * q:.3f}</td></tr>' for i, c, q in D.KIT)
    rows += f'<tr class="mc-fixed"><td>Delivery</td><td>{D.DELIVERY_COST:.3f}</td><td>1</td><td>{D.DELIVERY_COST:.3f}</td></tr>'
    return (f'<div class="mc-calc" data-budget="{D.BUDGET}" data-del="{D.DELIVERY_COST}">'
            f'<div class="mc-top"><label class="mc-fam">Families <input type="number" min="0" step="10" value="{D.FAMILIES}" data-k="fam" aria-label="Families"></label>'
            f'<span class="mc-note">Unit costs from the campaign brief · budget {kwd(D.BUDGET)}</span></div>'
            f'<table class="mc-t"><thead><tr><th>In the kit</th><th>Unit (KWD)</th><th>Per family</th><th>Line (KWD)</th></tr></thead><tbody>{rows}</tbody></table>'
            f'<div class="mc-out"><div><span>Cost per family</span><b data-o="per">{D.PER_FAMILY:,.3f}</b></div>'
            f'<div><span>Total for all families</span><b data-o="tot">{D.CAMPAIGN_COST:,.3f}</b></div>'
            f'<div><span>Budget left (minus = over)</span><b data-o="left">{D.LEFT:,.3f}</b></div></div></div>')
CALC_HTML = _calc_html()
EXTRA_CSS = """
.mc-calc{width:100%;max-width:1060px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.15);border-radius:16px;padding:14px 20px;font-size:16px}
.mc-top{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:8px}
.mc-fam{font-weight:700;display:flex;align-items:center;gap:10px}
.mc-calc input[type=number]{width:96px;font:inherit;font-weight:700;color:#fff;background:rgba(0,17,47,.7);border:1px solid rgba(255,255,255,.25);border-radius:8px;padding:4px 8px}
.mc-calc input.mc-q{width:64px}
.mc-calc input[type=checkbox]{width:18px;height:18px;accent-color:var(--cd-accent);vertical-align:-3px}
.mc-note{font-family:var(--cd-font-mono);font-size:12px;color:rgba(255,255,255,.72)}
.mc-t{width:100%;border-collapse:collapse}
.mc-t th{font-family:var(--cd-font-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.72);text-align:left;padding:4px 8px;border-bottom:1px solid rgba(255,255,255,.15)}
.mc-t td{padding:4px 8px;border-bottom:1px solid rgba(255,255,255,.08)}
.mc-t td:nth-child(n+2),.mc-t th:nth-child(n+2){text-align:right}
.mc-t tr.off td{opacity:.45}
.mc-out{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:10px}
.mc-out div{background:rgba(255,255,255,.06);border-radius:12px;padding:8px 12px}
.mc-out span{display:block;font-size:12px;font-family:var(--cd-font-mono);color:rgba(255,255,255,.72)}
.mc-out b{font-size:26px;color:var(--cd-accent);font-variant-numeric:tabular-nums}
.mc-out b.neg{color:#F84B4B}
/* the final survey slide: text on the left, the portal QR on the right (no MAP test in this session) */
#c6survey .cd-eyebrow,#c6survey .cd-h1,#c6survey .wk-lead,#c6survey .wk-map-timer{max-width:56%}
#c6survey .wk-lead{position:relative}
#c6survey .wk-survey-qr{position:absolute;left:calc(100% + clamp(48px,7vw,120px));top:50%;transform:translateY(-50%);margin:0;width:max-content}
#c6survey .wk-survey-qr .wk-qr-code{width:clamp(200px,20vw,300px)}
"""
EXTRA_JS = """
(function(){function f(n){var s=Math.abs(n).toFixed(3).split('.');s[0]=s[0].replace(/\\B(?=(\\d{3})+(?!\\d))/g,',');return (n<0?'-':'')+s.join('.');}
document.querySelectorAll('.mc-calc').forEach(function(c){var B=+c.dataset.budget,Dl=+c.dataset.del;
 function run(){var fam=+c.querySelector('[data-k=fam]').value||0,per=Dl;
  c.querySelectorAll('tr[data-u]').forEach(function(r){var on=r.querySelector('input[type=checkbox]').checked,q=+r.querySelector('.mc-q').value||0,l=on?(+r.dataset.u)*q:0;
   r.querySelector('.mc-line').textContent=f(l);r.classList.toggle('off',!on);per+=l;});
  var tot=per*fam,left=B-tot,L=c.querySelector('[data-o=left]');
  c.querySelector('[data-o=per]').textContent=f(per);c.querySelector('[data-o=tot]').textContent=f(tot);L.textContent=f(left);L.classList.toggle('neg',left<0);}
 c.addEventListener('input',run);c.addEventListener('change',run);c.addEventListener('keydown',function(e){e.stopPropagation();});run();});})();
"""

# ------------------------------------------------------------------ the final survey slide (no MAP test: Aya, 24 Nov 2026). Kit HTML: the portal QR with its name and time
_SV = C.FORMS["survey"]
SURVEY_LEAD = ("Scan the code with your phone. It takes about five minutes, and it is not a test. "
               f'<a class="wk-qr-card wk-survey-qr" href="{_SV["url"]}" target="_blank" rel="noopener">{wk.qr_svg(_SV["url"], label=_SV["name"])}'
               f'<span class="wk-qr-lbl">{_SV["name"]}</span> <span class="wk-qr-when">{_SV["when"]}</span></a>')

# ------------------------------------------------------------------ the day
TASK_N = N(do="Start the timer. Walk the room. Ask each person what they found so far.")
def day1():
    opener = [timer_slide("setup", "open", "Welcome · 09:00", "Ten minutes: <span class=\"hl\">get ready to build.</span>",
        "Open the Claude desktop app and sign in with your paid account. Open the workshop home and download the eight Misbah sample files. Keep the prompt sheet open in a browser tab.", 10,
        n=N(do="Start the timer. Walk the room and check every laptop: Claude signed in, the desktop app open, the files downloaded.", say="Everything today happens on your own laptop, so we set it up first.",
            fallback="If someone cannot sign in, pair them with a neighbor for the morning and fix the account at the break.", silent="open the workshop home on the screen and point to the sample files.",
            more=["Check the plan on each laptop: Cowork and scheduled tasks need a paid plan."], time="09:00-09:10"))]
    s = opening(1, opener=opener)
    s.append(scene("o_layers", "open", "Today · the roadmap", "Claude in <span class=\"hl\">four layers.</span>",
        "Each layer gives Claude something a new colleague needs: the conversation and its own tasks, then keys to your apps, then training, then a shift of its own. Today you switch them on, one by one.",
        "Chat and Cowork · Connectors · Teach once · Schedules.",
        [{"ground": 268}, {"laptop": (240, 268), "tone": "dim"}, {"person": (86, 268), "tone": "hot", "label": "You, the manager", "anim": "nod"},
         {"pill": "1 · Chat, Cowork, artifacts", "at": (240, 196), "tone": "hot", "delay": 0}, {"pill": "2 · Connectors", "at": (240, 152), "tone": "hot", "delay": 1.5},
         {"pill": "3 · Memory, Projects, Skills", "at": (240, 108), "tone": "hot", "delay": 3}, {"pill": "4 · Scheduled tasks", "at": (240, 64), "tone": "hot", "delay": 4.5},
         {"pill": "Your AI employee", "at": (240, 22), "tone": "ok", "delay": 6}],
        n=N(do="Point to each layer as it lights up. Then point to the top: the AI employee is where the morning ends.", expect="Most people already use layer 1 every day.", time="09:10-09:13",
            silent="ask which layer they already use every day (layer 1).", say="Each layer is one block this morning. The AI employee at the top uses all four.")))

    # Layer 1 · Chat
    s.append(story("l1story", "l1", "Layer 1 · Chat", "Sunday 22 November, 09:10",
        "A donor in the US pledges <b>USD 5,000</b> to the winter campaign. Fahad asks Claude what that is in KWD. The answer comes in one second, <b>with a rate and no date.</b>",
        "Fast is not <span class=\"hl\">the same as current.</span>", "Choose web search or trained knowledge, and give Claude your files.",
        n=N(do="Ask: would you put that amount on the donor's receipt?", expect="No, not without checking the rate.", silent="ask where they would check a rate today.", time="09:13-09:38")))
    s.append(scene("l1scene", "l1", "Layer 1 · the picture", "A library book and <span class=\"hl\">today's newspaper.</span>",
        "A library book was printed on one date. It knows nothing after that. Today's newspaper knows this morning, and it names its sources.",
        "Trained knowledge = the book. Web search = the newspaper.",
        [{"ground": 268}, {"doc": (130, 230), "tone": "dim", "label": "Trained knowledge"}, {"doc": (350, 230), "tone": "hot", "label": "Web search, today", "anim": "pop"},
         {"person": (240, 268), "label": "Fahad", "anim": "bob"}, {"pill": "Stops on a date", "at": (130, 120), "tone": "bad", "delay": 0.5}, {"pill": "Today, with sources", "at": (350, 120), "tone": "ok", "delay": 2}],
        n=N(do="Ask: which one would you use for a rate, a law or a price?", expect="The newspaper: anything that changes.", silent="say it yourself: anything that changes needs the newspaper.",
            say="For ideas and drafting, the book is fine. For anything that changes, switch on the newspaper.")))
    s.append(llmslide("l1llm", "l1", "Layer 1 · live widget", "Trained knowledge <span class=\"hl\">is a prediction.</span>",
        "Without web search, Claude writes the most likely next word from what it learned. A rate is a word too.", "It predicts a <b>likely</b> number. It does not look up <b>today's</b> number.",
        n=N(do="Read the start of the sentence. Ask the room which word comes next and click it.", more=["Click Pick the top word once. Then Start again and pick seven: the sentence still sounds sure.", "The percentages are made up for the demo."],
            say="Nothing in this sentence was looked up. That is why the rate had no date.", silent="ask one person to choose for the room.", time="2 min")))
    s.append(player("l1pp", "l1", "d11", n=N(time="3 min", more=["Older layout: the Web search switch is in the + menu. The new Claude experience has no switch: Claude searches when it helps, or when you ask."])))
    s.append(tslide("l1files", "l1", "Layer 1 · files and voice", "Give Claude <span class=\"hl\">the source, not a summary of it.</span>", ["Input", "How", "What Claude does", "Use it for"],
        [["<b>PDF</b>", "+ › Add files", "Reads the text and the pages", "Reports, contracts, minutes"],
         ["<b>Excel or CSV</b>", "+ › Add files", "Runs code to calculate", "Totals, checks, charts"],
         ["<b>Screenshot or photo</b>", "+ › Add files, or paste", "Reads the text and the layout", "Posts, forms, whiteboards"],
         ["<b>Microphone</b>", "The mic in the message box", "Types what you say (dictation)", "Long requests"],
         ["<b>Voice mode</b>", "The sound-wave icon, best on the phone", "A spoken conversation", "Thinking aloud, on the move"]],
        "Microphone: you speak, Claude reads. Voice mode: you talk together.",
        n=N(do="Point to the Excel row: code calculates, so pasted rows are never needed. Then the last two rows: one types, one talks.",
            expect="Someone asks about Arabic voice: the spoken language is set in Settings, under Voice.", silent="ask who has used voice mode in the car.",
            more=["Show voice mode for 30 seconds on your phone, on the projector camera or held up: ask one question about the campaign aloud."])))
    s.append(check("l1chk", "l1", "Fahad's answer gave a rate <b>with no date and no link</b>. What does that tell him?",
        [("It came from training, so it may be old", 1, "Right. No date and no source: trained knowledge. Ask Claude to search the web."),
         ("It is today's rate from the bank", 0, "Today's rate comes with a date and a source you can open."),
         ("Claude made an error in the math", 0, "The math may be fine. The rate itself may be old.")]))
    s.append(check("l1fchk", "l1", "Hessa wants to talk through the delivery plan with Claude <b>while she walks to the hall</b>. What fits?",
        [("The microphone in the message box", 0, "The microphone types what you say. Claude does not talk back."),
         ("Voice mode: the sound-wave icon on her phone", 1, "Right. A spoken conversation, made for thinking aloud on the move."),
         ("A photo of her notes, sent later", 0, "That works for a document, not for a conversation.")]))
    s.append(task("l1task", "l1", "t11", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.", time="15 min work. No share-out: as the next block starts, ask who found the two errors in the post.")))

    # Layer 1 · Cowork, right after chat: see the difference
    s.append(story("cwstory", "l1c", "Layer 1 · Cowork", "Thursday 26 November, 08:00",
        "Before each board pack, Fahad sorts the month's receipts by campaign. <b>Fifteen files, one spreadsheet, the whole morning.</b> The board pack is due Monday at 12:00.",
        "Hand over the task. <span class=\"hl\">Keep the decision.</span>", "Give Cowork a folder, then compare it with the chat you just used.",
        n=N(do="Ask: what folder do you open every week to do the same thing?", expect="Receipts, invoices, reports.", silent="say Fahad's receipts are today's folder.", time="09:38-10:00")))
    s.append(term("cwterm", "l1c", "Layer 1 · the idea", "Hand over a task, <span class=\"hl\">not a question.</span>", "Cowork",
        "<b>Cowork</b> is Claude working through a task with several steps: it reads a folder, makes a plan, creates Excel, Word or slides, and asks you before risky steps. In the new Claude experience, chat and Cowork share one message box.",
        "Chat: you ask, Claude answers…", "…Cowork: you hand over a task, <b>Claude delivers files</b>.", "Older accounts: select Cowork in the message box. New experience: ask in any chat.",
        n=N(do="Show the message box on the presenting laptop: Chat and Cowork, or the merged box.", expect="Some have the new experience, some the toggle. Both work.",
            more=["Cowork needs a paid plan. Local folders need the desktop app open."], silent="ask whose laptop shows the Cowork option.")))
    s.append(tslide("cwdiff", "l1c", "Layer 1 · chat or Cowork", "The same files, <span class=\"hl\">two ways to work.</span>", ["", "Chat (Task 1.1)", "Cowork (Task 1.2)"],
        [["<b>You give it</b>", "A question and a few files", "A task and a whole folder"],
         ["<b>It works</b>", "One answer in the chat", "A plan, then every file, step by step"],
         ["<b>You get</b>", "Text to read and copy", "A finished file: Excel, Word or slides"],
         ["<b>You approve</b>", "You read the answer", "Risky steps, such as creating or deleting a file"],
         ["<b>Best for</b>", "Questions and drafts", "Tasks with steps and many files"]],
        "Chat answers. Cowork delivers. You stay the manager.",
        n=N(do="Put Task 1.1 next to the receipts job. Ask: which one would you hand to a colleague and then walk away?", expect="The receipts job.",
            silent="say: the chat was a question; the receipts are a task.", more=["In the new Claude experience, both start from the same message box."])))
    s.append(player("cwpp", "l1c", "d41", n=N(time="3 min")))
    s.append(check("cwchk", "l1c", "Fahad has a folder of receipts to sort into one Excel table. <b>He has never done it with Claude.</b> Where does he start?",
        [("A scheduled task for every Thursday", 0, "Schedule only a job you have run and checked by hand."),
         ("A chat, pasting each receipt one by one", 0, "That works for one file. A folder with steps is a Cowork task."),
         ("A Cowork task on the folder, in Manual mode", 1, "Right. Run it once, check it, then schedule it.")]))
    s.append(task("cwtask", "l1c", "t41", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.", time="12 min work, then 2 min: the flags you found.")))


    # Layer 1 · Artifacts
    s.append(story("abstory", "l1b", "Layer 1 · Artifacts", "Monday 23 November, 11:00",
        "The board meets next Wednesday, 2 December. Noura needs <b>donations by campaign</b>, a <b>cost calculator</b> for the volunteers and <b>five slides</b>. Last month she copied numbers between three tools for a whole day.",
        "Ask for the tool, <span class=\"hl\">not the paragraph.</span>", "Turn a file or an idea into an artifact, check it and share it.",
        n=N(do="Ask: which of the three would you still build by hand today?", expect="The slides, usually.", silent="say most teams still build the slides by hand.", time="10:00-10:30")))
    s.append(term("abterm", "l1b", "Layer 1 · the idea", "An answer you read once. <span class=\"hl\">A tool you keep.</span>", "Artifact",
        "An <b>artifact</b> is something Claude makes that you put in front of people: a dashboard, a calculator, a deck, a doc, even a small game. It opens beside the chat. You edit it and share it with a link.",
        "A chat answer…", "…becomes a <b>tool you keep</b> and share.", "Artifacts start private. You choose who sees them.",
        n=N(do="Show the Artifacts tab on the presenting laptop for ten seconds.", expect="Some have seen artifacts; few have shared one.", silent="ask who has shared a link from Claude before.")))
    s.append(tslide("abmenu", "l1b", "Layer 1 · six artifacts", "Six things <span class=\"hl\">to ask for today.</span>", ["Artifact", "Ask for", "Misbah example"],
        [["<b>Calculator</b>", "A cost or pricing tool", "Winter-kit cost against the budget"], ["<b>Dashboard</b>", "Charts from a spreadsheet", "Donations by campaign and channel"],
         ["<b>Chart and summary</b>", "One chart, three lines", "This week's donations, for WhatsApp"], ["<b>Slide deck</b>", "Slides that export to PowerPoint or PDF", "Five slides for the board"],
         ["<b>Document</b>", "A doc you edit and share", "The volunteer guide"], ["<b>Game or quiz</b>", "A small interactive tool", "A quiz for new volunteers"]],
        "Name the artifact and the source in the first line.",
        n=N(do="Ask each person which one they would use next week.", expect="The dashboard and the deck are the usual picks.", silent="pick the calculator and move to the next slide.")))
    s.append(widget("abcalc", "l1b", "d12", "Demo 1.3 · a live artifact", "A calculator <span class=\"hl\">you can ask Claude for.</span>", CALC_HTML,
        "Ask for a tool, not a paragraph.",
        n=N(do="Change the families to 1200: the budget goes negative. Set it back to 1020. Untick the heater and watch the cost per family fall.",
            expect=f"{kwd(D.PER_FAMILY)} per family; {kwd(D.CAMPAIGN_COST)} in total; {kwd(D.LEFT)} left.", silent="ask what number the volunteers would change first.",
            say="This is what Claude builds when you ask for a tool. I ran the same prompt this morning: here it is in Claude.", more=["Switch to the real artifact you built before the session (runbook) and change one input there too."], time="3 min")))
    s.append(player("abpp", "l1b", "d13", n=N(time="4 min")))
    s.append(listslide("ablist", "l1b", "Layer 1 · before you share", "Change it, check it, <span class=\"hl\">then share it.</span>",
        ["<b>Change:</b> ask in the chat, or edit the doc or the deck in place.", "<b>Check:</b> one number against its file. A neat chart is not a checked chart.",
         "<b>Share:</b> open Share. Artifacts start private; you choose who sees them.", "<b>Export:</b> decks to PowerPoint or PDF, docs to Word or PDF."],
        "Artifact will not open? Settings › Capabilities › Create and edit files.",
        n=N(do="Stress the second line: the dashboard on the last slide was neat and wrong.", expect="Agreement; someone asks who can see a shared link.", silent="ask who would see the board deck if you shared it.",
            more=["Share options (Help Center, November 2026): Pro and Max choose Only you or Anyone with the link. Team and Enterprise choose Only people invited, Anyone at the organization, or Anyone with the link if an owner allows it. Free cannot share new artifacts.", "Older chat artifacts still show Publish or Share & copy link."])))
    s.append(check("abchk", "l1b", f"The dashboard total is {kwd(D.DIFF)} above the Control totals sheet. <b>What do you do before you share it?</b>",
        [("Share it: Claude calculated it with code", 0, "Code adds up what is in the file. The file can be wrong."),
         ("Find the rows behind the gap, then share", 1, "Right. A total that is too high often hides a duplicate row."),
         ("Delete the Winter Warmth chart", 0, "Hiding the chart hides the problem, not the cause.")]))
    s.append(task("abtask", "l1b", "t13", n=TASK_N))

    # Layer 2 · Connectors
    s.append(story("l2story", "l2", "Layer 2 · Connectors", "Tuesday 24 November, 07:50",
        "Hessa has a 09:00 meeting about the heater delivery. She opens <b>40 unread emails</b> and copies parts of them into Claude, one by one. At 08:55 she is still copying.",
        "Claude can read the inbox. <span class=\"hl\">You keep the send button.</span>", "Connect email and calendar, and keep every action under your approval.",
        n=N(do="Ask: how much of your morning goes on reading email before meetings?", expect="Half an hour or more.", silent="say how long your own inbox takes on a Sunday.", time="10:40-11:10")))
    s.append(scene("l2scene", "l2", "Layer 2 · the picture", "A visitor badge opens <span class=\"hl\">some doors, not all.</span>",
        "Reception gives a visitor a badge for the rooms they need. Some doors open at once. Some need a person to come down and say yes.",
        "A connector is a badge for Claude. You choose the doors.",
        [{"ground": 268}, {"building": (360, 268)}, {"person": (110, 268), "tone": "hot", "label": "Claude, with a badge", "anim": "bob"},
         {"move": "mail", "path": [(150, 210), (300, 210)], "dur": 4},
         {"pill": "Read: open", "at": (120, 40), "tone": "ok", "delay": 0}, {"pill": "Draft: open", "at": (120, 84), "tone": "ok", "delay": 1},
         {"pill": "Send: ask me", "at": (350, 40), "tone": "hot", "delay": 2}, {"pill": "Pay: blocked", "at": (350, 84), "tone": "bad", "delay": 3}],
        n=N(do="Ask: which doors would you open for Claude on day one?", expect="Read and draft. Not send.", silent="say you would open read and draft, and keep send.",
            say="You decide the doors. You can change them any time.")))
    s.append(term("l2term", "l2", "Layer 2 · the idea", "Claude reads the app. <span class=\"hl\">You hold the keys.</span>", "Connector",
        "A <b>connector</b> links Claude to an app you use, such as Gmail, Google Calendar or Google Drive. Claude searches and reads there with your sign-in, and acts there only when you allow it.",
        "Copy and paste from each app…", "…Claude <b>reads the app itself</b>, with your sign-in.", "Turn it on from the + menu, under Connectors.",
        n=N(do="Open the + menu on the presenting laptop and hover over Connectors.", expect="Gmail, Google Calendar and Drive in the list.",
            more=["On Team plans, an owner must turn the Google connectors on before members can sign in."], silent="ask which app they would connect first.")))
    s.append(player("l2pp", "l2", "d21", n=N(time="3 min")))
    s.append(tslide("l2rules", "l2", "Layer 2 · you decide", "You decide <span class=\"hl\">what Claude may do.</span>", ["Setting", "What happens", "Use it for"],
        [["<b>Manual mode</b>", "Claude asks you to Allow or Deny each action", "New tasks, email, anything with money"],
         ["<b>Auto mode</b>", "Claude runs; a safety check blocks risky steps, and can miss some", "Low-risk work you have run before"],
         ["<b>Needs approval or Always ask</b>", "That connector tool asks you first, every time", "Sending email, creating events"],
         ["<b>Blocked</b>", "Claude never uses that tool", "Deleting, paying, sharing outside"]],
        "Start in Manual. Loosen only for tasks you trust.",
        n=N(do="Point to Manual mode: the mode picker is in the message box. Gmail send, reply and forward ask first unless you are in Auto mode.",
            expect="Questions about who sees the inbox: only the person who signed in.", silent="ask which tool they would block on day one.")))
    s.append(sortslide("l2sort", "l2", "Safe-use sort · green, amber, red", "Green, amber or red? <span class=\"hl\">Tap a card.</span>", CD.SORT, C.SORT_LABELS,
        n=N(say="Call it out first, then I tap the card.", expect="Donor lists, case files and auto-sending are red.",
            more=["Amber needs two things: an account the organization approved, and approvals on.", "Donor and family data stays red in any account."], time="4 min")))
    s.append(check("l2chk", "l2", "You ask Claude to send the reply to Salem. You are in Manual mode. <b>What happens before it goes?</b>",
        [("Claude sends it at once", 0, "Not in Manual mode. Sending waits for you."),
         ("Claude asks you to allow or deny the send", 1, "Right. You read it, check it, then decide."),
         ("Salem sees it as a draft", 0, "Drafts stay in your account until you send.")]))
    s.append(task("l2task", "l2", "t21", n=TASK_N))

    # Layer 3 · Memory, instructions and Projects
    s.append(story("l3story", "l3", "Layer 3 · Teach once", "Wednesday 25 November, 10:00",
        "Every new chat, Noura pastes the same three paragraphs: who Misbah is, the brand voice, the campaign rules. <b>Last week she forgot the photo rule</b>, and a draft asked for a photo of a family at the door.",
        "Write the rules once. <span class=\"hl\">In the right place.</span>", "Put memory, instructions and a Project to work.",
        n=N(do="Ask: what do you paste into Claude again and again?", expect="The organization, the tone, a template.", silent="say what Noura pastes: the brand voice.", time="11:10-11:40")))
    s.append(tslide("l3where", "l3", "Layer 3 · where it goes", "Four places <span class=\"hl\">to teach Claude.</span>", ["Place", "What goes there", "It applies to", "Misbah example"],
        [["<b>Memory</b>", "Facts Claude keeps from your chats; view and edit them", "Your chats", "I work in Misbah's marketing team"],
         ["<b>Instructions for Claude</b>", "How you like answers", "Every chat", "English first, then Arabic"],
         ["<b>Project</b>", "Rules and files for one area of work", "Chats in that Project", "Winter campaign: brand guide and brief"],
         ["<b>Skill</b>", "A method for one task", "Any chat, when the task comes up", "Donor thank-you letter"]],
        "Who you are: memory. How you like it: instructions. One area: a Project. One method: a Skill.",
        n=N(do="Read the last column only. Ask where the photo rule belongs.", expect="In the Project, for the campaign.",
            more=["Memory: Settings › Your Claude, or Settings › Memory on the older layout. Each item can be edited or deleted.", "To keep one chat out of memory, turn Memory off in the + menu before the first message."],
            silent="answer it: the Project, because it is a campaign rule.")))
    s.append(term("l3term", "l3", "Layer 3 · the idea", "One area of work. <span class=\"hl\">One Project.</span>", "Project",
        "A <b>Project</b> keeps instructions, files and its own memory for one area of work. Every chat inside it starts with them.",
        "Like a team folder with the rules on the cover…", "…every new chat <b>already knows the campaign</b>.", "One Project per campaign, or per role.",
        n=N(do="Open the campaign Project on the presenting laptop. Show the instructions and the two files.", expect="Questions about sharing: Projects can be shared on Team plans.",
            silent="ask which Project they would make first at work.")))
    s.append(player("l3pp", "l3", "d31", n=N(time="3 min")))
    s.append(check("l3chk", "l3", "The brand guide shapes every winter-campaign chat, <b>but not your other work</b>. Where does it go?",
        [("Instructions for Claude, in Settings", 0, "That applies to every chat you start, not only the campaign."),
         ("The Project's knowledge", 1, "Right. Only chats in the Project use it."),
         ("Say it once in a chat, for memory", 0, "Memory keeps facts about you. Files belong in a Project.")]))
    s.append(task("l3task", "l3", "t31", n=N(do="Start the timer. Walk the room. Ask each person what they found so far.", time="15 min work, then 3 min: two people read their Project's post aloud.")))
    s.append(listslide("l3mem", "l3", "Layer 3 · memory", "Memory: what Claude <span class=\"hl\">keeps between chats.</span>",
        ["<b>See it:</b> Settings › Your Claude (older layout: Settings › Memory). Every topic Claude keeps is listed there.",
         "<b>Change it:</b> open a topic to edit or delete it. Or tell Claude “remember this”.",
         "<b>Projects:</b> each Project has its own memory. Your other Projects do not see it.",
         "<b>One chat without it:</b> turn Memory off in the + menu before the first message, or use an incognito chat."],
        "Memory is about you. Instructions say how you like answers. A Project holds one area of work.",
        n=N(do="Open Settings › Your Claude on the presenting laptop and show one memory topic. Do not open anything personal.", expect="Surprise at what Claude already keeps.",
            more=["On Team and Enterprise plans, an owner decides whether memory is on.", "Some details are never saved to memory, such as civil ID and bank account numbers."],
            silent="ask who has looked at their memory before.", time="2 min")))
    s.append(check("l3memchk", "l3", "Hessa wants one chat about next year's budget ideas <b>that Claude will not remember or find later</b>. What does she do?",
        [("Turn Memory off in the + menu", 0, "Memory off keeps it out of memory, but chat search can still find the chat."),
         ("Start an incognito chat (the ghost icon)", 1, "Right. An incognito chat is not saved to your history, memory or chat search."),
         ("Delete the chat a week later", 0, "Deleting a chat does not remove the memory it created.")]))

    # Layer 3 · Skills
    s.append(story("skstory", "l3b", "Layer 3 · Skills", "Wednesday 25 November, 13:30",
        "Fahad writes <b>30 thank-you letters</b> to donors every week. Each one has the same five steps. A new volunteer wrote them last week and <b>missed every receipt number.</b>",
        "A method in your head <span class=\"hl\">is a method nobody else can follow.</span>", "Create a skill, install one, and find more.",
        n=N(do="Ask: which method in your team lives in one person's head?", expect="Reports, letters, checklists.", silent="say Fahad's letters are the example for today.", time="11:55-12:20")))
    s.append(scene("skscene", "l3b", "Layer 3 · the picture", "A recipe card <span class=\"hl\">in the kitchen drawer.</span>",
        "The cook does not read every recipe each morning. When a dish is ordered, the right card comes out of the drawer, with its steps and a photo of the result.",
        "A skill comes out only when its task comes up.",
        [{"ground": 268}, {"person": (100, 268), "tone": "hot", "label": "Claude", "anim": "nod"}, {"doc": (300, 230), "tone": "hot", "label": "donor-thank-you", "anim": "pop"},
         {"pill": "Name", "at": (90, 50), "delay": 0}, {"pill": "When to use it", "at": (250, 50), "tone": "hot", "delay": 1}, {"pill": "Steps", "at": (400, 50), "delay": 2},
         {"pill": "Example", "at": (180, 100), "delay": 3}, {"pill": "Template", "at": (340, 100), "delay": 4}],
        n=N(do="Point to When to use it: that is the part Claude reads first.", expect="People connect skills with templates.", silent="say a skill is a template plus the method plus the trigger.")))
    s.append(term("skterm", "l3b", "Layer 3 · the idea", "Teach a method <span class=\"hl\">once.</span>", "Skill",
        "A <b>Skill</b> is a folder with a SKILL.md file: a name, a description of when to use it, the steps and an example. Claude reads the description and loads the full skill only when the task comes up.",
        "Like the recipe card in the drawer…", "…Claude takes it out <b>only for that dish</b>.", "A Project is where. A Skill is how.",
        n=N(do="Contrast with the Project slide: a Project is a place; a skill travels to any chat.", expect="The difference lands with the recipe picture.", silent="ask: would the thank-you method work outside the campaign Project? Yes.")))
    s.append(tslide("skanat", "l3b", "Layer 3 · inside a skill", "What is <span class=\"hl\">inside a Skill?</span>", ["Part", "What it says", "Donor thank-you example"],
        [["<b>name</b>", "A short name", "donor-thank-you"], ["<b>description</b>", "When Claude should use it", "Use when someone asks for a donor thank-you or receipt letter"],
         ["<b>steps</b>", "The method, in order", "Greeting, amount, what it paid for, thanks, receipt"], ["<b>example</b>", "One good result", "A letter under 120 words"],
         ["<b>files</b> (optional)", "A template, a logo, a checklist", "template.md"]],
        "The description decides when Claude uses it. Write it like a trigger.",
        n=N(do="Open the starter skill's SKILL.md on screen. Point to the description line.", expect="Surprise at how short it is.", silent="read the description aloud and ask what would trigger it.")))
    s.append(player("skpp", "l3b", "d32", n=N(time="3 min")))
    s.append(listslide("skfind", "l3b", "Layer 3 · find skills", "Search first. <span class=\"hl\">Build only what is missing.</span>",
        ["<b>Use one:</b> click + or type / in the chat, then pick the skill.", "<b>Find one:</b> the Plugins page in the sidebar (Customize on some accounts). Filter by skills.",
         "<b>Make one:</b> ask Claude to build it, or upload a .zip: Plugins page › Add (older layout: Customize › Skills › +).", "<b>Switch it on:</b> skills need Create and edit files, in Settings › Capabilities."],
        "Skills work on your paid plan.",
        n=N(do="Open the Plugins page and filter by skills. Then upload the starter .zip live, so the room sees the path Task 3.2 uses.", expect="Someone spots a skill for their job.",
            more=["The sidebar item was renamed from Customize to Plugins this month. Some accounts still show the old name."], silent="name one skill you would add for an accountant.")))
    s.append(check("skchk", "l3b", "Which job makes <b>a good Skill</b>?",
        [("A weekly letter with the same five steps", 1, "Right. A method you repeat is a skill."),
         ("One question about today's weather", 0, "A one-off question needs no skill."),
         ("A list of your passwords", 0, "Never put passwords in a skill, or anywhere in Claude.")]))
    s.append(task("sktask", "l3b", "t32", n=TASK_N))

    # Layer 4 · Scheduled tasks and your first AI employee
    s.append(story("aestory", "l5", "Layer 4 · Your first AI employee", "Thursday 26 November, 12:15",
        "The General Manager asks: <b>“Can Claude be our producer, our marketer, our designer and our accountant?”</b> Yes, if you set it up the way you set up a new hire.",
        "An AI employee is <span class=\"hl\">the layers, set up for one job.</span>", "Hire one AI employee for one Misbah role, and test its first job.",
        n=N(do="Turn to the General Manager: which role would save Al-Balagh the most time?", expect="Often the accountant or the marketer.", silent="suggest the accountant: the receipts are already in the room.", time="12:20-12:50")))
    s.append(term("aesched", "l5", "Layer 4 · schedules", "The same job, <span class=\"hl\">on a time you set.</span>", "Scheduled task",
        "A <b>scheduled task</b> runs on its own at the time you choose, for example every Thursday at 08:00. It runs in the cloud with your connectors and the files saved to Claude, so your laptop can be off. Open Scheduled › New task, or describe the job in a chat and click Schedule.",
        "A reminder in your calendar…", "…a colleague who <b>does the job at that time</b> and leaves the result.", "Schedule only what you have run and checked by hand.",
        n=N(do="Open Scheduled › New task on the presenting laptop and show the form. Do not save it.", expect="Questions about approvals: nobody is there to answer a scheduled task. A tool set to ask first may wait for your answer, or the task finishes without it.", more=["A task on a laptop folder runs only while the laptop is awake and the desktop app is open (Require this computer). For a job that must run with the laptop closed, use Google Drive or files saved to Claude."],
            silent="ask which weekly job they would schedule first.")))
    s.append(check("aeschk", "l5", "Fahad's weekly receipts job must run <b>even when his laptop is closed</b>. Where should it read the receipts from?",
        [("The Downloads folder on his laptop", 0, "A laptop folder works only while the laptop is awake and the desktop app is open."),
         ("A pinned chat with the receipts pasted in", 0, "Pasting by hand is the job you wanted to stop doing."),
         ("A Google Drive folder, through the connector", 1, "Right. Connectors and files saved to Claude work when the laptop is off.")]))
    s.append(scene("aescene", "l5", "Layer 4 · the recipe", "Hire it <span class=\"hl\">like a person.</span>",
        "A new hire gets a job description, a binder, the team's procedures, keys, a shift and a manager. An AI employee needs the same things.",
        "Job · binder · procedures · keys · shift · manager.",
        [{"ground": 268}, {"person": (240, 268), "tone": "hot", "label": "AI accountant", "anim": "bob"},
         {"pill": "Job: instructions", "at": (120, 36), "delay": 0}, {"pill": "Binder: files", "at": (360, 36), "delay": 0.8},
         {"pill": "Procedures: Skills", "at": (120, 80), "delay": 1.6}, {"pill": "Keys: connectors", "at": (360, 80), "delay": 2.4},
         {"pill": "Shift: schedule", "at": (240, 124), "delay": 3.2},
         {"pill": "Manager: you", "at": (240, 168), "tone": "ok", "delay": 4}],
        n=N(do="Map each pill to a layer from the morning: instructions and files were layer 3, keys were layer 2, the shift was layer 4.",
            expect="The room sees that they already built every part.", silent="point to the manager pill and say: that one is always a person.")))
    s.append(tslide("aetable", "l5", "Layer 4 · four roles", "Four AI employees <span class=\"hl\">for Misbah.</span>", ["Role", "Its job", "Skill", "Connectors", "Shift"],
        [["<b>Producer</b>", "Scripts and shot lists from the brief", "A video-script skill", "Google Drive", "Sunday: the content plan"],
         ["<b>Marketer</b>", "Posts and captions in the brand voice", "A post-checklist skill", "Google Drive, Gmail drafts", "Monday: the post plan"],
         ["<b>Designer</b>", "Posts and posters as artifacts", "A brand-check skill", "Google Drive", "Wednesday 09:00: the week's designs"],
         ["<b>Accountant</b>", "Donations, receipts, a three-line note", "The donor thank-you skill", "Google Drive, Gmail to read", "Thursday 08:00"]],
        "Same recipe, four jobs. You stay the manager.", cls="tight",
        n=N(do="Ask each person to choose a row for Task 4.1.", expect="Different roles across the room.", silent="assign the roles yourself, one each.")))
    s.append(player("aepp", "l5", "d42", n=N(time="3 min")))
    s.append(task("aetask", "l5", "t42", n=TASK_N))
    s.append(timer_slide("aeshow", "l5", "Show and tell · 12:45", "One minute each: <span class=\"hl\">meet your AI employee.</span>",
        "Show its job description, its first output, and the one fact you checked.", 5,
        n=N(do="One minute per person; with more than five people, pick five or give 30 seconds each. Ask each: what will it do next week, and what will you approve?", expect="Different roles across the room.", silent="show the accountant from the demo.",
            fallback="If nobody finished, show the backup note from Demo 4.1.")))

    # Close
    s.append(timer_slide("c6survey", "c6", "Final survey · 12:50", "Five minutes: <span class=\"hl\">tell us how it went.</span>", SURVEY_LEAD, 5,
        n=N(do="Leave the slide up while they scan. Start the timer.", say="This is not a test. Tell us what worked and what we should change.",
            fallback="Read out the short link: the site address, then /survey.", silent="give your own one-line answer to: which part was most useful?",
            more=["The same QR code is on the workshop home and the day page.", "Check the response count in the portal before you close."], time="12:50-12:55")))
    s.append(wrap("w1", "close", "Four layers, one morning: <span class=\"hl\">and you stay the manager.</span>",
        [("You built", "Six things", "A Cowork table, an artifact, a brief, a Project, a skill and an AI employee."),
         ("Between you, you caught", "5 planted problems", "2 errors in the post, 1 duplicate donation, 2 receipt flags."),
         ("The habit", "Claude drafts", "You check. You approve what goes out.")],
        "Your first week: one artifact, one Project, and your email in read mode in an approved account. Then one layer at a time.",
        n=N(do="Ask each person which layer they will switch on first at work.", expect="Connectors and Projects come up most.", silent="say which one you would start with: the Project.", time="12:55-13:00")))
    s.append(listslide("explore", "close", "After today · keep exploring", "Keep exploring <span class=\"hl\">on your own.</span>",
        ["<b>Claude Help Center:</b> support.claude.com explains every feature, step by step.", "<b>Claude Academy:</b> academy.claude.com has free short courses, such as Introduction to Claude Cowork.",
         "<b>The Plugins page:</b> search ready-made skills and connectors before you build.", "<b>Your cheat sheet and take-home guide:</b> on the workshop site, with every prompt from today.",
         "<b>The next layer:</b> Claude Code, where Claude builds tools and small apps with you."],
        "One new layer a week is enough.",
        n=N(do="Point to the site link on the cheat sheet. Mention Claude Code in one sentence only.", expect="Questions about a follow-up session: take them to Yousif.", silent="say the Help Center is where you check anything new.")))
    return s

TOPICS = {1: {"open": "Opening", "l1": "Layer 1 · Chat", "l1c": "Layer 1 · Cowork", "l1b": "Layer 1 · Artifacts", "l2": "Layer 2 · Connectors", "l3": "Layer 3 · Memory, instructions, Projects",
              "l3b": "Layer 3 · Skills", "l5": "Layer 4 · Schedules and AI employee", "c6": "Final survey", "close": "Close"}}
DAYFN = {1: day1}
