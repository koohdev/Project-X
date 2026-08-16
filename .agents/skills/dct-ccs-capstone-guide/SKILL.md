---
name: dct-ccs-capstone-guide
description: Authoritative guide, compliance checker, and formatting/drafting standard for BS Information Technology Capstone projects according to the Dominican College of Tarlac (DCT) College of Computer Studies (CCS) Capstone Manual and unified Project CARL Knowledge Base. Make sure to use this skill whenever the user is drafting, editing, reviewing, structuring, or auditing Capstone manuscripts (Chapters 1.0 to 5.0, Preliminary Pages, Appendices A-J), formatting citations and pages, sanitizing AI writing tone, preparing for proposal or final oral defense, checking rubrics and score thresholds, or verifying project compliance against DCT CCS standards.
---

# DCT CCS Capstone Guide

A specialized skill for guiding, writing, structuring, formatting, and auditing BS Information Technology Capstone projects and manuscripts under the **Dominican College of Tarlac (DCT) College of Computer Studies (CCS)** Capstone Manual and unified **Project CARL Knowledge Base**.

---

## 1. Quick Reference Navigation (Progressive Disclosure)

Consult the dedicated reference modules in `references/` for full details:

* **[Program & Governance](references/01-program-and-governance.md)**: Institutional Vision/Mission, Program Outcomes (IT01–IT13), Team Roles (PM, SA/DD, ND/UID, SE/P, QA/TW), Project Stages, and Adviser/Panel duties.
* **[Grading & Verdicts](references/02-grading-and-verdicts.md)**: Final grade computation (60% Panel / 30% Adviser / 10% Peer), detailed rubrics (Manuscript 50 pts, Software 30 pts, Oral 20 pts, Adviser 30 pts), and defense verdicts.
* **[Chapter Specifications](references/03-chapter-specifications.md)**: Deep section-by-section requirements for Chapters 1.0 through 5.0 (SMART objectives, SDLC models, Feasibility, Modeling, Testing matrices, Implementation plans).
* **[Formatting & Templates](references/04-formatting-and-templates.md)**: Physical paper standards, margins (1.5" left), fonts (Times New Roman 12/11pt), bracket citations `[AUTH2024]`, Preliminary pages, and Appendices A–J formats.
* **[Research Areas & Integrity](references/05-research-and-integrity.md)**: Project category baselines (TPS, MIS, DSS, GIS, CAI, Web, AI), unacceptable project list, IP transfer policy, and plagiarism clearance procedures.
* **[Writing Style & Tone Sanitation](references/06-writing-style-and-tone.md)**: Academic style rules, 2–5 sentence paragraphs, strict prohibition of bullet symbols in body text (use A., B., C. / 1., 2., 3.), and banned words dictionary.

---

## 2. Core Operational Workflows

### Workflow A: Chapter Drafting and Structuring

When drafting or expanding any manuscript section:
1. **Identify Chapter Context**: Check the required subsections and diagrams in [Chapter Specifications](references/03-chapter-specifications.md).
2. **Apply Mandatory Constraints**:
   * **Chapter 1.1 (Project Context)**: Ensure a minimum of **two (2) full pages** covering global, national, and local context plus researcher justification.
   * **Chapter 1.2 / 1.3 (Objectives)**: State General Objective in 1 paragraph; format Specific Objectives as **SMART** numbered statements beginning with active verbs (*"To develop..."*, *"To design..."*, *"To implement..."*) following What + How + Result.
   * **Chapter 1.3 / 1.4 (Scope & Limitations)**: Ensure every limitation includes an explicit operational justification.
   * **Chapter 2.0 (Literature)**: Begin with an **Anchor Theory**, followed by supporting theories. Include a comparative matrix evaluating 3–6 existing systems with UI screenshots.
   * **Chapter 3.0 (Technical Background)**: Structure by 3.1 Development & 3.2 Implementation across **Hardware, Software, Peopleware, Network**.
   * **Chapter 4.0 (Methodology & Results)**: Follow SDLC methodology strictly; include all 4 feasibility studies (Fishbone, Gantt, CBA), requirements modeling (DFD or UML; *no DFD for CAI*), multi-tier testing (Unit, Integration, System, Acceptance), and conversion plan (Direct, Phased, or Parallel).
   * **Chapter 5.0 (Conclusions & Recommendations)**: Align conclusions 1-to-1 with Chapter 1 specific objectives; provide actionable, feasible recommendations.
3. **Format Layout & Citations**: Apply Times New Roman fonts, 1.5 spacing, 1-inch indent, and `[AUTH2024]` citations from [Formatting & Templates](references/04-formatting-and-templates.md).
4. **Tone & Style Sanitation**: Ensure no bullet symbols exist in body text (use A., B., C. or 1., 2., 3. full paragraphs), sanitize banned buzzwords, and maintain third-person impersonal voice per [Writing Style & Tone Sanitation](references/06-writing-style-and-tone.md).

---

### Workflow B: Manuscript Compliance & Quality Audit

When reviewing an existing capstone document or chapter draft:
1. **Structural Audit**:
   * Verify all mandatory sub-headings exist per the DCT documentation outline.
   * Check preliminary pages (Title Page, Adviser Recommendation, Dean Acceptance, Panel Approval, Abstract without quotes/citations in 150–200 words, TOC, List of Tables/Figures).
   * Check appendices completeness (Appendices A to J).
2. **Formatting & Mechanics Audit**:
   * **Paper & Margins**: Top: 1", Left: 1.5", Bottom: 1", Right: 1". Spacing: 1.5 lines. Indent: 1.0".
   * **Typography**: Heading 1 (12pt Bold), Heading 2 (12pt Bold), Heading 3/Content (11pt Regular). Font: Times New Roman.
   * **Table & Figure Captions**: Table captions above table (`Table <ch>-<tbl> <Title>`), Figure captions below figure (`Figure <ch>-<fig> <Title>`).
   * **Citation Syntax**: Verify no traditional footnotes exist. Verify all citations follow `[AUTH2024]` format.
   * **List Check**: Ensure zero bullet characters (`•`, `-`, `*`, `▪`) in body text.
3. **Rubric Score Alignment**:
   * Evaluate the draft against the 50-point Manuscript Rubric in [Grading & Verdicts](references/02-grading-and-verdicts.md).
   * Flag any gaps that would deduct points from the panel rating.

---

### Workflow C: Project Scope & Acceptability Verification

When vetting a new project proposal:
1. **Unacceptable Project Check**: Confirm project is not in the prohibited list (DAMATH, video rental, basic record keeping, generic monitoring without hardware/analytics, static municipal/barangay websites).
2. **Quantitative Baseline Check**: Verify the project meets minimum scope requirements (e.g., Payroll $\ge 50$ employees, Sales/Inventory $\ge 1,000$ items & 5–10 product lines, Library $\ge 2,000$ books & 500 members, Enrollment $\ge 200$ students, Web apps deployed with live client).
3. **Client Justification**: Ensure the system has an identified real-world beneficiary and a signed Certificate to Use Company Data (Appendix F).

---

## 3. Master Manuscript Section Checklist

```text
[ ] PRELIMINARY PAGES
    [ ] Title Page (Page i - unnumbered)
    [ ] Adviser's Recommendation Sheet (Page ii - unnumbered)
    [ ] Dean's Acceptance Sheet (Page iii - unnumbered)
    [ ] Panel's Approval Sheet (Page iv - unnumbered)
    [ ] Acknowledgement (Page v)
    [ ] Abstract (Page vi - 150-200 words, no citations, no "This study/project...")
    [ ] Table of Contents (Page vii)
    [ ] List of Tables (Page viii)
    [ ] List of Figures (Page ix)
    [ ] List of Notations (Optional)

[ ] 1.0 INTRODUCTION (Page 1)
    [ ] 1.1 Project Context (Min 2 pages: Global/National/Local, guide questions)
    [ ] 1.2 Objectives (1-para General Objective + SMART Specific Objectives)
    [ ] 1.3 Scope and Limitations (Prototype boundary + justified limitations in 1.3.1/1.3.2 with A., B., C.)

[ ] 2.0 REVIEW OF RELATED LITERATURE / SYSTEMS
    [ ] 2.1 Related Theories (Anchor theory + auxiliary theories + [AUTH2024] citations)
    [ ] 2.2 Related Projects (3-6 systems, comparative matrix, UI screenshots)

[ ] 3.0 TECHNICAL BACKGROUND
    [ ] 3.1 Development & 3.2 Implementation (Hardware, Software, Peopleware, Network)

[ ] 4.0 METHODOLOGY, RESULTS AND DISCUSSION
    [ ] 4.1 Methodology (SDLC model identification & diagram)
    [ ] 4.2 Environment (Locale, Population, Organizational Profile & Chart)
    [ ] 4.3 Requirements Specification
        [ ] Operational (Fishbone & Functional Decomposition Diagrams)
        [ ] Technical (Compatibility checking & tech relevance)
        [ ] Schedule (Gantt Chart with phase intervals)
        [ ] Economic (Cost-Benefit Analysis & Cost Recovery Scheme / ROI)
        [ ] Requirements Modeling (Context, DFD/Flowcharts OR UML Use Case/Class/Seq/Act; no DFD for CAI)
        [ ] Risk Assessment & Mitigation
    [ ] 4.4 Design
        [ ] Output & UI Design (Colors, typography, icons, DCT Screen Design forms)
        [ ] Data Design (ERD + comprehensive Data Dictionary)
        [ ] System Architecture (Network model, topology, security model)
    [ ] 4.5 Development (Software/hardware specs, environment, deployment diagram, test plan)
    [ ] 4.6 Verification, Validation, Testing (Unit, Integration, System, ISO 25010 Acceptance)
    [ ] 4.7 Implementation Plan (Physical environment, interfaces, functionality, data, security)
    [ ] 4.8 Installation Processes (Direct, Phased, or Parallel conversion strategy)

[ ] 5.0 CONCLUSION AND RECOMMENDATIONS
    [ ] 5.1 Conclusions (Directly mapped to SMART specific objectives)
    [ ] 5.2 Recommendations (Feasible future enhancements & domain applications)

[ ] FINAL MATTER
    [ ] References (MLA / DCT Bracket Format [AUTH2024])
    [ ] Resource Persons (Full details: Name, Title, Institution, Contact)
    [ ] Glossary (Alphabetized operational definitions)
    [ ] Appendices (A: Work Assignment, B: Def of Terms, C: Test Docs, D: User Manual,
                   E: Program Listing, F: Certifications, G: Accomplished Forms,
                   H: Screen Designs, I: Interviews/Surveys/Photos, J: CVs)
```
