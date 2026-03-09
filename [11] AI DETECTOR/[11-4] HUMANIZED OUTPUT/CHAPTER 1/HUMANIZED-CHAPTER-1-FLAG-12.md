### 1.2.2 Specific Objectives

#### A. To implement battle mechanics

  This module will serve as the base structure for the custom math integration. It will include a time-based battle system, turn ordering, and character stat management for Health (HP), Mana (MP), and Tactical Points (TP). Additionally, the game will feature a tutorial sequence in the opening area where mentor characters will teach the basics of combat. To provide a continuous fail-safe for skill development, every town will feature at least one training hall where the player will be able to fight a training dummy to practice their combat and mathematical calculation skills. The user will interact with this module by inputting combat commands and managing their party's health, mana and tactical points during encounters.

#### B. To develop a Math Battle System plugin

 This module will serve as the core educational feature of the game. It will replace standard chance-based combat where random probability decides if an attack hits or misses with direct math challenges. The user will interact with this module by using a keyboard to solve generated math equations within a visual interface to successfully execute their in-game actions.

#### C. To implement a Level-Based Difficulty System

 This module will automatically adjust the complexity of the math equations based on the character's current level. It will change the amount of numbers in an equation, the types of math operators used, and the size of the numbers. To provide a risk-free environment for users to practice these mechanics, the game will feature designated Training Halls in every town. The user will interact with this module by solving math problems that dynamically increase in difficulty during normal gameplay, or by engaging a Training Dummy with infinite health. During these practice encounters, users can choose fixed-level dummies to practice specific equation types or a scaling dummy that matches their current party level, exiting the session at any time by clicking the "Escape" combat command.

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

#### L. To integrate diverse Game Assets and Entities

 This module will serve as the main world building structure by providing a collection of pixel art maps, background music, sound effects, enemies, and equipment. Users will engage with this module by exploring distinct areas such as forests, deserts, tundras, and volcanos, listening to location specific audio, defeating the specific enemies found in those locations, and equipping different weapons, armor, and accessories.
