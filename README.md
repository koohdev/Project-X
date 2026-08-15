# 📘 PROJECT CARL — Capstone Project & Documentation Workspace

> **Dominican College of Tarlac (DCT) — College of Computer Studies (CCS)**  
> **Bachelor of Science in Information Technology (BSIT)**  
> **Capstone Project Title:** *Chronicles of Arithmos: An Adaptive 2D Educational RPG for Mathematics Anxiety Reduction*

---

## 🎯 Repository Purpose (What You Are Achieving)

From a birds-eye perspective, this entire workspace serves a **dual objective**:

```mermaid
graph TD
    subgraph "1. The Capstone Project: Chronicles of Arithmos"
        A[Game Concept & Mechanics] --> B[RPG Maker MZ 2D Engine]
        B --> C[Math Battle Combat & Adaptive Scaling]
        C --> D[Game Assets, Database & Biomes]
    end

    subgraph "2. The Academic Manuscript & Compliance Engine: PROJECT CARL"
        E[DCT CCS Capstone Manual & Rubrics] --> F[.agents/skills/dct-ccs-capstone-guide]
        F --> G[Formatted Chapters 1.0 - 5.0 in [02] OUR_PROJECT]
        G --> H[Plagiarism & AI Tone Sanitizer: humanizer]
        H --> I[Oral Defense & Panel Approval]
    end

    D -.-> G
```

1. **The Actual IT Project**: Developing **"Chronicles of Arithmos"**, a 2D turn-based educational RPG built in RPG Maker MZ. It replaces stochastic dice-rolls with timed mental math arithmetic (PEMDAS) to combat the *"chocolate-covered broccoli"* effect and mitigate Mathematics Anxiety in learners.
2. **The Compliance & Manuscript Engine**: Automating the drafting, auditing, formatting, and rubric alignment of the entire 5-chapter manuscript, ensuring 100% adherence to DCT CCS standards (Times New Roman, 1.5" left margin, no bullet symbols in body text, `[AUTH2024]` citations, SMART objectives, and 50-point rubric criteria).

---

## 📂 Directory Roadmap & Architecture

| Directory / File | Core Purpose & Role |
| :--- | :--- |
| **`.agents/skills/`** | **AI Agent Skills Engine**: Houses `dct-ccs-capstone-guide` (DCT manual rules, rubrics, chapter specs), `humanizer` (tone de-AI tool), and `skill-creator`. |
| **`[01] CURRENT_KNOWLEDGE/`** | **Formatting Standard Archive**: Quick references for paragraph hierarchy, section numbering, and tone rules. |
| **`[02] OUR_PROJECT/`** | **Core Manuscript Drafts**: Complete working chapters (`final-chapter-1.md`, `final-chapter-2.md`, `final-chapter-3.md`, `final-chapter-4.md`) detailing Chronicles of Arithmos. |
| **`[03] DIAGRAMS/`** | **System & Feasibility Architecture**: Draw.io vector source diagrams including Fishbone Root-Cause Diagram and Functional Decomposition Diagram (FDD). |
| **`[04] PROJECT_DATABASE/`** | **Game Data Dictionaries & Entities**: Markdown catalogs for Characters, NPCs, Enemies, Items, Equipment, Skills/States, Audio/BGM, and Unified Tables. |
| **`[05] TASK DISTRIBUTION/`** | **Team Governance (Appendix A)**: Official role breakdown (PM, SA/DD, ND/UID, SE/P, QA/TW) and member contributions. |

---

## 🕹️ Project Snapshot: Chronicles of Arithmos

* **Genre / Engine**: 2D Turn-Based Educational Role-Playing Game (RPG Maker MZ, JS/Canvas).
* **Target Problem**: Mathematics Anxiety (Ashcraft, 2002; Richardson & Suinn, 1972) and lack of engagement in traditional arithmetic drills.
* **Core Innovation**:
  * **Math Battle Engine**: In-combat actions, attack power, and defense execution are driven by player mental calculations under time constraints.
  * **Adaptive Difficulty Tracking**: Dynamic equation difficulty scaling matching the player's proficiency to maintain flow state.
  * **Low-Stakes Learning**: Failures result in in-game resets rather than real-world penalties; Town Training Halls enable stress-free practice against test dummies.
* **Project Category**: Computer-Aided Instruction (CAI) & Multimedia Systems.
  * *Constraint compliance*: $\ge 4$ media types, 50 test items per topic, no DFDs used (storyboards, flowcharts, HIPO instead).

---

## 🛠️ Workflows: How to Use Agent Skills

### 1. Writing & Refining Chapters
To draft or expand any manuscript chapter:
```text
"Draft Section 4.3 Requirements Specification for Chronicles of Arithmos following DCT guidelines"
```
The `dct-ccs-capstone-guide` skill automatically enforces:
* 2-page minimum Project Context.
* SMART Specific Objectives starting with *"To develop..."* / *"To design..."*.
* 1.5" left margin, TNR 12/11pt typography, and `[AUTH2024]` citations.
* Categorical `A., B., C.` lists with complete 2–5 sentence paragraphs (no raw bullets).

### 2. Auditing & De-AI Tone Cleaning
To review drafts and eliminate synthetic AI writing patterns:
```text
"Run humanizer and audit final-chapter-1.md against the DCT 50-point rubric"
```

---

## 📊 DCT CCS Grading Distribution

$$\text{Final Grade} = (\text{Panel Average} \times 0.60) + (\text{Adviser Grade} \times 0.30) + (\text{Peer Grade} \times 0.10)$$

* **Proposal Defense (Capstone 1)**: Manuscript (40%) + Oral Examination (20%).
* **Final Defense (Capstone 2)**: Software Output (30%) + Oral Examination (20%) + Manuscript (10%).
* **Verdict Thresholds**:
  * *Approved*: 35–40 pts (Minor revisions).
  * *Approved with Revisions*: 24–34 pts (Major panel revisions).
  * *Disapproved*: Below 24 pts.
