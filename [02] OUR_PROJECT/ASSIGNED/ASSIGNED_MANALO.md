# Member Task Assignment & Reporting Guide: Manalo, Allan Joshua C.

> **Role in Project:** Systems Analyst / QA Tester & Research Specialist  
> **Primary Chapters:** Chapter 1, Chapter 3, Chapter 5

---

## 📌 Assigned Sections Checklist

### Chapter 1: Introduction

- [ ] **1.3.1 Scope (System Infrastructure & Assets 9 to 12)**:
  - [ ] 9. Saving System (20 manual save slots + automated map-transition checkpoints)
  - [ ] 10. Level Based Progression System (EXP milestones, Gold currency, Story Biome unlocks)
  - [ ] 11. Mobile Detection System and Virtual Numeric Keypad (Dynamic touch detection & on-screen keypad overlay)
  - [ ] 12. Game Assets and Entities (28-character NPC roster, 4 biome maps, audio tracks, equipment)
- [ ] **1.3.2 Limitations (All 7 Justified Constraints)**:
  - [ ] 1. Mathematical Scope and Generation Limits (Whole numbers only, max 20 divisor/multiplier caps)
  - [ ] 2. Input Handling Differences (Absence of tactile haptic feedback on flat glass screens)
  - [ ] 3. Input Method (Typing latency variance between physical keyboard numpads vs. mobile touch taps)
  - [ ] 4. Asset Fidelity (2D pixel art engine limits, absence of 3D physics)
  - [ ] 5. Peer to Peer Latency Sensitivity (Multiplayer timer synchronization dependent on host upload speed)
  - [ ] 6. Host Dependent Connection (Multiplayer session collapse if host player disconnects; no central lobby)
  - [ ] 7. Local Only Save Data (Local device storage only; absence of cross-platform cloud sync)

### Chapter 3: Technical Background

- [ ] **3.2 Implementation (Deployment & User Environment)**
  - [ ] 3.2.1 Hardware (Personal Computers / Laptops, Mobile Devices)
  - [ ] 3.2.2 Software (Operating Systems: Windows 10/11, Android, iOS; Chromium-based Browsers: Chrome, Edge)
  - [ ] 3.2.3 Peopleware (Young Learners aged 9–12 & General Casual Users)
  - [ ] 3.2.4 Network (Internet connection requirements: 5–10 Mbps for P2P multiplayer)

### Chapter 5: Conclusion and Recommendations

- [ ] **5.2 Recommendations (Future Enhancements)**:
  - [ ] Math Battle System (Adding support for fractions, decimals, and negative numbers for advanced practice)
  - [ ] Automatic Quest Generation System (Adding arithmetic logic riddles alongside monster hunts)
  - [ ] Performance Reward Mechanism (Implementing visual achievement badges, trophies, and unlockable avatar titles)

---

## 🎙️ Oral Defense & Presentation Reporting Script Guide

### In Chapter 1, you have to report:

1. **Infrastructure Scope (1.3.1 Modules 9–12)**:
   - **Saving System**: Explain how local device storage is managed via 20 manual save slots plus an auto-checkpoint slot triggered when players walk across map boundary lines.
   - **Progression System**: Detail the leveling formula, EXP reward bounds (10 EXP minimum from Level 1 Slimes to 99,999 EXP from final bosses), and Gold drops (5 G to 50,000 G) used for equipment upgrades.
   - **Mobile Touch Keypad**: Explain how the game checks user-agent screen capabilities to pop up the on-screen numeric keypad beside the combat equation prompt.
   - **World Assets**: Describe the world-building components across the 4 major regions (Forest, Desert, Tundra, Volcano), the 28-character story roster, and 30+ regional BGM tracks.

2. **Project Limitations & Operational Justifications (1.3.2)**:
   - *Crucial Panel Defense*: In DCT CCS guidelines, every limitation must have an explicit reason:
     - *Why whole numbers only?* To maintain fast-paced combat flow and prevent Grade 4–6 learners from getting bogged down typing long decimal strings.
     - *Why a max multiplier of 20?* To align strictly with DepEd MATATAG mental arithmetic speed competencies without requiring scratch paper.
     - *Why P2P instead of a dedicated server?* To keep the project 100% free, low-maintenance, and deployable in schools with zero server maintenance overhead.
     - *Why local saves?* To protect minor student privacy (no emails or passwords collected) and enable 100% offline play on PC.

### In Chapter 3, you have to report:

1. **Implementation Environment (3.2)**:
   - **Hardware Specifications (3.2.1)**: Detail the target client machines (standard school computer lab desktop/laptop or student mobile smartphone/tablet).
   - **Software Ecosystem (3.2.2)**: Explain that the game runs universally across Windows, Android, and iOS using standard web browsers (Chrome, Edge, Safari) or the standalone desktop executable.
   - **Target Audience & Peopleware (3.2.3)**: Describe the primary end-users (Grade 4–6 elementary learners aged 9–12) and casual users seeking mental math practice.
   - **Network Requirements (3.2.4)**: Clarify that single-player mode requires 0 Mbps (100% offline), while P2P multiplayer requires only a lightweight 5–10 Mbps connection.

### In Chapter 5, you have to report:

1. **Actionable Recommendations (5.2)**:
   - **Math Expansion**: Propose extending the engine to Junior High School math competencies (fractions, decimals, basic algebraic variables).
   - **Quest System**: Propose procedural riddle quests where NPCs require solving math word problems to open secret dungeon pathways.
   - **Gamification**: Propose achievement trophies (e.g., *"Speed Demon: 10 Critical Hits in a Row"*) to boost long-term replay value and intrinsic learner motivation.
