# 4.0 Methodology

## 4.1 Prototyping Model

According to Geeks for Geeks, the Prototyping Model is a branch of the SDLC. It is basically making a bare bones version before the final game. This helps when the proponents do not have a super detailed plan at the start. Proponents can just build a simple version to get feedback and fix the code logic before wasting time on the final product [11].

![Figure No. 7: Prototyping Model]()

The proponents went with the Prototyping Model because the math inside Chronicles of Arithmos is just too messy to figure out on paper. Specific numbers like how fast a timer runs or how hard a monster hits have to be tested to make sure they are not too tough for players playing Chronicles of Arithmos. If the proponents used a stiff plan like the Waterfall Model, they could not change those values easily later. Instead, this model lets the proponents fix the balance based on what the students or young learners say while they are actually playing the game.

The following are the phases of the Prototyping Model:

### 4.1.1 Requirements Gathering

In this phase, the proponents looked at the DepEd math lessons for young learners in Grade 4 to 6 to see what math to put in. They looked at basic plus and minus plus the harder PEMDAS too. The proponents also played Prodigy Math to see what their own game should do. By the end they had a list of what the game needs and what math to put in Chronicles of Arithmos.

### 4.1.2 Quick Design

In the next phase, the proponents made flowcharts and drawings to show how the game and buttons would look. These drawings show how a player goes from the menu to a fight. They also made storyboards for the Forest and Desert and other areas to plan where the monsters live and how the maps connect to each other.

### 4.1.3 Building Prototype

The proponents used RPG Maker MZ to make the first or initial version. RPG Maker MZ allows the team to make maps and monster stats. The proponents wrote a custom plugin script in JavaScript so the game can give math problems and check if the player is right. They also added a timer for the fights and used PeerJS so players can invite friends to play together. They finished the first few maps like the Forest to start with.

### 4.1.4 Customer Evaluation of Prototype

The proponents will find 10 students or young learners aged 9 to 12 typically from Grade 4 to 6 to play the game. The proponents will watch them to see if the game is easy or if the math is too hard to read. What the young learners or children say will help the proponents decide what to fix before they make the next version.

### 4.1.5 Refining Prototype

After the young learners play it, the proponents will fix the game and do the whole design and build part all over again. This happens two times. The proponents will change how hard the monsters are if they are too easy or too tough. They will also fix the buttons if they are too small for a phone screen and fix the multiplayer part.

### 4.1.6 Engineer Product

In the last phase, the proponents will make a final version that works on computers assuming the computers have the specific requirements needed, and on modern browsers. The proponents will check one last time to make sure the math and the multiplayer part works. Then they will put the game online and make a file or the .exe file so it can be downloaded and be played.

## 4.2 Requirements Specification

### 4.2.1 Operational Feasibility

#### A. Fishbone Diagram



![Figure No. 8: Fishbone Diagram]()

#### B. Functional Decomposition Diagram

![Figure No. 9: Functional Decomposition Diagram]()

### 4.2.2 Technical Feasibility

#### 4.2.2.1 Compatibility Checking

##### A. Hardware Compatibility

The proponents made the game with RPG Maker MZ. It runs on computers with 8 GB of RAM and an Intel Core i3 processor. Since there is a web version too, it works on tablets or any computer with a modern browser. This lets players jump into math battles without downloading executable files.

##### B. Software Compatibility

Since RPG Maker MZ runs on JavaScript, the math engine was built using that same language. This lets the math logic and combat mechanics work together without needing extra fixes or conversion of code to another programming language. For the multiplayer part, the proponents used PeerJS so players can use room codes to connect directly without needing a central server.

#### 4.2.2.2 Relevance of the Technology

Prodigy and Math Blaster are turn-based RPGs where math is the button the player presses to attack. Players get the answer right, the animation plays, and that is it. Chronicles of Arithmos ties calculation speed directly to combat execution. Instead of just "Right = Hit," it uses a Performance-Based Reward system. If a player is accurate and fast, they execute a 2.0x Critical Hit. If the player is slow or incorrect, the attack loses effectiveness or misses completely.

JavaScript (ES6) was chosen because it is the native scripting language of RPG Maker MZ, allowing the proponents to implement the Math Battle Engine and Content-Aware Timer without external dependencies. PeerJS, a WebRTC library, was selected for the multiplayer module as it enables direct Peer-to-Peer connections through room codes without requiring a dedicated server.

The proposed title deploys as a Windows desktop application via NW.js (Node Webkit) and as a web application hosted on Hostinger using HTML5 and WebGL. Desktop is the primary platform because the Math Battle System requires timed numerical input through a physical keyboard, which touchscreens cannot replicate due to the absence of physical tactile feedback. The desktop executable operates offline. Web deployment serves as a secondary access point, supported by the Virtual Numeric Keypad module for touch-enabled devices.

### 4.2.3 Schedule Feasibility

#### A. Gantt Chart

##### Table #1 November 2025 Gantt Chart

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|
| 1. Capstone Orientation | | | | |
| 2. Grouping of Capstone Members | | | | |
| 3. Planning and Brainstorming | | | | |
| 4. Capstone Adviser Selection | | | | |

##### Table #2 December 2025 Gantt Chart

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|
| 1. Requirements Gathering | | | | |
| 2. Quick Design | | | | |

##### Table #3 January 2026 Gantt Chart

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|
| 1. Building Initial Prototype | | | | |
| 2. Preparation for Title Defense | | | | |
| 3. Title Defense | | | | |
| 4. Capstone Adviser Consultation | | | | |
| 5. Dean Consultation | | | | |
| 6. Documentation (Chapter 1) | | | | |

##### Table #4 February 2026 Gantt Chart

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|
| 1. Documentation (Chapter 2) | | | | |
| 2. Documentation (Chapter 3) | | | | |
| 3. Capstone Adviser Consultations | | | | |
| 4. Documentation (Chapter 4) | | | | |

##### Table #5 March 2026 Gantt Chart

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|
| 1. Building Initial Prototype (Continued) | | | | |
| 2. AI & Plagiarism Checking | | | | |
| 3. AI & Plagiarism Checking | | | | |
| 4. Preparation for Oral Defense | | | | |
| 5. Oral Defense | | | | |

##### Table #6 April 2026 Gantt Chart

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|
| 1. Customer Evaluation of Prototype | | | | |
| 2. Refining Prototype | | | | |
| 3. Quick Design | | | | |

##### Table #7 May 2026 Gantt Chart

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|
| 1. Building Prototype | | | | |
| 2. Customer Evaluation of Prototype | | | | |
| 3. Capstone Adviser Consultation | | | | |

##### Table #8 June 2026 Gantt Chart

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|
| 1. Refining Prototype | | | | |
| 2. Capstone Adviser Consultation | | | | |

##### Table #9 July 2026 Gantt Chart

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|
| 1. Unit Testing | | | | |
| 2. Integration Testing | | | | |
| 3. Capstone Adviser Consultation | | | | |

##### Table #10 August 2026 Gantt Chart

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|
| 1. System Testing | | | | |
| 2. Acceptance Testing | | | | |
| 3. Engineer Product | | | | |
| 4. Implementation Plan | | | | |
| 5. Capstone Adviser Consultation | | | | |

##### Table #11 September 2026 Gantt Chart

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|
| 1. Engineer Product (Continued) | | | | |
| 2. Final Documentation (Chapter 5) | | | | |
| 3. Capstone Adviser Consultation | | | | |
| 4. Updating, Reviewing, and Revision of the whole document | | | | |

##### Table #12 October 2026 Gantt Chart

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|
| 1. Capstone 2 Defense | | | | |

### 4.2.4 Economic Feasibility

#### 4.2.4.1 Cost and Benefit Analysis

The cost and benefit analysis provides a breakdown of the materials required for development and the specific value each item brings to the study. The proponents have categorized these costs into software and hosting expenses.

##### Table #13 Cost and Benefits Table

| Category | Item | Cost | Benefits |
|---|---|---|---|
| Software | RPG Maker MZ (2 Licenses) | ₱4,600.00 | Allows the proponents to develop and test the game concurrently, and provides a built-in event system and map editor that can reduce the time needed to build the Active Time Battle (ATB) interface and Math Engine from scratch. |
| Hosting | Hostinger Domain & Web Hosting (5 years) | ₱12,108.00 | Allows students to either download the Windows executable or play via a web browser from home without requiring any software installation. |
| Temporary Hosting | Vercel | ₱0.00 | Provides a cost-free staging environment with automated preview deployments for testing the web-based game build before launching it to the primary hosting. |
| **TOTAL** | **Estimated Development Cost** | **₱16,708.00** | |

#### 4.2.4.2 Cost Recovery Scheme

The proponents will distribute Chronicles of Arithmos for both web browsers and Windows desktops free to the public, allowing users, especially students, to practice arithmetic skills without paying for access. To cover the development, hosting, and domain cost, the proponents will explore optional monetization and community channels.

These channels include voluntary community donations, optional rewarded advertisements that grant cosmetic character skins and custom virtual numeric keypad themes after opening loot chests, and downloadable content (DLC) packages. The DLC includes optional story expansions, new playable character classes, and cosmetic theme packs. All arithmetic lessons and core gameplay will remain free.

##### Table #14 Cost Recovery and Break-Even Projection Table

| Revenue Stream | Unit Price / Rate | Target Volume | Projected Gross Revenue | Target Recovery Phase |
|---|---|---|---|---|
| Optional Rewarded Ads (Keypads & Skins) | ₱115.00 / 1,000 Views | 35,000 Views | ₱4,025.00 | Months 1 to 24 |
| Story Expansion & Class DLC Bundles | ₱99.00 / ₱79.00 | 60 / 40 Units | ₱9,100.00 | Months 6 to 36 |
| Optional Cosmetic Packs & Keypad Skins | ₱49.00 | 50 Units | ₱2,450.00 | Months 3 to 24 |
| Voluntary Community Donations | ₱100.00 (Avg.) | 20 Contributors | ₱2,000.00 | Months 1 to 36 |
| **TOTAL** | | | **₱17,575.00** | **Break-Even Achieved at ₱16,708.00** |

Meeting these targets generates ₱17,575.00 over 24 to 36 months, fully recovering the estimated development cost of ₱16,708.00 while providing a ₱867.00 reserve for future hosting renewals. If external revenue progresses slowly, the project carries zero debt because the five-year hosting plan is fully prepaid through 2031, and the Windows desktop build runs completely offline without ongoing server expenses.

### 4.2.5 Requirements Modeling

#### 4.2.5.1 Object Modelling

##### A. Use Case Diagrams

![Figure No. 10: Young Learner Use Case Diagrams]()

##### B. Sequence Diagrams

![Figure No. 9: Auto Quest Sequence Diagram]()
![Figure No. 10: Enemy Auto-Scaling Sequence Diagram]()
![Figure No. 11: Level-Based Progression Sequence Diagram]()
![Figure No. 12: Math Battle System Sequence Diagram]()
![Figure No. 13: P2P Multiplayer Sequence Diagram]()
![Figure No. 14: Save Sequence Diagram]()

##### C. Activity Diagrams

![Figure No. 15: Game Loop Chronicles of Arithmos Activity Diagram]()

### 4.2.6 Risk Assessment/Analysis

Developing Chronicles of Arithmos comes with risks that the proponents have identified and prepared for. The proponents have limited experience with JavaScript and PeerJS, which may cause technical delays in building the Math Battle System and multiplayer features. Differences between desktop, web, and mobile versions may cause inconsistencies. The large project scope may lead to schedule delays, while young learners may lose interest if math overshadows gameplay.

External dependencies such as PeerJS and NW.js may receive breaking updates, and students' computers may lack adequate hardware or internet access. To reduce these risks, the proponents will study online resources and consult Capstone Adviser Mr. Jan Nicole B. Apostol, lock software versions during development, prioritize core features first with remaining items as stretch goals, review early prototypes for gameplay balance, and offer an offline single-player desktop executable fallback for students unable to play via the web application.

## 4.3 Design

### 4.3.1 Output and User-interface Design

The proponents designed the interface for Chronicles of Arithmos using a 2D pixel art style for all game assets and entities. The color scheme uses deep blue (`#005385`) for menu outlines and active pressed buttons. Black (`#000000`) serves as the background color for buttons and menu windows. White (`#FFFFFF`) is used for all text, mathematical equations, and numerical values.

![Figure No. 16: Dark Blue, Black and White]()

The proponents chose the M+ 1m regular font for clean readability across computer screens and mobile displays.

![Figure No. 17: M+ 1m regular Font]()

## REFERENCES

[1] Department of Education, "MATATAG Curriculum Overview and Guide," 2024. [Online]. Available: <https://matatagcurriculum.ph/>

[2] National Council for Children's Television, "Study: Personal screens becoming the new classroom," Philippine Information Agency, 2025. [Online]. Available: <https://pia.gov.ph/news/luzon/study-personal-screens-becoming-the-new-classroom/>

[3] M. Engelhardt, "Feedback in Digital Game Based Learning: Influencing Student Self Efficacy and Motivation," VTechWorks, 2023. [Online]. Available: <https://vtechworks.lib.vt.edu/>

[4] P. Mozelius and L. M. Eberhardt, "The Chocolate Covered Broccoli Syndrome in Educational Games," Academic Conferences International, 2023. [Online]. Available: <https://doi.org/10.34190/ecgbl.17.1.1344>

[5] Y. F. Chen et al., "Assessing the Effects of Flow, Social Interaction, and Engagement on Students Gamified Learning," MDPI, 2023. [Online]. Available: <https://www.mdpi.com/2071-1050/15/2/983>

[6] K. Skagerlund et al., "Mathematics anxiety and emotion regulation," Taylor and Francis, 2024. [Online]. Available: <https://www.tandfonline.com/doi/pdf/10.1080/00313831.2025.2559280>

[7] A. Gokce and N. Guner, "Innovative Approaches to Mitigate Math Anxiety," MDPI, 2024. [Online]. Available: <https://www.mdpi.com/2813-9844/7/2/46>

[8] A. S. Maryana et al., "Using Gamified Learning Strategies to Enhance Problem Solving Performance in Mathematics," International Journal of Research and Innovation in Social Science, 2024. [Online]. Available: <https://rsisinternational.org/journals/ijriss/uploads/vol9-iss11-pg3461-3480-202512_pdf.pdf>

[9] NW.js Community, "NW.js Downloads and Architecture Support," NW.js Official Homepage, 2024. [Online]. Available: <https://nwjs.io/>

[10] Mozilla Developer Network, "WebGL2RenderingContext Browser Compatibility," MDN Web Docs, 2024. [Online]. Available: <https://developer.mozilla.org/en-US/docs/Web/API/WebGL2RenderingContext#browser_compatibility>

[11] "Prototyping Model - Software Engineering," GeeksforGeeks, Jul. 11, 2025. [Online]. Available: <https://www.geeksforgeeks.org/software-engineering/software-engineering-prototyping-model/>
