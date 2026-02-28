# 4.0 Methodology

## 4.1 Prototyping Model
The Prototyping Model is a development cycle used when specific requirements are not fully defined at the start. In this model, an early version of the software is created to gather feedback and refine the logic before building the final product. This approach allows for the testing of math mechanics early in the project life cycle. This methodology verify that the game balance and educational goals are validated through testing instead of committing to a single code structure immediately [5].



*Figure No. :* Prototyping Model

The proponents have selected the Prototyping Model for this study to support the development of the proposed project that requires input to balance instructional content and gameplay engagement for Grade 4 to 6 students. This approach allows the proponents to verify that the mathematical mechanics and educational goals of the game remained aligned through repeated rounds of evaluation and revision, rather than committing to a fixed code structure at the outset.

The Prototyping Model follows a cycle consisting of the following stages:

### 4.1.1 Requirements Gathering
In this phase, the proponents defined the project objectives, scope, and mathematical requirements. The proponents reviewed the Grade 4 to 6 mathematics curriculum to identify the necessary arithmetic operations for the Math Engine. The proponents also surveyed existing educational games and consulted the Capstone Adviser to establish the core functions, which resulted in a documented list of functional requirements and target learning outcomes.


### 4.1.2 Quick Design
The proponents created flowcharts to map the student navigation and battle mechanics. Wireframes were developed to design the main menu, battle interface, and Virtual Numeric Keypad layouts. Finally, the proponents drafted storyboards for the four game biomes (Forest, Desert, Tundra, and Volcanic) to outline the visual progression and enemy placements.

### 4.1.3 Building Prototype
The proponents built the initial prototype using RPG Maker MZ and JavaScript. The Math Battle System plugin was coded to generate arithmetic equations and validate player input via the Virtual Numeric Keypad. The proponents also implemented PeerJS for peer-to-peer (P2P) multiplayer connectivity using room codes and constructed the initial game maps. The Active Time Battle (ATB) timer logic was then integrated into the battle system.

### 4.1.4 Customer Evaluation of Prototype
The proponents will conduct the customer evaluation in two stages. First, the prototype will be presented to the proponents' Capstone Adviser Mr. Jan Nichole B. Apostol for an internal review of the core mechanics. This review will focus on identifying gaps in the Math Engine, difficulty scaling algorithm, and Peer-to-Peer (P2P) connection stability. Second, the proponents will conduct a small-scale usability test with ten (10) Grade 4 to 6 students to gather feedback on gameplay clarity, math problem readability, and overall engagement. The combined feedback from the Capstone Adviser and the student participants will determine if the design aligns with the project objectives or if adjustments are necessary before proceeding with further development.

### 4.1.5 Refining Prototype
The proponents will adjust the system based on the feedback gathered from the Capstone Adviser review and the student usability test. Technical adjustments will be applied to the difficulty scaling algorithm to balance the progression of math problems across enemy tiers. The proponents will revise the battle menu and Virtual Numeric Keypad interface layouts based on observed student interaction patterns. Corrections will also be applied to the P2P synchronization logic to address timing inconsistencies in the peer-to-peer connection.


### 4.1.6 Engineer Product
In this phase, the proponents will perform final system testing to verify that all four biomes, the Math Engine, the adaptive difficulty algorithm, and the multiplayer module operate correctly. After verification, the proponents will package the application as a standalone desktop executable using NW.js and host the web-based version and domain via Hostinger for browser access.

## 4.2 Requirements Specification

### 4.2.1 Operational Feasibility
**A.** Fishbone Diagram
**B.** Functional Decomposition Diagram

### 4.2.2 Technical Feasibility
This section evaluates the hardware and software tools selected for the proposed system to verify that the project is technically achievable. The proponents focus on confirming that all components work together without conflict and that each tool directly supports the goal of teaching arithmetic to students.

#### 4.2.2.1 Compatibility Checking
**A.** Hardware Compatibility
The proponents will develop the game using RPG Maker MZ, which is compatible with standard personal computers having at least 8GB of RAM. Since the game is deployed via HTML5, it will run on devices with a modern web browser that supports HTML5, including the tablets and computers.

**B.** Software Compatibility
The proposed system uses JavaScript to extend the game engine's features, maintaining a consistent connection between the math logic and the RPG mechanics. The PeerJS library is utilized for multiplayer features because it is compatible with web-standard protocols, allowing students to establish peer-to-peer connections without requiring a dedicated central server.



#### 4.2.2.2 Relevance of the Technology
Existing educational game platforms such as Prodigy Math and Math Blaster address arithmetic instruction through gamified exercises; however, a common limitation is that mathematical tasks function as a separate reward layer rather than directly determining gameplay outcomes. Combat sequences in these tools proceed regardless of input accuracy or response speed, which the proposed title is designed to address.

JavaScript (ES6) was chosen because it is the native scripting language of RPG Maker MZ, allowing the proponents to implement the Math Battle Engine and Content-Aware Timer without external dependencies. PeerJS, a WebRTC (Web Real-Time Communication) library, was selected for the multiplayer module as it enables direct Peer-to-Peer connections through room codes without requiring a dedicated server.

The proposed title deploys as a Windows desktop application via NW.js (Node Webkit) and as a web application hosted on Hostinger using HTML5 and Web Graphics Library (WebGL). Desktop is the primary platform because the Math Battle System requires timed numerical input through a physical keyboard, which touchscreens cannot replicate due to the absence of a physical key-press sensation (haptic feedback). The desktop executable can also operate offline using a computer. The web deployment serves as a secondary access point, supported by the Virtual Numeric Keypad module for touch-enabled devices.

### 4.2.3 Schedule Feasibility
**A.** Gantt Chart

**Table #1** November 2025 Gantt Chart

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|
| 1. Capstone Orientation | ■ | | | |
| 2. Grouping of Capstone Members | ■ | | | |
| 3. Planning and Brainstorming | | ■ | ■ | ■ |


**Table #2** December 2025 Gantt Chart

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|
| 1. Requirements Gathering | ■ | ■ | ■ | |
| 2. Quick Design | | ■ | ■ | ■ |

**Table #3** January 2026 Gantt Chart

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|
| 1. Building Initial Prototype | ■ | ■ | ■ | |
| 2. Preparation for Title Defense | ■ | ■ | ■ | |
| 3. Title Defense | | | ■ | |
| 4. Capstone Adviser Consultation | | | ■ | ■ |
| 5. Documentation (Chapter 1) | | | ■ | ■ |

**Table #4** February 2026 Gantt Chart

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|
| 1. Documentation (Chapter 2) | ■ | | | |
| 2. Documentation (Chapter 3) | | ■ | ■ | |
| 3. Capstone Adviser Consultations | | ■ | ■ | |
| 4. Documentation (Chapter 4) | | ■ | ■ | ■ |

**Table #5** March 2026 Gantt Chart

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|
| 1. Building Prototype | ■ | ■ | | |
| 2. AI & Plagiarism Checking | ■ | ■ | | |
| 3. Preparation for Oral Defense | ■ | ■ | | |
| 4. Oral Defense | | | ■ | ■ |

**Table #6** April 2026 Gantt Chart

| Activities | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|
| 1. Customer Evaluation of Prototype | ■ | ■ | | |
| 2. Refining Prototype | ■ | ■ | ■ | ■ |


### 4.2.4 Economic Feasibility

#### 4.2.4.1 Cost and Benefit Analysis
The cost and benefit analysis provides a breakdown of the materials required for development and the specific value each item brings to the study. The proponents have categorized these costs into software and hosting expenses.

**Table #6** Cost and Benefits Table

| Category | Item | Cost | Benefits |
|---|---|---|---|
| Software | RPG Maker MZ (2 Licenses) | ₱4,600.00 | Provides the engine for the Active Time Battle (ATB) and Math Engine logic. |
| Hosting | Hostinger Domain & Web Hosting (5 years) | ₱12,108.00 | Enables cross-platform access via ".site" domain for students at home. |
| **TOTAL** | **Investment Required** | **₱16,708.00** | |

#### 4.2.4.2 Cost Recovery Scheme
The proponents will personally fund the total development cost of ₱16,708.00 as part of their academic requirements. Since the proposed project is not a commercial product, the proponents will not recover the cost through sales or fees. The application will instead be offered for free to students and teachers to support arithmetic learning. The five-year hosting plan included in the budget will keep the system accessible after the development period without additional expense.

### 4.2.5 Requirements Modeling

#### 4.2.5.1 Object Modelling
**A.** Use Case Diagram
**B.** Sequence Diagram
**C.** Activity Diagram

### 4.2.6 Risk Assessment/Analysis
Developing Chronicles of Arithmos comes with six identified risks that the proponents have identified and prepared for. The proponents have limited experience with JavaScript and PeerJS, which may cause technical delays in building the Math Battle System and multiplayer features and differences between the desktop, web, and mobile versions may cause inconsistencies. The large project scope may lead to schedule delays, while students may lose interest if math overshadows the gameplay.

External dependencies such as PeerJS and NW.js may receive breaking updates, and students' computers may lack adequate hardware or internet access. To reduce these risks, the proponents will study online resources and consult the proponents' Capstone Adviser for guidance, Mr. Jan Nicole B. Apostol, lock software versions during development, prioritize core features first with remaining items as stretch goals, review early prototypes for gameplay balance, offer an offline single-player option via windows executable application as a fallback when students are not playing via the web application.

## 4.3 Design

### 4.3.1 Output and User-interface Design
The proponents designed the interface for Chronicles of Arithmos using a 2D pixel art style for all game assets and entities. The color scheme uses deep blue (#005385) for menu outlines and for active buttons that are currently pressed. Black (#000000) serves as the background color for all buttons and menu windows. White (#FFFFFF) is used for all text, mathematical equations, and numerical values. The proponents selected the M+ 1m regular font for all on-screen content to verify that mathematical problems remain readable.


                              (Hex: #005385)                 (Hex: #000000)                 (Hex: #FFFFFF)



*Figure No. :* Dark Blue, Black and White



*Figure No. :* M+ 1m regular Font

The proponents chose the M+ 1m regular font as it is a typeface made for clear reading with uses that range from digital signs and multilingual systems, to computer screens and tools for writing code.


## REFERENCES:


