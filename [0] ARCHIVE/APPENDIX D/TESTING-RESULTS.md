# Testing Results: Chronicles of Arithmos

This document compiles the formal testing documents, unit test matrices, compatibility evaluations, performance benchmarks, and user survey instruments for *Chronicles of Arithmos: A 2D Role-Playing Game with Dynamic Math-Based Combat System and Adaptive Difficulty Scaling*.

---

## 1. Program Specifications

The program specifications define the core software modules, operational objectives, and system runtime events of *Chronicles of Arithmos*.

### 1.1 System Initialization and Title Lifecycle
* **Module:** System Initialization & Title Lifecycle
* **Purpose:** To initialize the game engine, render the title interface, and manage player session loading.
* **System Events and Operations:**
  1. Initiate application when the standalone desktop executable or web page is launched.
  2. Display the Title Screen interface (New Game, Continue, Options, Quit Game).
  3. Display the Options interface when Options is selected.
  4. Load local save file data when Continue is selected.
  5. Exit application when the quit option is selected.

### 1.2 Standard RPG Combat Mechanics & Math Battle System
* **Module:** Standard RPG Combat Mechanics & Math Battle System
* **Purpose:** To manage core combat turns and replace chance-based attacks with direct mathematical challenges.
* **System Events and Operations:**
  1. Fill character Action Gauges based on the Speed/Agility statistic.
  2. Display the visual combat menu (Attack, Skills, Guard, Items) when an Action Gauge is full.
  3. Track and update Health Points (HP), Mana Points (MP), and Tactical Points (TP) pools.
  4. Display a generated math equation in an input window when a combat action is selected.
  5. Accept numerical inputs via physical keyboard or virtual keypad.
  6. Execute the combat action upon pressing the "Enter" or "Submit" key.

### 1.3 Level-Based Difficulty System
* **Module:** Level-Based Difficulty System
* **Purpose:** To automatically adjust the complexity and types of math equations based on the player's current level.
* **System Events and Operations:**
  1. Generate addition and subtraction problems (two values) for player levels 1 to 29.
  2. Introduce multiplication and division equations for player levels 30 to 69.
  3. Generate three-part equations utilizing full PEMDAS rules for player levels 70 to 100.
  4. Scale equations dynamically or provide fixed-level equations during Training Dummy practice sessions.

### 1.4 Content-Aware Timer System
* **Module:** Content-Aware Timer System
* **Purpose:** To dynamically calculate the time limit for answering equations based on their complexity.
* **System Events and Operations:**
  1. Pause Time Progress Battle (TPB) action gauges the moment the math input window appears.
  2. Calculate total time limit based on the number of digits and types of math operators used.
  3. Display and update a visual countdown bar on the battle screen.
  4. Mark the user's input as "slow" if the answer is submitted after the countdown hits zero.

### 1.5 Enemy Auto-Scaling System
* **Module:** Enemy Auto-Scaling System
* **Purpose:** To balance map areas by dynamically scaling enemy stats to match the player's party level.
* **System Events and Operations:**
  1. Calculate the average level of the player's party upon initiating a combat encounter.
  2. Update the enemy's Health Points (HP) and Attack power (ATK) to match the party's level.
  3. Update the Experience Points (EXP) and Gold rewards dropped by the enemy based on the scale.

### 1.6 Performance-Based Reward Mechanism
* **Module:** Performance-Based Reward Mechanism
* **Purpose:** To determine the effectiveness of combat actions based on the speed and accuracy of the player's math input.
* **System Events and Operations:**
  1. Apply a 2.0x critical multiplier to the action's effect if the answer is correct and rapid.
  2. Execute the action at its normal 1.0x base value if the answer is correct but slow.
  3. Apply a 0.5x penalty to the action's effect if the answer is fast but wrong.
  4. Nullify the action completely (move fails) if the answer is incorrect and slow.

### 1.7 Automatic Quest Generation System
* **Module:** Automatic Quest Generation System
* **Purpose:** To dynamically build side quests (hunting and gathering) without requiring manual mission design.
* **System Events and Operations:**
  1. Scan the game database for monsters and items present within the maps the player has unlocked.
  2. Display new generated quest options when the player interacts with Receptionist Mila.
  3. Record the active task in the Quests tab if the player selects "Accept".
  4. Remove the task and queue a new generation if the player selects "Reject".

### 1.8 Peer-to-Peer (P2P) Multiplayer Framework
* **Module:** Peer-to-Peer (P2P) Multiplayer Framework
* **Purpose:** To enable cooperative multiplayer gameplay via direct connections without a centralized server.
* **System Events and Operations:**
  1. Display multiplayer options when the player interacts with Portal Keeper Alden.
  2. Generate and display a unique text-based Room Code when "Host Room" is selected.
  3. Prompt for text input when "Join Room" is selected.
  4. Establish a direct connection and merge the joiner's party with the host's party upon code verification.

### 1.9 Local Saving System
* **Module:** Saving System
* **Purpose:** To record and load the player's game progress using local files on the device.
* **System Events and Operations:**
  1. Display 20 manual save slots when the Save screen is opened from the main menu.
  2. Overwrite the selected manual slot with current game data upon user confirmation.
  3. Trigger an automatic save overwrite to a dedicated slot when the character moves through map exits.

### 1.10 Level-Based Progression System
* **Module:** Level-Based Progression System
* **Purpose:** To track player growth, award resources, and unlock advanced game stages and story events.
* **System Events and Operations:**
  1. Award Experience Points (EXP) and Gold (Currency) upon defeating enemies or completing quests.
  2. Raise the character's level when the required EXP threshold is met.
  3. Update Story Milestones to unlock higher-level maps, new biomes, and harder math stages.

### 1.11 Mobile Input System (Virtual Numeric Keypad)
* **Module:** Mobile Input System (Virtual Numeric Keypad)
* **Purpose:** To provide touchscreen support for mobile device users during math-based combat.
* **System Events and Operations:**
  1. Detect if the application is running on a touch-enabled mobile device or tablet.
  2. Display an on-screen Virtual Numeric Keypad next to the math input window during combat.
  3. Submit the numerical answer to the Math Engine when the user taps the on-screen "Submit" button.

---

## 2. Unit Testing Results

**Project Title:** *Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling*  
**Overall Result:** **PASSED**

| Module / Operational Event | Status (Passed / Failed) |
| :--- | :--- |
| **System Initialization** | |
| Initiate application when the user launches the game executable or web page. | Passed |
| Display the Title Screen interface (New Game, Continue, Options, Quit). | Passed |
| Display the Options interface when the user selects Options. | Passed |
| Load local save file data when the user selects Continue. | Passed |
| Exit application when the user selects the quit option. | Passed |
| **Standard RPG Combat Mechanics & Math Battle System** | |
| Fill character Action Gauges based on the Speed/Agility statistic. | Passed |
| Display the visual combat menu (Attack, Skills, Items) when an Action Gauge is full. | Passed |
| Track and update Health Points (HP), Mana Points (MP), and Tactical Points (TP) pools. | Passed |
| Display a generated math equation in an input window when the user selects a combat action. | Passed |
| Accept numerical inputs when the user uses the physical keyboard or virtual keypad. | Passed |
| Execute the combat action when the user presses the Enter or Submit key. | Passed |
| **Level-Based Difficulty System** | |
| Generate addition and subtraction problems (two values) for player levels 1 to 29. | Passed |
| Introduce multiplication and division equations for player levels 30 to 69. | Passed |
| Generate three-part equations utilizing full PEMDAS rules for player levels 70 to 100. | Passed |
| Scale equations dynamically or provide fixed-level equations during Training Dummy practice sessions. | Passed |
| **Content-Aware Timer System** | |
| Pause Time Progress Battle (TPB) action gauges the moment the math input window appears. | Passed |
| Calculate total time limit based on the number of digits and types of math operators used. | Passed |
| Display and update a visual countdown bar on the battle screen. | Passed |
| Mark the user's input as slow if the user submits the answer after the countdown hits zero. | Passed |
| **Enemy Auto-Scaling System** | |
| Calculate the average level of the player's party upon initiating a combat encounter. | Passed |
| Update the enemy's Health Points (HP) and Attack power (ATK) to match the party's level. | Passed |
| Update the Experience Points (EXP) and Gold rewards dropped by the enemy based on the scale. | Passed |
| **Performance-Based Reward Mechanism** | |
| Apply a 2.0x critical multiplier to the action's effect if the user answers correctly and rapidly. | Passed |
| Execute the action at its normal 1.0x base value if the user answers correctly but slowly. | Passed |
| Apply a 0.5x penalty to the action's effect if the user answers fast but wrong. | Passed |
| Nullify the action completely (move fails) if the user answers incorrectly and slowly. | Passed |
| **Automatic Quest Generation System** | |
| Scan the game database for monsters and items present within the maps the user has unlocked. | Passed |
| Display new generated quest options when the user interacts with Receptionist Mila. | Passed |
| Record the active task in the Quests tab if the user selects Accept. | Passed |
| Remove the task and queue a new generation if the user selects Reject. | Passed |
| **Peer-to-Peer (P2P) Multiplayer Framework** | |
| Display multiplayer options when the user interacts with Portal Keeper Alden. | Passed |
| Generate and display a unique text-based Room Code when the user selects Host Room. | Passed |
| Prompt for text input when the user selects Join Room. | Passed |
| Establish a direct connection and merge the joiner's party with the host's party upon code verification. | Passed |
| **Saving System** | |
| Display 20 manual save slots when the user opens the Save screen from the main menu. | Passed |
| Overwrite the selected manual slot with current game data when the user confirms. | Passed |
| Trigger an automatic save overwrite to a dedicated slot when the user moves the character through map exits. | Passed |
| **Level-Based Progression System** | |
| Award Experience Points (EXP) and Gold (Currency) upon defeating enemies or completing quests. | Passed |
| Raise the character's level when the required EXP threshold is met. | Passed |
| Update Story Milestones to unlock higher-level maps, new biomes, and harder math stages. | Passed |
| **Mobile Input System** | |
| Detect if the application is running on a touch-enabled mobile device or tablet. | Passed |
| Display an on-screen Virtual Numeric Keypad next to the math input window during combat. | Passed |
| Submit the numerical answer to the Math Engine when the user taps the on-screen Submit button. | Passed |

---

## 3. Compatibility Test Results

### 3.1 Web Desktop Compatibility Matrix

| Evaluation Criteria | Microsoft Edge | Google Chrome | Opera GX | Mozilla Firefox | Brave |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Did the application launch properly? | Passed | Passed | Passed | Passed | Passed |
| Did the UI adjust correctly to the screen resolution? | Passed | Passed | Passed | Passed | Passed |
| Did the main menu display properly? | Passed | Passed | Passed | Passed | Passed |
| Did the animation work as expected? | Passed | Passed | Passed | Passed | Passed |
| Did all interactive buttons function correctly? | Passed | Passed | Passed | Passed | Passed |
| Did the Combat Mechanics Module function correctly? | Passed | Passed | Passed | Passed | Passed |
| Did the Level-Based Difficulty System function correctly? | Passed | Passed | Passed | Passed | Passed |
| Did the Peer-to-Peer Multiplayer Framework function correctly? | Passed | Passed | Passed | Passed | Passed |

### 3.2 Windows Desktop Compatibility Matrix

| Evaluation Criteria | Windows 10 PC | Windows 11 PC | Windows 10 Laptop | Windows 11 Laptop |
| :--- | :---: | :---: | :---: | :---: |
| Did the application install properly? | Passed | Passed | Passed | Passed |
| Did the application launch properly? | Passed | Passed | Passed | Passed |
| Does the application run without the internet? | Passed | Passed | Passed | Passed |
| Did the UI adjust correctly to the screen resolution? | Passed | Passed | Passed | Passed |
| Did the main menu display properly? | Passed | Passed | Passed | Passed |
| Did the animation work as expected? | Passed | Passed | Passed | Passed |
| Did all interactive buttons function correctly? | Passed | Passed | Passed | Passed |
| Did the Combat Mechanics Module function correctly? | Passed | Passed | Passed | Passed |
| Did the Level-Based Difficulty System function correctly? | Passed | Passed | Passed | Passed |
| Did the Peer-to-Peer Multiplayer Framework function correctly? | Passed | Passed | Passed | Passed |

### 3.3 Mobile Web Compatibility Matrix

| Evaluation Criteria | Redmi Note 10 5G | INFINIX HOT 30i | INFINIX NOTE 12 | iPhone 15 Pro Max | Oppo A52 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Did the application launch properly? | Passed | Passed | Passed | Passed | Passed |
| Did the UI adjust correctly to the screen resolution? | Passed | Passed | Passed | Passed | Passed |
| Did the main menu display properly? | Passed | Passed | Passed | Passed | Passed |
| Did the animation work as expected? | Passed | Passed | Passed | Passed | Passed |
| Did all interactive buttons function correctly? | Passed | Passed | Passed | Passed | Passed |
| Did the Combat Mechanics Module function correctly? | Passed | Passed | Passed | Passed | Passed |
| Did the Level-Based Difficulty System function correctly? | Passed | Passed | Passed | Passed | Passed |
| Did the Mobile Input System function correctly? | Passed | Passed | Passed | Passed | Passed |
| Did the Peer-to-Peer Multiplayer Framework function correctly? | Passed | Passed | Passed | Passed | Passed |

---

## 4. Performance Test Results

### 4.1 Performance Test: Windows Desktop Edition

| Module | Action | Concurrent Users | Pacing Time | Response Time |
| :--- | :--- | :---: | :---: | :---: |
| **System Initialization** | Initiate application when the game executable is launched. | 1 | 5 seconds | < 1.5 s |
| | Display the Title Screen interface (New Game, Continue, Options, Quit Game). | 1 | - | < 0.2 s |
| | Display the Options interface when Options is selected. | 1 | 3 seconds | < 0.1 s |
| | Load local save file data when Continue is selected. | 1 | 5 seconds | < 0.3 s |
| | Exit application when the quit option is selected. | 1 | 3 seconds | Instant |
| **Standard RPG Combat & Math Battle** | Fill character Action Gauges based on Speed/Agility. | 1 | - | Real-time |
| | Display combat menu (Attack, Skills, Items) when Gauge is full. | 1 | - | Instant |
| | Track and update HP, MP, and TP pools. | 1 | - | Instant |
| | Display generated math equation in input window when action is selected. | 1 | 3 seconds | < 0.05 s |
| | Accept numerical inputs via physical keyboard. | 1 | 5 seconds | Real-time |
| | Execute combat action upon pressing Enter / Submit. | 1 | - | < 0.1 s |
| **Level-Based Difficulty System** | Generate addition & subtraction (Levels 1–29). | 1 | - | < 0.02 s |
| | Introduce multiplication & division (Levels 30–69). | 1 | - | < 0.02 s |
| | Generate three-part PEMDAS equations (Levels 70–100). | 1 | - | < 0.03 s |
| | Scale equations during Training Dummy sessions. | 1 | - | < 0.02 s |
| **Content-Aware Timer System** | Pause TPB gauges when math input appears. | 1 | - | Instant |
| | Calculate total time limit based on digits & operators. | 1 | - | < 0.01 s |
| | Display and animate visual countdown bar. | 1 | - | 60 fps |
| | Mark input as slow if submitted after countdown zero. | 1 | 10 seconds | Instant |
| **Enemy Auto-Scaling System** | Calculate average party level upon encounter init. | 1 | - | < 0.02 s |
| | Update enemy HP and ATK to match party level. | 1 | - | < 0.01 s |
| | Scale EXP and Gold rewards based on scale factor. | 1 | - | < 0.01 s |
| **Performance-Based Reward** | Apply 2.0x critical multiplier if correct and fast. | 1 | - | Instant |
| | Execute 1.0x normal value if correct but slow. | 1 | - | Instant |
| | Apply 0.5x penalty if fast but wrong. | 1 | - | Instant |
| | Nullify action completely if incorrect and slow. | 1 | - | Instant |
| **Automatic Quest Generation** | Scan database for unlocked biome monsters & items. | 1 | - | < 0.05 s |
| | Display generated quests upon Mila interaction. | 1 | 3 seconds | < 0.1 s |
| | Record active task in Quests tab upon Accept. | 1 | 5 seconds | Instant |
| | Remove task and queue new generation upon Reject. | 1 | 3 seconds | Instant |
| **Peer-to-Peer Multiplayer** | Scan database for monster and quest sync. | 2 | 3 seconds | < 0.2 s |
| | Display quest options during Mila interaction in co-op. | 2 | 5 seconds | < 0.3 s |
| | Record active task in Quests tab across both peers. | 2 | 5 seconds | < 0.2 s |
| | Remove task and queue new generation across peers. | 2 | 10 seconds | < 0.2 s |
| **Saving System** | Display 20 manual save slots when Save screen opens. | 1 | 3 seconds | < 0.1 s |
| | Overwrite selected slot upon user confirmation. | 1 | 5 seconds | < 0.2 s |
| | Trigger automatic save overwrite on map transitions. | 1 | - | < 0.1 s |
| **Progression System** | Award EXP and Gold upon victory or quest completion. | 1 | 3 seconds | Instant |
| | Raise character level when EXP threshold is met. | 1 | - | Instant |
| | Update Story Milestones to unlock maps and math stages. | 1 | - | Instant |

### 4.2 Performance Test: Web Desktop Edition

| Module | Action | Concurrent Users | Pacing Time | Response Time |
| :--- | :--- | :---: | :---: | :---: |
| **System Initialization** | Initiate application when web page is launched. | 1 | 5 seconds | < 2.0 s |
| | Display Title Screen interface. | 1 | - | < 0.2 s |
| | Display Options interface when selected. | 1 | 3 seconds | < 0.1 s |
| | Load local save file data when Continue is selected. | 1 | 5 seconds | < 0.3 s |
| | Exit application when quit is selected. | 1 | 3 seconds | Instant |
| **Combat & Math Battle** | Fill character Action Gauges based on Agility. | 1 | - | Real-time |
| | Display visual combat menu when Gauge is full. | 1 | - | Instant |
| | Track and update HP, MP, and TP pools. | 1 | - | Instant |
| | Display generated math equation in input window. | 1 | 3 seconds | < 0.05 s |
| | Accept numerical inputs via physical keyboard. | 1 | 5 seconds | Real-time |
| | Execute combat action upon Enter / Submit. | 1 | - | < 0.1 s |
| **Difficulty Scaling & Timer** | Generate two-term arithmetic (Levels 1–29). | 1 | - | < 0.02 s |
| | Introduce multiplication/division (Levels 30–69). | 1 | - | < 0.02 s |
| | Generate multi-step PEMDAS (Levels 70–100). | 1 | - | < 0.03 s |
| | Pause TPB gauges and compute time limit. | 1 | - | Instant |
| | Render animated countdown bar. | 1 | - | 60 fps |
| **P2P Multiplayer** | Establish WebRTC data channel via PeerJS room code. | 2 | 5 seconds | < 1.0 s |
| | Exchange live combat packets and turn state. | 2 | Real-time | < 80 ms |
| **Saving & Progression** | Serialize game state to browser IndexedDB / localStorage. | 1 | 5 seconds | < 0.2 s |
| | Restore session upon reload. | 1 | 5 seconds | < 0.3 s |

### 4.3 Performance Test: Web Mobile Edition

| Module | Action | Concurrent Users | Pacing Time | Response Time |
| :--- | :--- | :---: | :---: | :---: |
| **System Initialization** | Initiate application when web page is launched on mobile browser. | 1 | 5 seconds | < 3.0 s |
| | Display Title Screen interface. | 1 | - | < 0.3 s |
| | Display Options interface when selected. | 1 | 3 seconds | < 0.2 s |
| | Load local save file data when Continue is selected. | 1 | 5 seconds | < 0.4 s |
| **Mobile Input System** | Detect touch-enabled mobile hardware environment. | 1 | - | Instant |
| | Display on-screen Virtual Numeric Keypad during combat. | 1 | - | < 0.05 s |
| | Register on-screen numerical button touches without touch lag. | 1 | - | < 50 ms |
| | Transmit answer to Math Engine upon tapping Submit button. | 1 | 5 seconds | < 0.1 s |
| **Combat & Timer** | Pause TPB action gauges and display math modal. | 1 | 3 seconds | < 0.1 s |
| | Execute performance-based damage multiplier. | 1 | - | < 0.1 s |
| **P2P Multiplayer** | Connect mobile browser instance to host session. | 2 | 5 seconds | < 1.5 s |

---

## 5. Survey Result Instrument & Form

The following evaluation instrument measures user acceptance and instructional efficacy using a 6-point Likert scale (1 = Strongly Disagree, 2 = Disagree, 3 = Somewhat Disagree, 4 = Somewhat Agree, 5 = Agree, 6 = Strongly Agree).

| Evaluation Category / Statement | 1 (SD) | 2 (D) | 3 (SWD) | 4 (SWA) | 5 (A) | 6 (SA) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **A. Content** | | | | | | |
| 1. The content of *Chronicles of Arithmos* is clear. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 2. The content of *Chronicles of Arithmos* is easy to understand. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 3. The content of *Chronicles of Arithmos* is informative and interesting. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 4. The content of *Chronicles of Arithmos* is user-friendly. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **B. Core Modules** | | | | | | |
| 1. Standard RPG Combat Mechanics operate smoothly. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 2. Math Battle System integrates effectively into turn actions. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 3. Level-Based Difficulty System scales equations appropriately. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 4. Content-Aware Timer System provides sufficient calculation time. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 5. Enemy Auto-Scaling System keeps battles engaging and balanced. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 6. Performance-Based Reward Mechanism motivates fast, accurate calculation. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 7. Automatic Quest Generation System provides varied objectives. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 8. Peer-to-Peer Multiplayer Framework connects smoothly via room codes. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 9. Local Saving System accurately records and loads player progress. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 10. Mobile Input System (Virtual Keypad) is responsive on touch devices. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **C. Multimedia Elements** | | | | | | |
| 1. Font type (M+ 1m) is appropriate and readable. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 2. Font size is well-proportioned across screens. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 3. 2D pixel art images and sprites are visually appealing. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 4. Color scheme (Deep Blue, Black, White) provides high contrast. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 5. System icons and category badges are intuitive. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 6. Interactive buttons and touch targets are easy to tap and click. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **D. Navigation** | | | | | | |
| 1. Overall navigation throughout the game is easy. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 2. Menu transitions are clear and concise. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 3. Moving between gameplay menus and exploration is simple. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **E. Usefulness & Pedagogical Value** | | | | | | |
| 1. *Chronicles of Arithmos* is useful for practicing arithmetic equations. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 2. *Chronicles of Arithmos* is useful for offline entertainment and learning. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 3. *Chronicles of Arithmos* improves rapid problem-solving under time limits. | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
