---
description: Apply Turnitin anti-detection countermeasures and humanizer patterns to chapter writing, reducing AI detection score while maintaining academic compliance
---

# /humanize-writing Workflow

## PURPOSE
Apply the anti-detection strategies from `COUNTERMEASURES.md` and the Humanizer skill to a chapter file to reduce Turnitin's AI detection score. Produces a HUMANIZED version of the text that still passes `/check-writing` academic compliance.

## PROJECT CONTEXT (auto-injected into every run)

- **Project Title:** "Chronicles of Arithmos: A 2D RPG-Based Mathematics Learning Application for Grades 4–6"
- **Chapters Location:** `[04] OUR_PROJECT/`
- **Output Location:** `[11] AI DETECTOR/[11-4] HUMANIZED OUTPUT/CHAPTER {X}/`
- **Countermeasures Reference:** `[11] AI DETECTOR/[11-3] DISCUSSION/COUNTERMEASURES.md`
- **Humanizer Skill:** `[12] HUMANIZER/humanizer-main/SKILL.md`
- **Academic Writing Checker:** `[00] CONFIG_AND_PROMPTS/ACADEMIC_WRITING_CHECKER.md`
- **Flagged Report:** `[11] AI DETECTOR/[11-1] OFFICIAL TURNITIN REPORT/FLAGGED.md`
- **Writing Personality:** `[00] CONFIG_AND_PROMPTS/PERSONALITY.md`
- **Proponents Term:** "The proponents" (never "the team," "we," "I")
- **System Name:** "Chronicles of Arithmos" or "the proposed system"

## HARD CONSTRAINTS (never violate)

These rules from `ACADEMIC_WRITING_CHECKER.md` take priority over ALL countermeasure and humanizer suggestions:

1. Always use "the proponents" — never "the team," "we," "I," "our," "us"
2. No contractions — always expand ("does not" not "doesn't")
3. No sentence fragments — every paragraph needs 2–5 complete sentences
4. Third-person academic voice throughout — no informal register
5. No excessive em-dashes — use commas or restructure
6. Ch.3 MUST follow 4-part formula (WHAT → WHERE → WHY → OUTCOME)
7. Ch.2 theories MUST follow (DEFINE → RELEVANCE → CONNECT → SUPPORTING EXAMPLE)
8. No banned words from Cat 1A or Cat 7

## STEPS

### Step 1: Identify the Target File
// turbo-all

Determine which chapter file to humanize:
- If the user specifies a file → use that file.
- If the user says "humanize chapter X" → look for `[COA]-CHAPTER-X.md` inside `[04] OUR_PROJECT/`.
- If the user specifies a section (e.g., "humanize scope sections") → extract only that section.
- If neither → use the user's **currently active document**.

Read the full content of the target file.

### Step 2: Load References

Read these files in parallel:
1. `[11] AI DETECTOR/[11-3] DISCUSSION/COUNTERMEASURES.md` — for anti-detection strategies
2. `[12] HUMANIZER/humanizer-main/SKILL.md` — for AI pattern identification
3. `[00] CONFIG_AND_PROMPTS/ACADEMIC_WRITING_CHECKER.md` — for academic compliance rules
4. `[11] AI DETECTOR/[11-1] OFFICIAL TURNITIN REPORT/FLAGGED.md` — to check if this section was previously flagged
5. `[00] CONFIG_AND_PROMPTS/PERSONALITY.md` — for the proponent's natural writing voice

### Step 3: Identify the Chapter and Applicable Rules

From the filename or content, determine:
- **Chapter number** (1, 2, 3, 4, or 5)
- **Which sections were flagged** by Turnitin (cross-reference with `FLAGGED.md`)
- **Which countermeasure patterns apply** (from Strategy 9's Pattern 1–10)
- **Which paragraph structure formula applies** (from academic checker Category 5)

### Step 4: Pass 1 — Apply Anti-Detection Countermeasures

Rewrite the text applying these countermeasures in order of impact:

**4a. The "will" reduction (Pattern 1)**
- Count "will" in each paragraph
- If more than 3 per paragraph, rewrite using:
  - Present tense ("the system generates")
  - Passive voice ("equations are generated")
  - Nominalization ("the generation of equations")

**4b. Eliminate template repetition (Patterns 2, 4, 9)**
- Remove all "The user will interact/engage with this module by..." suffixes
- Replace "will serve as" with "is" or "functions as"
- Ensure no 3+ consecutive sentences start with the same word

**4c. Global word replacements (Pattern 3)**
- Replace ALL instances of "utilize/utilizes/utilized" → "use/uses/used"
- Remove all Cat 1A banned words (leverage, comprehensive, facilitate, etc.)
- Remove all Cat 7 banned words (efficient, effective, innovative, etc.)

**4d. Convert catalogs to tables (Pattern 5)**
- If the section contains 3+ consecutive "[Name] will [verb]" sentences → convert to a table
- Character lists, NPC rosters, enemy drop lists, skill lists → tables
- Add a single introductory prose sentence before each table

**4e. Vary justification structures (Pattern 6)**
- If 2+ sentences use "because" in the same paragraph → vary with "since," "as," "given that," or restructure

**4f. Vary theory bridges (Pattern 7, Ch.2 only)**
- If two consecutive theory sections use "but it does not explain" → rewrite one

**4g. Vary sentence structure**
- Apply the 8-15-25 Rule (sentence lengths of 8-12, ~15, and 20-25 words per paragraph)
- Front-load a clause in at least one sentence per section
- Vary paragraph length between 2 and 5 sentences

### Step 5: Pass 2 — Apply Humanizer Patterns

Scan the rewritten text for remaining AI patterns using the Humanizer skill. Focus on the patterns that are safe for academic writing:

| Check | Action |
| :--- | :--- |
| "serves as" / "stands as" copula avoidance | Replace with "is" |
| -ing tail clauses ("ensuring," "highlighting") | Drop the clause or convert to a new sentence |
| Rule of Three (First X, Second Y, Third Z) | Break into 2 or 4 items |
| Synonym cycling (interact/engage/utilize/employ for same concept) | Pick one verb, use consistently |
| Filler phrases ("In order to," "has the ability to") | Shorten: "To," "can" |
| Vague attributions ("Studies show") | Name the specific study and year |
| "Despite challenges" formula | State the challenge directly |
| Generic positive conclusions | Tie to specific measurable claims |

### Step 6: Pass 3 — Academic Compliance Check

After humanizing, verify the text still passes academic rules:

- [ ] No first person or "the team" anywhere
- [ ] No contractions anywhere
- [ ] No sentence fragments — every paragraph has 2–5 complete sentences
- [ ] No banned words (Cat 1A + Cat 7)
- [ ] Ch.3 paragraphs still follow 4-part formula (WHAT/WHERE/WHY/OUTCOME)
- [ ] Ch.2 paragraphs still follow 4-part formula (DEFINE/RELEVANCE/CONNECT/EXAMPLE)
- [ ] All citations still present and correctly formatted
- [ ] "will" appears no more than 3 times per paragraph

If any violations are found, fix them before proceeding.

### Step 7: Pass 4 — Final Anti-AI Audit

Ask yourself: "What makes this text still sound AI-generated?"

Check specifically:
- Any remaining "will" chains (more than 3 per paragraph)
- Any remaining identical sentence openers (3+ consecutive)
- Any remaining template-driven paragraphs
- Any uniform-length paragraphs (all 3 sentences)

Fix any remaining issues.

### Step 8: Compile Output

Produce TWO output files:

**File 1: Humanized Chapter — `HUMANIZED-CHAPTER-{X}.md`**
- The full rewritten text ready to paste into the manuscript
- Changes marked with `← HUMANIZED` comments for traceability

**File 2: Change Log — `HUMANIZE-LOG-CHAPTER-{X}.md`**
- Summary of changes made
- Count of patterns fixed per category:
  - "will" reductions (before → after count)
  - Template eliminations
  - Word replacements (utilize → use, etc.)
  - Table conversions
  - Structure variations applied
- Before/after comparison of the most heavily modified paragraphs (max 5)

### Step 9: Save the Output

Save results to `[11] AI DETECTOR/[11-4] HUMANIZED OUTPUT/CHAPTER {X}/`:
- `HUMANIZED-CHAPTER-{X}.md`
- `HUMANIZE-LOG-CHAPTER-{X}.md`

Where `{X}` is the chapter number (e.g., `CHAPTER 1/HUMANIZED-CHAPTER-1.md`).

If the user specified a section instead of a full chapter, name accordingly:
- `HUMANIZED-CHAPTER-{X}-SCOPE.md`
- `HUMANIZE-LOG-CHAPTER-{X}-SCOPE.md`

If file already exists, **overwrite** (previous humanization is outdated).

### Step 10: Report to User

After saving, report:
- Total patterns fixed (grouped by type)
- Estimated "will" count before → after
- Estimated Turnitin score impact (using the reduction table from COUNTERMEASURES.md)
- Top 3 most significant changes made
- Confirm the output file locations
- Recommend running `/check-writing` on the humanized output as a final validation

---

## USAGE EXAMPLES

The user can invoke this workflow in several ways:

```
/humanize-writing                                → humanizes the currently active document
/humanize-writing chapter 1                      → finds and humanizes [COA]-CHAPTER-1.md
/humanize-writing [COA]-CHAPTER-3.md             → humanizes Chapter 3
/humanize-writing chapter 1 scope                → humanizes only the Scope section of Ch.1
```

## NOTES

- The humanized output should be a COMPLETE rewrite, not a diff. The user should be able to copy-paste it directly into the manuscript.
- NEVER sacrifice academic compliance for anti-detection. If a countermeasure conflicts with `ACADEMIC_WRITING_CHECKER.md`, the checker wins.
- The `COUNTERMEASURES.md` file is the source of truth for anti-detection patterns. The Humanizer skill is supplementary.
- When converting prose to tables, ensure the table still meets the chapter's structural requirements (e.g., Ch.3 needs the 4-part formula per tool).
- Prioritize fixing sections that appear in `FLAGGED.md` — these are confirmed Turnitin triggers.
- After humanizing, always recommend the user run `/check-writing` on the output to catch any compliance issues introduced during humanization.
