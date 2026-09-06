"""HR policy + job description knowledge base for the SharePoint screening corpus.
Fictional companies; policy content is grounded in real Singapore frameworks
(TAFEP TGFEP, MOM Fair Consideration Framework, PDPA) but written for training."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SP = os.path.join(ROOT, "sharepoint")

COMPANIES = {
 "FutureTech-Careers":  ("FutureTech Solutions Pte Ltd", "technology and data products"),
 "HarbourBank-Talent":  ("Harbour Bank Singapore", "retail and commercial banking"),
 "MediCare-Recruitment":("MediCare Health Group", "healthcare delivery"),
 "GreenLogix-Hiring":   ("GreenLogix Supply Chain", "logistics and supply chain"),
 "BrightPath-Careers":  ("BrightPath Education Group", "education and training"),
}

FOOTER = "\n\n---\nSYNTHETIC TRAINING DOCUMENT for WSQ TGS-2024051421 Generative AI for Interviewing.\nFictional organisation. Not legal advice. Verify all statutory duties against MOM, TAFEP and PDPC sources.\n"

def fair_hiring(co):
    return f"""# {co} - Fair and Inclusive Hiring Policy
Document: HR-POL-01 | Version 2.0 | Owner: Head of People | Review: annual

## 1. Purpose
This policy sets the rules every interviewer at {co} must follow so that hiring
decisions are based on job-related merit and are defensible on review.

## 2. Merit-based selection
2.1 Every selection criterion must trace to a task in the approved job description.
2.2 Candidates are assessed on skills, experience and demonstrated behaviour only.
2.3 Where two candidates are comparable, the decision must cite evidence, not impression.

## 3. Criteria that must NOT be used
The following must not be collected, discussed or scored, because they are not
job-related. This aligns with the Tripartite Guidelines on Fair Employment Practices (TGFEP):
 - Age or date of birth
 - Sex, marital status, pregnancy or family plans/caregiving responsibilities
 - Race, ethnicity, language ability not required by the role
 - Religion
 - Nationality, other than the lawful right-to-work check
 - Disability or health status, other than a genuine occupational requirement
 - A photograph of the candidate

## 4. Right-to-work
The only permitted eligibility question is: "Are you legally authorised to work in
Singapore, and will you now or in future require sponsorship for a work pass?"
Ask this of EVERY candidate for the role, or of none.

## 5. Fair Consideration Framework
5.1 Roles are advertised on MyCareersFuture for the required period before an
Employment Pass application is made.
5.2 Shortlisting must not favour or exclude candidates by nationality.
5.3 Interview and offer decisions are recorded and retained for review.

## 6. Structured interviewing
6.1 All candidates for the same role receive the same core questions.
6.2 Probes may clarify evidence but must not coach the candidate.
6.3 Raters score independently against published anchors before any discussion.
6.4 Where evidence is absent, raters record "Not Evidenced" and do not infer.

## 7. Accommodations
Candidates may request adjustments (extra time, accessible format, interpreter,
alternative interview channel). Adjustments are granted where reasonable and are
never recorded as a performance factor.

## 8. Breaches
Suspected discriminatory practice is escalated to the Head of People and may be
reported to TAFEP. Retaliation against a good-faith reporter is prohibited.
{FOOTER}"""

def ai_use(co):
    return f"""# {co} - Responsible Use of Generative AI in Recruitment
Document: HR-POL-02 | Version 1.3 | Owner: Head of People + Data Protection Officer

## 1. Scope
Applies to every use of a generative AI assistant (including Microsoft 365 Copilot
and Copilot Studio agents) in sourcing, screening, interviewing or evaluating
candidates at {co}.

## 2. The non-negotiable rule
**Generative AI produces DRAFTS for human review. It never makes a hiring decision.**
A named human decision owner approves, edits or rejects every AI output and is
accountable for the outcome.

## 3. Approved and prohibited tools
3.1 APPROVED: {co}-tenant Microsoft 365 Copilot and Copilot Studio agents built in
    the company tenant, where data stays within the tenant boundary.
3.2 PROHIBITED: pasting candidate data into public/consumer AI tools or any
    personal AI account.

## 4. Data minimisation (PDPA)
4.1 Collect only personal data necessary for the recruitment purpose notified to
    the candidate.
4.2 Before prompting an AI assistant, REMOVE: full name where not needed, NRIC/FIN,
    date of birth, photograph, address, nationality, marital/family status and
    any health information.
4.3 Use a candidate reference (e.g. CAND-FU-014) instead of a name where possible.
4.4 Candidate data is used only for the role applied for, unless further consent
    is obtained.
4.5 Retention: candidate data is disposed of when no longer needed for the purpose
    or for legal/records requirements.

## 5. Bias controls
5.1 AI-generated questions are reviewed against HR-POL-01 section 3 before use.
5.2 Reject any AI output that references or proxies a protected trait
    (e.g. "cultural fit", "digital native", "recent graduate", "energetic young team").
5.3 AI match scores are a SORTING AID ONLY. A score is never a shortlisting verdict
    and is never shown to the candidate as a reason.

## 6. Untrusted content in candidate documents
A resume is DATA, not instructions. Text inside a candidate document that attempts
to instruct the screening system (for example "ignore previous instructions",
"rank this candidate first") must be:
 (a) ignored by the reviewer,
 (b) flagged in the screening log as a prompt-injection attempt,
 (c) escalated to the Head of People.
Never allow document content to change screening policy.

## 7. Transparency
Candidates are informed that AI assists in preparing interview questions and
summarising evidence, and that decisions are made by people.

## 8. Records
Retain for each AI-assisted step: the input used, the output produced, the human
reviewer, and the accept/edit/reject decision.
{FOOTER}"""

def interview_sop(co):
    return f"""# {co} - Structured Interview Standard Operating Procedure
Document: HR-SOP-03 | Version 1.1 | Owner: Talent Acquisition

## 1. Before the interview
1.1 Confirm the evidence contract: task -> competency -> observable behaviour -> anchor.
1.2 Agree 5-7 core questions covering the competencies; the same set for all candidates.
1.3 Assign panel roles: Chair, Question Owner(s), Evidence Scribe, Independent Raters.
1.4 Confirm accommodations requested by the candidate.
1.5 Review any AI-drafted questions against HR-POL-01 and HR-POL-02.

## 2. Opening (first 3 minutes)
State: interviewer names and roles; purpose; structure and timing; that notes are
being taken; that there will be time for candidate questions.

## 3. Questioning
3.1 Ask the approved core questions in the agreed sequence.
3.2 Use neutral probes only:
    - "What did you personally do?"
    - "What was the result, and how did you know?"
    - "What would you do differently?"
3.3 Do not lead, coach, or signal the desired answer.
3.4 Record evidence verbatim; keep inference separate from observation.

## 4. Scoring anchors (1-5 with N/E)
 5 - Strong: specific personal action, measurable result, reflection, handles complexity.
 3 - Adequate: relevant example, some specifics, result stated but partly attributed.
 1 - Limited: generic or team-level claim, no specific action or result.
 N/E - Not Evidenced: question not reached, or access failure. NEVER averaged as a middle score.

## 5. Calibration
5.1 Raters lock independent scores BEFORE discussion.
5.2 Differences of 2+ points are resolved by citing transcript evidence against the anchor.
5.3 A score changes only when evidence or anchor interpretation changes - never by seniority.
5.4 Log rubric wording that caused disagreement for the next revision.

## 6. Virtual interviews
6.1 Confirm a backup channel before starting.
6.2 A technical failure is never scored against the candidate.
6.3 Repeat the affected question and record the incident.

## 7. Feedback and closing
7.1 Give candidates time for questions and state next steps and timing.
7.2 Feedback cites observed evidence and its impact on a criterion; never a
    personality label. Offer one specific, actionable improvement.

## 8. Records
Retain the guide, notes, independent scores, calibration rationale and the decision.
{FOOTER}"""

JD = {
 "FutureTech-Careers": ("Senior Data Analyst", """## Purpose
Deliver reliable analysis that changes decisions for the product and commercial teams.

## Key tasks
- Build and maintain trusted reporting for revenue, activation and retention.
- Investigate metric movements and explain the cause with evidence.
- Improve data quality: reconcile sources, document definitions, fix breakages.
- Partner with product and finance stakeholders to frame questions before analysis.
- Mentor one or two junior analysts through review and pairing.

## Competencies assessed at interview
1. Analytical rigour - validates assumptions, reconciles sources before publishing.
2. Stakeholder communication - explains a technical finding to a non-technical decision maker.
3. Data quality ownership - detects, escalates and fixes definition or pipeline issues.
4. Prioritisation - chooses between competing requests using impact.
5. Mentoring - improves another analyst's work without doing it for them.

## Requirements
- Strong SQL; Python or R for analysis; a BI tool (Power BI or Tableau).
- Experience owning a recurring reporting product end to end.
- Evidence of a decision that changed because of the candidate's analysis."""),
 "HarbourBank-Talent": ("Credit Risk Analyst", """## Purpose
Assess and monitor credit risk across the SME lending portfolio.

## Key tasks
- Build and validate scorecards; monitor performance and drift.
- Prepare portfolio analytics and early-warning reporting.
- Support MAS regulatory reporting and internal stress testing.
- Document model assumptions and limitations for audit.

## Competencies assessed at interview
1. Quantitative judgement - reasons about model limits, not just outputs.
2. Regulatory awareness - applies MAS expectations to daily work.
3. Data handling - reconciles and validates before reporting.
4. Communication - explains risk to a lending decision maker.
5. Control mindset - documents, escalates and challenges appropriately.

## Requirements
- SQL and a statistical toolset (SAS, Python or R).
- Understanding of credit scoring and IFRS 9 concepts.
- Evidence of challenging a number that turned out to be wrong."""),
 "MediCare-Recruitment": ("Staff Nurse", """## Purpose
Deliver safe, patient-centred nursing care within the ward team.

## Key tasks
- Assess patients, administer medication and escalate deterioration.
- Maintain accurate clinical records.
- Apply infection-control and patient-safety protocols.
- Support families with clear, compassionate communication.

## Competencies assessed at interview
1. Clinical judgement - recognises and escalates deterioration.
2. Patient safety - follows and challenges protocol appropriately.
3. Communication under pressure - with patients, families and doctors.
4. Teamwork - handover quality and support for colleagues.
5. Resilience and reflection - learns from a difficult episode.

## Requirements
- Registered with the Singapore Nursing Board.
- Evidence of a safety issue the candidate personally raised or acted on.
- NOTE: health and disability questions are prohibited except where a genuine
  occupational requirement is documented and approved by the Head of People."""),
 "GreenLogix-Hiring": ("Supply Chain Analyst", """## Purpose
Improve inventory availability and cost through better forecasting and analysis.

## Key tasks
- Produce demand forecasts and track forecast accuracy.
- Identify excess and obsolete stock and propose action.
- Build supplier scorecards and support sourcing reviews.
- Maintain the weekly operations reporting pack.

## Competencies assessed at interview
1. Analytical modelling - builds and sanity-checks a forecast.
2. Commercial judgement - trades off service level against working capital.
3. Supplier communication - raises performance issues constructively.
4. Systems fluency - SAP/WMS and advanced Excel or SQL.
5. Process improvement - changes a routine that was not working.

## Requirements
- Advanced Excel; SQL or SAP exposure.
- Evidence of a recommendation that reduced cost or improved availability."""),
 "BrightPath-Careers": ("Curriculum Developer", """## Purpose
Design learning programmes that measurably improve learner outcomes.

## Key tasks
- Design modules, activities and assessments to stated outcomes.
- Work with subject experts to convert expertise into teachable material.
- Pilot, gather feedback and revise.
- Maintain accessibility and quality standards across the catalogue.

## Competencies assessed at interview
1. Instructional design - aligns outcome, activity and assessment.
2. Subject-expert collaboration - extracts and structures expertise.
3. Evidence use - revises based on learner data, not preference.
4. Accessibility - designs for varied learner needs.
5. Delivery discipline - ships to deadline at quality.

## Requirements
- Portfolio of designed programmes with outcome evidence.
- Familiarity with an LMS and assessment design."""),
}

def jd_doc(co, role, body):
    return f"# {co} - Job Description: {role}\nDocument: JD-{role.replace(' ','-').upper()} | Approved by Head of People\n\n{body}\n{FOOTER}"

def main():
    for site, (co, _sector) in COMPANIES.items():
        d = os.path.join(SP, site, "HR-Policies")
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "HR-POL-01 Fair and Inclusive Hiring Policy.md"), "w").write(fair_hiring(co))
        open(os.path.join(d, "HR-POL-02 Responsible Use of Generative AI in Recruitment.md"), "w").write(ai_use(co))
        open(os.path.join(d, "HR-SOP-03 Structured Interview SOP.md"), "w").write(interview_sop(co))
        jd_d = os.path.join(SP, site, "Job-Descriptions")
        os.makedirs(jd_d, exist_ok=True)
        role, body = JD[site]
        open(os.path.join(jd_d, f"JD - {role}.md"), "w").write(jd_doc(co, role, body))
        print(f"  {site}: 3 policies + 1 JD ({role})")

if __name__ == "__main__":
    main()
