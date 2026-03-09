# Compiled Humanized Revisions — All Chapters

**Total Revised Flags:** 41 (out of 55)  
**Date Compiled:** 2026-03-09  
**Source:** `REVISION-TRACKER.md` + `[11-4] HUMANIZED OUTPUT/`

> [!NOTE]
> This file compiles every revised flag in chapter order. Each entry shows the **original flagged text** (where available) and the **humanized replacement**. Revision notes are pulled from the REVISION-TRACKER.

---

## Chapter 1 — Introduction

### Flags 1–4 — § 1.1 Project Context (Opening Paragraphs)

**Revised:** 2026-03-09  
**Scope:** Lines 5–17 — RPG intro through Mathematics Anxiety paragraph (7 → 6 paragraphs)  
**Summary:** Eliminated 16× "will" (→ 0); merged Lines 7+9 into one paragraph; broke Rule of Three (First/Second/Third → flowing prose); 12 elevated vocab downgrades; 16 perplexity boosters added; 11 Angel-voice markers; citations [1–4] preserved.

**Humanized Text:**

The proposed project is a 2D turn-based Role-Playing Game (RPG) where the combat system runs on math instead of random chance. In a standard RPG, whether an attack hits or misses is decided by a probability roll, but in *Chronicles of Arithmos*, the player has to type the correct answer to a math equation before the attack goes through. The equations start with basic addition and subtraction for low-level enemies like a Slime, and scale up to three-part PEMDAS problems by Level 70.

This approach turns repetitive math drills into the main combat mechanic, so the player practices calculation speed and accuracy while they play. The system gives direct rewards for getting an answer right — the player levels up, collects Gold, and defeats bosses by solving equations correctly. Because every fight in the game, from a Level 1 Slime in the Plains of Origin to the Numeromancer in the Void Dimension, depends on answering a math problem, the practice happens as a natural part of the gameplay and not as a separate exercise.

The game is named *Chronicles of Arithmos*, and the proponents are building it in RPG Maker MZ, which is a 2D game development engine made for turn-based RPGs. It runs as a standalone .exe application on Windows computers, and players can also open it through a web browser on desktops or mobile devices. On touchscreens, the game shows a Virtual Numeric Keypad on-screen so the player can tap their answers instead of using a physical keyboard.

Educational games often fail because of the "Chocolate-Covered Broccoli" effect, where a developer takes a standard math drill and puts game graphics on top of it [1]. The gameplay and the learning are separate, so students figure out that they are just doing a disguised worksheet and stop playing. Static difficulty makes this worse too, because a game that does not adjust its challenge level loses students on both sides — those who find the problems too easy get bored, and those who find them too hard give up [2].

Games with limited replay value give students less reason to come back too. *Chronicles of Arithmos* deals with these problems by tying the math directly to combat, not as a separate mini-game on the side — the player's answer to a math equation is what decides whether an attack lands a 2.0x Critical Hit or misses entirely. The Level-Based Difficulty System also scales the equations to match the player's current character level, and an Automatic Quest Generation system builds new side quests from enemies and items the player has already unlocked, so there is always something new to do without the proponents having to write each quest by hand.

The primary purpose of this project is to reduce Mathematics Anxiety among Grade 4–6 students. Richardson and Suinn (1972) described it as a feeling of tension that gets in the way of working with numbers [3], and Ashcraft (2002) found that this kind of anxiety takes up working memory — the student's brain is too busy processing fear to actually solve the problem [4]. *Chronicles of Arithmos* reframes the math task as RPG combat, so instead of staring at a worksheet, the student is fighting a Skeleton Warrior in the Desert and has to answer 12 × 4 before the timer runs out.

---

### Flags 5–11 — § 1.1 Project Context (Gamification, Story, tables)

**Revised:** 2026-03-09  
**Scope:** Lines 19–37 — Gamification, Auto-Scaling, Story, Party/NPC tables, and Loot tables  
**Summary:** Eliminated 92+ "will" instances (→ 0) and 18+ identical Rule of Three/Many violations; converted three massive repetitive prose lists into 5 readable Markdown tables (Party, NPCs, Plains Loot, Desert Loot, Tundra Loot); downgraded 11 elevated vocabulary items; added 14 perplexity boosters; injected 9 Angel-voice markers; preserved citation [5].

**Humanized Text:**

Placing the math inside a low-stakes fantasy setting is what makes the practice feel different from a classroom drill. When the player gets the right answer fast enough, the game displays a Critical Hit and deals 2.0x damage, and that direct visual payoff is what Gee (2003) linked to building learner confidence with numbers [5]. The worst consequence for a wrong answer is a Game Over screen rather than a failing grade, so there is no lasting mark for making a mistake. Every town in the game also has a Training Hall where the player can fight a Training Dummy with infinite health to practice calculation speed at any time, and tapping the Escape command exits the session whenever they are done.

The game also has an Enemy Auto-Scaling System, so enemies automatically adjust their stats to match the party's average level regardless of which area the player is in. It also includes a Peer-to-Peer (P2P) Multiplayer mode where two players connect through Portal Keeper Alden using a Room Code and fight enemies together as a combined party.

The story starts in the Plains of Origin, where the protagonist wakes up to a world overrun by Anomalies — chaos fractures that appeared when the world's underlying laws collapsed. Bron, who teaches physical combat, and Martha, who covers magical theory, guide the player through the opening tutorial, and the player learns that their younger sister Lily has been cursed. The only way to lift the curse is to travel across the world and restore its broken logic.

That journey takes the protagonist through four biomes, each one guarded by a corrupted elemental force — the Forest Golem in the Forest, the Pharaoh's Guard in the Desert, Fenrir in the Tundra, and the Demon Lord in the Volcano. Recovering a fragment from each one leads to the Void Dimension, where the final antagonist The Numeromancer is the source of everything that has gone wrong. Beating the Numeromancer requires both combat ability and math accuracy, and that final confrontation is the game's last test of everything the player has practiced.

The player builds a party of eight recruitable companions over the course of the story, each one belonging to a different combat class.

| Companion | Class |
| :--- | :--- |
| Kael | Knight |
| Elara | Sorceress |
| Garrick | Tank |
| Sylas | Rogue |
| Isolde | Healer |
| Thorne | Ranger |
| Lyra | Magic Swordsman |
| Fenrin | Monk |

The narrative and mechanics are supported by a cast of named side characters, each assigned a specific gameplay function, as well as a larger group of generic background NPCs that populate the towns.

| NPC | Role |
| :--- | :--- |
| Elder Tobias | Issues the initial story quests |
| Merchant Oryn | Sells general goods |
| Receptionist Mila | Procedural quest hub — issues, accepts, or discards generated quests |
| Bard Jareth | Provides healing interactions |
| Captain Valerius | Gives the player directions to the next location |
| Professor Haze | Unlocks advanced skills |
| Innkeeper Gorm | Runs rest establishments that restore HP and MP |
| Blacksmith Rurik | Provides equipment upgrades |
| Widow Claire | Issues a specific side quest |
| Alchemist Vanya | Sells potions |
| Librarian Estel | Explains the game's lore and backstory |
| Guard Captain Aris | Patrols the towns |
| Street Urchin Pip | Hints at hidden items |
| Priestess Anara | Removes negative status effects |
| Hunter Kaelen | Scouts and provides map information |
| Portal Keeper Alden | Hosts or joins P2P Multiplayer rooms via Room Code |

The towns also include named background characters like Farmer Ben, Nobleman Caelus, and Fisherman Old Tom for flavor dialogue, alongside a population of non-mechanical NPCs — Townsmen, Townswomen, Playing Children, Market Shoppers, Tavern Patrons, Castle Guards, Farmhands, Stable Boys, Washerwomen, Street Sweepers, Beggars, Strolling Couples, Academy Students, Visiting Merchants, Nobles, Tourists, Drunkards, Gossiping Ladies, Messengers, Guards, Fishers, Old Ladies, Street Performers, and Crowd Members.

The game has a full set of original background music tracks that change depending on where the player is and what they are doing. Town areas use slow, peaceful melodies, battle encounters switch to an intense combat anthem, and dungeon interiors have their own darker, atmospheric themes to keep the audio matched to the moment.

The game world is organized into four distinct biomes, each with its own enemy roster and loot table.

#### Plains and Forest Biome
The Plains and Forests are the opening starter zones, and the enemies found here focus on basic early-game loot.

| Enemy | Loot Drop |
| :--- | :--- |
| Slime | Green Gel |
| Rat | Rat Tail |
| Bat | Bat Wing |
| Spider | Sticky Web |
| Hornet | Insect Wing |
| Wolf | Wolf Pelt |
| Bear | Bear Claw |
| Treant | Living Branch |
| Goblin / Goblin Archer | Goblin Cloth |
| Goblin Shaman | Shaman Beads |
| Orc | Orc Tusk |
| Bandit / Bandit Leader | Stolen Coin Purse |
| Crow | Shiny Feather |
| Snake | Snake Skin |
| Fairy | Fairy Dust |
| Mandrake | Mandrake Root |
| Wild Boar | Boar Meat |
| Forest Golem | Ancient Bark |

#### Desert Biome
The Desert is a harsher mid-game zone with enemies that drop sand and bone-themed loot.

| Enemy | Loot Drop |
| :--- | :--- |
| Sand Slime | Yellow Gel |
| Scorpion / Giant Scorpion | Scorpion Stingers |
| Cactus | Cactus Flower |
| Sand Worm / Ant Lion / Dust Spirit | Sand Essence |
| Mummy | Old Bandage |
| Skeleton Warrior | Bone Fragment |
| Skeleton Mage | Skull |
| Desert Wolf | Dry Fur |
| Lamia | Snake Scale |
| Basilisk | Petrified Eye |
| Gargoyle | Stone Wing |
| Sand Golem | Sandstone Block |
| Vulture | Vulture Beak |
| Sphinx | Riddle Tablet |
| Ancient Scarab | Scarab Shell |
| Desert Rogue / Pharaoh's Guard | Golden Fragments |

#### Tundra and Frost Biome
The Tundra and Frost region introduces ice-element enemies and cold-themed loot as a late-game area.

| Enemy | Loot Drop |
| :--- | :--- |
| Ice Slime | Blue Gel |
| Snow Wolf | Wolf Fang |
| Polar Bear | Thick Hide |
| Ice Bat / White Tiger | White Fur |
| Snow Spirit / Winter Wisp | Cold Wisps |
| Yeti | Yeti Horn |
| Ice Golem | Permafrost Shard |
| Crystal Spider | Crystal Leg |
| Frost Giant / Frozen Knight | Frost Metal |
| Corrupted Penguin | Corrupted Feather |
| Ice Drake | Drake Scale |
| Wendigo / Frost Mage | Frozen Hearts |
| Glacial Turtle | Ice Turtle Shell |
| Snow Harpy | Harpy Feather |
| Ice Elemental | Ice Crystal |
| Fenrir | Snowflake Core |

---

### Flag 12 — § 1.2.2 Specific Objectives (D–K)

**Revised:** 2026-03-08  
**Scope:** Full rewrite of Objectives D through K (8 specific objectives)  
**Summary:** Eliminated 24× "will", 8× "engage/interact/utilize this module by" closing formulas, 8× identical "This module will..." openers; each objective given unique opener (Question/Result/Example/NPC/Action/Data/Timeline/Device per Strategy 7); added 14 game-specific perplexity boosters; injected 9 Angel-level phrasings.

> [!IMPORTANT]
> Objectives A, B, C, and L were **not flagged** or not yet revised — they retain the original "This module will..." format.

**Humanized Text:**

#### D. To engineer a "Content-Aware" Timer System

How long should a player get to solve something like 15 × 7? The timer figures this out on its own based on the equation's complexity, the total digit count, and what math operators are in the problem. During combat, the player sees a countdown bar on screen and types their answer on a keyboard or touchscreen before it runs out.

#### E. To integrate an Enemy Auto-Scaling System

A Level 10 Slime in the Plains of Origin and a Level 50 Slime in the Volcano hit with different force because enemy stats scale to match the party's average level. The system adjusts Health Points, Attack power, EXP, and Gold on its own, so the proponents do not need to manually create separate copies of every enemy for each area. The player runs into these scaled enemies either by walking into enemy sprites on the map or through random encounters.

#### F. To create a Performance-Based Reward Mechanism

A correct answer typed in 2.1 seconds deals 2.0x damage, which the game calls a Critical Hit. A slow but correct answer only deals normal damage, while a wrong-but-fast answer goes through at 0.5x and a wrong-and-slow answer misses entirely. The player sees direct visual and sound feedback right after submitting, so they know immediately how their speed and accuracy affected the combat result.

#### G. To develop an Automatic Quest Generation system

Receptionist Mila keeps a rotating board of tasks that the player can accept or turn down. The quest engine behind this checks every area the player has unlocked and uses the enemies and items in those locations to build hunting and gathering quests on its own. If the player accepts a quest, it shows up in the Quests tab, and if they reject it, the system throws it out and makes a new one the next time the player talks to Mila.

#### H. To implement a Peer-to-Peer (P2P) Multiplayer Connection

The player talks to Portal Keeper Alden and clicks "Host Room" to get a unique Room Code that they can share. Whoever wants to join types that code after clicking "Join Room" from the same NPC, and the two parties merge for co-op combat, so both players fight the same enemies together. No online accounts are needed since the connection goes directly between the two devices through PeerJS.

#### I. To integrate a Save System

Twenty save slots and one autosave checkpoint store the player's progress as local files on their device. The autosave overwrites itself every time the player moves to a new map, and the manual slots let the player pick exactly where to record their data. If a slot already has a save file in it, the system overwrites the old one with the current progress.

#### J. To engineer a Level-Based Progression System

At Level 1, the player adds and subtracts single-digit numbers, and by Level 30 the equations start using multiplication and division. Once a character reaches Level 70, the system generates full PEMDAS equations with three or more parts. The player earns EXP and Gold from combat and quests, and as they level up the game unlocks new story events, harder math operators, and new areas to explore.

#### K. To implement a Mobile Input System

On a touch-screen device, there is no physical numpad, so the system detects the device type and shows a Virtual Numeric Keypad on screen during combat. The keypad appears right next to the math input window whenever an equation pops up, and the player taps the number buttons to type their answer and hits "Submit" to send it. This works on any supported mobile device, assuming the browser runs modern web standards too.

---

### Flags 13–23 — § 1.3.1 Scope (A–J)

**Revised:** 2026-03-09  
**Scope:** Full rewrite of Scope constraints A through J.  
**Summary:** Eliminated all 28+ "will" instances and AI template openers ("This module will feature", "The user will interact"); removed excessive Rule of Three parallelisms; completely rewrote the formal turn structure pattern; added Angel-voice connectors ("a nice afterthought", "means that", "so"); injected 16+ project-specific perplexity boosters (Chronicles of Arithmos, Slime, Goblin, Kael, Plains of Origin, Desert, Forest, Volcano, Numeromancer, Receptionist Mila, Portal Keeper Alden, Blacksmith Rurik, Merchant Oryn).

**Humanized Text:**

Chronicles of Arithmos uses a visible "Action Gauge" for each character and enemy that fills up based on their Speed or Agility stat. The game automatically freezes these action gauges the exact moment the math input window appears on the screen, which is a wait-based system. This complete pause of the battle timers means that an enemy like a Slime or a Goblin cannot take their turns or attack while the player calculates and types their answer.

The player knows it is Kael's turn when his visual Action Gauge completely fills up, and they can use a computer mouse or trackpad to click through the combat menus. They choose from options like "Attack," "Skills," or "Items" to manage the party's health and mana. Combat follows a specific flow where the player selects an action first, and then the system checks their math answer before the game executes the chosen move.

The game automatically scales the complexity of the math equations based on the character's current level, so the problems get harder with more terms and different operators as Kael and his party level up. This system also handles the math generation for the safe-practice Training Halls found in every town. The player can practice calculating answers by fighting a Training Dummy, which is a living target with infinite health. They can fight a fixed-level dummy to practice a specific math tier, or even a dynamic dummy that matches the party's average level. Since the dummy cannot die, the player just clicks "Escape" to manually stop the training session.

In these early stages (Levels 1-29), the game generates equations using only Addition and Subtraction with two numbers. A basic encounter with a Slime in the Plains of Origin might ask the player to solve 15 + 7 to hit it. As the party gets stronger (Levels 30-69), the game introduces Multiplication and Division operations. For the late game (Levels 70-100), the system creates three-part equations that use the full PEMDAS rule set. A boss fight against the Numeromancer might require the player to solve (10 + 5) * 2 to survive his attacks.

The game uses a dynamic timer that calculates the exact answer window based on how complex the equation is, the total digit length, and the specific math operators used. It gives extra time bonuses for harder operations or for equations with larger numbers, so a multiplication problem gives more time than basic addition. If the countdown bar actually hits zero during combat, the math input window stays open on the screen because the player still has to submit an answer to proceed. The system just records that late answer as "slow" and reduces the damage output, rewarding players who type fast on their keyboard or touchscreen.

This game constantly runs a background process that adjusts enemy stats like Health Points, Attack power, and Gold rewards in real-time based on the party's average level. The player starts these battles either by walking their character directly into visible enemy sprites, or by triggering a random encounter while exploring areas like the Plains of Origin. Once a fight starts, the player faces enemies that automatically match their health and attack values to provide a fair challenge for the current party.

Chronicles of Arithmos includes a combat calculation step where the game directly determines the outcome of an action based on how fast and accurately the player answers the math problem. Fast and correct answers apply a 2.0x critical multiplier to the action. Slow but correct answers execute the action at its normal base value. Fast but incorrect answers apply a half-damage penalty (0.5x) to the action. Slow and incorrect answers make the action fail completely.

The game features an internal quest engine that automatically scans the enemies and items found in the exact areas the player has already unlocked, like the Tundra or Volcano biomes. It uses this data to generate relevant hunting and gathering tasks, which do not have a time limit, so the player can finish them whenever they want. If the player accepts a quest from Receptionist Mila in the town hall, the game records it in the Quests tab for tracking. If the player rejects the quest, Mila simply discards it and generates a completely new objective the next time the player talks to her.

The game features a cooperative multiplayer mode that connects players directly using text-based Room Codes. This allows for drop-in combat where a joining player's characters simply merge with the host's party on the fly. The player talks to Portal Keeper Alden in any major town and clicks the "Host Room" button to generate a specific code, or types in a friend's code after clicking the "Join Room" button to enter their world.

The game records player progress by storing local save files directly on the computer or mobile device. The system comes with 20 manual save slots alongside a dedicated Autosave function. When a player selects a save slot that already has data, the game just completely overwrites the old file with their current progress. The Autosave function also overwrites its own specific slot every time the player crosses a map exit to reach a new checkpoint. To save manually, the player opens the "Save" screen from the main menu and clicks a slot, while the automatic checkpoints trigger naturally as they explore the world.

The game stages the player's progression by giving specific rewards after successful combat and exploration. The player earns these rewards by winning fights or finishing side quests, which keeps the gameplay loop moving forward. Accumulating EXP increases Kael's level over time. The minimum obtainable EXP from a single low-level source is 10 points from a Level 1 Slime, while the maximum possible gain from an endgame boss is capped at 99,999 points. The player gets gold by defeating enemies and completing quests, which the player uses to buy new equipment from Blacksmith Rurik or Merchant Oryn. Moving the story forward updates the "Story Progress" value, which is what the game uses to officially unlock higher-level maps like the Desert or Tundra.

---

### Flag 24 — § 1.3.2 Limitation A: Mathematical Scope

**Revised:** 2026-03-09  
**Summary:** Dropped "Furthermore" AI transition; merged 4→3 sentences; "strictly restricted" → "only produces"; "This specific numerical limitation applies universally" → "This cap applies"; added Level 70 + PEMDAS.

**Original:**
> The system does not currently support advanced algebra, calculus, or non-integer results (fractions/decimals). To maintain combat flow, the math generator is strictly restricted so that all division problems calculate to exact whole numbers, avoiding fractions or decimals entirely. Furthermore, the system imposes a hard limit on the multiplier and the divisor (the second number in any multiplication or division problem), capping them at a range of 1 to 20. This specific numerical limitation applies universally to every combat encounter, including multi-part equations at higher levels.

**Humanized:**
> The math generator only produces whole number arithmetic, so there are no fractions, decimals, algebra, or calculus problems in the game. Division equations always come out to exact whole numbers, and the second number in any multiplication or division problem stays between 1 and 20. This cap applies to every combat encounter, including the three-part PEMDAS equations at Level 70 and above.

---

### Flag 25 — § 1.3.2 Limitation B: Tactile Input Disparity

**Revised:** 2026-03-09  
**Summary:** Dropped "Consequently"; "enables mobile playability" → "lets the game run on touchscreens"; "reduced input velocity" → "slow the player down"; added Math Timer.

**Original:**
> While the inclusion of a Virtual Numeric Keypad enables mobile playability, the lack of tactile feedback on touchscreens may result in reduced input velocity compared to physical keyboards. Consequently, users on mobile devices may experience a slight disadvantage in high-level "Speed Math" calculations where millisecond reaction times are critical.

**Humanized:**
> The Virtual Numeric Keypad lets the game run on touchscreens, but tapping a flat screen does not feel the same as pressing physical keys, and that difference in feedback can slow the player down. This matters most during higher-level encounters where the Math Timer gives only a few seconds to type an answer.

---

### Flag 26 — § 1.3.2 Limitation C: Input Method

**Revised:** 2026-03-09  
**Summary:** "utilizes" → "types answers using"; dropped "This limitation means that"; 3→2 sentences.

**Original:**
> The input system utilizes the standard number row or numpad of a physical keyboard. On mobile and touch-screen devices, the system provides a Virtual Numeric Keypad as the primary input method. This limitation means that input speed may vary depending on the device used.

**Humanized:**
> On a PC, the player types answers using the keyboard's number row or numpad, and on mobile the Virtual Numeric Keypad replaces that. Because the two input methods feel different, answer speed can change depending on which device the player uses.

---

### Flag 27 — § 1.3.2 Limitation D: Asset Fidelity

**Revised:** 2026-03-09  
**Summary:** "utilizes" → "uses"; "The project" → "The game"; added RPG Maker MZ.

**Original:**
> The project utilizes standard 2D pixel art assets and does not focus on high-fidelity 3D rendering or physics simulations.

**Humanized:**
> The game uses 2D pixel art built in RPG Maker MZ and does not include 3D models, physics simulations, or high-fidelity rendering.

---

### Flag 28 — § 1.3.2 Limitation E: P2P Latency Sensitivity

**Revised:** 2026-03-09  
**Summary:** "utilizes" removed; 2→1 compound with "so"; added PeerJS.

**Original:**
> The multiplayer feature relies on the stability of the host's internet connection. As the system utilizes a direct P2P handshake, high latency or packet loss on the host side may result in desynchronization of the Math Timer for connected clients.

**Humanized:**
> The P2P multiplayer runs through PeerJS on the host's internet connection, so if the host has high latency or drops packets, the Math Timer on the guest's screen can fall out of sync with the host's.

---

### Flag 29 — § 1.3.2 Limitation F: Volatile Session + NEW Limitation G

**Revised:** 2026-03-09  
**Summary:** "is stateless" explained plainly; "state recovery not supported" → "cannot reconnect to the same Room Code"; added NEW Limitation G (Local-Only Save Data).

**Original (F):**
> The multiplayer system is stateless (no central dedicated server). If the host application is terminated, the game session dissolves immediately for all connected clients; state recovery for guest clients is not supported in this version.

**Humanized (F):**
> The multiplayer system has no central server and does not store session data. If the host closes the game or loses connection, the session ends for all connected players immediately, and the guest cannot reconnect to the same Room Code.

**NEW Limitation G: Local-Only Save Data:**
> The save system writes all progress to local files on the player's device because the system does not have a user authentication module or a centralized database. There is no account creation, login, or cloud sync, so a player that starts on one PC cannot continue on a different device or on a phone without manually copying the save file over.

---

## Chapter 2 — Review of Related Literature / Systems

### Flag 30 — § 2.1.1 Game-Based Learning

**Revised:** 2026-03-08  
**Summary:** Full section rewrite using PERSONALITY.md voice.

**Humanized Text:**

Game-Based Learning, or GBL, is a teaching method where academic content is taught through game mechanics like points, levels, and rewards instead of traditional classroom instruction [6]. The student does not sit through a lecture or fill out a drill sheet to learn the material, because the game itself is the lesson. Prensky (2001) studied this and found that elementary students who learned through games scored higher on tests and were more motivated to keep going [6].

The proponents chose GBL as the anchor theory for *Chronicles of Arithmos* because the whole game depends on it. The player cannot attack an enemy or cast a spell without first solving a math equation, and a wrong answer weakens the action. Every fight in the game, from a Slime in the Plains of Origin to the Numeromancer in the Void Dimension, is really just an arithmetic exercise wrapped in combat.

Three more theories build on GBL and each one covers a specific part of the system that GBL alone does not address. Mathematics Anxiety is relevant because Grades 4–6 students often develop negative feelings toward math, and the game format is supposed to reduce that pressure. Flow Theory deals with difficulty, since a player that keeps answering the same level of math problems will either get bored and stop playing or get overwhelmed and quit. Narrative-Centered Learning suggests that students may remember the math content better when it is tied to a story that they actually follow and care about.

---

### Flag 31 — § 2.1.2 Mathematics Anxiety in Primary Education

**Revised:** 2026-03-08  
**Summary:** Replaced "but it does not explain" bridge with rhetorical question; added Ashcraft (2002) year citation; inserted project-specific enemy names (Slime, Skeleton Warrior); varied sentence lengths (12→17→24→13 / 13→30→21).

**Humanized Text:**

What makes a game-based approach necessary for this age group? Ashcraft (2002) described mathematics anxiety as a feeling of tension or fear that interferes with math performance [7]. Among students in Grades 4–6, this tension occupies working memory and creates emotional barriers, sometimes called affective filters, that push learners away from math activities entirely. Reframing the math task inside a game context helps lower that barrier.

*Chronicles of Arithmos* addresses mathematics anxiety by embedding arithmetic drills inside RPG combat encounters. Each equation appears as a spell or attack input rather than a test question, so a student who would freeze before a worksheet instead types an answer to defeat a Slime or a Skeleton Warrior. This reframing shifts the focus from "taking a math test" to "battling an enemy," reducing the stress associated with timed academic assessments.

---

### Flag 32 — § 2.1.3 Flow Theory – DragonBox Algebra

**Revised:** 2026-03-08  
**Summary:** Replaced "but it does not explain" bridge with forward-looking design-problem statement; merged parallel "If X / If Y" into semicolon construction; added 7-word punchy closer; varied sentence lengths (15→26→12→27 / 28→20→7 / 13→25).

**Humanized Text:**

Once the emotional barrier drops, a different design problem appears: keeping the student engaged over time. Csikszentmihalyi (1990) introduced Flow Theory to describe a mental state where a person is fully absorbed in an activity because the challenge matches their current skill [8]. A task that is too easy causes boredom; one that is too hard triggers frustration. The state between these two extremes is called "flow," and a learning system that does not adjust its difficulty will eventually lose the student to one or the other.

*Chronicles of Arithmos* applies Flow Theory through its Adaptive Difficulty Scaling system, which adjusts the complexity of math problems during combat based on the player's performance and current character level. When a player demonstrates mastery of addition and subtraction, the equations shift to multiplication and division at higher enemy tiers. The difficulty changes with the learner.

DragonBox Algebra demonstrates a similar application of Flow Theory in educational gaming. Its progressive leveling system changes the gameplay as the player learns new algebraic concepts, with each stage presenting harder problems to maintain the state of flow [9].

---

### Flag 33 — § 2.2.1 Mage Math

**Revised:** 2026-03-08  
**Summary:** Full section rewrite using PERSONALITY.md; downgraded 14 elevated vocabulary items; replaced "traverse" → "walks around", "embed" → "put inside", "incorporates functionality" → "has"; added ESL marker ("students that learn"); injected Angel phrasing ("keep going", "costs money").

**Humanized Text:**

**Developer:** Mage Learning Interactive LLC.
**Date Published:** 7 September 2019 (Updated on: 14 May 2025)
**Reference:** <https://www.magemath.com/>  
Mage Math is a 3D fantasy adventure game for students in Grades 1–6, and it teaches math through a role-playing environment. The game was first released as a paid application on Steam and the Epic Games Store. It has a "math realm" where the player answers math problems to get magical skills and move through the story, and there is also a 3D exploration phase where the player walks around a fantasy world.

Mage Math and *Chronicles of Arithmos* both put math exercises inside RPG combat, and both games target primary school students that learn math through a fantasy setting. The two games also tie story progression to math problems, so the player has to answer equations to unlock new areas and keep going in the game.

Mage Math is a 3D game with only single-player mode, and it costs money to play since it is sold on Steam. *Chronicles of Arithmos* is a 2D standalone application that is free, and it also has Peer-to-Peer (P2P) multiplayer which lets players on the same local network connect and play together without needing a central server.

*Figure No. 1: Mage Math Gameplay*

---

### Flag 34 — § 2.2.2 Grand Prix Multiplication

**Revised:** 2026-03-08  
**Summary:** Full section rewrite for sliding window coverage; replaced "multiplayer learning platform" → "racing game"; "avatar's velocity is based on" → "car goes faster when"; "design goals center on" → "the whole game is built around" (Angel signature); added PEMDAS and four biomes as perplexity boosters.

**Humanized Text:**

**Developer:** Arcademics Inc.
**Date Published:** 2016-05-17
**Reference:** <https://www.arcademics.com/games/grand-prix/>
Grand Prix Multiplication is a web-based and mobile racing game that helps students in Grades 3–5 practice multiplication. The player controls a race car, and the car goes faster when the player answers multiplication questions quickly and correctly. The whole game is built around speed and getting the right answer as fast as possible.

Grand Prix Multiplication and *Chronicles of Arithmos* both use game mechanics to make students solve math problems, and both games are aimed at elementary-level students. The two games also have multiplayer features that let players play with other students during gameplay.

Grand Prix Multiplication only does multiplication drills and it runs on the web, so the player always needs internet and there is no exploration or story. *Chronicles of Arithmos* is a 2D standalone RPG that covers all four operations through PEMDAS, and it has a full narrative that runs across four biomes. The proposed system also uses P2P local multiplayer instead of online matchmaking.

*Figure No. 2: Grand Prix Multiplication Gameplay*

---

## Chapter 3 — Technical Background

### Flags 35–36 — § 3.1.2 Software (HTML5/WebGL/CSS & JS ES6)

**Revised:** 2026-03-09  
**Summary:** Enforced the Chapter 3 Four-Part Formula (What it is, Where it's used, Why, Outcome). Eliminated 4× "will" and 3× "utilize/used". Dropped ESL wording and passive AI transitions ("allowing the proponents to..."). Injected 6+ perplexity boosters (*Chronicles of Arithmos*, *.exe*, *RPG Maker MZ engine*, *Virtual Numeric Keypad*, *PeerJS*). Kept sentence structures compound and flowing, mirroring Angel's personal voice.

**Humanized Text (HTML5/WebGL & CSS):**

HTML5 is the standard markup language for the web, while WebGL is a JavaScript API for rendering graphics. The proponents apply these technologies to the web-based deployment build of Chronicles of Arithmos. These tools render hardware-accelerated 2D battle graphics directly within client web browsers, which lets the game run smoothly on shared school computers or mobile phones without asking the player to download a native .exe installer. Cascading Style Sheets (CSS) is a style-sheet language used to define the visual presentation of web pages. The proponents apply CSS directly to the index.html container that hosts the RPG Maker MZ engine. The code handles the scaling of the game canvas across different monitor sizes and visually pins the Virtual Numeric Keypad onto the screen. Because of this explicit styling, the math interface stays intact and usable even if a student plays the game on a smaller touch-screen device.

**Humanized Text (JavaScript ES6):**

JavaScript (ECMAScript 6) is a programming language that handles complex features and logic on web pages. The proponents write custom plugins in JavaScript to build the core mechanics of Chronicles of Arithmos. It is the native scripting language of RPG Maker MZ, so the developers can directly edit the source code to program the Math Battle System, the Enemy Auto-Scaling calculations, and the PeerJS multiplayer handshakes. This direct access removes the need to buy or install third-party bridge software just to change how the default turn-based combat works.

---

### Flag 42 — § 3.1.4 Network Testing

**Revised:** 2026-03-09  
**Summary:** Eliminated 3× "will"; dropped "During the development lifecycle" filler; downgraded 4 vocab items; added PeerJS as perplexity booster; 2 passive→active rewrites; 3→2 sentences; added "before going live" Angel-level aside.

**Original:**
> During the development lifecycle, the proponents will conduct multiplayer testing using two distinct network configurations. First, the peer-to-peer handshake and data synchronization will be validated using multiple personal computers connected to the same local internet connection (LAN/Same Wi-Fi) to verify low-latency performance. Second, the system will be tested with computers connected to different internet networks (WAN) to simulate remote play conditions and verify the stability of the "Room Code" connection over the public internet.

**Humanized:**
> The proponents test the P2P multiplayer connection in two setups before going live. The first one puts multiple PCs on the same Wi-Fi (LAN) to check whether the PeerJS handshake and player data sync without lag, and the second connects PCs through different internet networks (WAN) to see if the Room Code stays stable over the public internet.

---

### Flag 43 — § 3.2.1 Implementation Hardware — PC Requirements Intro

**Revised:** 2026-03-09  
**Summary:** Eliminated 1× "will be required"; merged 2 sentences → 1 compound with "so"; added NW.js and .exe as perplexity boosters; downgraded "will be required to have" → "needs".

**Original:**
> Users will be required to have a personal computer (PC), desktop, or laptop to install and use *Chronicles of Arithmos*. The minimum hardware requirements, based on the tested configuration, are as follows:

**Humanized:**
> The desktop version of Chronicles of Arithmos runs as a standalone .exe file through NW.js, so the player needs a PC or laptop that meets the tested minimum specs listed below:

---

### Flag 44 — § 3.2.1 Implementation Hardware — Mobile Requirements Intro

**Revised:** 2026-03-09  
**Summary:** Eliminated 1× "will require"; ESL marker ("Players that" instead of "Users who"); added .exe and WebGL 2.0 as perplexity boosters; downgraded "access the application via the web browser deployment" → "open the game through a mobile browser instead of the .exe".

**Original:**
> Users who access the application via the web browser deployment will require a mobile device with the following minimum specifications:

**Humanized:**
> Players that open the game through a mobile browser instead of the .exe need a device that can run WebGL 2.0, and the minimum tested specs are as follows:

---

### Flag 45 — § 3.2.2 Implementation Software — Operating System

**Revised:** 2026-03-09  
**Summary:** Eliminated 2× "will be"; merged 3 sentences → 2 compound; replaced "relies on modern 64-bit system components" → "needs 64-bit system components that older versions...do not have"; added .exe as perplexity booster; "since" connector replacing second "because"; user's manual macOS removal preserved.

**Original:**
> The minimum operating system requirement will be Windows 10 (64-bit). This OS environment is needed because the NW.js runtime wrapper, which powers the game's executable, relies on modern 64-bit system components that are not supported in older versions like Windows 7. For mobile users, Android 10 or iOS 14 will be required because the game's web technologies (WebGL 2.0) depend on updated support found in these mobile operating systems.

**Humanized:**
> The minimum operating system for the desktop version is Windows 10 (64-bit) because NW.js, which packages the game as an .exe file, needs 64-bit system components that older versions like Windows 7 do not have. Mobile users need at least Android 10 or iOS 14 since the browser version of the game runs on WebGL 2.0, and older mobile systems do not support it.

---

### Flag 46 — § 3.2.2 Implementation Software — Modern Browsers

**Revised:** 2026-03-09  
**Summary:** Eliminated 2× "will" + "utilize"; dropped AI filler transition ("To align with the development environment"); broke Rule of Three (overlay/rendering/handshake → 2 items); collapsed 3 sentences → 2; added PeerJS + Room Code as perplexity boosters; "which is why" Angel-style justification.

**Original:**
> Users will be required to use a modern web browser to access the web-deployed version via GitHub Pages. To align with the development environment, the supported browsers will specifically include Chromium-based web browsers such as Google Chrome and Microsoft Edge. These browsers are required because the game's Virtual Numeric Keypad overlay, WebGL rendering, and Peer-to-Peer (P2P) Multiplayer Framework handshake utilize HTML5 and Web Real-Time Communication (WebRTC) standards that are most reliably implemented within these browsers.

**Humanized:**
> The web-deployed version on GitHub Pages needs a modern Chromium-based browser, specifically Google Chrome or Microsoft Edge, because the game's Virtual Numeric Keypad and P2P Multiplayer handshake through PeerJS both depend on HTML5 and WebRTC support. These two browsers handle WebGL rendering and the Room Code connection most consistently, which is why the proponents chose them as the supported platforms.

---

### Flag 47 — § 3.2.3 Implementation Peopleware — Students

**Revised:** 2026-03-09  
**Summary:** Eliminated 3× "will"; broke Rule of Three (solve/explore/progress) into compound sentence; replaced "engage directly" → "interact with it mostly through"; added perplexity boosters (Slimes, Skeleton Warriors, Mila); reused Gold Standard phrasing "whether the attack goes through."

**Original:**
> Students (Grades 4-6) will serve as the primary operators of the system. They will engage directly with the Math Battle System to solve arithmetic equations, explore the game world, and progress through the narrative. Their interaction will focus on developing calculation speed and accuracy to defeat enemies and clear procedural quests.

**Humanized:**
> Students in Grades 4 to 6 are the primary users of the system, and they interact with it mostly through the Math Battle System, which is answering arithmetic equations to attack enemies like Slimes and Skeleton Warriors. Getting answers right decides whether the attack goes through, so the game naturally pushes them to work on calculation speed and accuracy as they clear quests from Mila and move through the narrative.

---

### Flag 48 — § 3.2.3 Implementation Peopleware — Educators and Guardians

**Revised:** 2026-03-09  
**Summary:** Eliminated 4× "will" and 2× "utilize"; removed "Meanwhile" transition; broke Rule of Three (reinforce/assign); downgraded "directly assist the primary learner" → "help their child"; added perplexity boosters (Training Dummy, PEMDAS, P2P Multiplayer, Room Code).

**Original:**
> Mathematics teachers instructing Grades 4 to 6, along with the parents or guardians of those specific students, will act as secondary users who utilize the application as a supplementary educational tool. These educators will use the software to reinforce classroom arithmetic topics (such as PEMDAS) or to assign specific Training Dummy practice drills. Meanwhile, guardians will utilize the game to support home-based learning, potentially joining via the P2P Multiplayer mode to directly assist the primary learner during difficult combat encounters.

**Humanized:**
> Mathematics teachers for Grades 4 to 6, along with the parents or guardians of those students, use the system as a classroom and home support tool. Teachers can set up Training Dummy drills to go over specific PEMDAS topics outside of regular combat, while guardians can join a session through the P2P Multiplayer Room Code to help their child through harder encounters.

---

### Flag 49 — § 3.2.3 Implementation Peopleware — Gamers

**Revised:** 2026-03-09  
**Summary:** Eliminated 2× "will"; removed "-ing tail" clause; replaced "interact with the system for entertainment purposes" → "use the system mainly for recreational play"; downgraded "cognitive reaction speeds" → "how quickly a player can solve equations under pressure"; added perplexity boosters (Performance-Based Efficacy, Omega Tier, Numeromancer).

**Original:**
> RPG enthusiasts and casual gamers will interact with the system for entertainment purposes. These users will focus on mastering the "Performance-Based Efficacy" mechanics to achieve high-efficiency combat ratings and complete "Omega Tier" endgame challenges, interacting with the system primarily to test cognitive reaction speeds and strategic planning.

**Humanized:**
> RPG enthusiasts and casual gamers use the system mainly for recreational play, focusing on the Performance-Based Efficacy mechanics which reward fast and accurate answers with higher damage multipliers. Completing the Omega Tier challenges, which include the Numeromancer as the final opponent, is the main draw for this group since those encounters test how quickly a player can solve equations under pressure.

---

### Flag 50 — § 3.2.4 Implementation Network — Internet Connection

**Revised:** 2026-03-09  
**Summary:** Broke Rule of Three (3 parallel infinitives → 2 plain-verb phrases); downgraded 3 elevated vocab items ("maintain gameplay connectivity" → "keep the session running", "synchronize player data" → "going out of sync"); added 4 perplexity boosters (PeerJS, WebRTC, Room Codes, Hostinger); expanded 2→3 sentences for burstiness.

**Original:**
> The system requires an active internet connection for the Peer-to-Peer (P2P) multiplayer feature and initial web resource loading. An internet speed of 6 to 10 Mbps is required to maintain gameplay connectivity, synchronize player data, and prevent connection delays during multiplayer sessions.

**Humanized:**
> The P2P multiplayer feature uses PeerJS and WebRTC to establish direct connections between players using Room Codes, and this requires an active internet connection on both ends. An internet speed of 6 to 10 Mbps is enough to keep the session running and prevent player data from going out of sync. The game also needs an internet connection on first load since it is web-hosted on Hostinger.

---

### § 3.1.2 Software — D.4 Git (Not numbered as a flag)

**Revised:** 2026-03-07  
**Summary:** Humanized Git paragraph with project-specific justification.

**Humanized Text:**

Because the plugin codebase for Chronicles of Arithmos changes frequently as new battle formulas and quest scripts are added, the proponents adopted Git, a distributed version control system, during the development phase. Git tracks each file modification as a separate commit. These commits are then pushed to the remote GitHub repository, which keeps the working copies of all four proponents synchronized and preserves a revertible history of every plugin revision.

---

### § 3.1.2 Software — D.5 Vercel (Not numbered as a flag)

**Revised:** 2026-03-07  
**Summary:** Humanized Vercel paragraph with WebRTC/HTTPS justification.

**Humanized Text:**

The WebRTC handshake that powers the P2P Multiplayer Framework requires an HTTPS connection. To satisfy this requirement during early development, the proponents deploy the web-based build of *Chronicles of Arithmos* on Vercel, a cloud-based hosting platform for frontend applications. Vercel connects directly to the project's GitHub repository, so each push to the main branch triggers an automatic rebuild of the playable web version. This staging configuration remains active until the proponents acquire a dedicated domain and production hosting plan.

---

## Chapter 4 — Methodology

### Flag 51 — § 4.1 Prototyping Model (All 6 stages)

**Revised:** 2026-03-09  
**Scope:** Full rewrite of all 6 prototyping stages  
**Summary:** Eliminated 14× "will" (reduced to 0); 6 unique openers (Method/Output/Tool/Participants/Feedback/Goal per Pattern 9); downgraded 8 elevated vocab items; added 22 game-specific perplexity boosters (PEMDAS, Slimes, Numeromancer, Mr. Apostol, Plains of Origin, .exe, NW.js, Hostinger, etc.); injected 9 Angel-voice markers; switched 4.1.4–4.1.6 from future → present tense.

**Humanized Text:**

#### 4.1.1 Requirements Gathering

The proponents started by reviewing the DepEd Grade 4 to 6 mathematics curriculum to identify which arithmetic operations the game should cover, and this ranged from basic addition and subtraction up to multi-step PEMDAS equations. The proponents also consulted the Capstone Adviser, Mr. Jan Nichole B. Apostol, and researched related materials to educational games like Prodigy Math to determine what the Math Engine should handle and what falls outside the scope of the project. The result was a working list of game requirements and the specific math topics each enemy tier should test.

#### 4.1.2 Quick Design

Flowcharts, wireframes, and storyboards were the main outputs of this stage. The proponents drew flowcharts that show how a student moves through the game from the main menu into the battle screen, and wireframes for the key interfaces like the math input prompt and the Virtual Numeric Keypad overlay. The proponents also drafted storyboards for the four biomes (Forest, Desert, Tundra, and Volcanic) to plan where each enemy type appears and how the maps connect to each other.

#### 4.1.3 Building Prototype

RPG Maker MZ was the primary tool for building the initial prototype because it already has a built-in map editor, event system, and a database for managing enemies and character stats. The proponents wrote the Math Battle System plugin in JavaScript to generate arithmetic equations and check player answers through the Virtual Numeric Keypad, and the Active Time Battle (ATB) timer was connected to the battle loop so that each combat turn runs on a countdown. PeerJS was also added for peer-to-peer (P2P) multiplayer so that two players can connect using room codes, and the proponents built the first versions of the Plains of Origin and Forest biome maps too.

#### 4.1.4 Customer Evaluation of Prototype

Ten (10) Grade 4 to 6 students and the Capstone Adviser, Mr. Jan Nichole B. Apostol, are the two groups that will evaluate the prototype. The Capstone Adviser reviews the core mechanics first to check whether the Math Engine generates the correct equations for each difficulty tier, whether the scaling adjusts properly across enemy levels, and whether the P2P connection holds during two-player sessions. After the internal review, the proponents will run a small usability test with the student participants to see if the gameplay is clear, if the math problems are readable on screen, and if the students stay interested enough to continue playing. What both groups provide determines what the proponents change before the next prototype cycle.

#### 4.1.5 Refining Prototype

Based on what the Capstone Adviser and the student testers report, the proponents adjust the prototype in this stage. If the difficulty scaling is too simple or too difficult for certain enemy tiers (Slimes at Level 1 compared to the Numeromancer at Level 100, for example), the algorithm is rebalanced so the math problems match the player's progress more accurately. The battle menu and the Virtual Numeric Keypad layouts are also revised based on how the students actually used them during testing, since what looks clear on a wireframe does not always work the same way on screen. P2P timing issues, assuming any arise during the multiplayer tests, are fixed in this stage too.

#### 4.1.6 Engineer Product

The goal of this final stage is a stable build of Chronicles of Arithmos that runs both as a desktop application and as a web application. The proponents will run final system tests to confirm that all four biomes, the Math Engine, the adaptive difficulty algorithm, and the multiplayer module work correctly on both platforms. Once testing is done, the proponents package the desktop version as a standalone .exe file using NW.js and host the web version on Hostinger so that students can access the game through a browser without requiring a separate installation.

---

### Flag 52 — § 4.2.2 Technical Feasibility (Intro)

**Revised:** 2026-03-07  
**Summary:** Applied 8-15-25 sentence length rule (14→9→21); front-loaded opening clause; removed repetitive "that" structures.

**Humanized Text:**

Before development begins, the proponents must verify that the proposed system is technically achievable. This evaluation covers the chosen hardware and software tools. The primary goal is confirming that these components operate together without conflict while directly supporting the educational mechanics of teaching arithmetic.

---

### Flag 53 — § 4.2.2.1 Compatibility Checking — Hardware

**Revised:** 2026-03-09  
**Summary:** Eliminated 2× "will"; replaced generic opener ("The proponents will develop...") with tool-first concrete opener ("RPG Maker MZ is the core development engine"); added Intel Core i3 as perplexity booster; "so" connector replacing "Since...it will"; added Math Battle System as specificity anchor.

**Original:**
> The proponents will develop the game using RPG Maker MZ, which is compatible with standard personal computers having at least 8GB of RAM. Since the game is deployed via HTML5, it will run on devices with a modern web browser that supports HTML5, including the tablets and computers.

**Humanized:**
> RPG Maker MZ is the core development engine, and it runs on standard personal computers with at least 8 GB of RAM, which the proponents confirmed through testing with an Intel Core i3 configuration. The web-deployed version also runs on any device with a modern HTML5 browser, so school tablets and computers can access the Math Battle System without needing to install anything.

---

### Flag 54 — § 4.2.2.1 Compatibility Checking — Software

**Revised:** 2026-03-09  
**Summary:** Removed "utilized" → "handles"; dropped 2× -ing tail clauses ("maintaining...", "allowing..."); replaced "compatible with web-standard protocols" → "uses WebRTC"; added Room Codes as specificity booster; "so" and "because" connectors replacing elevated phrasing; renamed to "Math Battle Engine" for proper project term.

**Original:**
> The proposed system uses JavaScript to extend the game engine's features, maintaining a consistent connection between the math logic and the RPG mechanics. The PeerJS library is utilized for multiplayer features because it is compatible with web-standard protocols, allowing students to establish peer-to-peer connections without requiring a dedicated central server.

**Humanized:**
> The Math Battle Engine is built in JavaScript (ES6), which is RPG Maker MZ's native scripting language, so the math logic connects directly to the RPG combat system without any extra conversion layer. PeerJS handles the multiplayer side because it uses WebRTC, which lets students connect through Room Codes directly without needing a central server in between.

---

### Flag 55 — § 4.2.2.2 Relevance of the Technology

**Revised:** 2026-03-07  
**Summary:** Broke formulaic "however, a common limitation" structure; added Performance-Based Reward system name, 2.0x Critical Hit detail; varied sentence lengths (27→20→15→21→19→10).

**Humanized Text:**

Prodigy Math and Math Blaster both use gamified exercises to teach arithmetic, yet in both platforms the math questions and the combat animations operate as separate layers. A correct answer triggers a pre-set action at full strength; the speed of the response does not affect the outcome. This separation means the math portion functions more as a gate than as a core mechanic. Chronicles of Arithmos addresses this gap through the Performance-Based Reward system, which feeds answer speed and correctness directly into the damage calculation. A fast, correct answer produces a 2.0x Critical Hit, while a slow, incorrect one results in a missed attack. The math does not precede the gameplay; it determines the result.

---

## Summary Table

| Flag | Chapter | Section | Date Revised | Status |
| :--- | :--- | :--- | :---: | :---: |
| 1–4 | Ch.1 | § 1.1 Project Context (Opening + Math Anxiety) | 2026-03-09 | ✅ |
| 5–11 | Ch.1 | § 1.1 Project Context (Gamification, Tables) | 2026-03-09 | ✅ |
| 12 | Ch.1 | § 1.2.2 Specific Objectives (D–K) | 2026-03-08 | ✅ |
| 13–23 | Ch.1 | § 1.3.1 Scope (A–J) | 2026-03-09 | ✅ |
| 24 | Ch.1 | § 1.3.2 Limitation A: Math Scope | 2026-03-09 | ✅ |
| 25 | Ch.1 | § 1.3.2 Limitation B: Tactile Input | 2026-03-09 | ✅ |
| 26 | Ch.1 | § 1.3.2 Limitation C: Input Method | 2026-03-09 | ✅ |
| 27 | Ch.1 | § 1.3.2 Limitation D: Asset Fidelity | 2026-03-09 | ✅ |
| 28 | Ch.1 | § 1.3.2 Limitation E: P2P Latency | 2026-03-09 | ✅ |
| 29 | Ch.1 | § 1.3.2 Limitation F+G: Session/Save | 2026-03-09 | ✅ |
| 30 | Ch.2 | § 2.1.1 Game-Based Learning | 2026-03-08 | ✅ |
| 31 | Ch.2 | § 2.1.2 Mathematics Anxiety | 2026-03-08 | ✅ |
| 32 | Ch.2 | § 2.1.3 Flow Theory | 2026-03-08 | ✅ |
| 33 | Ch.2 | § 2.2.1 Mage Math | 2026-03-08 | ✅ |
| 34 | Ch.2 | § 2.2.2 Grand Prix Multiplication | 2026-03-08 | ✅ |
| 35-36 | Ch.3 | § 3.1.2 Software (HTML5/WebGL/CSS/JS) | 2026-03-09 | ✅ |
| 42 | Ch.3 | § 3.1.4 Network Testing | 2026-03-09 | ✅ |
| 43 | Ch.3 | § 3.2.1 PC Requirements | 2026-03-09 | ✅ |
| 44 | Ch.3 | § 3.2.1 Mobile Requirements | 2026-03-09 | ✅ |
| 45 | Ch.3 | § 3.2.2 OS | 2026-03-09 | ✅ |
| 46 | Ch.3 | § 3.2.2 Browsers | 2026-03-09 | ✅ |
| 47 | Ch.3 | § 3.2.3 Students | 2026-03-09 | ✅ |
| 48 | Ch.3 | § 3.2.3 Educators/Guardians | 2026-03-09 | ✅ |
| 49 | Ch.3 | § 3.2.3 Gamers | 2026-03-09 | ✅ |
| 50 | Ch.3 | § 3.2.4 Internet Connection | 2026-03-09 | ✅ |
| — | Ch.3 | § 3.1.2 D.4 Git | 2026-03-07 | ✅ |
| — | Ch.3 | § 3.1.2 D.5 Vercel | 2026-03-07 | ✅ |
| 51 | Ch.4 | § 4.1 Prototyping Model (6 stages) | 2026-03-09 | ✅ |
| 52 | Ch.4 | § 4.2.2 Feasibility Intro | 2026-03-07 | ✅ |
| 53 | Ch.4 | § 4.2.2.1 Hardware Compatibility | 2026-03-09 | ✅ |
| 54 | Ch.4 | § 4.2.2.1 Software Compatibility | 2026-03-09 | ✅ |
| 55 | Ch.4 | § 4.2.2.2 Relevance of Technology | 2026-03-07 | ✅ |
