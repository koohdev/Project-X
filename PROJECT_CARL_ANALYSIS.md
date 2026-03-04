# 🔍 PROJECT CARL: Workflow & Setup Analysis

> An objective review, analysis, and set of recommendations for the PROJECT CARL Capstone repository.
>
> *Originally drafted by Gemini 3.1 Pro — Verified & patched by Antigravity (2026-03-04)*

---

## 🌟 1. Executive Summary: What You're Doing Right

This repository is **well-structured for an academic/LLM-assisted project**. You are already operating at a high level.

**Standout Strengths:**

* **Modular Prompt Design:** Separating `INSTRUCTIONS.md`, `KNOWLEDGE_BASE.md`, and `ACADEMIC_WRITING_CHECKER.md` into dedicated files is an effective modular prompting strategy. Each file serves a distinct purpose — AI behavior rules, capstone knowledge source, and writing audit reference — which prevents context confusion and enforces strict boundaries.
* **Numbered Directories:** Using `[01]` to `[08]` keeps the workspace sorted by pipeline phase, making navigation intuitive.
* **Automated Agent Workflows:** The `.agent/workflows/check-writing.md` workflow automates repetitive auditing tasks across 10 checking categories, saving significant manual effort.
* **Audit Trail Infrastructure:** The `[06] CHECKING REPORTS/` folder contains dedicated checking outputs (cleaned versions, diffs, findings) providing traceability of writing revisions.

> [!NOTE]
> The subdirectories `[06-1 CHECKING DIFF`, `[06-2] CHECKING FINDINGS`, and `[06-3] CHECKING CLEANED` exist inside `[06]` but are currently **empty** — all checking files are saved directly to the `[06]` root by the `/check-writing` workflow. Consider either populating these subdirectories or removing them to avoid confusion (see Section 2D).

While your current setup is robust, there is always room for optimization. Below are suggestions ranging from quick **Quality of Life (QoL) tweaks** to **Advanced Productivity Boosters**.

---

## 📂 2. Structural & Organizational Tweaks

### A. Establish a `[00] CONFIG_AND_PROMPTS` Directory

Currently, files like `README.md`, `INSTRUCTIONS.md`, `KNOWLEDGE_BASE.md`, and `ACADEMIC_WRITING_CHECKER.md` live in the root directory.

* **Suggestion:** Move the AI instruction and ruleset files into a dedicated `[00] CONFIG` or `[00] PROMPTS` folder. Keep only the `README.md` at the root. This keeps the highest level of your project completely clean.

### B. Separate "Drafts" from "Final" Explicitly

Your `[04] OUR_PROJECT` and `[05] REVISED_CHAPTERS_OR_SECTIONS` folders are good, but can get messy as chapters grow.

* **Suggestion:** Inside `[04]`, enforce a strict `WIP` (Work In Progress) vs `READY_FOR_REVIEW` sub-folder structure. This makes it instantly obvious to your human team members which files are safe to read/compile and which are still being drafted.

### C. Create an Archival Workflow

As you iterate on chapter drafts, folders can get cluttered with superseded versions.

* **Suggestion:** Create a `[99] ARCHIVE` folder. Once a chapter is finalized and moved to `[05]`, move all the old drafts, diffs, and findings for that chapter into the archive. Out of sight, out of mind, but kept for version history.

### D. Fix Folder Naming Inconsistencies

Several subdirectories have **inconsistent bracket formatting**:

| Current Name | Issue | Suggested Fix |
|---|---|---|
| `[04-3 APPENDICES` | Missing closing `]` | `[04-3] APPENDICES` |
| `[06-1 CHECKING DIFF` | Missing closing `]` | `[06-1] CHECKING DIFF` |

Compare with their properly named siblings: `[06-2] CHECKING FINDINGS`, `[06-3] CHECKING CLEANED`. Consistent naming matters for scripting, searching, and general tidiness.

### E. Decide the Fate of Empty `[06]` Subdirectories

The three subdirectories inside `[06] CHECKING REPORTS/` are all empty:

* `[06-1 CHECKING DIFF` — empty
* `[06-2] CHECKING FINDINGS` — empty
* `[06-3] CHECKING CLEANED` — empty

Meanwhile, all actual check output files (`CHECK-CHAPTER-1-CLEANED.md`, `CHECK-CHAPTER-1-DIFF.md`, `CHECK-CHAPTER-1-FINDINGS.md`, etc.) sit directly in the `[06]` root. The `/check-writing` workflow is configured to save to `[06] CHECKING/CHECK-CHAPTER-{X}.md`.

* **Option A:** Update the `/check-writing` workflow to save files into the appropriate subdirectories (DIFF → `[06-1]`, FINDINGS → `[06-2]`, CLEANED → `[06-3]`).
* **Option B:** Remove the empty subdirectories and keep the flat structure — simpler, fewer folders to manage.

### F. Standardize File Extensions in `[05]`

The `[05] REVISED_CHAPTERS_OR_SECTIONS/` folder currently contains `.txt` files while the rest of the project uses `.md`:

* `4.2.2.2_Relevance_of_the_Technology_REVISED.txt`
* `4.2.4.2_Cost_Recovery_Scheme_REVISED.txt`
* `4.2.6_Risk_Assessment_Analysis_REVISED.txt`
* `CHAPTER4_METHODOLOGY_AND_SCHEDULE_REVISED.txt`

* **Suggestion:** Rename these to `.md` for consistency. Markdown renders better in VS Code, GitHub, and any future Pandoc pipeline.

---

## ⚡ 3. Quality of Life (QoL) Improvements

### A. Add Markdown Checklists to Chapter Templates

Right now, you prompt the AI to generate sections based on the knowledge base.

* **Suggestion:** At the top of your draft files in `[04]`, maintain a markdown checklist of the required sections for that chapter. As you or the AI finishes a section, check it off.

```markdown
# Chapter 1 Progress
- [x] 1.1 Project Context
- [ ] 1.2.1 General Objective
- [ ] 1.2.2 Specific Objectives
```

### B. Standardize Naming Conventions

There are mixed naming conventions across the project:

| Location | Current Pattern | Example |
|---|---|---|
| `[04]` Drafts | `[COA]-CHAPTER-X.md` | `[COA]-CHAPTER-2.md` |
| `[06]` Checks (pattern 1) | `CHECK-CHAPTER-X-*.md` | `CHECK-CHAPTER-1-CLEANED.md` |
| `[06]` Checks (pattern 2) | `CHAPTER-X-CHECK-*.md` | `CHAPTER-4-CHECK-RESULTS.md` |

* **Suggestion:** Adopt a strict naming convention to make searching and scripting easier. The `[COA]-CHAPTER-X` prefix is already strong for drafts. For checking files, standardize to one pattern — e.g., always `CHECK-CHAPTER-{X}-{TYPE}.md`.

---

## 🚀 4. Productivity Boosters (VS Code / IDE Integration)

Assuming you are using VS Code (or Cursor/Windsurf), you can install extensions that do half the checking work *before* you even ask an AI.

### A. Automated Markdown Linting

* **Tool:** `markdownlint` (VS Code Extension)
* **Why:** It will automatically highlight basic formatting errors (trailing spaces, inconsistent heading levels, list formatting) in real-time, saving your AI calls for actual content checking.

### B. Vale.sh for Academic Prose

* **Tool:** [Vale.sh](https://vale.sh/) (with the VS Code extension)
* **Why:** Vale is a specialized linter for prose. You can write a custom Vale rule that flags your "banned words" (efficient, innovative, improve, etc.). If a human types "innovative", the editor will place a red squiggly line under it immediately, exactly like a spellchecker.

### C. Draw.io / Mermaid Previewer

* **Tool:** `Draw.io Integration` (VS Code Extension) — for your existing `.drawio` diagrams
* **Why:** Your diagrams in `[08] DIAGRAMS/` use the `.drawio` format. This extension lets you view and edit `FDD_FUNCTIONAL_DECOMPOSITION.drawio` and `FISHBONE_DIAGRAM.drawio` directly inside VS Code without opening a separate application.

* **Optional Tool:** `Mermaid Preview` (VS Code Extension) — for any future Mermaid diagrams
* **Why:** Your `INSTRUCTIONS.md` mentions Mermaid.js as a diagram generation strategy. If you generate Mermaid code blocks in the future, this extension renders them live in a split pane.

---

## ⚙️ 5. Advanced / Power-User Setup

### A. The "Compile to Manuscript" Script

Currently, your chapters are spread across multiple markdown files.

* **Advanced Move:** Install [Pandoc](https://pandoc.org/). Write a simple script (e.g., `build.bat` or `build.sh`) that automatically merges your `[05] REVISED_CHAPTERS_OR_SECTIONS` into a single, beautifully formatted `.docx` or `.pdf` file with a Table of Contents.
* **Example command:**
  `pandoc [05]/*/*.md -o Final_Manuscript.docx --reference-doc=template.docx`
  *(You can set up a `template.docx` that strictly follows the DCT CCS font/margin formatting rules, ensuring your outputs are instantly ready for printing).*

> [!NOTE]
> You would first need to rename the `.txt` files in `[05]` to `.md` (see Section 2F) for this command to pick them up.

### B. Automated Diff Generation (Git History)

You currently generate "Diff" and "Findings" files manually.

* **Advanced Move:** Your repository already has a `.git` folder with commit history. You can use native `git diff` to see exact word-by-word changes between commits without creating separate DIFF files.
* You can even create a simple script that logs `git log -p > VERSION_HISTORY.md` to automatically compile a history of all changes made to a chapter over time.

### C. Custom Agent Workflows (Expanding `.agent/workflows/`)

You already have `/check-writing`. Consider adding:

1. `/compile-chapter`: An agent workflow that reads all notes for a specific chapter, runs it through the knowledge base, outputs the draft, and immediately runs the `/check-writing` sequence on its own output in one seamless loop.
2. `/verify-requirements`: A specialized workflow that strictly cross-references a finished chapter against the "Minimum Requirements Quick Reference" matrix in your instructions.

> [!IMPORTANT]
> Your existing `/check-writing` workflow already generates findings and a cleaned version in a single pass. Any new `/audit-chapter` or `/compile-chapter` workflow should **build on top of** `/check-writing` rather than duplicate its functionality.

---

## 🔥 6. Eradicating Manual & Tedious Tasks (The "Better Way")

Here are areas where manual effort can be reduced or eliminated:

### A. Streamline the Audit Pipeline

* **Current Process:** The `/check-writing` workflow generates findings and a cleaned version, but DIFF and FINDINGS are generated as separate steps or conversations.
* **The Better Way:** Extend the existing `/check-writing` workflow (or create a complementary `/audit-chapter` wrapper) to produce all three outputs (`_CLEANED.md`, `_DIFF.md`, `_FINDINGS.md`) in a single invocation. This would eliminate the multi-step manual prompting.

### B. Stop Copying/Uploading Instructions to Google AI Studio

* *Result:* Every time you ask the AI to "Write chapter 1," it already knows the DCT CCS rules by default via the workspace files. No uploading necessary. You can generate entire chapters instantly inside your editor.

### C. Stop Manually Typing `[WU__2024]` Citations

* **Current Struggle:** Counting citations and ensuring every inline `[AUTHOR_YEAR]` citation matches the Bibliography at the bottom is agonizing and error-prone.
* **The Better Way:** Use **Zotero** with a Markdown extension, or use standard BibTeX with Pandoc (`pandoc-citeproc`).
  * You simply type `[@wu2024]` in your markdown.
  * When you compile the document (using the Pandoc script mentioned in Section 5A), it automatically places the perfectly formatted inline citation *and* builds the References section at the end of the document without you lifting a finger.

### D. Automate Banned-Word Checking at Commit Time

* **Current Struggle:** You write a chapter, then manually trigger your `/check-writing` workflow to ensure there are no banned words (like "efficient" or "innovative").
* **The Better Way:** Set up a **Git Pre-Commit Hook** using a simple shell/batch script.
  * Create a `.git/hooks/pre-commit` script that runs the Vale linter (from Section 4B) on any staged `.md` files.
  * If it detects the word "innovative" or an AI-sounding phrase, it will *block the commit* and print out exactly which line needs fixing. This guarantees zero academic formatting errors slip through.

> [!TIP]
> Since this is a pure documentation repository (no `package.json`), you don't need npm-based tools like Husky. A simple shell script in `.git/hooks/pre-commit` achieves the same result with zero dependencies.

---

## 📋 7. Immediate Action Items

Based on this analysis, here are quick wins you can do **right now** with minimal effort:

| Priority | Action | Effort |
|---|---|---|
| 🔴 High | Fix broken folder brackets (`[04-3 APPENDICES` → `[04-3] APPENDICES`, `[06-1 CHECKING DIFF` → `[06-1] CHECKING DIFF`) | 2 min |
| 🔴 High | Rename `.txt` files in `[05]` to `.md` | 2 min |
| 🟡 Medium | Decide whether to use or remove empty `[06]` subdirectories | 5 min |
| 🟡 Medium | Standardize check file naming (`CHAPTER-4-CHECK-RESULTS.md` → `CHECK-CHAPTER-4-RESULTS.md`) | 5 min |
| 🟢 Low | Install `markdownlint` VS Code extension | 1 min |
| 🟢 Low | Install `Draw.io Integration` VS Code extension | 1 min |

---

### Final Thoughts

Your methodology is highly professional and emulates enterprise-grade documentation workflows. By integrating a prose linter (like Vale), a document compiler (like Pandoc), fixing the minor naming inconsistencies, and slightly refining your directory structure, you will eliminate the remaining manual friction in your Capstone journey.
