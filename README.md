# 📘 PROJECT CARL — Capstone Documentation Editor

> **Your AI-powered assistant for creating DCT CCS-compliant Capstone documentation**

Transform your rough notes into polished, academically formatted chapters that follow every rule in the Dominican College of Tarlac's Capstone Manual.

---

## 🚀 Quick Start

### Step 1: Set Up the GEM in Google AI Studio

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Create a new **Gemini GEM**
3. Set the **Name**: `PROJECT CARL`
4. Set the **Description**: "Your AI-powered assistant for creating DCT CCS-compliant Capstone documentation"
5. Upload these knowledge files:
   - `[00] CONFIG_AND_PROMPTS/KNOWLEDGE_BASE.md` (required)
   - `[00] CONFIG_AND_PROMPTS/INSTRUCTIONS.md` (required)
   - `[01] CURRENT_KNOWLEDGE/Capstone_Formatting_Rules.md` (optional, for extra detail)

### Step 2: Start Using It

Just tell the GEM what you need:

```
"Write Section 1.1 Project Context for our Library Management System"
```

The GEM will generate properly formatted content with an audit summary.

---

## 📖 How to Use PROJECT CARL

### Basic Command Format

```
[Action] [Section/Chapter] for [Your Project Topic]
```

**Examples:**

- "Write the Abstract for our Inventory System"
- "Generate Chapter 3 Technical Background for a Hotel Reservation project"
- "Create specific objectives for a Payroll System"

---

## 🎯 What You Can Ask For

### 📄 Document Sections

| Section | Example Prompt |
|---------|----------------|
| **Abstract** | "Write an abstract for our student enrollment system" |
| **1.1 Project Context** | "Generate project context about online ordering for small businesses" |
| **1.2.1 General Objective** | "Create the general objective for a library system" |
| **1.2.2 Specific Objectives** | "Turn these bullet points into specific objectives: [your notes]" |
| **1.3 Scope & Limitations** | "Write scope and limitations for hospital patient management" |
| **Chapter 2** | "Generate related literature for inventory management systems" |
| **Chapter 3** | "Write technical background covering React, Node.js, MongoDB" |
| **Chapter 4** | "Create methodology section using RAD model" |
| **Chapter 5** | "Write conclusions based on these findings: [your notes]" |

### 📊 Diagrams & Charts

| Type | Example Prompt |
|------|----------------|
| **Gantt Chart** | "Create a Gantt chart for 6-month development cycle" |
| **Use Case Diagram** | "Generate use case diagram for admin and student users" |
| **Flowchart** | "Create a login process flowchart" |
| **ERD Description** | "Describe the ERD for student, course, and enrollment tables" |

### 📋 Templates

| Template | Example Prompt |
|----------|----------------|
| **Title Page** | "Show me the title page template" |
| **Adviser's Sheet** | "Generate adviser's recommendation sheet" |
| **Panel's Approval** | "Create panel approval sheet for our group" |
| **Screen Design** | "Format this screen design for Appendix H" |

### ❓ Information Queries

| Query | Example Prompt |
|-------|----------------|
| **Requirements** | "What are the minimum requirements for a Sales & Inventory system?" |
| **Grading** | "How is the Capstone manuscript graded?" |
| **Team Roles** | "What are the roles in a Capstone group?" |
| **Project Validity** | "Is a Video Rental System an acceptable project?" |

---

## ✅ Input Tips for Best Results

### DO ✓

```
✓ "Write Section 1.1 for our School Library Management System that helps 
   students search and borrow books. The library has 3,000 books and 
   serves 500 students."

✓ "Convert these objectives to proper format:
   - user login
   - book search
   - borrowing records
   - overdue notifications"

✓ "Generate Chapter 3 Technical Background. We're using:
   - Frontend: ReactJS, Tailwind CSS
   - Backend: Node.js, Express
   - Database: MongoDB
   - Hosting: Vercel"
```

### DON'T ✗

```
✗ "Write my capstone" (too vague)
✗ "Make it sound impressive" (against academic tone rules)
✗ "Add some innovative features" (uses banned word)
```

---

## 🚫 Banned Project Types

PROJECT CARL will **reject** these project types:

| ❌ Rejected | Reason |
|-------------|--------|
| DAMATH | Not acceptable |
| Video Rental System | Not acceptable |
| Card Games | Not acceptable |
| Non-educational Games | Not acceptable |
| Simple Record Keeping | Too basic |
| Basic Monitoring System | Too basic |
| Barangay/Municipal Websites | Not acceptable |

**If you submit a banned project type**, the GEM will respond with a rejection message and suggest alternatives.

---

## 📏 Minimum Requirements Reference

If your project is a Transaction Processing System (TPS), it must meet these minimums:

| Project Type | Key Minimums |
|--------------|--------------|
| **Payroll** | 50 employees, SSS/Tax tables |
| **Sales & Inventory** | 1,000 items, 5-10 product lines |
| **Library** | 2,000 books, 500 members |
| **Accounting** | AR/AP with aging technique |
| **Enrollment** | 200 students, 2 sections/year level |
| **Hotel Reservation** | 20 rooms, 100 customers |
| **Hospital/Patient** | 20 beds, 50 patients |

**Other Types:**

| Type | Requirements |
|------|--------------|
| **CAI** | 4+ media types, 50 test items/topic |
| **Web App** | Database-driven, deployed, security |
| **Multimedia** | 4+ media types, dynamic content |
| **Expert Systems** | Inference engine, knowledge base |

---

## 📝 Output Format

Every response from PROJECT CARL follows this format:

```markdown
[Generated Content]
- Properly numbered sections (1.0, 1.1, A., B., etc.)
- Academic tone
- Complete paragraphs (2-5 sentences)
- No banned words

---
**Audit Summary:** Section 1.1 generated with global→local scope structure. 
Banned words removed: "efficient" → "supports", "innovative" → removed. 
Format verified: 2 pages, proper transitions.
```

---

## 🔧 Automatic Corrections

PROJECT CARL automatically:

| Issue | Correction |
|-------|------------|
| Bullet points in body | Converts to A., B., C. format |
| "efficient" | Replaces with "supports" or removes |
| "innovative" | Removes or rephrases |
| "This paper..." | Rewrites to not start with "This..." |
| Single-line objectives | Expands to 2-3 sentence paragraphs |
| Missing justifications | Prompts you for details |

---

## 📊 Understanding Grading (So You Know What Matters)

PROJECT CARL knows how panelists grade your work:

### Manuscript Grading (50 pts)

| Section | Points | Key Criteria |
|---------|--------|--------------|
| Initial Pages | 4 | TOC consistent, abstract complete |
| Chapter 1 | 10 | Clear overview, SMART objectives |
| Chapter 2 | 8 | Recent literature, proper citations |
| Chapter 3 | 8 | Comprehensive tech discussion |
| Chapter 4 | 10 | SDLC methodology, complete specs |
| Final Pages | 3 | Conclusions match objectives |
| Appendices | 2 | All deliverables complete |
| Mechanics | 5 | Grammar, formatting, organization |

### Software Grading (30 pts)

| Criteria | Points |
|----------|--------|
| Matches proposal objectives | 10 |
| All features delivered | 10 |
| Design/aesthetics | 3 |
| Debugging competence | 7 |

### Oral Exam (20 pts)

| Criteria | Points |
|----------|--------|
| Comprehensive answers | 10 |
| Team contribution | 7 |
| English delivery | 3 |

---

## 📦 PROJECT CARL GEM Suite

PROJECT CARL is now a **suite of specialized GEMs** for your complete Capstone journey:

### 📘 Documentation GEM (Main)

**Purpose:** Generate DCT CCS-compliant written documentation  
**Use for:** Chapters 1-5, templates, formatting  
**Files:** `[00] CONFIG_AND_PROMPTS/INSTRUCTIONS.md`, `[00] CONFIG_AND_PROMPTS/KNOWLEDGE_BASE.md`

**Recommended Workflow:**

```
1. Documentation GEM → Generate Chapter 1
2. Review and finalize
3. Defend!
```

---

## 📂 File Structure

```
PROJECT CARL/
├── README.md                             # 📘 This manual
├── [00] CONFIG_AND_PROMPTS/              # Core AI rules and guidelines
│   ├── INSTRUCTIONS.md                   # AI behavior instructions
│   ├── KNOWLEDGE_BASE.md                 # Complete DCT CCS knowledge
│   └── ACADEMIC_WRITING_CHECKER.md       # Writing audit reference
│
├── [02] CURRENT_KNOWLEDGE/
│   ├── Capstone_Formatting_Rules.md      # Detailed formatting patterns
│   └── Specific_Format.md                # Quick structure reference
│
├── [01] CAPSTONE_GUIDELINES_CHAPTERS/         # Source chapters (reference)
│   ├── 00_Front_Matter.md
│   ├── 01_Introduction.md
│   ├── 02_Scope.md
│   ├── 03_Suggested_Areas.md
│   ├── 04_Project_Duration.md
│   ├── 05_Composition_of_Project_Groups.md
│   ├── 06_Adviser_Panel_Composition.md
│   ├── 07_Presentation.md
│   ├── 08_Grading_System.md
│   ├── 09_Verdicts.md
│   ├── 10_Documentation_Guidelines.md
│   └── 11_Areas_of_Research.md
│
├── [03] SCHOOL_CAPSTONE_GUIDELINES/
│   ├── Documentation_Guidelines.md       # Extract from manual
│   └── School_Capstone_Guidelines.md     # Extract from manual
│
├── [04] OUR_PROJECT/                          # User's working folder
│   ├── WIP/                                   # Work in progress drafts
│   └── READY_FOR_REVIEW/                      # Drafts ready for check
├── [05] REVISED_CHAPTERS_OR_SECTIONS/         # Revised chapters
├── [06] CHECKING REPORTS/                     # Audit and findings outputs
│   ├── [06-1] CHECKING DIFF/
│   ├── [06-2] CHECKING FINDINGS/
│   └── [06-3] CHECKING CLEANED/
├── [07] ARTIFACTS/                            # Generated artifacts
├── [08] DIAGRAMS/                             # Project diagrams
└── [99] ARCHIVE/                              # Superseded versions
```

---

## ❓ FAQ

### Q: Can I use this for Capstone 1 AND Capstone 2?

**A:** Yes! The GEM covers both proposal stage (Chapters 1-4 planning) and final defense (complete documentation).

### Q: What if the GEM asks me for more details?

**A:** Provide them! The GEM won't fabricate information. If it asks "What database are you using?", tell it specifically.

### Q: Can it write my entire Capstone?

**A:** It can generate each section, but you need to provide:

- Your project topic and scope
- Technical decisions (languages, frameworks)
- Research findings
- Test results

### Q: What if I disagree with the GEM's output?

**A:** You can ask it to revise: "Rewrite this section with more focus on security features" or "Expand the scope section."

### Q: Does it support Filipino/Tagalog?

**A:** The GEM is designed for English academic writing per DCT CCS standards, but you can ask it to explain concepts in Filipino if needed.

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| Output too short | Add more details to your input |
| Wrong section format | Specify the exact section number (e.g., "4.3.1") |
| GEM refuses project | Your project type may be banned; ask for alternatives |
| Missing technical details | Provide your tech stack explicitly |
| Output has banned words | This shouldn't happen; report if it does |

---

## 📞 Support

This GEM was built using the official **DCT CCS Capstone Manual**. If you find discrepancies between the GEM's output and current guidelines, update the `KNOWLEDGE_BASE.md` accordingly.

---

## 📜 Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | January 2026 | Complete overhaul with 8-part knowledge base, grading rubrics, team roles, verdicts |
| 1.0 | Initial | Basic documentation generation |

---

**Happy Capstone Writing! 🎓**

*Remember: The GEM helps you write better, but the ideas and research must be yours.*
