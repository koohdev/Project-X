---
description: Run a complete writing audit on a chapter and save all three output files (DIFF, FINDINGS, CLEANED) in a single pass
---

# /audit-chapter Workflow

## PURPOSE

A single-invocation audit pipeline that wraps around `/check-writing` and produces **all three output files** automatically:

1. `CHECK-CHAPTER-{X}-FINDINGS.md` → `[06-2] CHECKING FINDINGS/`
2. `CHECK-CHAPTER-{X}-DIFF.md` → `[06-1] CHECKING DIFF/`
3. `CHECK-CHAPTER-{X}-CLEANED.md` → `[06-3] CHECKING CLEANED/`

> [!IMPORTANT]
> This workflow builds directly on top of `/check-writing`. It does NOT re-implement the scanning logic — it simply adds automatic file routing and a DIFF generation step that `/check-writing` may skip in a one-shot context.

---

## PROJECT CONTEXT

- **Chapters Location:** `[04] OUR_PROJECT/`
- **Output Root:** `[06] CHECKING REPORTS/`
- **Checker Reference:** `[00] CONFIG_AND_PROMPTS/ACADEMIC_WRITING_CHECKER.md`
- **Knowledge Base:** `[00] CONFIG_AND_PROMPTS/KNOWLEDGE_BASE.md`

---

## STEPS

// turbo-all

### Step 1: Identify the Target File

Determine which chapter file to audit:
- If the user specifies a file → use that file.
- If the user says "audit chapter X" → look for `[COA]-CHAPTER-X.md` inside `[04] OUR_PROJECT/`.
- If the user says "audit chapter 1" → look inside `[04] OUR_PROJECT/[04-1 CHAPTER 1]/` for `[COA]-CHAPTER-1-FULL.md`.
- If neither → use the user's **currently active document**.

Read the full content of the target file. Store this as `ORIGINAL_TEXT`.

Determine the chapter number `{X}` from the filename or heading.

### Step 2: Run the Full /check-writing Scan

Execute all steps from the `/check-writing` workflow:

1. Load `[00] CONFIG_AND_PROMPTS/ACADEMIC_WRITING_CHECKER.md`
2. Load `[00] CONFIG_AND_PROMPTS/KNOWLEDGE_BASE.md` PART 4
3. Determine chapter number and applicable formatting rules
4. Scan all 10 categories (in priority order)
5. Compile the findings table (all categories, all severities)
6. Produce a cleaned version with all fixes applied and `←` comments

Do NOT save any files yet. Hold the results in memory as:
- `FINDINGS_CONTENT` — the per-category findings tables + summary + top 10 priority list
- `CLEANED_CONTENT` — the fully rewritten chapter text

### Step 3: Generate the DIFF File

Compare `ORIGINAL_TEXT` (Step 1) against `CLEANED_CONTENT` (Step 2) and produce a structured diff:

Format the diff as a markdown table with one row per change:

```
| # | Location | Original Text | Cleaned Text | Category | Severity |
|---|----------|--------------|-------------|----------|----------|
| 1 | Line 4   | "utilize"     | "use"        | Cat 1 — AI Phrasing | 🟡 MED |
```

Group changes by category. Include section headers to match the FINDINGS structure.

Store this as `DIFF_CONTENT`.

### Step 4: Write the FINDINGS File

Save to: `[06] CHECKING REPORTS/[06-2] CHECKING FINDINGS/CHECK-CHAPTER-{X}-FINDINGS.md`

File should contain:
1. Header block (file checked, date, checker reference)
2. Per-category findings tables from `FINDINGS_CONTENT`
3. Summary counts (per category + by severity)
4. Priority Fixes — Top 10 ranked by severity

If the file already exists → **overwrite it**.

### Step 5: Write the DIFF File

Save to: `[06] CHECKING REPORTS/[06-1] CHECKING DIFF/CHECK-CHAPTER-{X}-DIFF.md`

File should contain:
1. Header block (source file, cleaned file, date)
2. The change table from `DIFF_CONTENT`
3. A count of total changes made

If the file already exists → **overwrite it**.

### Step 6: Write the CLEANED File

Save to: `[06] CHECKING REPORTS/[06-3] CHECKING CLEANED/CHECK-CHAPTER-{X}-CLEANED.md`

File should contain:
1. A brief header noting this is a cleaned version and which original file it came from
2. The full cleaned chapter text from `CLEANED_CONTENT`
3. Inline `← [fix description]` comments next to each changed line

If the file already exists → **overwrite it**.

### Step 7: Update the WIP Progress Tracker

After saving all three files, open the corresponding progress tracker:
- `[04] OUR_PROJECT/WIP/CHAPTER-{X}-PROGRESS.md`

Update the **Output Files** section to check off the files that were just saved:
```
- [x] CHECK-CHAPTER-{X}-FINDINGS.md → [06-2] CHECKING FINDINGS/
- [x] CHECK-CHAPTER-{X}-DIFF.md → [06-1] CHECKING DIFF/
- [x] CHECK-CHAPTER-{X}-CLEANED.md → [06-3] CHECKING CLEANED/
```

### Step 8: Report to User

Print a final summary:
- Chapter audited and date
- Total findings: `{N}` issues (`{CRIT}` CRIT / `{HIGH}` HIGH / `{MED}` MED / `{LOW}` LOW)
- Top 3 priority fixes (one-liner each)
- Confirmation of the 3 output files saved (with paths)
- Reminder to apply fixes back to the main draft in `[04] OUR_PROJECT/`

---

## USAGE EXAMPLES

```
/audit-chapter                         → audits the currently active document
/audit-chapter chapter 2               → audits [COA]-CHAPTER-2.md
/audit-chapter [COA]-CHAPTER-3.md      → audits Chapter 3 by filename
```

## NOTES

- `/audit-chapter` is the recommended full-pipeline command. Use `/check-writing` only when you want findings reported in-chat without saving to files.
- The CLEANED file is NOT the final draft. The proponents must review and apply changes back to the source file in `[04] OUR_PROJECT/`.
- Always overwrite existing output files — old check results are invalidated once the source file changes.
