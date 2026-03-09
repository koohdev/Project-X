
*Figure No. 4 : Prototyping Model*

The proponents have selected the Prototyping Model for this study to support the development of the proposed project that requires input to balance instructional content and gameplay engagement for Grade 4 to 6 students. This approach allows the proponents to verify that the mathematical mechanics and educational goals of the game remained aligned through repeated rounds of evaluation and revision, rather than committing to a fixed code structure at the outset.

The Prototyping Model follows a cycle consisting of the following stages:

### 4.1.1 Requirements Gathering

In this phase, the proponents defined the project objectives, scope, and mathematical requirements. The proponents reviewed the Grade 4 to 6 mathematics curriculum to identify the necessary arithmetic operations for the Math Engine. The proponents also surveyed existing educational games and consulted the Capstone Adviser to establish the core functions, which resulted in a documented list of functional requirements and target learning outcomes.

### 4.1.2 Quick Design

The proponents created flowcharts to map the student navigation and battle mechanics. Wireframes were developed to design the main menu, battle interface, and Virtual Numeric Keypad layouts. Finally, the proponents drafted storyboards for the four game biomes (Forest, Desert, Tundra, and Volcanic) to outline the visual progression and enemy placements.

### 4.1.3 Building Prototype

 The proponents built the initial prototype using RPG Maker MZ and JavaScript. The Math Battle System plugin was coded to generate arithmetic equations and validate player input via the Virtual Numeric Keypad. The proponents also implemented PeerJS for peer-to-peer (P2P) multiplayer connectivity using room codes and constructed the initial game maps. The Active Time Battle (ATB) timer logic was then integrated into the battle system.

### 4.1.4 Customer Evaluation of Prototype

The proponents will conduct the customer evaluation in two stages. First, the prototype will be presented to the proponents Capstone Adviser Mr. Jan Nichole B. Apostol for an internal review of the core mechanics. This review will focus on identifying gaps in the Math Engine, difficulty scaling algorithm, and Peer-to-Peer (P2P) connection stability. Second, the proponents will conduct a small-scale usability test with ten (10) Grade 4 to 6 students to gather feedback on gameplay clarity, math problem readability, and overall engagement. The combined feedback from the Capstone Adviser and the student participants will determine if the design aligns with the project objectives or if adjustments are necessary before proceeding with further development.

### 4.1.5 Refining Prototype

 The proponents will adjust the system based on the feedback gathered from the Capstone Adviser review and the student usability test. Technical adjustments will be applied to the difficulty scaling algorithm to balance the progression of math problems across enemy tiers. The proponents will revise the battle menu and Virtual Numeric Keypad interface layouts based on observed student interaction patterns. Corrections will also be applied to the P2P synchronization logic to address timing inconsistencies in the peer-to-peer connection.

### 4.1.6 Engineer Product

In this phase, the proponents will perform final system testing to verify that all four biomes, the Math Engine, the adaptive difficulty algorithm, and the multiplayer module operate correctly. After verification, the proponents will package the application as a standalone desktop executable using NW.js and host the web-based version and domain via Hostinger for browser access.

## 4.2 Requirements Specification

### 4.2.1 Operational Feasibility

#### A. Fishbone Diagram

*Figure No. 5: Fishbone Diagram*

#### B. Functional Decomposition Diagram

*Figure No. 6: Functional Decomposition Diagram*

### 4.2.2 Technical Feasibility

This section evaluates the hardware and software tools selected for the proposed system to verify that the project is technically achievable. The proponents focus on confirming that all components work together without conflict and that each tool directly supports the goal of teaching arithmetic to students.

#### 4.2.2.1 Compatibility Checking

#### A. Hardware Compatibility

RPG Maker MZ is the core development engine, and it runs on standard personal computers with at least 8 GB of RAM, which the proponents confirmed through testing with an Intel Core i3 configuration. The web-deployed version also runs on any device with a modern HTML5 browser, so school tablets and computers can access the Math Battle System without needing to install anything.

#### B. Software Compatibility

The Math Battle Engine is built in JavaScript (ES6), which is RPG Maker MZ's native scripting language, so the math logic connects directly to the RPG combat system without any extra conversion layer. PeerJS handles the multiplayer side because it uses WebRTC, which lets students connect through Room Codes directly without needing a central server in between.

#### 4.2.2.2 Relevance of the Technology

Existing educational game platforms such as Prodigy Math and Math Blaster address arithmetic instruction through gamified exercises; however, a common limitation is that mathematical tasks function as a separate reward layer rather than directly determining gameplay outcomes. Combat sequences in these tools proceed regardless of input accuracy or response speed, which the proposed title is designed to address.

JavaScript (ES6) was chosen because it is the native scripting language of RPG Maker MZ, allowing the proponents to implement the Math Battle Engine and Content-Aware Timer without external dependencies. PeerJS, a WebRTC (Web Real-Time Communication) library, was selected for the multiplayer module as it enables direct Peer-to-Peer connections through room codes without requiring a dedicated server.

The proposed title deploys as a Windows desktop application via NW.js (Node Webkit) and as a web application hosted on Hostinger using HTML5 and Web Graphics Library (WebGL). Desktop is the primary platform because the Math Battle System requires timed numerical input through a physical keyboard, which touchscreens cannot replicate due to the absence of a physical key-press sensation (haptic feedback). The desktop executable can also operate offline using a computer. The web deployment serves as a secondary access point, supported by the Virtual Numeric Keypad module for touch-enabled devices.

### 4.2.3 Schedule Feasibility

#### A. Gantt Chart

**Table #3 November 2025 Gantt Chart**

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| :--- | :--- | :--- | :--- | :--- |
| 1.Capstone Orientation | | | | |
| 2.Grouping of Capstone Members | | | | |
| 3.Planning and Brainstorming | | | | |
| 4.Capstone Adviser Selection | | | | |

**Table #4 December 2025 Gantt Chart**

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| :--- | :--- | :--- | :--- | :--- |
| 1.Requirements Gathering | | | | |
| 2.Quick Design | | | | |

**Table #5 January 2026 Gantt Chart**

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| :--- | :--- | :--- | :--- | :--- |
| 1.Building Initial Prototype / Construction of core Modules | | | | |
| 2.Preparation for Title Defense | | | | |
| 3.Title Defense | | | | |
| 4.Capstone Adviser Consultation | | | | |
| 5.Dean Consultation | | | | |
| 6.Documentation (Chapter 1) | | | | |

**Table #6 February 2026 Gantt Chart**

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| :--- | :--- | :--- | :--- | :--- |
| 1.Documentation (Chapter 2) | | | | |
| 2.Documentation (Chapter 3) | | | | |
| 3.Capstone Adviser Consultations | | | | |
| 4.Documentation (Chapter 4) | | | | |

**Table #7 March 2026 Gantt Chart**

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| :--- | :--- | :--- | :--- | :--- |
| 1.Building Prototype | | | | |
| 2.AI & Plagiarism Checking | | | | |
| 3.Preparation for Oral Defense | | | | |
| 4.Oral Defense | | | | |

**Table #8 April 2026 Gantt Chart**

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| :--- | :--- | :--- | :--- | :--- |
| 1.Customer Evaluation of Prototype (Stage 1) | | | | |
| 2.Refining Prototype | | | | |

**Table #9 May 2026 Gantt Chart**

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| :--- | :--- | :--- | :--- | :--- |
| 1.Building Prototype (Continued) | | | | |
| 2.Capstone Adviser Consultation | | | | |

**Table #10 June 2026 Gantt Chart**

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| :--- | :--- | :--- | :--- | :--- |
| 1.Building Prototype (Continued) | | | | |
| 2.Customer Evaluation of Prototype (Stage 2) | | | | |
| 3.Capstone Adviser Consultation | | | | |

**Table #11 July 2026 Gantt Chart**

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| :--- | :--- | :--- | :--- | :--- |
| 1.Refining Prototype | | | | |
| 2.Unit Testing | | | | |
| 3.Integration Testing | | | | |
| 4.Capstone Adviser Consultation | | | | |

**Table #12 August 2026 Gantt Chart**

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| :--- | :--- | :--- | :--- | :--- |
| 1.System Testing | | | | |
| 2.Acceptance Testing | | | | |
| 3.Engineer Product | | | | |
| 4.Implementation Plan | | | | |
| 5.Capstone Adviser Consultation | | | | |

**Table #13 September 2026 Gantt Chart**

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| :--- | :--- | :--- | :--- | :--- |
| 6.Engineer Product (Continued) | | | | |
| 7.Final Documentation (Chapter 5) | | | | |
| 8.Capstone Adviser Consultation | | | | |
| 9.Updating, Reviewing, and Revision of the whole document | | | | |

**Table #14 October 2026 Gantt Chart**

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
| :--- | :--- | :--- | :--- | :--- |
| 10.Capstone 2 Defense | | | | |

### 4.2.4 Economic Feasibility

#### 4.2.4.1 Cost and Benefit Analysis

The cost and benefit analysis provides a breakdown of the materials required for development and the specific value each item brings to the study. The proponents have categorized these costs into software and hosting expenses.

**Table #15 Cost and Benefits Table**

| Category | Item | Cost | Benefits |
| :--- | :--- | :--- | :--- |
| Software | RPG Maker MZ (1 License) | ₱2,300.00 | Allows the proponents to develop and test the game concurrently, and provides a built-in event system, and map editor that can reduce the time needed to build the Active Time Battle (ATB) interface and Math Engine from scratch. |
| Hosting | Hostinger Domain & Web Hosting (5 years) | ₱12,108.00 | Allows students to access the game from home through a web browser without requiring a separate installation or a computer |
| TOTAL | Investment Required | ₱14,408.00 | |

#### 4.2.4.2 Cost Recovery Scheme

 The proponents will personally fund the total development cost of ₱16,708.00 as part of their academic requirements. Since the proposed project is not a commercial product, the proponents will not recover the cost through sales or fees. The application will instead be offered for free to students and teachers to support arithmetic learning. The five-year hosting plan included in the budget will keep the system accessible after the development period without additional expense.

### 4.2.5 Requirements Modeling

#### 4.2.5.1 Object Modelling

#### A. Use Case Diagrams

*Figure No. 7:  Educator Use Case Diagrams*

*Figure No. 8:  Student Use Case Diagrams*

#### B. Sequence Diagrams

*Figure No. 9:  Auto Quest Sequence Diagram*

*Figure No. 10:  Enemy Auto-Scaling Sequence Diagram*

*Figure No. 11:   Level-Based Progression Sequence Diagram*

*Figure No. 12:  Math Battle System Sequence Diagram*

*Figure No. 13:  P2P Multiplayer Sequence Diagram*

*Figure No. 14:  Save Sequence Diagram*

#### C. Activity Diagrams

*Figure No. 15: Game Loop of *Chronicles of Arithmos*  Activity Diagram*

### 4.2.6 Risk Assessment/Analysis

Developing *Chronicles of Arithmos* comes with six identified risks that the proponents have identified and prepared for. The proponents have limited experience with JavaScript and PeerJS, which may cause technical delays in building the Math Battle System and multiplayer features and differences between the desktop, web, and mobile versions may cause inconsistencies. The large project scope may lead to schedule delays, while students may lose interest if math overshadows the gameplay.

External dependencies such as PeerJS and NW.js may receive breaking updates, and students' computers may lack adequate hardware or internet access. To reduce these risks, the proponents will study online resources and consult the proponents Capstone Adviser for guidance, Mr. Jan Nicole B. Apostol, lock software versions during development, prioritize core features first with remaining items as stretch goals, review early prototypes for gameplay balance, offer an offline single-player option via windows executable application as a fallback when students are not playing via the web application.

## 4.3 Design

### 4.3.1 Output and User-interface Design

The proponents designed the interface for *Chronicles of Arithmos* using a 2D pixel art style for all game assets and entities. The color scheme uses deep blue (#005385) for menu outlines and for active buttons that are currently pressed. Black (#000000) serves as the background color for all buttons and menu windows. White (#FFFFFF) is used for all text, mathematical equations, and numerical values.

                       (Hex: #005385)                 (Hex: #000000)                 (Hex: #FFFFFF)

*Figure No. : Dark Blue, Black and White*

The proponents chose the M+ 1m regular font as it is a typeface made for clear reading with uses that range from digital signs and multilingual systems, to computer screens and tools for writing code.

*Figure No. : M+ 1m regular Font*

## REFERENCES

[1] B. Bruckman, "The 'Chocolate-Covered Broccoli' Problem," International Journal of Game-Based Learning, vol. 3, no. 2, pp. 1-15, 2013. [Online]. Available: <https://www.google.com/search?q=https://www.researchgate.net/publication/220968132_The_Chocolate-Covered_Broccoli_Problem>

[2] M. Csikszentmihalyi, Flow: The Psychology of Optimal Experience. New York, NY: Harper & Row, 1990. [Online]. Available: <https://www.HarperCollins.com/products/flow-mihaly-csikszentmihalyi>

[3] F. C. Richardson and R. M. Suinn, "The Mathematics Anxiety Rating Scale: Psychometric data," Journal of Counseling Psychology, vol. 19, no. 6, pp. 551–554, 1972. [Online]. Available: <https://www.google.com/search?q=https://psycnet.apa.org/record/1973-09757-001>

[4] M. H. Ashcraft, "Math anxiety: Personal, educational, and cognitive consequences," Current Directions in Psychological Science, vol. 11, no. 5, pp. 181–185, 2002. [Online]. Available: <https://journals.sagepub.com/doi/10.1111/1467-8721.00196>

[5]J. P. Gee, What Video Games Have to Teach Us About Learning and Literacy. New York, NY: Palgrave Macmillan, 2003. [Online]. Available: <https://www.google.com/search?q=https://link.springer.com/book/10.1007/978-1-137-52660-3>

[6] C. Wardoyo et al., "Influence of Game-Based Learning in Mathematics Education on the Students' Cognitive and Affective Domain: A Systematic Review," Education Research International, 2023. [Online]. Available: <https://pmc.ncbi.nlm.nih.gov/articles/PMC10720791/>
[7] A. Karamehic et al., "The Role of Technological Interventions in Alleviating Math Anxiety Among Primary School Students: A Systematic Literature Review," Contemporary Educational Technology, 2024. [Online]. Available: <https://www.cedtech.net/article/the-role-of-technology-in-reducing-mathematics-anxiety-in-primary-school-students-14717>
[8] A. Perttula et al., "Flow Experience in Game-Based Learning: Enhancing Student Engagement and Knowledge Retention Through Adaptive Design," European Conference on e-Learning, 2023. [Online]. Available: <https://papers.academic-conferences.org/index.php/ecgbl/article/view/3873>
[9] T. Hulse et al., "The Impacts of Three Educational Technologies on Algebraic Understanding in the Context of COVID-19," PLOS ONE, 2023. [Online]. Available: <https://pmc.ncbi.nlm.nih.gov/articles/PMC10125888/>
