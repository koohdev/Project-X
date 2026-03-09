# 🤖 PROJECT CARL's Workflow & Agent Guide

Welcome to the **Workflow and Agent Guide**. This document explains how your project directory is structured, how the agent system operates, and how to utilize custom workflows to automate reviewing and finalizing your Capstone documentation.

---

## 🎯 1. What Can You Use PROJECT CARL For?

PROJECT CARL is your dedicated Capstone documentation assistant. You can use this AI agent for three main phases of your project:

### 📝 A. Documentation & Making (Drafting)
- **Generate Sections from Scratch:** Give the agent rough bullet points or raw ideas, and ask it to write complete, academically-formatted sections (e.g., *"Write Section 1.1 Project Context for our Library System"*).
- **Create Diagrams & Tables:** Ask the agent to generate markdown tables (like Cost & Benefit Analysis, Gantt charts) or Mermaid.js diagrams (like Use Case Diagrams, Flowcharts) based on your system variables.
- **Format Templates:** Request standard DCT CCS templates for Title Pages, Adviser's Sheets, or Panel Approval Sheets.

### 🔄 B. Revising & Editing
- **De-AI Your Writing:** Use the agent to scan drafts and remove robotic "AI phrasing," banned words (like "efficient" or "innovative"), and first-person pronouns ("we", "I", "our team").
- **Fix Academic Tone:** Ask the agent to rewrite paragraphs that contain vague claims, lack citations, or are too "sales-pitchy" to sound more objective and academic.
- **Verify Compliance:** Automatically cross-check your finished chapters against the official manual to see if you missed any mandatory sections or diagrams.

### ❓ C. Asking & Consulting
- **Clarify Guidelines:** Ask questions like *"What are the minimum requirements for an Inventory System?"* or *"How is the final manuscript graded?"*
- **Check Project Validity:** Ask if your project idea (e.g., A Barangay Website) is allowed under the rules. (Spoiler: Barangay websites are banned!)
- **Role & Defense Prep:** Ask about the responsibilities of each team member during the Capstone defense.

---

## 📂 2. How This Directory Works

The `PROJECT CARL` repository is specifically structured to separate rules, drafts, checking reports, and finalized outputs. Here is how the key environments function:

- **`.agent/` (Hidden Folder)**: The central brain of the agent capabilities for this project. It contains the `workflows/` directory, which holds the step-by-step slash-commands the agent uses to perform complex, automated tasks.
- **`[00] CONFIG_AND_PROMPTS/`**: Holds the core AI rules, the `ACADEMIC_WRITING_CHECKER.md`, and the `KNOWLEDGE_BASE.md`. The agent references these heavily to grade and format your work according to DCT CCS standards.
- **`[04] OUR_PROJECT/`**: **Your main workspace.** This is where your actual project documentation lives.
  - `WIP/`: Work in Progress. Drafts go here.
  - `READY_FOR_REVIEW/`: Chapters that have passed initial agent checks and are awaiting final approval.
- **`[06] CHECKING REPORTS/`**: Where the agent saves the results of its writing audits. Whenever you run a full chapter check, the DIFFs (change logs), FINDINGS (error reports), and CLEANED texts are generated here.
- **`[07] ARTIFACTS/` & `[08] DIAGRAMS/`**: Storage for finalized agent outputs and visual assets like flowcharts or Gantt charts.

---

## ⚙️ 3. The Agent Workflow System

Think of "Workflows" as specialized mini-programs or macros built into PROJECT CARL. Instead of giving the AI a long, repetitive instruction every time, you can just call a single **slash-command**, and the agent will execute a complex series of predefined checks.

Currently, you have **three custom workflows** located in `.agent/workflows/`.

### 🛠️ The Available Workflows

#### 1. `/verify-requirements` (The Structural Gatekeeper)
- **What it does:** Scans your chapter to ensure every mandatory section, diagram, and formatting element is present according to the DCT CCS Minimum Requirements Matrix. It does NOT grade your grammar; it purely grades your completeness.
- **When to use it:** When you've *finished drafting* a chapter but want to make sure you didn't miss a requirement (e.g., "Did I include the Fishbone Diagram?", "Did I miss a specific objective?").
- **Output:** It will create a standalone verification report grading your structural completion out of 100%.

#### 2. `/check-writing` (The Grammar & Tone Analyst)
- **What it does:** Scans your writing line-by-line against 10 strict academic categories (such as banned words, AI phrasing, first-person pronouns, and vague claims) using the `ACADEMIC_WRITING_CHECKER.md`. 
- **When to use it:** When you want a fast, in-chat report of your writing quality without the agent necessarily generating and saving all output files.

#### 3. `/audit-chapter` (The Complete Pipeline)
- **What it does:** The ultimate writing command. It runs the full `/check-writing` scan but automates the routing of **three critical files** in a single pass:
  1. **FINDINGS:** A deep-dive report on all errors found (saved to `[06-2] CHECKING FINDINGS/`).
  2. **DIFF:** A clear table showing what the original text was vs. what the AI changed (saved to `[06-1] CHECKING DIFF/`).
  3. **CLEANED:** A completely rewritten, corrected version of your chapter with inline `←` notes explaining edits (saved to `[06-3] CHECKING CLEANED/`).
- **When to use it:** When your draft is complete, fully structurally verified, and you're ready to polish it into a final academic submission.

---

## 🚀 4. How to Execute Workflows (The Ideal Process)

You can trigger a workflow simply by typing the slash command in your chat prompt. You can optionally tell the agent which file to look at.

**Examples:**
- *"Run `/audit-chapter` on Chapter 2."*
- *"`/verify-requirements` on my currently active document."*
- *Please run `/check-writing` on `[COA]-CHAPTER-3.md`.*

### 📋 The Step-by-Step "Draft to Final" Process:

1. **Drafting:** Write your rough content in `[04] OUR_PROJECT/WIP/`. Just get the ideas down without worrying too much about perfection.
2. **Verify Structure:** Run `/verify-requirements`. If the agent reports `❌ MISSING` items, go back and add them. Keep replacing content until you hit 100%.
3. **Audit Writing:** Once structural requirements are verified, run `/audit-chapter`. 
4. **Review & Apply:** Open the generated "CLEANED" file in `[06] CHECKING REPORTS/`. Review the AI's changes using the "DIFF" or "FINDINGS" file. If you agree, apply the cleaned text back to your main draft.
5. **Finalize:** Move the finalized document to `[04] OUR_PROJECT/READY_FOR_REVIEW/`.

> **Tip:** If you ever find yourself doing a repetitive, multi-step task frequently, you can ask me to create a "new workflow" for it, and I will write a new `.md` file inside `.agent/workflows/` so you can use it in the future!
