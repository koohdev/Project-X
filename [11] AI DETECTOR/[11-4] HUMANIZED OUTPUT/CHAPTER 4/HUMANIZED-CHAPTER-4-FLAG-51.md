### 4.1.1 Requirements Gathering

The proponents started by reviewing the DepEd Grade 4 to 6 mathematics curriculum to identify which arithmetic operations the game should cover, and this ranged from basic addition and subtraction up to multi-step PEMDAS equations. The proponents also consulted the Capstone Adviser, Mr. Jan Nichole B. Apostol, and researched related materials to educational games like Prodigy Math to determine what the Math Engine should handle and what falls outside the scope of the project. The result was a working list of game requirements and the specific math topics each enemy tier should test.

### 4.1.2 Quick Design

Flowcharts, wireframes, and storyboards were the main outputs of this stage. The proponents drew flowcharts that show how a student moves through the game from the main menu into the battle screen, and wireframes for the key interfaces like the math input prompt and the Virtual Numeric Keypad overlay. The proponents also drafted storyboards for the four biomes (Forest, Desert, Tundra, and Volcanic) to plan where each enemy type appears and how the maps connect to each other.

### 4.1.3 Building Prototype

RPG Maker MZ was the primary tool for building the initial prototype because it already has a built-in map editor, event system, and a database for managing enemies and character stats. The proponents wrote the Math Battle System plugin in JavaScript to generate arithmetic equations and check player answers through the Virtual Numeric Keypad, and the Active Time Battle (ATB) timer was connected to the battle loop so that each combat turn runs on a countdown. PeerJS was also added for peer-to-peer (P2P) multiplayer so that two players can connect using room codes, and the proponents built the first versions of the Plains of Origin and Forest biome maps too.

### 4.1.4 Customer Evaluation of Prototype

Ten (10) Grade 4 to 6 students and the Capstone Adviser, Mr. Jan Nichole B. Apostol, are the two groups that will evaluate the prototype. The Capstone Adviser reviews the core mechanics first to check whether the Math Engine generates the correct equations for each difficulty tier, whether the scaling adjusts properly across enemy levels, and whether the P2P connection holds during two-player sessions. After the internal review, the proponents will run a small usability test with the student participants to see if the gameplay is clear, if the math problems are readable on screen, and if the students stay interested enough to continue playing. What both groups provide determines what the proponents change before the next prototype cycle.

### 4.1.5 Refining Prototype

Based on what the Capstone Adviser and the student testers report, the proponents adjust the prototype in this stage. If the difficulty scaling is too simple or too difficult for certain enemy tiers (Slimes at Level 1 compared to the Numeromancer at Level 100, for example), the algorithm is rebalanced so the math problems match the player's progress more accurately. The battle menu and the Virtual Numeric Keypad layouts are also revised based on how the students actually used them during testing, since what looks clear on a wireframe does not always work the same way on screen. P2P timing issues, assuming any arise during the multiplayer tests, are fixed in this stage too.

### 4.1.6 Engineer Product

The goal of this final stage is a stable build of Chronicles of Arithmos that runs both as a desktop application and as a web application. The proponents will run final system tests to confirm that all four biomes, the Math Engine, the adaptive difficulty algorithm, and the multiplayer module work correctly on both platforms. Once testing is done, the proponents package the desktop version as a standalone .exe file using NW.js and host the web version on Hostinger so that students can access the game through a browser without requiring a separate installation.
