# 🔍 ACADEMIC WRITING CHECKER — Reference Guide

> **Purpose:** Detect and replace problematic wording in Capstone Chapters 1–5  
> **How to Use:** Invoke via the `/check-writing` workflow, or mention this file when pasting chapter text  
> **Companion:** Works alongside `KNOWLEDGE_BASE.md` PART 4 (Tone Sanitation / Banned Words)

---

## ⚡ QUICK SCAN REFERENCE (Machine-Friendly)

> **For the AI:** Use these condensed lists for fast pattern matching in a single pass. When a match is found, consult the detailed tables in the relevant category for replacement suggestions and context.

### 🚫 Banned Words (Category 7 — all conjugations banned)

`efficient, effective, innovative, powerful, reliable, streamlined, user-friendly, robust, scalable, secure, seamless, cutting-edge, optimize, enhance, improve, ensure, accurate, fast, quick, intuitive, easy`

### 🤖 AI-Flagged Words (Category 1A)

`delve, tapestry, nuanced, intricate, multifaceted, meticulous, pivotal, foster, realm, landscape, paradigm, underpins, revolutionize, reverberate, cornerstone, spearhead, culminate, underscore, commendable, noteworthy, leverage, harness, navigate, embark, endeavor, comprehensive, holistic, empower, elevate, groundbreaking, advanced, engaging, immersive, ecosystem, real-world, high-quality, injection, distinguished`

### 🤖 AI-Flagged Phrases (Category 1B)

`"It is worth noting", "It's important to consider", "In today's rapidly evolving", "In the ever-changing landscape", "plays a crucial role", "has garnered significant attention", "serves as a testament", "at the heart of", "pave the way", "shed light on", "a game-changer", "bridges the gap", "a deep dive", "the key takeaway", "let's explore", "when it comes to", "in essence", "from a [X] perspective", "this approach offers", "a significant factor", "one can argue", "it goes without saying", "without further ado", "imagine this", "in a nutshell", "valuable insights", "expert guidance", "introduces features that distinguish"`

### ⚠️ Vague Quantifiers (Category 2B)

`a lot of, many (uncited), some (uncited), several, most (uncited), few, significant (no metric), various, numerous, a great deal of, things, stuff`

### ⚠️ Absolute Claims (Category 2C)

`always, never, every, all (unsupported), none (unsupported), the best, the only, perfect, impossible, guarantee`

### 👤 First Person (Category 3A — remove all)

`I, me, my, mine, we, us, our, ours, myself, ourselves, "I think", "I believe", "In my opinion", "We decided", "Our system", "We conducted", "We observed", "We used", "the team", "our team"`

### 👤 Second Person (Category 3B — remove all)

`you, your, yours, "You can see", "You need to", "Your data", "If you click", "You will notice"`

### 👤 Contractions (Category 3C — expand all)

`don't, can't, won't, it's, they're, we're, couldn't, shouldn't, wouldn't, hasn't, haven't, isn't, aren't, there's, that's`

### 🔬 AI Structural Patterns to Watch (Category 1C)

- Every paragraph starting with "Moreover," "Furthermore," "Additionally"
- "In conclusion, it is evident that..."
- Excessive em-dashes (—) mid-sentence
- All sentences same length (15–20 words)
- Exactly 3 or 5 bullet points with identical structure
- Redundancies: "collaborate together," "completely eliminate," "future plans," "end result," "basic fundamentals"

---

## HOW THIS CHECKER WORKS

When you paste your chapter text and invoke this checker, the AI will:

1. **Scan** the text against every category below (Categories 1–10)
2. **Flag** each problematic phrase with its category tag (e.g., `[AI-PHRASE]`, `[VAGUE]`)
3. **Assign severity** using the framework below
4. **Suggest** a concrete replacement that fits the sentence context
5. **Output** per-category findings tables, a summary, priority fixes, and a cleaned version

### Severity Framework

Every finding must be assigned a severity level:

| Severity | Tag | What It Covers | Examples |
|----------|-----|----------------|----------|
| 🔴 **Critical** | `CRIT` | Factual errors, missing required sections, structural misnumbering, wrong content in wrong chapter | "CSS is a container" (factually wrong); missing comparative matrix; section "2.3.3" should be "2.2.3" |
| 🟠 **High** | `HIGH` | Banned words, uncited claims, person-view violations, run-on/fragment sentences | "ensure," "studies show" (no cite), first-person usage |
| 🟡 **Medium** | `MED` | AI phrasing, jargon without definition, paragraph structure issues | "delve," undefined "WebRTC," single-sentence paragraphs |
| 🟢 **Low** | `LOW` | Minor style preferences, small comma issues, transition variety | Missing Oxford comma, repeated transition word |

---

## CATEGORY 1: AI-GENERATED PHRASING 🤖

These words and phrases are statistical telltale signs of AI-generated text. Panelists and Turnitin AI detectors flag these heavily.

### 1A. Single Words to Flag

| Flagged Word | Why It's Flagged | Suggested Replacements |
|---|---|---|
| delve | Top AI-overused word | examine, investigate, explore, analyze |
| tapestry | AI metaphor cliché | combination, mixture, collection |
| nuanced | AI filler adjective | specific, detailed, particular |
| intricate | AI filler adjective | complex, detailed, multi-part |
| multifaceted | AI filler adjective | varied, diverse, multiple |
| meticulous | AI formality cliché | careful, thorough, systematic |
| pivotal | AI emphasis word | important, central, key |
| foster | AI verb cliché | support, develop, build |
| realm | AI metaphor cliché | area, field, domain |
| landscape | AI metaphor (non-literal) | field, environment, context |
| paradigm | AI buzzword | model, approach, framework |
| underpins | AI formality | supports, forms the basis of |
| revolutionize | AI hype verb | change, transform, update |
| reverberate | AI dramatic verb | affect, influence, impact |
| cornerstone | AI metaphor cliché | foundation, basis, core |
| spearhead | AI dramatic verb | lead, initiate, begin |
| culminate | AI formality | result in, lead to, end with |
| underscore | AI emphasis verb | highlight, emphasize, show |
| commendable | AI flattery | notable, significant |
| noteworthy | AI filler | significant, important |
| leverage | AI buzzword (non-technical) | use, apply, utilize |
| harness | AI metaphor | use, apply, employ |
| navigate | AI metaphor (non-literal) | manage, handle, address |
| embark | AI dramatic verb | begin, start, undertake |
| endeavor | AI formality | effort, attempt, project |
| comprehensive | AI filler adjective | complete, full, thorough |
| holistic | AI buzzword | complete, overall, total |
| empower | AI buzzword | enable, allow, support |
| elevate | AI hype verb | raise, increase, improve upon |
| groundbreaking | AI hype | new, novel, original |
| advanced | AI filler adjective | additional, extended, specialized |
| engaging | AI buzzword | interactive, participatory |
| immersive | AI overused adjective | interactive, experiential |
| ecosystem | AI metaphor (non-literal) | collection, range, set |
| real-world | AI overused modifier | actual, practical, observed |
| high-quality | AI praise pattern | well-structured, properly formatted |
| injection | AI dramatic word choice | addition, inclusion, integration |
| distinguished | AI comparison pattern | differs, varies, stands apart |

### 1B. Phrases to Flag

| Flagged Phrase | Suggested Replacement |
|---|---|
| "It is worth noting that..." | *(Remove entirely and state the point directly)* |
| "It's important to consider..." | *(Remove — just state what should be considered)* |
| "In today's rapidly evolving..." | "In the current..." or "At present..." |
| "In the ever-changing landscape of..." | "In the field of..." |
| "plays a crucial role in..." | "contributes to..." or "is used in..." |
| "has garnered significant attention" | "has received attention" or "is widely studied" |
| "serves as a testament to..." | "demonstrates..." or "shows..." |
| "at the heart of..." | "central to..." or "the basis of..." |
| "pave the way for..." | "enable..." or "allow for..." |
| "shed light on..." | "clarify..." or "explain..." |
| "a game-changer" | *(Remove — use specific description instead)* |
| "bridges the gap between..." | "connects..." or "links..." |
| "a deep dive into..." | "an analysis of..." or "a review of..." |
| "the key takeaway is..." | *(Remove — state the point directly)* |
| "let's explore..." | *(Remove — not academic tone)* |
| "when it comes to..." | "regarding..." or "for..." |
| "in essence..." | *(Remove or replace with specific restatement)* |
| "from a [X] perspective..." | "regarding [X]..." or "in terms of [X]..." |
| "this approach offers..." | "this method provides..." |
| "a significant factor is..." | "[Factor] affects..." |
| "one can argue that..." | *(State the argument directly)* |
| "it goes without saying..." | *(Remove entirely — just say it)* |
| "without further ado..." | *(Remove entirely)* |
| "imagine this..." | *(Remove entirely — not academic)* |
| "in a nutshell..." | *(Remove — rephrase directly)* |
| "valuable insights" | "guidance" or "recommendations" |
| "expert guidance" | "guidance" |
| "introduces features that distinguish it from" | "includes features that differ from" |

### 1C. Structural Patterns That Signal AI

| Pattern | What to Look For | Fix |
|---|---|---|
| **Over-smooth transitions** | Every paragraph starts with "Moreover," "Furthermore," "Additionally" | Vary transitions; some paragraphs need no transition word (see Transition Reference below) |
| **Formulaic conclusions** | "In conclusion, it is evident that..." | Tie back to objectives specifically |
| **Excessive em-dashes** | Sentences broken by — em-dashes — mid-thought | Use commas or restructure the sentence |
| **Uniform sentence length** | All sentences are 15–20 words with no variation | Mix short (8–12 words) and medium (15–22 words) sentences |
| **Bullet-point-like paragraphs** | Short, choppy paragraphs that read like a bulleted list | Merge related points into flowing paragraphs |
| **Symmetrical lists** | Exactly 3 or 5 points with identical sentence structure | Vary count and structure naturally |

#### Tautology / Redundancy (REMOVE the redundant word)

| Redundancy | Fix |
|---|---|
| "collaborate together" | "collaborate" |
| "completely eliminate" | "eliminate" |
| "future plans" | "plans" |
| "past experience" | "experience" |
| "end result" | "result" |
| "basic fundamentals" | "fundamentals" |
| "each and every" | "each" or "every" |
| "first and foremost" | "first" |
| "still remains" | "remains" |
| Same adjective repeated in one sentence | Remove one instance (e.g., "immersive...immersive") |

#### Transition Variety Reference

Do **not** start every paragraph with the same transition word. Use varied types:

| Type | Options |
|------|---------|
| **Contrast** | However, In contrast, On the other hand, Conversely |
| **Addition** | Also, In addition, Similarly, Likewise |
| **Cause/Effect** | As a result, Consequently, Therefore, Thus |
| **Sequence** | First, Next, Subsequently, Finally |
| **Example** | For instance, Specifically, In particular |
| **Summary** | In summary, Overall, To summarize |
| **No transition** | Start the sentence directly — not every paragraph needs a connector |

---

## CATEGORY 2: SUBJECTIVE & VAGUE CLAIMS ⚠️

These weaken academic credibility. Every claim must be evidence-backed.

### 2A. Subjective / Opinion Phrases

| Flagged Phrase | Why It's Flagged | Replacement Strategy |
|---|---|---|
| "obviously..." | Assumes the reader agrees | Remove — state the evidence |
| "clearly..." | Same as above | Remove or cite the source |
| "undoubtedly..." | Unsubstantiated certainty | "Research by [Author] indicates..." |
| "everyone knows that..." | Unsupported universal claim | Cite a specific source |
| "needless to say..." | If it's needless, remove the sentence | Remove entirely |
| "it is common knowledge..." | Must still be cited | Replace with citation |
| "it is believed that..." | Who believes? | Name the source |
| "many experts agree..." | Which experts? | "[Author, Year] states..." |
| "studies show..." (uncited) | Which studies? | Cite the specific study |
| "research suggests..." (uncited) | Which research? | Cite the specific research |
| "arguably..." | Weak qualifier | State the argument with evidence |

### 2B. Vague Quantifiers

| Flagged Term | Replacement |
|---|---|
| "a lot of" | Specify a number or percentage |
| "many" (uncited) | Provide data: "78% of respondents..." |
| "some" (uncited) | Specify: "three out of five..." |
| "several" | Specify the actual count |
| "most" (uncited) | Cite the statistic |
| "few" | Specify: "two participants..." |
| "significant" (no metric) | Define significance: "a 30% increase..." |
| "various" | List them: "PHP, Java, and Python..." |
| "numerous" | Provide the actual count |
| "a great deal of" | Quantify with data |
| "things" | Name the specific items |
| "stuff" | Name the specific items |

### 2C. Absolute Claims to Avoid

| Flagged Term | Why | Replacement |
|---|---|---|
| "always" | Rarely provable | "frequently," "in most cases," or cite data |
| "never" | Rarely provable | "rarely," "in no observed case" + citation |
| "every" | Overgeneralization | Specify the actual scope |
| "all" (unsupported) | Overgeneralization | "the majority of..." + citation |
| "none" (unsupported) | Overgeneralization | "no observed instances" + citation |
| "the best" | Subjective superlative | "one of the widely used..." or compare with data |
| "the only" | Difficult to prove | "among the few..." or "a primary..." |
| "perfect" | Nothing is perfect in research | "suitable," "appropriate," "well-suited" |
| "impossible" | Very strong claim | "not feasible given..." |
| "guarantee" | Cannot be guaranteed | "is expected to," "is designed to" |

---

## CATEGORY 3: PERSON-VIEW VIOLATIONS 👤

Academic writing uses **third person, impersonal voice**. Flag all first and second person usage.

### 3A. First Person (REMOVE)

| Flagged | Replacement Strategy |
|---|---|
| I, me, my, mine | "The proponents," "the researchers," "This study" |
| we, us, our, ours | "The proponents," |
| myself, ourselves | Rephrase in third person |
| "I think..." | Remove — state the claim directly |
| "I believe..." | Remove — state with evidence |
| "In my opinion..." | Remove — the thesis is your opinion by definition |
| "We decided to..." | "The proponents opted to..." |
| "Our system..." | "The proposed system..." or "The system..." |
| "We conducted..." | "A survey was conducted..." (passive) or "The proponents conducted..." |
| "We observed..." | "The results indicate..." |
| "We used..." | "[Tool] was used..." or "The methodology employed..." |
| **"the team," "our team"** | **"The proponents" — never use "team" to refer to the group** |

### 3B. Second Person (REMOVE)

| Flagged | Replacement Strategy |
|---|---|
| you, your, yours | "the user," "the administrator," "one" |
| "You can see..." | "The figure shows..." |
| "You need to..." | "The user must..." |
| "Your data..." | "The user's data..." |
| "If you click..." | "When the user selects..." |
| "You will notice..." | "It can be observed that..." |

### 3C. Informal Contractions (EXPAND)

| Flagged | Replacement |
|---|---|
| don't | do not |
| can't | cannot |
| won't | will not |
| it's (= it is) | it is |
| they're | they are |
| we're | we are |
| couldn't | could not |
| shouldn't | should not |
| wouldn't | would not |
| hasn't | has not |
| haven't | have not |
| isn't | is not |
| aren't | are not |
| there's | there is |
| that's | that is |

### 3D. Ambiguous Pronouns (CLARIFY)

**RULE:** Never start a section or paragraph with a pronoun (It, This, They, These, He, She) unless the antecedent is unambiguously in the immediately preceding sentence within the same section.

| Flagged | Why | Fix |
|---|---|---|
| "It utilizes..." (at section start) | No antecedent — which "it"? | Name the subject: "DragonBox Algebra uses..." |
| "This explores..." (at section start) | Ambiguous "This" — this what? | "This research project explores..." or name it directly |
| "They guided..." | Singular antecedent (one person) | "He guided..." or "The adviser guided..." |
| "These are used..." | No clear antecedent | "These browsers are used..." or name them |
| "It is a..." (starting a subsection) | Reader has to guess the referent | Start with the proper noun: "PeerJS is a..." |

---

## CATEGORY 4: OVERLY TECHNICAL / DEEP WORDING 🔬

Capstone documentation must be understandable by panelists who may not be specialists in your exact technology stack. Flag jargon that isn't defined or is unnecessary.

### 4A. Jargon Without Definition

**RULE:** Any technical term used for the **first time** in a chapter MUST be defined or explained in parentheses or in a follow-up sentence.

| Example — Flagged | Example — Fixed |
|---|---|
| "The API uses RESTful endpoints." | "The Application Programming Interface (API) uses Representational State Transfer (REST) endpoints, which allow client applications to request data over HTTP." |
| "We implemented JWT authentication." | "The system implements JSON Web Token (JWT) authentication, a standard method for securely transmitting user identity between client and server." |
| "Using a NoSQL database..." | "Using a non-relational (NoSQL) database..." |

### 4B. Unnecessarily Deep Technical Descriptions

If the section is **Chapter 1 (Introduction)**, technical depth should be **minimal**. Save deep technical discussion for **Chapter 3 (Technical Background)**.

| Context | Flagged Example | Why | Fix |
|---|---|---|---|
| Chapter 1 | "The system's microservice architecture uses gRPC for inter-service communication with protocol buffers for serialization" | Too deep for intro | "The system uses a modular architecture that allows independent components to communicate." |
| Chapter 2 | "The O(n log n) time complexity of the sorting algorithm..." | Too deep unless comparing algorithms | Remove or simplify unless directly comparing related systems |
| Chapter 1 | "Leveraging containerized Docker environments with Kubernetes orchestration..." | Intro doesn't need deployment details | "The system is designed for scalable deployment." |

### 4C. Buzzword Stacking

**RULE:** Do not stack more than 2 technical terms in a single sentence without explanation.

| Flagged | Fixed |
|---|---|
| "The cloud-native, AI-powered, blockchain-enabled IoT platform..." | Split into separate sentences, each explaining one technology and its role |
| "Using machine learning, natural language processing, and computer vision..." | Dedicate a sentence to each, explaining its purpose in the project |

---

## CATEGORY 5: CHAPTER RELEVANCE CHECK 📋

Content must be relevant to the specific chapter. This checks for misplaced content AND correct paragraph structure per chapter.

### 5A. Chapter 1 — Introduction

**Content Scope:**

| ✅ Belongs | ❌ Does NOT Belong |
|---|---|
| Problem description (global → local) | Detailed code explanations |
| Project justification | Hardware/software specifications |
| General system overview | Database schema details |
| Objectives (SMART format) | Test results |
| Scope and limitations | Development methodology phases |

### 5B. Chapter 2 — Review of Related Literature/Systems

**Content Scope:**

| ✅ Belongs | ❌ Does NOT Belong |
|---|---|
| Anchor theory + supporting theories | Your own system's features |
| Related projects/systems overview | Your methodology |
| Comparative matrix | Your test results |
| Screenshots of related systems | Your implementation details |
| Citations and references | Unrelated theories with no tie to your project |

**Required Paragraph Structure — Related Theories:**

Each theory subsection must follow this formula:

| Part | Purpose | Example Starter |
|------|---------|-----------------|
| **1. DEFINE** | Define the theory and cite its originator | "[Theory], as formulated by [Author], is..." |
| **2. RELEVANCE** | Explain why this theory matters to the project | "This theory is relevant because..." |
| **3. CONNECT** | Show how the proposed system applies this theory | "Chronicles of Arithmos applies [Theory] by..." |
| **4. SUPPORTING EXAMPLE** | Cite an existing system that also uses this theory | "[System] demonstrates [Theory] in practice by..." |

**Required Paragraph Structure — Related Projects:**

Each related project must follow this formula:

| Part | Purpose |
|------|---------|
| **Title + Metadata** | Developer, Date Published, Reference URL |
| **Overview** | What the system is and does (neutral description) |
| **Similarities** | What it shares with your proposed system |
| **Differences** | How your proposed system differs |

### 5C. Chapter 3 — Technical Background

**Content Scope:**

| ✅ Belongs | ❌ Does NOT Belong |
|---|---|
| Hardware requirements | Problem statement (belongs in Ch. 1) |
| Software tools and technologies | Related literature (belongs in Ch. 2) |
| Peopleware | Methodology steps (belongs in Ch. 4) |
| Network architecture | Test results (belongs in Ch. 4) |
| How technologies will be used | Business justification (belongs in Ch. 1) |

**Required Paragraph Structure — Each Technology:**

Every software/hardware paragraph in Chapter 3 must follow this 4-part formula:

| Part | Purpose | Example Starter |
|------|---------|-----------------|
| **1. WHAT IT IS** | Define the technology in one sentence | "[Tool] is a [category] used to [general purpose]." |
| **2. WHERE IT'S USED** | State where in the project it applies | "[Tool] will be used/applied to [specific module/phase]." |
| **3. WHY** | Justify why this tool was chosen | "The proponents utilize [tool] because [technical reason]." |
| **4. OUTCOME** | State the benefit or result | "...allowing/so that [benefit for project/users]." |

**Example — Before vs. After:**

❌ **Without definition:**
> CSS will be used as the web container (index.html) that wraps the game engine. The proponents utilize CSS to handle the scaling of the game canvas.

✅ **With 4-part formula:**
> Cascading Style Sheets (CSS) is a style-sheet language used to define the visual presentation and layout of HTML documents. CSS will be applied to the web container (index.html) that hosts the game engine. The proponents utilize CSS to handle the scaling of the game canvas across different screen sizes and to position the "Virtual Keypad" overlay, so that the interface remains usable on touch-screen devices.

### 5D. Chapter 4 — Methodology, Results and Discussion

**Content Scope:**

| ✅ Belongs | ❌ Does NOT Belong |
|---|---|
| SDLC methodology and phases | Background of the problem (Ch. 1) |
| Feasibility studies | Theory discussion (Ch. 2) |
| Requirements modeling (DFD, Use Case) | General technology overview (Ch. 3) |
| System design and architecture | Extended literature review |
| Test plans and results | Recommendations (belongs in Ch. 5) |
| Implementation details | |

### 5E. Chapter 5 — Conclusion and Recommendations

**Content Scope:**

| ✅ Belongs | ❌ Does NOT Belong |
|---|---|
| Summary of accomplishments tied to specific objectives | New data or findings not discussed earlier |
| Conclusions referenced back to each objective | Extended methodology discussion |
| Recommendations for future work and enhancements | Repetition of Chapter 1 introduction |
| Suggested future research directions | New literature not previously reviewed |
| Limitations acknowledged and lessons learned | Detailed test results (belongs in Ch. 4) |

---

## CATEGORY 6: TITLE RELEVANCE CHECK 📌

Every sentence in every chapter should connect back to the project title.

### 6A. Common Title Drift Problems

| Problem | Example | Fix |
|---|---|---|
| **Off-topic tangent** | Title is about "Inventory System" but a paragraph discusses general e-commerce trends | Tie back: "These trends directly affect how inventory systems must track stock levels across online and physical stores." |
| **Generic filler** | "Technology has changed the world significantly over the past decades." | Replace with project-specific context: "Inventory management practices have shifted from manual logbooks to digital systems in the past decade [CITE]." |
| **Unrelated theory** | Title is about a "Patient Records System" but you discuss AI/ML theory at length | Only include theories that directly relate to your system |
| **Scope creep in writing** | Your system is a POS, but you write paragraphs about ERP features | Refocus every paragraph back to your project's scope |

### 6B. Quick Self-Test

For each paragraph, ask:

1. Does this paragraph mention or relate to the project by name or function?
2. If someone read ONLY this paragraph, would they know what project this paper is about?
3. Can I draw a direct line from this paragraph to one of my specific objectives?

If the answer to all three is **NO**, the paragraph needs revision or removal.

---

## CATEGORY 7: DCT-SPECIFIC BANNED WORDS 🚫

*(Synced from KNOWLEDGE_BASE.md PART 4)*

> **RULE:** All conjugated forms of a banned word are also banned. If "ensure" is banned, then "ensures," "ensuring," and "ensured" are ALL banned. If "improve" is banned, then "improves," "improving," "improved," and "improvement" are ALL banned. Apply this rule to every word in the table below.

### 7A. Banned Words

| Banned Word | Safe Replacements |
|---|---|
| efficient | supports, facilitates, performs |
| effective | functional, capable, operational |
| innovative | proposed, developed, designed |
| powerful | capable, high-capacity |
| reliable | consistent, tested, verified |
| streamlined | simplified, organized |
| user-friendly | accessible, usable, navigable |
| robust | stable, tested, structured |
| scalable | expandable, modular, extensible |
| secure | protected, access-controlled, encrypted |
| seamless | integrated, continuous, uninterrupted |
| cutting-edge | current, modern, recent |
| optimize | adjust, configure, refine |
| enhance | extend, add, expand |
| improve | update, modify, revise |
| ensure | verify, validate, confirm |
| accurate | precise, validated, verified |
| fast | within [X] seconds, prompt, timely |
| quick | prompt, timely, within [X] seconds |
| intuitive | clear, structured, guided |
| easy | straightforward, simplified, accessible |

### 7B. Borderline Words (Flag for Awareness)

These are not strictly banned but are consistently flagged by panelists and AI detectors. Prefer the replacements when possible:

| Borderline Word | Why It's Risky | Safer Replacement |
|---|---|---|
| engaging | AI buzzword; close to "innovative" tone | interactive, participatory |
| immersive | AI overused; subjective claim without evidence | interactive, experiential |
| advanced | AI filler; vague without context | additional, extended, specialized |
| high-quality | AI praise pattern; subjective | well-structured, properly formatted |
| native performance | Vague technical claim | "without performance degradation" or remove |

---

## CATEGORY 8: GRAMMAR & MECHANICS ✏️

These are common grammar and structural errors found in capstone writing. Each is a concrete, checkable rule.

### 8A. Punctuation Errors

| Rule | Flagged Example | Fix |
|---|---|---|
| **Missing possessive apostrophe** | "the proponents Capstone Adviser" | "the proponents' Capstone Adviser" |
| **Missing possessive apostrophe** | "students computers" | "students' computers" |
| **Missing closing punctuation** | "Math Battle System. (no closing `"`) | Add the missing `"` or `)` |
| **Double punctuation** | "massive online server.." | Remove the extra period |
| **Missing comma in lists** | "a programmer, UI/UX designer, tester and graphic designer" | "a programmer, a UI/UX designer, a tester, and a graphic designer" |

### 8B. Sentence Structure Errors

| Rule | Flagged Example | Fix |
|---|---|---|
| **Comma splice** | "exercises, however, a common limitation..." (two independent clauses joined by comma) | "exercises; however, a common limitation..." or split into two sentences |
| **Sentence fragment** | "For users accessing the application via the web browser deployment." | Not a complete sentence — rewrite: "Users who access the application via the web browser deployment will require..." |
| **Run-on sentence** | Two independent clauses joined with comma + repeated subject | Split into two sentences |
| **Incorrect preposition** | "focuses more about" | "focuses more on" |

### 8C. Article and Pronoun Errors

| Rule | Flagged Example | Fix |
|---|---|---|
| **Missing articles in series** | "a programmer, UI/UX designer, tester" | "a programmer, a UI/UX designer, a tester" — use consistent articles |
| **Pronoun-antecedent mismatch** | "They guided" (referring to singular Mr. Apostol) | "He guided" or "The adviser guided" |
| **Ambiguous "They/These/It"** | "They will be used in the testing phase" (what will?) | "These browsers will be used in the testing phase" |

### 8D. Passive Voice Overuse

**RULE:** If more than 60% of sentences in a single paragraph use passive voice ("was developed," "was implemented," "was utilized"), flag the paragraph for revision. Some passive voice is acceptable in academic writing, but overuse makes text flat and difficult to read.

| Flagged Pattern | Fix |
|---|---|
| "was developed... was implemented... was tested... was deployed..." (4+ passive in a row) | Alternate: "The proponents developed... The system implements... Testing confirmed..." |

---

## CATEGORY 9: DCT FORMATTING & CITATIONS 📏

### 9A. Citation Format

**RULE:** DCT uses a specific citation code format. Flag any non-DCT citation format:

| Flagged Format | Expected DCT Format | Example |
|---|---|---|
| [1], [2], [3] (numbered) | [CODE] = first 4 chars of author's last name + year | [WARD2023] |
| (Author, Year) — APA style | [CODE] | [KARA2024] |
| Author (Year) — narrative APA | [CODE] | [PERT2023] |
| Footnotes / endnotes | [CODE] inline | [HULSE2023] |
| Same author, same year | Add letter suffix | [MILL1991a], [MILL1991b] |

### 9B. Formatting Rules (Cross-Reference from KNOWLEDGE_BASE.md)

| Issue | DCT Rule |
|---|---|
| Bullet points (•, -, *) in body text | Use **A., B., C.** lettered format or **tables** instead — NO bullet symbols in body text |
| Table numbering | `Table <chapter#>-<table#>: <Table Title>` (e.g., "Table 3-1: Hardware Requirements") |
| Figure numbering | `Figure <chapter#>-<figure#>: <Figure Title>` (e.g., "Figure 2-2: Prodigy Game Menu") |
| Figure captions | Must accurately describe the content — flag mismatches (e.g., caption says "Arcademics" but image shows Prodigy) |
| Date format | Use consistent format throughout the document |
| Section numbering | Must follow sequential decimal format (1.1, 1.2, 1.2.1) — flag jumps like "2.2.2" → "2.3.3" |

---

## CATEGORY 10: PARAGRAPH STANDARDS 📐

### 10A. Paragraph Length

| Rule | Standard |
|---|---|
| **Minimum depth** | Every paragraph must have **2–5 sentences** |
| **Single-sentence paragraph** | 🚫 Flag — merge with adjacent paragraph or expand with supporting detail |
| **Overly long paragraph** | >8 sentences — consider splitting into two focused paragraphs |
| **Thin named subsection** | If a named subsection (e.g., "A.3 Canva") has only 1–2 sentences, it needs expansion to meet the 2–5 sentence standard |

### 10B. Paragraph Completeness

Every body paragraph should contain:

| Element | Purpose |
|---|---|
| **Topic sentence** | States the main point of the paragraph |
| **Supporting detail** | Evidence, example, or explanation |
| **Connection** | Links back to the thesis/objective or transitions to the next idea |

Flag paragraphs that are only topic sentences with no supporting detail.

---

## OUTPUT FORMAT

When this checker is invoked, results **must** be formatted as:

```
## 🔍 Writing Check Results for [Chapter X.X — Section Name]

> **File Checked:** `[filename]`  
> **Date:** YYYY-MM-DD  
> **Checker Reference:** `ACADEMIC_WRITING_CHECKER.md`

---

## Findings

### Category 1 — AI Phrasing 🤖

| # | Line | Phrase | Tag | Severity | Issue | Suggested Fix |
|---|------|--------|-----|----------|-------|---------------|
| 1 | 12 | "delve into the intricacies" | AI-PHRASE | MED | AI cliché | "examine the details of" |

### Category 2 — Subjective & Vague Claims ⚠️

| # | Line | Phrase | Tag | Severity | Issue | Suggested Fix |
|---|------|--------|-----|----------|-------|---------------|
| 2 | 18 | "many users" | VAGUE | HIGH | No quantifier | "Based on [CITE], X% of users" |

### Category 3 — Person-View Violations 👤

(same table format — or "No violations found ✅" if clean)

### Category 4 — Overly Technical / Deep Wording 🔬

(same table format)

### Category 5 — Chapter Relevance 📋

(same table format — include paragraph structure violations here)

### Category 6 — Title Drift 📌

(same table format)

### Category 7 — DCT Banned Words 🚫

| # | Line | Phrase | Tag | Banned Word | Severity | Suggested Replacement |
|---|------|--------|-----|-------------|----------|-----------------------|

### Category 8 — Grammar & Mechanics ✏️

| # | Line | Issue | Severity | Suggested Fix |
|---|------|-------|----------|---------------|

### Category 9 — DCT Formatting & Citations 📏

(same table format — flag citation format issues and formatting violations)

### Category 10 — Paragraph Standards 📐

(flag thin paragraphs, single-sentence paragraphs, missing structure)

---

## Summary

| Category | Count |
|----------|-------|
| 🤖 AI Phrases Found | X |
| ⚠️ Vague Claims | X |
| 👤 Person-View Violations | X |
| 🔬 Technical Issues | X |
| 📋 Chapter Relevance Issues | X |
| 📌 Title Drift Issues | X |
| 🚫 Banned Words | X |
| ✏️ Grammar & Mechanics | X |
| 📏 DCT Formatting & Citations | X |
| 📐 Paragraph Standards | X |
| **Total Issues** | **X** |

### By Severity

| Severity | Count |
|----------|-------|
| 🔴 Critical | X |
| 🟠 High | X |
| 🟡 Medium | X |
| 🟢 Low | X |

---

## Priority Fixes (Top 10)

| Priority | Finding # | Severity | Why It's Urgent |
|----------|-----------|----------|-----------------|
| 1 | XX | 🔴 CRIT | [Explanation] |
| 2 | XX | 🟠 HIGH | [Explanation] |
| ... | ... | ... | ... |

---

## Cleaned Version

[Full rewritten text with all fixes applied]
```

---

*Last Updated: February 2026 (V2 — expanded to 10 categories with severity framework)*
