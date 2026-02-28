---
description: Check academic writing for AI phrasing, vague claims, person-view violations, jargon, and chapter relevance issues
---

# /check-writing Workflow

## Purpose
Audit capstone chapter text against the **ACADEMIC_WRITING_CHECKER.md** reference to flag and fix problematic wording before submission.

## Steps

1. **Read the checker reference file**
   - Open and review `ACADEMIC_WRITING_CHECKER.md` located in the project root (`Projext X GEM/`)
   - Also review `KNOWLEDGE_BASE.md` PART 4 for the latest banned words and tone sanitation rules

2. **Identify the input**
   - The user will paste chapter text or point to a file
   - Determine which chapter the text belongs to (Chapter 1, 2, 3, or 4)
   - If not specified, ask: "Which chapter and section is this text from?"

3. **Run the full scan**
   Scan the text against ALL 7 categories from `ACADEMIC_WRITING_CHECKER.md`:
   - **Category 1 — AI Phrasing:** Flag AI-overused words, AI cliché phrases, and AI structural patterns
   - **Category 2 — Subjective & Vague Claims:** Flag opinion phrases, vague quantifiers, and absolute claims
   - **Category 3 — Person-View Violations:** Flag first-person, second-person, and informal contractions
   - **Category 4 — Overly Technical Wording:** Flag undefined jargon, misplaced technical depth, and buzzword stacking
   - **Category 5 — Chapter Relevance:** Check if content belongs in the stated chapter
   - **Category 6 — Title Relevance:** Check if content ties back to the project title
   - **Category 7 — DCT Banned Words:** Flag words from the banned list with safe replacements

4. **Output the results**
   Format the output as specified in the "OUTPUT FORMAT" section of `ACADEMIC_WRITING_CHECKER.md`:
   - A numbered findings table with: phrase, category tag, issue, and suggested fix
   - A summary count per category
   - A **full cleaned version** of the text with ALL fixes applied

5. **Ask for user decision**
   After presenting results, ask:
   - "Would you like me to apply all fixes to the text?"
   - "Would you like to review specific changes before applying?"
   - "Are there any flagged items you want to keep as-is?"

## Notes
- This workflow is designed for **Chapters 1–4** (pre-defense manuscript)
- The checker is complementary to the content generation rules in `INSTRUCTIONS.md` — use INSTRUCTIONS for **generating** text, use this workflow for **auditing** existing text
- If the text has more than 20 issues, prioritize fixes by severity: Banned Words > Person-View > AI Phrasing > Vague Claims > Chapter Relevance > Title Drift > Technical Depth
