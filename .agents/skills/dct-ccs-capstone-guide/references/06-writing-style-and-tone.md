# 6. Academic Writing Style, List Formatting, and Tone Sanitation (DCT CCS)

This reference outlines the required linguistic style, paragraph structure, list rules, and tone sanitation dictionary for all BSIT Capstone manuscript content.

---

## 6.1 Global Writing Standards

| Rule | Requirement |
| :--- | :--- |
| **Paragraph Length** | Strictly **2 to 5 sentences** per paragraph |
| **Academic Tone** | Objective, third-person impersonal, evidence-backed (no "we", "I", "our team") |
| **System Descriptions** | **Present Tense** (e.g., *"The system validates user credentials..."*) |
| **Development & Testing Activities** | **Past Tense** (e.g., *"The researchers conducted unit tests on the authentication module..."*) |
| **Paragraph Transitions** | Exactly one transitional phrase per paragraph (e.g., *Furthermore, Additionally, Consequently, In contrast*) |
| **Adjective Density** | $\le 1$ descriptive adjective per noun; strictly zero intensifiers (*very, extremely, highly*) |

---

## 6.2 List Formatting Rules in Body Text

> ⚠️ **CRITICAL DCT RULE**: **NO BULLET SYMBOLS IN BODY TEXT**

| Allowed in Manuscript | Strictly Prohibited in Body Text |
| :--- | :--- |
| **A., B., C.** (Categorical lists within sections) | `•` Bullet point |
| **1., 2., 3.** (Sequential / procedural lists) | `-` Hyphen dash |
| **A.1, A.2** / **1.1, 1.2** (Indented sub-items) | `*` Asterisk |
| Markdown Tables (for multi-attribute data) | `▪` Square bullet |

### Paragraph List Rule
Each categorical or sequential list item in the body text must be written as a **complete, standalone paragraph of 2 to 5 sentences** explaining the concept, rather than a raw one-line bullet.

---

## 6.3 Tone Sanitation & Banned Words Dictionary

Avoid subjective fluff, marketing buzzwords, and unsubstantiated claims. Use precise operational verbs.

| Banned Words / Fluff ❌ | Why It Is Flagged | Approved Academic Replacements ✅ |
| :--- | :--- | :--- |
| *efficient, effective* | Subjective, unproven claim | *supports, facilitates, accelerates, reduces processing time* |
| *innovative, cutting-edge, powerful* | Promotional marketing hype | *features, implements, incorporates, is designed to* |
| *user-friendly, intuitive, easy* | Subjective user experience claim | *accessible, standardized, requires minimal operational steps* |
| *robust, scalable* | Vague engineering buzzword | *modular, extensible, handles concurrent transactions* |
| *seamless, streamlined* | Vague buzzword | *integrated, coordinated, automated* |
| *secure* (unqualified) | Unsubstantiated security claim | *enforces role-based access control, utilizes AES-256 encryption* |
| *fast, quick, rapid* | Vague velocity claim | *executes within [X] milliseconds, processes transactions in real-time* |
| *ensure, guarantee* | Absolute claim | *verifies, validates, checks, enforces* |
| *optimize, enhance, improve* | Ambiguous improvement | *updates, adjusts, reconfigures, computes* |

---

## 6.4 Section-Specific Phrasing Conventions

### 1. Chapter 1.2.2 Specific Objectives
* Every specific objective must start with an infinitive action verb: **"To develop..."**, **"To design..."**, **"To implement..."**, or **"To evaluate..."**.
* Structure each objective with the **What + How + Result** pattern:
  * *Example*: *"To design and implement a role-based access control module using JSON Web Tokens (JWT) to restrict system access according to user privileges."*

### 2. Chapter 1.4 Scope and Limitations
* Structure Scope and Limitations into distinct numbered subsections (`1.4.1 Scope` and `1.4.2 Limitations`).
* Use **A., B., C.** subheadings.
* Each limitation must include a direct operational justification explaining why the constraint exists beyond the team's control.

### 3. Chapter 3.0 Technical Background
* Maintain strict hierarchical numbering: `3.0` $\rightarrow$ `3.1` $\rightarrow$ `3.1.1` $\rightarrow$ `A., B., C.` $\rightarrow$ `A.1, B.1`.
* Adhere strictly to the four-part structure: **Hardware**, **Software**, **Peopleware**, and **Network**.
* End Chapter 3 with a transitional synthesis paragraph leading into Chapter 4.

### 4. Chapter 4.1 Methodology
* Define the chosen SDLC model with proper scholarly citation `[AUTH2024]`.
* Number SDLC phases as `4.1.1`, `4.1.2`, etc.
* In each phase, detail: (1) Phase Goal, (2) Activities performed (past tense), (3) Timeframe, and (4) Tangible Deliverables.

---

## 6.5 Pre-Submission Self-Check Protocol

Before finalizing any section, verify the following checklist:

```text
[ ] STRUCTURE & MECHANICS
    [ ] Numbering strictly follows DCT decimal/alphanumeric hierarchy (1.0 -> 1.1 -> 1.1.1 -> A. -> A.1)
    [ ] Zero bullet characters (•, -, *, ▪) in body text; all lists use A., B., C. or 1., 2., 3.
    [ ] Every paragraph is between 2 and 5 sentences in length
    [ ] Exactly one logical transitional phrase used per paragraph

[ ] TONE & VOCABULARY
    [ ] Zero banned marketing words (user-friendly, seamless, cutting-edge, robust, etc.)
    [ ] System functionality described in present tense; completed development in past tense
    [ ] Strictly third-person impersonal perspective (no "I", "we", "our")

[ ] CONTENT INTEGRITY
    [ ] Project Context is at least two (2) full pages
    [ ] Specific Objectives follow What + How + Result and SMART criteria
    [ ] Related literature includes Anchor Theory + Auxiliary Theories + Comparative Matrix
    [ ] All citations strictly follow DCT bracketed code format [AUTH2024]
```
