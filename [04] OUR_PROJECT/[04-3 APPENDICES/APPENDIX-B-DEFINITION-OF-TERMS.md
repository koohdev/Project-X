# Appendix B. Definition of Terms

The following terms are defined based on how they are used in this paper.

---

**Active Time Battle (ATB) / Time Progress Battle (TPB)** – The combat timing system in *Chronicles of Arithmos* where each character has a visible Action Gauge that fills based on their Speed or Agility stat. The moment the Math Input Window appears, all action gauges freeze completely so that enemies cannot act while the player is solving a math equation.

**Adaptive Difficulty Scaling** – The combined operation of the Level-Based Difficulty System and the Enemy Auto-Scaling System working together to ensure that both the math equation complexity and the enemy statistics remain proportional to the player's current progression level throughout the entire game.

**Arithmetic Operations** – The specific mathematical computations that the Math Battle System generates as challenges during combat. These include addition, subtraction, multiplication, division, and multi-operator expressions governed by the PEMDAS rule set, depending on the player's current character level.

**Automatic Quest Generation System** – The module that automatically creates side quests by scanning the specific enemies and collectible items found in all geographical areas the player has currently unlocked. These quests are offered through Receptionist Mila and require no manual authoring.

**Biome** – One of the four distinct geographical regions of the game world in *Chronicles of Arithmos*: the Plains and Forest, the Desert, the Tundra and Frost, and the Volcano and Fire zones. Each biome contains a unique set of enemies, loot drops, and environmental visual themes.

**"Chocolate-Covered Broccoli" Effect** – The design pitfall identified by Bruckman (2013) where a game's educational content is poorly integrated with its gameplay mechanics, resulting in students perceiving the game as a disguised drill and losing motivation to engage with it. *Chronicles of Arithmos* addresses this by making math the direct mechanical input for all combat actions rather than a separate reward layer.

**Chronicles of Arithmos** – The proposed 2D educational Role-Playing Game developed using RPG Maker MZ. It is the primary subject of this study, designed to teach arithmetic to Grade 4–6 students by making the outcome of all combat actions dependent on the player's ability to solve math equations under a time limit.

**Content-Aware Timer System** – The module that dynamically calculates the time limit for answering a math equation during combat. The allowed time window is determined by the equation's complexity, the total number of digits involved, and the types of math operators used, with additional time granted for more complex operations.

**Enemy Auto-Scaling System** – The background module that automatically adjusts enemy statistics—specifically Health Points (HP), Attack power (ATK), Experience Points (EXP), and Gold rewards—based on the active party's average level. This ensures combat difficulty remains consistent across all geographical areas without requiring duplicate enemy entries.

**Experience Points (EXP)** – A numerical reward earned by the player after defeating enemies or completing quests. Accumulating enough EXP increases the player's character level, which in turn triggers difficulty changes in the Level-Based Difficulty System and unlocks new game areas.

**Flowchart** – The diagrams created by the proponents during the Quick Design phase to map the student navigation paths, battle mechanic sequences, and system logic flows for the development of *Chronicles of Arithmos*.

**Flow Theory** – The psychological concept introduced by Csikszentmihalyi describing a mental state where a person is fully focused because the challenge level of a task matches their current skill level. It serves as one of the supporting theories for *Chronicles of Arithmos*, applied through the Adaptive Difficulty Scaling system to keep students engaged without causing boredom or frustration.

**Game-Based Learning (GBL)** – The anchor instructional theory for *Chronicles of Arithmos*, wherein game mechanics such as levels, combat rewards, and character progression are used to deliver and reinforce arithmetic content. The system is built on the principle that students learn mathematical material as a result of engaging with the gameplay itself.

**Gold (G)** – The in-game currency earned by defeating enemies and completing quests in *Chronicles of Arithmos*. Gold is used to purchase equipment and consumable items from in-game merchants as part of the progression system.

**Health Points (HP)** – One of the three primary resource pools managed during combat in *Chronicles of Arithmos*. It represents the amount of damage a character can withstand before being knocked out of the battle.

**Hue Shifting** – The specific color manipulation technique applied using GIMP to create visually distinct, biome-specific enemy variants from a single base sprite asset. For example, the default Slime sprite is recolored to produce the Sand Slime, Ice Slime, and Magma Slime variants for the Desert, Tundra, and Volcano biomes respectively.

**JavaScript (ES6)** – The primary programming language used to develop all custom system plugins for *Chronicles of Arithmos*, including the Math Battle System, the Level-Based Difficulty System, the Enemy Auto-Scaling System, the Automatic Quest Generation system, and the Peer-to-Peer Multiplayer Framework. It was selected because it is the native scripting language of RPG Maker MZ.

**Level-Based Difficulty System** – The module that automatically adjusts the complexity of the math equations generated during combat based on the player character's current level. Players at levels 1–29 receive addition and subtraction equations, levels 30–69 introduce multiplication and division, and levels 70–100 generate multi-operator equations governed by the PEMDAS rule set.

**Level-Based Progression System** – The module that structures the overall educational flow of the game by managing the transition between gameplay stages, triggering story milestones, and unlocking harder math operators as the player's character reaches higher levels.

**Mana Points (MP)** – One of the three primary resource pools managed during combat in *Chronicles of Arithmos*. It is the resource spent to cast magical spells and is managed by the player alongside Health Points and Tactical Points.

**Math Battle System** – The core educational plugin developed for *Chronicles of Arithmos* that replaces standard chance-based combat with direct arithmetic challenges. When a player selects a combat action, the system generates a math equation that the player must solve within a time limit. The correctness and speed of the answer determine the outcome of the action.

**Math Engine** – The underlying logic component of the Math Battle System responsible for generating arithmetic equations according to the parameters defined by the Level-Based Difficulty System and the Content-Aware Timer System.

**Mathematics Anxiety** – The psychological condition described by Ashcraft (2002) and Richardson and Suinn (1972) as a feeling of tension and fear that interferes with a student's ability to manipulate numbers and perform mathematical tasks. It is the primary problem that *Chronicles of Arithmos* is designed to address by reframing arithmetic practice within a low-stakes fantasy game context.

**Narrative-Centered Learning** – One of the supporting theories for *Chronicles of Arithmos*, which holds that embedding academic content within a story context helps students retain the material more effectively. The game applies this through its main story involving Lily's curse and the player's quest to restore world logic by recovering biome fragments.

**NPC (Non-Player Character)** – Any character found in the game world of *Chronicles of Arithmos* that is not directly controlled by the player. NPCs include named story characters such as Receptionist Mila and Portal Keeper Alden, as well as generic background figures such as Townsmen and Market Shoppers who populate the towns.

**NW.js (Node Webkit)** – The open-source runtime framework used to package the HTML5 and JavaScript game engine of *Chronicles of Arithmos* into a standalone Windows desktop executable (.exe) file, enabling the game to run offline with direct access to the local file system for save data.

**P2P (Peer-to-Peer) Multiplayer Framework** – The cooperative multiplayer module that allows two players to connect their game sessions directly using unique text-based Room Codes, without requiring a central dedicated server. The connection is implemented using the PeerJS library and the WebRTC standard.

**PeerJS** – The WebRTC wrapper library used to implement the Peer-to-Peer Multiplayer Framework in *Chronicles of Arithmos*. It manages the generation of Room Codes and facilitates direct browser-to-browser data exchange between the host player and the joining player.

**PEMDAS** – The mathematical order of operations rule set—Parentheses, Exponents, Multiplication, Division, Addition, and Subtraction—that governs the structure of advanced math equations generated by the Level-Based Difficulty System for players at character levels 70 through 100.

**Performance-Based Reward Mechanism** – The module that determines the outcome of a combat action based on two variables: the correctness and the speed of the player's math answer. A correct and rapid answer applies a 2.0x critical multiplier; a correct but slow answer executes the action at its base value; an incorrect but rapid answer applies a 0.5x penalty; and an incorrect and slow answer results in a complete action failure.

**Pixel Art** – The visual art style used for all game assets, maps, characters, and enemy sprites in *Chronicles of Arithmos*, characterized by low-resolution, grid-based graphics rendered in a 2D plane.

**Plains of Origin** – The starting area of the game world in *Chronicles of Arithmos* where the story begins and the player completes the tutorial with mentor characters Bron and Martha.

**Proponents** – The student developers of *Chronicles of Arithmos* who planned, programmed, designed, tested, and documented the proposed system as their capstone project requirement.

**Prototyping Model** – The software development methodology selected for this study, which follows a cycle of Requirements Gathering, Quick Design, Building Prototype, Customer Evaluation, Refining Prototype, and Engineer Product phases. It was chosen because it allows the proponents to verify that the game's math mechanics and educational goals remain aligned through repeated rounds of evaluation and revision.

**Role-Playing Game (RPG)** – The game genre that serves as the foundational framework for *Chronicles of Arithmos*, characterized by character progression through levels and experience points, turn-based or action-based combat, party management, inventory systems, and narrative-driven exploration across a game world.

**Room Code** – The unique text string generated by the Peer-to-Peer Multiplayer Framework when a player hosts a game session through Portal Keeper Alden. Other players use this code to join the host's game session directly.

**RPG Maker MZ** – The primary game development engine used to build *Chronicles of Arithmos*. It provides the built-in architecture for RPG mechanics such as inventory management, map traversal, and the battle interface, which the proponents extended with custom JavaScript plugins to implement the Math Battle System and other proposed features.

**Save System** – The module that records player progress as local files on the user's device. The system provides 20 manual save slots and a dedicated Autosave function that triggers automatically each time the player passes through a map exit checkpoint.

**Standalone Application** – The desktop deployment version of *Chronicles of Arithmos*, packaged as a Windows executable (.exe) file using NW.js, which allows the game to be installed and played offline without requiring a web browser or internet connection for single-player mode.

**Status Effects** – The temporary conditions that can be applied to characters during combat in *Chronicles of Arithmos*. Negative status effects, referred to as debuffs, include Poison, Blind, Silence, Paralysis, and Sleep, among others. Positive status effects, referred to as buffs, include Regenerate, Haste, Protect, Shell, and Focus, among others.

**Tactical Points (TP)** – One of the three primary resource pools managed during combat in *Chronicles of Arithmos*. TP is spent to execute special combat skills unique to each character class.

**The Numeromancer** – The primary antagonist and final boss of *Chronicles of Arithmos*, described as the source of the chaos fractures called Anomalies that the player must resolve throughout the game's story.

**Training Dummy** – The special battle entity found in the Training Hall of every town in *Chronicles of Arithmos*. It possesses infinite Health Points and exists solely so that players can safely practice their mathematical calculation speed and combat mechanics without consequence. Players may exit training sessions at any time by selecting the Escape command.

**Training Hall** – The designated area located in every in-game town that provides players a safe, consequence-free environment to practice math equations and combat skills against a Training Dummy.

**Vercel** – The cloud-based deployment platform used as a staging host for the web-based version of *Chronicles of Arithmos* during the development phase. It connects to the project's GitHub repository to automate the build and provides an HTTPS environment required for the PeerJS and WebRTC handshake.

**Virtual Numeric Keypad** – The on-screen input interface that the Mobile Detection System displays automatically when the Math Input Window opens on a touch-screen device, allowing mobile users to tap numeric buttons to submit their math answers during combat in place of a physical keyboard.

**WebGL (Web Graphics Library)** – A JavaScript API used to render the 2D graphics of *Chronicles of Arithmos* within web browsers, enabling hardware-accelerated graphics for the web-based deployment without requiring the installation of native software on the user's device.

**WebRTC (Web Real-Time Communication)** – The browser-standard communication protocol that underpins the Peer-to-Peer Multiplayer Framework, enabling direct browser-to-browser data connections between players using the PeerJS library.

**Wireframe** – The low-fidelity layout sketches created during the Quick Design phase of the Prototyping Model to plan the visual structure of the main menu, battle interface, and Virtual Numeric Keypad before full development began.
