# Member Task Assignment & Reporting Guide: Lacsina, Justine C.

> **Role in Project:** Technical Writer / Quality Assurance Tester & Systems Analyst  
> **Primary Chapters:** Chapter 1, Chapter 4

---

## 📌 Assigned Sections Checklist

### Chapter 1: Introduction

- [ ] **1.3.1 Scope (Core Gameplay & Math Modules 1 to 8)**:
  - [ ] 1. Standard Role-Playing Game (RPG) Combat Mechanics (TPB, Turn Structure, Resource Management)
  - [ ] 2. Math Battle System Plugin (In-combat math calculations replacing RNG hit rates)
  - [ ] 3. Level-Based Difficulty System (Player Levels 1–29 Basics, 30–69 Intermediate, 70–100 Advanced PEMDAS)
  - [ ] 4. "Content Aware" Timer System (Dynamic equation timer countdown)
  - [ ] 5. Enemy Auto Scaling System (Party average level stat scaling)
  - [ ] 6. Performance Based Reward Mechanism (2.0x Critical, 1.0x Base, 0.5x Penalty, Miss)
  - [ ] 7. Automatic Quest Generation System (Procedural hunting/gathering quests via Mila)
  - [ ] 8. Peer-to-Peer (P2P) Multiplayer Framework (Direct WebRTC room codes via Alden)

### Chapter 4: Methodology, Results and Discussion

- [ ] **4.2.6 Risk Assessment / Analysis**
  - [ ] Risk Identification (Technical complexity, connection drops, device compatibility, math anxiety balance)
  - [ ] Risk Severity & Probability Matrix
  - [ ] Proactive Mitigation Strategies
- [ ] **4.3.2 Data Design**
  - [ ] Entity Relationships, Data Tables (States, Weapons, Armors, Items, Save Files)
  - [ ] Database Architecture & Data Dictionary
- [ ] **4.3.3 System Architecture**
  - [ ] 4.3.3.1 Network Model (Decentralized Peer-to-Peer communication)
  - [ ] 4.3.3.2 Network Topology (Mesh connection between host and client devices)
  - [ ] 4.3.3.3 Security (LocalStorage isolation, sandboxed browser execution, room code privacy)
- [ ] **4.4.4 Programming Environment**
  - [ ] 4.4.4.1 Front End (RPG Maker MZ rendering, WebGL canvas, touch event responsiveness)
  - [ ] 4.4.4.2 Back End (Client-side JavaScript architecture, PeerJS signaling)
  - [ ] 4.4.4.3 Programming Considerations and Issues (Scaling formulas, memory optimization, touch latency, host disconnects)
- [ ] **4.5.2 Integration Testing**
  - [ ] 4.5.2.1 Compatibility Testing (Cross-platform testing on Windows 10/11, Chrome, Edge, Firefox, Brave, Mobile devices: Redmi, Infinix, iPhone, Galaxy)
  - [ ] 4.5.2.2 Performance Testing (Pacing time and response time benchmarks across Windows Desktop, Web Desktop, and Web Mobile environments)

---

## 🎙️ Oral Defense & Presentation Reporting Script Guide

### In Chapter 1, you have to report:

1. **Core Scope & Mechanics (1.3.1 Modules 1–8)**:
   - Walk through the main functional boundary of the game:
     - **Time Progress Battle (TPB)**: Action gauges fill based on Agility; timers freeze when the math window opens so students can calculate without taking incoming damage.
     - **Math Battle Plugin**: Replaces random dice rolls with mental calculations.
     - **Difficulty Progression**: Level 1–29 (Addition/Subtraction), Level 30–69 (Multiplication/Division), Level 70–100 (Full PEMDAS with Parentheses).
     - **Content-Aware Timer & Rewards**: Countdown duration expands based on equation length; correct+fast answers yield **2.0x Critical Hits**, while slow/incorrect answers yield penalties.
     - **Multiplayer**: P2P room code cooperative play without account registration.

### In Chapter 4, you have to report:

1. **Risk Assessment & Mitigation (4.2.6)**:
   - Explain the technical and operational risks identified during development (e.g., JavaScript/PeerJS learning curves, potential game pacing fatigue, network latency).
   - Explain the proactive mitigations: version locking, adviser consultations with Mr. Jan Nicole B. Apostol, stress-free Town Training Halls, and offline single-player fallback.

2. **Data Design & Database Architecture (4.3.2)**:
   - Present the database structure for actors, enemy stats, weapon attributes, states/buffs, and local save files.

3. **System Architecture & Security (4.3.3)**:
   - Detail the **P2P Decentralized Network Topology** (direct data exchange between host and peer instances).
   - Highlight **Security & Privacy**: the game collects zero personal information, requires no login credentials, and isolates save data inside the browser's LocalStorage sandbox.

4. **Programming Considerations (4.4.4)**:
   - Discuss how the team solved equation generation memory loads, standardized touch event latency, and handled P2P host disconnection.

5. **Compatibility Testing (4.5.2.1)**:
   - Present the results of testing across Windows 10/11, multiple Chromium/Gecko browsers (Edge, Chrome, Firefox, Brave, Opera GX), and multiple mobile test phones (Redmi Note 10 5G, Infinix Hot 30i/Note 12, iPhone 15 Pro Max, Galaxy A73 5G).

6. **Performance Testing (4.5.2.2)**:
   - Present the pacing time and response time benchmarks across the three execution platforms:
     - **Windows Desktop**: 5s launch/pacing, 7s title screen, sub-second combat actions, 5s late timer calculation.
     - **Web Desktop**: 3s launch under 5s pacing, sub-second arithmetic/attack executions, 3–10s P2P synchronization.
     - **Web Mobile**: 6s launch under 5s pacing, 1s virtual keypad latency, 3s save load, 3–10s multiplayer synchronization.
