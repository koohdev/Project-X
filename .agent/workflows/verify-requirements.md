---
description: Verify a finished chapter against the DCT CCS minimum requirements matrix, checking all mandatory sections, diagrams, and content elements
---

# /verify-requirements Workflow

## PURPOSE

Cross-reference a finished chapter against the **Minimum Requirements Quick Reference** from the DCT CCS Capstone Manual (stored in `[00] CONFIG_AND_PROMPTS/KNOWLEDGE_BASE.md`). This workflow acts as a pre-submission compliance gate — after you're happy with the writing quality, run this to ensure no required section is missing.

> [!IMPORTANT]
> This workflow checks for **structural completeness** (required sections, diagrams, tables, element counts), NOT writing quality. For writing quality, use `/check-writing` or `/audit-chapter`.

---

## PROJECT CONTEXT

- **Project:** Chronicles of Arithmos: A 2D RPG-Based Mathematics Learning Application for Grades 4–6
- **Chapters Location:** `[04] OUR_PROJECT/`
- **Requirements Authority:** `[00] CONFIG_AND_PROMPTS/KNOWLEDGE_BASE.md` PART 1 (Section-by-Section Content Guide)
- **Output Location:** `[06] CHECKING REPORTS/` root (as a standalone results file)
- **Proponents Term:** "The proponents"

---

## STEPS

// turbo-all

### Step 1: Identify the Target Chapter

Determine which chapter to verify:
- If the user specifies a file → use that file.
- If the user says "verify chapter X" → locate `[COA]-CHAPTER-X.md` in `[04] OUR_PROJECT/`.
- If the user says "verify chapter 1" → look in `[04] OUR_PROJECT/[04-1 CHAPTER 1]/`.
- If neither → use the user's **currently active document**.

Read the full content of the target file.

Determine the chapter number `{X}` and chapter title from the content.

### Step 2: Load the Requirements Matrix

Read `[00] CONFIG_AND_PROMPTS/KNOWLEDGE_BASE.md` and extract the requirements for the target chapter from **PART 1**.

Build an internal checklist of every mandatory element for that chapter:

**Chapter 1 Requirements:**
- [ ] 1.1 Project Context — minimum 2 pages; covers global, national, local scope; justification provided
- [ ] 1.2.1 General Objective — single clear paragraph
- [ ] 1.2.2 Specific Objectives — SMART list, each objective is specific/measurable/achievable/realistic/time-bound
- [ ] 1.3 Scope — extent of prototype described; all major modules listed
- [ ] 1.3 Limitations — each limitation separately justified; conditions beyond control

**Chapter 2 Requirements:**
- [ ] Related Theories section present
- [ ] At least one Anchor Theory explicitly identified
- [ ] Supporting theories connect anchor theory
- [ ] All theories cited with correct `[CODE_YEAR]` format
- [ ] Related Projects/Systems section present
- [ ] 3–6 related systems reviewed
- [ ] Each system has: Overview, Similarities, Differences
- [ ] Comparative Matrix table present
- [ ] Screenshots mentioned or included for each related system

**Chapter 3 Requirements:**
- [ ] 3.1 Development section present
  - [ ] Hardware (development machines)
  - [ ] Software (all tools used during development)
  - [ ] Peopleware (proponents + adviser)
  - [ ] Network (development network setup)
- [ ] 3.2 Implementation section present
  - [ ] Hardware (end-user minimum specs — with table)
  - [ ] Software (OS, browser requirements)
  - [ ] Peopleware (student users, teachers, guardians)
  - [ ] Network (internet requirements)
- [ ] Each tool entry follows the 4-part formula: WHAT → WHERE USED → WHY → OUTCOME
- [ ] Hardware requirement tables present (Table #1, Table #2)

**Chapter 4 Requirements:**
- [ ] Development model identified and justified (Prototyping, SDLC, Agile, etc.)
- [ ] Each phase of the model has: activities performed, stakeholders, inputs, outputs
- [ ] 4.3.1 Operational Feasibility: Fishbone Diagram present; FDD present
- [ ] 4.3.2 Technical Feasibility: Compatibility Checking (hardware + software); Relevance of Technology
- [ ] 4.3.3 Schedule Feasibility: Gantt Chart table covering full project duration
- [ ] 4.3.4 Economic Feasibility: Cost and Benefit Analysis table; Cost Recovery Scheme
- [ ] 4.3.5 Requirements Modeling: at least one diagram from Data/Process OR Object Modeling (Use Case, Sequence, Activity, DFD, etc.)
- [ ] 4.3.6 Risk Assessment: Risk matrix table with at minimum 3 identified risks
- [ ] 4.4.1 Output and UI Design: color scheme documented; typography documented; sample UI screenshots or descriptions
- [ ] References section present at end of chapter

**Chapter 5 Requirements:**
- [ ] Conclusions reference all specific objectives from Chapter 1.2.2
- [ ] Conclusions present findings/results (past tense)
- [ ] Recommendations provided for future developers
- [ ] Recommendations suggest enhancements and alternative solutions

### Step 3: Scan the Chapter

Go through the target chapter and check each item in the requirements matrix.

For each item:
- ✅ **PRESENT** — the section/element exists and appears complete
- ⚠️ **PARTIAL** — the section exists but is missing sub-elements or is too thin (< 2 sentences)
- ❌ **MISSING** — the section or element does not appear in the chapter

Track specific evidence for each ✅ (e.g., "Comparative Matrix found at line 87 — Table 2.1").
Track specific gap for each ⚠️ and ❌ (e.g., "Limitations found but no justification provided for Limitation B").

### Step 4: Compile the Verification Report

Build a structured report with the following sections:

```
# ✅ Chapter {X} Requirements Verification Report

> **File Checked:** [filename]
> **Date:** [date]
> **Chapter:** [title]

---

## Compliance Summary

| Status | Count |
|--------|-------|
| ✅ Present & Complete | {N} |
| ⚠️ Partial / Thin | {N} |
| ❌ Missing | {N} |
| **Overall Score** | **{N}/{TOTAL} ({%}%)** |

---

## Detailed Findings

### ✅ Compliant Elements
[List each passing item with evidence]

### ⚠️ Partial Elements (Action Required)
[List each partial item with the specific gap and how to fix it]

### ❌ Missing Elements (Must Fix Before Submission)
[List each missing item with its Knowledge Base reference and what content to add]

---

## Priority Action List

| Priority | Gap | What to Add |
|----------|-----|-------------|
| 🔴 HIGH | [missing element] | [specific content needed] |
| 🟡 MED | [partial element] | [what to expand] |

---

## Verdict

- **READY FOR SUBMISSION:** All required elements present (100%)
- **NEEDS MINOR FIXES:** Minor gaps — fix ⚠️ items before submitting
- **NOT READY:** Critical elements missing — fix ❌ items first
```

### Step 5: Save the Report

Save to: `[06] CHECKING REPORTS/VERIFY-CHAPTER-{X}-REQUIREMENTS.md`

If the file already exists → **overwrite it**.

### Step 6: Update the WIP Progress Tracker

Open `[04] OUR_PROJECT/WIP/CHAPTER-{X}-PROGRESS.md`.

If a "Requirements Verification" section exists → update it.
If not → append this block to the end:

```markdown
---

## Requirements Verification (auto-generated)

- [x/] Ran `/verify-requirements` on [date]
- [ ] All ❌ MISSING items resolved
- [ ] All ⚠️ PARTIAL items expanded
- **Last Score:** {N}/{TOTAL} ({%}%)
```

### Step 7: Report to User

Print a brief summary:
- Overall score: `{N}/{TOTAL}`
- Count of ❌ MISSING and ⚠️ PARTIAL items
- Top 3 gaps to address (highest priority)
- Path to the saved verification report

---

## USAGE EXAMPLES

```
/verify-requirements                    → verifies the currently active document
/verify-requirements chapter 2          → verifies [COA]-CHAPTER-2.md
/verify-requirements chapter 4          → verifies [COA]-CHAPTER-4.md
```

## NOTES

- This workflow does NOT edit or rewrite content — it reports gaps only.
- After resolving gaps, re-run `/verify-requirements` to confirm all items pass before `/audit-chapter`.
- Recommended order: **Draft → `/verify-requirements` → fix gaps → `/audit-chapter` → apply fixes**.
- A chapter should score **100%** on requirements AND pass `/audit-chapter` before it is moved to `READY_FOR_REVIEW/`.
