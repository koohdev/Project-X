# 🔍 ACADEMIC WRITING CHECKER — Reference Guide

> **Purpose:** Detect and replace problematic wording in Capstone Chapters 1–4  
> **How to Use:** Invoke via the `/check-writing` workflow, or mention this file when pasting chapter text  
> **Companion:** Works alongside `KNOWLEDGE_BASE.md` PART 4 (Tone Sanitation / Banned Words)

---

## HOW THIS CHECKER WORKS

When you paste your chapter text and invoke this checker, the AI will:

1. **Scan** the text against every category below
2. **Flag** each problematic phrase with its category tag (e.g., `[AI-PHRASE]`, `[VAGUE]`)
3. **Suggest** a concrete replacement that fits the sentence context
4. **Output** a summary table of all findings at the end

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

### 1C. Structural Patterns That Signal AI

| Pattern | What to Look For | Fix |
|---|---|---|
| **Over-smooth transitions** | Every paragraph starts with "Moreover," "Furthermore," "Additionally" | Vary transitions; some paragraphs need no transition word |
| **Formulaic conclusions** | "In conclusion, it is evident that..." | Tie back to objectives specifically |
| **Excessive em-dashes** | Sentences broken by — em-dashes — mid-thought | Use commas or restructure the sentence |
| **Uniform sentence length** | All sentences are 15–20 words with no variation | Mix short (8–12 words) and medium (15–22 words) sentences |
| **Tautology / redundancy** | "collaborate together," "completely eliminate," "future plans" | Remove the redundant word |
| **Bullet-point-like paragraphs** | Short, choppy paragraphs that read like a bulleted list | Merge related points into flowing paragraphs |
| **Symmetrical lists** | Exactly 3 or 5 points with identical sentence structure | Vary count and structure naturally |

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

Content must be relevant to the specific chapter. This checks for misplaced content.

### 5A. Chapter 1 — Introduction

| ✅ Belongs | ❌ Does NOT Belong |
|---|---|
| Problem description (global → local) | Detailed code explanations |
| Project justification | Hardware/software specifications |
| General system overview | Database schema details |
| Objectives (SMART format) | Test results |
| Scope and limitations | Development methodology phases |

### 5B. Chapter 2 — Review of Related Literature/Systems

| ✅ Belongs | ❌ Does NOT Belong |
|---|---|
| Anchor theory + supporting theories | Your own system's features |
| Related projects/systems overview | Your methodology |
| Comparative matrix | Your test results |
| Screenshots of related systems | Your implementation details |
| Citations and references | Unrelated theories with no tie to your project |

### 5C. Chapter 3 — Technical Background

| ✅ Belongs | ❌ Does NOT Belong |
|---|---|
| Hardware requirements | Problem statement (belongs in Ch. 1) |
| Software tools and technologies | Related literature (belongs in Ch. 2) |
| Peopleware | Methodology steps (belongs in Ch. 4) |
| Network architecture | Test results (belongs in Ch. 4) |
| How technologies will be used | Business justification (belongs in Ch. 1) |

### 5D. Chapter 4 — Methodology, Results and Discussion

| ✅ Belongs | ❌ Does NOT Belong |
|---|---|
| SDLC methodology and phases | Background of the problem (Ch. 1) |
| Feasibility studies | Theory discussion (Ch. 2) |
| Requirements modeling (DFD, Use Case) | General technology overview (Ch. 3) |
| System design and architecture | Extended literature review |
| Test plans and results | Recommendations (belongs in Ch. 5) |
| Implementation details | |

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

---

## OUTPUT FORMAT

When this checker is invoked, results should be formatted as:

```
## 🔍 Writing Check Results for [Chapter X.X — Section Name]

### Findings

| # | Line / Phrase | Category | Issue | Suggested Fix |
|---|---|---|---|---|
| 1 | "delve into the intricacies" | AI-PHRASE | AI cliché | "examine the details of" |
| 2 | "many users" | VAGUE | No quantifier | "Based on [CITE], X% of users" |
| 3 | "We implemented..." | PERSON | First person | "The proponents implemented..." |
| ... | ... | ... | ... | ... |

### Summary
- 🤖 AI Phrases Found: X
- ⚠️ Vague Claims: X
- 👤 Person-View Violations: X
- 🔬 Technical Issues: X
- 📋 Chapter Relevance Issues: X
- 📌 Title Drift Issues: X
- 🚫 Banned Words: X

### Cleaned Version
[Full rewritten text with all fixes applied]
```

---

*Last Updated: February 2026*
