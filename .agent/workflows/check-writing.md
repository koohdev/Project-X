---
description: Check academic writing for AI phrasing, vague claims, person-view violations, jargon, and chapter relevance issues
---

# /check-writing Workflow

## PURPOSE
Audit a chapter file against `ACADEMIC_WRITING_CHECKER.md` (all 10 categories) and produce a structured findings report with a cleaned version.

## PROJECT CONTEXT (auto-injected into every check)

- **Project Title:** "Chronicles of Arithmos: A 2D RPG-Based Mathematics Learning Application for Grades 4–6"
- **Chapters Location:** `[04] OUR_PROJECT/`
- **Output Location:** `[06] CHECKING/`
- **Checker Reference:** `ACADEMIC_WRITING_CHECKER.md` (root of workspace)
- **Knowledge Base:** `KNOWLEDGE_BASE.md` (root of workspace)
- **Proponents Term:** "The proponents" (never "the team," "we," "I")
- **System Name:** "Chronicles of Arithmos" or "the proposed system"

## STEPS

### Step 1: Identify the Target File
// turbo-all

Determine which chapter file to check:
- If the user specifies a file → use that file.
- If the user says "check chapter X" → look for `[COA]-CHAPTER-X.md` inside `[04] OUR_PROJECT/`.
- If neither → use the user's **currently active document**.

Read the full content of the target file.

### Step 2: Load the Checker Reference

Read `ACADEMIC_WRITING_CHECKER.md` from the workspace root. Focus on:
1. The **QUICK SCAN REFERENCE** section first (for fast pattern matching)
2. The detailed category tables only when you need replacement suggestions or context

Also glance at `KNOWLEDGE_BASE.md` PART 4 if you need to cross-check banned words or DCT formatting rules.

### Step 3: Determine Chapter Number and Context

From the filename or content, determine:
- **Chapter number** (1, 2, 3, 4, or 5)
- **Chapter title** (e.g., "Introduction," "Review of Related Literature/Systems")

This determines:
- Which paragraph structure formula applies (from Category 5)
- Which chapter relevance table to use (from Category 5)
- How deep technical terms should go (from Category 4B)

### Step 4: Scan — Execute All 10 Categories

Scan the chapter text line-by-line against all 10 categories. Use the QUICK SCAN REFERENCE for fast word/phrase matching, then consult the detailed tables for replacement suggestions.

**Scanning order (most impactful first):**

1. **Category 7 — Banned Words** — Scan for all banned words and their conjugations. This is the fastest check.
2. **Category 1 — AI Phrasing** — Scan for flagged words, phrases, and structural patterns.
3. **Category 3 — Person-View** — Scan for first person, second person, contractions, and ambiguous pronouns.
4. **Category 2 — Vague Claims** — Scan for uncited claims, vague quantifiers, and absolute statements.
5. **Category 8 — Grammar & Mechanics** — Check punctuation, sentence structure, articles, and pronoun agreement.
6. **Category 4 — Technical Wording** — Flag undefined jargon and buzzword stacking.
7. **Category 5 — Chapter Relevance** — Check if content belongs in this chapter AND if paragraph structure formulas are followed.
8. **Category 6 — Title Relevance** — For each paragraph, test: does it connect back to the project title?
9. **Category 9 — DCT Formatting** — Check citation format, section numbering, table/figure numbering, bullet points.
10. **Category 10 — Paragraph Standards** — Flag single-sentence paragraphs, thin subsections, overly long paragraphs.

For each finding, record:
- Finding number (sequential across all categories)
- Line number or section reference
- The flagged phrase (quoted)
- Category tag
- Severity (🔴 CRIT / 🟠 HIGH / 🟡 MED / 🟢 LOW)
- Issue description
- Suggested fix

### Step 5: Compile the Output

Format the output exactly as specified in the checker's OUTPUT FORMAT section:

1. **Header** — File checked, date, checker reference
2. **Per-category findings tables** — One table per category (skip categories with 0 findings, noting "No violations found ✅")
3. **Summary counts** — Total per category + total by severity
4. **Priority Fixes (Top 10)** — The 10 most urgent findings ranked by severity and impact
5. **Cleaned Version** — The full chapter text rewritten with ALL fixes applied. Mark changes with `←` comments for traceability.

### Step 6: Save the Output

Save the results to:
```
[06] CHECKING/CHECK-CHAPTER-{X}.md
```

Where `{X}` is the chapter number (e.g., `CHECK-CHAPTER-2.md`).

If the file already exists, **overwrite it** with the new results (the old check is outdated once changes are made).

### Step 7: Report to User

After saving, report:
- Total issues found (with severity breakdown)
- The top 3 priority fixes as a quick summary
- Confirm the output file location

---

## USAGE EXAMPLES

The user can invoke this workflow in several ways:

```
/check-writing                              → checks the currently active document
/check-writing [COA]-CHAPTER-2.md           → checks Chapter 2
/check-writing chapter 3                    → finds and checks [COA]-CHAPTER-3.md
```

## NOTES

- The cleaned version should be a COMPLETE rewrite, not a diff. The user should be able to copy-paste it directly.
- If a paragraph structure formula exists for the chapter (Category 5), the cleaned version MUST follow it.
- All banned word conjugations must be caught (e.g., "ensuring" when "ensure" is banned).
- When in doubt about severity, default to 🟡 MED.
- The checker reference file is the source of truth for all rules — do not invent rules not in the checker.
