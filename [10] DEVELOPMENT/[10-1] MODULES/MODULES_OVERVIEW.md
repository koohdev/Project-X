# Chronicles of Arithmos: Development Modules & Sub-Modules Overview

This document outlines the core technical modules required for the development of *Chronicles of Arithmos*, specifically formatted to reflect the project's Specific Objectives (Main Modules) and Scope (Sub-Modules/Features). It is intended to serve as a structured roadmap for the programmer.

## A. Standard Role-Playing Game (RPG) Combat Mechanics

*This module serves as the base structure for all combat interactions.*

- **Purpose**: Establishes the foundational logic, timing, and resource pools for all battle scenes.
- **Key Features**: Time Progress Battle (TPB) Wait system, turn ordering sequence, HP/MP/TP management, and the Training Hall implementation.
- **A.1 Time Progress Battle (TPB)**: Implementation of a visible "Action Gauge" based on character Speed/Agility, which forcibly freezes when a math equation is on screen.
  - *Technical Constraint*: The system must pause all enemy action gauges the exact millisecond the math window opens to prevent attacks while calculating.
- **A.2 Turn Structure**: The sequenced logic of combat (1. Select Action -> 2. Solve Math -> 3. Execute Action).
- **A.3 Resource Management**: Tracking of Health Points (HP), Mana Points (MP), and Tactical Points (TP) during battle.

## B. Math Battle System Plugin

*The core educational feature replacing standard random number generation (RNG) probability.*

- **Purpose**: Replaces standard RPG 'hit or miss' probability with mental arithmetic challenges to build calculation speed.
- **Key Features**: Math equation generation upon action selection, keyboard/numpad physical inputs.
- **Core Function**: Generates math equations during combat selection. The player must successfully solve equations to execute actions (Attack, Skill, Items) using keyboard inputs.
- **Input Method**: Must capture physical keyboard keystrokes (number row or numpad).
- **Math Constraints (CRITICAL)**:
  - Answers must strictly be exact whole numbers.
  - The script must prevent fractions or decimals from ever being generated, especially during division logic.
  - The multiplier and divisor (the second number in multiplication/division operations) are strictly capped at a range of 1 to 20 across all difficulty levels.

## C. Level-Based Difficulty System

*Automatically scales the complexity of the generated math equations to match the player's progression.*

- **Purpose**: Automatically adapts the complexity of the generated math operations to ensure the player is consistently challenged.
- **Key Features**: Multi-tiered operator unlocking (Basics to PEMDAS) and dynamic vs fixed equation generation.
- **C.1 Levels 1-29 (Basics)**: Addition and Subtraction using two numbers (e.g., 15 + 7).
- **C.2 Levels 30-69 (Intermediate)**: Introduces Multiplication and Division operations (e.g., 12 * 4).
- **C.3 Levels 70-100 (Advanced)**: Generates full PEMDAS equations (e.g., (10 + 5) * 2).
- **Training Dummy Logic**: Generates variable (matching party level) or fixed-level equations for safe practice in Training Halls. Dummy must have infinite HP and an "Escape" command to exit manually.

## D. "Content-Aware" Timer System

*Calculates the dynamic countdown timer allowed for the player to input their answer.*

- **Purpose**: Provides a scalable time limit that adjusts based on the specific math problem generated.
- **Key Features**: Dynamically calculated base time windows with bonuses for harder operators.
- **Timer Logic**: Automatically calculates the time window based on equation complexity, total length, and operators.
  - *Base Time Formula*: `Equation length / Number of digits`.
  - *Bonus Time*: Added if operations include `*` or `/`, or if numbers are exceptionally large.
- **Penalty Logic**: Answers entered after the timer hits zero automatically register as "slow" inputs, even if technically correct.

## E. Enemy Auto-Scaling System

*Maintains difficulty across all geographical areas.*

- **Purpose**: Prevents players from out-leveling early-game areas, maintaining combat relevance without duplicating enemy states manually.
- **Key Features**: Background adjustment of enemy metrics relative to the party level.
- **Scaling Logic**: A background process that automatically recalculates Enemy base `Max HP`, `ATK`, `EXP drop`, and `Gold drop` values relative to the active party's average level upon battle start.

## F. Performance-Based Reward Mechanism

*Calculates the direct mechanical outcome of a selected action based on input speed and correctness.*

- **Purpose**: Directly ties combat success and damage output to the player's mathematical speed and accuracy.
- **Key Features**: Four distinct result tiers (Critical hit, normal hit, weak hit, complete miss).
- **Correct & Rapid**: Applies a 2.0x critical multiplier to the action's base effect.
- **Correct & Slow**: Executes the action at normal 1.0x capacity.
- **Incorrect & Rapid**: Applies a 0.5x penalty to the action's base effect.
- **Incorrect & Slow**: Action is completely nullified (Fail/Miss).

## G. Automatic Quest Generation System

*Dynamically creates side quests to maintain replayability.*

- **Purpose**: Creates an infinite loop of side content to encourage continued calculation practice outside of the main story.
- **Key Features**: Location-aware procedural quest hunting/gathering algorithms.
- **Quest Logic**: Scans boolean flags for unlocked areas to generate relevant hunting/gathering tasks based on regional enemies and drops.
- **Constraints**: Quests must have no time limits. They can be natively rejected to flush the variables and roll new tasks immediately.

## H. Peer-to-Peer (P2P) Multiplayer Framework

*Enables drop-in cooperative gameplay without centralized server accounts.*

- **Purpose**: Allows players to cooperatively solve math puzzles and fight bosses together.
- **Key Features**: Direct text-based ID connections and real-time state syncing.
- **Networking Logic**: Text-based Room Code generation for the Host, allowing a direct connection to merge the joining player's party into the Host's game.
- **Known Limitations**:
  - Stateless architecture: If the host application closes, the session dissolves immediately for all clients (no state recovery).
  - High host ping may cause Math Timer desyncs on the client side.

## I. Save System

*Manages persistent local data storage.*

- **Purpose**: Secures user progress via manual slots and automated checkpoints.
- **Key Features**: 20 manual save slots + 1 autosave background script.
- **Save Slots**: Features 20 manual save slots with overwrite capability.
- **Autosave**: A dedicated slot triggered sequentially in the background upon crossing map transition checkpoints.

## J. Level-Based Progression

*Establishes the phases of progression by providing rewards following successful combat and completing quests.*

- **Purpose**: Controls the game's pacing, narrative unraveling, and the timeline for releasing harder math problems.
- **Key Features**: Leveling caps, gold caps, and switch-based map unlocking.
- **J.1 Experience Points (EXP)**: Thresholds ranging from 10 EXP (basics) up to a hard cap of 99,999 EXP (endgame bosses).
- **J.2 Gold (Currency)**: Economic scaling from 5 G (basics) up to a hard cap of 50,000 G (endgame drops).
- **J.3 Story Milestones**: Triggers (switches/variables) that unlock new maps and higher-level stages, preventing the math scaling from breaking due to over-grinding.

## K. Mobile Detection System and Virtual Numeric Keypad

*Ensures accessibility on touch-screen interfaces.*

- **Purpose**: Allows the game to be played on tablets and mobile devices lacking hardware keyboards.
- **Key Features**: Environment detection triggers and a custom overlay UI element.
- **Keypad UI**: Automatic environment check (`Touch screen == true`) that renders a Virtual Numeric Keypad UI layer adjacent to the math equation window for tapping inputs. Buttons must map directly to physical keys.

## L. Game Assets and Entities

*The databasing of all world-building structures: visual maps, BGM, SFX, class parameters, and items.*

- **Purpose**: The physical databases required to bring the narrative and systems to life visually.
- **Key Features**: Over 160 weapons, 8 distinct classes, 5 biomes, and multiple layered Status Effect buffs/debuffs.
- **L.1 Character Roster**: 30+ Main Story Characters & Companions.
- **L.2 Background NPCs**: Townspeople, Guards, Merchants.
- **L.3 Enemies**: Separated by biomes.
  - L.3.1 Plains & Forest Biome
  - L.3.2 Desert Biome
  - L.3.3 Tundra & Frost Biome
  - L.3.4 Volcano & Fire Biome
  - L.3.5 General & Dungeon
- **L.4 Items**: Over 50+ consumable and loot items.
  - L.4.1 Consumable Items (Recovery & Utility)
  - L.4.2 Stat Boosters (Permanent Upgrades)
  - L.4.3 Monster Loot & Drops
- **L.5 Class Roster**: 8 defined classes (Swordsman, Sorcerer, Priest, Knight, Martial Artist, Magic Swordsman, Hunter, Bandit).
- **L.6 Weapons**: 160+ unique class-specific weapons.
  - L.6.1 Swordsman (Swords)
  - L.6.2 Sorcerer (Staves)
  - L.6.3 Priest (Maces)
  - L.6.4 Knight (Spears)
  - L.6.5 Martial Artist (Claws)
  - L.6.6 Magic Swordsman (Enchanted Blades)
  - L.6.7 Hunter (Bows)
  - L.6.8 Bandit (Daggers)
- **L.7 Skills**: Dedicated combat skills tailored for each class.
- **L.8 Status Effects Scripting**:
  - *Debuffs*: Need DoT logic (Poison, Bleed, Burn) and Action restriction logic (Sleep, Paralysis, Freeze).
  - *Buffs*: Need stat boosters, Auto-Life revival logic, and Magic Reflection logic.
