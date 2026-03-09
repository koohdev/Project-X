# Post-Mortem: Where the AI Detection Analysis Went Wrong

**Date:** March 7, 2026  
**Compared:** `AI-DETECTION-ANALYSIS.md` (my predictions) vs `FLAGGED.md` (actual Turnitin results)

---

## Scorecard

| Metric | Value |
| :--- | :--- |
| Total predictions made | 19 flagged sections |
| Correctly predicted as flagged | **15 / 19** (79% accuracy) |
| Predicted as flagged but NOT flagged (false positives) | **3** |
| Actually flagged but NOT predicted (missed) | **~8 sections** |
| Biggest single error | Overestimating prose lists as the #1 contributor |

---

## The Biggest Mistake — Prose Lists Were NOT the Biggest Contributor

### What I Predicted

> 🔴 **Flag #1** — Prose Lists of Enemies, Loot, Weapons, Skills, Equipment (Lines 33–87)
> "These ~55 lines contain hundreds of sentences with identical grammatical structure... This is the **single biggest AI trigger** in the entire manuscript... approximately **12–15% of the total AI score**."

### What Actually Happened

**Most of those lists were NOT flagged.** Out of the massive block spanning lines 33–87:

| Section | Flagged? |
| :--- | :--- |
| Plains/Forest enemy loot (Line 33) | ❌ No |
| Desert enemy loot (Line 35) | ⚠️ Partially (Mummy through Pharaoh's Guard only) |
| Tundra enemy loot (Line 37) | ⚠️ First sentence only ("Ice Slime will drop Blue Gel") |
| Volcano enemy loot (Line 39) | ❌ No |
| Dungeon enemy loot (Line 41) | ❌ No |
| Items/Consumables (Line 43) | ❌ No |
| ALL Weapon descriptions (Lines 45–59) | ❌ **No — none flagged** |
| ALL Skill descriptions (Lines 61–75) | ❌ **No — none flagged** |
| ALL Status effects (Lines 77–79) | ❌ **No — none flagged** |
| ALL Equipment descriptions (Lines 81–87) | ❌ **No — none flagged** |

I called these *"the single biggest AI trigger in the entire manuscript"* and predicted **12–15% of the score**. In reality, they contributed almost **nothing**.

### Why I Was Wrong

**Turnitin's "qualifying text" filter.** According to Turnitin's own documentation:

> *"Our model only processes qualifying text in the form of long-form writing. Long-form writing means individual sentences contained in paragraphs that make up a longer piece of written work, such as an essay, a dissertation, or an article. Non-qualifying text, such as **bullet points, annotated bibliographies**, etc., **will not be processed** and can create disparity between the submission highlights and the percentage shown."*

The weapon/skill/equipment descriptions — while technically written as prose sentences — are **enumerative catalog content**. Turnitin's preprocessor likely classified them as list-like material rather than expository academic writing. The pattern `"The [X] will be a [Y]"` repeated 150+ times is so mechanically regular that it doesn't resemble the kind of AI-generated *essay prose* that Turnitin is trained to detect.

**Key insight:** Turnitin distinguishes between:
- **Expository/argumentative paragraphs** → Processed and scored
- **Enumerative/catalog-style prose** → Often skipped as non-qualifying

I treated all prose equally. Turnitin doesn't.

---

## Three False Positives — What I Flagged That Turnitin Didn't

### ❌ False Positive #1: Acknowledgement Page

**My Prediction:** 🟡 MEDIUM risk, ~1% contribution. *"Acknowledgements are one of the MOST commonly AI-generated sections."*

**Actual Result:** Not flagged at all.

**Why I was wrong:** The Acknowledgement is only ~260 words — likely below the threshold where Turnitin's AI model can make a confident determination. Also, it contains **project-specific names** (Mr. Jan Nicole B. Apostol, Mr. Rossano C. Samson, Dominican College of Tarlac) that make it harder to classify as generic AI output. More importantly, it's **genuine emotional writing** — even if the phrasing sounds formulaic, real gratitude paragraphs often genuinely sound like that.

### ❌ False Positive #2: Ch.4 Risk Assessment (Lines 219–221)

**My Prediction:** 🟡 MEDIUM risk. *"Has that 'AI summary' feel."*

**Actual Result:** Not flagged.

**Why I was wrong:** Despite being a bit run-on, the Risk Assessment contains highly **project-specific** details — naming specific technologies (PeerJS, NW.js), a specific person (Mr. Jan Nicole B. Apostol), and specific mitigation strategies. This specificity creates **higher perplexity** (unpredictability), which actually makes it look MORE human to Turnitin's detector.

### ❌ False Positive #3: Ch.4 UI Design Description (Lines 227–233)

**My Prediction:** 🟡 MEDIUM risk. *"Polished, formulaic description of color choices."*

**Actual Result:** Not flagged.

**Why I was wrong:** The section contains **hex color codes** (#005385, #000000, #FFFFFF) and a **specific font name** (M+ 1m regular). These are concrete, technical details that AI wouldn't generate in exactly this way. The precision and specificity of the content signals human authorship to the detector.

---

## Eight Missed Flags — What Turnitin Caught That I Didn't Predict

### ⚠️ Missed #1: ALL 6 Limitations (Lines 1086–1104)

I didn't specifically call out ANY of the Limitations as flagged. Turnitin flagged **every single one**:
- A. Mathematical Scope and Generation Limits
- B. Tactile Input Disparity
- C. Input Method
- D. Asset Fidelity
- E. Peer-to-Peer Latency Sensitivity
- F. Volatile Session Architecture

**Why I missed them:** I focused my analysis on the longer, denser paragraphs and assumed that shorter Limitation entries (some are only 1–2 sentences) would fly under the radar. But they all follow the same formulaic pattern: *"The [feature] [verb] [technical description]. This [consequence]."* — and Turnitin's ~250-word sliding window groups them together into one uniform block.

### ⚠️ Missed #2: Story/Narrative Opening (Lines 23–25)

The story paragraphs about the protagonist, the four biomes, and The Numeromancer were flagged. I overlooked them because I was focused on the more "academic-sounding" sections. But the narrative prose still uses the same predictable `"will [verb]"` future-tense structure that runs through the entire chapter.

### ⚠️ Missed #3: Chapter 3 Implementation Scope (6 additional sections)

I predicted Chapter 3's **software descriptions** (3.1.2) would be flagged, which was correct. But I underestimated how far the flagging extended into the **implementation** subsections:
- 3.1.4 Network testing (WAN simulation)
- 3.2.1 Hardware requirement intros (PC and Mobile)
- 3.2.2 OS requirements, Browser requirements
- 3.2.3 Peopleware (Students, Educators, Gamers)
- 3.2.4 Network (Internet speed requirements)

These sections use the same formulaic template as the software descriptions. I should have treated all of Chapter 3 as one continuous block of uniform writing rather than isolating just the software descriptions.

---

## Root Cause Analysis

| Error | Root Cause |
| :--- | :--- |
| Overvalued prose lists | Did not account for Turnitin's "qualifying text" preprocessor that filters out enumerative/catalog-style content |
| False positive on Acknowledgement | Assumed formulaic phrasing = AI-like, but ignored word count threshold and project-specific names |
| False positive on Risk Assessment | Underestimated how project-specific details increase perplexity (making text look human) |
| False positive on UI Design | Underestimated how concrete technical details (hex codes, font names) signal human authorship |
| Missed all 6 Limitations | Focused on paragraph length rather than pattern uniformity across grouped short sections |
| Missed story paragraphs | Assumed narrative content wouldn't trigger detection; overlooked the persistent "will" pattern |
| Underestimated Ch.3 scope | Treated Ch.3 as two separate issues instead of one continuous block of templated writing |

---

## Revised Understanding: What ACTUALLY Drives the 33%

Based on the real Turnitin flags, here is the corrected breakdown:

| Actual Contributor | Approx. % of Score | Why Flagged |
| :--- | :--- | :--- |
| **Ch.1 Scope sections (A–J)** | ~8–10% | "This module will... The user will..." repeated for every module |
| **Ch.1 § 1.1 Project Context** (all expository prose) | ~6–8% | Dense "will" pattern, smooth theoretical transitions |
| **Ch.3 ALL technical descriptions** (3.1 + 3.2) | ~5–7% | "[Tool] is a [definition]. It will be used..." template across entire chapter |
| **Ch.2 Theories + Related Projects** | ~3–4% | Define → explain → apply formula, rigid comparison template |
| **Ch.4 Methodology + Feasibility** | ~2–3% | "The proponents will..." + smooth technical prose |
| **Ch.1 Limitations** | ~1–2% | Short but uniformly formulaic entries grouped together |
| **Ch.1 Partial enemy loot** | <1% | Only fragments of Desert/Tundra sections qualified as prose |
| **TOTAL** | **~26–35%** | Consistent with **33%** |

### The Real #1 Contributor

The actual biggest driver isn't the game catalogs — it's the **Scope/Objective descriptions** in Chapter 1 combined with the **software/implementation descriptions** in Chapter 3. Both use the same three-part template (`[X] is... It will... The user/proponents will...`) repeated across 20+ consecutive occurrences of expository prose. This is exactly what Turnitin is designed to catch: **formulaic academic writing that mimics LLM output patterns.**

---

## Lessons Learned

1. **Turnitin only scores prose** — enumerative content (lists, catalogs, tables) is excluded from AI scoring, even when written as sentences
2. **Specificity protects you** — sections with project-specific names, hex codes, and concrete technical details were NOT flagged despite being formulaic
3. **Short sections still get caught** — Turnitin's sliding window groups adjacent short paragraphs, so even 1–2 sentence limitations get scored when they're next to each other
4. **The "will" pattern is toxic** — the single most pervasive signal across all flagged content is the relentless use of future-tense "will" constructions, which creates very low perplexity
5. **Turnitin treats academic boilerplate ≈ AI** — sections that follow standard thesis templates (define tool → state purpose → explain proponent usage) look statistically identical to what an LLM would generate
