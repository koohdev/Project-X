# 📘 PROJECT CARL — Capstone Documentation & Compliance Assistant

> **AI-powered assistant and compliance engine for Dominican College of Tarlac (DCT) College of Computer Studies (CCS) BSIT Capstone projects.**

Follows every rule in the official DCT CCS Capstone Manual, CMO 25 s. 2015, and the unified Project CARL knowledge base.

---

## 🚀 Quick Start

### Using Antigravity / Agent Skills (Recommended)
This workspace is pre-configured with agent skills in `.agents/skills/`:
* **`dct-ccs-capstone-guide`**: Automatic formatting, chapter writing, rubric audits, SMART objectives, and compliance checks.
* **`humanizer`**: Cleans synthetic phrasing, eliminates AI writing patterns, and refines academic tone.

Simply ask in chat:
```text
"Draft Section 1.1 Project Context for our Library Management System"
"Audit Chapter 3 according to DCT CCS formatting rules"
"Generate SMART Specific Objectives for an Online Ordering System"
```

### Using in Google AI Studio (GEM Setup)
If uploading to an external Gemini GEM:
1. Create a GEM named `PROJECT CARL`.
2. Upload references from `.agents/skills/dct-ccs-capstone-guide/references/` (or `[01] CURRENT_KNOWLEDGE/`).
3. Set system instructions to enforce DCT CCS documentation standards.

---

## 📖 What You Can Generate & Audit

### 📄 Manuscript Sections
| Section | Example Prompt |
| :--- | :--- |
| **Abstract** | *"Write a 150–200 word abstract without citations for our enrollment system"* |
| **1.1 Project Context** | *"Generate 2-page project context covering global, national, and local scopes"* |
| **1.2.1 General Objective** | *"Draft the single-paragraph major objective for our hospital system"* |
| **1.2.2 Specific Objectives** | *"Convert these modules into SMART specific objectives (What + How + Result)"* |
| **1.3 / 1.4 Scope & Limitations** | *"Draft Scope (1.4.1) and Limitations (1.4.2) with justifications for our project"* |
| **Chapter 2.0 Literature** | *"Structure Chapter 2 with anchor theory, supporting theories, and comparative matrix"* |
| **Chapter 3.0 Technical Background**| *"Write Chapter 3.1 & 3.2 across Hardware, Software (A.1/B.1), Peopleware, Network"* |
| **Chapter 4.0 Methodology** | *"Draft Chapter 4 covering SDLC, 4 feasibility studies, testing, and conversion"* |
| **Chapter 5.0 Conclusions** | *"Map findings 1-to-1 to Chapter 1 specific objectives with future recommendations"* |

### 📊 Diagrams & Specifications
| Diagram / Spec | Purpose & Format |
| :--- | :--- |
| **Fishbone & FDD** | Operational feasibility root-cause & functional hierarchy breakdown |
| **Gantt Chart** | Schedule feasibility marking timeline intervals |
| **CBA & Cost Recovery** | Economic feasibility tangible/intangible ROI and payback period |
| **DFD / Flowcharts / UML** | Process & object modeling (Context, DFD Level 1, Use Case, Sequence; *no DFD for CAI*) |
| **ERD & Data Dictionary** | Data design entity relationships, fields, types, constraints, and keys |
| **Screen Design (Appendix H)**| UI specifications: Screen No., Name, Narrative Overview, Layout |

---

## 📂 Workspace Structure

```text
PROJECT CARL/
├── README.md                             # 📘 Project manual and quick reference
├── skills-lock.json                      # Agent skills configuration lockfile
│
├── .agents/skills/                       # 🧠 Active Agent Skills
│   ├── dct-ccs-capstone-guide/           # Core DCT CCS Capstone standard skill
│   │   ├── SKILL.md                      # Master workflows and compliance checklists
│   │   └── references/                   # Deep reference modules
│   │       ├── 01-program-and-governance.md  # Vision/Mission, IT01-IT13, team roles
│   │       ├── 02-grading-and-verdicts.md    # 60/30/10 formula, rubrics, verdicts
│   │       ├── 03-chapter-specifications.md  # Detailed specs for Ch 1.0–5.0
│   │       ├── 04-formatting-and-templates.md# 1.5" margin, TNR 12/11pt, [AUTH2024] syntax
│   │       ├── 05-research-and-integrity.md  # Category metrics, unacceptable projects, IP
│   │       └── 06-writing-style-and-tone.md  # Tone dictionary, paragraph rules, no bullets
│   ├── humanizer/                        # Natural academic tone and de-AI writing skill
│   └── skill-creator/                    # Skill benchmarking and creation tool
│
├── [01] CURRENT_KNOWLEDGE/               # Reference copies of formatting rules
│   ├── Capstone_Formatting_Rules.md      # Structure enforcement reference
│   └── Specific_Format.md                # Quick layout reference
│
├── [02] OUR_PROJECT/                     # Working capstone manuscript chapters
│   ├── final-chapter-1.md                # Chapter 1 (Introduction)
│   ├── final-chapter-2.md                # Chapter 2 (Literature & Related Systems)
│   ├── final-chapter-3.md                # Chapter 3 (Technical Background)
│   └── final-chapter-4.md                # Chapter 4 (Methodology & Results)
│
├── [03] DIAGRAMS/                        # System and feasibility diagrams (.drawio)
│   ├── FDD_FUNCTIONAL_DECOMPOSITION.drawio
│   └── FISHBONE_DIAGRAM.drawio
│
├── [04] PROJECT_DATABASE/                # Game/system entity datasets & data dictionaries
│   ├── 01_Characters_and_NPCs.md
│   ├── 02_Enemies.md
│   ├── 03_Items.md
│   ├── 04_Equipment.md
│   ├── 05_Skills_and_States.md
│   ├── 06_Audio_and_BGM.md
│   └── 07_ALL.md
│
└── [05] TASK DISTRIBUTION/               # Team member role assignments (Appendix A)
    └── task_distribution.md
```

---

## 📏 Mandatory Project Baselines & Rules

### 1. Transaction Processing Systems (TPS)
* **Payroll**: $\ge 50$ employees, timekeeping, tax tables (SSS, BIR, PhilHealth, Pag-IBIG), payslips.
* **Sales & Inventory**: $\ge 1,000$ inventory items, 5–10 product lines (5–10 items/line), reorder points.
* **Library**: $\ge 2,000$ book titles (CHED), $\ge 500$ students/members, circulation, overdue penalty.
* **Accounting**: AR/AP monitoring, aging technique, journal posting, 30 accounts test baseline.
* **Enrollment**: $\ge 200$ students, $\ge 2$ sections per year level, prerequisites tracking.
* **Hotel Reservation**: $\ge 20$ rooms, $\ge 100$ customer capacity, automated billing.
* **Hospital/Patient**: $\ge 20$ beds, $\ge 50$ patients, admitting, diagnosis, auto-billing.

### 2. Specialized Project Rules
* **CAI**: $\ge 4$ media types, 2–3 presentation methods, 50 test items/topic, random test generator. **DFDs are prohibited**; use Storyboarding, Flowcharts, and HIPO.
* **Web Applications**: Host client required, **must be deployed on live server**, dynamic DB pages, e-consultation module.
* **Multimedia Systems**: $\ge 4$ media types, dynamic content management, media database, multi-tier user levels.

### 3. ❌ Strictly Rejected Projects
* DAMATH or simple board games
* Video Rental Systems
* Generic non-educational card games
* Basic CRUD Record Keeping without operational depth
* Generic Monitoring Systems without automated control/telemetry
* Static LGU / Barangay Websites

---

## 📐 Formatting Standards Summary

| Element | Standard |
| :--- | :--- |
| **Paper** | Letter ($8.5 \times 11\text{ in}$), Substance 20, Portrait |
| **Margins** | Top: 1.0", Left: **1.5"** (binding), Bottom: 1.0", Right: 1.0" |
| **Line Spacing** | Strictly **1.5 lines** throughout |
| **Paragraph Indent** | **1.0 inch** first-line indent |
| **Font** | Strictly **Times New Roman** (Heading 1: 12pt Bold, Heading 2: 12pt Bold, Heading 3/Body: 11pt Regular) |
| **Pagination** | Bottom-Right. Roman numerals for preliminary pages; decimal numbers from Ch 1 page 1. No page # on first page of chapters. |
| **Citations** | Bracketed author-year code `[AUTH2024]`. **Zero traditional footnotes.** |
| **List Rule in Body** | **NO BULLET SYMBOLS** (`•`, `-`, `*`, `▪`). Use **A., B., C.** or **1., 2., 3.** with complete 2–5 sentence paragraphs. |

---

## 📊 Grading Rubrics Summary

### Overall Grade
$$\text{Final Grade} = (\text{Panel Average} \times 0.60) + (\text{Adviser} \times 0.30) + (\text{Peer} \times 0.10)$$

### Component Distribution
* **Capstone 1 (Proposal)**: Manuscript 40% (out of 50 pts) + Oral Examination 20% (out of 20 pts).
* **Capstone 2 (Final)**: Capstone Software 30% (out of 30 pts) + Oral Examination 20% (out of 20 pts) + Manuscript 10% (out of 50 pts).
* **Adviser Grade (30 pts)**: Deliverables (20 pts) + Attendance (5 pts) + Journal & Attitude (5 pts).

### Verdict Thresholds
* **Capstone 1**: Approved (35–40 pts), Approved with Revisions (24–34 pts), Disapproved (<24 pts).
* **Capstone 2**: Accepted with Revisions (31–50 pts), Re-Oral Defense (21–30 pts), Not Accepted (<21 pts).
