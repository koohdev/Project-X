# Turnitin AI Detection Analysis — Chronicles of Arithmos Manuscript

**Date:** March 7, 2026  
**Turnitin AI Score:** 33%  
**Analyzed Files:** Chapter 1, Chapter 2, Chapter 3, Chapter 4, Acknowledgement

---

## How Turnitin AI Detection Works (2025–2026)

Turnitin flags text as "AI-generated" based on these signals:

| Signal | What It Means |
| :--- | :--- |
| **Low Perplexity** | Sentences follow highly predictable word sequences — the "next word" is always the obvious choice |
| **Syntactic Uniformity** | Many consecutive sentences share the same grammatical structure (Subject → will → verb → object) |
| **Overly Smooth Transitions** | Paragraphs flow too perfectly with balanced clauses and zero awkwardness |
| **Formulaic Templates** | Writing repeats a clear pattern: define → explain → apply, or "[X] is a [definition]. It will be used for [purpose]. The proponents utilize it because [reason]." |
| **Lack of Personal Voice** | No idiosyncratic phrasing, no informal markers, no "mistakes" that signal a human author |

> Turnitin analyzes text in ~250-word windows. It flags each window individually. Even if only scattered sections are AI-like, they sum to the total percentage.

---

## Risk Legend

| Risk | Meaning |
| :--- | :--- |
| 🔴 **HIGH** | Almost certainly flagged — extreme uniformity or classic AI template |
| 🟡 **MEDIUM** | Likely flagged — smooth academic formula that mimics AI output |
| 🟢 **LOW** | Probably safe — natural enough or too short to trigger detection |

---

## CHAPTER 1 — Introduction (Biggest Contributor)

Chapter 1 is the largest file (~64 KB, 1,105 lines) and contains the **most flagged content by volume**. The main culprits are the prose-format lists and the opening theoretical paragraphs.

---

### 🔴 FLAG #1 — Prose Lists of Enemies, Loot, Weapons, Skills, Equipment (Lines 33–87)

**Why flagged:** These ~55 lines contain hundreds of sentences with **identical grammatical structure** repeated back-to-back. This is the single biggest AI trigger in the entire manuscript.

**Pattern detected:** `"The [Enemy Name] will drop [Item Name]."`  /  `"The [Weapon Name] will be a [description]."`

**Flagged excerpts:**

> "The Slime will drop Green Gel. The Rat will drop a Rat Tail. The Bat will drop a Bat Wing. The Spider will drop a Sticky Web. The Hornet will drop an Insect Wing. The Wolf will drop a Wolf Pelt. The Bear will drop a Bear Claw. The Treant will drop a Living Branch." *(Line 33)*

> "The Long Sword will be a standard issue blade. The Woodcutter's Blade will be a simple cutting tool. The Wolf Fang Sword will be an animal-themed blade. The Forest Cutter will be a nature themed sword. The Bandit's Edge will be a thief's blade." *(Line 45)*

> "The Oak Staff will be a basic wooden staff. The Briar Rod will be a thorny stick. The Druid's Staff will be a nature themed pole. The Faerie Wand will be a small magical stick." *(Line 47)*

> "For the Swordsman, Strong Attack will deliver a heavy physical strike. Slash will execute a basic sword technique. Double Slash will hit the enemy twice in succession. Wide Swing will deal physical damage to all enemies." *(Line 61)*

> "Knockout will prevent characters from acting until revived. Poison will cause continuous damage at the end of every turn. Blind will greatly reduce physical attack precision." *(Line 77)*

> "Small Shields and Round Shields will provide basic protection. Bucklers will be lightweight shields. Kite Shields, Iron Shields, and Steel Shields will provide larger coverage and metal protection." *(Line 81)*

**These lines span approximately 30–40% of Chapter 1's word count.** Because they are pure repetitive templates, Turnitin's perplexity analyzer sees them as machine-generated text with near-zero entropy.

**Fix suggestion:** Convert these to **tables** instead of prose. Tables are not scored by Turnitin's sentence-level AI detector.

---

### 🔴 FLAG #2 — Character Roster as Prose (Lines 27–29)

**Why flagged:** Every character introduction follows the exact same Subject-Verb-Object template.

**Flagged excerpt:**

> "Kael will join as a knight companion. Elara will be recruited as a sorceress companion. Garrick will serve as a heavily armored tank companion. Sylas will join as a rogue companion. Isolde will be recruited as a healer companion. Thorne will serve as a ranger companion." *(Line 27)*

> "Elder Tobias will provide the initial story quests. Merchant Oryn will sell general goods. Receptionist Mila will act as a procedural quest hub. Bard Jareth will offer healing interactions." *(Line 29)*

**Fix suggestion:** Use a character table: `| Name | Role | Description |`

---

### 🟡 FLAG #3 — Opening Paragraphs of Section 1.1 (Lines 5–11)

**Why flagged:** Almost every sentence starts with "This [noun] will..." or "The [noun] will...", creating a highly predictable pattern within Turnitin's ~250-word sliding window.

**Flagged excerpt:**

> "The proposed project will be a 2D turn-based Role-Playing Game (RPG). While standard RPGs use random chance to decide combat outcomes, this game will implement a custom math battle system. In this system, the outcome of attacks, defenses, and skills will depend directly on the player's ability to solve math equations under a time limit." *(Line 5)*

> "This approach will address the problem of repetitive math drills by turning them into a combat system. It will help players practice the transition from basic math, like addition and subtraction, to intermediate operations, like PEMDAS. By doing this, the system will build mental math speed and precision. It will also provide direct rewards for mental effort, allowing players to level up and defeat bosses when they solve math problems correctly." *(Line 7)*

> "The project will integrate math exercises directly into its gameplay mechanics. Because advancing in the game will depend on answering math equations correctly, players will continuously practice their calculation skills as they play. This setup will create a purely interactive environment for arithmetic practice." *(Line 9)*

**Fix suggestion:** Vary sentence starters, break the "will" pattern, insert personal phrasing, or rewrite in mixed voice.

---

### 🟡 FLAG #4 — "Chocolate-Covered Broccoli" and Educational Games Paragraph (Lines 13–15)

**Why flagged:** Perfectly structured academic argumentation with smooth transitions. Classic AI pattern: problem → cause → consequence → solution.

**Flagged excerpt:**

> "Educational games often fail to retain player interest because of the 'Chocolate-Covered Broccoli' effect [1]. This occurs when developers take a standard, repetitive school task and place it behind game graphics. Because the learning mechanics are poorly integrated with the actual gameplay, students may recognize they are simply completing a disguised drill and lose motivation." *(Line 13)*

> "Games with limited replay value may also offer reduced incentive for students to return. *Chronicles of Arithmos* will address these issues through three integrated systems. First, the math battle system will function as the primary variable... Second, the system will feature a Level-Based Difficulty System... Third, to maintain replayability..." *(Line 15)*

**Fix suggestion:** Add more of your own interpretation/commentary rather than pure textbook-style explanation. Use less formulaic transitions.

---

### 🟡 FLAG #5 — Mathematics Anxiety Definition Paragraph (Line 17)

**Why flagged:** Follows a very typical AI template: cite definition → paraphrase → elaborate with smooth follow-up.

**Flagged excerpt:**

> "The primary purpose of this project will be to reduce Mathematics Anxiety among Grade 4–6 students. Richardson and Suinn (1972) defined this as 'a feeling of tension and anxiety that interferes with the manipulation of numbers' [3]. This phenomenon creates a psychological barrier; when students experience this tension, they will struggle to perform well in academics regardless of their actual aptitude or intelligence. Ashcraft (2002) further suggested that high math anxiety occupies a student's working memory capacity [4]. This means that because the student's brain is actively processing fear and worry, there is less mental energy left available to actually solve the math problem."

**Fix suggestion:** Inject more of your own phrasing between the citations. Break up the perfect logical chain.

---

### 🟡 FLAG #6 — Gamification / Low-Stakes Learning (Line 19)

**Why flagged:** Polished academic phrasing with common AI vocabulary like "direct feedback loop," "tangible," "rewarding reinforcement," "shift the learner's association."

**Flagged excerpt:**

> "By gamifying these math operations within a low-stakes, fantasy context, the game will aim to reduce the negative emotional responses usually associated with classroom drills. The system will provide a direct feedback loop where a correct calculation will result in a tangible in-game 'Critical Hit.' Seeing direct success will provide rewarding reinforcement, which may shift the learner's association with arithmetic from tension to confidence (Gee, 2003)."

---

### 🟡 FLAG #7 — Specific Objectives (Lines 99–143)

**Why flagged:** Each objective follows the same three-sentence template: "This module will serve as [purpose]. It will include [features]. The user will interact with this module by [interaction]."

**Flagged excerpt:**

> "This module will serve as the base structure for the custom math integration. It will include a time-based battle system, turn ordering, and character stat management..." *(Line 99)*

> "This module will serve as the core educational feature of the game. It will replace standard chance-based combat..." *(Line 103)*

> "This module will automatically adjust the complexity of the math equations..." *(Line 107)*

---

### 🟡 FLAG #8 — Scope Sections A–L (Lines 149–224)

**Why flagged:** Same formulaic intro pattern as the objectives, heavily repeated. "This module will feature... The user will interact with this module by..."

---

## CHAPTER 2 — Review of Related Literature (Medium Contributor)

### 🟡 FLAG #9 — Game-Based Learning Theory (Lines 7–9)

**Why flagged:** Smooth, textbook-quality explanation with perfect topic sentence → supporting detail → application chain.

**Flagged excerpt:**

> "Game-Based Learning (GBL) is a teaching approach that uses game mechanics like points, levels, and rewards to teach academic content through gameplay instead of traditional instruction (Prensky, 2001) [6]. The idea is that students learn the material as a result of playing the game, not by sitting through lectures or drills."

---

### 🟡 FLAG #10 — Mathematics Anxiety in Primary Education (Lines 13–15)

**Why flagged:** Perfect definition → explanation → application pattern. Very polished.

**Flagged excerpt:**

> "Mathematics anxiety, first described by Ashcraft, is a feeling of tension or fear that gets in the way of math performance [7]. This is common among students in Grades 4–6, where it affects working memory and creates emotional barriers, sometimes called affective filters, that cause students to avoid math activities altogether."

> "*Chronicles of Arithmos* deals with mathematics anxiety by turning arithmetic drills into fantasy RPG combat encounters. Instead of showing problems in a test format, the system presents each equation as a spell or attack input. This shifts the student's focus from 'taking a math test' to 'battling an enemy,' which helps reduce the stress that comes with timed academic assessments."

---

### 🟡 FLAG #11 — Flow Theory (Lines 19–23)

**Why flagged:** Clean three-part structure: problem → theory definition → application.

**Flagged excerpt:**

> "Flow Theory, introduced by Csikszentmihalyi, describes a mental state where a person is fully focused on an activity because the challenge level matches their current skill [8]. If a task is too easy, the person gets bored. If it is too hard, they get frustrated. The ideal state between these two is called 'flow.'"

---

### 🟡 FLAG #12 — Related Projects (Mage Math, Grand Prix, Prodigy) (Lines 32–62)

**Why flagged:** All three follow an identical rigid template: [Description] → [Similarities] → [Differences]. This structural repetition across three consecutive sections is a signal.

**Flagged excerpt (pattern visible across all three):**

> "Both Mage Math and *Chronicles of Arithmos* embed mathematical exercises into RPG combat and exploration. Both systems target primary school learners..."

> "Both Grand Prix Multiplication and *Chronicles of Arithmos* use game mechanics to present mathematical problems. Both systems target elementary-level students..."

> "Both Prodigy and *Chronicles of Arithmos* use Game-Based Learning (GBL) within a fantasy RPG framework. They share a 'Combat-to-Curriculum' loop..."

---

## CHAPTER 3 — Technical Background (Medium Contributor)

### 🔴 FLAG #13 — Software Descriptions (Lines 15–83)

**Why flagged:** Every single technology description follows the **exact same three-part formula**, repeated ~15 times across the chapter:

**Pattern:** `"[Tool] is a [generic definition]. It will be used/utilized in [phase] for [purpose]. The proponents utilize [tool] because [reason]."`

**Flagged excerpts:**

> "RPG Maker MZ is a game development engine designed for creating 2D role-playing games. It will be used in the core application development to construct the visual environment..." *(Line 17)*

> "HyperText Markup Language 5 (HTML5) is the standard markup language for structuring web content. Web Graphics Library (WebGL) is a JavaScript API for rendering 2D and 3D graphics within web browsers. HTML5 and WebGL will be used in the web-based deployment..." *(Line 21)*

> "Cascading Style Sheets (CSS) is a style-sheet language used to define the visual presentation and layout of HTML documents. CSS will be applied to the web container..." *(Line 25)*

> "JavaScript (ECMAScript 6) is a programming language used for creating dynamic and interactive content on web pages. JavaScript will serve as the core programming language..." *(Line 31)*

> "Visual Studio Code is an Integrated Development Environment (IDE) developed by Microsoft for writing, debugging, and managing code. It will be the primary IDE used for managing..." *(Line 35)*

> "Node.js is an open-source, server-side runtime environment that executes JavaScript outside of a web browser. It will be utilized during the development phase..." *(Line 39)*

> "PeerJS is a Web Real-Time Communication (WebRTC) wrapper library... It will be used to implement the Peer-to-Peer (P2P) Multiplayer Framework..." *(Line 43)*

> "GIMP is a free, open-source raster graphics editor... It will be utilized as the primary graphics editor..." *(Line 49)*

> "Canva is a web-based graphic design platform... It will be utilized as the primary design tool..." *(Line 53)*

> "Draw.io (also known as diagrams.net) is a free, web-based diagramming application... It will be utilized during the documentation and design phases..." *(Line 57)*

> "NW.js is an open-source framework... It will serve as the core runtime environment..." *(Line 63)*

> "GitHub is a cloud-based platform for hosting and managing source code repositories... It serves as the central repository..." *(Line 71)*

> "Git is a distributed version control system... The proponents use Git during the development phase..." *(Line 75)*

> "Vercel is a cloud-based deployment and hosting platform... It operates as the staging host..." *(Line 79)*

> "Hostinger is a web hosting service provider... It will serve as the production hosting platform..." *(Line 83)*

**This is 15 back-to-back instances of the same template.** This is one of the strongest AI signals in the manuscript.

**Fix suggestion:** Vary the sentence structure for each tool. Don't start every description with "[Tool] is a [definition]."

---

### 🟡 FLAG #14 — Implementation Peopleware (Lines 147–155)

**Why flagged:** Formulaic descriptions of user roles with smooth, balanced sentences.

**Flagged excerpt:**

> "Students (Grades 4-6) will serve as the primary operators of the system. They will engage directly with the Math Battle System to solve arithmetic equations, explore the game world, and progress through the narrative."

> "Mathematics teachers instructing Grades 4 to 6, along with the parents or guardians of those specific students, will act as secondary users who utilize the application as a supplementary educational tool."

---

## CHAPTER 4 — Methodology (Low–Medium Contributor)

### 🟡 FLAG #15 — Prototyping Model Phases (Lines 8–30)

**Why flagged:** Each phase starts with "In this phase, the proponents..." or "The proponents will..." creating a repeated pattern.

**Flagged excerpt:**

> "In this phase, the proponents defined the project objectives, scope, and mathematical requirements. The proponents reviewed the Grade 4 to 6 mathematics curriculum..." *(Line 10)*

> "The proponents created flowcharts to map the student navigation and battle mechanics. Wireframes were developed to design..." *(Line 14)*

> "The proponents built the initial prototype using RPG Maker MZ and JavaScript. The Math Battle System plugin was coded to generate..." *(Line 18)*

---

### 🟡 FLAG #16 — Technical Feasibility (Lines 46–64)

**Why flagged:** Smooth academic prose with polished transitions.

**Flagged excerpt:**

> "Existing educational game platforms such as Prodigy Math and Math Blaster address arithmetic instruction through gamified exercises; however, a common limitation is that mathematical tasks function as a separate reward layer rather than directly determining gameplay outcomes." *(Line 60)*

---

### 🟡 FLAG #17 — Risk Assessment (Lines 219–221)

**Why flagged:** Long, compound paragraph with smooth listings of risks and mitigations. Has that "AI summary" feel.

---

### 🟡 FLAG #18 — UI Design Description (Lines 227–233)

**Why flagged:** Polished, formulaic description of color choices and font selection.

---

## ACKNOWLEDGEMENT (Low–Medium Contributor)

### 🟡 FLAG #19 — Entire Acknowledgement Page (Lines 3–17)

**Why flagged:** Acknowledgements are one of the MOST commonly AI-generated sections. The phrasing "express their sincerest gratitude," "heartfelt thanks," "unwavering love, support, and understanding" are extremely common AI patterns.

**Flagged excerpt:**

> "The proponents would like to express their sincerest gratitude to the Almighty God, for the wisdom, strength, and guidance that made the completion of this Capstone Project possible."

> "Sincere appreciation is extended to Mr. Rossano C. Samson, Dean of the College of Computer Studies, for his leadership and support in upholding the academic standards..."

> "To their families, the proponents offer their deepest thanks for the unwavering love, support, and understanding given throughout this journey."

---

## Summary: Estimated Contribution to the 33% AI Score

| Section | Risk Level | Estimated % of Total AI Score | Reason |
| :--- | :--- | :--- | :--- |
| **Ch.1 Prose Lists** (enemies, weapons, skills, equipment, lines 27–87) | 🔴 HIGH | **~12–15%** | Extreme syntactic repetition across massive blocks of text |
| **Ch.3 Software Descriptions** (lines 15–83) | 🔴 HIGH | **~5–7%** | 15 consecutive tools described with identical template |
| **Ch.1 Opening Paragraphs** (lines 5–19) | 🟡 MEDIUM | **~3–4%** | Predictable "will" pattern, smooth academic prose |
| **Ch.1 Objectives + Scope** (lines 99–224) | 🟡 MEDIUM | **~3–4%** | Repetitive module description template |
| **Ch.2 Theories + Related Projects** (lines 7–62) | 🟡 MEDIUM | **~2–3%** | Formulaic define → explain → apply pattern |
| **Ch.4 Prototyping + Feasibility** (lines 8–64) | 🟡 MEDIUM | **~1–2%** | Repeated "proponents will" starter |
| **Acknowledgement** (lines 3–17) | 🟡 MEDIUM | **~1%** | Classic AI acknowledgement template |
| **TOTAL ESTIMATED** | | **~27–36%** | Consistent with the reported **33%** score |

---

## Top Recommendations for Lowering the Score

### 1. Convert Prose Lists → Tables (Biggest Impact)

All enemy drops, weapon descriptions, skill descriptions, and equipment descriptions in Chapter 1 should be **tables**, not prose sentences. Tables are not analyzed by Turnitin's sentence-level AI detector.

**Before (flagged):**
> "The Slime will drop Green Gel. The Rat will drop a Rat Tail. The Bat will drop a Bat Wing."

**After (safe):**

| Enemy | Drop |
| :--- | :--- |
| Slime | Green Gel |
| Rat | Rat Tail |
| Bat | Bat Wing |

### 2. Break the "[Tool] is a [definition]" Template in Chapter 3

Vary the opening of each technology description. Don't start every paragraph with the tool name followed by a textbook definition.

### 3. Vary Sentence Starters in Chapter 1

The "This module will..." and "It will..." pattern repeats dozens of times. Mix in different sentence structures.

### 4. Add Personal Voice to Theory Sections

In Chapters 1 and 2, the theory explanations are too smooth. Add your own observations, connect ideas in unexpected ways, or use less formal bridging language.

### 5. Rewrite the Acknowledgement

Use more personal, unique phrasing rather than the standard template phrases. Reference specific things people did.

---

*This analysis is an educated estimate based on how Turnitin's AI detection algorithm (perplexity + burstiness scoring) works. The actual flagged sections may vary slightly. Turnitin does not publicly disclose exact detection algorithms.*
