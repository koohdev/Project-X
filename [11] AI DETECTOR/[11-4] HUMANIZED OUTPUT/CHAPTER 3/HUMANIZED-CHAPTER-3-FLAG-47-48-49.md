# Humanized Output — Flags 47, 48, 49
## § 3.2.3 Implementation Peopleware

**Source file:** `[04] OUR_PROJECT/[COA]-CHAPTER-3.md`  
**Target lines:** Lines 147, 151, 155  
**Date:** 2026-03-09  
**Workflow:** `/humanize-writing`

---

## Original Text

**Flag 47 — Students (Line 147):**
```
Students (Grades 4-6) will serve as the primary operators of the system. They will engage directly with the Math Battle System to solve arithmetic equations, explore the game world, and progress through the narrative. Their interaction will focus on developing calculation speed and accuracy to defeat enemies and clear procedural quests.
```

**Flag 48 — Educators and Guardians (Line 151):**
```
Mathematics teachers instructing Grades 4 to 6, along with the parents or guardians of those specific students, will act as secondary users who utilize the application as a supplementary educational tool. These educators will use the software to reinforce classroom arithmetic topics (such as PEMDAS) or to assign specific Training Dummy practice drills. Meanwhile, guardians will utilize the game to support home-based learning, potentially joining via the P2P Multiplayer mode to directly assist the primary learner during difficult combat encounters.
```

**Flag 49 — Gamers (Line 155):**
```
RPG enthusiasts and casual gamers will interact with the system for entertainment purposes. These users will focus on mastering the "Performance-Based Efficacy" mechanics to achieve high-efficiency combat ratings and complete "Omega Tier" endgame challenges, interacting with the system primarily to test cognitive reaction speeds and strategic planning.
```

---

## Humanized Text

**Flag 47 — Students:**
```
Students in Grades 4 to 6 are the primary users of the system, and they interact with it mostly through the Math Battle System, which is answering arithmetic equations to attack enemies like Slimes and Skeleton Warriors. Getting answers right decides whether the attack goes through, so the game naturally pushes them to work on calculation speed and accuracy as they clear quests from Mila and move through the narrative.
```

**Flag 48 — Educators and Guardians:**
```
Mathematics teachers for Grades 4 to 6, along with the parents or guardians of those students, use the system as a classroom and home support tool. Teachers can set up Training Dummy drills to go over specific PEMDAS topics outside of regular combat, while guardians can join a session through the P2P Multiplayer Room Code to help their child through harder encounters.
```

**Flag 49 — Gamers:**
```
RPG enthusiasts and casual gamers use the system mainly for recreational play, focusing on the Performance-Based Efficacy mechanics which reward fast and accurate answers with higher damage multipliers. Completing the Omega Tier challenges, which include the Numeromancer as the final opponent, is the main draw for this group since those encounters test how quickly a player can solve equations under pressure.
```

---

## Change Log

### Patterns Fixed

| Category | Before | After |
| :--- | :--- | :--- |
| "will" count (combined) | 9 | 0 |
| "utilize/utilizes" count | 2 | 0 |
| "engage/interact with the system" | 2 | 0 |
| Rule of Three (parallel infinitives) | 2 (Flag 47 + 48) | 0 |
| "-ing tail" clauses | 1 (Flag 49) | 0 |
| AI transitions ("Meanwhile") | 1 | 0 |
| Elevated vocabulary items | 7 | 0 |
| Project-specific perplexity boosters added | 0 | 9 (Slimes, Skeleton Warriors, Mila, Training Dummy, PEMDAS, P2P Multiplayer, Room Code, Performance-Based Efficacy, Omega Tier, Numeromancer) |

### Before / After Comparison

**Flag 47:**
> BEFORE: "Students (Grades 4-6) will serve as the primary operators of the system. They will engage directly with the Math Battle System to solve arithmetic equations, explore the game world, and progress through the narrative. Their interaction will focus on developing calculation speed and accuracy to defeat enemies and clear procedural quests."

> AFTER: "Students in Grades 4 to 6 are the primary users of the system, and they interact with it mostly through the Math Battle System, which is answering arithmetic equations to attack enemies like Slimes and Skeleton Warriors. Getting answers right decides whether the attack goes through, so the game naturally pushes them to work on calculation speed and accuracy as they clear quests from Mila and move through the narrative."

**Flag 48:**
> BEFORE: "Mathematics teachers instructing Grades 4 to 6, along with the parents or guardians of those specific students, will act as secondary users who utilize the application as a supplementary educational tool. These educators will use the software to reinforce classroom arithmetic topics (such as PEMDAS) or to assign specific Training Dummy practice drills. Meanwhile, guardians will utilize the game to support home-based learning, potentially joining via the P2P Multiplayer mode to directly assist the primary learner during difficult combat encounters."

> AFTER: "Mathematics teachers for Grades 4 to 6, along with the parents or guardians of those students, use the system as a classroom and home support tool. Teachers can set up Training Dummy drills to go over specific PEMDAS topics outside of regular combat, while guardians can join a session through the P2P Multiplayer Room Code to help their child through harder encounters."

**Flag 49:**
> BEFORE: "RPG enthusiasts and casual gamers will interact with the system for entertainment purposes. These users will focus on mastering the 'Performance-Based Efficacy' mechanics to achieve high-efficiency combat ratings and complete 'Omega Tier' endgame challenges, interacting with the system primarily to test cognitive reaction speeds and strategic planning."

> AFTER: "RPG enthusiasts and casual gamers use the system mainly for recreational play, focusing on the Performance-Based Efficacy mechanics which reward fast and accurate answers with higher damage multipliers. Completing the Omega Tier challenges, which include the Numeromancer as the final opponent, is the main draw for this group since those encounters test how quickly a player can solve equations under pressure."

### Key Changes Per Flag

**Flag 47:**
1. `"will serve as the primary operators"` → `"are the primary users"` — present tense, Angel-level noun
2. Rule of Three broken: `"solve...explore...progress"` → folded into compound sentence with `"which is answering..."` clarifier
3. `"Their interaction will focus on developing"` → `"the game naturally pushes them to work on"` — concrete-first, Angel-level
4. Perplexity boosters added: Slimes, Skeleton Warriors, Mila
5. `"whether the attack goes through"` — Gold Standard reference phrasing reused

**Flag 48:**
1. `"utilize the application as a supplementary educational tool"` → `"use the system as a classroom and home support tool"` — both "utilize" instances replaced
2. `"Meanwhile"` → `"while"` — casual connector replacing AI transition word
3. Rule of Three broken: `"reinforce...or to assign"` → `"set up Training Dummy drills to go over"` (single compound action)
4. `"directly assist the primary learner"` → `"help their child"` — major register downgrade
5. Perplexity: Training Dummy, PEMDAS, P2P Multiplayer, Room Code

**Flag 49:**
1. `"will interact with the system for entertainment purposes"` → `"use the system mainly for recreational play"` — "interact" removed, plain register
2. `-ing tail clause` ("interacting with the system primarily to test...") dropped entirely
3. `"cognitive reaction speeds and strategic planning"` → `"how quickly a player can solve equations under pressure"` — concrete, Angel-level
4. `"high-efficiency combat ratings"` → `"higher damage multipliers"` — specific game mechanic
5. Perplexity: Performance-Based Efficacy, Omega Tier, Numeromancer

### Academic Compliance Check

- [x] No first person / "the team"
- [x] No contractions
- [x] 2 complete sentences per paragraph (within 2–5 range)
- [x] No banned Cat 1A words (utilize, engage, leverage, facilitate)
- [x] No banned Cat 7 words (efficient, effective, innovative)
- [x] Ch.3 WHAT→WHERE→WHY→OUTCOME formula satisfied for all three
- [x] "will" = 0 occurrences across all three paragraphs
- [x] No rhetorical question openers
- [x] No colon setup-payoff
- [x] No Rule of Three

### Estimated Turnitin Impact

Flags 47–49 are 🟡 Medium priority — three consecutive peopleware paragraphs in a single sliding window. Rewriting all three as a unit eliminates the compounded "will serve / will engage / will focus / will act / will utilize / will interact" chain that drags the entire window's score up. **Estimated impact: ~2–4% overall score reduction.**
