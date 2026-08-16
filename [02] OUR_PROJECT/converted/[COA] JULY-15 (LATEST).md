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

Jan Nicole B. Apostol

Adviser

March, 2026

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

Jan Nicole B. Apostol

Adviser

March, 2026

**DOMINICAN COLLEGE OF TARLAC, INC.**

**DEAN’S ACCEPTANCE SHEET**

This Capstone Proposal entitled

**Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling.**

After having been recommended and approved is hereby accepted

by the College of Computer Studies,

Dominican College of Tarlac, Inc.

Rossano C. Samson

Dean

March, 2026

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

Airon Prince C. Beltran Crisha Cayabyab

Panelist Panelist

Gerald B. Tolentino

Lead Panelist

March, 2026

**TABLE OF CONTENTS**

**1.0 Introduction** 1

1.1 Project Context 1 -4

1.2 Story Overview 4-5

1.3 Biomes 5

1.3.1 Plains and Forest 5-8

1.3.2 Desert 6-8

1.3.3 Tundra and Forest 7

1.3.4 Volcano and Fire 7-8

1.4 Items 8-9

1.5 Character Classes 9

1.5.1 Swordsman 9-10

1.5.2 Sorcerer 10-11

1.5.3 Priest 11-12

1.5.4 Knight 12-14

1.5.5 Martial Artist 14-15

1.5.6 Magic Swordsman 15-16

1.5.7 Hunter 16-17

1.5.8 Bandit 17-18

1.6 Buffs and Debuffs 19

1.6.1 Debuffs 19

1.6.2 Buff 19

1.7 Equipment and Accessories 20

1.7.1 Shields 20

1.7.2 Headgear 20

1.7.3 Body Armor 21

1.7.4 Accessories 21

1.8 Objectives 21

1.8.1 General Objective 21

1.8.2 Specific Objectives 21-24

1.9 Scope and Limitations 24

1.9.1 Scope 24-54

1.9.2 Limitations 54-55

**2.0 Review of Related Literature / Systems** 56

2.1 Review of Related Theories 56

  2.1.1 Effectiveness of Game-Based Learning 56

  2.1.2 Mathematics Anxiety in Primary Education 56

2.1.3 Transformative Role-Playing Game Design 56-57

  2.2 Review of Related Projects 57

2.21 Mage Math 57-58

2.2.2 Grand Prix Multiplication 58-59

2.2.3 Prodigy Game 60-61

**3.0 Technical Background** 62

3.1 Development 62

3.1.1 Hardware 62

  3.1.2 Software 62-66

3.1.3 Peopleware 66

3.1.4 Network 66

3.2 Implementation 67

3.2.1 Hardware 67

3.2.2 Software 67

3.2.3 Peopleware 67-68

3.2.4 Network 68

**4.0 Methodology** 69

4.1 Prototyping Model 69

4.1.1 Requirements Gathering 69

4.1.2 Quick Design 70

4.1.3 Building Prototype 70

4.1.4 Customer Evaluation of Prototype 70

4.1.5 Refining Prototype 70

4.1.6 Engineer Product 70

4.2 Requirements Specification 71

4.2.1 Operational Feasibility 71-72

4.2.2 Technical Feasibility 72

4.2.2.1 Compatibility Checking 72-73

4.2.2.2 Relevance of the Technology 73

4.2.3 Schedule Feasibility 74-77

4.2.4 Economic Feasibility 77

4.2.4.1 Cost and Benefit Analysis 77

4.2.4.2 Cost Recovery Scheme 77-78

4.2.5 Requirements Modeling 78

4.2.5.1 Object Modeling 77-83

4.2.6 Risk Assessment 84

4.3 Design 84

4.3.1 Output and user-Interface Design 84-85

**LIST OF APPENDICES**

APPENDIX A. Work Assignment A1-5

APPENDIX B. Definition of Terms B1-2

APPENDIX C. Curriculum Vitae C1-5

**LIST OF TABLES**

Table # 1 November 2025 74

Table # 2 December 2025 74

Table # 3 January 2026 74

Table # 4 February 2026 74-75

Table # 5 March 2026 75

Table #6 April 2026 75

Table # 7 May 2026 75-76

Table # 8 June 2026 76

Table # 9 July 2026 76

Table # 10 August 2026 76

Table # 11 September 2026 76-77

Table # 12 October 2026 77

Table # 13 Cost and Benefits 77

**LIST OF FIGURES**

Figure No. 1 Mage Math Logo 57

Figure No. 2 Mage Math Gameplay 58 Figure No. 3 Grand Prix Multiplication Logo 58

Figure No. 4     Grand Prix Multiplication Gameplay 59

Figure No. 5     Prodigy Math Logo 60 Figure No. 6 Prodigy Gameplay 61

Figure No. 7     Prototyping Model 69

Figure No. 8     Fishbone Diagram 71

Figure No. 9     Functional Decomposition Diagram 72

Figure No. 10   Young Learner Use Case Diagrams 78

Figure No. 11   Level-Based Progression Sequence Diagram 80

Figure No. 12   Math Battle System Sequence Diagram 81

Figure No. 13   P2P Multiplayer Sequence Diagram 81 Figure No. 14   Save Sequence Diagram 82

Figure No. 15 Game Loop Chronicles of Arithmos 83

Activity Diagram

Figure No. 16 Dark Blue, Black and White 84

Figure No. 17 M+ 1m regular Font 85

1. **Introduction**
   1. **Project Context**

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

* 1. **Objectives**

**1.2.1 General Objective**

The primary objective of this project is to design and develop Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling.

**1.2.2 Specific Objectives**

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

**1.3 Scope and Limitations**

**1.3.1 Scope**

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

* 1. *Player Levels 1-29 (Basics): The game will make math problems that use addition and subtraction with two values. For example: 15 + 7.*
  2. *Player Levels 30-69 (Intermediate): The game will introduce Multiplication and Division operations. For example: 12 \* 4.*
  3. *Player Levels 70-100 (Advanced): The game will generate three part equations utilizing the full PEMDAS rules (Parentheses, Exponents, Multiplication, Division, Addition, Subtraction). For example: (10 + 5) \* 2.*

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

**1.3.2 Limitations**

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

**2.0 Review of Related Literature/Systems**

**2.1 Related Theories**

*2.1.1 Effectiveness of Game-Based Learning – Learning in Modern Education*

Game based learning is when a game handles the teaching instead of a teacher giving physical lecture and handing out a stack of worksheets. The approach in the game mechanics will enhance the students problem solving skills. A study by Wardoyo, Satrio, and Ma'ruf et .al (2023) found that kids who experienced gamified learning had shown significant improvement in their test scores. The students stayed motivated as they were having fun in the process.

Author: Cipto Wardoyo, Yogi Dwi Satrio, and Dudung Ma'ruf

Source:https://kneopen.com/kne-social/article/view/6844

Date Retrieved: Febuary 5, 2026

*2.1.2 Mathematics Anxiety in Primary Education*

Math anxiety is a state of bad stress from number tasks. It messes with working memory since the brain focus goes to fear instead of math. This happens to students aged 9 to 12 and makes them hate the subject. Proponents use games in teaching to lower stress and help grades.

Author: Zara Ersozlu

Source:https://www.cedtech.net/article/the-role-of-technology-in-reducing-mathematics-anxiety-in-primary-school-students-14717

Date Retrieved: Febuary 5, 2026

*2.1.3 Transformative Role-playing Game Design*

RPGs or role playing games are basically games where players pretend to be characters in a story. Because players have to make all the choices, they actually have to think and solve problems instead of just memorizing facts. This makes learning way less boring because the players are the ones in control of what happens next. Since they are not just sitting there listening, they stay focused much longer.

Author: Bowman, S. L., Diakolambrianou, E., & Brind, S. (Eds.)

Source: https://books.uu.se/uup/catalog/book/35

Date Retrieved: February 5, 2026

**2.2 Related Projects**

*2.2.1 Mage Math*

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

*2.2.2 Grand Prix Multiplication*

Developer: Arcademics Inc.

Date Published: 2016-05-17

Reference: <https://www.arcademics.com/games/grand-prix>

![IMG_256](data:image/png;base64...)

Figure No. 3 Grand Prix Multiplication Logo

Grand Prix Multiplication is a web-based and mobile racing game that helps students in Grades 3–5 practice multiplication. The system or Grand Prix Multiplication uses a competitive racing mechanism in which the avatar velocity is based on how quickly and accurately the player answers mathematical questions.

Both Grand Prix Multiplication and Chronicles of Arithmos use game mechanics to present mathematical problems. Both systems target elementary-level students and include multiplayer features that allow learners to interact with peers during gameplay.

Grand Prix Multiplication is a web-based racing game that requires an internet connection and focuses solely on multiplication speed drills. It does not include an exploration-based narrative or multi-step problem-solving scenarios. Chronicles of Arithmos is a 2D RPG with a narrative, covers multiple arithmetic operations (PEMDAS), and uses P2P local multiplayer rather than online matchmaking.

![arcagrand](data:image/png;base64...)

Figure No. 4: Grand Prix Multiplication Gameplay

*2.3.3 Prodigy Game*

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

**3.0 Technical Background**

**3.1 Development**

3.1.1 Hardware

*A. Personal Computers and Laptops*

The proponents will primarily use personal computers (PCs), desktop computers, mobile devices and laptops for documentation, system design, testing, and development of the proposed project.

3.1.2 Software

*A. Frontend*

*A.1 RPG Maker MZ*

RPG Maker MZ is a game development engine designed for creating 2D role-playing games. It will be used in the core application development to construct the visual environment, manage the database of enemies and items, and script game events. The proponents utilize this engine because its built-in architecture provides a framework for RPG mechanics (such as inventory and movement) while allowing for the addition of custom JavaScript plugins to create the "Math Battle System."

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

**3.1.3 Peopleware**

*A. The Proponents*

The proponents consisted of a project manager, a programmer, a UI UX designer, a tester, and a graphic designer. Each person executed specific tasks to complete the system according to the agreed standards. The project manager oversaw the overall development schedule and guided the team workflow. The programmer wrote the game scripts. The UI UX designer planned the visual layouts. The tester conducted the multiplayer network checks and recorded software bugs during the trials. Finally, the graphic designer created some of the assets like the game logo.

1. *Capstone Adviser*

Mr. Jan Nicole B. Apostol provided guidance, clarifications, and recommendations for the project. The adviser guided the proponents through the technicalities and documentation, provided necessary revisions, and verified that the system met the required formatting and quality standards.

**3.1.4 Network**

*A. Local Area Network (LAN) & Cloud Staging*

The proponents will test the multiplayer mode using two different network setups during development. First, the team will check the peer to peer connection and game data sync. They will do this by connecting multiple computers to the same Local Area Network or Wi Fi to make sure the game runs without lag. Next, the proponents will test the game using computers on completely different networks to observe how the system handles a Wide Area Network. This secondary test will prove that the Room Code connection stays stable over the public internet.

**3.2 Implementation**

3.2.1 Hardware

*A. Personal Computer or Laptop*

Users need a personal computer desktop or laptop to download, install, and play the main application of Chronicles of Arithmos. These devices process the local game files. They also allow the player to control the game using a keyboard and a mouse.

*B. Mobile Device*

Users need a mobile phone or tablet running the Android or iOS platform to open a web browser and play the online version of the game. These devices connect to the internet to load the game pages. They allow the player to interact with the screen using touch controls.

3.2.2 Software

*A. Operating System (OS)*

The game requires Windows 10 64 bit or higher. The NW js wrapper depends on 64 bit architecture to function [9]. Older systems can not run this. Mobile devices need Android 10 or iOS 14 at a minimum. These versions are needed to fully support WebGL 2.0 rules [10]. This tool powers the 2D visuals of the game.

*B. Modern Browsers*

Players will need a modern web browser to play. The proponents recommend Google Chrome or Microsoft Edge. These browsers run the WebGL graphics and Virtual Keypad of the game very well. These Chromium based browsers also support the WebRTC rules. The P2P multiplayer needs these rules to connect.

3.2.3 Peopleware

*A. Young Learners and General Users*

Primary school students between 9 and 12 years old will act as the primary players of the game. However, the system accommodates all possible users regardless of age. Children below 9 years old can play the game using the early difficulty stages to learn basic addition and subtraction. Older students and individuals above 12 years old can also play the game for casual entertainment or to refresh their mental calculation speed. These learners will use the battle system to solve math problems while they explore different biomes such as the tundra biome and finish the main story. By playing, all users can practice their math skills and improve how they calculate numbers.

3.2.4 Network

*A. Internet Connection*

The system required a stable internet connection to function properly. A minimum of 5 to 10 Mbps internet speed will be needed for the multiplayer mode or to load the web files on the web app version.

**4.0 Methodology**

**4.1 Prototyping Model**

According to Geeks for Geeks the Prototyping Model is a branch of the SDLC. It is basically making a bare bones version before the final game. This helps when the proponents do not have a super detailed plan at the start. Proponents can just build a simple version to get feedback and fix the code logic before wasting time on final product [11].

**![PROTOTYPING-MODEL-NO-MAINTENANCE](data:image/png;base64...)**

Figure No. 7 : Prototyping Model

The proponents went with the Prototyping Model because the math inside Chronicles of Arithmos is just too messy to figure out on paper. Specific numbers like how fast a timer runs or how hard a monster hits have to be tested to make sure they are not too tough for players playing Chronicles of Arithmos. If the proponents used a stiff plan like the Waterfall Model, they could not change those values easily later. Instead, this model lets the proponents fix the balance based on what the students or young learners say while they are actually playing the game.

The following are the phases of the Prototyping Model:

#### 4.1.1 Requirements Gathering

In this phase, the proponents looked at the DepEd math lessons for young learners in Grade 4 to 6 to see what math to put in. They looked at basic plus and minus plus the harder PEMDAS too. The proponents also played Prodigy Math to see what their own game should do. By the end they had a list of what the game needs and what math to put in Chronicles of Arithmos.

#### 4.1.2 Quick Design

In the next phase, the proponents made flowcharts and drawings to show how the game and buttons would look. These drawings show how a player goes from the menu to a fight. They also made storyboards for the Forest and Desert and other areas to plan where the monsters live and how the maps connect to each other.

#### 4.1.3 Building Prototype

The proponents used RPG Maker MZ to make the first or initial version, RPG Maker MZ allows the to make maps and monster stats. The proponents wrote a custom plugin script in JavaScript so the game can give math problems and check if the player is right. They also added a timer for the fights and used PeerJS so players can invite friends to play together. They finished the first few maps like the Forest to start with.

#### 4.1.4 Customer Evaluation of Prototype

The proponents will find 10 students or young learners aged 9 to 12 typically from Grade 4 to 6 to play the game. The proponents will watch them to see if the game is easy or if the math is too hard to read. What the young learners or children say will help the proponents decide what to fix before they make the next version.

#### 4.1.5 Refining Prototype

After the young learners play it, the proponents will fix the game and do the whole design and build part all over again. This happens two times. The proponents will change how hard the monsters are if they are too easy or too tough. They will also fix the buttons if they are too small for a phone screen and fix the multiplayer part.

#### 4.1.6 Engineer Product

In the last phase, the proponents will make a final version that works on computers assuming the computers have the specific requirements needed, and on modern browsers. The proponents will check one last time to make sure the math and the multiplayer part works. Then they will put the game online and make a file or the .exe file so it can be downloaded and be played.

**4.2 Requirements Specification**

**4.2.1 Operational Feasibility**

1. *Fishbone Diagram*

![FISHBONE-GEL.drawio](data:image/png;base64...)

Figure No. 8: Fishbone Diagram

1. *Functional Decomposition Diagram*

![Decision Path Option-2026-03-11-050023](data:image/png;base64...)

Figure No. 9: Functional Decomposition Diagram

**4.2.2 Technical Feasibility**

**4.2.2.1 Compatibility Checking**

1. *Hardware Compatibility*

The proponents made the game with RPG Maker MZ. It runs on computers with assuming the computers have 8 GB of RAM and the proponents checked that an Intel Core i3 can handle it. Since there is a web version too, it works on tablets or any computer with a modern browser. This lets players jump into the math battles without downloading any executable files.

1. *Software Compatibility*

Since RPG Maker MZ runs on JavaScript, the math engine was built using that same language. This letss the math logic and the combat mechanics work together without needing any extra fixes or translations or conversion of code to another programming language. For the multiplayer part, the proponents used PeerJS so players can just use room codes to connect. This way, the game allows player to play without needing a server to run everything.

**4.2.2.2 Relevance of the Technology**

Prodigy and Math Blaster are basically a turn-based RPGs where math is the button the player presses to attack. Players get the answer right, the animation plays, and that’s it. It’s a bit disconnected. Chronicles of Arithmos actually ties your brain speed to the sword swing, in a sense, the player solving math is equivalent to a sword swing. Instead of just "Right = Hit," it uses a Performance-Based Reward system. If a player is really good ath math and accurate too, players can pull off a 2.0x Critical Hit. If the player is slow and stumble, the player might totally miss.

JavaScript (ES6) was chosen because it is the native scripting language of RPG Maker MZ, allowing the proponents to implement the Math Battle Engine and Content-Aware Timer without external dependencies. PeerJS, a WebRTC (Web Real-Time Communication) library, was selected for the multiplayer module as it enables direct Peer-to-Peer connections through room codes without requiring a dedicated server.

The proposed title deploys as a Windows desktop application via NW.js (Node Webkit) and as a web application hosted on Hostinger using HTML5 and Web Graphics Library (WebGL). Desktop is the primary platform because the Math Battle System requires timed numerical input through a physical keyboard, which touchscreens cannot replicate due to the absence of a physical key-press sensation (haptic feedback). The desktop executable can also operate offline using a computer. The web deployment serves as a secondary access point, supported by the Virtual Numeric Keypad module for touch-enabled devices.

**4.2.3 Schedule Feasibility**

1. *Gantt Chart*

*Table #1 November 2025 Gantt Chart*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| 1. Capstone Orientation |  |  |  |  |
| 1. Grouping of Capstone Members |  |  |  |  |
| 1. Planning and Brainstorming |  |  |  |  |
| 1. Capstone Adviser Selection |  |  |  |  |

*Table #2 December 2025 Gantt Chart*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| 1. Requirements Gathering |  |  |  |  |
| 1. Quick Design |  |  |  |  |

*Table #3 January 2026 Gantt Chart*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| 1. Building Initial Prototype |  |  |  |  |
| 1. Preparation for Title Defense |  |  |  |  |
| 1. Title Defense |  |  |  |  |
| 1. Capstone Adviser Consultation |  |  |  |  |
| 1. Dean Consultation |  |  |  |  |
| 1. Documentation (Chapter 1) |  |  |  |  |

*Table #4 February 2026 Gantt Chart*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| 1. Documentation (Chapter 2) |  |  |  |  |
| 1. Documentation (Chapter 3) |  |  |  |  |
| 1. Capstone Adviser Consultations |  |  |  |  |
| 1. Documentation (Chapter 4) |  |  |  |  |

*Table #5 March 2026 Gantt Chart*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| 1. Building Initial Prototype (Continued) |  |  |  |  |
| 1. AI & Plagiarism Checking |  |  |  |  |
| 1. AI & Plagiarism Checking |  |  |  |  |
| 1. Preparation for Oral Defense |  |  |  |  |
| 1. Oral Defense |  |  |  |  |

*Table #6 April 2026 Gantt Chart*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| 1. Customer Evaluation of Prototype |  |  |  |  |
| 1. Refining Prototype |  |  |  |  |
| 1. Quick Design |  |  |  |  |

*Table #7 May 2026 Gantt Chart*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| 1. Building Prototype |  |  |  |  |
| 1. Customer Evaluation of Prototype |  |  |  |  |
| 1. Capstone Adviser Consultation |  |  |  |  |

*Table #8 June 2026 Gantt Chart*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| 1. Refining Prototype |  |  |  |  |
| 1. Capstone Adviser Consultation |  |  |  |  |

*Table #9 July 2026 Gantt Chart*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| 1. Unit Testing |  |  |  |  |
| 1. Integration Testing |  |  |  |  |
| 1. Capstone Adviser Consultation |  |  |  |  |

*Table #10 August 2026 Gantt Chart*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| 1. System Testing |  |  |  |  |
| 1. Acceptance Testing |  |  |  |  |
| 1. Engineer Product |  |  |  |  |
| 1. Implementation Plan |  |  |  |  |
| 1. Capstone Adviser Consultation |  |  |  |  |

*Table #11 September 2026 Gantt Chart*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| 1. Engineer Product (Continued) |  |  |  |  |
| 1. Final Documentation (Chapter 5) |  |  |  |  |
| 1. Capstone Adviser Consultation |  |  |  |  |
| 1. Updating, Reviewing, and Revision of the whole document |  |  |  |  |

*Table #12 October 2026 Gantt Chart*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| 1. Capstone 2 Defense |  |  |  |  |

**4.2.4 Economic Feasibility**

**4.2.4.1 Cost and Benefit Analysis**

The cost and benefit analysis provides a breakdown of the materials required for development and the specific value each item brings to the study. The proponents have categorized these costs into software and hosting expenses.

Table #13 Cost and Benefits Table

|  |  |  |  |
| --- | --- | --- | --- |
| Category | Item | Cost | Benefits |
| Software | RPG Maker MZ (2 License) | ₱4,600.00 | Allows the proponents to develop and test the game concurrently, and provides a built-in event system, and map editor that can reduce the time needed to build the Active Time Battle (ATB) interface and Math Engine from scratch. |
| Hosting | Hostinger Domain & Web Hosting (5 years) | ₱12,108.00 | Allows students to access the game from home through a web browser without requiring a separate installation or a computer |
| TOTAL | Investment Required | ₱16.708.00 |  |

**4.2.4.2 Cost Recovery Scheme**

The proponents personally fund the total development cost of ₱16,708.00 since the project is part of their academic requirements. Chronicles of Arithmos stays completely free for students and teachers so they can practice their arithmetic without paying for access. To recover the development costs and pay for the Hostinger servers after the five-year plan expires, the proponents plan to set up a voluntary donation page like Patreon or "Buy Me a Coffee" where parents can send financial support if they like the game.

**4.2.5 Requirements Modeling**

**4.2.5.1 Object Modelling**

1. *Use Case Diagrams*

![Copy of Usecase Student.drawio](data:image/png;base64...)

Figure No. 10: Young Learner Use Case Diagrams

1. *Sequence Diagrams*

*![Sequence Auto Quest.drawio (2)](data:image/png;base64...)*Figure No. 9: Auto Quest Sequence Diagram

![Sequence Enemy Auto-Scaling System.drawio](data:image/png;base64...)

Figure No. 10: Enemy Auto-Scaling Sequence Diagram

![Sequence Level-Based Progression System.drawio](data:image/png;base64...)Figure No. 11: Level-Based Progression Sequence Diagram

![Sequence Math Battle System.drawio (2)](data:image/png;base64...)

Figure No. 12: Math Battle System Sequence Diagram

![Sequence P2P multiplayer.drawio (2)](data:image/png;base64...)

Figure No. 13: P2P Multiplayer Sequence Diagram

![Sequence Save.drawio (1)](data:image/png;base64...)

Figure No. 14: Save Sequence Diagram

1. *Activity Diagrams*

*![Activity Diagram.drawio](data:image/png;base64...)*

Figure No. 15: Game Loop Chronicles of Arithmos Activity Diagram

**4.2.6 Risk Assessment/Analysis**

Developing Chronicles of Arithmos comes with risks that the proponents have identified and prepared for. The proponents have limited experience with JavaScript and PeerJS, which may cause technical delays in building the Math Battle System and multiplayer features and differences between the desktop, web, and mobile versions may cause inconsistencies. The large project scope may lead to schedule delays, while players or young learners may lose interest if math overshadows the gameplay.

External dependencies such as PeerJS and NW.js may receive breaking updates, and students' computers may lack adequate hardware or internet access. To reduce these risks, the proponents will study online resources and consult the proponents Capstone Adviser for guidance, Mr. Jan Nicole B. Apostol, lock software versions during development, prioritize core features first with remaining items as stretch goals, review early prototypes for gameplay balance, offer an offline single-player option via windows executable application as a fallback when students are not playing via the web application.

**4.3 Design**

**4.3.1 Output and User-interface Design**

The proponents designed the interface for Chronicles of Arithmos using a 2D pixel art style for all game assets and entities. The color scheme uses deep blue (#005385) for menu outlines and for active buttons that are currently pressed. Black (#000000) serves as the background color for all buttons and menu windows. White (#FFFFFF) is used for all text, mathematical equations, and numerical values.

(Hex: #005385) (Hex: #000000) (Hex: #FFFFFF)

![C:/Users/Angel/Downloads/Documents/Frame 1.pngFrame 1](data:image/png;base64...)![](data:image/png;base64...)![C:/Users/Angel/Downloads/Documents/Frame 2.pngFrame 2](data:image/png;base64...)

Figure No. 16 : Dark Blue, Black and White

The proponents chose the M+ 1m regular font as it is a typeface made for clear reading with uses that range from digital signs and multilingual systems, to computer screens and tools for writing code.

**![FONT-DESIGN-FIGURE](data:image/png;base64...)**

Figure No. 17: M+ 1m regular Font

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

[11] "Prototyping Model - Software Engineering," GeeksforGeeks, Jul. 11, 2025. [Online]. Available: <https://www.geeksforgeeks.org/software-engineering/software-engineering-prototyping-model/>

**APPENDICES**

**APPENDIX A. Work Assignments**

![](data:image/png;base64...)**![](data:image/png;base64...)**

**DOMINICAN COLLEGE OF TARLAC**

Mc Arthur Highway, Poblacion, Capas 2315, Tarlac, Philippines

**College of Computer Studies (CCS)**

|  |
| --- |
| Title of Project: Date: March, 2026  **Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling** |
| Name of the proponent: **Panganiban, Justine T. Signature:** |

**Project Participation:**

* Participated in Composing Fishbone Diagram
* Participated in Documentation Chapter 2

**APPENDIX A. Work Assignments**

![](data:image/png;base64...)**![](data:image/png;base64...)**

**DOMINICAN COLLEGE OF TARLAC**

Mc Arthur Highway, Poblacion, Capas 2315, Tarlac, Philippines

**College of Computer Studies (CCS)**

|  |
| --- |
| Title of Project: Date: March, 2026  **Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling** |
| Name of the proponent: **Guevarra, John Angel D. Signature:** |

**Project Participation:**

* Project Manager
* Participated in Brain Storming
* Participated in Documentation Chapter 1
* Participated in Documentation Chapter 2
* Participated in Documentation Chapter 3
* Participated in Documentation Chapter 4
* Participated in System Designing
* Composed APPENDIX A

**APPENDIX A. Work Assignments**

![](data:image/png;base64...)**![](data:image/png;base64...)**

**DOMINICAN COLLEGE OF TARLAC**

Mc Arthur Highway, Poblacion, Capas 2315, Tarlac, Philippines

**College of Computer Studies (CCS)**

|  |
| --- |
| Title of Project: Date: March, 2026  **Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling** |
| Name of the proponent: **Lacsina, Justine C. Signature:** |

**Project Participation:**

* Participated in Brain Storming
* Participated in Documentation Chapter 2
* Participated in Documentation Chapter 3
* Participated in Documentation Chapter 4
* Composed APPENDIX B

**APPENDIX A. Work Assignments**

![](data:image/png;base64...)**![](data:image/png;base64...)**

**DOMINICAN COLLEGE OF TARLAC**

Mc Arthur Highway, Poblacion, Capas 2315, Tarlac, Philippines

**College of Computer Studies (CCS)**

|  |
| --- |
| Title of Project: Date: March, 2026  **Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling** |
| Name of the proponent: **Quinez, John Benedict D. Signature:** |

**Project Participation:**

* Participated in Brain Storming
* Composed Documentation Chapter 1
* Composed Documentation Chapter 3
* Participated in System Designing
* Lead Programmer
* Composed Sequence Diagrams
* Composed Activity Diagrams

**APPENDIX A. Work Assignments**

![](data:image/png;base64...)**![](data:image/png;base64...)**

**DOMINICAN COLLEGE OF TARLAC**

Mc Arthur Highway, Poblacion, Capas 2315, Tarlac, Philippines

**College of Computer Studies (CCS)**

|  |
| --- |
| Title of Project: Date: March, 2026  **Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling** |
| Name of the proponent: **Manalo, Allan Joshua C. Signature:** |

**Project Participation:**

* Participated in Brain Storming
* Participated In Composing APPENDIX A
* Participated in Documentation Chapter 2
* Participated in Documentation Chapter 4

**APPENDIX B. Definition of Terms**

1. **Adaptive Difficulty Scaling – The system that ensures math equation complexity and enemy statistics remain proportional to the player's level throughout the game.**
2. **Arithmetic Operations – The mathematical computations generated during combat, includingaddition, subtraction, multiplication, division, and PEMDAS equations based on character level.**
3. **ATB Timer – The fight clock in the game. It shows a bar that fills up, but it stops when a math question pops up so the player can think without getting hit.**
4. **Automatic Quest Generation System – The module that automatically creates side quests basedonunlocked areas, offered through Receptionist Mila.**
5. **Biome – One of four geographical regions (Plains and Forest, Desert, Tundra and Frost, VolcanoandFire) featuring unique enemies, loot, and visual themes.**
6. **Content-Aware Timer System – The module that dynamically calculates the time limit for answering math equations based on their complexity, length, and operators.**
7. **Enemy Auto-Scaling System – The module that automatically adjusts enemy statistics and rewardsbased on the party's average level, ensuring consistent difficulty.**
8. **Experience Points (EXP) – Numerical rewards earned from combat and quests that increase character level, unlocking new areas and harder equations.**
9. **Flowcharts – Visual represantation that show how a student moves through menus or battle screens during the planning stage.**
10. **Gold – The in-game money players get from quests. They use it to buy better items to help them stay alive in the game.**
11. **HP – This stands for health. It shows how much damage a character can take in the fight.**
12. **JavaScript – The main coding language used for the game.**
13. **Math Battle – Main part of the game, it replaces regular fighting with math questions that the player must solve.**
14. **Math Engine – The logic that creates the random math equations and sets the timer for each question.**
15. **Math Levels – This system picks the math type based on level. Easy plus and minus are for levels 1 to 29, while PEMDAS starts at level 70.**
16. **MP – The points that used to cast magic spells during a fight.**
17. **NPC – The characters that the player does not control, like the people standing around in towns.**
18. **Numeromancer – The main bad guy of the story. The final boss who caused all the math trouble in the game.**
19. **NW.js – A tool that turns the web game into a file for Windows. This lets kids play the game on a computer without the internet.**
20. **P2P Multiplayer – This lets two players play together using a room code.**
21. **PeerJS – A coding tool that handles the multiplayer room codes and the connection between players.**
22. **PEMDAS – The rule for which math part to solve first.**
23. **Pixel Art – A blocky 2D art style used for all the characters and the maps in the game.**
24. **Plains of Origin – This is the first map where the player learns how to play.**
25. **Progression – The module that keep the track of where the player is in the story.**
26. **Quest Maker – This is a system that makes new jobs/quest for the player to do.**
27. **Reward System – The module that gives the player a reward at how fast and right a player is.**
28. **Room Code – A short password that used to join a friend in the multiplayer mode.**
29. **RPG – A type of game where players level up a character and follow a story.**
30. **RPG Maker MZ – The software that the proponents used to build the game.**
31. **Status Effects – These are temporary changes that affect a character during battle.**
32. **TP – Points that players earn and spend to use special skills in the battle.**
33. **Training Dummy – A practice monster that cannot die.**
34. **Training Hall – This is a safe place in the towns. Players can go here to practice math or testing their skills for free.**
35. **Vercel – A online platform that used to host the game on the web while the proponents were still building it.**
36. **WebGL – A tool that helps the web browser show the game graphics smoothly using the computer hardware.**
37. **WebRTC (Web Real-Time Communication) – The browser-standard protocol enabling direct peerto-peer multiplayer connections.**
38. **Wireframe – Low-fidelity sketches used to plan the interface layout during the Quick Design phase.**

**APPENDIX C.**

**Curriculumn Vitae**

![C:/Users/justi/Downloads/ChatGPT Image Feb 28, 2026, 01_08_18 AM.pngChatGPT Image Feb 28, 2026, 01_08_18 AM](data:image/png;base64...)Justine T. Panganbian

Concepcion, Tarlac

09858330350

Justinepanganiban96@gmail.com

**Personal Information**

Age: 24

Sex: Male

Date of Birth: November 8, 2001

Religion: Roman Catholic

Nationality: Filipino

Civil Status: Single

**Information**

Tertiary: Dominican College of Tarlac. Capas, Tarlac.

Bachelor of Science in Information Technology

Secondary: Benigno S. Aquino National High School

Concepcion, Tarlac

Information and Communication Technology (ICT)

Primary: North Elementary School

Concepcion, Tarlac

**APPENDIX C.**

**Curriculumn Vitae**

![IMG_256](data:image/jpeg;base64...)

John Angel D. Guevarra

Concepcion, Tarlac

09762802968

johnangelguevarra@gmail.com

**Personal Information**

Age: 22

Sex: Male

Date of Birth: June 6, 2004

Religion: Roman Catholic

Nationality: Filipino

Civil Status: Single

**Information**

Tertiary: Dominican College of Tarlac. Capas, Tarlac.

Bachelor of Science in Information Technology

Secondary: Capas National High School

Capas, Tarlac

General Academic Strand (GAS)

Primary: San Juan Elementary School

Concepcion, Tarlac

**APPENDIX C.**

**Curriculumn Vitae**

**![New Project 2 [8700FC5]](data:image/png;base64...)**

**Justine C. Lacsina**

**Lawy, Capas, Tarlac
09502581534**justinelacsina@gmail.com

**Personal Information**

**Age: 21
Sex: Male
Date of Birth: July 1, 2004
Religion: Roman Catholic
Nationality: Filipino
Civil Status: Single**

**Educational Background**

**Tertiary: Dominican College of Tarlac, Capas, Tarlac
Bachelor of Science in Information Technology**

**Secondary: St. Nichole's Technical School
Capas, Tarlac**

Information and Communication Technology (ICT)

**Primary: Lawy Elementary School
Lawy, Capas, Tarlac**

**APPENDIX C.**

**Curriculumn Vitae**

**![C:/Users/justi/Downloads/benedik.pngbenedik](data:image/png;base64...)**

**John Benedict D. Quinez**

**Regina Nortview, Cut-cut 1st, Capas, Tarlac
09984958395
johnbenedictquinez@gmail.com**

**Personal Information**

**Age: 20
Sex: Male
Date of Birth: July 1, 2005
Religion: Roman Catholic
Nationality: Filipino
Civil Status: Single**

**Educational Background**

**Tertiary: Dominican College of Tarlac, Capas, Tarlac
Bachelor of Science in Information Technology**

**Secondary: Dominican College of Tarlac, Capas, Tarlac**

Information and Communication Technology (ICT)

**Primary:Lightgiver Christian School
Capas, Tarlac**

**APPENDIX C.**

**Curriculumn Vitae**

**![C:/Users/justi/Downloads/41e19c07-142a-4dcd-a9df-76a34232495f.png41e19c07-142a-4dcd-a9df-76a34232495f](data:image/jpeg;base64...)**

**Allan Joshua C. Manalo**

**Capas, Tarlac
09637081134
allanjoshmanalo25@gmail.com**

**Personal Information**

**Age: 20
Sex: Male
Date of Birth:September 9, 2005
Religion: Roman Catholic
Nationality: Filipino
Civil Status: Single**

**Educational Background**

**Tertiary: Dominican College of Tarlac, Capas, Tarlac
Bachelor of Science in Information Technology**

**Secondary: Capas National High School
Capas, Tarlac**

SPORTS

**Primary: Capas East Central School
Capas, Tarlac**

**APPENDIX D.**

**D.1 Story Overview**

The narrative of Chronicles Of Arithmos specifically starts in the Plains of Origin. The main character wakes up to discover a world filled with monsters. Guided by Bron, a mentor for physical combat, and Martha, a main mentor character for magical combat, the player will complete a tutorial. Players will discover that a curse affects Lily, the younger sister of the main character. The protagonist will need to restore the worlds logic to cure her condition.

The main character will travel through four separate biomes. A corrupted elemental force will guard each area. Players will fight the Forest Golem, Pharaoh's Guard, Fenrir wolf, and Demon Lord to recover story fragments. This journey will eventually end in the Void Dimension. Here, the player will face The Numeromancer. This final boss causes the chaos, and players will use math and combat skills to defeat him and fix the realm.

The game will involve the player forming an alliance to accomplish this mission. Kael will be initiated into the group as a knight. Elara will also bring spellcraft as a sorceress. Garrick will also act as a heavy-duty defender. Sylas the bandit and Isolde the priest will also be enlisted to the group. Other members will include Thorne as a hunter, Lyra as a magic swordsman and Fenrin as a monk.

Game mechanics will be strengthened by major supporting characters. Elder Tobias will direct the player on where to head next. The further movement of the player will be guided by Captain Valerius. There will be several positions which will monitor the buying and selling of items. Merchant Oryn will be selling general merchandise and buying enemy drops. Potions will be administered by alchemist Vanya. There will be blacksmith Rurik who will sell equipment. Innkeeper Gorm will give health and mana-regeneration.

Additional characters will provide certain services. Quest-generated hubs will be based around receptionist Mila. Bard Jareth and Priestess Anara will heal party and nullify negative statuses. Professor Haze will man the training facility. Players will learn where enemies appear with the help of Librarian Estel. The party can have their TP charged from Hunter Kaelen. Portal Keeper Alden will also allow users to create or join multiplayer. Extra dialogue will be offered by characters such as Widow Claire, Guard Captain Aris, and Street Urchin Pip. There will be background Npc’s that might give items like Farmer Ben, Nobleman Caelus and Fisherman Old Tom.

The towns will also include generic non-interactive characters to fill the environment. Examples of these characters are normal townspeople, playing children, tavern regulars, merchants, and security guards at the castle. It will also be included in the maps with stable boys, street sweepers, beggars, and walking couples to develop a dynamic atmosphere. Students, tourists, drunkards and street performers will be the visual only characters.

The ambient music will be used to complement the visual aesthetics in the game and reduce mathematical anxiety. Music tracks will be different depending on the place of location. Rhythmic patterns will see players experience compositions of calmness in the town, active tunes in battles, and relaxed tunes in dungeons. There will be unique biomes that present particular enemies and loot gathering chance in the game environment.

**D.2 Biomes**

**D.2.1 Plains and Forest**

The first zone or level of the game will be the Plains and Forests where the story begins. Players will be given the chance to openly explore the first area/zone to fight early level monsters and to collect basic items. The Forest Golem known as the corrupted elemental will be guarding the end of the region.

**D.2.1.1 Enemies & Drops**

The slime in Chronicles of Arithmos will drop Green Gel. The Rat will drop a Rat Tail. The Bat will drop a Bat Wing. The Spider will drop a Sticky Web. The Hornet will drop an Insect Wing. The Wolf will drop a Wolf Pelt. The Bear will drop a Bear Claw. The Treant will drop a Living Branch. The Goblin and Goblin Archer will drop Goblin Cloth. The Goblin Shaman will drop Shaman Beads. The Orc will drop an Orc Tusk. The Bandit and Bandit Leader will drop a Stolen Coin Purse. The Crow will drop a Shiny Feather. The Snake will drop Snake Skin. The Fairy will drop Fairy Dust. The Mandrake will drop a Mandrake Root. The Wild Boar will drop Boar Meat. The Forest Golem will drop Ancient Bark.

**D.2.2 Desert**

The Deserts will serve as harsh drylands for the party to explore. Players will travel across this sandy area to face harder monsters and gather new items. A corrupted elemental force known as the Pharaoh's Guard will block the end of this region.

**D.2.2.1 Enemies & Drops**

The Sand Slime will drop Yellow Gel. The Scorpion and Giant Scorpion will drop Scorpion Stingers. The Cactus will drop a Cactus Flower. The Sand Worm, Ant Lion, and Dust Spirit will drop Sand Essence. A Mummy will drop an Old Bandage. Players will get a Bone Fragment from the Skeleton Warrior, and the Skeleton Mage will drop a Skull. Fighting a Desert Wolf will give the player Dry Fur. The Lamia will drop a Snake Scale. When a user defeats a Basilisk, the creature will leave a Petrified Eye. The Gargoyle and Sand Golem will give a Stone Wing and a Sandstone Block. A Vulture will drop a Vulture Beak. Players will get a Riddle Tablet from the Sphinx, and the Ancient Scarab will drop a Scarab Shell. Both the Desert Rogue and the Pharaoh's Guard will drop Golden Fragments.

**D.2.3 Tundra and Frost**

The Tundra and Frost regions will serve as massive frozen expanses. Players will navigate these cold zones to battle ice enemies and collect rare loot. A corrupted elemental force known as the Fenrir wolf will guard the final part of this area.

**D.2.3.1 Enemies & Drops**

In these cold zones, the Ice Slime will drop Blue Gel. The Snow Wolf will drop a Wolf Fang. The Polar Bear will drop Thick Hide. The Ice Bat and White Tiger will drop White Fur. The Snow Spirit and Winter Wisp will drop Cold Wisps. The Yeti will drop a Yeti Horn. The Ice Golem will drop a Permafrost Shard. The Crystal Spider will drop a Crystal Leg. The Frost Giant and Frozen Knight will drop Frost Metal. The Corrupted Penguin will drop a Corrupted Feather. The Ice Drake will drop a Drake Scale. The Wendigo and Frost Mage will drop Frozen Hearts. The Glacial Turtle will drop an Ice Turtle Shell. The Snow Harpy will drop a Harpy Feather. The Ice Elemental will drop an Ice Crystal. The Fenrir will drop a Snowflake Core.

**D.2.4 Volcano and Fire**

The Volcano and Fire zones will act as the most dangerous harsh wasteland. Players will fight through this extreme heat to survive very strong enemies and find the best materials. A corrupted elemental force known as the Demon Lord will wait at the end of this region.

**D.2.4.1 Enemies & Drops**

The Magma Slime will drop Red Gel. The Fire Spirit and Fire Elemental will drop Embers. The Imp will drop an Imp Wing. The Demon and Minotaur will drop Demon Horns. The Succubus will drop Succubus Cloth. The Cerberus will drop a Hellhound Fang. The Lava Golem will drop an Obsidian Shard. The Fire Bat will drop a Fire Gland. The Salamander and Dragon Hatchling will drop Red Scales. The Red Dragon will drop a Dragon Tooth. The Efreet will drop a Djinn Lamp. The Phoenix will drop Phoenix Ash. The Iron Giant will drop Iron Scraps. The Dark Knight will drop Dark Armor Pieces. The Cultist will drop a Forbidden Page. The Chimera will drop a Chimera Tail. The Demon Lord will drop an Infernal Core.

**D.2.5 General Areas and Dungeons**

General areas and dungeons throughout the game will provide different types of enemy encounters. Players will face common enemies scattered across every map region to collect basic items. They will also explore hidden dungeon spaces to fight special monsters that drop rare essences and fragments.

**D.2.5.1 Enemies & Drops**

The Ghost and Shadow will drop Ectoplasm. The Zombie will drop Rotten Flesh. The Vampire and Vampire Bat will drop Vampire Fangs. The Mimic and Magic Pot will drop Unknown Fluid. The Will-o'-the-Wisp will drop Spirit Dust. The Animated Armor and Flying Sword will drop Haunted Metal. The Gazer will drop an Evil Eye. The Ogre and Troll will drop Ogre Clubs. The Warlock will drop Magic Powder. The Necromancer will drop a Tattered Robe. The Reaper will drop a Chaos Mote. The Ceramic Shard will drop randomly in general dungeons. The Chaos Cloud, Number Eater, Equation Spirit, and The Unknown will drop Arithmetic Essences and Void Fragments.

**D.3 Items**

Items will support gameplay with various consumables. Potions, Hi-Potions, and Full Potions will restore health. Magic Waters, Hi-Magic Waters, and Elixirs will restore mana or both health and mana. Antidotes, Eye Drops, Echo Herbs, Stimulants, Potent Stimulants, Panaceas, and Dispel Herbs will cure negative status ailments. Escape Ropes and Repel Sprays will help players avoid or leave battles. Permanent stat boosters like HP Up, MP Up, Strength Seeds, Defense Seeds, Magic Seeds, Agility Seeds, Luck Seeds, and Skill Books will permanently upgrade a character's core attributes.

**D.4 Character Classes**

Players will choose from eight distinct character classes, each with access to a specialized weapon arsenal and skill set that will expand as the player progresses.

**D.4.1 Swordsman**

The Swordsman class will focus on heavy physical strikes to damage monsters. Players will equip swords to act as their main weapon during encounters. This role will have access to various skills, for example, lowering the defense of targets or hitting all enemies at once.

**D.4.1.1 Weapons**

The Swordsman class will wield swords, The Long Sword will be a standard issue blade. The Woodcutter's Blade will be a simple cutting tool. The Wolf Fang Sword will be an animal-themed blade. The Forest Cutter will be a nature themed sword. The Bandit's Edge will be a thief's blade. The Verdant Blade will be a green sword. The Sand Scimitar will be a desert curved sword. The Scorpion Tail will be a stinger-shaped sword. The Dune Blade will be a sandy sword. The Sun-Scorched Sword will be a heat-themed sword. The Ancient Khopesh will be an old desert blade. The Ice Brand will be a cold-forged sword. The Glacial Edge will be a frozen sword. The Frostbite Sword will be a chilling blade. The Crystal Saber will be a crystalline sword. The Blizzard Blade will be a winter themed sword. The Magma Blade will be a molten sword. The Dragon Bone Sword will be crafted from dragon remains. The Infernal Edge will be a demonic blade. The Flame Tongue will be a fire-forged sword. The Phoenix Feather Sword will be a legendary fiery sword.

**D.4.1.2 Skills**

For the Swordsman, Strong Attack will deliver a heavy physical strike. Slash will execute a basic sword technique. Double Slash will hit the enemy twice in succession. Wide Swing will deal physical damage to all enemies. Armor Break will damage an enemy and lower their defense. Blade Bash will strike with the flat of the blade with a chance to stun. Focus will increase the critical hit rate. Parry will greatly increase evasion. Sonic Wave will deal ranged wind damage. Wind Slash will perform a wind elemental physical attack. Power Break will damage an enemy and lower their attack. Mind Break will damage an enemy and lower their magic attack. Berserk Stance will increase attack but lower defense. Cross Cut will perform two intersecting slashes. Omnislash will execute rapid strikes against random targets.

**D.4.2 Sorcerer**

The Sorcerer class will rely on elemental magic to deal high damage. Players will wield staves and rods to attack their targets. This role will have access to various skills, for example, shooting fire at a single enemy or absorbing mana from monsters.

**D.4.2.1 Weapons**

The Sorcerer class will wield staves and rods. The Oak Staff will be a basic wooden staff. The Briar Rod will be a thorny stick. The Druid's Staff will be a nature themed pole. The Faerie Wand will be a small magical stick. The Root Staff will be made of tree roots. Nature's Call will be an earth-themed staff. The Sandstone Rod will be a desert-forged staff. The Mirage Staff will be an illusion-themed rod. The Cobra Head Staff will be shaped like a snake. The Sun Rod will be a light-themed staff. The Sphinx Cane will be an ancient desert cane. The Icicle Rod will be made of ice. The Snowflake Staff will be a frost-themed pole. The Hailstorm Wand will be a winter-themed wand. The Permafrost Cane will be an enduring cold cane. The Frozen Core Staff will be a deeply chilled staff. The Ember Rod will be a smoldering stick. The Ash Staff will be made from burnt wood. The Dragon Breath Wand will be a dragon-themed wand. The Core Magma Staff will be a molten pole. The Hellfire Rod will be a demonic fiery staff.

**D.4.2.2 Skills**

For the Sorcerer, Fire, Fire II, and Fire III will deal varying levels of fire magic damage to one enemy. Ice, Ice II, and Ice III will deal varying levels of ice magic damage. Thunder, Thunder II, and Thunder III will deal varying levels of lightning magic damage. Flare will deal massive non elemental magic damage. Freeze will deal ice damage with a high chance to stun. Shock will deal lightning damage with a chance to paralyze. Magic Drain will absorb mana from the target. Concentrate will drastically multiply magic attack for the next spell. Meteor Swarm will deal massive fire and earth damage to all enemies.

**D.4.3 Priest**

The Priest class will act as the main support role for the group. Players will use maces and canes to defend themselves during battle. This role will have access to various skills, for example, restoring the health of the party or removing negative status effects.

**D.4.3.1 Weapons**

The Priest class will wield maces and canes. The Wooden Mace will be a simple blunt weapon. The Oak Club will be a sturdy wooden stick. The Spirit Mace will be a spiritually aligned blunt weapon. The Blessed Branch will be a holy wooden stick. The Mossy Hammer will be an overgrown blunt weapon. The Guardian's Cudgel will be a protective club. The Golden Scepter will be an ornate rod. The Sandstone Hammer will be a desert crafted mallet. The Sun Disc Mace will be a light-themed weapon. The Tomb Guardian Club will be an ancient blunt weapon. The Sacred Ankh will be a cross shaped holy relic. The Crystal Mace will be a crystalline blunt weapon. The Hailstone Hammer will be a frozen mallet. The Frozen Scepter will be an icy rod. The Polar Club will be a cold weather club. The Divine Ice Mace will be a holy frozen weapon. The Obsidian Mace will be a dark volcanic weapon. The Lava Rock Hammer will be a molten mallet. The Cleansing Fire Club will be a fiery blunt weapon. The Forge Master's Hammer will be a heavy smithing tool. The Phoenix Down Mace will be a legendary healing blunt weapon.

**D.4.3.2 Skills**

For the Priest, Heal, Heal II, and Heal III will restore varying amounts of health to an ally. Party Heal will restore health to the entire party. Cure Poison, Cure Blind, and Cure Silence will remove specific status ailments. Panacea will remove all negative status effects from one ally. Raise will revive a knocked-out ally. Holy Light will deal light magic damage to undead enemies. Protect will increase an ally's physical defense. Shell will increase an ally's magic defense. Regenerate will grant continuous health regeneration. Purify will damage an enemy and remove their buffs. Divine Intervention will fully heal the party and revive all dead allies.

**D.4.4 Knight**

The Knight class will provide heavy defense to protect the rest of the team. Players will equip spears and lances to fight on the front lines. This role will have access to various skills, for example, forcing enemies to target them instead of weaker allies or completely blocking incoming damage.

**D.4.4.1 Weapons**

The Knight class will wield spears and lances. The Short Spear will be a basic reach weapon. The Hunter's Spear will be a basic hunting tool. The Boar Tusk Lance will be an animal-themed spear. The Forest Guard Pike will be a woodland spear. The Wooden Pike will be a lightweight reach weapon. The Leaf-Blade Spear will be a nature themed polearm. The Scorpion Stinger will be a desert themed spear. The Desert Pike will be a sandy polearm. The Bronze Lance will be a metallic reach weapon. The Sand Piercer will be a desert lance. The Pharaoh's Guard will be an ancient royal spear. The Ice Shard Lance will be a frozen reach weapon. The Glacier Pike will be a heavy cold polearm. The Tundra Harpoon will be a hunting spear for the cold. The Frost Wyrm Spear will be a dragon themed ice lance. The Frozen Needle will be a sharp icy spear. The Magma Pike will be a molten polearm. The Dragon Scale Lance will be a heavy reptilian spear. The Red Steel Spear will be a crimson metallic lance. The Obsidian Lance will be a dark volcanic spear. The Hellfire Harpoon will be a demonic fiery spear.

**D.4.4.2 Skills**

For the Knight, Provoke will force enemies to target the player. Shield Bash will deal physical damage with a chance to stun. Cover will allow the knight to take damage in place of a low-health ally. Iron Defense will greatly increase defense. Guard Ally will protect a selected ally from all physical attacks. Shield Wall will increase the entire party's defense. Fortify will reduce damage taken by the user while skipping their turn. Sentinel will counter attack whenever hit physically. Justice Strike will deal damage based on the user's current defense. Heavy Charge will deliver a high damage but low-precision strike. Taunt will lower enemy attack but direct them to target the user. Unbreakable Will will grant immunity to status ailments. Phalanx will increase physical and magic defense for the user. Retribution will reflect a portion of physical damage back to the attacker. Castle of Stone will make the party immune to all damage for a turn.

**D.4.5 Martial Artist**

The Martial Artist class will fight using fast blunt damage. Players will equip claws and knuckles to strike their targets. This role will have access to various skills, for example, hitting a target multiple times or spending their own health to deliver massive damage.

**D.4.5.1 Weapons**

The Martial Artist class will wield claws and knuckles. The Leather Gloves will be basic hand protection. The Bear Claws will be animal-themed fist weapons. The Wolf Paws will be lupine hand gear. The Sharp Thorns will be spiky hand wraps. The Tree Bark Knuckles will be wooden fist weapons. The Wild Beast Fists will be feral gloves. The Scorpion Pincers will be desert-themed claws. The Sandstone Gauntlets will be heavy rocky gloves. The Cactus Spines will be prickly hand weapons. The Mummy Wraps will be ancient cloth bindings. The Golden Knuckles will be ornate metallic fist weapons. The Ice Picks will be sharp frozen claws. The Yeti Fists will be heavy snowy gloves. The Frostbite Gloves will be chilling hand gear. The Crystal Talons will be magical glass claws. The Polar Paws will be cold-weather animal gloves. The Salamander Claws will be fiery hand weapons. The Dragon Fangs will be reptilian fist weapons. The Magma Fists will be molten hand gear. The Burning Knuckles will be flaming fist weapons. The Demon Hands will be dark supernatural claws.

**D.4.3.2 Skills**

For the Martial Artist, Punch and Kick will deal basic blunt damage. Triple Kick will hit a target multiple times. Roundhouse will hit all enemies with physical damage. Chakra will restore the user's health and cure basic ailments. Meditate will restore the user's tactical points. Pressure Point will ignore enemy defense. Earth Splitter will perform an earth elemental physical attack. Gale Palm will perform a wind elemental strike that pushes the turn order back. Spirit Wave will deal ranged non-elemental damage. Counter will provide a high chance to counter-attack physical hits. Leg Sweep will carry a chance to lower enemy agility. Fists of Fury will deliver rapid punches to one target. Chi Blast will use the player's health to deal massive damage. Seven Star Strike will deliver heavy hits with guaranteed criticals.

**D.4.6 Magic Swordsman**

The Magic Swordsman class will combine physical sword strikes with elemental power. Players will use rapiers and enchanted blades to deal damage. This role will have access to various skills, for example, adding ice to their physical attacks or bouncing magic spells back at the enemy.

**D.4.6.1 Weapons**

The Magic Swordsman class will wield enchanted blades and rapiers. The Rapier will be a thrusting sword. The Wind Blade will be a gust-themed sword. The Leaf Cutter will be a nature-themed rapier. The Elven Rapier will be a mystical thrusting sword. The Swift Blade will be a lightweight sword. The Whisper Edge will be a silent blade. The Mirage Rapier will be an illusionary sword. The Heatwave Saber will be a desert-themed blade. The Dust Devil Blade will be a sandy thrusting sword. The Golden Epee will be an ornate rapier. The Sun-Strike Sword will be a bright blade. The Chill Spike will be a cold-themed thrusting sword. The Frozen Needle will be an icy rapier. The Aurora Blade will be a light-themed cold sword. The Ice Queen's Rapier will be a royal frozen blade. Zero Kelvin will be an ultimate freezing sword. The Searing Saber will be a hot blade. The Molten Rapier will be a liquid fire sword. The Blaze Edge will be a flaming blade. The Phoenix Tail will be a fiery magical sword. The Volcanic Spike will be a molten thrusting sword.

**D.4.6.2 Skills**

For the Magic Swordsman, Fire Blade, Ice Blade, Thunder Blade, and Wind Blade will add specific elements to physical attacks. Drain Blade will damage an enemy and restore the user's health. Aspir Blade will damage enemy mana to restore the user's mana. Magic Barrier will grant magic reflection to the user. Enchant Weapon will buff an ally's weapon with fire. Dispel Strike will remove enemy buffs on hit. Elemental Burst will consume all mana to deal damage. Arcane Slash will deal magic damage capable of critical hits. Spell Shield will grant immunity to the next magic spell received. Mystic Thrust will pierce magical defenses. Teleport Strike will execute a high evasion attack. Rune Breaker will deal massive non-elemental magic slash damage to foes.

**D.4.7 Hunter**

The Hunter class will specialize in long range attacks. Players will shoot bows to damage targets safely. This role will have access to various skills, for example, shooting multiple arrows at once or putting targets to sleep.

**D.4.7.1 Weapons**

The Hunter class will wield bows. The Short Bow will be a basic ranged weapon. The Oak Bow will be a standard wooden bow. The Hunter's Bow will be a tool for tracking. The Ranger's Crossbow will be a mechanical ranged weapon. The Vine Bow will be a nature themed weapon. The Elven Bow will be a mystical archery tool. The Bone Bow will be made from skeletal remains. The Sandstone Crossbow will be a desert-themed mechanical bow. The Scorpion Recurve will be an animal-themed desert bow. The Desert Wind Bow will be a sandy ranged weapon. The Golden Arrow will be an ornate projectile weapon. The Ice Crystal Bow will be a frozen ranged weapon. The Frostbite Crossbow will be a chilling mechanical bow. The Mammoth Ivory Bow will be a heavy prehistoric weapon. The Blizzard String will be a winter themed bow. The Glacial Shot will be a heavy frozen weapon. The Ash Wood Bow will be a burnt wooden bow. The Flame String will be a fiery ranged weapon. The Magma Rock Crossbow will be a molten mechanical bow. The Dragon Bone Bow will be a reptilian ranged weapon. The Phoenix Fire Bow will be a legendary flaming bow.

**D.4.7.2 Skills**

For the Hunter, Aim will guarantee the next attack will hit and critically strike. Power Shot will deal high damage after a charge turn. Rapid Fire will shoot multiple arrows at random targets. Poison Arrow, Sleep Arrow, Blind Arrow, and Silence Arrow will inflict specific status ailments on hit. Arrow Rain will deal physical damage to all enemies. Eagle Eye will increase precision and critical rate. Beast Slayer will deal massive damage against animals. Piercing Shot will ignore enemy defense. Camouflage will lower the user's aggro. Trap Set will damage enemies who physically attack the user. Snipe will deal high damage to low-health enemies. Hail of Arrows will deal heavy damage to all enemies and lower their agility.

**D.4.8 Bandit**

The Bandit class will rely on high speed and evasion to win fights. Players will use short daggers and knives to quickly strike targets. This role will have access to various skills, for example, draining the core statistics of the enemy.

**D.4.8.1 Weapons**

The Bandit class will wield daggers and knives. The Knife will be a simple utility blade. The Rusty Shiv will be an old, degraded dagger. The Hunter's Knife will be an animal-skinning tool. The Poison Tip will be a toxic dagger. The Thief's Shank will be a rogue's blade. The Forest Tooth will be a woodland dagger. The Curved Dagger will be a swept blade. The Sand Shiv will be a desert-themed knife. The Scorpion Barb will be an animal-themed desert dagger. The Tomb Blade will be an ancient knife. The Golden Dagger will be an ornate short blade. The Icicle Shiv will be a frozen knife. The Frozen Dagger will be a cold short blade. The Shard of Glass will be an improvised sharp tool. The Cold Steel Knife will be a pristine metallic dagger. The Frostbite Dirk will be a chilling short blade. The Obsidian Knife will be a dark volcanic dagger. The Heated Dagger will be a hot short blade. The Ember Shiv will be a smoldering knife. The Dragon Claw will be a reptilian short blade. The Hell's Tooth will be a demonic dagger.

**D.4.8.2 Skills**

For the Bandit, Steal will temporarily reduce an enemy's core statistics while granting those same stat boosts to the user. Mug will deal physical damage while simultaneously draining the enemy's statistics. Sneak Attack will deal high damage if used at the start of battle. Poison Edge will add a toxic effect to the dagger. Sand Throw will inflict blindness on one enemy. Smoke Bomb will provide a high chance to flee battle or blind all enemies. Backstab will provide a high critical chance. Sprint will greatly increase agility. Gold Snatch will steal coins from the enemy. Venom Strike will deal heavy damage to poisoned targets. Shadow Step will drastically increase evasion. Dirty Trick will carry a chance to stun the enemy. Twin Daggers will hit twice. Lucky Strike will scale damage based on the luck stat. Assassinate will carry a chance to instantly kill non-boss enemies.

**D.5 Buffs and Debuffs**

Combat will also be affected by various positive and negative status effects.

**D.5.1 Debuffs**

The negative states will act as debuffs. Knockout will prevent characters from acting until revived. Poison will cause continuous damage at the end of every turn. Blind will greatly reduce physical attack precision. Silence will prevent the usage of all magic skills. Confusion will force characters to attack random targets. Sleep will prevent characters from acting until they take damage. Paralysis will force the character to skip their turn entirely. Stun will make characters flinch and lose their current turn. Bleed will deal physical damage over time and reduce healing received. Burn will deal fire damage over time and lower attack power. Freeze will prevent action until physical damage shatters the ice. Slow will reduce agility, filling the action gauge much slower. Curse will double mana costs and prevent health regeneration. Weakness will lower all elemental resistances. Fear will prevent the use of special tactical skills.

**D.5.2 Buffs**

The positive states will act as buffs. Regenerate will restore a portion of health at the end of every turn. Haste will double agility to fill the action gauge faster. Protect will reduce physical damage taken. Shell will reduce magic damage taken. Focus will increase the critical hit rate. Magic Barrier will nullify the next magical attack received. Attack Up, Defense Up, Magic Up, and Agility Up will increase physical attack, physical defense, magic attack, and speed respectively. Evasion Up will add a chance to dodge physical attacks. Immortal will prevent health from dropping below one. Auto-Life will give a Hp boost, healing effectiveness and physical damage reduction. Reflect will bounce magic spells back at the caster. Counter Stance will guarantee a counter-attack against physical hits.

**D.6** **Equipment and Accessories**

Equipment options will further customize gameplay by providing stat boosts and elemental resistances.

**D.6.1 Shields**

Shields will provide various defensive benefits. Small Shields and Round Shields will provide basic protection. Bucklers will be lightweight shields. Kite Shields, Iron Shields, and Steel Shields will provide larger coverage and metal protection. Mythril Shields will be made of lightweight magical metal. Gold Shields will be highly decorative. Wooden Lids will be improvised village shields. Hunter's Bucklers will not hinder movement. Bronze Shields will be durable desert alloys. Scale Guards will resist fire. Shell Bucklers will resist water. Ice Shields will reduce ice damage. Crystal Guards will reflect minor spells. Frost Shields will chill physical attackers. Dragon Shields and Flame Guards will reduce fire damage. Obsidian Shields will be unbreakable dark shields. The Aegis will be the ultimate shield preventing instant death.

**D.6.2 Headgear**

Headgear will provide additional defense and stat bonuses when equipped. Leather Caps, Leather Helms, Iron Helmets, and Steel Helmets will provide varying degrees of physical protection. Mythril Helms will offer high defense with low weight. Full Helms will cover the entire head. Viking Helms will have horns. Dragon Helms will resist fire. Genji Helms will be legendary armor. Feathered Hats will be stylish. Magician's Hats will be pointy magic gear. Circlets will be simple metal bands. Ribbons will prevent status ailments. Bandanas will be worn by thieves. Turbans will protect against desert heat. Silk Hoods and Fur Hoods will provide climate and magic resistance. Ice Crowns and Salamander Coifs will provide elemental resistance. Royal Crowns will offer high overall stats.

**D.6.3** Body Armor

Body armor will serve as the character's main defensive equipment to reduce overall incoming damage. Cloth Tunics and Traveler's Tunics will be basic clothing. Leather Armor and Hard Leather will be light protection. Iron Armor, Steel Armor, Plate Mail, and Heavy Mail will be heavy metal plating. Mythril Armor will be made of magical metal. Scale Mail will use flexible overlapping scales. Glacial Mail and Flame Mail will resist extreme temperatures. Dragon Armor will be the ultimate elemental resistance gear. Hunter's Vests and Ninja Suits will provide camouflage and agility. Cotton Robes, Silk Robes, Sorcerer's Robes, and Sage's Robes will provide magical protection for spellcasters. Winter Robes and Lava Robes will provide elemental resistance for casters.

**D.6.4** Accessories

Accessories will provide specific utility benefits. Rings of Protection, Power, Magic, Speed, and Life will increase their respective core statistics. Poison Charms, Silence Amulets, Blindness Glasses, Paralysis Talismans, and Sleep Earrings will prevent specific status ailments. Fire, Ice, Thunder, and Earth Rings will reduce elemental damage taken. Gold Rings and Lucky Coins will increase post-battle rewards. Warrior's Badges will offer counter-attacks. Scholar's Specs will reveal enemy stats. Knight's Crests will start battles with defensive buffs. Sniper's Eyes will greatly increase precision.

![](data:image/png;base64...)