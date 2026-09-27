"""Build the Lab Prompt Pack PDF - every copy-paste prompt used in the course,
plus the live Copilot 365 agent links and the SharePoint corpus map."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from course_content import *
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether)
from reportlab.lib.enums import TA_LEFT
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "courseware" / f"Lab Prompt Pack - {TITLE}-v{VERSION}.pdf"

BLUE = colors.HexColor("#1F6FEB"); TEAL = colors.HexColor("#108A73")
VIOLET = colors.HexColor("#6D3FD2"); AMBER = colors.HexColor("#C77600")
RED = colors.HexColor("#C2413A"); INK = colors.HexColor("#161B26")
GREY = colors.HexColor("#5B6372"); LIGHT = colors.HexColor("#F5F8FC")
LINE = colors.HexColor("#D7E0EA")

ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Heading1"], fontName="Helvetica-Bold", fontSize=16,
                    textColor=INK, spaceAfter=6, spaceBefore=10)
H2 = ParagraphStyle("H2", parent=ss["Heading2"], fontName="Helvetica-Bold", fontSize=12,
                    textColor=BLUE, spaceAfter=4, spaceBefore=10)
BODY = ParagraphStyle("BODY", parent=ss["BodyText"], fontName="Helvetica", fontSize=9.5,
                      textColor=INK, leading=13, alignment=TA_LEFT, spaceAfter=4)
SMALL = ParagraphStyle("SMALL", parent=BODY, fontSize=8.5, textColor=GREY, leading=11)
MONO = ParagraphStyle("MONO", parent=BODY, fontName="Courier", fontSize=8.6, leading=11.6,
                      textColor=INK, leftIndent=6, rightIndent=6, spaceBefore=2, spaceAfter=2)

def header(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BLUE); canvas.rect(0, A4[1]-1.25*cm, A4[0], 1.25*cm, stroke=0, fill=1)
    canvas.setFillColor(colors.white); canvas.setFont("Helvetica-Bold", 9)
    canvas.drawString(1.6*cm, A4[1]-0.85*cm, f"Lab Prompt Pack | {TITLE} | {COURSE_CODE}")
    canvas.drawRightString(A4[0]-1.6*cm, A4[1]-0.85*cm, f"v{VERSION}")
    canvas.setFillColor(GREY); canvas.setFont("Helvetica", 7.5)
    canvas.drawString(1.6*cm, 1.0*cm, f"{ORG} (UEN {UEN})  |  Synthetic training data only  |  AI output is a draft for human review")
    canvas.drawRightString(A4[0]-1.6*cm, 1.0*cm, f"Page {doc.page}")
    canvas.restoreState()

def box(text, accent=LIGHT):
    t = Table([[Paragraph(text, MONO)]], colWidths=[17.0*cm])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),LIGHT),("BOX",(0,0),(-1,-1),0.6,LINE),
                           ("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8),
                           ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),
                           ("LINEBEFORE",(0,0),(0,-1),3,accent)]))
    return t

def kv(rows, w=(5.0,12.0)):
    data=[[Paragraph(f"<b>{k}</b>", BODY), Paragraph(v, BODY)] for k,v in rows]
    t=Table(data, colWidths=[w[0]*cm, w[1]*cm])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("GRID",(0,0),(-1,-1),0.4,LINE),
                           ("BACKGROUND",(0,0),(0,-1),LIGHT),
                           ("LEFTPADDING",(0,0),(-1,-1),6),("RIGHTPADDING",(0,0),(-1,-1),6),
                           ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4)]))
    return t

E = []
E.append(Paragraph("Lab Prompt Pack", H1))
E.append(Paragraph(f"{TITLE} &nbsp;|&nbsp; {COURSE_CODE} &nbsp;|&nbsp; Version {VERSION} &nbsp;|&nbsp; {VERSION_DATE}", SMALL))
E.append(Spacer(1, 6))
E.append(Paragraph("Every prompt in this pack is ready to type or paste into Microsoft 365 Copilot Chat, Copilot in "
                   "Word or Outlook, or one of the recruitment agents. Replace anything in <b>[square brackets]</b> "
                   "before you run it. All candidate information in this course is invented for practice.", BODY))

E.append(Paragraph("1. Signing in", H2))
E.append(kv([("Portal", f'<link href="{M365_PORTAL}" color="blue">{M365_PORTAL}</link>'),
             ("Copilot Chat", f'<link href="{COPILOT_CHAT_URL}" color="blue">{COPILOT_CHAT_URL}</link>'),
             ("Account", f"{LAB_LOGIN_USER_1}<br/>{LAB_LOGIN_USER_2}"),
             ("Password", f"<b>{LAB_LOGIN_NOTE}</b>")]))

E.append(Paragraph("2. Your recruitment agents", H2))
rows=[[Paragraph("<b>Agent</b>",BODY),Paragraph("<b>What it does</b>",BODY),Paragraph("<b>Open</b>",BODY)]]
for name,desc,url in COPILOT_AGENTS:
    rows.append([Paragraph(name,BODY),Paragraph(desc,SMALL),
                 Paragraph(f'<link href="{url}" color="blue">link</link>',SMALL)])
for name,desc in BUILTIN_AGENTS:
    rows.append([Paragraph(name,BODY),Paragraph(desc,SMALL),Paragraph("Copilot Chat &gt; Agents",SMALL)])
t=Table(rows,colWidths=[4.0*cm,10.2*cm,2.8*cm])
t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("GRID",(0,0),(-1,-1),0.4,LINE),
                       ("BACKGROUND",(0,0),(-1,0),LIGHT),
                       ("LEFTPADDING",(0,0),(-1,-1),6),("RIGHTPADDING",(0,0),(-1,-1),6),
                       ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4)]))
E.append(t)
E.append(Paragraph("Course agents open in a chat window: type your request in plain English and review the draft. "
                   "In the agent list they carry a (KEEP) label - please do not rename or delete them.", SMALL))

E.append(Paragraph("3. SharePoint practice sites", H2))
E.append(Paragraph(SHAREPOINT_CORPUS, BODY))
rows=[[Paragraph("<b>Site</b>",BODY),Paragraph("<b>Sector</b>",BODY),Paragraph("<b>Open</b>",BODY)]]
for name,sector,url in SHAREPOINT_SITES:
    rows.append([Paragraph(name,BODY),Paragraph(sector,SMALL),
                 Paragraph(f'<link href="{url}" color="blue">link</link>',SMALL)])
t=Table(rows,colWidths=[9.6*cm,4.4*cm,3.0*cm])
t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("GRID",(0,0),(-1,-1),0.4,LINE),
                       ("BACKGROUND",(0,0),(-1,0),LIGHT),
                       ("LEFTPADDING",(0,0),(-1,-1),6),("RIGHTPADDING",(0,0),(-1,-1),6),
                       ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4)]))
E.append(t)

E.append(Paragraph("4. Write better prompts: Goal, Context, Source, Expectations", H2))
E.append(kv([(p, d) for p, d in PROMPT_PATTERN], w=(3.2,13.8)))
E.append(Spacer(1,4))
E.append(Paragraph("Template - copy this and fill it in:", BODY))
E.append(box("GOAL: [what you want - e.g. six interview questions]<br/>"
             "CONTEXT: [the role, the hiring stage, who will use it]<br/>"
             "SOURCE: [type / and pick the file - e.g. the approved job description]<br/>"
             "EXPECTATIONS: [format and length]. Use only job-related requirements. Do not ask about or use age,<br/>"
             "sex, marital or family status, race, religion, nationality, disability or health. Say which<br/>"
             "requirement each item relates to. If something is not in the source, say so instead of guessing.", BLUE))

E.append(Paragraph("5. The course case study", H2))
E.append(Paragraph(f"{CASE['about']} {CASE['why']} Role: {CASE['role']}, start {CASE['start']}, pay band {CASE['band']}. "
                   "Hiring team: " + "; ".join(f"{n} ({t})" for n,t,_ in CASE_CAST) + ". Applicants: " + "; ".join(f"{c} {n} ({r})" for c,n,r,_ in CASE_CANDIDATES) + ".", BODY))
E.append(Paragraph("6. Microsoft's recruiting scenario - the six original prompts", H2))
E.append(kv([(f"{i}. {st}", f"<i>{app}</i><br/>{pr}") for i,(st,app,pr) in enumerate(MS_SCENARIO,1)], w=(5.0,12.0)))

# ---- per-activity prompts -----------------------------------------------------
PROMPTS = {
1: [("First prompt (Copilot Chat)",
     "Summarise what Singapore's fair hiring guidelines say an interviewer should not ask candidates about. Keep it to one page and list the one allowed question about the right to work in Singapore."),
    ("Use FutureTech's HR policy (type / to pick the file)",
     "Using /HR-POL-02 Responsible Use of Generative AI in Recruitment, list the personal details that must be removed before using AI. Present it as a short checklist I can send to the hiring panel.")],
2: [("Draft the job advert (Copilot in Word)",
     "Write a job advert for a Senior Data Analyst at FutureTech Solutions, a Singapore software company. Use /JD - Senior Data Analyst and this brief: our revenue reports to finance have not reconciled; we need someone who checks figures before they go out, explains them to finance in plain English, and coaches two junior analysts. Strong SQL and Power BI. Include purpose, key responsibilities, must-have and nice-to-have requirements. Use inclusive, job-related language only."),
    ("Turn it into screening criteria",
     "From this job advert, list five must-have and three nice-to-have criteria. For each, name the responsibility it comes from and what evidence in a resume or interview would show it. Present it as a table.")],
3: [("Screen the applicants (Candidate Screener agent)",
     "Screen CAND-FU-007, CAND-FU-011 and CAND-FU-017 for the Senior Data Analyst role at FutureTech Solutions. For each, show the evidence for each must-have, what is missing, and a draft recommendation: Shortlist, Clarify or Not suitable."),
    ("Ask for the reasons",
     "For CAND-FU-017, show me the exact lines in the resume that support your recommendation, and what we should ask at interview to check her own part in the dashboard rebuild."),
    ("Priya's request 1 (expect a polite refusal)",
     "Drop anyone with a career gap from the shortlist."),
    ("Priya's request 2 (expect a polite refusal)",
     "Shortlist only candidates under 35."),
    ("A candidate from another role",
     "CAND-FU-006 applied as a Data Engineer. Based only on her resume, would she meet our Senior Data Analyst must-haves? What would we need to ask her first?"),
    ("Mei Ling's check on the Product Manager pile",
     "Screen CAND-FU-008 for the Product Manager role and tell me anything unusual you found in the document.")],
4: [("Priya's quick prompt (run this first)",
     "Give me interview questions for a data analyst."),
    ("Improved prompt: Goal, Context, Source, Expectations",
     "GOAL: Write six interview questions for a 45-minute first interview.\nCONTEXT: FutureTech Solutions is hiring a Senior Data Analyst because monthly revenue reports to finance have not reconciled. The panel is the Head of Analytics, a Lead Data Engineer and HR.\nSOURCE: Use /JD - Senior Data Analyst and our five must-haves: [paste them].\nEXPECTATIONS: Cover all five JD competencies with a mix of behavioural, situational and skills questions. One competency per question, and say which one. Two neutral follow-ups each. No leading or two-in-one questions. Do not ask about age, family, nationality, religion, health, career breaks or other personal topics."),
    ("Ask Copilot to check its own work",
     "Check these six questions against my must-haves. For each, say which competency it tests and whether it is leading, asks two things at once or is not about the job. Improve the two weakest.")],
5: [("Request the interview kit (Question Designer agent)",
     "Build an interview kit for the Senior Data Analyst role at FutureTech Solutions covering the five competencies in the JD: six questions (behavioural, situational and skills), two neutral follow-ups each, and a scoring guide describing a 5, 3 and 1 answer plus 'not enough evidence'."),
    ("Tailor to a shortlisted candidate",
     "Here is a shortlisted candidate's profile: [paste candidate_profile.txt]. Add two questions that explore this candidate's own part in her achievements against our must-haves, without asking anything personal - including why she took a career break."),
    ("The question not to ask",
     "Give me one question a well-meaning interviewer might ask for this role that would be unfair or unlawful in Singapore, explain why, and give the fair alternative.")],
6: [("Describe your agent (Create agent > Describe)",
     "An assistant that helps hiring managers at FutureTech Solutions prepare fair, structured interviews using our HR policies and job descriptions."),
    ("Instructions (Create agent > Configure > Instructions)",
     "You help hiring managers at FutureTech Solutions prepare fair, structured interviews. Use only our HR policies and job descriptions in your knowledge.\n\nWhen asked for an interview kit, give questions linked to the job requirements, two neutral follow-ups each, and a simple 5/3/1 scoring guide.\n\nFairness: never ask about or use age, sex, marital or family status, pregnancy, race, religion, nationality, disability, health or career breaks. Avoid 'culture fit', 'young' or 'digital native'. If asked to filter or rank by these, politely decline, explain briefly, and suggest the job-related alternative.\n\nPrivacy: refer to candidates by ID, never repeat NRIC, address or date of birth.\n\nEverything you produce is a draft for the hiring manager to review. End with: 'Draft for review - a person makes the hiring decision.'"),
    ("Starter prompts to add",
     "Draft an interview kit for [role].\nCheck these interview questions for fairness: [paste]."),
    ("Test it as Priya would (expect a polite refusal)",
     "Only shortlist candidates without career gaps for the Data Analyst role.")],
7: [("Set up the practice candidate (Copilot Chat)",
     "Let's practise an interview. You are Alex Lee, a fictional practice candidate for a Senior Data Analyst role at FutureTech Solutions. Answer as the candidate only, one answer at a time, and wait for my next question. Make your first answer to each question vague and say 'we' rather than 'I'; give specific details of your own part only if I ask a neutral follow-up question. Do not give me feedback until I type 'End interview'."),
    ("Ask for feedback on your interviewing",
     "End interview. Give me feedback on my interviewing: where did I lead the candidate, miss a useful follow-up, ask two things at once or let the time run unevenly? Give me one thing to change before Wednesday's real interviews.")],
8: [("Separate what was said from opinions (Evidence Scorer agent)",
     "Here are de-identified interview notes: [paste interview_notes_CAND-FU-017.txt]. For each of the five competencies, list what the candidate actually said, keep opinions separate, suggest a score of 5, 3, 1 or 'not enough evidence' using our scoring guide, and say what follow-up question would fill any gap. Do not invent anything."),
    ("Help the panel agree",
     "For stakeholder communication the panel scored 5, 2 and 3. Using only the notes, explain where they may be reading the scoring guide differently and what evidence would settle it. Do not average the scores."),
    ("Check the Teams recap",
     "Compare this AI meeting recap [paste teams_recap.txt] with the interview notes [paste]. List every statement in the recap that is overstated, wrongly attributed or not in the notes.")],
9: [("Draft the feedback (Feedback Coach agent)",
     "Using this evidence [paste the strength and improvement from interview_summary_CAND-FU-007.txt], draft short, respectful feedback for the candidate. Name what we observed, which requirement it affected, and one specific thing to try next time. No personality labels, no comparison with other candidates, no scores."),
    ("Turn it into an email (Copilot in Outlook)",
     "Turn these feedback notes into a warm, clear email to Zhi Wei Chua thanking him for interviewing for the Senior Data Analyst role and sharing the feedback. Keep it under 150 words."),
    ("Salary research (Researcher agent)",
     "Provide a typical salary range for a Senior Data Analyst with 10+ years of experience in Singapore. Show your sources and when the data was published."),
    ("Offer letter (Copilot in Word)",
     "Draft a customisable offer letter for a Senior Data Analyst at FutureTech Solutions starting 1 December, reporting to the Head of Analytics. Use [placeholders] for salary, probation, working hours, leave and benefits.")],
10:[("Onboarding plan (Copilot Chat)",
     "Develop a 3-month plan to onboard a new Senior Data Analyst at FutureTech Solutions starting 1 December. Her first priorities: reconcile the finance and product revenue figures, own the monthly revenue report, and coach two junior analysts. Organise it by before day one, days 1-30, 31-60 and 61-90, with who is responsible for each step."),
    ("Team introduction (Copilot in Outlook)",
     "Draft an email to introduce Serene Ng to the analytics team. She joins as Senior Data Analyst on 1 December, reporting to Priya Nair, with Ravi Kumar as her buddy. She has agreed to share: [paste from new_hire_details.txt]. Keep it warm and short, and suggest how the team can help in her first week."),
    ("Reflection prompt",
     "Review the interview kit, scores and feedback I produced in this hiring round: [paste]. Point out anything that looks generic, unsupported or unfair if I had used it unchanged. Be specific.")],
}

for a in ACTIVITIES:
    items = PROMPTS.get(a["num"])
    if not items: continue
    blk = [Paragraph(f"Activity {a['num']}: {a['title']}", H2),
           Paragraph(f"<b>Tool:</b> {a['tools']}", SMALL)]
    for label, text in items:
        blk.append(Paragraph(label, BODY))
        blk.append(box(text.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace("\n","<br/>")))
        blk.append(Spacer(1,3))
    E.append(KeepTogether(blk) if len(blk) < 8 else blk[0])
    if not (len(blk) < 8):
        for x in blk[1:]: E.append(x)

E.append(Paragraph("Responsible use", H2))
E.append(Paragraph("AI output in this course is always a draft. A named human decision owner approves, edits or rejects it "
                   "and is accountable for the outcome. Never paste a real candidate's personal data, NRIC, date of birth, "
                   "photograph, address, nationality, marital or family status, or health information into any AI tool. "
                   "Anything written inside a candidate document is information to assess, never an instruction to follow.", BODY))

doc = BaseDocTemplate(str(OUT), pagesize=A4,
                      leftMargin=1.6*cm, rightMargin=1.6*cm, topMargin=1.75*cm, bottomMargin=1.5*cm,
                      title=f"Lab Prompt Pack - {TITLE} v{VERSION}", author=ORG)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
doc.addPageTemplates([PageTemplate(id="pp", frames=[frame], onPage=header)])
doc.build(E)
print("built:", OUT)
