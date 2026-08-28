**DOMINICAN COLLEGE OF TARLAC, INC.**

**Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling.**

A Capstone Proposal Presented to

Dominican College of Tarlac, Inc.

In Partial Fulfillment of the Requirements

for the Degree of Bachelor of Science in Information Technology

by:

Guevarra, John Angel D.

Lacsina, Justine C.

Manalo, Allan Joshua C.

Panganiban, Justine T.

Quinez, John Benedict D.

Jan Nicole B. Apostol, LPT

Adviser

September, 2026

**DOMINICAN COLLEGE OF TARLAC, INC.**

**ADVISER’S RECOMMENDATION SHEET**

This Capstone Proposal entitled

**Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling**

by:

Guevarra, John Angel D.

Lacsina, Justine C.

Manalo, Allan Joshua C.

Panganiban, Justine T.

Quinez, John Benedict D.

And submitted in partial fulfillment of the requirements of the

Bachelor of Science in Information Technology degree has been examined and is

recommended for acceptance and approval

Jan Nicole B. Apostol, LPT

Adviser

September, 2026

**DOMINICAN COLLEGE OF TARLAC, INC.**

**DEAN’S ACCEPTANCE SHEET**

This Capstone Proposal entitled

**Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling.**

After having been recommended and approved is hereby accepted

by the College of Computer Studies,

Dominican College of Tarlac, Inc.

Rossano C. Samson

Dean

September, 2026

**DOMINICAN COLLEGE OF TARLAC, INC.**

**PANEL’S APPROVAL SHEET**

This Capstone Proposal entitled

**Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling.**

Developed by:

Guevarra, John Angel D.

Lacsina, Justine C.

Manalo, Allan Joshua C.

Panganiban, Justine T.

Quinez, John Benedict D.

After having been presented is hereby approved by the following

members of the panel.

Airon Prince C. Beltran , LPT Crisha Cayabyab

Panelist Panelist

Gerald B. Tolentino

Lead Panelist

September, 2026

# Acknowledgement

The proponents express their gratitude to Almighty God for the wisdom, strength, good health, and peace of mind granted to the proponents throughout the development of this project. His constant grace provided clarity during difficult moments and sustained the proponents across every stage of the study.

Sincere appreciation is extended to Mr. Jan Nicole B. Apostol, the capstone adviser, for his consistent direction and constructive critiques. His technical guidance helped refine the game mechanics and keep the documentation aligned with college standards. His patience in addressing technical questions and reviewing drafts was vital to completing this manuscript.

The proponents extend their gratitude to our OIC-dean, Mr. Rossano C. Samson, Dean of the College of Computer Studies, along with the faculty members of Dominican College of Tarlac. Their instruction provided the foundational technical skills needed to carry out this capstone undertaking. The institutional resources and administrative assistance offered by the college enabled the proponents to work effectively.

Special thanks are offered to the capstone defense panel, composed of Mr. Gerald B. Tolentino as Lead Panelist, alongside Mr. Airon Prince C. Beltran, LPT and Ms. Crisha Cayabyab. Their thorough evaluation, practical suggestions, and discerning questions during the defense sessions substantially improved both the software architecture and the written documentation.

The proponents express deep gratitude to their parents and families for their constant encouragement, patience, and financial assistance. Their understanding during long working hours and demanding milestones gave the proponents the motivation to finish this study.

The proponents also thank their classmates and friends who offered helpful feedback, tested early game builds, and shared moral support. Finally, the members of the research group acknowledge one another for the hard work, teamwork, and shared dedication that made the completion of this capstone project possible.

Abstract

Chronicles of Arithmos is a 2D role-playing game designed to help elementary students in Grades 4 to 6 practice mental mathematics. Developed under a prototyping model using RPG Maker MZ, JavaScript, and PeerJS, the game blends standard turn-based combat with arithmetic problems aligned with the Department of Education MATATAG curriculum. Instead of treating math exercises as separate pop-up drills, the battle system uses calculation speed and accuracy to calculate attack damage, spell strength, and healing.

The game includes an adaptive difficulty system scaling from basic addition and subtraction to multi-step PEMDAS equations, a timer that adjusts to problem length, auto-scaling enemies, and a local peer-to-peer multiplayer mode. Dedicated town Training Halls feature practice dummies so players can work through calculations without taking damage or losing progress. Accessible on Windows computers and mobile web browsers with an on-screen keypad. Overall, Chronicles of Arithmos provides a game environment that turns math drills into active combat challenges.

Keywords: Game-Based Learning, Role-Playing Game, Dynamic Difficulty Adjustment, Mathematics Anxiety, Prototyping Model, Peer-to-Peer Multiplayer.

# Table of Contents

1.0 Introduction 1

1.1 Project Context 1

1.2 Objectives 4

1.2.1 General Objective 4

1.2.2 Specific Objectives 4

1.3 Scope and Limitations 7

1.3.1 Scope 7

1.3.2 Limitations 37

2.0 Review of Related Literature/Systems 39

2.1 Related Theories 39

2.1.1 Dynamic Difficulty Adjustment 39

2.1.2 Peer-to-Peer (P2P) 39

2.1.3 Order of Operations (PEMDAS) 40

2.2 Related Projects 40

2.2.1 Mage Math 40

2.2.2 Grand Prix Multiplication 41

2.3.3 Prodigy Game 44

3.0 Technical Background 46

3.1 Development 46

3.1.1 Hardware 46

3.1.2 Software 46

3.1.3 Peopleware 50

3.1.4 Network 50

3.2 Implementation 51

3.2.1 Hardware 51

3.2.2 Software 51

3.2.3 Peopleware 51

3.2.4 Network 52

4.0 Methodology 53

4.1 Prototyping Model 53

4.1.1 Requirements Gathering 53

4.1.2 Quick Design 54

4.1.3 Building Prototype 54

4.1.4 Customer Evaluation of Prototype 54

4.1.5 Refining Prototype 55

4.1.6 Engineer Product 55

4.2 Requirements Specification 56

4.2.1 Operational Feasibility 56

4.2.2 Technical Feasibility 58

4.2.3 Schedule Feasibility 60

4.2.4 Economic Feasibility 65

4.2.5 Requirements Modeling 67

4.2.6 Risk Assessment/Analysis 81

4.3 Design 81

4.3.1 Output and User-interface Design 81

4.3.2 Data Design 83

4.3.3 System Architecture 83

4.4 Development 84

4.4.1 Software Specification 84

4.4.2 Hardware Specification 85

4.4.3 Program Specification 85

4.4.4 Programming Environment 88

4.4.5 Test Plan 89

4.5 Verification, Validation, Testing 90

4.5.1 Unit Testing 90

4.5.2 Integration Testing 91

4.6 Acceptance Testing 92

4.7 Implementation Plan 93

4.7.1 Physical Environment 93

4.7.2 Interfaces 93

4.7.3 Functionality 93

4.7.4 Data 94

4.7.5 Security 94

4.8 Installation Processes 95

5.0 Conclusion and Recommendations 96

5.1 Conclusion 96

5.2 Recommendations 97

**List of Appendices**

Appendix A: Work Assignments A1-A2

Appendix B: Definition of Terms B1-B3

Appendix C: Database Design C1-C4

Appendix D: Screen Design D1-D21

Appendix E: Evaluation Tools/ Test Documents and Test Results E1-E3

Appendix F: Certifications and Letters F1

Appendix G: Program Listings G1-G15

Appendix H: User’s Manual H1-H20

Appendix I: Curriculum Vitae I1-I5

Appendix J: Story, Characters, Items, Character Classes and Biomes J1-J17

**List of Tables**

Table #1 November 2025 Gantt Chart 60

Table #2 December 2025 Gantt Chart 60

Table #3 January 2026 Gantt Chart 61

Table #4 February 2026 Gantt Chart 61

Table #5 March 2026 Gantt Chart 62

Table #6 April 2026 Gantt Chart 62

Table #7 May 2026 Gantt Chart 63

Table #8 June 2026 Gantt Chart 63

Table #9 July 2026 Gantt Chart 63

Table #10 August 2026 Gantt Chart 64

Table #11 September 2026 Gantt Chart 64

Table #13 Cost and Benefits Table 65

Table # 14: System Information 84

Table # 15: System Information 85

Table #16: Program Specification 85

Table #17: Actors Table Database Design C-1

Table #18: Animations Table Database Design C-1

Table #19: Armors Table Database Design C-1

Table #20: Classes Table Database Design C-2

Table #21: Enemies Table Database Design C-2

Table #22: Items Table Database Design C-2

Table #23: Skills Table Database Design C-3

Table #24: States Table Database Design C-3

Table #25: Weapons Table Database Design C-3

Table #26: Save File Data Table Database Design C-4

Table #27 Test Data E-1

Table #28 Unit Testing Results E-3

Table #29 Compatibility Test Result (Web Desktop) E-7

Table #30 Compatibility Test Result (Windows) E-8

Table #31 Compatibility Test Result (Mobile Web) E-9

Table #32 Performance Test Result (Windows) E-10

Table #33 Performance Test Result (Web Desktop) E-14

Table #34 Performance Test Result (Web Mobile) E-18

Table #35 Stress Testing Result E-22

Table #36 Acceptance Testing Result E-23

**List of Figures**

Figure No. 1. Mage Math Logo 40

Figure No. 2: Mage Math Gameplay 41

Figure No. 3 Grand Prix Multiplication Logo 42

Figure No. 4: Grand Prix Multiplication Gameplay 43

Figure No. 5: Prodigy Math Logo 44

Figure No. 6: Prodigy Game Gameplay 45

Figure No. 7 : Prototyping Model 53

Figure No. 8: Fishbone Diagram 56

Figure No. 9: Functional Decomposition Diagram 57

Figure No. 10: Player Use Case Diagrams 67

Figure No. 9: Auto Quest Sequence Diagram 68

Figure No. 10: Enemy Auto-Scaling Sequence Diagram 69

Figure No. 11: Level-Based Progression Sequence Diagram 70

Figure No. 12: Math Battle System Sequence Diagram 71

Figure No. 13: P2P Multiplayer Sequence Diagram 72

Figure No. 14: Save Sequence Diagram 73

Figure No. 15: Title Screen Module Activity Diagram 74

Figure No. 16: Figure: Exploration, Main Menu and Save Module Activity Diagram 75

Figure No. 17: Enemy Auto-Scaling Module Activity Diagram 76

Figure No. 18: Math Battle System Module Activity Diagram 77

Figure No. 16 : Dark Blue, Black and White 81

Figure No. 17: Chronicles of Arithmos Logo 82

Figure No. 18: M+ 1m regular Font 82

Figure No. 19: Survey Result - Content Evaluation E-25

Figure No. 20: Survey Result - Demographics E-26

Figure No. 21: Survey Result - Module Evaluation E-28

Figure No. 22: Survey Result – Multimedia Elements E-29

Figure No. 23: Survey Result – Navigation E-30

Figure No. 24: Survey Result – Usefulness E-31

Figure No. 25: Beta Testing Session E-35

Figure No. 26: Endorsement Letter F-1

# Introduction

## Project Context

RPG or role-playing games is a kind of video game where the gamer or the player moves through a story, completes missions and battles hostile elements. The core mechanics of these games include exploration of the environment, character progression and combat. Traditional role playing games often use random chance to determine the outcome of combat. This brings an element of luck when deciding the winner.

Game based learning is an educational method that combines game mechanics with academic lessons. This teaching method uses systems of points, grades, and rewards to deliver information. Instead of standard lectures or drilling exercises, the system provides education directly to the learners through immersive play.

Placing RPG games into the learning environment aims to increase the focus of the students and improve their test results. Academic activities, such as solving basic arithmetic operations and practicing PEMDAS rules under the DepEd MATATAG curriculum, are incorporated into a virtual fantasy world. The MATATAG curriculum strictly focuses on building foundational mathematics skills for primary students [1]. Furthermore, data shows that children aged 9 to 12 frequently use mobile phones and digital screens as their primary tools for learning and entertainment [2]. Placing these math exercises inside a familiar digital game softens the psychological difficulties of the students. This virtual environment reduces the anxiety levels linked with strict time limited tests [3]. In spite of these benefits, educational games do not have it so easy.

In spite of these benefits, educational games do not have it so easy. An informal phenomenon, also known as the chocolate covered broccoli effect, occurs when creators of games with an educational theme carefully hide routine educational activities behind the veneer of superficial aesthetic elements [4]. Under these conditions, the education does not interact with the fundamental gameplay loop. When players feel an activity is just a hidden test, it lowers their natural desire to play. Furthermore, games with a single difficulty level fail to keep the attention of students. According to the rules of Flow theory, fast learners get bored when a game is too easy. At the same time, slow learners get frustrated when a game is too hard [5].

To overcome these barriers, educational role playing games must bring the learning goals into the main game mechanics. This ensures that the academic tasks become the determining factor for victory. The adaptive difficulty scaling matches the changing skill of the learner. The system must use this to maintain the best level of challenge. As a result, this creates a state of flow that removes boredom and frustration.

Educational RPGs must mix learning into the core gameplay to solve these issues. School exercises should act as the main factor to decide success in the game. It should not act as a separate layered activity. Systems must also use adaptive difficulty scaling to adjust the challenge based on the current skill of the player. Balancing the game difficulty keeps students in a mental state called flow. This flow state prevents boredom and frustration.

The proposed project is a 2D turn based Role Playing Game. Standard RPGs use random chance to decide combat results. This project will feature a custom math battle system instead. The success of attacks, blocks, and skills in this system will depend completely on the player. They must solve math equations under a time limit.

The approach overcomes the shortcoming of traditional mathematics drills by converting them into combat system mechanisms. Players perform primitive arithmetic tasks, including addition, subtraction, multiplication, and division, along with more complicated intermediate steps like PEMDAS. These operations are carried out to improve the mind in both speed and accuracy of mental mathematics. Furthermore, the system provides immediate physical rewards for mental hard work. Players manage to solve the numerical problems successfully, achieve the next character level, and eliminate boss enemies.

The mathematical activities are considered part of the main game loop in the project. In the game, progression requires the delivery of accurate mathematical answers which hence make players always engage in mathematical skills throughout play. This building creates a space that is specifically targeted to support the practice of mathematics.

The proposed game is given the title of the game is Chronicles of Arithmos. The proponents will build the project using RPG Maker MZ, a 2-dimensional engine designed to create turn-based role-playing games. The completed work shall be in the form of an application to run on windows platforms and a web browser and have a virtual number keypad to support touchscreen tools.

Educational games often do not provide the player with long-term engagement because of the so-called Chocolate Covered Broccoli effect. Under these conditions, game makers obstruct traditional academic exercises with aesthetics related to the game, which leads to the learning mechanics that do not interact with the main game. As a result, the learners will know about the disguised drills, and the motivation will be lowered. Permanent challenge roads also discourage players, the fast learners see the material as inadequately challenging and lose interest as well as the slow learners feel discouraged. The lack of replay value also reduces the reasons to play the game multiple times. Chronicles of Arithmos aims to solve these problems by using three main features: a math battle engine, a changing difficulty scale, and automatic enemy scaling.

Chronicles of Arithmos aims to solve the specific challenges of separated learning, fixed difficulty, and low replay value. The arithmetic combat engine solves the separated learning issue. This engine acts as the main determinant for success in combat and is never an independent activity. A difficulty tracking subsystem solves the static difficulty problem. It automatically changes the math equations to match the player at their exact level. Moreover, the game solves the low replay value using an automatic quest system. The game creates new quests automatically depending on the parts of the map explored by the player. This maintains a sense of novelty without the game developers doing manual mission design.

Reducing mathematics anxiety among primary school students in Grade 4 to 6 is the major aim of this project. These specific learners are usually 9 to 12 years old. Skagerlund et al. (2024) define this condition as a feeling of tension and fear that stops problem solving [6]. The tension comes in the form of a massive mental block. Students show lower academic results even when they actually have the needed intelligence and skills. Gokce and Guner (2024) also state that extreme mathematics anxiety consumes a massive section of working memory capacity [7]. This leads to students wasting mental resources to process negative emotions. They will then have less mental energy left to solve the actual math problems.

Placing math operations into a fantasy game world creates a low stakes environment. This setting lowers the negative emotional reactions linked to normal classroom activities. Players get real time feedback when playing a game. A successful calculation will result in an in combat Critical Hit and will act as a tangible reward. This instant reinforcement redefines the attitude of the learner towards mathematics from a source of stress into a source of confidence (Maryana et al., 2024) [8].

The inability to answer a mathematical problem appears as a Game Over screen instead of a failing grade so that students can do the calculations over and over again without the consequences of actual failure in the real world. Every in-game town contains a Training Hall, which facilitates a stress-free study method; players are able to train to achieve speed in calculations and combat controls by using a Training Dummy with maximum health, and end the lessons at their own will.

## Objectives

### 1.2.1 General Objective

The primary objective of this project is to design and develop Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling.

### 1.2.2 Specific Objectives

1. *To implement battle mechanics.*

This module will serve as the base structure for the custom math integration. It will include a time based battle system, turn ordering, and character stat management for Health (HP), Mana (MP), and Tactical Points (TP). Additionally, the game will feature a tutorial sequence in the opening area where mentor characters will teach the basics of combat. To provide a continuous fail-safe for skill development, every town will feature at least one training hall where the player will be able to fight a training dummy to practice their combat and mathematical calculation skills. The user will interact with this module by inputting combat commands and managing their party's health, mana and tactical points during encounters.

1. *To develop a Math Battle System plugin.*

This module will serve as the core educational feature of the game. It will replace standard chance based combat where random probability decides if an attack hits or misses with direct math challenges. The user will interact with this module by using a keyboard to solve generated math equations within a visual interface to successfully execute their in game actions.

1. *To implement a Level-Based Difficulty System.*

This module will automatically adjust the complexity of the math equations based on the character's current level. It will change the amount of numbers in an equation, the types of math operators used, and the size of the numbers. To provide a risk-free environment for users to practice these mechanics, the game will feature designated Training Halls in every town. The user will interact with this module by solving math problems that dynamically increase in difficulty during normal gameplay, or by engaging a Training Dummy with infinite health. During these practice encounters, users can choose fixed-level dummies to practice specific equation types or a scaling dummy that matches their current party level, exiting the session at any time by clicking the "Escape" combat command.

1. *To engineer a "Content Aware" Timer System.*

This module will serve as the time limit during combat. It will automatically calculate the amount of time given to the player based on the equation's complexity, the total number of digits, and the types of math operators used. Users will use this feature by typing their math answers before the countdown clock runs out.

1. *To integrate an Enemy Auto Scaling System*

This module will change enemy stats like health and attack power to match the average level of the players party. Doing this will keep battles balanced in all map areas. Because of this, the proponents will not have to make copy pasted versions of the exact same monsters. Players will experience this system when they fight enemies that get stronger as their own characters level up.

1. *To create a Performance Based Reward Mechanism.*

This module will handle the main combat rewards. It will check how fast and accurate the math answer is to find the result of an action. The system gives a double effect (2.0x) for a fast and correct answer. A slow but correct answer gives a normal effect. A fast but wrong answer gives half the effect (0.5x). A slow and wrong answer makes the move fail completely. Players get these exact results during combat. They trigger the results by typing the math answer on the screen.

1. *To develop an Automatic Quest Generation system*

This module will build side quests on its own. It will check the exact monsters and items inside unlocked map areas. The proponents will not write every single mission by hand. The system will make the tasks. Players will talk to Receptionist Mila to use this feature. She will give the party new tasks to hunt monsters or collect items.

1. *To implement a Peer to Peer (P2P) Multiplayer Connection.*

This module will run the cooperative gameplay feature. It will link players together directly. Users will not create online accounts to play together. Players will talk to Portal Keeper Alden to access this feature. He will let them create a unique room code to host a game. He will also let them type a code to join the match of another player.

1. *To integrate a Saving System.*

This module saves game data in local files. Moving maps makes auto checkpoints. It has manual save spots. Players pick a slot to save. They can load old data to play again.

1. *To engineer a Level Based Progression System.*

This modules will handle the game speed. It moves stages and triggers story events. Proponents unlock harder math when character levels go up. Users go through Foundational then Intermediate then Advanced stages. Harder math and new map areas or biomes show the progress.

1. *To implement a Mobile Input System.*

This module will check if the user is playing the game on a touch screen device. When the math input box opens in battle, the system will show a Virtual Numeric Keypad right of the screen. This will let the player tap on screen number buttons to send their answers. Players will use this feature by tapping the virtual keypad on their mobile phones to solve math problems during combat.

1. *To integrate diverse Game Assets and Entities.*

This module will serve as the main world building structure by providing a collection of pixel art maps, background music, sound effects, enemies, and equipment. Users will engage with this module by exploring distinct areas such as forests, deserts, tundras, and volcanos, listening to location specific audio, defeating the specific enemies found in those locations, and equipping different weapons, armor, and accessories.

## 1.3 Scope and Limitations

### 1.3.1 Scope

1. *Standard Role-Playing Game (RPG) Combat Mechanics*

The user interacts with this module by using a computer mouse or trackpad to click through visual combat menus (such as "Attack," "Skills," or "Items"), explicitly selecting actions to manage their party's health and mana during encounters. The scope of the proposed project includes core combat mechanics structured around:

* 1. *Time Progress Battle (TPB)*

This module will feature a visible "Action Gauge" for each combatant that fills based on their Speed or Agility stat. The game will utilize a wait-based system to automatically freeze all of these action gauges the exact moment the math input window appears on the screen. This full stop of the battle timers will make sure that enemies cannot take their turns. They will not be able to attack while the player solves the math problem and types the answer.

* 1. *Turn Structure*

Players will know it is their turn when the Action Gauge of their character fills up. During this phase, they will use a computer mouse to click through the combat menus. The player will choose from options like Attack, Skills, or Items to manage the health and mana of the party. Battles will follow a clear order. A player will pick an action first. The system will then check the math answer.

* 1. *Resource Management*

Players will track three point pools. HP shows the damage a character takes. If HP hits zero the unit is out. Players use MP for magic. TP is for combat skills.

1. *Math Battle System Plugin.*

This module or part is the main gameplay loop for Chronicles of Arithmos. The game switches to this system when a player meets an enemy and picks a battle command. The player must solve a math equation before the time limit ends to finish their move. The system changes the difficulty of this math problem to match the current level of the user. Players will type whole number answers into the screen using the number row or numpad of the keyboard. They will then press the Enter key to attack before the clock runs out.

1. *Level Based Difficulty System*

This module will automatically scale the complexity of the generated math equations based on the character's current level. The user will interact with this module by visually reading the generated equations on the screen and mentally calculating answers for problems that automatically increase in term counts and operator types as their character levels up. Furthermore, this module will govern the mathematical generation for safe-practice Training Halls located in every town. The user will interact with this feature by engaging a Training Dummy, which possesses infinite Health Points (HP) and serves solely as a target for calculation practice. Users will choose between two types of targets. A fixed level dummy will give math problems for a set difficulty rank. A dynamic dummy will make equations that match the current average level of the party. Because the dummy cannot be defeated, the user will interact with the visual combat menu by clicking the "Escape" button to manually exit the training session. The math difficulty will follow a level based order:

* 1. Player Levels 1-29 (Basics): The game will make math problems that use addition and subtraction with two values. For example: 15 + 7.
  2. Player Levels 30-69 (Intermediate): The game will introduce Multiplication and Division operations. For example: 12 \* 4.
  3. Player Levels 70-100 (Advanced): The game will generate three part equations utilizing the full PEMDAS rules (Parentheses, Exponents, Multiplication, Division, Addition, Subtraction). For example: (10 + 5) \* 2.

1. *"Content Aware" Timer System*

This module will use a changing timer to decide how much time players get to answer. The system will check the difficulty of the math equation. It will count the total digits and look at the symbols. It will give extra time for harder math like multiplication and division. The game will also add bonus seconds for problems with larger numbers. The input box will stay on the screen even if the clock hits zero. Players must still type an answer to move forward. However, the system will mark any late answer as slow. This happens even if the math is correct. Players will watch a countdown bar during battles. They will type their answers on a keyboard or touch screen before the time runs out.

1. *Enemy Auto Scaling System*

This module will change enemy stats in the background. It will update Health Points (HP) and Attack power (ATK). It will also update Experience Points (EXP) and Gold rewards in real time. These numbers will change to match the average level of the party. Players will see this change during combat. Users will start battles by touching visible monster graphics. They will also start random fights while exploring the map. The health and attack values of the monsters will match the strength of the team during these fights.

1. *Performance Based Reward Mechanism*

This module will run the combat math. It will check the speed and accuracy of the math answer. This action will find the exact result of a move. Players will type their answers using fast keystrokes or screen taps. The game will give visual and sound feedback. This feedback will depend on the final speed and accuracy of the user. This rule will apply to all battle commands. The math check will give the following results based on the performance of the player:

* + Correct and rapid answers will apply a 2.0x critical multiplier to the action's overall effect.
  + Correct but slow answers will execute the action at its normal, base value.
  + Fast but wrong answers will apply a 0.5x penalty to the final effect of the action.
  + Incorrect and slow answers will result in complete action nullification, causing the selected move to fail entirely.

1. *Automatic Quest Generation system*

This module will run a system to build quests on its own. It will check the details of all the map areas the player has already opened. Chronicles of Arithmos will look at the monsters and items inside these biomes or locations. It will use this data to make new hunting and gathering tasks. These new missions will not have a time limit. Because of this, players can finish them at any point during the game. When a quest is accepted, the system will save it in the Quests tab so the user can track their progress. If a quest is rejected, the game will remove it and create a different task during the next conversation. Players will use this feature by clicking the map to walk their character toward Receptionist Mila. They will click on her to open the menu, and then they will click to accept or reject the new side quests.

1. *Peer-to-Peer (P2P) Multiplayer Framework*

This module will handle the cooperative multiplayer gameplay. It will use direct connections with text based room codes. The game will allow drop in combat, which means the system will automatically merge the party of a joining player with the party of the host. Players will use this feature by talking to an NPC. Players will click the Host Room button to make a room code for their game. They will click the Join Room button from the exact same character to enter another match. They will then type the code of a friend to join the room.

1. *Save*

This module will save game progress into local files on the device. The system will give users 20 manual save slots. It will also have one auto save function. A player can pick a slot that already has old data. The game will then replace that old file with the new progress. The auto save feature will also rewrite its own specific slot every time the character reaches a new checkpoint. Players will use this feature by opening the Save screen from the main menu. They will click a specific slot to manually record their progress. They will also trigger the automatic saves just by clicking to move their character through map exits.

1. *Level Based Progression*

This module will set up the stages of player growth. It will give specific rewards after players win battles and explore the map. Players will use this feature by fighting monsters or finishing quests to earn the rewards listed below:

* 1. Experience Points (EXP): Gaining EXP will raise the level of the character. The lowest amount a player can get from a low level monster is 10 points (Level 1 Slime). The game will limit the highest possible reward from an end game boss to 99,999 points.
  2. Gold (Currency): Players will collect this money when they beat enemies and finish quests. The minimum gold drop from a basic enemy is 5 G, while the maximum reward from a high-tier boss or elite quest is 50,000 G. This currency is used to buy new equipment and items from merchants.
  3. Story Milestones: Updates the "Story Progress", allowing the game to unlock higher-level maps.

1. *Mobile Detection System and Virtual Numeric Keypad*

This module will automatically detect if the user is on a mobile device. When the math input window opens during combat, the system will display a Virtual Numeric Keypad directly next to it on the screen. The user will interact with this module on supported mobile devices by physically tapping the on-screen number buttons and the "Submit" button to enter math answers.

1. *Game Assets and Entities*

This module will serve as the main world-building structure by providing a collection of pixel art maps, background music, sound effects, enemies, and equipment. The user will interact with this module by exploring distinct areas such as forests, deserts, tundras, and volcanos, defeating area specific enemies, and equipping various weapons, armor, and accessories. These assets will include:

* 1. *Character Roster*

This includes the main characters that the player will talk to, fight alongside, or receive quests from to move the story forward

* + - *Bron*
    - *Martha*
    - *Lily*
    - *Kael*
    - *Elara*
    - *Garrick*
    - *Sylas*
    - *Isolde*
    - *Thorne*
    - *Lyra*
    - *Fenrin*
    - *Elder Tobias*
    - *Merchant Oryn*
    - *Receptionist Mila*
    - *Bard Jareth*
    - *Captain Valerius*
    - *Professor Haze*
    - *Innkeeper Gorm*
    - *Blacksmith Rurik*
    - *Widow Claire*
    - *Farmer Ben*
    - *Alchemist Vanya*
    - *Librarian Estel*
    - *Guard Captain Aris*
    - *Fisherman Old Tom*
    - *Street Urchin Pip*
    - *Nobleman Caelus*
    - *Priestess Anara*
    - *Hunter Kaelen*
    - *Portal Keeper Alden*
    - *The Numeromancer*
  1. *Background NPC’s*

This includes the generic townspeople and villagers used to fill up the maps to make the game world feel alive and busy.

* + - *Townsman 1-5 (Male)*
    - *Townswoman 1-5 (Female)*
    - *Playing Boy 1-2*
    - *Playing Girl 1-2*
    - *Market Shopper 1-3*
    - *Tavern Patron 1-4*
    - *Knight*
    - *Farmhand 1-2*
    - *Stable Boy*
    - *Washerwoman*
    - *Street Sweeper*
    - *Beggar 1-2*
    - *Strolling Couple (Man/Woman)*
    - *Academy Student 1-4*
    - *Visiting Merchant*
    - *Visiting Noble*
    - *Lost Tourist*
    - *Drunkard*
    - *Gossiping Lady 1-2*
    - *Running Messenger*
    - *Sleeping Guard*
    - *Fishing Boy*
    - *Old Cat Lady*
    - *Street Performer*
    - *Watching Crowd Member*
  1. *Enemies:*

This includes the enemies that the user may encounter during their playthrough.

* + 1. *Plains & Forest Biome:*
       - *Slime*
       - *Rat*
       - *Bat*
       - *Spider*
       - *Hornet*
       - *Wolf*
       - *Bear*
       - *Treant*
       - *Goblin*
       - *Goblin Archer*
       - *Goblin Shaman*
       - *Orc*
       - *Bandit*
       - *Bandit Leader*
       - *Crow*
       - *Snake*
       - *Fairy*
       - *Mandrake*
       - *Wild Boar*
       - *Forest Golem*
    2. *Desert Biome:*
       - *Sand Slime*
       - *Scorpion*
       - *Giant Scorpion*
       - *Cactus*
       - *Sand Worm*
       - *Mummy*
       - *Skeleton Warrior*
       - *Skeleton Mage*
       - *Desert Wolf*
       - *Lamia*
       - *Basilisk*
       - *Gargoyle*
       - *Sand Golem*
       - *Vulture*
       - *Sphinx*
       - *Desert Rogue*
       - *Ant Lion*
       - *Dust Spirit*
       - *Ancient Scarab*
       - *Pharaoh’s Guard*
    3. *Tundra & Frost Biome*
       - *Ice Slime*
       - *Snow Wolf*
       - *Polar Bear*
       - *Ice Bat*
       - *Snow Spirit*
       - *Yeti*
       - *Ice Golem*
       - *Crystal Spider*
       - *Frost Giant*
       - *White Tiger*
       - *Corrupted Penguin*
       - *Ice Drake*
       - *Frozen Knight*
       - *Winter Wisp*
       - *Wendigo*
       - *Frost Mage*
       - *Glacial Turtle*
       - *Snow Harpy*
       - *Ice Elemental*
       - *Fenrir*
    4. *Volcano & Fire Biome*
       - *Magma Slime*
       - *Fire Spirit*
       - *Imp*
       - *Demon*
       - *Succubus*
       - *Cerberus*
       - *Lava Golem*
       - *Fire Bat*
       - *Salamander*
       - *Dragon Hatchling*
       - *Red Dragon*
       - *Efreet*
       - *Phoenix*
       - *Iron Giant*
       - *Dark Knight*
       - *Cultist*
       - *Fire Elemental*
       - *Minotaur*
       - *Chimera*
       - *Demon Lord*
    5. *General & Dungeon*
       - *Training Dummy*
       - *Ghost*
       - *Zombie*
       - *Vampire*
       - *Vampire Bat*
       - *Mimic*
       - *Shadow*
       - *Will-o'-the-Wisp*
       - *Animated Armor*
       - *Flying Sword*
       - *Magic Pot*
       - *Gazer*
       - *Ogre*
       - *Troll*
       - *Warlock*
       - *Necromancer*
       - *Reaper*
       - *Chaos Cloud*
       - *Number Eater*
       - *Equation Spirit*
       - *The Unknown*
  1. *Items*

This includes the items that the user may receive from either buying from shops, completing quests or being dropped as loot from enemies during their playthrough.

* + 1. *Consumable Items (Recovery & Utility)*
       - *Potion*
       - *Hi-Potion*
       - *Full Potion*
       - *Magic Water*
       - *Hi-Magic Water*
       - *Elixir*
       - *Antidote*
       - *Eye Drops*
       - *Echo Herb*
       - *Stimulant*
       - *Potent Stimulant*
       - *Panacea*
       - *Dispel Herb*
       - *Escape Rope*
       - *Repel Spray*
    2. *Stat Boosters (Permanent Upgrades)*
       - *HP Up*
       - *MP Up*
       - *Strength Seed*
       - *Defense Seed*
       - *Magic Seed*
       - *Agility Seed*
       - *Luck Seed*
       - *Skill Book*
    3. *Monster Loot & Drops*
       1. *Plains/Forest*
          - *Green Gel*
          - *Rat Tail*
          - *Bat Wing*
          - *Sticky Web*
          - *Insect Wing*
          - *Wolf Pelt*
          - *Bear Claw*
          - *Living Branch*
          - *Goblin Cloth*
          - *Shaman Bead*
          - *Orc Tusk*
          - *Stolen Coin Purse*
          - *Shiny Feather*
          - *Snake Skin*
          - *Fairy Dust*
          - *Mandrake Root*
          - *Boar Meat*
          - *Ancient Bark*
       2. *Desert*
          - *Yellow Gel*
          - *Scorpion Stinger*
          - *Cactus Flower*
          - *Sand Essence*
          - *Old Bandage*
          - *Bone Fragment*
          - *Skull*
          - *Dry Fur*
          - *Snake Scale*
          - *Petrified Eye*
          - *Stone Wing*
          - *Sandstone Block*
          - *Vulture Beak*
          - *Riddle Tablet*
          - *Scarab Shell*
          - *Golden Fragment*
       3. *Tundra*
          - *Blue Gel*
          - *White Fur*
          - *Thick Hide*
          - *Ice Crystal*
          - *Snowflake Core*
          - *Yeti Horn*
          - *Permafrost Shard*
          - *Crystal Leg*
          - *Frost Metal*
          - *Corrupted Feather*
          - *Drake Scale*
          - *Cold Wisp*
          - *Frozen Heart*
          - *Ice Turtle Shell*
          - *Harpy Feather*
          - *Wolf Fang*
       4. *Volcano*
          - *Red Gel*
          - *Ember*
          - *Imp Wing*
          - *Demon Horn*
          - *Succubus Cloth*
          - *Hellhound Fang*
          - *Obsidian Shard*
          - *Fire Gland*
          - *Dragon Tooth*
          - *Red Scale*
          - *Djinn Lamp*
          - *Phoenix Ash*
          - *Iron Scraps*
          - *Dark Armor Piece*
          - *Forbidden Page*
          - *Chimera Tail*
          - *Infernal Core.*
       5. *General*
          - *Ectoplasm*
          - *Rotten Flesh*
          - *Vampire Fang*
          - *Unknown Fluid*
          - *Spirit Dust*
          - *Haunted Metal*
          - *Ceramic Shard*
          - *Evil Eye*
          - *Ogre Club*
          - *Magic Powder*
          - *Tattered Robe*
          - *Chaos Mote*
          - *Arithmetic Essence*
          - *Void Fragment*
  1. *Class Roster:*
     + *Swordsman*
     + *Sorcerer*
     + *Priest*
     + *Knight*
     + *Martial Artist*
     + *Magic Swordsman*
     + *Hunter*
     + *Bandit*
  2. *Weapons*
     1. *Swordsman (Swords)*
        + *Long Sword*
        + *Woodcutter's Blade*
        + *Wolf Fang Sword*
        + *Forest Cutter*
        + *Bandit's Edge*
        + *Verdant Blade*
        + *Sand Scimitar*
        + *Scorpion Tail*
        + *Dune Blade*
        + *Sun-Scorched Sword*
        + *Ancient Khopesh*
        + *Ice Brand*
        + *Glacial Edge*
        + *Frostbite Sword*
        + *Crystal Saber*
        + *Blizzard Blade*
        + *Magma Blade*
        + *Dragon Bone Sword*
        + *Infernal Edge*
        + *Flame Tongue*
        + *Phoenix Feather Sword*
     2. *Sorcerer (Staves)*
        + *Oak Staff*
        + *Briar Rod*
        + *Druid's Staff*
        + *Faerie Wand*
        + *Root Staff*
        + *Nature's Call*
        + *Sandstone Rod*
        + *Mirage Staff*
        + *Cobra Head Staff*
        + *Sun Rod*
        + *Sphinx Cane*
        + *Icicle Rod*
        + *Snowflake Staff*
        + *Hailstorm Wand*
        + *Permafrost Cane*
        + *Frozen Core Staff*
        + *Ember Rod*
        + *Ash Staff*
        + *Dragon Breath Wand*
        + *Core Magma Staff*
        + *Hellfire Rod*
     3. *Priest (Maces)*
        + *Wooden Mace*
        + *Oak Club*
        + *Spirit Mace*
        + *Blessed Branch*
        + *Mossy Hammer*
        + *Guardian's Cudgel*
        + *Golden Scepter*
        + *Sandstone Hammer*
        + *Sun Disc Mace*
        + *Tomb Guardian Club*
        + *Sacred Ankh*
        + *Crystal Mace*
        + *Hailstone Hammer*
        + *Frozen Scepter*
        + *Polar Club*
        + *Divine Ice Mace*
        + *Obsidian Mace*
        + *Lava Rock Hammer*
        + *Cleansing Fire Club*
        + *Forge Master's Hammer*
        + *Phoenix Down Mace*
     4. *Knight (Spears)*
        + *Short Spear*
        + *Hunter's Spear*
        + *Boar Tusk Lance*
        + *Forest Guard Pike*
        + *Wooden Pike*
        + *Leaf-Blade Spear*
        + *Scorpion Stinger*
        + *Desert Pike*
        + *Bronze Lance*
        + *Sandpiercer*
        + *Pharaoh's Guard*
        + *Ice Shard Lance*
        + *Glacier Pike*
        + *Tundra Harpoon*
        + *Frost Wyrm Spear*
        + *Frozen Needle*
        + *Magma Pike*
        + *Dragon Scale Lance*
        + *Red Steel Spear*
        + *Obsidian Lance*
        + *Hellfire Harpoon*
     5. *Martial Artist (Claws)*
        + *Leather Gloves*
        + *Bear Claws*
        + *Wolf Paws*
        + *Sharp Thorns*
        + *Tree Bark Knuckles*
        + *Wild Beast Fists*
        + *Scorpion Pincers*
        + *Sandstone Gauntlets*
        + *Cactus Spines*
        + *Mummy Wraps*
        + *Golden Knuckles*
        + *Ice Picks*
        + *Yeti Fists*
        + *Frostbite Gloves*
        + *Crystal Talons*
        + *Polar Paws*
        + *Salamander Claws*
        + *Dragon Fangs*
        + *Magma Fists*
        + *Burning Knuckles*
        + *Demon Hands*
     6. *Magic Swordsman (Enchanted Blades)*
        + *Rapier*
        + *Wind Blade*
        + *Leaf Cutter*
        + *Elven Rapier*
        + *Swift Blade*
        + *Whisper Edge*
        + *Mirage Rapier*
        + *Heatwave Saber*
        + *Dust Devil Blade*
        + *Golden Epee*
        + *Sun-Strike Sword*
        + *Chill Spike*
        + *Frozen Needle*
        + *Aurora Blade*
        + *Ice Queen's Rapier*
        + *Zero Kelvin, Searing*
        + *Saber*
        + *Molten Rapier*
        + *Blaze Edge*
        + *Phoenix Tail*
        + *Volcanic Spike*
     7. *Hunter (Bows)*
        + *Short Bow*
        + *Oak Bow*
        + *Hunter's Bow*
        + *Ranger's Crossbow*
        + *Vine Bow*
        + *Elven Bow*
        + *Bone Bow*
        + *Sandstone Crossbow*
        + *Scorpion Recurve*
        + *Desert Wind Bow*
        + *Golden Arrow*
        + *Ice Crystal Bow*
        + *Frostbite Crossbow*
        + *Mammoth Ivory Bow*
        + *Blizzard String*
        + *Glacial Shot*
        + *Ash Wood Bow*
        + *Flame String*
        + *Magma Rock Crossbow*
        + *Dragon Bone Bow*
        + *Phoenix Fire Bow*
     8. *Bandit (Daggers)*
        + *Knife*
        + *Rusty Shiv*
        + *Hunter's Knife*
        + *Poison Tip*
        + *Thief's Shank*
        + *Forest Tooth*
        + *Curved Dagger*
        + *Sand Shiv*
        + *Scorpion Barb*
        + *Tomb Blade*
        + *Golden Dagger*
        + *Icicle Shiv*
        + *Frozen Dagger*
        + *Shard of Glass*
        + *Cold Steel Knife*
        + *Frostbite Dirk*
        + *Obsidian Knife*
        + *Heated Dagger*
        + *Ember Shiv*
        + *Dragon Claw*
        + *Hell's Tooth*
  3. *Skills*
     1. *Swordsman*
        + *Strong Attack*
        + *Slash*
        + *Double Slash*
        + *Wide Swing*
        + *Armor Break*
        + *Blade Bash*
        + *Focus*
        + *Parry*
        + *Sonic Wave*
        + *Wind Slash*
        + *Power Break*
        + *Mind Break*
        + *Berserk Stance*
        + *Cross Cut*
        + *Omnislash*
     2. *Sorcerer*
        + *Fire*
        + *Fire II*
        + *Fire III*
        + *Ice, Ice II*
        + *Ice III*
        + *Thunder*
        + *Thunder II*
        + *Thunder III*
        + *Flare*
        + *Freeze*
        + *Shock*
        + *Magic Drain*
        + *Concentrate*
        + *Meteor Swarm*
     3. *Priest*
        + *Heal*
        + *Heal II*
        + *Heal III*
        + *Party Heal*
        + *Cure Poison*
        + *Cure Blind*
        + *Cure Silence*
        + *Panacea*
        + *Raise*
        + *Holy Light*
        + *Protect, Shell*
        + *Regenerate*
        + *Purify*
        + *Divine Intervention*
     4. *Knight*
        + *Provoke*
        + *Shield Bash*
        + *Cover, Iron Defense*
        + *Guard Ally*
        + *Shield Wall*
        + *Fortify*
        + *Sentinel*
        + *Justice Strike*
        + *Heavy Charge*
        + *Taunt*
        + *Unbreakable Will*
        + *Phalanx*
        + *Retribution*
        + *Castle of Stone*
     5. *Martial Artist*
        + *Punch*
        + *Kick*
        + *Triple Kick*
        + *Roundhouse*
        + *Chakra*
        + *Meditate*
        + *Pressure Point*
        + *Earth Splitter*
        + *Gale Palm*
        + *Spirit Wave*
        + *Counter*
        + *Leg Sweep*
        + *Fists of Fury*
        + *Chi Blast*
        + *Seven Star Strike*
     6. *Magic Swordsman*
        + *Fire Blade*
        + *Ice Blade*
        + *Thunder Blade*
        + *Wind Blade*
        + *Drain Blade*
        + *Aspir Blade*
        + *Magic Barrier*
        + *Enchant Weapon*
        + *Dispel Strike*
        + *Elemental Burst*
        + *Arcane Slash*
        + *Spell Shield*
        + *Mystic Thrust*
        + *Teleport Strike*
        + *Rune Breaker*
     7. *Hunter*
        + *Aim*
        + *Power Shot*
        + *Rapid Fire*
        + *Poison Arrow*
        + *Sleep Arrow*
        + *Blind Arrow*
        + *Silence Arrow*
        + *Arrow Rain*
        + *Eagle Eye*
        + *Beast Slayer*
        + *Piercing Shot*
        + *Camouflage*
        + *Trap Set*
        + *Snipe*
        + *Hail of Arrows.*
     8. *Bandit*
        + *Steal*
        + *Mug*
        + *Sneak Attack*
        + *Poison Edge*
        + *Sand Throw*
        + *Smoke Bomb*
        + *Backstab*
        + *Sprint*
        + *Gold Snatch*
        + *Venom Strike*
        + *Shadow Step*
        + *Dirty Trick*
        + *Twin Daggers*
        + *Lucky Strike*
        + *Assassinate*
  4. *Status Effects*
     1. *Negative States (Debuffs)*
        + *Knockout*
        + *Poison*
        + *Blind*
        + *Silence*
        + *Confusion*
        + *Sleep*
        + *Paralysis*
        + *Stun*
        + *Bleed*
        + *Burn*
        + *Freeze*
        + *Slow*
        + *Curse*
        + *Weakness*
        + *Fear*
     2. *Positive States (Buffs)*
        + *Regenerate*
        + *Haste*
        + *Protect*
        + *Shell*
        + *Focus*
        + *Magic Barrier*
        + *Attack Up*
        + *Defense Up*
        + *Magic Up*
        + *Agility Up*
        + *Evasion Up*
        + *Immortal*
        + *Auto-Life*
        + *Reflect*
        + *Counter Stance*
  5. *Armor & Accessory*
     1. *Shields*

*Equippable only by Knights, Swordsmen, Priests*

* + - * *Small Shield*
      * *Buckler*
      * *Round Shield*
      * *Kite Shield*
      * *Iron Shield*
      * *Steel Shield*
      * *Mythril Shield*
      * *Gold Shield*
      * *Wooden Lid*
      * *Hunter's Buckler*
      * *Bronze Shield*
      * *Scale Guard*
      * *Shell Buckler*
      * *Ice Shield*
      * *Crystal Guard*
      * *Frost Shield*
      * *Dragon Shield*
      * *Flame Guard*
      * *Obsidian Shield*
      * *Aegis*
    1. *Headgear*
       - *Leather Cap*
       - *Iron Helmet*
       - *Steel Helmet*
       - *Mythril Helm*
       - *Full Helm*
       - *Viking Helm*
       - *Dragon Helm*
       - *Genji Helm*
       - *Leather Helm*
       - *Feathered Hat*
       - *Magician's Hat*
       - *Circlet, Ribbon*
       - *Bandana, Turban*
       - *Silk Hood*
       - *Fur Hood*
       - *Ice Crown*
       - *Salamander Coif*
       - *Royal Crown*
    2. *Body Armor*
       - *Cloth Tunic*
       - *Leather Armor*
       - *Iron Armor*
       - *Steel Armor*
       - *Mythril Armor*
       - *Plate Mail*
       - *Heavy Mail*
       - *Scale Mail*
       - *Glacial Mail*
       - *Flame Mail*
       - *Dragon Armor*
       - *Traveler's Tunic*
       - *Hard Leather*
       - *Hunter's Vest*
       - *Ninja Suit*
       - *Cotton Robe*
       - *Silk Robe*
       - *Sorcerer's Robe*
       - *Winter Robe*
       - *Lava Robe*
       - *Sage's Robe*
    3. *Accessories*
       - *Ring of Protection*
       - *Ring of Power*
       - *Ring of Magic*
       - *Ring of Speed*
       - *Ring of Life*
       - *Poison Charm*
       - *Silence Amulet*
       - *Blindness Glasses*
       - *Paralysis Talisman*
       - *Sleep Earring*
       - *Fire Ring*
       - *Ice Ring*
       - *Thunder Ring*
       - *Earth Ring*
       - *Gold Ring*
       - *Lucky Coin*
       - *Warrior's Badge*
       - *Scholar's Specs*
       - *Knight's Crest*
       - *Sniper's Eye*
  1. *Background Music (BGM)*
     1. *Battle & Boss Themes*
        + *Battle1*
        + *Battle2*
        + *Battle3*
        + *Battle4*
        + *Battle5*
        + *Battle6*
        + *Battle7*
        + *Boss1*
        + *Boss2*
        + *Boss3*
        + *Boss4*
        + *Boss5*
     2. *Towns & Safe Zones*
        + *Town1*
        + *Town2*
        + *Town3*
        + *Town4*
        + *Town5*
        + *Town6*
        + *Town7*
        + *Castle1*
        + *Castle2*
     3. *Exploration (Overworld & Dungeons)*
        + *Field1*
        + *Field2*
        + *Field3*
        + *Field4*
        + *Dungeon1*
        + *Dungeon2*
        + *Dungeon3*
        + *Dungeon4*
        + *Dungeon5*
        + *Dungeon6*
        + *Dungeon7*
        + *Dungeon8*
        + *Ship1*
        + *Ship2*
        + *Ship3*
     4. *Story & Cutscenes*
        + *Scene1*
        + *Scene2*
        + *Scene3*
        + *Scene4*
        + *Scene5*
        + *Scene6*
        + *Theme1*
        + *Theme2*
        + *Theme3*
        + *Theme4*
        + *Theme5*
        + *Theme6*

### 1.3.2 Limitations

1. *Mathematical Scope and Generation Limits*

The system does not currently support advanced algebra, calculus, or non-integer results (fractions/decimals). To maintain combat flow, the math generator is strictly restricted so that all division problems calculate to exact whole numbers, avoiding fractions or decimals entirely. Furthermore, the system imposes a hard limit on the multiplier and the divisor (the second number in any multiplication or division problem), capping them at a range of 1 to 20. This number limit applies to all battles in the game. It also covers the multi part math problems in higher levels.

1. *Input handling differences*

The Virtual Numeric Keypad lets the game run on touch screens. Tapping a flat screen does not give the physical feedback of real keys.

1. *Input Method*

Input uses number rows or numpads on keyboards. Proponents give mobile users a Virtual Numeric Keypad. Input speed changes depending on the device.

1. *Asset Fidelity*

Chronicles of Arithmos uses 2D pixel art from RPG Maker MZ. Proponents do not use 3D models or hard physics, since RPG Maker MZ is for 2D games pixel.

1. *Peer to Peer Latency Sensitivity*

The multiplayer is based on the internet connection of the host. The intended project will utilize direct peer-to-peer communications instead. Slow internet connection on the host side may cause the Math Timer to stop or result in other players who are involved in the multiplayer feature to be disconnected.

1. *Host Dependent Connection*

Since the project will utilize the peer-to-peer (P2P) architecture, there will be no node that manages a list of games or sessions. When the host shutss down the application or loses its connection, the whole game experience will be ended by everyone. Under these conditions, the participants are not able to re-use the old room code and continue their game, but have to start the new game session.

1. *Local Only Save Data*

Proponents use local files for the save system on the player device. No login or cloud database exists. There is no cloud sync. A player cannot switch from a PC to a phone. They must move the files manually to do this.

# 2.0 Review of Related Literature/Systems

## 2.1 Related Theories

### 2.1.1 Dynamic Difficulty Adjustment

Dynamic Difficulty Adjustment (DDA) adjusts game challenge in real time based on player performance. By matching difficulty to a learner's skill level, DDA keeps players engaged, reducing frustration during hard tasks and preventing boredom during easy drills. Studies show that dynamic difficulty scaling helps sustain motivation across varying student skill levels.

In Chronicles of Arithmos, DDA works through the Level-Based Difficulty System and Enemy Auto-Scaling module. As player characters gain levels, the game increases math equation complexity by adding larger numbers and more advanced operators, while scaling enemy health and damage to keep battles balanced.

Author: Z. Guo, R. Thawonmas, and X. Ren

Source:https://www.sciencedirect.com/science/article/abs/pii/S187595212400034

Date Retrieved: July 8, 2026

### 2.1.2 Peer-to-Peer (P2P)

Peer-to-Peer (P2P) architecture is a network model where connected devices share resources and communicate directly, without routing traffic through a central host server. This structure removes reliance on external server hosting and allows direct local communication between client machines.

In Chronicles of Arithmos, cooperative multiplayer uses a lightweight P2P connection model. Players start local sessions by sharing short alphanumeric room codes through Portal Keeper Alden, allowing teams to clear dungeons and solve math problems together.

Author: Tyler Biscontini

Source:https://www.ebsco.com/research-starters/architecture/peer-peer-p2p

Date Retrieved: July 8, 2026

### 2.1.3 Order of Operations (PEMDAS)

The Order of Operations (PEMDAS: Parentheses, Exponents, Multiplication, Division, Addition, Subtraction) is the standard rule for evaluating multi-operator math expressions. Department of Education (DepEd) MATATAG curriculum guidelines indicate that learning this operational sequence helps elementary students transition from basic arithmetic to multi-step problem solving.

Chronicles of Arithmos follows this curriculum progression across character levels. Levels 1 through 29 cover two-term addition and subtraction, Levels 30 through 69 introduce multiplication and division, and Levels 70 through 100 present three-part expressions that follow full PEMDAS rules.

Author: Department of Education

Source: https://matatagcurriculum.ph/

Date Retrieved: July 8, 2026

## 2.2 Related Projects

### 2.2.1 Mage Math

Developer: Mage Learning Interactive LLC.

Date Published: 7 September 2019 (Updated on: 14 May 2025)

Reference: https://www.magemath.com/

![IMG_256](data:image/png;base64...)

Figure No. 1. Mage Math Logo

Mage Math is a 3D fantasy adventure game for students in Grades 1–6, and it teaches math through a role-playing environment. The game was first released as a paid application on Steam and the Epic Games Store. It has a "math realm" where the player answers math problems to get magical skills and move through the story, and there is also a 3D exploration phase where the player walks around in Mage Math fantasy world.

Mage Math and Chronicles of Arithmos both put math exercises inside RPG combat, and both games target primary school students that learn math through a fantasy setting. The two games also tie story progression to math problems, so the player has to answer equations to unlock new areas and keep going in the game.

Mage Math is a 3D game with only single-player mode, and it costs money to play since it is sold on Steam. Chronicles of Arithmos is a 2D application that is free, and it also has Peer-to-Peer (P2P) multiplayer.

![IMG_256](data:image/png;base64...)

Figure No. 2: Mage Math Gameplay

### 2.2.2 Grand Prix Multiplication

Developer: Arcademics Inc.

Date Published: February 5, 2012 (Updated on: February 5, 2024)

Reference: <https://www.arcademics.com/games/grand-prix>

![IMG_256](data:image/png;base64...)

Figure No. 3 Grand Prix Multiplication Logo

Grand Prix Multiplication is a web-based and mobile racing game that helps students in Grades 3–5 practice multiplication. The system or Grand Prix Multiplication uses a competitive racing mechanism in which the avatar velocity is based on how quickly and accurately the player answers mathematical questions.

Both Grand Prix Multiplication and Chronicles of Arithmos use game mechanics to present mathematical problems. Both systems target elementary-level students and include multiplayer features that allow learners to interact with peers during gameplay.

Grand Prix Multiplication is a web-based racing game that requires an internet connection and focuses solely on multiplication speed drills. It does not include an exploration-based narrative or multi-step problem-solving scenarios. Chronicles of Arithmos is a 2D RPG with a narrative, covers multiple arithmetic operations (PEMDAS), and uses P2P local multiplayer rather than online matchmaking.

![arcagrand](data:image/png;base64...)

Figure No. 4: Grand Prix Multiplication Gameplay

### 2.3.3 Prodigy Game

Developer: Prodigy Education

Date Published: October 9, 2015 (Updated: December 10, 2025)

Reference: https://math.prodigygame.com/?launcher=true&code=7c43d2dd6a0fe

![IMG_256](data:image/jpeg;base64...)

Figure No. 5: Prodigy Math Logo

Prodigy Game is a web-based mathematics role-playing game designed for primary and middle school learners. The system integrates curriculum-aligned math problems into a fantasy combat environment. Players solve arithmetic problems to execute spells and defeat enemies while progressing through levels and collecting in-game rewards.

Both Prodigy and Chronicles of Arithmos use Game-Based Learning (GBL) within a fantasy RPG framework. They share a "Combat-to-Curriculum" loop where mathematical equations serve as inputs for spells and attacks. Both systems also present arithmetic drills as narrative events, which may support the retention of mathematical concepts among students or young learners in Grades 4–6.

Prodigy is an internet-dependent Massively Multiplayer Online RPG (MMORPG) with a freemium subscription model that requires constant connectivity. Chronicles of Arithmos is a 2D application designed for local use without internet dependency. Chronicles of arithmos uses Peer-to-Peer (P2P) cooperative gameplay, focusing on students or young learners collaboration rather than a massive online server. Chronicles of Arithmos also includes Adaptive Difficulty Scaling that adjusts in real-time, whereas Prodigy follows a curriculum-aligned sequence.

![IMG_256](data:image/jpeg;base64...)

Figure No. 6: Prodigy Game Gameplay

# 3.0 Technical Background

## 3.1 Development

### 3.1.1 Hardware

*A. Personal Computers and Laptops*

The proponents will primarily use personal computers (PCs), desktop computers, mobile devices and laptops for documentation, system design, testing, and development of the proposed project.

### 3.1.2 Software

*A. Frontend*

*A.1 RPG Maker MZ*

RPG Maker MZ [GOTC2020] is a game development engine designed for creating 2D role playing games. It will be used in the core application development to construct the visual environment using supplementary tilesets [COMS2020] [WHTD2016a] [WHTD2016b] and character generator parts [HIDD2015] [SOME2026]. The engine will also manage the database of enemy graphics [AEKA2022] and items, and script game events. The proponents utilize this engine because its built in architecture provides a framework for RPG mechanics. To extend these mechanics, the proponents developed custom JavaScript plugins to implement the Math Battle System and core game logic, while integrating select VisuStella plugins [YANF2015] primarily for visual displays, item management, and baseline interface support.

*A.2 HTML5 / WebGL*

HyperText Markup Language 5 (HTML5) is the standard markup language for structuring web content. Web Graphics Library (WebGL) is a JavaScript API for rendering 2D and 3D graphics within web browsers. HTML5 and WebGL will run the web version of the proposed project. The proponents will use these tools to display 2D graphics directly on internet browsers. Doing this will allow the game to work easily on mobile phones and school computers. Users will not need to download or install any extra files to play the game.

*A.3 Cascading Style Sheets (CSS)*

Cascading Style Sheets (CSS) is a style sheet language used to set the visual look and layout of HTML documents and is always partnered up with Javascript. CSS will be use as it allows the proponents to resize the game window across different screen sizes. It will also place the Virtual Keypad overlay in the exact right spot.

*B. Backend*

*B.1 JavaScript (ES6)*

JavaScript (ECMAScript 6) is a programming language used for creating dynamic and interactive content on web pages and is the native scripting language of RPG Maker MZ. JavaScript will be used as it allows the proponents to make custom plugins for the Math Battle System, Level Based Difficulty System, Enemy Auto Scaling System, Automatic Quest Generation system, and P2P Multiplayer Framework.

*B.2 Visual Studio Code (v1.111)*

Visual Studio Code is the project’s main coding hub. While built by Microsoft. The proponents will use it to write game scripts, specifically managing the JavaScript codebase.

*B.3 Node.js (v25.8.1)*

Node.js is an open-source, server-side runtime environment that executes JavaScript outside of a web browser. It will be used during the development phase to run local server environments. Node.js will be used to simulate server-side operations for testing the P2P multiplayer handshake so that the connection logic is stable before deploying to the public web.

*B.4 PeerJS (v1.5.5)*

PeerJS is a Web Real-Time Communication (WebRTC) wrapper library that simplifies the process of establishing direct browser-to-browser connections. It will be used to implement the Peer-to-Peer (P2P) Multiplayer Framework by managing the generation of unique "Room Codes" and facilitating the data exchange between the host and connected clients. This library establishes direct connections between players without requiring a centralized backend server.

*C. Multimedia and Asset Development Tools*

*C.1 GIMP (GNU Image Manipulation Program)*

GIMP is a free, open-source raster graphics editor used for image retouching and editing. It will be utilized as the primary graphics editor for the manipulation of game assets. GIMP will be used in the asset creation phase to perform "Hue Shifting" on default enemy sprites because its color manipulation tools allow for the creation of biome-specific enemy variants (e.g., Sand Slime, Magma Slime) from a single base asset.

*C.2 Canva*

Canva is a web-based graphic design platform that provides templates and drag-and-drop tools for creating visual content. It will be utilized as the primary design tool for creating the Chronicles of Arithmos game logo and visual identity materials. during the design phase.

C.3 Draw.io

Draw.io also known as diagrams.net is a free, web-based diagramming application used for creating flowcharts, diagrams, and system architecture visuals. Draw.io will be used to create fundamental diagrams for the documentation of the system, which includes the Functional Decomposition Diagrams and Fishbone Diagram.

*D. Deployment and Runtime Platform*

*D.1 NW.js (Native Executable Wrapper)*

NW.js is an open source framework that allows HTML5 and JavaScript applications to run as native desktop programs. It will act as the main program to run the PC version. The proponents will use NW.js to pack the web game files into one executable file (.exe) for Windows. This wrapper gives the application direct access to local folders to store save files. Because of this, the game can run completely offline.

*D.2 Google Chrome / Microsoft Edge*

Google Chrome version 145 and Microsoft Edge version 145 are Chromium based web browsers. They run modern web tools like HTML5, WebGL, and WebRTC. These specific browser versions will act as the main programs to run the web based version of the project.

*D.3 GitHub*

GitHub is the cloud hub for Chronicles of Arithmos files and JavaScript scripts and is always partnered up with Git, since Git tracks every single code change. Proponents work on ATB timer files together without ruining each other progress. If an update breaks the math logic, the proponents return to a past version since the history stays.

*D.4 Git*

Git is a version control system where developers or people can track changes in their code during software making. The proponents use Git while building the game to save edits to the code. This tool lets the proponents send updated files from their own computers straight to the GitHub storage or repository.

*D.5 Vercel*

Vercel is the project’s temporary web host. The proponents will use it to test the game online before committing to a paid domain. Since it syncs directly with GitHub, every code update goes live automatically. Most importantly, it provides the HTTPS security required for the game’s P2P multiplayer (WebRTC and PeerJS) to actually connect.

*D.6 Hostinger*

Hostinger is a web hosting service that offer domains to be bought and cloud based hosting for web apps. It will act as the final live host for the game when it launches. This service will replace the Vercel testing setup during the final release.

### 3.1.3 Peopleware

*A. The Proponents*

The proponents consisted of a project manager, a programmer, a UI UX designer, a tester, and a graphic designer. Each person executed specific tasks to complete the system according to the agreed standards. The project manager oversaw the overall development schedule and guided the team workflow. The programmer wrote the game scripts. The UI UX designer planned the visual layouts. The tester conducted the multiplayer network checks and recorded software bugs during the trials. Finally, the graphic designer created some of the assets like the game logo.

1. *Capstone Adviser*

Mr. Jan Nicole B. Apostol provided guidance, clarifications, and recommendations for the project. The adviser guided the proponents through the technicalities and documentation, provided necessary revisions, and verified that the system met the required formatting and quality standards.

### 3.1.4 Network

*A. Local Area Network (LAN) & Cloud Staging*

The proponents will test the multiplayer mode using two different network setups during development. First, the team will check the peer to peer connection and game data sync. They will do this by connecting multiple computers to the same Local Area Network or Wi Fi to make sure the game runs without lag. Next, the proponents will test the game using computers on completely different networks to observe how the system handles a Wide Area Network. This secondary test will prove that the Room Code connection stays stable over the public internet.

## 3.2 Implementation

### 3.2.1 Hardware

*A. Personal Computer or Laptop*

Users need a personal computer desktop or laptop to download, install, and play the main application of Chronicles of Arithmos. These devices process the local game files. They also allow the player to control the game using a keyboard and a mouse.

*B. Mobile Device*

Users need a mobile phone or tablet running the Android or iOS platform to open a web browser and play the online version of the game. These devices connect to the internet to load the game pages. They allow the player to interact with the screen using touch controls.

### 3.2.2 Software

*A. Operating System (OS)*

The game requires Windows 10 64 bit or higher. The NW js wrapper depends on 64 bit architecture to function [9]. Older systems can not run this. Mobile devices need Android 10 or iOS 14 at a minimum. These versions are needed to fully support WebGL 2.0 rules [10]. This tool powers the 2D visuals of the game.

*B. Modern Browsers*

Players will need a modern web browser to play. The proponents recommend Google Chrome or Microsoft Edge. These browsers run the WebGL graphics and Virtual Keypad of the game very well. These Chromium based browsers also support the WebRTC rules. The P2P multiplayer needs these rules to connect.

### 3.2.3 Peopleware

*A. Young Learners and General Users*

Primary school students between 9 and 12 years old will act as the primary players of the game. However, the system accommodates all possible users regardless of age. Children below 9 years old can play the game using the early difficulty stages to learn basic addition and subtraction. Older students and individuals above 12 years old can also play the game for casual entertainment or to refresh their mental calculation speed. These learners will use the battle system to solve math problems while they explore different biomes such as the tundra biome and finish the main story. By playing, all users can practice their math skills and improve how they calculate numbers.

### 3.2.4 Network

*A. Internet Connection*

The system required a stable internet connection to function properly. A minimum of 5 to 10 Mbps internet speed will be needed for the multiplayer mode or to load the web files on the web app version.

# 4.0 Methodology

## 4.1 Prototyping Model

According to Geeks for Geeks the Prototyping Model is a branch of Software Development Life Cycle (SDLC). It is basically making a bare bones version before the final game. This helps when the proponents do not have a super detailed plan at the start. Proponents can just build a simple version to get feedback and fix the code logic before the final product [11].

**![PROTOTYPING-MODEL-NO-MAINTENANCE](data:image/png;base64...)**

Figure No. 7 : Prototyping Model

The proponents chose the Prototyping Model because mathematical pacing and battle balance require dynamic testing. Specific parameters, including timer countdown speeds and monster damage formulas, must be tested in real-time to maintain an appropriate difficulty level for learners. Unlike linear models like the Waterfall Model, the Prototyping Model allows proponents to adjust game balance based on actual gameplay feedback. To achieve this, the proponents executed a continuous prototyping cycle comprising quick design, prototype construction, customer evaluation, and prototype refinement before engineering the final production release.

The following are the phases of the Prototyping Model:

### 4.1.1 Requirements Gathering

In this phase, the proponents analyzed the Department of Education (DepEd) MATATAG curriculum for Grades 4 to 6 to define the educational scope, focusing on basic arithmetic operations and multi-step Order of Operations (PEMDAS) equations. Additionally, the proponents conducted a competitive analysis of Prodigy Math to benchmark functional game requirements. This phase concluded with a definitive document outlining the functional system specifications and necessary mathematical criteria for Chronicles of Arithmos.

### 4.1.2 Quick Design

In this phase, the proponents converted gathered requirements into tangible system blueprints and interface schematics. The proponents drafted navigation flowcharts, combat state transitions, and environmental storyboards across all four game regions: Forest, Desert, Tundra, and Volcano. Furthermore, the proponents designed user interface wireframes, including on-screen virtual numeric keypad layouts for mobile touchscreen gameplay.

### 4.1.3 Building Prototype

In this phase, the proponents translated design schematics into a functional game within the RPG Maker MZ engine through a continuous development process. The proponents first configured the development environment and monster attribute statistics. Next, the proponents wrote custom JavaScript plugins for the core Math Battle System, including procedural arithmetic generation and Performance-Based Reward multiplier logic. The proponents constructed the initial Forest starter map and integrated the Content-Aware Timer to dynamically adjust countdown durations based on equation complexity. To support mobile and tablet devices, the proponents developed and integrated the Virtual Numeric Keypad plugin for on-screen touch inputs. The proponents also scripted procedural side quest generation routines for non-player characters (NPCs). Following core plugin development, the proponents integrated the PeerJS to enable peer-to-peer multiplayer connections using room codes. The proponents then expanded the game world by constructing the Desert, Tundra, and Volcano biome maps. Throughout this construction phase, the proponents conducted internal alpha testing to verify system stability before advancing to customer evaluation.

### 4.1.4 Customer Evaluation of Prototype

In this phase, the proponents conducted customer evaluation through beta testing sessions with target learners. The proponents administered evaluation sessions with Grade 4 to 6 elementary students aged 9 to 12 years old. The participants played the fully integrated game across desktop and mobile web platforms. This evaluation allowed the proponents to assess user interface usability, on-screen keypad responsiveness, math battle engagement, and level difficulty scaling.

### 4.1.5 Refining Prototype

Following data collection from the customer evaluation sessions, the proponents refined the prototype based on feedback from the evaluation sessions. The proponents resolved reported defects and balanced gameplay difficulty.

### 4.1.6 Engineer Product

In the final phase, the proponents consolidated all verified and refined modules. The proponents compiled the game into a standalone desktop executable (.exe) using NW.js for offline use on Windows personal computers. Additionally, the proponents deployed the web application to the Hostinger hosting platform to provide online browser access across desktop and mobile devices.

## 4.2 Requirements Specification

### 4.2.1 Operational Feasibility

1. *Fishbone Diagram*

![FISHBONE_DIAGRAM](data:image/png;base64...)

Figure No. 8: Fishbone Diagram

1. *Functional Decomposition Diagram*

![](data:image/png;base64...)

Figure No. 9: Functional Decomposition Diagram

### 4.2.2 Technical Feasibility

4.2.2.1 Compatibility Checking

1. *Hardware Compatibility*

The proponents made the game with RPG Maker MZ. It runs on computers with assuming the computers have 8 GB of RAM and the proponents checked that an Intel Core i3 can handle it. Since there is a web version too, it works on tablets or any computer with a modern browser. This lets players jump into the math battles without downloading any executable files.

1. *Software Compatibility*

Since RPG Maker MZ runs on JavaScript, the math engine was built using that same language. This lets the math logic and the combat mechanics work together without needing any extra fixes or translations or conversion of code to another programming language. For the multiplayer part, the proponents used PeerJS so players can just use room codes to connect. This way, the game allows player to play without needing a server to run everything.

4.2.2.2 Relevance of the Technology

Prodigy and Math Blaster are basically a turn-based RPGs where math is the button the player presses to attack. Players get the answer right, the animation plays, and that’s it. It’s a bit disconnected. Chronicles of Arithmos actually ties your brain speed to the sword swing, in a sense, the player solving math is equivalent to a sword swing. Instead of just "Right = Hit," it uses a Performance-Based Reward system. If a player is really good ath math and accurate too, players can pull off a 2.0x Critical Hit. If the player is slow and stumble, the player might totally miss.

JavaScript (ES6) was chosen because it is the native scripting language of RPG Maker MZ, allowing the proponents to implement the Math Battle Engine and Content-Aware Timer without external dependencies. PeerJS, a WebRTC (Web Real-Time Communication) library, was selected for the multiplayer module as it enables direct Peer-to-Peer connections through room codes without requiring a dedicated server.

The proposed title deploys as a Windows desktop application via NW.js (Node Webkit) and as a web application hosted on Hostinger using HTML5 and Web Graphics Library (WebGL). Desktop is the primary platform because the Math Battle System requires timed numerical input through a physical keyboard, which touchscreens cannot replicate due to the absence of a physical key-press sensation (haptic feedback). The desktop executable can also operate offline using a computer. The web deployment serves as a secondary access point, supported by the Virtual Numeric Keypad module for touch-enabled devices.

### 4.2.3 Schedule Feasibility

1. *Gantt Chart*

Table #1 November 2025 Gantt Chart

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| 1. Capstone Orientation |  |  |  |  |
| 1. Grouping of Capstone Members |  |  |  |  |
| 1. Capstone Adviser Selection |  |  |  |  |
| Requirements Gathering | | | | |
| 1. Planning and Brainstorming |  |  |  |  |

Table #2 December 2025 Gantt Chart

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| Requirements Gathering | | | | |
| 1. DepEd MATATAG Curriculum Analysis & Arithmetic/PEMDAS |  |  |  |  |
| 1. Analysis of Prodigy Math Game |  |  |  |  |
| 1. Functional System Specifications (Chapter 1 Scope) |  |  |  |  |
| 1. Documentation (Chapter 1) |  |  |  |  |
| Quick Design | | | | |
| 1. System Navigation & Combat State Transistions |  |  |  |  |
| 1. User Interface (UI) Schematics & Interaction States |  |  |  |  |
| 1. Environmental Storyboarding & Spatial Pathing (Forest and Desert, Tundra, Volcano) |  |  |  |  |

Table #3 January 2026 Gantt Chart

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| Building Prototype | | | | |
| 1. RPG Maker MZ Environment & Monster Stats Configuration Setup |  |  |  |  |
| 1. Custom JS Math Plugin (Problem Gen & Multipliers) |  |  |  |  |
| 1. Starter Map Construction (Forest Region) |  |  |  |  |
| 1. Preparation for Title Defense |  |  |  |  |
| 1. Title Defense |  |  |  |  |
| 1. Capstone Adviser Consultation |  |  |  |  |
| 1. Revision of Documentation  (Chapter 1) |  |  |  |  |
| 1. Dean Consultation |  |  |  |  |

Table #4 February 2026 Gantt Chart

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| 1. Documentation (Chapter 2) |  |  |  |  |
| 1. Documentation (Chapter 3) |  |  |  |  |
| 1. Capstone Adviser Consultations |  |  |  |  |
| 1. Documentation (Chapter 4) |  |  |  |  |

Table #5 March 2026 Gantt Chart

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| 1. AI & Plagiarism Checking |  |  |  |  |
| 1. Preparation for Oral Defense |  |  |  |  |
| Building Prototype | | | | |
| 1. Virtual Numeric Keypad Plugin (Mobile Touch Input) |  |  |  |  |
| 1. Content-Aware Timer Integration |  |  |  |  |
| 1. PeerJS Multiplayer Integration |  |  |  |  |
| 1. Oral Defense |  |  |  |  |

Table #6 April 2026 Gantt Chart

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| 1. Revision of Documentation  (Chapter 1) |  |  |  |  |
| 1. Revision of Documentation  (Chapter 2) |  |  |  |  |
| 1. Capstone Adviser Consultation |  |  |  |  |
| Building Prototype | | | | |
| 1. Procedural Side Quest Generation Routines for NPCs |  |  |  |  |
| 1. Biome Maps Construction (Desert) |  |  |  |  |

Table #7 May 2026 Gantt Chart

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| Building Prototype | | | | |
| 1. Multi-Biome Maps Construction (Tundra, Volcano) |  |  |  |  |
| 1. Revision of Documentation  (Chapter 3) |  |  |  |  |
| 1. Capstone Adviser Consultation |  |  |  |  |
| 1. Revision of Documentation  (Chapter 4) |  |  |  |  |

Table #8 June 2026 Gantt Chart

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| 1. Revision of Activity Diagrams |  |  |  |  |
| 1. Capstone Adviser Consultation |  |  |  |  |
| 1. Revision of Sequence Diagrams |  |  |  |  |
| 1. Revision of Functional Decomposition Diagram |  |  |  |  |

Table #9 July 2026 Gantt Chart

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| 1. Program Specification Documentation |  |  |  |  |
| 1. Preparation of Unit Test Data  & Test Cases |  |  |  |  |

Table #10 August 2026 Gantt Chart

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| Building Prototype | | | | |
| 1. Unit Testing |  |  |  |  |
| 1. Integration Testing |  |  |  |  |
| Customer Evaluation | | | | |
| 1. Randomized Target Audience Beta Testing |  |  |  |  |
| 1. Usability & Difficulty Scaling Observational Evaluation |  |  |  |  |
| 1. Documentation Chapter 5 |  |  |  |  |

Table #11 September 2026 Gantt Chart

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| Refining Prototype | | | | |
| 1. Resolving Reported Defects & Source Code Bug Fixes |  |  |  |  |
| 1. Balancing Gameplay Difficulty Curves |  |  |  |  |
| 1. Virtual Numeric Keypad Mobile Button Adjustments |  |  |  |  |
| 1. Multiplayer Synchronization Bug Fixes |  |  |  |  |
| Engineer Product | | | | |
| 1. Finalizing the application |  |  |  |  |
| 1. Web Deployment & Compiled Build (.exe) |  |  |  |  |

### 4.2.4 Economic Feasibility

4.2.4.1 Cost and Benefit Analysis

The cost and benefit analysis provides a breakdown of the materials required for development and the specific value each item brings to the study. The proponents have categorized these costs into software and hosting, domain expenses.

Table #13 Cost and Benefits Table

|  |  |  |  |
| --- | --- | --- | --- |
| Category | Item | Cost | Benefits |
| Software | RPG Maker MZ (2 License) | ₱4,600.00 | Allows the proponents to develop and test the game concurrently, and provides a built-in event system, and map editor that can reduce the time needed to build the Active Time Battle (ATB) interface and Math Engine from scratch. |
| Hosting | Hostinger Domain & Web Hosting (4 years) | ₱9,133.60 | Allows students to either download the Windows executable or play via a web browser from home without requiring any software installation. |
| Total | Total Estimated Development Cost | ₱13,733.60 |  |

4.2.4.2 Cost Recovery Scheme

The proponents will distribute Chronicles of Arithmos for both web browsers and Windows desktops free to the public, allowing users and students to practice arithmetic skills without paying for access. To cover the development, web hosting and domain costs, the proponents will explore a Voluntary contribution or Pay what you want distribution model on itch.io, a prominent digital storefront for video games. This platform natively supports web browser games and desktop downloads. This setup allows players to download the base game for free while giving them the option to provide a voluntary financial contribution to the developers.

Furthermore, the proponents will explore to release an optional downloadable content package. This paid expansion will introduce new map areas and an infinite dungeon mode. In this specific mode, players can continuously explore endless floors and engage in combat, with the freedom to leave the dungeon and secure their loot at any given time.

### 4.2.5 Requirements Modeling

4.2.5.1 Object Modelling

1. *Use Case Diagrams*

![](data:image/png;base64...)

Figure No. 10: Player Use Case Diagrams

1. *Sequence Diagrams*

![Sequence Auto Quest.drawio (2)](data:image/png;base64...)

Figure No. 9: Auto Quest Sequence Diagram

![Sequence Enemy Auto-Scaling System.drawio](data:image/png;base64...)

Figure No. 10: Enemy Auto-Scaling Sequence Diagram

![Sequence Level-Based Progression System.drawio](data:image/png;base64...)

Figure No. 11: Level-Based Progression Sequence Diagram

![Sequence Math Battle System.drawio (2)](data:image/png;base64...)

Figure No. 12: Math Battle System Sequence Diagram

![Sequence P2P multiplayer.drawio (2)](data:image/png;base64...)

Figure No. 13: P2P Multiplayer Sequence Diagram

![Sequence Save.drawio (1)](data:image/png;base64...)

Figure No. 14: Save Sequence Diagram

1. *Activity Diagrams*

![](data:image/png;base64...)

Figure No. 15: Title Screen Module Activity Diagram

![](data:image/png;base64...)

Figure No. 16: Figure: Exploration, Main Menu and

Save Module Activity Diagram

![](data:image/png;base64...)

Figure No. 17: Enemy Auto-Scaling Module Activity Diagram

![](data:image/png;base64...)

Figure No. 18: Math Battle System Module Activity Diagram

![](data:image/png;base64...)

Figure 19: Level-Based Progression Module Activity Diagram

![](data:image/png;base64...)

Figure 20: Automatic Quest Generation Module Activity Diagram

![](data:image/png;base64...)

Figure 21: Peer-to-Peer (P2P) Multiplayer Module Activity Diagram

### 4.2.6 Risk Assessment/Analysis

Developing Chronicles of Arithmos comes with risks that the proponents have identified and prepared for. The proponents have limited experience with JavaScript and PeerJS, which may cause technical delays in building the Math Battle System and multiplayer features and differences between the desktop, web, and mobile versions may cause inconsistencies. The large project scope may lead to schedule delays, while players or young learners may lose interest if math overshadows the gameplay.

External dependencies such as PeerJS and NW.js may receive breaking updates, and students' computers may lack adequate hardware or internet access. To reduce these risks, the proponents will study online resources and consult the proponents Capstone Adviser for guidance, Mr. Jan Nicole B. Apostol, lock software versions during development, prioritize core features first with remaining items as stretch goals, review early prototypes for gameplay balance, offer an offline single-player option via windows executable application as a fallback when students are not playing via the web application.

## 4.3 Design

### 4.3.1 Output and User-interface Design

The proponents designed the interface for Chronicles of Arithmos using a 2D pixel art style for all game assets and entities. The color scheme uses deep blue (#005385) for menu outlines and for active buttons that are currently pressed. Black (#000000) serves as the background color for all buttons and menu windows. White (#FFFFFF) is used for all text, mathematical equations, and numerical values.

(Hex: #005385) (Hex: #000000) (Hex: #FFFFFF)

![C:/Users/Angel/Downloads/Documents/Frame 1.pngFrame 1](data:image/png;base64...)![](data:image/png;base64...)![C:/Users/Angel/Downloads/Documents/Frame 2.pngFrame 2](data:image/png;base64...)

Figure No. 16 : Dark Blue, Black and White

![coa-logo](data:image/png;base64...)

Figure No. 17 Chronicles of Arithmos Logo

The proponents chose the M+ 1m regular font as it is a typeface made for clear reading with uses that range from digital signs and multilingual systems, to computer screens and tools for writing code.

**![FONT-DESIGN-FIGURE](data:image/png;base64...)**

Figure No. 18: M+ 1m regular Font

### 4.3.2 Data Design

The data design of Chronicles of Arithmos utilizes simple structures to store and manage game information in a single system. This database handles the data for states, weapons, and save files to ensure smooth gameplay and accurate progress tracking. The states section stores the conditions, rules, and messages for buffs and debuffs applied during combat. The weapons section holds the statistics, purchase prices, and combat properties of equippable items used in battles. Furthermore, the save file section records the exact progress and inventory of the players. This includes tracking the current party level, accumulated gold, current map location, and total play time so that users can securely store their game data locally and resume their practice sessions at any time.

Database Design (see Table 17 on page C-1)

### 4.3.3 System Architecture

4.3.3.1 Network Model

The proponents included a peer to peer network model specifically for the multiplayer framework of the game. The main campaign and core math combat systems operate entirely offline and do not require internet connectivity.

4.3.3.1 Network Topology

Chronicles of Arithmos utilizes a decentralized peer to peer topology for the optional multiplayer mode. This allows the host device to connect directly to the client device without using a main central server. The core application operates independently on personal computers and web browsers of both mobile and windows, allowing users to access the educational content without continuous internet connectivity.

4.3.3.3 Security

The Chronicles of Arithmos application does not require account creation, personal information, or login credentials. The game is accessible for anyone who wishes to download the executable file or load the universal web link. All save files and progress data are stored directly on the local storage of the device to ensure user privacy is protected.

## 4.4 Development

### 4.4.1 Software Specification

Table # 14: System Information

|  |  |
| --- | --- |
| **Software** | **Description** |
| RPG Maker MZ | A game development engine used to create 2D role playing games, build the visual environment, and script game events. |
| HTML5 and WebGL | Tools used to run the web version of the game and display 2D graphics directly on internet browsers. |
| Cascading Style Sheets (CSS) | A style sheet language used to resize the game window and place the virtual keypad overlay. |
| JavaScript (ES6) | A programming language used to create custom plugins for the math battle system and multiplayer framework. |
| Visual Studio Code (v1.111) | The main coding tool used to write and manage the JavaScript game scripts. |
| Node js (v25.8.1) | A runtime environment used to simulate server operations and test the peer to peer connection logic. |
| PeerJS (v1.5.5) | A library used to handle the peer to peer multiplayer connections through room codes. |
| GIMP | A graphics editor used to manipulate game assets and create different colored enemy variants. |
| Canva | A graphic design platform used to create the game logo and visual identity materials. |
| Draw io | A diagramming application used to create flowcharts and system architecture visuals. |
| NW js | A framework used to pack the web game files into one executable file for Windows desktops. |
| Google Chrome and Microsoft Edge | Modern web browsers used to run the online version of the game and support the multiplayer connections. |
| GitHub and Git | Tools used to track code changes and store project files in the cloud. |
| Vercel | A temporary web host used to test the game online before the final release. |
| Hostinger | A web hosting service that will act as the final live host for the game. |

### 4.4.2 Hardware Specification

The following hardware requirements were used in the development of the system:

Table # 15: System Information

|  |  |
| --- | --- |
| Operating System | Windows 10 Pro 64-bit |
| System Manufacturer | Dell Inc. |
| System Model | OptiPlex 3010 |
| Processor | Intel(R) Core(TM) i3-3220 CPU @ 3.30GHz |
| Memory | 16384MB RAM |
| Page File | 17725MB used, 5982MB available |
| DirectX Version | DirectX12 |

### 4.4.3 Program Specification

Table #16: Program Specification

|  |
| --- |
| **Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat**  **System and Adaptive Difficulty Scaling.** |
| **Events:** |
| Initiate application when the game executable or web page is launched. |
| Display the Title Screen interface (New Game, Continue, Options, Quit Game). |
| Display the Options interface when options is selected. |
| Load local save file data when "Continue" is selected. |
| Exit application when the quit option is selected. |
|  |
| **Module:** Standard RPG Combat Mechanics & Math Battle System |
| **Purpose:** To manage core combat turns and replace chance-based attacks with direct mathematical challenges. |
| **Events:** |
| Fill character Action Gauges based on the Speed/Agility statistic. |
| Display the visual combat menu (Attack, Skills, Items) when an Action Gauge is full. |
| Track and update Health Points (HP), Mana Points (MP), and Tactical Points (TP) pools. |
| Display a generated math equation in an input window when a combat action is selected. |
| Accept numerical inputs via physical keyboard or virtual keypad. |
| Execute the combat action upon pressing the "Enter" or "Submit" key. |
|  |
| **Module:** Level-Based Difficulty System |
| **Purpose:** To automatically adjust the complexity and types of math equations based on the player's current level. |
| **Events:** |
| Fill character Action Gauges based on the Speed/Agility statistic. |
| Display the visual combat menu (Attack, Skills, Guard, Items) when an Action Gauge is full. |
| Track and update Health Points (HP), Mana Points (MP), and Tactical Points (TP) pools. |
| Display a generated math equation in an input window when a combat action is selected. |
| Accept numerical inputs via physical keyboard or virtual keypad. |
| Execute the combat action upon pressing the "Enter" or "Submit" key. |
|  |
| **Module:** Level-Based Difficulty System |
| **Purpose:** To automatically adjust the complexity and types of math equations based on the player's current level. |
| **Events:** |
| Generate addition and subtraction problems (two values) for player levels 1-29. |
| Introduce multiplication and division equations for player levels 30-69. |
| Generate three-part equations utilizing full PEMDAS rules for player levels 70-100. |
| Scale equations dynamically or provide fixed-level equations during Training Dummy practice sessions. |
|  |
| **Module:** "Content Aware" Timer System |
| **Purpose:** To dynamically calculate the time limit for answering equations based on their complexity. |
| **Events:** |
| Pause Time Progress Battle (TPB) action gauges the moment the math input window appears. |
| Calculate total time limit based on the number of digits and types of math operators used. |
| Display and update a visual countdown bar on the battle screen. |
| Mark the user's input as "slow" if the answer is submitted after the countdown hits zero. |
|  |
| **Module:** Enemy Auto Scaling System |
| **Purpose:** To balance map areas by dynamically scaling enemy stats to match the player's party level. |
| **Events:** |
| Calculate the average level of the player's party upon initiating a combat encounter. |
| Update the enemy's Health Points (HP) and Attack power (ATK) to match the party's level. |
| Update the Experience Points (EXP) and Gold rewards dropped by the enemy based on the scale. |
|  |
| **Module:** Performance Based Reward Mechanism |
| **Purpose:** To determine the effectiveness of combat actions based on the speed and accuracy of the player's math input. |
| **Events:** |
| Apply a 2.0x critical multiplier to the action's effect if the answer is correct and rapid. |
| Execute the action at its normal 1.0x base value if the answer is correct but slow. |
| Apply a 0.5x penalty to the action's effect if the answer is fast but wrong. |
| Nullify the action completely (move fails) if the answer is incorrect and slow. |
|  |
| **Module:** Automatic Quest Generation System |
| **Purpose:** To dynamically build side quests (hunting and gathering) without requiring manual mission design. |
| **Events:** |
| Scan the game database for monsters and items present within the maps the player has unlocked. |
| Display new generated quest options when the player interacts with Receptionist Mila. |
| Record the active task in the Quests tab if the player selects "Accept". |
| Remove the task and queue a new generation if the player selects "Reject". |
|  |
| **Module:** Peer-to-Peer (P2P) Multiplayer Framework |
| **Purpose:** To enable cooperative multiplayer gameplay via direct connections without a centralized server. |
| **Events:** |
| Display multiplayer options when the player interacts with Portal Keeper Alden. |
| Generate and display a unique text-based Room Code when "Host Room" is selected. |
| Prompt for text input when "Join Room" is selected. |
| Establish a direct connection and merge the joiner's party with the host's party upon code verification. |
|  |
| **Module:** Saving System |
| **Purpose:** To record and load the player's game progress using local files on the device. |
| **Events:** |
| Display 20 manual save slots when the Save screen is opened from the main menu. |
| Overwrite the selected manual slot with current game data upon user confirmation. |
| Trigger an automatic save overwrite to a dedicated slot when the character moves through map exits. |
|  |
| **Module:** Level-Based Progression System |
| **Purpose:** To track player growth, award resources, and unlock advanced game stages and story events. |
| **Events:** |
| Award Experience Points (EXP) and Gold (Currency) upon defeating enemies or completing quests. |
| Raise the character's level when the required EXP threshold is met. |
| Update Story Milestones to unlock higher-level maps, new biomes, and harder math stages. |
| **Module:** Mobile Input System (Virtual Numeric Keypad) |
| **Purpose:** To provide touchscreen support for mobile device users during math-based combat. |
| **Events:** |
| Detect if the application is running on a touch-enabled mobile device or tablet. |
| Display an on-screen Virtual Numeric Keypad next to the math input window during combat. |
| Submit the numerical answer to the Math Engine when the user taps the on-screen "Submit" button. |

### 4.4.4 Programming Environment

4.4.4.1 Front End

The proponents used RPG Maker MZ, HTML5, WebGL, and CSS as the front end for developing Chronicles of Arithmos. RPG Maker MZ and WebGL allowed cross platform 2D graphics rendering on both desktop and mobile web environments without third party plugins. It allowed the proponents to design an interactive combat menu and a virtual numeric keypad and standard touch event responsiveness across both computer desktop and mobile web browsers.

4.4.4.2 Back End

Since the core application is designed to function entirely offline, it does not require a traditional back end or an online database. All content including the math battle engine and interactive quests is built directly into the application, allowing players to access the game without an internet connection. However, the proponents used JavaScript and PeerJS to script the peer to peer multiplayer framework. This specific setup allows players to connect directly using room codes instead of relying on a central host server.

4.4.4.3 Programming Considerations and Issues

The proponents faced specific programming considerations regarding the math battle system. The main issue was ensuring the generated math equations scaled correctly with the character level without causing memory strain. Another consideration was standardizing the input methods to keep touch input latency within an acceptable threshold comparable to physical keyboard input. Finally, the proponents had to consider peer to peer connection stability, because a sudden disconnection from the host device would end the multiplayer session for everyone in the room.

### 4.4.5 Test Plan

After the development of Chronicles of Arithmos, the proponents worked on a testing plan that included Unit Testing, Compatibility Testing, Pacing Time Testing, Response Time Testing, Stress Testing, Alpha Testing and Beta Testing to ensure the quality and reliability of the application. The proponents conducted Unit Testing so that they can verify the functionality of each module. Compatibility Testing checked the application if it runs smoothly on different Windows computers and mobile web browsers. Pacing Time and Response Time Testing measured how quickly the application processed the user inputs and displayed results. Stress Testing evaluated the application stability under heavy usage, specifically focusing on the web server delivering game assets to concurrent users. Alpha Testing was performed by the proponents to help identify and fix bugs before release, while the Beta Testing involved selected users who provided real world feedback on the usability, performance, and learning effectiveness of the game. Through these tests, the proponents confirmed and identified that Chronicles of Arithmos delivers a stable and efficient platform for practicing mathematics through a role playing game.

## 4.5 Verification, Validation, Testing

### 4.5.1 Unit Testing

The proponents conducted a unit testing for Chronicles of Arithmos, and the modules successfully passed their test cases. Each part of the application was checked for functionality and stability to ensure it operates according to the program specifications. When launched, the application properly displayed the title screen and allowed users to quickly access the core game features or load their local save files. The Standard RPG Combat Mechanics and Math Battle System worked as expected, requiring users to solve generated math equations using a physical keyboard or virtual keypad to execute combat actions. The Level Based Difficulty System successfully adjusted the complexity of the math problems based on the current level of the character, while the Enemy Auto Scaling System updated the statistics of the monsters to match the party. Overall, the unit testing confirmed that Chronicles of Arithmos is functional, stable, and reliable as an educational tool for practicing arithmetic skills through a role playing game.

Unit Testing Result (see Table 28 on page E-3)

### 4.5.2 Integration Testing

4.5.2.1 Compatibility Testing

The Chronicles of Arithmos application was tested on multiple platforms including Windows personal computers, desktop web browsers, and mobile web browsers to ensure smooth functionality and consistent performance. For the desktop web environment, the application was tested on Microsoft Edge, Google Chrome, Opera GX, Mozilla FireFox, and Brave. For the Windows environment, it was evaluated on Windows 10 and Windows 11 operating systems using both desktop and laptop hardware. Finally, for the mobile web environment, the system was tested on various devices including a Redmi Note 10 5G, INFINIX HOT 30i, INFINIX NOTE 12, Iphone 15 pro max, and Galaxy A73 5G. The tests verified that the application launched properly, the user interface adjusted correctly to different screen resolutions, and all core modules like the peer to peer multiplayer framework and mobile input system functioned exactly as intended across all devices.

Compatibility Testing Result (see Table 29 on page E-7)

4.5.2.2 Stress Testing

The stress testing in Chronicles of Arithmos assessed the performance and stability of the system under high load conditions. This test evaluated the capacity of the web host when multiple users access the game at the same time. The proponents simulated 25 concurrent users requesting web assets over the internet. The test scenarios included the initial web page boot, the loading of battle graphics and enemy sprites during combat initialization, the fetching of background music during map transitions, and the continuous loading of user interface elements and the virtual numeric keypad. As a result, the web version of the application maintained consistent and reliable performance. All visual and audio assets loaded successfully without severe delays or crashes. The testing confirmed that the web host can handle heavy usage and continue to provide a stable educational platform for users.

Stress Testing Result (see Table 35 on page E-22)

4.5.2.3 Load Testing

Load testing is a process used to evaluate how an application performs when many users access it at the same time, usually in systems that depend on centralized servers and online connections. Because the main campaign of Chronicles of Arithmos is an offline application and the multiplayer framework uses a decentralized peer to peer network model, the system does not require a central server for simultaneous user access. Therefore, this type of testing is not applicable and will not be conducted for the project.

## 4.6 Acceptance Testing

The acceptance testing of the Chronicles of Arithmos application focused on ensuring that it met all specified requirements and functioned effectively for its intended users. This phase engaged with students who tested the application for the purpose of verifying that it offered the expected educational features including the dynamic math based combat and the adaptive difficulty scaling. The testing also examined the ease of use of the application and its performance across Windows computers and web browsers and also its capability to function offline. This successful completion of testing confirmed that the Chronicles of Arithmos application is ready for deployment meeting both technical standards and user expectations while delivering an engaging learning experience.

4.6.1 Alpha Testing

The proponents conducted alpha testing which allowed the proponents to closely examine the Chronicles of Arithmos application performance by simulating different user interactions across its modules. The primary objective of this phase was to identify and resolve the issues regarding functionality, usability, and interface design. During the alpha testing phase, the developers conducted activities such as navigating between the game menus, testing the math battle system, accepting quests, and also verifying the responsiveness of the virtual numeric keypad as well as checking the overall consistency of the interface.

4.6.2 Beta Testing

After the alpha testing phase the proponents conducted beta testing using the nearly final version of the Chronicles of Arithmos application. For this testing phase the proponents gathered the target audience including students and general users to play the game and provide their feedback. These selected users evaluated the usability, navigation, multimedia elements, and overall learning experience of the game. The proponents collected this feedback through a structured survey to determine the effectiveness of the application.

The tabulated survey results indicated an overall positive reception from the participants. A majority of the users strongly agreed that the game content is clear, the saving system is reliable, and the visual multimedia elements are appropriate. Furthermore, the survey data confirmed that the participants found Chronicles of Arithmos to be a user friendly application that is highly useful for practicing math equations and improving quick problem solving skills under a time limit.

Survey Result (see Table 36 on page E-21)

## 4.7 Implementation Plan

This section describes everything about how the system is to interact with its

environment. Included are the following kinds of items:

### 4.7.1 Physical Environment

The system is designed to function across several locations wherever the personal device of the user is present. The application requires no dedicated on premises server or specialized facility, operating directly on client endpoint devices. The application operates within standard client hardware operating conditions.

### 4.7.2 Interfaces

The input comes directly from the player and is not coming from other systems. The output is displayed directly on the screen and is not going to other systems. The data is formulated through numerical answers using a prescribed medium of a physical keyboard or virtual keypad.

### 4.7.3 Functionality

The system will operate as an educational role playing game that tests math skills. The system will do this whenever the player enters a combat encounter. The system can be enhanced by adding new map areas or harder math operators. There are constraints in execution speed because the player must answer equations before the dynamic time limit runs out.

### 4.7.4 Data

For the input, the format of the data must be exact numerical values. This data is received every time the player selects a combat action. Inputs are evaluated as exact integer matches against the dynamically generated solution for the attack to succeed. Save data is stored indefinitely in local browser local storage or indexed local file storage until manually cleared by the user.

### 4.7.5 Security

The application does not implement user authentication or role based access control for single player gameplay, while multiplayer access is restricted via randomized room codes. The data of one user will be isolated from others because the save files are stored locally on their personal device. It executes within the standard browser sandbox or NW js client environment without modifying external system registries or files. The system will be backed up locally whenever the player uses a manual save slot or triggers an automatic save.

## 4.8 Installation Processes

To access the application, a computer or mobile device with an internet connection must be used to open a web browser and either search for the website or enter its link directly. Additionally, the application can be downloaded and installed for offline use on Windows computers once the primary website has been accessed..

The following are the steps to access the web application:

1. The user must prepare a desktop computer, laptop, or mobile tablet connected to the internet.
2. Open a modern web browser such as Google Chrome, Mozilla Firefox, or Microsoft Edge.
3. Navigate to the primary website by entering "https://chroniclesofarithmos.site".
4. Click or tap the "Play in browser" button on the main page.
5. Allow the web browser to load the game canvas and start playing directly from the Title Screen.

The following are the steps to download and install the desktop application:

1. The user must prepare a desktop or laptop computer running Windows with an active internet connection.
2. Open a modern web browser such as Google Chrome, Mozilla Firefox, or Microsoft Edge.
3. Navigate to the primary website by entering "https://chroniclesofarithmos.site".
4. Click the "Download for PC" button located on the homepage.
5. Save and locate the downloaded ZIP package within the computer storage.
6. Right-click the ZIP archive and select "Extract All" to extract the game files into a local folder.
7. Open the extracted folder and double-click "ChroniclesofArithmos.exe" to launch the game.

# 5.0 Conclusion and Recommendations

## 5.1 Conclusion

The proponents conducted a survey with a total of 20 target participants, which included students, to evaluate the Chronicles of Arithmos application. The survey aimed to evaluate various aspects of the software, including the content, module design, multimedia elements, navigation, and overall usefulness.

* Content

A significant majority of the respondents found the content easy to understand at 100%, and 95% agreed that the overall text and presentation of the game are clear. Furthermore, 85% of the participants considered the application to be both informative and user friendly.

* Module

The core features achieved high satisfaction rates, with the Enemy Auto Scaling System, Automatic Quest Generation, and Multiplayer Framework all reaching 100% approval. Modules such as Standard RPG Combat Mechanics, Performance Reward Mechanism, and Mobile Input System followed closely at 95%, while the Level Difficulty System and Math Battle System scored 90% and 80% respectively.

* Multimedia Element

Respondents rated the appropriateness of font sizes, colors, and icons at a perfect 100%. The appropriateness of the font types, images, and buttons scored between 94% and 95%, demonstrating the visual appeal and functionality of the application.

* Navigation

The ease of navigation within the application was highly praised, with both moving between game menus and clarity of directions scoring 95%. The participants also confirmed that overall navigation is easy with a 90% positive rating.

* Usefulness

The utility of the application for practicing math equations and improving quick problem solving under a time limit was confirmed by 100% of respondents. Additionally, 85% of the participants agreed that the game is useful for offline entertainment.

## 5.2 Recommendations

After conducting an analysis and reviewing the findings, the proponents recommend the following improvements for the future enhancement of the project.

* Math Battle System

In the Math Battle System, the proponents recommend adding support for non integer results such as fractions and decimals. This addition will address current system limitations and provide advanced practice options for students who have mastered basic whole number arithmetic and want to test their skills on more complex equations.

* Automatic Quest Generation System

In the Automatic Quest Generation System, the proponents suggest expanding the variety of generated tasks. Adding specific math riddles or logic puzzles alongside the standard hunting and gathering missions will provide a richer educational experience.

* Performance Reward Mechanism

In the Performance Reward Mechanism, the proponents recommend introducing visual achievement badges or trophies. This addition will give learners or players a clearer sense of progression and further motivate them to consistently answer the math equations correctly and rapidly.

**REFERENCES:**

[1] Department of Education, "MATATAG Curriculum Overview and Guide," 2024. [Online]. Available: https://matatagcurriculum.ph/

[2] National Council for Childrens Television, "Study: Personal screens becoming the new classroom," Philippine Information Agency, 2025. [Online]. Available: https://pia.gov.ph/news/luzon/study-personal-screens-becoming-the-new-classroom/

[3] M. Engelhardt, "Feedback in Digital Game Based Learning: Influencing Student Self Efficacy and Motivation," VTechWorks, 2023. [Online]. Available: https://vtechworks.lib.vt.edu/

[4] P. Mozelius and L. M. Eberhardt, "The Chocolate Covered Broccoli Syndrome in Educational Games," Academic Conferences International, 2023. [Online]. Available: https://doi.org/10.34190/ecgbl.17.1.1344

[5] Y. F. Chen et al., "Assessing the Effects of Flow, Social Interaction, and Engagement on Students Gamified Learning," MDPI, 2023. [Online]. Available: https://www.mdpi.com/2071-1050/15/2/983

[6] K. Skagerlund et al., "Mathematics anxiety and emotion regulation," Taylor and Francis, 2024. [Online]. Available: https://www.tandfonline.com/doi/pdf/10.1080/00313831.2025.2559280

[7] A. Gokce and N. Guner, "Innovative Approaches to Mitigate Math Anxiety," MDPI, 2024. [Online]. Available: https://www.mdpi.com/2813-9844/7/2/46

[8] A. S. Maryana et al., "Using Gamified Learning Strategies to Enhance Problem Solving Performance in Mathematics," International Journal of Research and Innovation in Social Science, 2024. [Online]. Available: https://rsisinternational.org/journals/ijriss/uploads/vol9-iss11-pg3461-3480-202512\_pdf.pdf

[9] NW js Community, "NW js Downloads and Architecture Support," NW js Official Homepage, 2024. [Online]. Available: https://nwjs.io/

[10] Mozilla Developer Network, "WebGL2RenderingContext Browser Compatibility," MDN Web Docs, 2024. [Online]. Available: https://developer.mozilla.org/en-US/docs/Web/API/WebGL2RenderingContext#browser\_compatibility

[11] "Prototyping Model - Software Engineering," GeeksforGeeks, Jul. 11, 2025. [Online]. Available: https://www.geeksforgeeks.org/software-engineering/software-engineering-prototyping-model/

[AEKA2022] Aekashics (2022). 'Librarium Static Batch Megapack'. https://aekashics.itch.io/aekashics-librarium-librarium-static-batch-megapack

[COMS2020] Com\_Sho (2020). 'Com\_Sho MV RTP Tileset Pack'. https://forums.rpgmakerweb.com/threads/com\_sho-mv-rtp-tileset-pack.130647/

[GOTC2020] Gotcha Gotcha Games (2020). 'RPG Maker MZ'. https://www.rpgmakerweb.com/

[HIDD2015] hiddenone (2015). 'MV Generator Parts'. https://www.hiddenone-sprites.com/mv-generator-parts.html

[SOME2026] SomeNewWork (2026). 'RPG Maker MZ Generator Pack EX'. https://somenewwork.itch.io/rpg-maker-mz-generator-pack-ex

[WHTD2016a] whtdragon (2016). 'whtdragons tilesets addons fixes and more'. https://forums.rpgmakerweb.com/threads/whtdragons-tilesets-addons-fixes-and-more.60504/

[WHTD2016b] whtdragon (2016). 'whtdragons trees recolors'. https://forums.rpgmakerweb.com/threads/whtdragons-trees-recolors.49581/

[YANF2015] Yanfly (2015). 'Category:Yanfly Engine Plugins'. https://www.yanfly.moe/wiki/Category:Yanfly\_Engine\_Plugins#Terms\_of\_Use

Appendix A: Work Assignments

|  |  |
| --- | --- |
| **Title of the Project:** | Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling. |

|  |  |
| --- | --- |
| **Name of the Proponent:** | **Guevarra, John Angel D.** |
| **Project Participation:** | * Project Manager * Participated in Brain Storming * Participated in Documentation Chapter 1 * Participated in Documentation Chapter 2 * Participated in Documentation Chapter 3 * Participated in Documentation Chapter 4 * Participated in System Designing * Composed APPENDIX A * Composed APPENDIX D * Composed APPENDIX H * Composed APPENDIX I * Composed APPENDIX F |
| **Signature:** |  |

|  |  |
| --- | --- |
| **Name of the Proponent:** | **Lacsina, Justine C.** |
| **Project Participation:** | * Participated in Brain Storming * Participated in Documentation Chapter 2 * Participated in Documentation Chapter 3 * Participated in Documentation Chapter 4 * Composed APPENDIX B |
| **Signature:** |  |

|  |  |
| --- | --- |
| **Name of the Proponent:** | **Manalo, Allan Joshua C.** |
| **Project Participation:** | * Participated in Brain Storming * Participated in Documentation Chapter 2 * Participated in Documentation Chapter 4 |
| **Signature:** |  |

|  |  |
| --- | --- |
| **Name of the Proponent:** | **Panganiban, Justine T.** |
| **Project Participation:** | * Participated in Composing Fish Bone Diagram * Logo Design and Creation |
| **Signature:** |  |

|  |  |
| --- | --- |
| **Name of the Proponent:** | **Quinez, John Benedict D.** |
| **Project Participation:** | * Participated in Brain Storming * Composed Documentation Chapter 1 * Composed Documentation Chapter 3 * Participated in System Designing * Lead Programmer * Composed Sequence Diagrams * Composed Activity Diagrams * Composed Appendix G * Composed Appendix C * Composed Appendix J * Composed Appendix E |
| **Signature:** |  |

Appendix B: Definition of Terms

**Active Time Battle (ATB) Timer.** Refers to the combat pacing mechanism that fills an action gauge over time but pauses during math prompt generation to provide players dedicated calculation time without incoming damage.

**Adaptive Difficulty Scaling.** Refers to the game mechanic that dynamically adjusts math equation complexity, operator selection, and enemy combat attributes based on the player's character level and combat performance.

**Arithmetic Operations.** Refers to the mathematical computations generated during combat, including addition, subtraction, multiplication, division, and multi-step PEMDAS expressions tailored to Grade 4 to 6 learning competencies.

**Automatic Quest Generation System.** Refers to the algorithmic module that creates procedural side quests based on unlocked biomes and delivers in-game objectives through the non-player character Mila.

**Biome.** Refers to one of four distinct geographical regions in the game world (Plains and Forest, Desert, Tundra and Frost, and Volcano and Fire), each featuring region-specific enemy encounters and progression milestones.

**Content-Aware Timer System.** Refers to the calculation module that allocates an answering countdown proportional to the digit count, operator complexity, and calculation steps of a presented math equation.

**Enemy Auto-Scaling System.** Refers to the algorithm that recalculates enemy health, defense, attack stats, and experience rewards to match the player party's average character level.

**Experience Points (EXP).** Refers to the numerical score awarded to players upon completing math battles and quests, used to increase character level and unlock higher-tier arithmetic topics.

**Gold.** Refers to the in-game currency earned through battle victories and completed quests, used to purchase equipment, consumables, and recovery items from merchant shops.

**Health Points (HP).** Refers to the numerical resource measuring the remaining vitality of player characters and enemy units during combat encounters.

**JavaScript.** Refers to the primary scripting language used to create custom plugins, calculate math equation logic, control user interface elements, and manage multiplayer sockets in RPG Maker MZ.

**Magic Points (MP).** Refers to the consumable resource expended by characters to cast offensive, defensive, or healing spells during combat.

**Math Battle System.** Refers to the core combat loop where physical and magical attack execution is governed by solving dynamically generated arithmetic equations under time constraints.

**Math Engine.** Refers to the custom software module responsible for procedural arithmetic problem generation, input verification, timing calculations, and damage modifier outputs.

**Math Levels.** Refers to the curriculum-aligned difficulty tiers that govern equation types based on player level, progressing from basic addition and subtraction to multi-step PEMDAS problems.

**Non-Player Character (NPC).** Refers to computer-controlled characters within the game environment that provide quest dialogue, story exposition, gameplay guidance, and merchant services.

**Numeromancer.** Refers to the primary story antagonist and final boss entity representing mathematical chaos and corrupted arithmetic within the game narrative.

**NW.js.** Refers to the desktop application framework that packages the HTML5 and JavaScript game into a Windows executable capable of running without an active internet connection.

**PeerJS.** Refers to the JavaScript client library built on WebRTC that establishes peer connections and session coordination using alphanumeric room codes.

**Peer-to-Peer (P2P) Multiplayer.** Refers to the decentralized network architecture that connects two player instances directly for cooperative gameplay without routing battle data through a central server.

**PEMDAS.** Refers to the mathematical order of operations rule (Parentheses, Exponents, Multiplication, Division, Addition, Subtraction) implemented in advanced combat equations for high-level players.

**Performance-Based Reward System.** Refers to the evaluation mechanism that scales damage multipliers, critical hit rates, and combat rewards based on player calculation speed and answer accuracy.

**Pixel Art.** Refers to the 2D raster graphic art style used to render all character sprites, monster models, environment tilesets, and visual battle animations.

**Plains of Origin.** Refers to the initial starting region in the game where players learn basic movement, interface navigation, and introductory arithmetic battle mechanics.

**Progression System.** Refers to the state management module that tracks story quest milestones, unlocked map areas, earned achievements, and character level thresholds.

**Prototyping Model.** Refers to the iterative software development life cycle methodology utilized in the study, involving cyclical user feedback and refinement across repeated prototype phases.

**Role-Playing Game (RPG).** Refers to the game genre featuring character leveling, inventory management, narrative exploration, and turn-based tactical combat.

**Room Code.** Refers to a unique alphanumeric session identifier generated by the host player to allow a second player to join a multiplayer match via direct WebRTC signaling.

**RPG Maker MZ.** Refers to the game engine software used by the proponents to build map layouts, event triggers, database records, and baseline combat structures.

**Status Effects.** Refers to temporary positive or negative combat conditions, such as poison, stun, or stat buffs, that alter character performance for a set number of turns.

**Technical Points (TP).** Refers to tactical battle points generated during combat through successful answers or damage taken, used to activate specialized character skills.

**Training Dummy.** Refers to an invincible in-game practice target that allows players to test arithmetic response speed and damage output without risk of defeat.

**Training Hall.** Refers to a safe, non-combat zone located in towns where players can practice math calculations, review operational formulas, and test abilities.

**Vercel.** Refers to the cloud hosting platform used during development for automated preview deployments and web browser testing before production hosting.

**Virtual Numeric Keypad.** Refers to the on-screen touch and mouse input interface developed to facilitate numerical input across touch-enabled screens and web browsers without requiring a physical keyboard

**WebGL.** Refers to the JavaScript graphics API that renders 2D visual assets and animations using hardware-accelerated computer processing in modern web browsers.

**Web Real-Time Communication (WebRTC).** Refers to the browser standard protocol enabling real-time audio, video, and data communication directly between web browsers without intermediary proxy servers.

**Wireframe.** Refers to the schematic layout sketches used during the Quick Design phase to plan user interface structure, menu hierarchy, and button placement.

Appendix C: Database Design

Table #17: Actors Table Database Design

|  |  |  |
| --- | --- | --- |
| **Table Name:** Actors.json | | |
| **Purpose:** Stores the base information and starting setup for the playable characters. | | |
| **Field Name** | **Data Type** | **Example Value** |
| id | Integer | 1 |
| name | String | Garrick |
| classId | Integer | 1 |
| initialLevel | Integer | 1 |
| maxLevel | Integer | 99 |
| equips | Array | [4, 27, 51, 74, 0] |

Table #18: Animations Table Database Design

|  |  |  |
| --- | --- | --- |
| **Table Name:** Animations.json | | |
| **Purpose:** Stores the visual and sound settings for combat effects. | | |
| **Field Name** | **Data Type** | **Example Value** |
| id | Integer | 1 |
| name | String | Hit Physical |
| effectName | String | HitPhysical |
| displayType | Integer | 0 |
| scale | Integer | 50 |
| speed | Integer | 100 |
| soundTimings | Array | [{"frame":0, "se":{"name":"Blow1", "volume":90}}] |

Table #19: Armors Table Database Design

|  |  |  |
| --- | --- | --- |
| **Table Name:** Armors.json | | |
| **Purpose:** Stores the details and values of equipable armor and accessories. | | |
| **Field Name** | **Data Type** | **Example Value** |
| id | Integer | 2 |
| name | String | Ring of Life |
| description | String | Increases Hp, received healing and gives physical damage resistance. |
| etypeId | Integer | 5 |
| price | Integer | 5000 |
| params | Array | [0, 0, 0, 0, 0, 0, 0, 0] |

Table #20: Classes Table Database Design

|  |  |  |
| --- | --- | --- |
| **Table Name:** Classes.json | | |
| **Purpose:** Stores the base stats, experience curves, and skill learning progression for the character classes. | | |
| **Field Name** | **Data Type** | **Example Value** |
| id | Integer | 1 |
| name | String | Swordsman |
| expParams | Array | [30, 20, 30, 30] |
| traits | Array | [{"code":23, "dataId":0, "value":1}] |
| learnings | Array | [{"level":1, "skillId":173, "note":""}] |
| params | Array | [[1, 544, 618...], [0, 41, 50...]] |

Table #21: Enemies Table Database Design

|  |  |  |
| --- | --- | --- |
| **Table Name:** Enemies.json | | |
| **Purpose:** Stores the visual assets, battle stats, combat actions, and rewards for the monsters. | | |
| **Field Name** | **Data Type** | **Example Value** |
| id | Integer | 2 |
| name | String | Fairy |
| battlerName | String | Wind Fairy |
| exp | Integer | 12 |
| gold | Integer | 6 |
| params | Array | [15, 40, 6, 5, 15, 15, 20, 15] |
| actions | Array | [{"conditionType":0, "rating":5, "skillId":1}] |
| dropItems | Array | [{"kind":1, "dataId":32, "denominator":2}] |

Table #22: Items Table Database Design

|  |  |  |
| --- | --- | --- |
| **Table Name:** Items.json | | |
| **Purpose:** Stores the details, usage rules, and effects of all consumable objects and general items. | | |
| **Field Name** | **Data Type** | **Example Value** |
| id | Integer | 3 |
| name | String | Potion |
| description | String | Restores a small portion (25%) of an allys HP. |
| price | Integer | 50 |
| consumable | Boolean | TRUE |
| scope | Integer | 7 |
| damage | Object | {"critical":true, "formula":"b.mhp \* 0.25", "type":3} |

Table #23: Skills Table Database Design

|  |  |  |
| --- | --- | --- |
| **Table Name:** Skills.json | | |
| **Purpose:** Stores the combat actions, magic spells, resource costs, and damage formulas used by characters and enemies. | | |
| **Field Name** | **Data Type** | **Example Value** |
| id | Integer | 172 |
| name | String | Strong Attack |
| description | String | Performs a powerful attack on an enemy. (can crit) |
| tpCost | Integer | 15 |
| mpCost | Integer | 0 |
| scope | Integer | 1 |
| damage | Object | {"critical":true, "formula":"a.atk \* 6 - b.def \* 2", "type":1} |

Table #24: States Table Database Design

|  |  |  |
| --- | --- | --- |
| **Table Name:** States.json | | |
| **Purpose:** Stores the conditions, rules, and messages for all buffs and debuffs applied during combat. | | |
| **Field Name** | **Data Type** | **Example Value** |
| id | Integer | 4 |
| name | String | Poison |
| minTurns | Integer | 3 |
| maxTurns | Integer | 5 |
| removeAtBattleEnd | Boolean | FALSE |
| message1 | String | %1 is poisoned! |
| traits | Array | [{"code":22, "dataId":7, "value":-0.05}] |

Table #25: Weapons Table Database Design

|  |  |  |
| --- | --- | --- |
| **Table Name:** Weapons.json | | |
| **Purpose:** Stores the details, statistics, and combat properties of equippable weapons. | | |
| **Field Name** | **Data Type** | **Example Value** |
| id | Integer | 2 |
| name | String | Long Sword |
| description | String | A balanced steel blade for standard combat. |
| price | Integer | 150 |
| wtypeId | Integer | 2 |
| params | Array | [0, 0, 8, 0, 0, 0, 0, 0] |
| traits | Array | [{"code":31, "dataId":1, "value":0}] |

Table #26: Save File Data Table Database Design

|  |  |  |
| --- | --- | --- |
| **Table Name:** Save File Data | | |
| **Purpose:** Records the exact progress and inventory of the player. | | |
| **Field Name** | **Data Type** | **Example Value** |
| saveSlotId | Integer | 1 |
| partyLevel | Integer | 35 |
| currentGold | Integer | 1500 |
| currentMapId | Integer | 5 |
| playTime | String | 2:15:30 |
| saveSlotId | Integer | 1 |

Appendix D: Screen Design

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 1** |
| **Screen Name:** | Title Screen Interface |
| **Narrative Overview:** | The Title Screen serves as the primary gateway and initial landing interface for *Chronicles of Arithmos*. It displays the official game title banner centered against a high-contrast fantasy castle background featuring a holy sword embedded in stone under a vibrant sky. A centered modal command box with deep blue framing (#005385) and dark translucency provides the primary navigation options: **New Game** (initializes a fresh campaign session and opens the character naming workflow), **Continue** (opens the saved games browser to restore recorded progress), **Options** (navigates to system configuration), and **Exit** (closes the desktop executable). Users can interact via physical keyboard arrow keys with Z (confirm) and X (cancel), mouse clicks, or direct touchscreen taps. |
| **Screen Layout:** | **![1 Title Screen](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 2-1** |
| **Screen Name:** | System Options Menu (General & Audio Settings) |
| **Narrative Overview:** | The System Options Menu (Page 1) allows players to configure operational behaviors and audiovisual volumes to suit their local hardware environment. Rendered as a centered modal dialog with a blurred background overlay, this menu contains customizable toggles and sliders: **Always Dash** (toggles automatic party running in exploration maps), **Command Remember** (retains cursor position in combat submenus), **Touch UI** (enables or disables on-screen touch overlays and dedicated touch buttons for mobile/tablet devices), **Show HP Gauge** (toggles visual health bars above battlers during combat), **BGM Volume** (adjusts background music volume, set by default to 60%), **BGS Volume** (adjusts ambient background sound volume, set to 40%), and **ME Volume** (adjusts music effect stingers, set to 40%). A down arrow indicator signifies additional settings, a dedicated Back arrow button is anchored at the top-right corner for touch users, and a bottom hotkey bar indicates Z:Select and X:Back. |
| **Screen Layout:** | **![2 - 1 Options](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 2-2** |
| **Screen Name:** | System Options Menu (Sound Effect Setting) |
| **Narrative Overview:** | The System Options Menu (Page 2) provides granular acoustic adjustment for tactical sound effects. Scrolling down from the primary options menu reveals the **SE Volume** setting (configured to 40%). This control regulates the acoustic feedback for arithmetic inputs, countdown alert chimes, menu confirmations, critical hit sound cues, and monster damage impacts. Seamless real-time volume adjustments allow learners to maintain auditory clarity during classroom or home study sessions without external audio distortion. |
| **Screen Layout:** | **![2 - 2 Options](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 3** |
| **Screen Name:** | Continue and Load Game Interface |
| **Narrative Overview:** | The Continue and Load Game Interface allows players to retrieve and restore previously saved game states from local device storage without requiring network authentication. The top header displays the contextual query *"Which file would you like to load?"*. The selection list features a dedicated **Autosave** slot (automatically updated whenever the party transitions between regional map boundaries) alongside twenty manual save slots (e.g., **File 1**, **File 2**, **File 3**, **File 4**). Each populated slot presents rich metadata including thumbnail sprites of active party members (e.g., protagonist Alpha and companion Elara) and total accumulated playtime (e.g., 00:02:08 or 00:01:25). A scrollable vertical viewport accommodates all twenty save slots, while an on-screen return button and standard keyboard hotkeys (Z:Select, X:Back) provide intuitive navigation. |
| **Screen Layout:** | **![3 Continue or Load Screen](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 4** |
| **Screen Name:** | Protagonist Character Name Input Interface |
| **Narrative Overview:** | The Protagonist Character Name Input Interface is presented upon starting a new campaign, allowing learners to personalize their lead hero. The top card displays the animated 2D anime-style face portrait of the young swordsman protagonist alongside an editable text entry field with underline placeholders and an active typing cursor (defaulting to *"Alpha"*). The lower pane renders a comprehensive 9x8 virtual alphanumeric keyboard grid containing uppercase letters (A–Z), lowercase letters (a–z), numeric digits (0–9), punctuation, and arithmetic symbols (+, -, \*, /, =, @, ^). Dedicated functional buttons include **Page** (for character set cycling) and **OK** (for name confirmation). This interface provides full dual-input compatibility, accepting direct typing from physical keyboards as well as touch tap inputs on touchscreen tablets. |
| **Screen Layout:** | **![4 Name Input Screen](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 5** |
| **Screen Name:** | Overworld & Interior Exploration Environment |
| **Narrative Overview:** | The Overworld and Interior Exploration Environment displays the 2D top-down grid exploration perspective of *Chronicles of Arithmos*. The screen illustrates the detailed interior of the starting Adventurer Lodge / Headquarters rendered with custom pixel art tilesets. The layout features distinct architectural zones: a private hero bedroom (containing protagonist Alpha, a bed, desk with research books, mirror, potion shelf, and wardrobe), a tiled bathroom suite with a swimming bath and plumbing amenities, a spacious grand study with hardwood flooring, a stone hearth fireplace, a grandfather clock, floor-to-ceiling bookshelves, and a massive study table arranged with ancient scrolls, manuscripts, letters with wax seals, hourglasses, and an ink quill, as well as an adjoining kitchen area. Players navigate their avatar using physical directional keys (WASD / Arrows) or touch tap pathfinding. An anchored hamburger menu button at the top-right corner allows mobile users to open the main pause menu seamlessly without a keyboard Escape key. |
| **Screen Layout:** | **![5 Game Example](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 6** |
| **Screen Name:** | Title Screen Interface |
| **Narrative Overview:** | The Main System Pause Menu serves as the central operational hub for character growth, party management, and gameplay configuration during field exploration. Accessed via the Escape/X key or the top-right touch menu icon, the interface is split into structured functional panels over a darkened map backdrop. The left panel displays a summary card for active party members, featuring the character face portrait, name (*"Alpha"*), assigned class (*"Swordsman"*), character level (*"Lv 1"*), and real-time vital gauges for Health Points (HP 544), Magic Points (MP 41), and Tactical Points (TP 0). The right panel houses the vertical primary command list: **Item**, **Skill**, **Equip**, **Status**, **Formation**, **Quests**, **Options**, **Save**, and **Exit**. The bottom-right window tracks the player's accumulated Gold currency balance (G 0), while the bottom navigation bar displays action prompts (Z:Select, X:Back). |
| **Screen Layout:** | **![6 Pause Menu](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 7** |
| **Screen Name:** | Inventory & Item Management Menu |
| **Narrative Overview:** | The Inventory and Item Management Menu enables players to inspect, organize, and utilize consumable supplies, combat utilities, weapons, and protective armor. The top horizontal pane serves as a contextual help box that displays comprehensive item descriptions, recovery values, and operational effects. Directly beneath, an intuitive icon-driven category bar partitions the inventory into nine distinct classifications: **Field Items** (potion pouch icon), **Combat Consumables** (bomb icon), **Magical Recovery** (crystal orb icon), **Weapons** (sword icon), **Shields** (shield icon), **Headgear** (helmet icon), **Body Armor** (tunic icon), **Accessories** (ring icon), and **Key / Quest Items** (golden key icon). The lower split pane lists acquired items with numerical inventory counters. Players navigate between categories using << and >> hotkeys or touch swipe gestures, confirming selections with Z:Select and canceling via X:Back. |
| **Screen Layout:** | **![7 Items Menu](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 8** |
| **Screen Name:** | Character Skills & Abilities Management Menu |
| **Narrative Overview:** | The Character Skills and Abilities Management Menu allows players to review unlocked martial skills, tactical abilities, and class-specific spells. The top window displays contextual skill explanations detailing tactical damage output and status effects. The middle-left card displays active character data (portrait, name *"Alpha"*, class *"Swordsman"*, Lv 1, HP 544, MP 41, TP 0). The middle-right panel provides skill classification tabs (e.g., **Special**, **Magic**). The lower pane lists available techniques—such as the physical sword technique **Slash**—alongside its resource consumption cost (5 TP/MP) and custom skill icon. Players can cycle between party members using Q/W keyboard shortcuts or the top-left touch arrow buttons (< and >), allowing rapid review of full party arsenals. |
| **Screen Layout:** | **![8 Character Skills Menu](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 9** |
| **Screen Name:** | Character Equipment & Gear Configuration Menu |
| **Narrative Overview:** | The Character Equipment and Gear Configuration Menu governs the arming and defensive preparation of player characters. The top pane displays item descriptions and attribute modifiers for the selected piece of gear. The left panel shows the character portrait, name, class, vital gauges, and an eight-row combat parameter matrix: **Max HP** (544), **Max MP** (41), **Attack** (19), **Defense** (17), **M.Attack** (15), **M.Defense** (17), **Agility** (29), and **Luck** (27), with dynamic comparison arrows (->) that calculate projected stat gains or losses in real time. The right panel displays the five canonical equipment slots: **Weapon**, **Shield**, **Head**, **Body**, and **Accessory**, accompanied by an upper **Clear** button (allowing one-click unequipping of all gear). Controls include Shift (unequip current slot), Q/W (cycle active party member), Z:Select, and X:Back. |
| **Screen Layout:** | **![9 Character Equipment Menu](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 10** |
| **Screen Name:** | Character Status & Detailed Attributes Menu |
| **Narrative Overview:** | The Character Status and Detailed Attributes Menu provides an exhaustive breakdown of a character's developmental statistics, experience progression, and equipment loadout. The upper window presents the character portrait, full name (*"Alpha"*), class (*"Swordsman"*), level (*"Lv 1"*), vital resource meters (HP 544, MP 41, TP 0), **Current EXP** (0), and exact **To Next Level** numerical requirements (50). The middle-left panel displays core combat parameters (Attack 19, Defense 17, M.Attack 15, M.Defense 17, Agility 29, Luck 27). The middle-right panel lists currently equipped items across Weapon, Shield, Head, Body, and Accessory slots. The lower text container displays narrative lore, class background descriptions, and active passive traits. Party switching is supported via Q/W hotkeys or touch buttons (<, >). |
| **Screen Layout:** | **![10 Character Status Menu](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 11** |
| **Screen Name:** | Party Formation & Roster Arrangement Menu |
| **Narrative Overview:** | The Party Formation and Roster Arrangement Menu allows players to configure party combat lineups and reposition members between frontline and backline tactical roles. The left panel displays all active combatants with full status cards: lead swordsman **Alpha** (Lv 1 Swordsman, HP 544, MP 41, TP 0), elemental mage **Elara** (Lv 1 Sorcerer with wizard hat and sapphire hair, HP 297, MP 141, TP 0), and ranged tracker **Thorne** (Lv 1 Hunter with feathered cap and fur collar, HP 335, MP 70, TP 0). The right command panel highlights the active **Formation** mode. Selecting two character cards swaps their order in the battle queue, allowing learners to strategically position high-defense characters at the front while protecting specialized spellcasters. |
| **Screen Layout:** | **![11 - Formation Menu](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 12** |
| **Screen Name:** | Quests & Mission Log Interface |
| **Narrative Overview:** | The Quests and Mission Log Interface tracks active campaign progression and procedural bounty tasks generated by the Automatic Quest Generation System. Rendered as a centered two-tier parchment window, the top section (**MAIN STORY**) specifies the active narrative milestone—such as *"Go to the kitchen."*—guiding players through story-driven exploration and arithmetic dungeon progression. The bottom section (**ACTIVE COMMISSION**) tracks procedural hunting and gathering assignments accepted from Receptionist Mila (displaying *"No active commissions. (Visit an NPC to get work)"* when idle). This dual-structure log prevents task ambiguity and supports self-directed learning workflows. |
| **Screen Layout:** | **![12 Quests Menu](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 13** |
| **Screen Name:** | Game Save & Progress Recording Interface |
| **Narrative Overview:** | The Game Save and Progress Recording Interface enables players to record current game states, quest milestones, character levels, and inventory data into local device storage. The header prompt asks *"Which file would you like to save to?"*. The screen presents twenty manual save slots (**File 1** through **File 20**) in addition to the designated **Autosave** slot. Populated slots display miniature character sprites representing active party members alongside precise elapsed playtime timestamps (e.g., File 1 showing Alpha and companion at 00:01:25). Selecting a slot prompts an overwrite confirmation, ensuring safe data storage without server dependencies. The interface fully supports both keyboard controls (Z:Select, X:Back) and touchscreen taps. |
| **Screen Layout:** | **![13 Save Menu](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 14** |
| **Screen Name:** | Return to Title / Game Exit Confirmation Dialog |
| **Narrative Overview:** | The Return to Title and Game Exit Confirmation Dialog provides a protective confirmation modal when players select the Exit command from the main pause menu. Positioned in the center of the screen with deep blue borders and a semi-transparent dark fill, the dialog presents two clear choices: **To Title** (which terminates the active gameplay session and safely returns the player to the main Title Screen) and **Cancel** (which dismisses the modal dialog and returns focus to the Pause Menu). This modal prevents accidental loss of unsaved dungeon progress and ensures deliberate session termination. |
| **Screen Layout:** | **![14 Pause Menu Exit](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 15** |
| **Screen Name:** | Tactical Battle Command Menu - Page 1 (Primary Actions) |
| **Narrative Overview:** | The Tactical Battle Command Menu (Page 1) represents the core turn-based combat screen of *Chronicles of Arithmos* during an encounter in the Plains Biome. The visual battlefield displays enemy monsters on the left side (a flying Fairy/Wasp Archer and a green Slime, both with overhead real-time HP health bars and active status icons) and the player's animated battler sprite on the right (**Garrick**, a Lv 50 Swordsman). The lower-left combatant HUD card displays Garrick's portrait, name, HP (4,161), MP (468), TP (21), and an illuminated action gauge signaling ready command entry. The lower-right command window (Page 1) provides four primary combat commands: **Attack** (sword icon - executes a standard strike and triggers the Math Battle challenge), **Special** (flame icon - opens martial skill submenus), **Guard** (shield icon - reduces incoming damage), and **Item** (potion bottle icon - opens combat restorative items). A down arrow signals access to secondary system commands. |
| **Screen Layout:** | **![15 Battle Menu](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 16** |
| **Screen Name:** | Tactical Battle Command Menu - Page 2 (System & Tactical Actions) |
| **Narrative Overview:** | The Tactical Battle Command Menu (Page 2) provides secondary tactical options and combat system utilities. Scrolling down on the lower-right command menu reveals four additional options: **Fight** (sword slash icon - returns immediately to the primary combat actions on Page 1), **Status** (three stars icon - opens the real-time combatant inspection window), **Options** (gear icon - opens audio and visual settings mid-battle), and **Escape** (running boot icon - initiates a tactical retreat from non-boss encounters). The battlefield maintains full visibility of all enemy entities, active combatant health gauges, and character resource pools during menu transitions. |
| **Screen Layout:** | **![16 Battle Menu 2nd page](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 17** |
| **Screen Name:** | Battle Skills & Special Abilities Selection Submenu |
| **Narrative Overview:** | The Battle Skills and Special Abilities Selection Submenu opens when selecting the Special/Skill command during combat. The top contextual banner provides immediate explanatory feedback on the highlighted technique (e.g., *"Decreases the attack of an enemy"* for **Power Break**). The lower two-column skill matrix displays unlocked techniques alongside their TP/MP resource costs and skill type icons: **Strong Attack** (15 TP), **Slash** (5 TP), **Double Slash** (20 TP), **Armor Break** (20 TP), **Blade Bash** (20 TP), **Sonic Wave** (10 TP), **Wind Slash** (15 TP), and **Power Break** (20 TP). Selecting a skill freezes all Time Progress Battle (TPB) gauges and activates the Math Battle Engine, which generates an arithmetic equation aligned with character level (Levels 1–29 addition/subtraction, Levels 30–69 multiplication/division, Levels 70–100 PEMDAS) and applies performance multipliers (2.0x critical, 1.0x normal, 0.5x weak, 0x miss) based on calculation speed and accuracy. |
| **Screen Layout:** | **![17 Battle Menu Skills](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 18** |
| **Screen Name:** | Battle Consumables & Item Selection Submenu |
| **Narrative Overview:** | The Battle Consumables and Item Selection Submenu allows players to deploy restorative potions, mana elixirs, and status curatives during active combat encounters. The top help banner explains the exact curative function of the highlighted item (e.g., *"Cures a target of Blindness."* for **Eye Drops**). The lower two-column grid displays all available battle inventory with distinct item category icons, item names, **NEW!** tags indicating recent acquisitions, and remaining stock quantities (e.g., x90): **Potion**, **Hi-Potion**, **Full Potion**, **Magic Water**, **Hi-Magic Water**, **Elixir**, **Antidote**, and **Eye Drops**. Selecting a restorative item opens target ally selection, allowing players to heal wounds or cure ailments caused by enemy attacks. |
| **Screen Layout:** | **![18 Battle Menu Items](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 19** |
| **Screen Name:** | Combatant Tactical Status & Condition Submenu |
| **Narrative Overview:** | The Combatant Tactical Status and Condition Submenu enables players to inspect real-time character statistics, active buff modifiers, and status ailments during combat. Opened via the Status command on Page 2 of the battle menu, the top banner reports the general physical state (e.g., *"Status is currently normal."*). The upper inspection window displays the combatant portrait (**Garrick**), class (*"Swordsman"*), level (*"Lv 50"*), current HP (4,161), MP (468), TP (21), mini battler sprite, an active status badge (**Normal** with heart icon), and exact combat parameters: **Max HP** (4,161), **Max MP** (468), **Attack** (136), **Defense** (95), **M.Attack** (74), **M.Defense** (88), **Agility** (178), and **Luck** (180). Touch arrow buttons (< and >) allow cycling through all party members, empowering players to monitor status debuffs (Poison, Blind, Silence, Stun) and positive buffs (Haste, Protect, Shell) dynamically. |
| **Screen Layout:** | **![19 Battle Menu Status](data:image/png;base64...)** |

|  |  |
| --- | --- |
| **Screen No.:** | **Screen 20** |
| **Screen Name:** | Math Battle System & Mobile Virtual Numeric Keypad Interface |
| **Narrative Overview:** | The Math Battle System and Mobile Virtual Numeric Keypad Interface appears when a player selects a combat action on a touch device. The upper battle window displays the Content-Aware Timer bar, character level (Lv 1), and the arithmetic equation (such as 3 + 3 = ?). The lower area displays the Virtual Numeric Keypad. It contains number buttons (0 to 9), a minus key, a **DEL** key, and an **OK** button. The timer bar pauses while the player enters the answer. Fast and accurate answers give a 2.0x critical damage multiplier. Tapping **OK** submits the answer to the Math Engine to execute the combat action. |
| **Screen Layout:** | **![19 Battle Menu Status](data:image/png;base64...)** |

Appendix E: Evaluation Tools/ Test Documents and Test Results

**E.1 Test Data**

Table #27 Test Data

|  |
| --- |
| **Test Data for Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling** |
| **Test Data for Unit Test:** |
| Initiate application when the user launches the game executable or web page. |
| Display the Title Screen interface (New Game, Continue, Options, Quit). |
| Display the Options interface when the user selects Options. |
| Load local save file data when the user selects Continue. |
| Exit application when the user selects the quit option. |
|  |
| Module: Standard RPG Combat Mechanics and Math Battle System |
| **Events:** |
| Fill character Action Gauges based on the Speed/Agility statistic. |
| Display the visual combat menu (Attack, Skills, Items) when an Action Gauge is full. |
| Track and update Health Points (HP), Mana Points (MP), and Tactical Points (TP) pools. |
| Display a generated math equation in an input window when the user selects a combat action. |
| Accept numerical inputs when the user uses the physical keyboard or virtual keypad. |
| Execute the combat action when the user presses the Enter or Submit key. |
|  |
| **Module:** Level Based Difficulty System |
| **Events:** |
| Generate addition and subtraction problems (two values) for players levels 1 to 29. |
| Introduce multiplication and division equations for players levels 30 to 69. |
| Generate three part equations utilizing full PEMDAS rules for players levels 70 to 100. |
| Scale equations dynamically or provide fixed level equations during Training Dummy practice sessions. |
|  |
| **Module:** Content Aware Timer System |
| **Events:** |
| Pause Time Progress Battle (TPB) action gauges the moment the math input window appears. |
| Calculate total time limit based on the number of digits and types of math operators used. |
| Display and update a visual countdown bar on the battle screen. |
| Mark the users input as slow if the user submits the answer after the countdown hits zero. |
|  |
| **Module:** Enemy Auto Scaling System |
| **Events:** |
| Calculate the average level of the players party upon initiating a combat encounter. |
| Update the enemys Health Points (HP) and Attack power (ATK) to match the partys level. |
| Update the Experience Points (EXP) and Gold rewards dropped by the enemy based on the scale. |
|  |
| **Module:** Performance Based Reward Mechanism |
| **Events:** |
| Apply a 2.0x critical multiplier to the actions effect if the user answers correctly and rapidly. |
| Execute the action at its normal 1.0x base value if the user answers correctly but slowly. |
| Apply a 0.5x penalty to the actions effect if the user answers fast but wrong. |
| Nullify the action completely (move fails) if the user answers incorrectly and slowly. |
|  |
| **Module:** Automatic Quest Generation System |
| **Events:** |
| Scan the game database for monsters and items present within the maps the user has unlocked. |
| Display new generated quest options when the user interacts with Receptionist Mila. |
| Record the active task in the Quests tab if the user selects Accept. |
| Remove the task and queue a new generation if the user selects Reject. |
|  |
| **Module:** Peer to Peer Multiplayer Framework |
| **Events:** |
| Display multiplayer options when the user interacts with Portal Keeper Alden. |
| Generate and display a unique text based Room Code when the user selects Host Room. |
| Prompt for text input when the user selects Join Room. |
| Establish a direct connection and merge the joiners party with the hosts party upon code verification. |
|  |
| **Module:** Saving System |
| **Events:** |
| Display 20 manual save slots when the user opens the Save screen from the main menu. |
| Overwrite the selected manual slot with current game data when the user confirms. |
| Trigger an automatic save overwrite to a dedicated slot when the user moves the character through map exits. |
|  |
| **Module:** Level Based Progression System |
| **Events:** |
| Award Experience Points (EXP) and Gold (Currency) upon defeating enemies or completing quests. |
| Raise the characters level when the required EXP threshold is met. |
| Update Story Milestones to unlock higher level maps, new biomes, and harder math stages. |
| **Module:** Mobile Input System |
| **Events:** |
| Detect if the application is running on a touch enabled mobile device or tablet. |
| Display an on screen Virtual Numeric Keypad next to the math input window during combat. |
| Submit the numerical answer to the Math Engine when the user taps the on screen Submit button. |
| Detect if the application is running on a touch enabled mobile device or tablet. |
| Display an on screen Virtual Numeric Keypad next to the math input window during combat. |

**E.2 Unit Testing Results**

Table #28 Unit Testing Results

|  |  |  |
| --- | --- | --- |
| **Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling** | | |
| **Overall Result: Passed** | | |
|  | | |
| **Events:** | **Passed** | **Failed** |
|  | | |
| Initiate application when the user launches the game executable or web page. | Passed |  |
| Display the Title Screen interface (New Game, Continue, Options, Quit). | Passed |  |
| Display the Options interface when the user selects Options. | Passed |  |
| Load local save file data when the user selects Continue. | Passed |  |
| Exit application when the user selects the quit option. | Passed |  |
| **Module:** Standard RPG Combat Mechanics and Math Battle System | | |
| Fill character Action Gauges based on the Speed/Agility statistic. | Passed |  |
| Display the visual combat menu (Attack, Skills, Items) when an Action Gauge is full. | Passed |  |
| Track and update Health Points (HP), Mana Points (MP), and Tactical Points (TP) pools. | Passed |  |
| Display a generated math equation in an input window when the user selects a combat action. | Passed |  |
| Accept numerical inputs when the user uses the physical keyboard or virtual keypad. | Passed |  |
| Execute the combat action when the user presses the Enter or Submit key. | Passed |  |
| **Module:** Level Based Difficulty System | | |
| Generate addition and subtraction problems (two values) for players levels 1 to 29. | Passed |  |
| Introduce multiplication and division equations for players levels 30 to 69. | Passed |  |
| Generate three part equations utilizing full PEMDAS rules for players levels 70 to 100. | Passed |  |
| Scale equations dynamically or provide fixed level equations during Training Dummy practice sessions. | Passed |  |
| **Module:** Content Aware Timer System | | |
| Pause Time Progress Battle (TPB) action gauges the moment the math input window appears. | Passed |  |
| Calculate total time limit based on the number of digits and types of math operators used. | Passed |  |
| Display and update a visual countdown bar on the battle screen. | Passed |  |
| Mark the users input as slow if the user submits the answer after the countdown hits zero. | Passed |  |
| **Module:** Enemy Auto Scaling System | | |
| Calculate the average level of the players party upon initiating a combat encounter. | Passed |  |
| Update the enemys Health Points (HP) and Attack power (ATK) to match the partys level. | Passed |  |
| Update the Experience Points (EXP) and Gold rewards dropped by the enemy based on the scale. | Passed |  |
| **Module:** Performance Based Reward Mechanism | | |
| Apply a 2.0x critical multiplier to the actions effect if the user answers correctly and rapidly. | Passed |  |
| Execute the action at its normal 1.0x base value if the user answers correctly but slowly. | Passed |  |
| Apply a 0.5x penalty to the actions effect if the user answers fast but wrong. | Passed |  |
| Nullify the action completely (move fails) if the user answers incorrectly and slowly. | Passed |  |
| **Module:** Automatic Quest Generation System | | |
| Scan the game database for monsters and items present within the maps the user has unlocked. | Passed |  |
| Display new generated quest options when the user interacts with Receptionist Mila. | Passed |  |
| Record the active task in the Quests tab if the user selects Accept. | Passed |  |
| Remove the task and queue a new generation if the user selects Reject. | Passed |  |
| **Module:** Peer to Peer Multiplayer Framework | | |
| Display multiplayer options when the user interacts with Portal Keeper Alden. | Passed |  |
| Generate and display a unique text based Room Code when the user selects Host Room. | Passed |  |
| Prompt for text input when the user selects Join Room. | Passed |  |
| Establish a direct connection and merge the joiners party with the hosts party upon code verification. | Passed |  |
| **Module:** Saving System | | |
| Display 20 manual save slots when the user opens the Save screen from the main menu. | Passed |  |
| Overwrite the selected manual slot with current game data when the user confirms. | Passed |  |
| Trigger an automatic save overwrite to a dedicated slot when the user moves the character through map exits. | Passed |  |
| **Module:** Level Based Progression System | | |
| Award Experience Points (EXP) and Gold (Currency) upon defeating enemies or completing quests. | Passed |  |
| Raise the characters level when the required EXP threshold is met. | Passed |  |
| Update Story Milestones to unlock higher level maps, new biomes, and harder math stages. | Passed |  |
| **Module:** Mobile Input System | | |
| Detect if the application is running on a touch enabled mobile device or tablet. | Passed |  |
| Display an on screen Virtual Numeric Keypad next to the math input window during combat. | Passed |  |
| Submit the numerical answer to the Math Engine when the user taps the on screen Submit button. | Passed |  |

**E.3 Integration Testing Results**

E.3.1 Compatibility Test Result (Web Desktop)

Table #29 Compatibility Test Result (Web Desktop)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling** | | | | | |
|  | **Microsoft**  **Edge** | **Google**  **Chrome** | **Opera GX** | **Mozilla**  **FireFox** | **Brave** |
| **Events:** | **Passed/Failed** | **Passed/Failed** | **Passed/Failed** | **Passed/Failed** | **Passed/Failed** |
| Did the application launch properly? | Passed | Passed | Passed | Passed | Passed |
| Did the UI adjust correctly to the screen resolution? | Passed | Passed | Passed | Passed | Passed |
| Did the main menu display properly? | Passed | Passed | Passed | Passed | Passed |
| Did the animation work as expected? | Passed | Passed | Passed | Passed | Passed |
| Did all interactive buttons function correctly? | Passed | Passed | Passed | Passed | Passed |
| Did the Combat Mechanics Module function correctly? | Passed | Passed | Passed | Passed | Passed |
| Did the Level Based Difficulty System function correctly? | Passed | Passed | Passed | Passed | Passed |
| Did the Peer to Peer Multiplayer Framework function correctly? | Passed | Passed | Passed | Passed | Passed |

E.3.2 Compatibility Test Result (Windows)

Table #30 Compatibility Test Result (Windows)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling** | | | | |
|  | **Windows 10**  **Personal Computer** | **Windows 11**  **Personal Computer** | **Windows 10**  **Laptop** | **Windows 11**  **Laptop** |
| **Events:** | **Passed/Failed** | **Passed/Failed** | **Passed/Failed** | **Passed/Failed** |
| Did the application install properly? | Passed | Passed | Passed | Passed |
| Did the application launch properly? | Passed | Passed | Passed | Passed |
| Does the application run without the internet? | Passed | Passed | Passed | Passed |
| Did the UI adjust correctly to the screen resolution? | Passed | Passed | Passed | Passed |
| Did the main menu display properly? | Passed | Passed | Passed | Passed |
| Did the animation work as expected? | Passed | Passed | Passed | Passed |
| Did all interactive buttons function correctly? | Passed | Passed | Passed | Passed |
| Did the Combat Mechanics Module function correctly? | Passed | Passed | Passed | Passed |
| Did the Level Based Difficulty System function correctly? | Passed | Passed | Passed | Passed |
| Did the Peer to Peer Multiplayer Framework function correctly? | Passed | Passed | Passed | Passed |

E.3.3 Compatibility Test Result (Mobile Web)

Table #31 Compatibility Test Result (Mobile Web)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling** | | | | | |
|  | **Redmi Note 10 5G** | **INFINIX HOT 30i** | **INFINIX NOTE 12** | **Iphone 15 pro max** | **Oppo A52** |
| **Events:** | **Passed/Failed** | **Passed/Failed** | **Passed/Failed** | **Passed/Failed** | **Passed/Failed** |
| Did the application launch properly? | Passed | Passed | Passed | Passed | Passed |
| Did the UI adjust correctly to the screen resolution? | Passed | Passed | Passed | Passed | Passed |
| Did the main menu display properly? | Passed | Passed | Passed | Passed | Passed |
| Did the animation work as expected? | Passed | Passed | Passed | Passed | Passed |
| Did all interactive buttons function correctly? | Passed | Passed | Passed | Passed | Passed |
| Did the Combat Mechanics Module function correctly? | Passed | Passed | Passed | Passed | Passed |
| Did the Level Based Difficulty System function correctly? | Passed | Passed | Passed | Passed | Passed |
| Did the Mobile Input System function correctly? | Passed | Passed | Passed | Passed | Passed |
| Did the Peer to Peer Multiplayer Framework function correctly? | Passed | Passed | Passed | Passed | Passed |

E.3.4 Performance Test Result (Windows)

Table #32 Performance Test Result (Windows)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ***Module*** | ***Action*** | ***Concurrent Users*** | ***Pacing Time*** | ***Response Time*** |
| ***System Initialization*** |  |  |  |  |
|  | Initiate application when the game executable is launched. | - | 5 seconds | 5 seconds |
|  | Display the Title Screen interface (New Game, Continue, Options, Quit Game). | - | - | *7 seconds* |
|  | Display the Options interface when options is selected. | - | 3 seconds | 1 second |
|  | Load local save file data when Continue is selected. | - | 5 seconds | 1 second |
|  | Exit application when the quit option is selected. | - | 3 seconds |  |
| ***Standard RPG Combat Mechanics & Math Battle System*** |  |  |  |  |
|  | Fill character Action Gauges based on the Speed/Agility statistic. | - | - | *-* |
|  | Display the visual combat menu (Attack, Skills, Items) when an Action Gauge is full. | - | - | *-* |
|  | Track and update Health Points (HP), Mana Points (MP), and Tactical Points (TP) pools. | - | - | *-* |
|  | Display a generated math equation in an input window when a combat action is selected. | - | 3 seconds | 1 second |
|  | Accept numerical inputs via physical keyboard. | - | 5 seconds | *-* |
|  | Execute the combat action upon pressing the Enter or Submit key. |  | - | 1 second |
| ***Level Based Difficulty System*** |  |  |  |  |
|  | Generate addition and subtraction problems (two values) for player levels 1 to 29. | - | - | *-* |
|  | Introduce multiplication and division equations for player levels 30 to 69. | - | - | *-* |
|  | Generate three part equations utilizing full PEMDAS rules for player levels 70 to 100. | - | - | *-* |
|  | Scale equations dynamically or provide fixed level equations during Training Dummy practice sessions. | - | - | *-* |
| ***Content Aware Timer System*** |  |  |  |  |
|  | Pause Time Progress Battle (TPB) action gauges the moment the math input window appears. | - | - | *-* |
|  | Calculate total time limit based on the number of digits and types of math operators used. | - | - | *-* |
|  | Display and update a visual countdown bar on the battle screen. | - | - | *-* |
|  | Mark the users input as slow if the answer is submitted after the countdown hits zero. | - | 10 seconds | 5 seconds |
| ***Enemy Auto Scaling System*** |  |  |  |  |
|  | Calculate the average level of the players party upon initiating a combat encounter. | - | - | *-* |
|  | Update the enemys Health Points (HP) and Attack power (ATK) to match the partys level. | - | - | *-* |
|  | Update the Experience Points (EXP) and Gold rewards dropped by the enemy based on the scale. | - | - | *-* |
| ***Performance Based Reward Mechanism*** |  |  |  |  |
|  | Apply a 2.0x critical multiplier to the actions effect if the answer is correct and rapid. | - | 2 seconds | *-* |
|  | Execute the action at its normal 1.0x base value if the answer is correct but slow. | - | 4 seconds | *-* |
|  | Apply a 0.5x penalty to the actions effect if the answer is fast but wrong. | - | 2 seconds | *-* |
|  | Nullify the action completely (move fails) if the answer is incorrect and slow. | - | - | *-* |
| ***Automatic Quest Generation System*** |  |  |  |  |
|  | Scan the game database for monsters and items present within the maps the player has unlocked. | - | - | *-* |
|  | Display new generated quest options when the player interacts with Receptionist Mila. | - | 3 seconds | *-* |
|  | Record the active task in the Quests tab if the player selects Accept. | - | 5 seconds | *-* |
|  | Remove the task and queue a new generation if the player selects Reject. | - | 3 seconds | *-* |
| ***Peer to Peer (P2P) Multiplayer Framework*** |  |  |  |  |
|  | Scan the game database for monsters and items present within the maps the player has unlocked. | 2 | 3 seconds | *-* |
|  | Display new generated quest options when the player interacts with Receptionist Mila. | 2 | 5 seconds | *-* |
|  | Record the active task in the Quests tab if the player selects Accept. | 2 | 5 seconds | *-* |
|  | Remove the task and queue a new generation if the player selects Reject. | 2 | 10 seconds | *-* |
| ***Saving System*** |  |  |  |  |
|  | Display 20 manual save slots when the Save screen is opened from the main menu. | - | 3 seconds | 1 second |
|  | Overwrite the selected manual slot with current game data upon user confirmation. | - | 5 seconds | *-* |
|  | Trigger an automatic save overwrite to a dedicated slot when the character moves through map exits. | - | - | *-* |
| ***Level Based Progression System*** |  |  |  |  |
|  | Award Experience Points (EXP) and Gold (Currency) upon defeating enemies or completing quests. | - | 3 seconds | 1 second |
|  | Raise the characters level when the required EXP threshold is met. | - | - | *-* |
|  | Update Story Milestones to unlock higher level maps, new biomes, and harder math stages. | - | - | *-* |

E.3.5 Performance Test Result (Web Desktop)

Table #33 Performance Test Result (Web Desktop)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ***Module*** | ***Action*** | ***Concurrent Users*** | ***Pacing Time*** | ***Response Time*** |
| ***System Initialization*** |  |  |  |  |
|  | Initiate application when the web page is launched. | - | 5 seconds | 3 seconds |
|  | Display the Title Screen interface (New Game, Continue, Options, Quit Game). | - | - | *-* |
|  | Display the Options interface when options is selected. | - | 3 seconds | *-* |
|  | Load local save file data when Continue is selected. | - | 5 seconds | 1 second |
|  | Exit application when the quit option is selected. | - | 3 seconds | *-* |
| ***Standard RPG Combat Mechanics & Math Battle System*** |  |  |  |  |
|  | Fill character Action Gauges based on the Speed/Agility statistic. | - | - | *-* |
|  | Display the visual combat menu (Attack, Skills, Items) when an Action Gauge is full. | - | - | *-* |
|  | Track and update Health Points (HP), Mana Points (MP), and Tactical Points (TP) pools. | - | - | *-* |
|  | Display a generated math equation in an input window when a combat action is selected. | - | 3 seconds | *-* |
|  | Accept numerical inputs via physical keyboard. | - | 5 seconds | *-* |
|  | Execute the combat action upon pressing the Enter or Submit key. |  | - | *-* |
| ***Level Based Difficulty System*** |  |  |  |  |
|  | Generate addition and subtraction problems (two values) for player levels 1 to 29. | - | - | *-* |
|  | Introduce multiplication and division equations for player levels 30 to 69. | - | - | *-* |
|  | Generate three part equations utilizing full PEMDAS rules for player levels 70 to 100. | - | - | *-* |
|  | Scale equations dynamically or provide fixed level equations during Training Dummy practice sessions. | - | - | *-* |
| ***Content Aware Timer System*** |  |  |  |  |
|  | Pause Time Progress Battle (TPB) action gauges the moment the math input window appears. | - | - | *-* |
|  | Calculate total time limit based on the number of digits and types of math operators used. | - | - | *-* |
|  | Display and update a visual countdown bar on the battle screen. | - | - | *-* |
|  | Mark the users input as slow if the answer is submitted after the countdown hits zero. | - | 10 seconds | 5 seconds |
| ***Enemy Auto Scaling System*** |  |  |  |  |
|  | Calculate the average level of the players party upon initiating a combat encounter. | - | - | *-* |
|  | Update the enemys Health Points (HP) and Attack power (ATK) to match the partys level. | - | - | *-* |
|  | Update the Experience Points (EXP) and Gold rewards dropped by the enemy based on the scale. | - | - | *-* |
| ***Performance Based Reward Mechanism*** |  |  |  |  |
|  | Apply a 2.0x critical multiplier to the actions effect if the answer is correct and rapid. | - | 2 seconds | - |
|  | Execute the action at its normal 1.0x base value if the answer is correct but slow. | - | 4 seconds | - |
|  | Apply a 0.5x penalty to the actions effect if the answer is fast but wrong. | - | 2 seconds | - |
|  | Nullify the action completely (move fails) if the answer is incorrect and slow. | - | - | - |
| ***Automatic Quest Generation System*** |  |  |  |  |
|  | Scan the game database for monsters and items present within the maps the player has unlocked. | - | - | - |
|  | Display new generated quest options when the player interacts with Receptionist Mila. | - | 3 seconds | - |
|  | Record the active task in the Quests tab if the player selects Accept. | - | 5 seconds | - |
|  | Remove the task and queue a new generation if the player selects Reject. | - | 3 seconds | - |
| ***Peer to Peer (P2P) Multiplayer Framework*** |  |  |  |  |
|  | Scan the game database for monsters and items present within the maps the player has unlocked. | 2 | 3 seconds | *-* |
|  | Display new generated quest options when the player interacts with Receptionist Mila. | 2 | 5 seconds | *-* |
|  | Record the active task in the Quests tab if the player selects Accept. | 2 | 5 seconds | *-* |
|  | Remove the task and queue a new generation if the player selects Reject. | 2 | 10 seconds | *-* |
| ***Saving System*** |  |  |  |  |
|  | Display 20 manual save slots when the Save screen is opened from the main menu. | - | 3 seconds | *-* |
|  | Overwrite the selected manual slot with current game data upon user confirmation. | - | 5 seconds | *-* |
|  | Trigger an automatic save overwrite to a dedicated slot when the character moves through map exits. | - | - | *-* |
| ***Level Based Progression System*** |  |  |  |  |
|  | Award Experience Points (EXP) and Gold (Currency) upon defeating enemies or completing quests. | - | 3 seconds | 1 second |
|  | Raise the characters level when the required EXP threshold is met. | - | - | *-* |
|  | Update Story Milestones to unlock higher level maps, new biomes, and harder math stages. | - | - | *-* |

E.3.6 Performance Test Result (Web Mobile)

Table #34 Performance Test Result (Web Mobile)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ***Module*** | ***Action*** | ***Concurrent Users*** | ***Pacing Time*** | ***Response Time*** |
| ***System Initialization*** |  |  |  |  |
|  | Initiate application when the web page is launched. | - | 5 seconds | 6 second |
|  | Display the Title Screen interface (New Game, Continue, Options, Quit Game). | - | - | *-* |
|  | Display the Options interface when options is selected. | - | 3 seconds | 1 second |
|  | Load local save file data when Continue is selected. | - | 5 seconds | 3 seconds |
|  | Exit application when the quit option is selected. | - | 3 seconds | 1 second |
| ***Standard RPG Combat Mechanics & Math Battle System*** |  |  |  |  |
|  | Fill character Action Gauges based on the Speed/Agility statistic. | - | - | *-* |
|  | Display the visual combat menu (Attack, Skills, Items) when an Action Gauge is full. | - | - | *-* |
|  | Track and update Health Points (HP), Mana Points (MP), and Tactical Points (TP) pools. | - | - | *-* |
|  | Display a generated math equation in an input window when a combat action is selected. | - | 3 seconds | 1 second |
|  | Accept numerical inputs via virtual keypad. | - | 5 seconds | *-* |
|  | Execute the combat action upon pressing the Submit key. |  | - | *-* |
| ***Level Based Difficulty System*** |  |  |  |  |
|  | Generate addition and subtraction problems (two values) for player levels 1 to 29. | - | - | *-* |
|  | Introduce multiplication and division equations for player levels 30 to 69. | - | - | *-* |
|  | Generate three part equations utilizing full PEMDAS rules for player levels 70 to 100. | - | - | *-* |
|  | Scale equations dynamically or provide fixed level equations during Training Dummy practice sessions. | - | - | *-* |
| ***Content Aware Timer System*** |  |  |  |  |
|  | Pause Time Progress Battle (TPB) action gauges the moment the math input window appears. | - | - | *-* |
|  | Calculate total time limit based on the number of digits and types of math operators used. | - | - | *-* |
|  | Display and update a visual countdown bar on the battle screen. | - | - | *-* |
|  | Mark the users input as slow if the answer is submitted after the countdown hits zero. | - | 10 seconds | *-* |
| ***Enemy Auto Scaling System*** |  |  |  |  |
|  | Calculate the average level of the players party upon initiating a combat encounter. | - | - | *-* |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Update the enemys Health Points (HP) and Attack power (ATK) to match the partys level. | - | - | - |
|  | Update the Experience Points (EXP) and Gold rewards dropped by the enemy based on the scale. | - | - | - |
| ***Performance Based Reward Mechanism*** |  |  |  |  |
|  | Apply a 2.0x critical multiplier to the actions effect if the answer is correct and rapid. | - | - | - |
|  | Execute the action at its normal 1.0x base value if the answer is correct but slow. | - | - | - |
|  | Apply a 0.5x penalty to the actions effect if the answer is fast but wrong. | - | - | - |
|  | Nullify the action completely (move fails) if the answer is incorrect and slow. | - | - | - |
| ***Automatic Quest Generation System*** |  |  |  |  |
|  | Scan the game database for monsters and items present within the maps the player has unlocked. | - | - | - |
|  | Display new generated quest options when the player interacts with Receptionist Mila. | - | 3 seconds | - |
|  | Record the active task in the Quests tab if the player selects Accept. | - | 5 seconds | - |
|  | Remove the task and queue a new generation if the player selects Reject. | - | 3 seconds | - |
| ***Peer to Peer (P2P) Multiplayer Framework*** |  |  |  |  |
|  | Scan the game database for monsters and items present within the maps the player has unlocked. | 2 | 3 seconds | - |
|  | Display new generated quest options when the player interacts with Receptionist Mila. | 2 | 5 seconds | - |
|  | Record the active task in the Quests tab if the player selects Accept. | 2 | 5 seconds | - |
|  | Remove the task and queue a new generation if the player selects Reject. | 2 | 10 seconds | - |
| ***Saving System*** |  |  |  |  |
|  | Display 20 manual save slots when the Save screen is opened from the main menu. | - | 3 seconds | *-* |
|  | Overwrite the selected manual slot with current game data upon user confirmation. | - | 5 seconds | *-* |
|  | Trigger an automatic save overwrite to a dedicated slot when the character moves through map exits. | - | - | *-* |
| ***Level Based Progression System*** |  |  |  |  |
|  | Award Experience Points (EXP) and Gold (Currency) upon defeating enemies or completing quests. | - | 3 seconds | - |
|  | Raise the characters level when the required EXP threshold is met. | - | - | - |
|  | Update Story Milestones to unlock higher level maps, new biomes, and harder math stages. | - | - | - |
| ***Mobile Input System (Virtual Numeric Keypad)*** |  |  |  |  |
|  | Detect if the application is running on a touch enabled mobile device or tablet. | - | - | - |
|  | Display an on screen Virtual Numeric Keypad next to the math input window during combat. | - | - | - |
|  | Submit the numerical answer to the Math Engine when the user taps the on screen Submit button. | - | 5 seconds | - |

E.3.7 Stress Testing Result

Table #35 Stress Testing Result

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Module** | **Test Scenario** | **Concurrent Users** | **Average Response Time** | **Expected Result** |
| Web Asset Delivery | Initial web page boot and registration of the service worker | 25 | 2 seconds | System performs normally and begins the initial setup process |
| Web Asset Delivery | Sequential downloading and caching of all game assets for offline play | 25 | 150 seconds | System successfully downloads over 1000 files. Server remains stable because the service worker requests files one by one |
| Web Asset Delivery | Loading the game title screen after the initial cache is complete | 25 | 1 second | Game launches immediately using local device storage |
| Web Asset Delivery | Verifying the service worker cache upon opening the application again | 25 | 2 seconds | System quickly checks for updates then loads the game. Players can turn off their wifi and continue playing without issues |

**E.4 Acceptance Testing Results**

Table #36 Acceptance Testing Result

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Items** | **1**  Strongly Disagree | **2**  Somewhat Disagree | **3**  Disagree | **4**  Agree | **5**  Somewhat Agree | **6**  Strongly Agree |
| **Content** |  |  |  |  |  |  |
| The content of Chronicles of Arithmos is clear | 0 (0%) | 0 (0%) | 1 (5%) | 8 (40%) | 4 (20%) | 7 (35%) |
| The content of Chronicles of Arithmos is easy to understand | 0 (0%) | 0 (0%) | 0 (0%) | 11 (55%) | 5 (25%) | 4 (20%) |
| The content of Chronicles of Arithmos is informative and interesting | 0 (0%) | 0 (0%) | 3 (15%) | 8 (40%) | 6 (30%) | 3 (15%) |
| The content of Chronicles of Arithmos is user friendly | 0 (0%) | 0 (0%) | 3 (15%) | 11 (55%) | 1 (5%) | 5 (25%) |
| **Module** |  |  |  |  |  |  |
| Standard RPG Combat Mechanics | 0 (0%) | 0 (0%) | 1 (5%) | 8 (42%) | 5 (26%) | 5 (26%) |
| Math Battle System | 0 (0%) | 0 (0%) | 4 (20%) | 9 (45%) | 2 (10%) | 5 (25%) |
| Level Difficulty System | 0 (0%) | 0 (0%) | 2 (10%) | 10 (50%) | 6 (30%) | 2 (10%) |
| Content Aware Timer System | 0 (0%) | 0 (0%) | 2 (12%) | 7 (41%) | 4 (24%) | 4 (24%) |
| Enemy Auto Scaling System | 0 (0%) | 0 (0%) | 0 (0%) | 10 (53%) | 5 (26%) | 4 (21%) |
| Performance Reward Mechanism | 0 (0%) | 0 (0%) | 1 (5%) | 8 (40%) | 6 (30%) | 5 (25%) |
| Automatic Quest Generation | 0 (0%) | 0 (0%) | 0 (0%) | 9 (47%) | 8 (42%) | 2 (11%) |
| Multiplayer Framework | 0 (0%) | 0 (0%) | 0 (0%) | 9 (50%) | 6 (33%) | 3 (17%) |
| Saving System | 0 (0%) | 0 (0%) | 2 (10%) | 9 (45%) | 3 (15%) | 6 (30%) |
| Mobile Input System | 0 (0%) | 0 (0%) | 1 (5%) | 12 (60%) | 3 (15%) | 4 (20%) |
| **Multimedia Element** |  |  |  |  |  |  |
| Appropriate font type | 0 (0%) | 0 (0%) | 1 (6%) | 10 (56%) | 1 (6%) | 6 (33%) |
| Appropriate font size | 0 (0%) | 0 (0%) | 0 (0%) | 11 (55%) | 5 (25%) | 4 (20%) |
| Appropriate images | 0 (0%) | 0 (0%) | 1 (5%) | 8 (40%) | 5 (25%) | 6 (30%) |
| Appropriate colors | 0 (0%) | 0 (0%) | 0 (0%) | 8 (40%) | 8 (40%) | 4 (20%) |
| Appropriate icons | 0 (0%) | 0 (0%) | 0 (0%) | 12 (63%) | 3 (16%) | 4 (21%) |
| Appropriate button | 0 (0%) | 0 (0%) | 1 (5%) | 11 (55%) | 3 (15%) | 5 (25%) |
| **Navigation** |  |  |  |  |  |  |
| Navigation is easy | 0 (0%) | 0 (0%) | 2 (10%) | 8 (40%) | 6 (30%) | 4 (20%) |
| Navigation is clear and concise | 0 (0%) | 0 (0%) | 1 (5%) | 11 (55%) | 5 (25%) | 3 (15%) |
| Moving between game menus is simple | 0 (0%) | 0 (0%) | 1 (5%) | 12 (60%) | 2 (10%) | 5 (25%) |
| **Usefulness** |  |  |  |  |  |  |
| Chronicles of Arithmos is useful for practicing math equations | 0 (0%) | 0 (0%) | 0 (0%) | 11 (58%) | 5 (26%) | 3 (16%) |
| Chronicles of Arithmos is useful for offline entertainment | 0 (0%) | 0 (0%) | 3 (15%) | 9 (45%) | 4 (20%) | 4 (20%) |
| Chronicles of Arithmos is useful for improving quick problem solving under a time limit | 0 (0%) | 0 (0%) | 0 (0%) | 12 (60%) | 4 (20%) | 4 (20%) |

![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)

Figure No. 19: Survey Result - Content Evaluation

![](data:image/png;base64...)![](data:image/png;base64...)

Figure No. 20: Survey Result - Demographics

![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)

![](data:image/png;base64...)

![](data:image/png;base64...)

![](data:image/png;base64...)![](data:image/png;base64...)

![](data:image/png;base64...)![](data:image/png;base64...)

Figure No. 21: Survey Result - Module Evaluation

![](data:image/png;base64...)![](data:image/png;base64...)

![](data:image/png;base64...)![](data:image/png;base64...)

![](data:image/png;base64...)![](data:image/png;base64...)

Figure No. 22: Survey Result – Multimedia Elements

![](data:image/png;base64...)

![](data:image/png;base64...)

![](data:image/png;base64...)

Figure No. 23: Survey Result – Navigation

![](data:image/png;base64...)

![](data:image/png;base64...)

![](data:image/png;base64...)

Figure No. 24: Survey Result – Usefulness

**![image 22](data:image/png;base64...)![p1-blur](data:image/png;base64...)**

**![20260823_170719](data:image/jpeg;base64...)**

**![20260823_170034](data:image/jpeg;base64...)**

**![20260823_171809](data:image/jpeg;base64...)![20260823_165415](data:image/jpeg;base64...)**

**![IMG_20260823_164518](data:image/jpeg;base64...)**

**![Screenshot 2026-08-23 215500](data:image/png;base64...)**

Figure No. 25: Beta Testing Session

1Appendix F: Certifications and Letters

**F.1** **Endorsement Letter/Certificate of Interview**

![](data:image/jpeg;base64...)

Figure No. 26: Endorsement Letter

Appendix G: Program Listings

**Module Name: Math Battle System**

Purpose: To manage core combat turns and replace chance based attacks with direct mathematical challenges.

const \_BattleManager\_invokeAction = BattleManager.invokeAction;

BattleManager.invokeAction = function(subject, target) {

if (subject.isActor() && this.\_action.\_mathProcessed) {

\_BattleManager\_invokeAction.call(this, subject, target);

return;

}

if (subject.isActor() && !this.\_action.isGuard() && !subject.\_mathSolvedForThisTurn) {

this.\_action.\_mathProcessed = true;

MathSystem.isMathPaused = true;

let mathLevel = subject.level;

if ($gameVariables.value(50) > 0) {

mathLevel = $gameVariables.value(50);

}

MathSystem.currentActorLevel = mathLevel;

const problem = MathSystem.generateProblem(mathLevel);

SceneManager.\_scene.startMathChallenge(problem, (result) => {

// (Reward Logic Handled in Performance Reward Module)

subject.\_mathSolvedForThisTurn = true;

setTimeout(() => {

MathSystem.isMathPaused = false;

\_BattleManager\_invokeAction.call(this, subject, target);

}, 600);

});

} else {

\_BattleManager\_invokeAction.call(this, subject, target);

}

};

**Module Name: Level Based Difficulty System**

Purpose: To automatically adjust the complexity and types of math equations based on the players current level.

generateProblem: function(level) {

let isValid = false;

let problemData = {};

let safetyCount = 0;

while (!isValid && safetyCount < 300) {

safetyCount++;

let visualStr = "";

let formulaStr = "";

let numTerms = 2;

let operatorsPool = ['+', '-'];

let useParens = false;

let maxVal = 20;

// --- DIFFICULTY CONFIG ---

if (level >= 40) {

numTerms = 3;

maxVal = 50;

}

if (level >= 50) {

operatorsPool = ['+', '-', '\*', '/'];

if (Math.random() < 0.5) useParens = true;

maxVal = 100;

}

if (level >= 70) {

maxVal = 500;

}

// Generate Numbers

let nums = [];

for(let i=0; i<numTerms; i++) nums.push(Math.floor(Math.random() \* maxVal) + 1);

// Generate Operators

let ops = [];

let hasDivision = false;

for(let i=0; i<numTerms-1; i++) {

let op = operatorsPool[Math.floor(Math.random() \* operatorsPool.length)];

if (op === '/') {

if (hasDivision) { op = '+'; } else { hasDivision = true; }

}

ops.push(op);

}

**Module Name: Content Aware Timer System**

Purpose: To dynamically calculate the time limit for answering equations based on their complexity.

// --- SMART TIMER CALCULATION ---

let frames = 180;

for (let op of ops) {

if (op === '\*' || op === '/') {

frames += 75;

} else {

frames += 30;

}

}

for (let n of nums) {

if (n > 30) frames += 30;

if (n > 100) frames += 30;

}

if (visualStr.includes('(')) frames += 45;

if (visualStr.includes('/')) frames += 45;

frames += (level \* 2);

let totalDigits = nums.reduce((sum, n) => sum + String(n).length, 0);

frames += (totalDigits \* 20);

if (frames > 1800) frames = 1800;

problemData = { question: visualStr + " = ?", answer: answer, maxTime: frames };

isValid = true;

**Module Name: Enemy Auto Scaling System**

Purpose: To balance map areas by dynamically scaling enemy stats to match the players party.

const \_Game\_Enemy\_paramBase = Game\_Enemy.prototype.paramBase;

Game\_Enemy.prototype.paramBase = function(paramId) {

const base = \_Game\_Enemy\_paramBase.call(this, paramId);

if (this.enemy().meta.NoScale) return base;

if (ignoredList.includes(paramId)) return base;

const party = $gameParty.battleMembers();

let lvlSum = 0;

for (const actor of party) {

lvlSum += actor.level;

}

const avgLvl = Math.max(1, Math.floor(lvlSum / party.length));

return Math.floor(base \* (1 + (rate \* (avgLvl - 1))));

};

const \_Game\_Enemy\_exp = Game\_Enemy.prototype.exp;

Game\_Enemy.prototype.exp = function() {

const base = \_Game\_Enemy\_exp.call(this);

if (this.enemy().meta.NoScale) return base;

const party = $gameParty.battleMembers();

let lvlSum = 0;

for (const actor of party) lvlSum += actor.level;

const avgLvl = Math.max(1, Math.floor(lvlSum / party.length));

return Math.floor(base \* (1 + (rate \* (avgLvl - 1))));

};

const \_Game\_Enemy\_gold = Game\_Enemy.prototype.gold;

Game\_Enemy.prototype.gold = function() {

const base = \_Game\_Enemy\_gold.call(this);

if (this.enemy().meta.NoScale) return base;

const party = $gameParty.battleMembers();

let lvlSum = 0;

for (const actor of party) lvlSum += actor.level;

const avgLvl = Math.max(1, Math.floor(lvlSum / party.length));

return Math.floor(base \* (1 + (rate \* (avgLvl - 1))));

};

**Module Name: Performance Based Reward Mechanism**

Purpose: To determine the effectiveness of combat actions based on the speed and accuracy of the players math input.

MathSystem.forceCrit = false;

MathSystem.forceMiss = false;

if (result.correct) {

if (result.fast) {

MathSystem.resultMultiplier = 2.0;

MathSystem.forceCrit = true;

this.\_logWindow.addText("\\C[24]MATH GENIUS! (2x Crit)\\C[0]");

} else {

MathSystem.resultMultiplier = 1.0;

this.\_logWindow.addText("\\C[0]Correct, but slow.\\C[0]");

}

} else {

if (result.fast) {

MathSystem.resultMultiplier = 0.5;

this.\_logWindow.addText("\\C[18]Wrong! (Weakened)\\C[0]");

} else {

MathSystem.resultMultiplier = 0.0;

MathSystem.forceMiss = true;

this.\_logWindow.addText("\\C[18]Wrong & Slow! (Miss)\\C[0]");

}

}

const \_Game\_Action\_makeDamageValue = Game\_Action.prototype.makeDamageValue;

Game\_Action.prototype.makeDamageValue = function(target, critical) {

let value = \_Game\_Action\_makeDamageValue.call(this, target, critical);

if (this.subject().isActor()) {

critical = MathSystem.forceCrit;

let multiplier = MathSystem.resultMultiplier > 0 ? MathSystem.resultMultiplier : 1.0;

value = Math.floor(value \* multiplier);

}

return value;

};

**Module Name: Automatic Quest Generation System**

Purpose: To dynamically build side quests like hunting without requiring manual mission design.

registerCurrentMap: function(storyLevel) {

checkSystemData();

const sys = $gameSystem.\_pQuest;

const mapName = $dataMap.displayName || "Wilderness";

let localEnemies = [];

$gameMap.encounterList().forEach(enc => {

const troop = $dataTroops[enc.troopId];

if (troop) {

troop.members.forEach(m => {

if (!localEnemies.includes(m.enemyId)) localEnemies.push(m.enemyId);

});

}

});

let localItems = [];

localEnemies.forEach(eId => {

const enemy = $dataEnemies[eId];

if (enemy && enemy.dropItems) {

enemy.dropItems.forEach(d => {

if (d.kind === 1) localItems.push(d.dataId);

});

}

});

if (localEnemies.length > 0) {

sys.knownZones[storyLevel] = { name: mapName, enemies: localEnemies, items: localItems };

}

},

generateFromProgress: function() {

$gameVariables.setValue(VAR\_TEXT, "Looking for work...");

try {

checkSystemData();

const progress = $gameVariables.value(VAR\_PROGRESS) || 1;

const sys = $gameSystem.\_pQuest;

let validLevels = [];

for (let lvl in sys.knownZones) {

if (Number(lvl) <= progress) validLevels.push(lvl);

}

if (validLevels.length === 0) return;

const zoneLevel = validLevels[Math.floor(Math.random() \* validLevels.length)];

const zone = sys.knownZones[zoneLevel];

let type = "HUNT";

if (zone.items && zone.items.length > 0 && Math.random() > 0.5) type = "GATHER";

this.createQuest(type, zone, Number(zoneLevel));

} catch (e) {

console.error(e);

}

},

checkCompletion: function() {

checkSystemData();

const q = $gameSystem.\_pQuest;

if (!q.active) return;

let done = false;

if (q.type === "HUNT") {

if (q.amountCurrent >= q.amountNeeded) done = true;

} else {

if ($gameParty.numItems($dataItems[q.targetId]) >= q.amountNeeded) {

done = true;

$gameParty.loseItem($dataItems[q.targetId], q.amountNeeded);

}

}

if (done) {

$gameMessage.add("Quest Complete!");

$gameParty.gainGold(Math.floor(q.rewardGold));

$gameParty.members().forEach(a => a.changeExp(a.currentExp() + Math.floor(q.rewardExp), true));

q.active = false;

$gameVariables.setValue(VAR\_STATUS, 0);

}

}

};

const \_Game\_Enemy\_performCollapse = Game\_Enemy.prototype.performCollapse;

Game\_Enemy.prototype.performCollapse = function() {

\_Game\_Enemy\_performCollapse.call(this);

checkSystemData();

const q = $gameSystem.\_pQuest;

if (q && q.active && q.type === "HUNT" && this.enemyId() === q.targetId) {

q.amountCurrent++;

}

};

**Module Name: Peer to Peer Multiplayer Framework**

Purpose: To enable cooperative multiplayer gameplay via direct connections without a centralized server.

init: function(callback) {

if (this.peer) { if (callback) callback(this.myId); return; }

const config = {

debug: 1,

config: {

iceServers: [

{ urls: 'stun:stun.l.google.com:19302' },

{ urls: 'stun:global.stun.twilio.com:3478' }

]

}

};

try {

this.peer = new Peer(null, config);

this.peer.on('open', (id) => {

this.myId = id;

if (callback) callback(id);

});

this.peer.on('connection', (c) => {

this.setupConnection(c);

$gameMessage.add("Partner Connected!");

});

this.peer.on('error', (e) => console.warn(e));

} catch (e) {

console.warn("PeerJS not loaded.");

}

},

host: function() {

this.isHost = true;

this.init((id) => {

if (navigator.clipboard) navigator.clipboard.writeText(id);

$gameMessage.add("Hosting! ID Copied.");

$gameMessage.add(id);

});

},

join: function(code) {

this.isHost = false;

const target = String(code).trim();

this.init(() => {

const conn = this.peer.connect(target, { label: 'rpg', reliable: true });

this.setupConnection(conn);

$gameMessage.add("Connecting...");

});

},

setupConnection: function(conn) {

this.conn = conn;

this.conn.on('open', () => {

this.isConnected = true;

this.sendUpdate();

});

this.conn.on('data', (data) => this.handleData(data));

this.conn.on('close', () => {

this.isConnected = false;

$gameMessage.add("Partner Disconnected.");

if (SceneManager.\_scene instanceof Scene\_Battle) {

if (this.remoteData.isFighting) {

$gameMessage.add(this.remoteData.charName + " left the fight!");

}

BattleManager.processAbort();

this.restoreParty();

this.refreshBattleVisuals(true);

}

this.remoteData.isFighting = false;

this.wasRemoteFighting = false;

});

},

sendUpdate: function() {

const leader = $gameParty.leader();

const inBattle = (SceneManager.\_scene instanceof Scene\_Battle);

if (!leader) return;

const myActors = $gameParty.members().slice(0, 2).map(a => ({

id: a.actorId(),

hp: a.hp,

mp: a.mp,

tp: a.tp,

mhp: a.mhp,

mmp: a.mmp

}));

const packet = {

type: 'state',

mapId: $gameMap.mapId(),

x: $gamePlayer.x,

y: $gamePlayer.y,

charName: leader.characterName(),

charIndex: leader.characterIndex(),

isFighting: inBattle,

actors: myActors

};

try { this.conn.send(packet); } catch(e) {}

},

handleData: function(data) {

if (data.type === 'state') {

this.remoteData = data;

this.syncRemoteStats();

}

if (data.type === 'request\_join') {

if (SceneManager.\_scene instanceof Scene\_Battle) {

const myActors = $gameParty.members().slice(0, 2).map(a => a.actorId());

this.conn.send({

type: 'accept\_join',

troopId: $gameTroop.\_troopId,

hostActors: myActors

});

const remoteActorIds = this.remoteData.actors.map(a => a.id);

this.mergeParty(remoteActorIds);

$gameMessage.add(this.remoteData.charName + " joined the fight!");

}

}

if (data.type === 'accept\_join') {

this.joinBattleAsClient(data.troopId, data.hostActors);

$gameMessage.add("Joined " + this.remoteData.charName + " fight!");

}

if (data.type === 'battle\_action') {

this.executeRemoteAction(data);

}

},

mergeParty: function(remoteActorIds) {

if (!this.originalParty) this.backupParty();

const myActors = $gameParty.\_actors.slice(0, 2);

$gameParty.\_actors = myActors.concat(remoteActorIds);

this.refreshBattleVisuals(true);

},

joinBattleAsClient: function(troopId, hostActorIds) {

if (!this.originalParty) this.backupParty();

const myActors = $gameParty.\_actors.slice(0, 2);

$gameParty.\_actors = hostActorIds.concat(myActors);

$gamePlayer.refresh();

BattleManager.setup(troopId, true, true);

BattleManager.setEventCallback(n => this.\_branch = n);

$gamePlayer.makeEncounterCount();

SceneManager.push(Scene\_Battle);

setTimeout(() => this.refreshBattleVisuals(true), 100);

}

**Module Name: Mobile Input System**

Purpose: To provide touchscreen support for mobile device users during math based combat.

class Window\_MathKeypad extends Window\_Command {

constructor(rect) {

super(rect);

this.openness = 0;

this.active = false;

this.hide();

}

makeCommandList() {

this.addCommand("1", "1");

this.addCommand("2", "2");

this.addCommand("3", "3");

this.addCommand("4", "4");

this.addCommand("5", "5");

this.addCommand("6", "6");

this.addCommand("7", "7");

this.addCommand("8", "8");

this.addCommand("9", "9");

this.addCommand("-", "-");

this.addCommand("0", "0");

this.addCommand("DEL", "back");

this.addCommand("OK", "ok");

}

maxCols() {

return 3;

}

processTouch() {

if (this.isOpenAndActive()) {

if (TouchInput.isTriggered() && this.isTouchOkEnabled()) {

const hitIndex = this.hitIndex();

if (hitIndex >= 0) {

this.select(hitIndex);

this.processOk();

return;

}

}

}

super.processTouch();

}

}

Appendix H: User’s Manual

**Figure No.: 1**

**Figure Title: Title Screen Interface Navigation**

![Fig-H1-Title-Screen 1](data:image/png;base64...)

**Figure No.: 2**

**Figure Title: System Options Menu (General & Audio Settings)**

![Fig-H2-Options-General 1](data:image/png;base64...)

**Figure No.: 3**

**Figure Title: System Options Menu (Sound Effect Setting)**

![Fig-H3-Options-SE 1](data:image/png;base64...)

**Figure No.: 4**

**Figure Title: Continue and Load Game Interface**

![Fig-H4-Load-Game 1](data:image/png;base64...)

**Figure No.: 5**

**Figure Title: Protagonist Character Name Input**

![Fig-H5-Name-Input 1](data:image/png;base64...)

**Figure No.: 6**

**Figure Title: Overworld & Interior Exploration Environment**

**![Fig-H6-Overworld-Exploration 1](data:image/png;base64...)**

**Figure No.: 7**

**Figure Title: Main System Pause Menu**

**![Fig-H7-Pause-Menu 1](data:image/png;base64...)**

**Figure No.: 8**

**Figure Title: Inventory & Item Management Menu**

**![Fig-H8-Items-Menu 1](data:image/png;base64...)**

**Figure No.: 9**

**Figure Title: Character Skills & Abilities Management Menu**

**![Fig-H9-Character-Skills-Menu 1](data:image/png;base64...)**

**Figure No.: 10**

**Figure Title: Character Equipment & Gear Configuration Menu**

**![Fig-H10-Equipment-Menu 1](data:image/png;base64...)**

**Figure No.: 11**

**Figure Title: Character Status & Detailed Attributes Menu**

**![Fig-H11-Status-Menu 1](data:image/png;base64...)**

**Figure No.: 12**

**Figure Title: Party Formation & Roster Arrangement Menu**

**![Fig-H12-Formation-Menu 1](data:image/png;base64...)**

**Figure No.: 13**

**Figure Title: Quests & Mission Log Interface**

**![Fig-H13-Quests-Menu 1](data:image/png;base64...)**

**Figure No.: 14**

**Figure Title: Game Save & Progress Recording Interface**

**![Fig-H14-Save-Menu 1](data:image/png;base64...)**

**Figure No.: 15**

**Figure Title: Return to Title / Game Exit Confirmation Dialog**

**![Fig-H15-Pause-Menu-Exit 1](data:image/png;base64...)**

**Figure No.: 16**

**Figure Title: Tactical Battle Command Menu - Page 1 (Primary Actions)**

**![Fig-H16-Battle-Menu-Page1 1](data:image/png;base64...)**

**Figure No.: 17**

**Figure Title: Tactical Battle Command Menu - Page 2 (System & Tactical Actions)**

**![Fig-H17-Battle-Menu-Page2 1](data:image/png;base64...)**

**Figure No.: 18**

**Figure Title: Battle Skills & Special Abilities Selection Submenu**

**![Fig-H18-Battle-Skills 1](data:image/png;base64...)**

**Figure No.: 19**

**Figure Title: Battle Consumables & Item Selection Submenu**

**![Fig-H19-Battle-Items 1](data:image/png;base64...)**

**Figure No.: 20**

**Figure Title: Combatant Tactical Status & Condition Submenu**

**![Fig-H20-Battle-Status 1](data:image/png;base64...)**

**Figure No.: 21**

**Figure Title: Math Battle System & Mobile Virtual Numeric Keypad Interface**

**![Fig-H21-Math-Combat-Keypad 1](data:image/png;base64...)**

Appendix I: Curriculum Vitae

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **PERSONAL INFORMATION** | | | | ![IMG_256](data:image/jpeg;base64...) |
| **Full Name:** | John Angel D. Guevarra | | |
| **Address:** | Concepcion, Tarlac | | |
| **Contact Number:** | +63 9762802968 | | |
| **Email Address:** | Johnangelguevarra.6@gmail.com | | |
| **Date of Birth:** | June 6, 2004 | | |
| **Place of Birth:** | Concepcion, Tarlac | | |
| **EUCATIONAL BACKGROUND** | | | | |
| **Tertiary Education** | **Degree/Program:** | Bachelor of Science in Information Technology (BSIT) | | |
| **School/University:** | Dominican College of Tarlac, Inc. | | |
| **Inclusive Years:** | 2023 – 2027 | | |
| **Senior High School** | **Strand:** | General Academic Strand (GAS) | | |
| **School:** | Capas National High School.  Sto. Domingo II, Capas, Tarlac | | |
| **Inclusive Years:** | 2020 – 2021 | | |
| **Junior High School** | **School:** | Capas National High School.  Capas, Tarlac | | |
| **Inclusive Years:** | 2017 – 2021 | | |
| **Elementary** | **School:** | San Juan Elementary School.  Concepcion, Tarlac | | |
| **Inclusive Years:** | 2011 – 2017 | | |
| **TECHNICAL SKILLS** | | | | |
| **Skill/Technology** | **Proficiency Level** | | | |
| **Database Management**  **(PostgreSQL)** | Beginner | | | |
| **Web Development (JavaScript,**  **HTML5, CSS, React)** | Intermediate | | | |
| **UI/UX Design  (Figma, Graphic Design)** | Advanced | | | |
| **Multimedia**  **(Canva, CapCut)** | Beginner | | | |
| **RESEARCH/CAPSTONE EXPERIENCE** | | | | |
| **Project Title:** | Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling. | | | |
| **Role in the Project:** | Project Manager | | | |
| **Responsibilities:** | Setting project timelines, schedules, and milestone targets. Delegated development tasks. Managed task tracking and held weekly team progress meetings, participated in designing and coordinating final defense deliverables. | | | |
| **WORK EXPERIENCE** | | | | |
| **POSITION** | **COMPANY/ORGANIZATION** | | **Inclusive Dates** | |
| **Freelance Web Developer** | **Mercury Marketing** | | **05/2026 - 06/2026** | |
| **Freelance Web Developer & Graphic Designer** | **KickFi** | | **08/2023 - 09/2023** | |

|  |  |  |  |
| --- | --- | --- | --- |
| **PERSONAL INFORMATION** | | | **![New Project 2 [8700FC5]](data:image/png;base64...)** |
| **Full Name:** | Justine C. Lacsina | |
| **Address:** | 1164 San Felipe St. Lawy, Capas, Tarlac | |
| **Contact Number:** | 09502581534 | |
| **Email Address:** | lacsina1342@gmail.com | |
| **Date of Birth:** | July 01, 2004 | |
| **Place of Birth:** | Capas, Tarlac | |
| **EUCATIONAL BACKGROUND** | | | |
| **Tertiary Education** | **Degree/Program:** | Bachelor of Science in Informarion Technology | |
| **School/University:** | Dominican College of Tarlac INC. | |
| **Inclusive Years:** | 2023 - up to present | |
| **Senior High School** | **Strand:** | Information and Communications Technology (ICT) | |
| **School:** | St. Nichole Technical School | |
| **Inclusive Years:** | 2021-2023 | |
| **Junior High School** | **School:** | Lawy High School | |
| **Inclusive Years:** | 2016-2021 | |
| **Elementary** | **School:** | Lawy Elementary School | |
| **Inclusive Years:** | 2011-2016 | |
| **TECHNICAL SKILLS** | | | |
| **Skill/Technology** | **Proficiency Level** | | |
| **Programming** | Intermediate | | |
| **Database Management** | Intermediate | | |
| **Web Development** | Intermediate | | |
| **Mobile Development** | Beginner | | |
| **Networking** | Beginner | | |
| **UI/UX Design** | Beginner | | |
| **Multimedia** | Intermediate | | |
| **RESEARCH/CAPSTONE EXPERIENCE** | | | |
| **Project Title:** | Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling. | | |
| **Role in the Project:** | Tester/Quality Assurance | | |
| **Responsibilities:** | Collaboration with the programmer and the UI/UX designer to ensure the quality and security of the project. | | |
| **AWARDS AND ACHIEVEMENTS** | | | |
| **Title of the Award:** | **First Year, First Semester Dean’s Lister** | | |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **PERSONAL INFORMATION** | | | | **![C:/Users/justi/Downloads/41e19c07-142a-4dcd-a9df-76a34232495f.png41e19c07-142a-4dcd-a9df-76a34232495f](data:image/jpeg;base64...)** |
| **Full Name:** | Allan Joshua C. Manalo | | |
| **Address:** | Sitio, Sampaguita, Cub-Cub, Capas, Tarlac | | |
| **Contact Number:** | 0963-708-114 | | |
| **Email Address:** | allanjoshmanalo25@gmail.com | | |
| **Date of Birth:** | September 25, 2005 | | |
| **Place of Birth:** | Tarlac Provincial Hospital (TPH) | | |
| **EUCATIONAL BACKGROUND** | | | | |
| **Tertiary Education** | **Degree/Program:** | Bachelor of Science in Information Technology | | |
| **School/University:** | Dominican College of Tarlac, Inc. | | |
| **Inclusive Years:** | 2023- up to present | | |
| **Senior High School** | **Strand:** | Sports Track | | |
| **School:** | Senior High School | | |
| **Inclusive Years:** | 2021-2023 | | |
| **Junior High School** | **School:** | Capas National High School | | |
| **Inclusive Years:** | 2016-2021 | | |
| **Elementary** | **School:** | Capas East Central School | | |
| **Inclusive Years:** | 2011-2016 | | |
| **TECHNICAL SKILLS** | | | | |
| **Skill/Technology** | **Proficiency Level** | | | |
| **Programming** | Beginner | | | |
| **Database Management** | Beginner | | | |
| **Web Development** | Beginner | | | |
| **Mobile Development** | Beginner | | | |
| **Networking** | Beginner | | | |
| **UI/UX Design** | Beginner | | | |
| **Multimedia** | Beginner | | | |
| **RESEARCH/CAPSTONE EXPERIENCE** | | | | |
| **Project Title:** | Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling. | | | |
| **Role in the Project:** | Database Designer | | | |
| **Responsibilities:** | Collaborated closely with backend developers and game logic programmers to ensure data integrity and reliable data retrieval. | | | |
| **AWARDS AND ACHIEVEMENTS** | | | | |
| **Title of the Award:** | **Academic Excellence Award / With Honors**  **Senior High School** | | | |
| **WORK EXPERIENCE** | | | | |
| **POSITION** | **COMPANY/ORGANIZATION** | | **Inclusive Dates** | |
| **Enumerator** | **Municipal of Capas** | | **2023-2025** | |
| **Department Store Support Staff** | **Walter Mart Department Store** | | **2025** | |

|  |  |  |  |
| --- | --- | --- | --- |
| **PERSONAL INFORMATION** | | | ![C:/Users/justi/Downloads/ChatGPT Image Feb 28, 2026, 01_08_18 AM.pngChatGPT Image Feb 28, 2026, 01_08_18 AM](data:image/png;base64...) |
| **Full Name:** | Justine T.Panganiban | |
| **Address:** | Sta.Maria Riverside Concepcion, Tarlac | |
| **Contact Number:** | 09858330350 | |
| **Email Address:** | justinepanganiban96@gmail.com | |
| **Date of Birth:** | November 8, 2001 | |
| **Place of Birth:** | Concepcion, Tarlac | |
| **EUCATIONAL BACKGROUND** | | | |
| **Tertiary Education** | **Degree/Program:** | Bachelor of Science in Informarion Technology | |
| **School/University:** | Dominican College of Tarlac INC. | |
| **Inclusive Years:** | 2023 - up to present | |
| **Senior High School** | **Strand:** | Information and Communications Technology (ICT) | |
| **School:** | Benigno S. Aquino National High School | |
| **Inclusive Years:** | 2020-2022 | |
| **Junior High School** | **School:** | Benigno S. Aquino National High School | |
| **Inclusive Years:** | 2013-2019 | |
| **Elementary** | **School:** | Concepcion North Central Elementary School | |
| **Inclusive Years:** | 2007-2013 | |
| **TECHNICAL SKILLS** | | | |
| **Skill/Technology** | **Proficiency Level** | | |
| **Database Management** | Intermediate | | |
| **Web Development** | Intermediate | | |
| **Mobile Development** | Beginner | | |
| **Networking** | Beginner | | |
| **UI/UX Design** | Advanced | | |
| **Multimedia** | Intermediate | | |
| **Others – Specify** | Unity 3D Game Development | | |
| **RESEARCH/CAPSTONE EXPERIENCE** | | | |
| **Project Title:** | Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling. | | |
| **Role in the Project:** | UI/UX designer | | |
| **Responsibilities:** | To design the frontend and to help the programmer to test the project | | |

|  |  |  |  |
| --- | --- | --- | --- |
| **PERSONAL INFORMATION** | | | **![C:/Users/justi/Downloads/benedik.pngbenedik](data:image/png;base64...)** |
| **Full Name:** | John Benedict D. Quinez | |
| **Address:** | Regina Nortview, Cut-cut 1st, Capas, Tarlac | |
| **Contact Number:** | 09984958395 | |
| **Email Address:** | johnbenedictquinez@gmail.com | |
| **Date of Birth:** | July 1, 2005 | |
| **Place of Birth:** | Tarlac City | |
| **EUCATIONAL BACKGROUND** | | | |
| **Tertiary Education** | **Degree/Program:** | Bachelor of Science Information Technology | |
| **School/University:** | Dominican College of Tarlac Inc. | |
| **Inclusive Years:** | 2023 - Onwards | |
| **Senior High School** | **Strand:** | Information & Communication Technology | |
| **School:** | Dominican College of Tarlac Inc. | |
| **Inclusive Years:** | 2021 - 2023 | |
| **Junior High School** | **School:** | Dominican College of Tarlac Inc. | |
| **Inclusive Years:** | 2017 - 2021 | |
| **Elementary** | **School:** | Lightgiver Christian School inc | |
| **Inclusive Years:** | 2016 - 2017 | |
| **TECHNICAL SKILLS** | | | |
| **Skill/Technology** | **Proficiency Level** | | |
| **Programming** | Intermediate - Advanced | | |
| **Database Management** | Beginner | | |
| **Web Development** | Beginner | | |
| **Mobile Development** | Beginner | | |
| **Networking** | Beginner | | |
| **UI/UX Design** | Intermediate | | |
| **Multimedia** | Intermediate - Advanced | | |
| **RESEARCH/CAPSTONE EXPERIENCE** | | | |
| **Project Title:** | Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling. | | |
| **Role in the Project:** | Programmer | | |
| **Responsibilities:** | Wrote the core game scripts using JavaScript to build the custom math battle system and the level based difficulty scaling. Set up the peer to peer multiplayer connection to allow cooperative gameplay. Created the FDD, Use Case, Sequence and Activity diagrams to map out the system architecture for the project documentation. | | |

Appendix J: Story, Characters, Items, Character Classes and Biomes

**J.1 Story Overview**

The narrative of Chronicles Of Arithmos specifically starts in the Plains of Origin. The main character wakes up to discover a world filled with monsters. Guided by Bron, a mentor for physical combat, and Martha, a main mentor character for magical combat, the player will complete a tutorial. Players will discover that a curse affects Lily, the younger sister of the main character. The protagonist will need to restore the worlds logic to cure her condition.

The main character will travel through four separate biomes. A corrupted elemental force will guard each area. Players will fight the Forest Golem, Pharaoh's Guard, Fenrir wolf, and Demon Lord to recover story fragments. This journey will eventually end in the Void Dimension. Here, the player will face The Numeromancer. This final boss causes the chaos, and players will use math and combat skills to defeat him and fix the realm.

The game will involve the player forming an alliance to accomplish this mission. Kael will be initiated into the group as a knight. Elara will also bring spellcraft as a sorceress. Garrick will also act as a heavy-duty defender. Sylas the bandit and Isolde the priest will also be enlisted to the group. Other members will include Thorne as a hunter, Lyra as a magic swordsman and Fenrin as a monk.

Game mechanics will be strengthened by major supporting characters. Elder Tobias will direct the player on where to head next. The further movement of the player will be guided by Captain Valerius. There will be several positions which will monitor the buying and selling of items. Merchant Oryn will be selling general merchandise and buying enemy drops. Potions will be administered by alchemist Vanya. There will be blacksmith Rurik who will sell equipment. Innkeeper Gorm will give health and mana-regeneration.

Additional characters will provide certain services. Quest-generated hubs will be based around receptionist Mila. Bard Jareth and Priestess Anara will heal party and nullify negative statuses. Professor Haze will man the training facility. Players will learn where enemies appear with the help of Librarian Estel. The party can have their TP charged from Hunter Kaelen. Portal Keeper Alden will also allow users to create or join multiplayer. Extra dialogue will be offered by characters such as Widow Claire, Guard Captain Aris, and Street Urchin Pip. There will be background Npc’s that might give items like Farmer Ben, Nobleman Caelus and Fisherman Old Tom.

The towns will also include generic non-interactive characters to fill the environment. Examples of these characters are normal townspeople, playing children, tavern regulars, merchants, and security guards at the castle. It will also be included in the maps with stable boys, street sweepers, beggars, and walking couples to develop a dynamic atmosphere. Students, tourists, drunkards and street performers will be the visual only characters.

The ambient music will be used to complement the visual aesthetics in the game and reduce mathematical anxiety. Music tracks will be different depending on the place of location. Rhythmic patterns will see players experience compositions of calmness in the town, active tunes in battles, and relaxed tunes in dungeons. There will be unique biomes that present particular enemies and loot gathering chance in the game environment.

**J.2 Biomes**

**J.2.1 Plains and Forest**

The first zone or level of the game will be the Plains and Forests where the story begins. Players will be given the chance to openly explore the first Golem known as the corrupted elemental will be guarding the end of the region.

**J.2.1.1 Enemies & Drops**

The slime in Chronicles of Arithmos will drop Green Gel. The Rat will drop a Rat Tail. The Bat will drop a Bat Wing. The Spider will drop a Sticky Web. The Hornet will drop an Insect Wing. The Wolf will drop a Wolf Pelt. The Bear will drop a Bear Claw. The Treant will drop a Living Branch. The Goblin and Goblin Archer will drop Goblin Cloth. The Goblin Shaman will drop Shaman Beads. The Orc will drop an Orc Tusk. The Bandit and Bandit Leader will drop a Stolen Coin Purse. The Crow will drop a Shiny Feather. The Snake will drop Snake Skin. The Fairy will drop Fairy Dust. The Mandrake will drop a Mandrake Root. The Wild Boar will drop Boar Meat. The Forest Golem will drop Ancient Bark.

**J.2.2 Desert**

The Deserts will serve as harsh drylands for the party to explore. Players will travel across this sandy area to face harder monsters and gather new items. A corrupted elemental force known as the Pharaoh's Guard will block the end of this region.

**J.2.2.1 Enemies & Drops**

The Sand Slime will drop Yellow Gel. The Scorpion and Giant Scorpion will drop Scorpion Stingers. The Cactus will drop a Cactus Flower. The Sand Worm, Ant Lion, and Dust Spirit will drop Sand Essence. A Mummy will drop an Old Bandage. Players will get a Bone Fragment from the Skeleton Warrior, and the Skeleton Mage will drop a Skull. Fighting a Desert Wolf will give the player Dry Fur. The Lamia will drop a Snake Scale. When a user defeats a Basilisk, the creature will leave a Petrified Eye. The Gargoyle and Sand Golem will give a Stone Wing and a Sandstone Block. A Vulture will drop a Vulture Beak. Players will get a Riddle Tablet from the Sphinx, and the Ancient Scarab will drop a Scarab Shell. Both the Desert Rogue and the Pharaoh's Guard will drop Golden Fragments.

**J.2.3 Tundra and Frost**

The Tundra and Frost regions will serve as massive frozen expanses. Players will navigate these cold zones to battle ice enemies and collect rare loot. A corrupted elemental force known as the Fenrir wolf will guard the final part of this area.

**J.2.3.1 Enemies & Drops**

In these cold zones, the Ice Slime will drop Blue Gel. The Snow Wolf will drop a Wolf Fang. The Polar Bear will drop Thick Hide. The Ice Bat and White Tiger will drop White Fur. The Snow Spirit and Winter Wisp will drop Cold Wisps. The Yeti will drop a Yeti Horn. The Ice Golem will drop a Permafrost Shard. The Crystal Spider will drop a Crystal Leg. The Frost Giant and Frozen Knight will drop Frost Metal. The Corrupted Penguin will drop a Corrupted Feather. The Ice Drake will drop a Drake Scale. The Wendigo and Frost Mage will drop Frozen Hearts. The Glacial Turtle will drop an Ice Turtle Shell. The Snow Harpy will drop a Harpy Feather. The Ice Elemental will drop an Ice Crystal. The Fenrir will drop a Snowflake Core.

**J.2.4 Volcano and Fire**

The Volcano and Fire zones will act as the most dangerous harsh wasteland. Players will fight through this extreme heat to survive very strong enemies and find the best materials. A corrupted elemental force known as the Demon Lord will wait at the end of this region.

**J.2.4.1 Enemies & Drops**

The Magma Slime will drop Red Gel. The Fire Spirit and Fire Elemental will drop Embers. The Imp will drop an Imp Wing. The Demon and Minotaur will drop Demon Horns. The Succubus will drop Succubus Cloth. The Cerberus will drop a Hellhound Fang. The Lava Golem will drop an Obsidian Shard. The Fire Bat will drop a Fire Gland. The Salamander and Dragon Hatchling will drop Red Scales. The Red Dragon will drop a Dragon Tooth. The Efreet will drop a Djinn Lamp. The Phoenix will drop Phoenix Ash. The Iron Giant will drop Iron Scraps. The Dark Knight will drop Dark Armor Pieces. The Cultist will drop a Forbidden Page. The Chimera will drop a Chimera Tail. The Demon Lord will drop an Infernal Core.

**J.2.5 General Areas and Dungeons**

General areas and dungeons throughout the game will provide different types of enemy encounters. Players will face common enemies scattered across every map region to collect basic items. They will also explore hidden dungeon spaces to fight special monsters that drop rare essences and fragments.

**J.2.5.1 Enemies & Drops**

The Ghost and Shadow will drop Ectoplasm. The Zombie will drop Rotten Flesh. The Vampire and Vampire Bat will drop Vampire Fangs. The Mimic and Magic Pot will drop Unknown Fluid. The Will-o'-the-Wisp will drop Spirit Dust. The Animated Armor and Flying Sword will drop Haunted Metal. The Gazer will drop an Evil Eye. The Ogre and Troll will drop Ogre Clubs. The Warlock will drop Magic Powder. The Necromancer will drop a Tattered Robe. The Reaper will drop a Chaos Mote. The Ceramic Shard will drop randomly in general dungeons. The Chaos Cloud, Number Eater, Equation Spirit, and The Unknown will drop Arithmetic Essences and Void Fragments.

**J.3 Items**

Items will support gameplay with various consumables. Potions, Hi-Potions, and Full Potions will restore health. Magic Waters, Hi-Magic Waters, and Elixirs will restore mana or both health and mana. Antidotes, Eye Drops, Echo Herbs, Stimulants, Potent Stimulants, Panaceas, and Dispel Herbs will cure negative status ailments. Escape Ropes and Repel Sprays will help players avoid or leave battles. Permanent stat boosters like HP Up, MP Up, Strength Seeds, Defense Seeds, Magic Seeds, Agility Seeds, Luck Seeds, and Skill Books will permanently upgrade a character's core attributes.

**J.4 Character Classes**

Players will choose from eight distinct character classes, each with access to a specialized weapon arsenal and skill set that will expand as the player progresses.

**J.4.1 Swordsman**

The Swordsman class will focus on heavy physical strikes to damage monsters. Players will equip swords to act as their main weapon during encounters. This role will have access to various skills, for example, lowering the defense of targets or hitting all enemies at once.

**J.4.1.1 Weapons**

The Swordsman class will wield swords, The Long Sword will be a standard issue blade. The Woodcutter's Blade will be a simple cutting tool. The Wolf Fang Sword will be an animal-themed blade. The Forest Cutter will be a nature themed sword. The Bandit's Edge will be a thief's blade. The Verdant Blade will be a green sword. The Sand Scimitar will be a desert curved sword. The Scorpion Tail will be a stinger-shaped sword. The Dune Blade will be a sandy sword. The Sun-Scorched Sword will be a heat-themed sword. The Ancient Khopesh will be an old desert blade. The Ice Brand will be a cold-forged sword. The Glacial Edge will be a frozen sword. The Frostbite Sword will be a chilling blade. The Crystal Saber will be a crystalline sword. The Blizzard Blade will be a winter themed sword. The Magma Blade will be a molten sword. The Dragon Bone Sword will be crafted from dragon remains. The Infernal Edge will be a demonic blade. The Flame Tongue will be a fire-forged sword. The Phoenix Feather Sword will be a legendary fiery sword.

**J.4.1.2 Skills**

For the Swordsman, Strong Attack will deliver a heavy physical strike. Slash will execute a basic sword technique. Double Slash will hit the enemy twice in succession. Wide Swing will deal physical damage to all enemies. Armor Break will damage an enemy and lower their defense. Blade Bash will strike with the flat of the blade with a chance to stun. Focus will increase the critical hit rate. Parry will greatly increase evasion. Sonic Wave will deal ranged wind damage. Wind Slash will perform a wind elemental physical attack. Power Break will damage an enemy and lower their attack. Mind Break will damage an enemy and lower their magic attack. Berserk Stance will increase attack but lower defense. Cross Cut will perform two intersecting slashes. Omnislash will execute rapid strikes against random targets.

**J.4.2 Sorcerer**

The Sorcerer class will rely on elemental magic to deal high damage. Players will wield staves and rods to attack their targets. This role will have access to various skills, for example, shooting fire at a single enemy or absorbing mana from monsters.

**J.4.2.1 Weapons**

The Sorcerer class will wield staves and rods. The Oak Staff will be a basic wooden staff. The Briar Rod will be a thorny stick. The Druid's Staff will be a nature themed pole. The Faerie Wand will be a small magical stick. The Root Staff will be made of tree roots. Nature's Call will be an earth-themed staff. The Sandstone Rod will be a desert-forged staff. The Mirage Staff will be an illusion-themed rod. The Cobra Head Staff will be shaped like a snake. The Sun Rod will be a light-themed staff. The Sphinx Cane will be an ancient desert cane. The Icicle Rod will be made of ice. The Snowflake Staff will be a frost-themed pole. The Hailstorm Wand will be a winter-themed wand. The Permafrost Cane will be an enduring cold cane. The Frozen Core Staff will be a deeply chilled staff. The Ember Rod will be a smoldering stick. The Ash Staff will be made from burnt wood. The Dragon Breath Wand will be a dragon-themed wand. The Core Magma Staff will be a molten pole. The Hellfire Rod will be a demonic fiery staff.

**J.4.2.2 Skills**

For the Sorcerer, Fire, Fire II, and Fire III will deal varying levels of fire magic damage to one enemy. Ice, Ice II, and Ice III will deal varying levels of ice magic damage. Thunder, Thunder II, and Thunder III will deal varying levels of lightning magic damage. Flare will deal massive non elemental magic damage. Freeze will deal ice damage with a high chance to stun. Shock will deal lightning damage with a chance to paralyze. Magic Drain will absorb mana from the target. Concentrate will drastically multiply magic attack for the next spell. Meteor Swarm will deal massive fire and earth damage to all enemies.

**J.4.3 Priest**

The Priest class will act as the main support role for the group. Players will use maces and canes to defend themselves during battle. This role will have access to various skills, for example, restoring the health of the party or removing negative status effects.

**J.4.3.1 Weapons**

The Priest class will wield maces and canes. The Wooden Mace will be a simple blunt weapon. The Oak Club will be a sturdy wooden stick. The Spirit Mace will be a spiritually aligned blunt weapon. The Blessed Branch will be a holy wooden stick. The Mossy Hammer will be an overgrown blunt weapon. The Guardian's Cudgel will be a protective club. The Golden Scepter will be an ornate rod. The Sandstone Hammer will be a desert crafted mallet. The Sun Disc Mace will be a light-themed weapon. The Tomb Guardian Club will be an ancient blunt weapon. The Sacred Ankh will be a cross shaped holy relic. The Crystal Mace will be a crystalline blunt weapon. The Hailstone Hammer will be a frozen mallet. The Frozen Scepter will be an icy rod. The Polar Club will be a cold weather club. The Divine Ice Mace will be a holy frozen weapon. The Obsidian Mace will be a dark volcanic weapon. The Lava Rock Hammer will be a molten mallet. The Cleansing Fire Club will be a fiery blunt weapon. The Forge Master's Hammer will be a heavy smithing tool. The Phoenix Down Mace will be a legendary healing blunt weapon.

**J.4.3.2 Skills**

For the Priest, Heal, Heal II, and Heal III will restore varying amounts of health to an ally. Party Heal will restore health to the entire party. Cure Poison, Cure Blind, and Cure Silence will remove specific status ailments. Panacea will remove all negative status effects from one ally. Raise will revive a knocked-out ally. Holy Light will deal light magic damage to undead enemies. Protect will increase an ally's physical defense. Shell will increase an ally's magic defense. Regenerate will grant continuous health regeneration. Purify will damage an enemy and remove their buffs. Divine Intervention will fully heal the party and revive all dead allies.

**J.4.4 Knight**

The Knight class will provide heavy defense to protect the rest of the team. Players will equip spears and lances to fight on the front lines. This role will have access to various skills, for example, forcing enemies to target them instead of weaker allies or completely blocking incoming damage.

**J.4.4.1 Weapons**

The Knight class will wield spears and lances. The Short Spear will be a basic reach weapon. The Hunter's Spear will be a basic hunting tool. The Boar Tusk Lance will be an animal-themed spear. The Forest Guard Pike will be a woodland spear. The Wooden Pike will be a lightweight reach weapon. The Leaf-Blade Spear will be a nature themed polearm. The Scorpion Stinger will be a desert themed spear. The Desert Pike will be a sandy polearm. The Bronze Lance will be a metallic reach weapon. The Sand Piercer will be a desert lance. The Pharaoh's Guard will be an ancient royal spear. The Ice Shard Lance will be a frozen reach weapon. The Glacier Pike will be a heavy cold polearm. The Tundra Harpoon will be a hunting spear for the cold. The Frost Wyrm Spear will be a dragon themed ice lance. The Frozen Needle will be a sharp icy spear. The Magma Pike will be a molten polearm. The Dragon Scale Lance will be a heavy reptilian spear. The Red Steel Spear will be a crimson metallic lance. The Obsidian Lance will be a dark volcanic spear. The Hellfire Harpoon will be a demonic fiery spear.

**J.4.4.2 Skills**

For the Knight, Provoke will force enemies to target the player. Shield Bash will deal physical damage with a chance to stun. Cover will allow the knight to take damage in place of a low-health ally. Iron Defense will greatly increase defense. Guard Ally will protect a selected ally from all physical attacks. Shield Wall will increase the entire party's defense. Fortify will reduce damage taken by the user while skipping their turn. Sentinel will counter attack whenever hit physically. Justice Strike will deal damage based on the user's current defense. Heavy Charge will deliver a high damage but low-precision strike. Taunt will lower enemy attack but direct them to target the user. Unbreakable Will will grant immunity to status ailments. Phalanx will increase physical and magic defense for the user. Retribution will reflect a portion of physical damage back to the attacker. Castle of Stone will make the party immune to all damage for a turn.

**J.4.5 Martial Artist**

The Martial Artist class will fight using fast blunt damage. Players will equip claws and knuckles to strike their targets. This role will have access to various skills, for example, hitting a target multiple times or spending their own health to deliver massive damage.

**J.4.5.1 Weapons**

The Martial Artist class will wield claws and knuckles. The Leather Gloves will be basic hand protection. The Bear Claws will be animal-themed fist weapons. The Wolf Paws will be lupine hand gear. The Sharp Thorns will be spiky hand wraps. The Tree Bark Knuckles will be wooden fist weapons. The Wild Beast Fists will be feral gloves. The Scorpion Pincers will be desert-themed claws. The Sandstone Gauntlets will be heavy rocky gloves. The Cactus Spines will be prickly hand weapons. The Mummy Wraps will be ancient cloth bindings. The Golden Knuckles will be ornate metallic fist weapons. The Ice Picks will be sharp frozen claws. The Yeti Fists will be heavy snowy gloves. The Frostbite Gloves will be chilling hand gear. The Crystal Talons will be magical glass claws. The Polar Paws will be cold-weather animal gloves. The Salamander Claws will be fiery hand weapons. The Dragon Fangs will be reptilian fist weapons. The Magma Fists will be molten hand gear. The Burning Knuckles will be flaming fist weapons. The Demon Hands will be dark supernatural claws.

**J.4.3.2 Skills**

For the Martial Artist, Punch and Kick will deal basic blunt damage. Triple Kick will hit a target multiple times. Roundhouse will hit all enemies with physical damage. Chakra will restore the user's health and cure basic ailments. Meditate will restore the user's tactical points. Pressure Point will ignore enemy defense. Earth Splitter will perform an earth elemental physical attack. Gale Palm will perform a wind elemental strike that pushes the turn order back. Spirit Wave will deal ranged non-elemental damage. Counter will provide a high chance to counter-attack physical hits. Leg Sweep will carry a chance to lower enemy agility. Fists of Fury will deliver rapid punches to one target. Chi Blast will use the player's health to deal massive damage. Seven Star Strike will deliver heavy hits with guaranteed criticals.

**J.4.6 Magic Swordsman**

The Magic Swordsman class will combine physical sword strikes with elemental power. Players will use rapiers and enchanted blades to deal damage. This role will have access to various skills, for example, adding ice to their physical attacks or bouncing magic spells back at the enemy.

**J.4.6.1 Weapons**

The Magic Swordsman class will wield enchanted blades and rapiers. The Rapier will be a thrusting sword. The Wind Blade will be a gust-themed sword. The Leaf Cutter will be a nature-themed rapier. The Elven Rapier will be a mystical thrusting sword. The Swift Blade will be a lightweight sword. The Whisper Edge will be a silent blade. The Mirage Rapier will be an illusionary sword. The Heatwave Saber will be a desert-themed blade. The Dust Devil Blade will be a sandy thrusting sword. The Golden Epee will be an ornate rapier. The Sun-Strike Sword will be a bright blade. The Chill Spike will be a cold-themed thrusting sword. The Frozen Needle will be an icy rapier. The Aurora Blade will be a light-themed cold sword. The Ice Queen's Rapier will be a royal frozen blade. Zero Kelvin will be an ultimate freezing sword. The Searing Saber will be a hot blade. The Molten Rapier will be a liquid fire sword. The Blaze Edge will be a flaming blade. The Phoenix Tail will be a fiery magical sword. The Volcanic Spike will be a molten thrusting sword.

**J.4.6.2 Skills**

For the Magic Swordsman, Fire Blade, Ice Blade, Thunder Blade, and Wind Blade will add specific elements to physical attacks. Drain Blade will damage an enemy and restore the user's health. Aspir Blade will damage enemy mana to restore the user's mana. Magic Barrier will grant magic reflection to the user. Enchant Weapon will buff an ally's weapon with fire. Dispel Strike will remove enemy buffs on hit. Elemental Burst will consume all mana to deal damage. Arcane Slash will deal magic damage capable of critical hits. Spell Shield will grant immunity to the next magic spell received. Mystic Thrust will pierce magical defenses. Teleport Strike will execute a high evasion attack. Rune Breaker will deal massive non-elemental magic slash damage to foes.

**J.4.7 Hunter**

The Hunter class will specialize in long range attacks. Players will shoot bows to damage targets safely. This role will have access to various skills, for example, shooting multiple arrows at once or putting targets to sleep.

**J.4.7.1 Weapons**

The Hunter class will wield bows. The Short Bow will be a basic ranged weapon. The Oak Bow will be a standard wooden bow. The Hunter's Bow will be a tool for tracking. The Ranger's Crossbow will be a mechanical ranged weapon. The Vine Bow will be a nature themed weapon. The Elven Bow will be a mystical archery tool. The Bone Bow will be made from skeletal remains. The Sandstone Crossbow will be a desert-themed mechanical bow. The Scorpion Recurve will be an animal-themed desert bow. The Desert Wind Bow will be a sandy ranged weapon. The Golden Arrow will be an ornate projectile weapon. The Ice Crystal Bow will be a frozen ranged weapon. The Frostbite Crossbow will be a chilling mechanical bow. The Mammoth Ivory Bow will be a heavy prehistoric weapon. The Blizzard String will be a winter themed bow. The Glacial Shot will be a heavy frozen weapon. The Ash Wood Bow will be a burnt wooden bow. The Flame String will be a fiery ranged weapon. The Magma Rock Crossbow will be a molten mechanical bow. The Dragon Bone Bow will be a reptilian ranged weapon. The Phoenix Fire Bow will be a legendary flaming bow.

**J.4.7.2 Skills**

For the Hunter, Aim will guarantee the next attack will hit and critically strike. Power Shot will deal high damage after a charge turn. Rapid Fire will shoot multiple arrows at random targets. Poison Arrow, Sleep Arrow, Blind Arrow, and Silence Arrow will inflict specific status ailments on hit. Arrow Rain will deal physical damage to all enemies. Eagle Eye will increase precision and critical rate. Beast Slayer will deal massive damage against animals. Piercing Shot will ignore enemy defense. Camouflage will lower the user's aggro. Trap Set will damage enemies who physically attack the user. Snipe will deal high damage to low-health enemies. Hail of Arrows will deal heavy damage to all enemies and lower their agility.

**J.4.8 Bandit**

The Bandit class will rely on high speed and evasion to win fights. Players will use short daggers and knives to quickly strike targets. This role will have access to various skills, for example, draining the core statistics of the enemy.

**J.4.8.1 Weapons**

The Bandit class will wield daggers and knives. The Knife will be a simple utility blade. The Rusty Shiv will be an old, degraded dagger. The Hunter's Knife will be an animal-skinning tool. The Poison Tip will be a toxic dagger. The Thief's Shank will be a rogue's blade. The Forest Tooth will be a woodland dagger. The Curved Dagger will be a swept blade. The Sand Shiv will be a desert-themed knife. The Scorpion Barb will be an animal-themed desert dagger. The Tomb Blade will be an ancient knife. The Golden Dagger will be an ornate short blade. The Icicle Shiv will be a frozen knife. The Frozen Dagger will be a cold short blade. The Shard of Glass will be an improvised sharp tool. The Cold Steel Knife will be a pristine metallic dagger. The Frostbite Dirk will be a chilling short blade. The Obsidian Knife will be a dark volcanic dagger. The Heated Dagger will be a hot short blade. The Ember Shiv will be a smoldering knife. The Dragon Claw will be a reptilian short blade. The Hell's Tooth will be a demonic dagger.

**J.4.8.2 Skills**

For the Bandit, Steal will temporarily reduce an enemy's core statistics while granting those same stat boosts to the user. Mug will deal physical damage while simultaneously draining the enemy's statistics. Sneak Attack will deal high damage if used at the start of battle. Poison Edge will add a toxic effect to the dagger. Sand Throw will inflict blindness on one enemy. Smoke Bomb will provide a high chance to flee battle or blind all enemies. Backstab will provide a high critical chance. Sprint will greatly increase agility. Gold Snatch will steal coins from the enemy. Venom Strike will deal heavy damage to poisoned targets. Shadow Step will drastically increase evasion. Dirty Trick will carry a chance to stun the enemy. Twin Daggers will hit twice. Lucky Strike will scale damage based on the luck stat. Assassinate will carry a chance to instantly kill non-boss enemies.

**J.5 Buffs and Debuffs**

Combat will also be affected by various positive and negative status effects.

**J.5.1 Debuffs**

The negative states will act as debuffs. Knockout will prevent characters from acting until revived. Poison will cause continuous damage at the end of every turn. Blind will greatly reduce physical attack precision. Silence will prevent the usage of all magic skills. Confusion will force characters to attack random targets. Sleep will prevent characters from acting until they take damage. Paralysis will force the character to skip their turn entirely. Stun will make characters flinch and lose their current turn. Bleed will deal physical damage over time and reduce healing received. Burn will deal fire damage over time and lower attack power. Freeze will prevent action until physical damage shatters the ice. Slow will reduce agility, filling the action gauge much slower. Curse will double mana costs and prevent health regeneration. Weakness will lower all elemental resistances. Fear will prevent the use of special tactical skills.

**J.5.2 Buffs**

The positive states will act as buffs. Regenerate will restore a portion of health at the end of every turn. Haste will double agility to fill the action gauge faster. Protect will reduce physical damage taken. Shell will reduce magic damage taken. Focus will increase the critical hit rate. Magic Barrier will nullify the next magical attack received. Attack Up, Defense Up, Magic Up, and Agility Up will increase physical attack, physical defense, magic attack, and speed respectively. Evasion Up will add a chance to dodge physical attacks. Immortal will prevent health from dropping below one. Auto-Life will give a Hp boost, healing effectiveness and physical damage reduction. Reflect will bounce magic spells back at the caster. Counter Stance will guarantee a counter-attack against physical hits.

**J.6** **Equipment and Accessories**

Equipment options will further customize gameplay by providing stat boosts and elemental resistances.

**J.6.1 Shields**

Shields will provide various defensive benefits. Small Shields and Round Shields will provide basic protection. Bucklers will be lightweight shields. Kite Shields, Iron Shields, and Steel Shields will provide larger coverage and metal protection. Mythril Shields will be made of lightweight magical metal. Gold Shields will be highly decorative. Wooden Lids will be improvised village shields. Hunter's Bucklers will not hinder movement. Bronze Shields will be durable desert alloys. Scale Guards will resist fire. Shell Bucklers will resist water. Ice Shields will reduce ice damage. Crystal Guards will reflect minor spells. Frost Shields will chill physical attackers. Dragon Shields and Flame Guards will reduce fire damage. Obsidian Shields will be unbreakable dark shields. The Aegis will be the ultimate shield preventing instant death.

**J.6.2 Headgear**

Headgear will provide additional defense and stat bonuses when equipped. Leather Caps, Leather Helms, Iron Helmets, and Steel Helmets will provide varying degrees of physical protection. Mythril Helms will offer high defense with low weight. Full Helms will cover the entire head. Viking Helms will have horns. Dragon Helms will resist fire. Genji Helms will be legendary armor. Feathered Hats will be stylish. Magician's Hats will be pointy magic gear. Circlets will be simple metal bands. Ribbons will prevent status ailments. Bandanas will be worn by thieves. Turbans will protect against desert heat. Silk Hoods and Fur Hoods will provide climate and magic resistance. Ice Crowns and Salamander Coifs will provide elemental resistance. Royal Crowns will offer high overall stats.

**J.6.3** Body Armor

Body armor will serve as the character's main defensive equipment to reduce overall incoming damage. Cloth Tunics and Traveler's Tunics will be basic clothing. Leather Armor and Hard Leather will be light protection. Iron Armor, Steel Armor, Plate Mail, and Heavy Mail will be heavy metal plating. Mythril Armor will be made of magical metal. Scale Mail will use flexible overlapping scales. Glacial Mail and Flame Mail will resist extreme temperatures. Dragon Armor will be the ultimate elemental resistance gear. Hunter's Vests and Ninja Suits will provide camouflage and agility. Cotton Robes, Silk Robes, Sorcerer's Robes, and Sage's Robes will provide magical protection for spellcasters. Winter Robes and Lava Robes will provide elemental resistance for casters.

**J.6.4** Accessories

Accessories will provide specific utility benefits. Rings of Protection, Power, Magic, Speed, and Life will increase their respective core statistics. Poison Charms, Silence Amulets, Blindness Glasses, Paralysis Talismans, and Sleep Earrings will prevent specific status ailments. Fire, Ice, Thunder, and Earth Rings will reduce elemental damage taken. Gold Rings and Lucky Coins will increase post-battle rewards. Warrior's Badges will offer counter-attacks. Scholar's Specs will reveal enemy stats. Knight's Crests will start battles with defensive buffs. Sniper's Eyes will greatly increase precision.