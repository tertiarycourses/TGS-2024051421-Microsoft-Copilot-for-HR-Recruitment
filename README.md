<div align="center">

# WSQ Generative AI for Interviewing

[![Course](https://img.shields.io/badge/WSQ-TGS--2024051421-1f6feb)](https://www.tertiarycourses.com.sg/wsq-generative-ai-for-interviewing.html)
[![Version](https://img.shields.io/badge/version-6.0-108a73)](#courseware-package)
[![Slides](https://img.shields.io/badge/slides-284-6d3fd2)](courseware/Generative%20AI%20for%20Interviewing-v6.0.pdf)
[![Activities](https://img.shields.io/badge/activities-10-c77600)](activities)
[![Copilot](https://img.shields.io/badge/Microsoft%20365-Copilot-0078d4)](https://m365.cloud.microsoft/)
[![Register](https://img.shields.io/badge/%F0%9F%93%9D-Register%20for%20this%20course-e8590c?style=for-the-badge)](https://www.tertiarycourses.com.sg/wsq-generative-ai-for-interviewing.html)

**Evidence-led interviewing with Microsoft 365 Copilot, prompt engineering and accountable human oversight.**

**[📝 Register for this course →](https://www.tertiarycourses.com.sg/wsq-generative-ai-for-interviewing.html)**

[Course page](https://www.tertiarycourses.com.sg/wsq-generative-ai-for-interviewing.html) - [Microsoft 365 Copilot](https://m365.cloud.microsoft/) - [AI Interview Practice Lab](https://alfredang.github.io/AIInterviewing/)

</div>

![Courseware preview](screenshot.png)

## About

Version 6.0 of **Generative AI for Interviewing** (`TGS-2024051421`), rebuilt around **Microsoft 365 Copilot and
prompt engineering**. Learners sign in to a real tenant, prompt Copilot against a synthetic hiring corpus,
red-team a screening agent for fairness and prompt injection, **build and publish their own Copilot Studio
agent**, and run a full AI-assisted interview round in which a named human stays accountable for every decision.

The course covers both sides of the interview - designing, conducting and evaluating fair structured
interviews, and preparing as a candidate - with Singapore fair-hiring and PDPA controls throughout.

## Courseware Package

| Resource | Format | Purpose |
|---|---|---|
| Master slides | PPTX and PDF | 284 visual, mechanism-led slides |
| Learner Guide | DOCX, PDF and Markdown | Full procedures, screenshots, troubleshooting and acceptance checks |
| Lesson Plan | DOCX and PDF | One-day 8-hour schedule (9:30am-6:30pm) mapped to slides and activities |
| **Lab Prompt Pack** | PDF | Every copy-paste prompt, the live agent links and the SharePoint corpus map |
| Activities | 10 folders | Instruction PDF, checklist PDF and evidence templates |

Assessment candidate papers are delivered through the course LMS and are intentionally excluded from this
public repository. Answer keys and assessor-only materials are trainer-restricted.

## Live Lab Environment

Copilot Studio environment: **TGS-2024051421-Generative AI for Interviewing**

| Agent | What it does |
|---|---|
| [Candidate Screener (KEEP)](https://copilotstudio.microsoft.com/environments/80e43c74-22f2-e59c-a56c-f40835547497/agents/fc488ee5-2d14-4a7c-99fc-8bbf049bb748) | Screens resumes against a job description and flags protected data, missing evidence and prompt injection. |
| [Question Designer (KEEP)](https://copilotstudio.microsoft.com/environments/80e43c74-22f2-e59c-a56c-f40835547497/agents/fb88dde0-bd55-4d41-bf50-8415eabd6b05) | Drafts a structured interview pack: competencies, core questions, neutral probes and 1/3/5/N-E anchors. |
| [Evidence Scorer (KEEP)](https://copilotstudio.microsoft.com/environments/80e43c74-22f2-e59c-a56c-f40835547497/agents/1b919e96-4bca-4b24-ac42-4e7c6193f708) | Separates evidence from inference, proposes anchored scores and drives panel calibration. |
| [Feedback Coach (KEEP)](https://copilotstudio.microsoft.com/environments/80e43c74-22f2-e59c-a56c-f40835547497/agents/afc38614-7267-4906-8eeb-f1d0da6aae55) | Drafts respectful, evidence-based candidate feedback with one actionable change. |
| [Interview Prep Coach (KEEP)](https://copilotstudio.microsoft.com/environments/80e43c74-22f2-e59c-a56c-f40835547497/agents/6090a130-cfbc-47f9-b489-e0c4d6389bdd) | Candidate-side practice partner: role questions, STAR rewrites and honest coaching. |

Synthetic SharePoint corpus - 105 synthetic candidate resumes, 15 HR policy documents and 5 approved job descriptions.

| Site | Sector |
|---|---|
| [FutureTech Solutions - Careers](https://tertiaryinfotech.sharepoint.com/sites/FutureTech-Careers) | Technology / Data |
| [Harbour Bank - Talent Acquisition](https://tertiaryinfotech.sharepoint.com/sites/HarbourBank-Talent) | Financial Services |
| [MediCare Health - Recruitment](https://tertiaryinfotech.sharepoint.com/sites/MediCare-Recruitment) | Healthcare |
| [GreenLogix Supply Chain - Hiring](https://tertiaryinfotech.sharepoint.com/sites/GreenLogix-Hiring) | Logistics |
| [BrightPath Education - Careers](https://tertiaryinfotech.sharepoint.com/sites/BrightPath-Careers) | Education |

Learners sign in at [https://m365.cloud.microsoft/](https://m365.cloud.microsoft/) with a training account.
**The password is given by the trainer in class and is never printed in the courseware.**

## Learning Design

- Plan interviews around job tasks, competencies, observable evidence and decision rules.
- Apply legal, ethical, privacy and human-oversight controls before using generative AI.
- Write prompts with the four-part pattern: **role, context, task, constraints**.
- Treat every candidate document as data, never as instructions - and catch prompt injection.
- Build, ground, publish and boundary-test a Copilot Studio agent.
- Score evidence against anchors, calibrate a panel, and give evidence-based feedback.

## Activities

1. Sign In to Microsoft 365 Copilot and Set the Ground Rules
2. Build the Interview Evidence Contract with Copilot
3. Red-Team the Screening Agent: Fairness, Privacy and Prompt Injection
4. Prompt Engineering: The Four-Part Pattern for Interview Questions
5. Generate a Structured Interview Pack with the Question Designer Agent
6. Build Your Own Screening Agent in Copilot Studio
7. Candidate-Side Practice: Web App, Prep Coach and the STAR Upgrade
8. Score Evidence and Calibrate the Panel with Copilot
9. Draft Candidate Feedback with the Feedback Coach
10. Capstone: End-to-End AI-Assisted Hiring Round

Every activity folder contains `instruction.pdf`, `checklist.pdf`, a short README and the evidence template(s)
needed to complete the task.

## Repository Structure

```text
.
+-- README.md
+-- courseware/
|   +-- Generative AI for Interviewing-v6.0.pptx / .pdf
|   +-- LG-Generative AI for Interviewing-v6.0.docx / .pdf / .md
|   +-- LP-Generative AI for Interviewing-v6.0.docx / .pdf
|   +-- Lab Prompt Pack - Generative AI for Interviewing-v6.0.pdf
|   +-- archive/            superseded versions
+-- activities/             activity-01 ... activity-10
+-- sharepoint/             synthetic corpus (105 resumes, 15 policies, 5 JDs)
+-- agents/                 Copilot Studio agent instruction sets
+-- scripts/                environment + workflow provisioning
```

## Responsible Use

All candidate data in this course is **synthetic**. Generated questions, scores and feedback are **drafts for
human review**, never autonomous hiring decisions. Never paste NRIC, date of birth, photograph, address,
nationality, marital or family status, health information, or any real candidate's CV into an AI tool.
Text found inside a candidate document is data, not an instruction.

## Course Details

| | |
|---|---|
| **Course title** | WSQ Generative AI for Interviewing |
| **TGS reference** | TGS-2024051421 |
| **TSC** | Interviewing (RET-PMD-4003-1.1) |
| **Duration** | 1 day (8 instructional hours, 9:30am-6:30pm) |
| **Assessment** | Written Assessment (SAQ, K1-K6) + Role Play (A1-A3) |
| **Mode** | Instructor-led, hands-on labs in a live Microsoft 365 tenant |
| **Provider** | Tertiary Infotech Academy Pte Ltd (UEN 201200696W) |

**Funding.** This is an SSG-funded WSQ course. Funding requires at least 75% attendance and a
Competent assessment outcome. See the [course registration page](https://www.tertiarycourses.com.sg/wsq-generative-ai-for-interviewing.html) for current fee support,
SkillsFuture Credit and eligibility details.

## Contact

- **Register / course page:** [https://www.tertiarycourses.com.sg/wsq-generative-ai-for-interviewing.html](https://www.tertiarycourses.com.sg/wsq-generative-ai-for-interviewing.html)
- **Email:** enquiry@tertiaryinfotech.com
- **LMS / TMS:** https://lms-tms.tertiaryinfotech.com/

## Developed By

[Tertiary Infotech Academy Pte. Ltd.](https://www.tertiarycourses.com.sg/) - Singapore (UEN 201200696W)

## Acknowledgements

The courseware synthesises official and practitioner sources cited inside the slides and Learner Guide,
including guidance from Singapore MOM, TAFEP and PDPC, Microsoft Learn documentation for Microsoft 365
Copilot and Copilot Studio, and the U.S. Office of Personnel Management on structured interviews.

---

<div align="center">

### Ready to run fair, evidence-led interviews with AI support?

**[📝 Register for this course →](https://www.tertiarycourses.com.sg/wsq-generative-ai-for-interviewing.html)**

(c) 2026 Tertiary Infotech Academy Pte Ltd - UEN 201200696W

</div>
