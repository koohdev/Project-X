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

4.5.2.2 Performance Testing

The proponents tested system performance across the Windows desktop application, desktop web browsers, and mobile web browsers. The evaluation measured pacing time and response time across all eleven functional modules. Pacing time recorded user interaction intervals between inputs, while response time measured the duration required to execute actions and display outputs. All eleven modules completed their test cases and operated within their designated time limits.

4.5.2.2.1 Performance Testing (Windows Desktop)

In the Windows desktop environment, application launch recorded a pacing time of 5 seconds and a response time of 5 seconds. The title screen displayed in 7 seconds. Accessing the options menu and loading local save files each recorded a response time of 1 second under 3 to 5 seconds of pacing time. During combat, math equation prompts and player attack executions each registered a response time of 1 second. The Content-Aware Timer recorded a response time of 5 seconds after 10 seconds of pacing time to mark late submissions, while the 20 manual save slots and victory rewards processed in 1 second.

4.5.2.2.2 Performance Testing (Web Desktop)

In the desktop web environment across Chrome, Edge, Firefox, Opera GX, and Brave, the application launched in 3 seconds of response time under 5 seconds of pacing time. Retrieving save files from browser local storage recorded a response time of 1 second under 5 seconds of pacing time. Combat equation generation, player attacks, and reward allocations resolved with sub-second execution speeds. The Content-Aware Timer marked slow submissions in 5 seconds under 10 seconds of pacing time. Two-player peer-to-peer multiplayer interactions synchronized quest actions within 3 to 10 seconds of pacing time.

4.5.2.2.3 Web Mobile Performance Evaluation

In the mobile web environment across smartphones and tablets, the application launched in 6 seconds of response time under 5 seconds of pacing time. The options menu opened in 1 second, and loading stored data from mobile storage took 3 seconds under 5 seconds of pacing time. In combat encounters, equation prompts generated in 1 second, and the Mobile Input System processed on-screen virtual keypad inputs within 1 second. Dynamic difficulty scaling, timer tracking, quest management, and two-player multiplayer sessions synchronized across mobile devices within 3 to 10 seconds of pacing time.

Performance Test Result (see Table 32, Table 33, and Table 34 on pages E-13 to E-20)

4.5.2.3 Stress Testing

The stress testing in Chronicles of Arithmos assessed the performance and stability of the system under high load conditions. This test evaluated the capacity of the web host when multiple users access the game at the same time. The proponents simulated 25 concurrent users requesting web assets over the internet. The test scenarios included the initial web page boot, the loading of battle graphics and enemy sprites during combat initialization, the fetching of background music during map transitions, and the continuous loading of user interface elements and the virtual numeric keypad. As a result, the web version of the application maintained consistent and reliable performance. All visual and audio assets loaded successfully without severe delays or crashes. The testing confirmed that the web host can handle heavy usage and continue to provide a stable educational platform for users.

Stress Testing Result (see Table 35 on page E-22)

4.5.2.4 Load Testing

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
