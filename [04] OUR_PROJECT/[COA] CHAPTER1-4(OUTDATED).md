NOTE: our adviser check these contents and did not approved it for missing stuffs and indication, so technically this is not all right, theres some mistakes here and there.


# 1.0 Introduction

## 1.1 Project Context

 Chronicles of Arithmos is a 2D turn-based Role-Playing Game (RPG) developed using the RPG Maker MZ engine. Unlike traditional RPGs that rely on probabilistic mechanics (RNG) for combat, this project implements a custom Math Battle System where the efficacy of every action attack, defense, and skill usage is directly correlated to the user's ability to solve arithmetic equations under calculated time constraints. The game is designed as a standalone application deployable on Windows desktops and web browsers, featuring a unique "Virtual Keypad" interface for touch-screen accessibility. Educational methodology has increasingly integrated gamification to enhance student engagement and cognitive retention. Chronicles of Arithmos bridges the gap between entertainment and education by transforming abstract mathematical drills into high-stakes fantasy combat. This approach specifically targets the transition from basic arithmetic (Addition/Subtraction) to intermediate operations (PEMDAS), reinforcing mental math speed and accuracy through the "Magic Circle" of play. By linking mathematical success directly to game progression (leveling up, defeating bosses), the system provides immediate, tangible rewards for cognitive effort. Common problems in educational games often include the "Chocolate-Covered Broccoli" effect, where learning mechanics are poorly integrated with gameplay, leading to boredom [1]. Additionally, static difficulty curves can alienate students who find the content either too easy or too difficult [2], and low replayability offers little incentive to return. Chronicles of Arithmos addresses these issues through integrated mechanics where math is the weapon, an Adaptive Difficulty Algorithm that scales equation complexity to the learner's proficiency, and Procedural Quest Generation that ensures infinite replayability without manual content creation. The primary purpose of this project is to alleviate Mathematics Anxiety among Grade 4-6 students. Defined by Richardson and Suinn (1972) as "a feeling of tension and anxiety that interferes with the manipulation of numbers," this phenomenon creates a psychological barrier that hinders academic performance regardless of actual aptitude [3]. Studies by Ashcraft (2002) further suggest that high math anxiety occupies working memory capacity, reducing the cognitive resources available for problem-solving [4]. By gamifying these operations within a low-stakes, fantasy context (the "Magic Circle" of play), Chronicles of Arithmos aims to alleviate the

 negative emotional response typically associated with classroom drills. The immediate, deterministic feedback loop where a correct calculation results in a tangible "Critical Hit" provides dopamine-driven reinforcement, potentially reconditioning the learner's association with arithmetic from fear to empowerment (Gee, 2003) [5]. By providing a safe environment where failure results in a "Game Over" rather than a bad grade, students can practice without fear. The game features a Dynamic Enemy Scaling system that ensures combat remains challenging regardless of the player's level, and a Peer-to-Peer (P2P) Multiplayer mode that fosters cooperative learning and social engagement. The story begins in the Plains of Origin, where the protagonist awakens to find the world filled with " Anomalies" chaos fractures caused by the breakdown of world laws. Guided by their mentors, Bron (Physical Combat) and Martha (Magical Theory), the player completes the "Tutorial Spar" and learns that their younger sister, Lily, has been afflicted by a curse that can only be cured by restoring the world's logic. The protagonist travels across four distinct biomes, each guarded by a corrupted elemental force. They must recover the "Fragments" from the Forest Golem, the Pharaoh's Guard, the Fenrir wolf, and finally the Demon Lord. Along the way, they recruit a diverse party of allies, including the knight Kael and the sorceress Elara, who lend their unique combat strengths to the cause. The journey culminates in the Void Dimension, where the player confronts The Numeromancer, the source of the chaos. In a final test of mastery, the player must utilize their skills both in combat and in math to defeat the Numeromancer, stabilizing the realm and curing Lily. The game world features distinct environmental biomes. The Plains & Forests (Levels 1- 25) serve as lush starter zones focusing on Addition/Subtraction. The Deserts (Levels 25-50) are harsh wastelands introducing Multiplication. The Tundra & Frost (Levels 50-75) regions introduce Division mechanics, while the Volcano & Fire (Levels 75-99) zones. With Dungeons that provide rare enemy encounters and high-tier loot throughout the game. The character roster includes main characters like Bron, Martha, and Lily, alongside recruitable companions such as Kael, Elara, Garrick, Sylas, Isolde, Thorne, Lyra, and Fenrin. Key NPCs driving the narrative and mechanics include Elder Tobias, Merchant Oryn, Receptionist Mila, Bard Jareth, Captain Valerius, Professor Haze, Innkeeper Gorm, Blacksmith Rurik, Widow Claire, Farmer Ben, Alchemist Vanya, Librarian Estel, Guard Captain Aris, Fisherman Old Tom, Street Urchin Pip, Nobleman Caelus, Priestess Anara, and Hunter Kaelen. The primary antagonist

 is The Numeromancer. To populate the world, background NPCs such as Townsmen, Townswomen, Playing Children, Market Shoppers, Tavern Patrons, Castle Guards, Farmhands, Stable Boys, Washerwomen, Street Sweepers, Beggars, Strolling Couples, Academy Students, Visiting Merchants, Nobles, Tourists, Drunkards, Gossiping Ladies, Messengers, Guards, Fishers, Old Ladies, Street Performers, and Crowd Members provide flavor and atmosphere. The game features distinct enemies tailored to each biome. In the Plains, players encounter creatures such as the Slime, Rat, Bat, Spider, Hornet, Wolf, Bear, Treant, Goblin, Goblin Archer, Goblin Shaman, Orc, Bandit, Bandit Leader, Crow, Snake, Fairy, Mandrake, Wild Boar, and Forest Golem. The Desert biome introduces the Sand Slime, Scorpion, Giant Scorpion, Cactus, Sand Worm, Mummy, Skeleton Warrior, Skeleton Mage, Desert Wolf, Lamia, Basilisk, Gargoyle, Sand Golem, Vulture, Sphinx, Desert Rogue, Ant Lion, Dust Spirit, Ancient Scarab, and Pharaoh ’ s Guard. Progressing to the Tundra, hostile entities include the Ice Slime, Snow Wolf, Polar Bear, Ice Bat, Snow Spirit, Yeti, Ice Golem, Crystal Spider, Frost Giant, White Tiger, Corrupted Penguin, Ice Drake, Frozen Knight, Winter Wisp, Wendigo, Frost Mage, Glacial Turtle, Snow Harpy, Ice Elemental, and Fenrir. The Volcano biome challenges players with the Magma Slime, Fire Spirit, Imp, Demon, Succubus, Cerberus, Lava Golem, Fire Bat, Salamander, Dragon Hatchling, Red Dragon, Efreet, Phoenix, Iron Giant, Dark Knight, Cultist, Fire Elemental, Minotaur, Chimera, and Demon Lord. Finally, General enemies found throughout dungeons include the Ghost, Zombie, Vampire, Vampire Bat, Mimic, Shadow, Will-o'-the-Wisp, Animated Armor, Flying Sword, Magic Pot, Gazer, Ogre, Troll, Warlock, Necromancer, Reaper, Chaos Cloud, Number Eater, Equation Spirit, and The Unknown. The item database supports gameplay with consumables like Potions, Hi-Potions, Full Potions, Magic Waters, Hi-Magic Waters, Elixirs, Antidotes, Eye Drops, Echo Herbs, Stimulants, Potent Stimulants, Panaceas, Dispel Herbs, Escape Ropes, and Repel Sprays. Permanent stat boosters include HP Up, MP Up, Strength Seeds, Defense Seeds, Magic Seeds, Agility Seeds, Luck Seeds, and Skill Books. Monster drops are specific to biomes, ranging from Green Gel and Rat Tails in the Plains to Red Gel and Dragon Teeth in the Volcano regions, ensuring a diverse economy for crafting and selling. Players can choose from eight distinct character classes: Swordsman, Sorcerer, Priest, Knight, Martial Artist, Magic Swordsman, Hunter, and Bandit. Each class has access to a specialized weapon arsenal that expands as the player unlocks new biomes. Swordsmen wield

 everything from Long Swords to the Phoenix Feather Sword; Sorcerers progress from Oak Staffs to Hellfire Rods; Priests upgrade from Wooden Maces to Phoenix Down Maces; Knights advance from Short Spears to Hellfire Harpoons; Martial Artists utilize Leather Gloves up to Demon Hands; Magic Swordsmen wield Rapiers through Volcanic Spikes; Hunters upgrade from Short Bows to Phoenix Fire Bows; and Bandits progress from simple Knives to Hell's Tooth daggers. Combat skills are class-specific, with Swordsmen utilizing techniques like Strong Attack and Omnislash, Sorcerers casting elemental spells like Fire and Meteor Swarm, and Priests providing vital support with Heal and Divine Intervention. Knights offer protection with Shield Bash and Castle of Stone, while Martial Artists deal rapid damage with Triple Kick and Seven Star Strike. Magic Swordsmen combine physical and magical attacks, Hunters utilize precision shots and traps, and Bandits focus on stealing and status infliction. These skills interact with various status effects, including negative states like Poison, Silence, and Paralysis, and positive buffs like Regenerate, Haste, and Protect. Equipment options further customize gameplay, with a wide array of Shields, Headgear, Body Armor, and Accessories providing stat boosts and resistance to elemental damage or status ailments.

## 1.2 Objectives

### 1.2.1 General Objective

 The primary objective of this project is to design and develop Chronicles of Arithmos, a 2D turn-based Role-Playing Game (RPG) using the RPG Maker MZ engine, featuring a custom-coded combat system where action outcomes are determined by real-time mathematical problem solving and reaction speed.

### 1.2.2 Specific Objectives

 

**A.** To implement standard RPG battle mechanics. The user interacts with this module by inputting combat commands and managing their party's health and mana during encounters. This includes a time- based battle system, turn ordering, and managing character stats (HP/MP/TP), serving as the base structure for the custom math integration. 

**B.** To develop a Math Battle System plugin. The user interacts with this module by solving generated arithmetic equations within a visual interface using a keyboard to execute actions. This

 replaces standard combat probability (chance to hit) with math challenges, serving as the core educational feature. 

**C.** To implement an Adaptive Difficulty Algorithm. To implement an Adaptive Difficulty Algorithm. The user interacts with this module by experiencing dynamic changes to the complexity of the math problems based on their current character level. This includes changing the number of terms, math operators, and number sizes, keeping the challenge fair and balanced. 

**D.** To engineer a "Content-Aware" Timer System The user interacts with this module by racing against a dynamically calculated countdown to input their answers before the time expires. This includes calculating allowed time based on equation complexity, total digits, and operator types, acting as the time pressure during battles . 

**E.** To integrate an Enemy Auto-Scaling System The user interacts with this module by fighting enemies that remain consistently challenging regardless of the geographical area they are exploring. This includes automatically adjusting enemy stats (Health, Attack) to match the battling party's average level, ensuring game balance without needing to manually create duplicate enemies. 

**F.** To implement an Integer-Only Generation Logic The user interacts with this module by solving equations that are guaranteed to have whole numbers and manageable difficulty limits. This includes restricting division operations to whole numbers and capping multiplication/division numbers at manageable ranges (1-20), preventing the player from getting overly frustrated . 

**G.** To create a Performance-Based Reward Mechanism The user interacts with this module by receiving immediate combat feedback, dealing critical damage for fast answers or missing entirely for slow, incorrect ones. This includes double damage (2.0x) for rapid correct answers and

 half damage (0.5x) or missed attacks for errors, acting as the primary combat reward system. 

**H.** To develop an Automatic Quest Generation system The user interacts with this module by accepting infinite, location-aware side missions from "Quest Giver" NPCs to hunt enemies or gather specific items. This includes automatically checking the active map's enemy and item data, ensuring the game has high replay value without manually typing in every quest. 

**I.** To implement a Peer-to-Peer (P2P) Multiplayer Connection The user interacts with this module by generating a unique "Room Code" to host a game or entering a code to join a friend's game via interacting with an npc. This includes setting up a direct local connection without requiring players to make online accounts, acting as the cooperative gameplay feature. 

**J.** To design and integrate a User Interface (UI) The user interacts with this module by navigating a menu system to track missions, manage inventory, and monitor party stats. This includes a dynamic "Quest Journal" and standard on-screen displays, acting as the main navigation system during gameplay . 

**K.** To integrate a Save System The user interacts with this module by manually saving their progress into dedicated slots and relying on automatic checkpoints when moving between maps. This includes supporting manual saves and automatic checkpoints, saving game progress into local files so players don't lose their data . 

**L.** To engineer a Level-Based Progression System The user interacts with this module by progressing through different stages (Foundational, Intermediate, Advanced) and unlocking harder math operators as their characters level up. This manages the transition between gameplay stages and triggers story events, structuring the game's educational flow.

 

**M.** To implement a Mobile Input System The user interacts with this module by utilizing touch controls on their mobile device to input mathematical answers during combat. This includes automatically identifying mobile browsers and displaying an on-screen number pad, ensuring the game is playable on phones and tablets. 

**N.** To integrate diverse Game Assets and Entities The user interacts with this module by exploring distinct areas (Forests, Deserts, Tundras, Volcanos), defeating area-specific enemies, and equipping various weapon, armor and accessories. This includes a structured collection of pixel-art maps, enemies, and equipment, serving as the main world-building structure.

## 1.3 Scope and Limitations

### 1.3.1 Scope

 

**A.** Standard Role-Playing Game (RPG) Combat Mechanics The user interacts with this module by using a computer mouse or trackpad to click through visual combat menus (such as "Attack," "Skills," or "Items"), explicitly selecting actions to manage their party's health and mana during encounters. The scope of the proposed project includes core combat mechanics structured around: 

**A.1** Time Progress Battle (TPB) A wait-based active battle system used to pause the game for the math input window, preventing enemies from attacking while the player calculates. The system features a visible "Action Gauge" for each combatant that fills based on their Speed/Agility. 

**A.2** Turn Structure Combat follows a specific order of steps: Action Selection (Player Input) -> Math Answer Check -> Action Execution. 

**A.3** Resource Management: Players must manage three primary pools: HP (Health Points/Vitality), MP (Mana Points), and TP (Tactical Points).

 

**A.4** User Interaction: The user interacts with this module by using a computer mouse or trackpad to click through visual combat menus (such as "Attack," "Skills," or "Items"), explicitly selecting actions to manage their party's health and mana during encounters. 

**B.** Math Battle System Plugin. The scope includes a core gameplay loop designed to build skills through repetition and reward. Upon encountering an enemy and selecting an action, the game switches to the Math Battle System. The player must solve the generated equation (scaled to their level) within the time limit to execute the action, replacing traditional chance-based hitting. The user interacts by utilizing the physical keyboard's number row or numpad to type whole-number answers into the screen and pressing the "Enter" key to attack before the visual timer runs out. 

**C.** Adaptive Difficulty Algorithm The user interacts with this module by visually reading the generated equations on the screen and mentally calculating answers for problems that automatically scale in term counts and operator types based on their current character level. The scope of the proposed project includes adaptive difficulty settings. To ensure a steady learning curve, the mathematical difficulty is strictly tiered based on the character's level: 

**C.1** Player Levels 1-29 (Basics): Focuses on simple Addition and Subtraction (2 numbers) to help players build speed and confidence. 

**C.2** Player Levels 30-69 (Intermediate): Introduces Multiplication and Division, requiring players to manage larger numbers and factors. 

**C.3** Player Levels 70-100 (Advanced): Unlocks the full PEMDAS rule set (Parentheses, Exponents, Multiplication, Division, Addition, Subtraction) with 3-part equations, testing the player's ability to solve complex problems quickly.

 D. "Content-Aware" Timer System: The scope of the proposed project includes a dynamic timer that calculates the allowed answer window based on the complexity of the generated equation, total digit length, and operator types. It awards extra time bonuses for more complex operations like multiplication/division or larger values. The user interacts with this module by actively monitoring a visual countdown bar during combat and typing their answers on a keyboard or touchscreen before the calculated time expires. 

**E.** Enemy Auto-Scaling System The scope of the proposed project includes Dynamic Enemy Scaling. This is a background process that automatically adjusts enemy stats (HP, ATK, EXP, Gold) in real- time based on the active party's average level. The user interacts with this module by engaging in combat sequences initiated by walking their character into enemy sprites or during a random encounter while they are roaming the map. fighting against opponents that automatically adjust their health and attack values. F. "Clean Integer" Logic The scope of the proposed project restricts the mathematical equation generator to ensure all division operations result in whole numbers and no decimals. It also caps multiplication and division numbers at manageable ranges (1-20). The user interacts with this module by typing whole-number answers (avoiding fractions or decimals) using the keyboard for equations specifically designed to prevent extreme difficulty spikes. 

**G.** Performance-Based Reward Mechanism The user interacts with this module by reacting quickly with their keystrokes or screen taps to receive immediate visual and sound feedback, dealing critical damage for fast inputs or receiving damage penalties for slow entries. The scope of the proposed project includes a combat calculation step where the specific outcome of an action is decided by the player's input speed and accuracy: 
-  Correct and rapid answers trigger a Critical Damage Multiplier (2.0x). 
-  Correct but slow answers will result in normal damage. 
-  Incorrect but rapid answers result in a Damage Penalty (0.5x). 
-  Incorrect and slow answers result in action nullification (Miss).

 

**H.** Automatic Quest Generation Algorithm. The scope of the proposed project includes Automatic Content Generation. The system features a quest engine that scans the details of the player's current location (Enemies and Items) to generate infinite, location-aware objectives (Hunting or Gathering). The user interacts with this module by moving their character towards "Quest Giver" NPCs using directional keys, clicking on the NPC to interact, and clicking to accept automatically generated side missions. 

**I.** Peer-to-Peer (P2P) Multiplayer Framework The scope of the proposed project incorporates Networked Cooperative Gameplay using direct connections with text-based Room Codes. It allows drop-in combat where a joining player's party merges with the host's party dynamically. The user interacts with this module by interacting with an NPC and clicking the ” Host Room ” button to generate a "Room Code" for hosting a game, or typing a friend's code after clicking the "Join Room" button from the same NPC to join their game. 

**J.** User Interface (UI) The scope of the proposed project encompasses visual screens and menus, including a Standard Menu System for Party Status and Inventory, System Options, and an Integrated Quest Journal that automatically updates with active missions. The user interacts with this module by pressing a designated menu button (e.g., 'Esc') or clicking a menu icon to open screens, using the mouse or touch input to view detailed party statistics (HP/MP/EXP), equip items, and scroll through the "Quest Journal" to track mission progress. 

**K.** Save System The scope of the proposed project incorporates game saving and progress tracking. Game data is saved and stored as local files in the user's device. It includes 20 manual save slots and an Autosave feature. The user interacts with this module by navigating to the "Save" screen via the main menu, clicking to select one of 20 manual save slots to record progress, or by walking their character through map exits to trigger automatic checkpoints.

 

**L.** Level-Based Progression Architecture The user interacts with this module by participating in combat or completing quests. The scope of the proposed project defines Player Progression phases. Successful combat and exploration yield the following progression rewards: 

**L.1** Experience Points (EXP): Accumulating EXP increases the character's level. The minimum obtainable EXP from a single low-level source is 10 points (Level 1 Slime), while the maximum possible gain from an endgame boss is capped at 99,999 points. 

**L.2** Gold (Currency): Acquired via enemy defeats and quest completion. The minimum gold drop from a basic enemy is 5 G, while the maximum reward from a high-tier boss or elite quest is 50,000 

**G.** This currency is used to buy new equipment and items from merchants. 

**L.3** Story Milestones: Updates the "Story Progress", allowing the game to unlock higher-level maps. 

**M.** Mobile Detection System and Virtual Numeric Keypad The scope of the proposed project includes a mobile-friendly input system. The game automatically detects if the user is on a mobile device and displays a Virtual Numeric Keypad on the screen. The user interacts with this module on supported mobile devices by physically tapping the on-screen number buttons and the "Submit" button to enter math answers during combat. 

**N.** Game Assets and Entities The scope of the proposed project includes a mobile-friendly input system. The game automatically detects if the user is on a mobile device and displays a Virtual Numeric Keypad on the screen. The user interacts with this module on supported mobile devices by physically tapping the on-screen number buttons and the "Submit" button to enter math answers during combat.

 

**N.1** Character Roster This includes the main characters that the player will talk to, fight alongside, or receive quests from to move the story forward 
-  Bron 
-  Martha 
-  Lily 
-  Kael 
-  Elara 
-  Garrick 
-  Sylas 
-  Isolde 
-  Thorne 
-  Lyra 
-  Fenrin 
-  Elder Tobias 
-  Merchant Oryn 
-  Receptionist Mila 
-  Bard Jareth 
-  Captain Valerius 
-  Professor Haze 
-  Innkeeper Gorm 
-  Blacksmith Rurik 
-  Widow Claire 
-  Farmer Ben 
-  Alchemist Vanya 
-  Librarian Estel 
-  Guard Captain Aris 
-  Fisherman Old Tom 
-  Street Urchin Pip 
-  Nobleman Caelus 
-  Priestess Anara 
-  Hunter Kaelen 
-  The Numeromancer

 

**N.2** Background NPC ’ s This includes the generic townspeople and villagers used to fill up the maps to make the game world feel alive and busy. 
-  Townsman 1-5 (Male) 
-  Townswoman 1-5 (Female) 
-  Playing Boy 1-2 
-  Playing Girl 1-2 
-  Market Shopper 1-3 
-  Tavern Patron 1-4 
-  Castle Guard 1-4 
-  Farmhand 1-2 
-  Stable Boy 
-  Washerwoman 
-  Street Sweeper 
-  Beggar 1-2 
-  Strolling Couple (Man/Woman) 
-  Academy Student 1-4 
-  Visiting Merchant 
-  Visiting Noble 
-  Lost Tourist 
-  Drunkard 
-  Gossiping Lady 1-2 
-  Running Messenger 
-  Sleeping Guard 
-  Fishing Boy 
-  Old Cat Lady 
-  Street Performer 
-  Watching Crowd Member 

**N.3** Enemies: This includes the enemies that the user may encounter during their playthrough.

 

**N.3.1** Plains & Forest Biome: 
-  Slime 
-  Rat 
-  Bat 
-  Spider 
-  Hornet 
-  Wolf 
-  Bear 
-  Treant 
-  Goblin 
-  Goblin Archer 
-  Goblin Shaman 
-  Orc, Bandit 
-  Bandit Leader 
-  Crow 
-  Snake 
-  Fairy 
-  Mandrake 
-  Wild Boar 
-  Forest Golem 

**N.3.2** Desert Biome: 
-  Sand Slime 
-  Scorpion 
-  Giant Scorpion 
-  Cactus 
-  Sand Worm 
-  Mummy 
-  Skeleton Warrior 
-  Skeleton Mage 
-  Desert Wolf 
-  Lamia, Basilisk 
-  Gargoyle

 
-  Sand Golem 
-  Vulture, Sphinx 
-  Desert Rogue 
-  Ant Lion 
-  Dust Spirit 
-  Ancient Scarab 
-  Pharaoh ’ s Guard 

**N.3.3** Tundra & Frost Biome 
-  Ice Slime 
-  Snow Wolf 
-  Polar Bear 
-  Ice Bat 
-  Snow Spirit 
-  Yeti 
-  Ice Golem 
-  Crystal Spider 
-  Frost Giant 
-  White Tiger 
-  Corrupted Penguin 
-  Ice Drake 
-  Frozen Knight 
-  Winter Wisp 
-  Wendigo 
-  Frost Mage 
-  Glacial Turtle 
-  Snow Harpy 
-  Ice Elemental 
-  Fenrir 

**N.3.4** Volcano & Fire Biome 
-  Magma Slime 
-  Fire Spirit

 
-  Imp 
-  Demon 
-  Succubus 
-  Cerberus 
-  Lava Golem 
-  Fire Bat 
-  Salamander 
-  Dragon Hatchling 
-  Red Dragon 
-  Efreet 
-  Phoenix 
-  Iron Giant 
-  Dark Knight 
-  Cultist 
-  Fire Elemental 
-  Minotaur 
-  Chimera 
-  Demon Lord 

**N.3.5** General & Dungeon 
-  Ghost 
-  Zombie 
-  Vampire 
-  Vampire Bat 
-  Mimic 
-  Shadow 
-  Will-o'-the-Wisp 
-  Animated Armor 
-  Flying Sword 
-  Magic Pot 
-  Gazer 
-  Ogre 
-  Troll

 
-  Warlock 
-  Necromancer 
-  Reaper 
-  Chaos Cloud 
-  Number Eater 
-  Equation Spirit 
-  The Unknown 

**N.4** Items This includes the items that the user may receive can receive from either buying from shops, completing quests or being dropped as loot from enemies during their playthrough . 

**N.4.1** Consumable Items (Recovery & Utility) 
-  Potion 
-  Hi-Potion 
-  Full Potion 
-  Magic Water 
-  Hi-Magic Water 
-  Elixir, Antidote 
-  Eye Drops 
-  Echo Herb 
-  Stimulant 
-  Potent Stimulant 
-  Panacea 
-  Dispel Herb 
-  Escape Rope 
-  Repel Spray 

**N.4.2** Stat Boosters (Permanent Upgrades) 
-  HP Up 
-  MP Up 
-  Strength Seed

 
-  Defense Seed 
-  Magic Seed 
-  Agility Seed 
-  Luck Seed 
-  Skill Book 

**N.4.3** Monster Loot & Drops 

**N.4.1** Plains/Forest 
-  Green Gel 
-  Rat Tail 
-  Bat Wing 
-  Sticky Web 
-  Insect Wing 
-  Wolf Pelt 
-  Bear Claw 
-  Living Branch 
-  Goblin Cloth 
-  Shaman Bead 
-  Orc Tusk 
-  Stolen Coin Purse 
-  Shiny Feather 
-  Snake Skin 
-  Fairy Dust 
-  Mandrake Root 
-  Boar Meat 
-  Ancient Bark 

**N.4.2** Desert 
-  Yellow Gel 
-  Scorpion Stinger 
-  Cactus Flower 
-  Sand Essence 
-  Old Bandage 
-  Bone Fragment

 
-  Skull 
-  Dry Fur 
-  Snake Scale 
-  Petrified Eye 
-  Stone Wing 
-  Sandstone Block 
-  Vulture Beak 
-  Riddle Tablet 
-  Scarab Shell 
-  Golden Fragment 

**N.4.3** Tundra 
-  Blue Gel 
-  White Fur 
-  Thick Hide 
-  Ice Crystal 
-  Snowflake Core 
-  Yeti Horn 
-  Permafrost Shard 
-  Crystal Leg 
-  Frost Metal 
-  Corrupted Feather 
-  Drake Scale 
-  Cold Wisp 
-  Frozen Heart 
-  Ice Turtle Shell 
-  Harpy Feather 
-  Wolf Fang 

**N.4.4** Volcano 
-  Red Gel 
-  Ember 
-  Imp Wing

 
-  Demon Horn 
-  Succubus Cloth 
-  Hellhound Fang 
-  Obsidian Shard 
-  Fire Gland 
-  Dragon Tooth 
-  Red Scale 
-  Djinn Lamp 
-  Phoenix Ash 
-  Iron Scraps 
-  Dark Armor Piece 
-  Forbidden Page 
-  Chimera Tail 
-  Infernal Core. 

**N.4.5** General 
-  Ectoplasm 
-  Rotten Flesh 
-  Vampire Fang 
-  Unknown Fluid 
-  Spirit Dust 
-  Haunted Metal 
-  Ceramic Shard 
-  Evil Eye 
-  Ogre Club 
-  Magic Powder 
-  Tattered Robe 
-  Chaos Mote 
-  Arithmetic Essence 
-  Void Fragment

 

**N.5** Class Roster: 
-  Swordsman 
-  Sorcerer 
-  Priest 
-  Knight 
-  Martial Artist 
-  Magic Swordsman 
-  Hunter 
-  Bandit 

**N.6** Weapons 

**N.6.1** Swordsman (Swords) 
-  Long Sword 
-  Woodcutter's Blade 
-  Wolf Fang Sword 
-  Forest Cutter 
-  Bandit's Edge 
-  Verdant Blade 
-  Sand Scimitar 
-  Scorpion Tail 
-  Dune Blade 
-  Sun-Scorched Sword 
-  Ancient Khopesh 
-  Ice Brand 
-  Glacial Edge 
-  Frostbite Sword 
-  Crystal Saber 
-  Blizzard Blade 
-  Magma Blade 
-  Dragon Bone Sword 
-  Infernal Edge 
-  Flame Tongue 
-  Phoenix Feather Sword

 

**N.6.2** Sorcerer (Staves) 
-  Oak Staff 
-  Briar Rod 
-  Druid's Staff 
-  Faerie Wand 
-  Root Staff 
-  Nature's Call 
-  Sandstone Rod 
-  Mirage Staff 
-  Cobra Head Staff 
-  Sun Rod 
-  Sphinx Cane 
-  Icicle Rod 
-  Snowflake Staff 
-  Hailstorm Wand 
-  Permafrost Cane 
-  Frozen Core Staff 
-  Ember Rod 
-  Ash Staff 
-  Dragon Breath Wand 
-  Core Magma Staff 
-  Hellfire Rod 

**N.6.3** Priest (Maces) 
-  Wooden Mace 
-  Oak Club 
-  Spirit Mace 
-  Blessed Branch 
-  Mossy Hammer 
-  Guardian's Cudgel 
-  Golden Scepter 
-  Sandstone Hammer 
-  Sun Disc Mace

 
-  Tomb Guardian Club 
-  Sacred Ankh 
-  Crystal Mace 
-  Hailstone Hammer 
-  Frozen Scepter 
-  Polar Club 
-  Divine Ice Mace 
-  Obsidian Mace 
-  Lava Rock Hammer 
-  Cleansing Fire Club 
-  Forge Master's Hammer 
-  Phoenix Down Mace 

**N.6.4** Knight (Spears) 
-  Short Spear 
-  Hunter's Spear 
-  Boar Tusk Lance 
-  Forest Guard Pike 
-  Wooden Pike 
-  Leaf-Blade Spear 
-  Scorpion Stinger 
-  Desert Pike 
-  Bronze Lance 
-  Sandpiercer 
-  Pharaoh's Guard 
-  Ice Shard Lance 
-  Glacier Pike 
-  Tundra Harpoon 
-  Frost Wyrm Spear 
-  Frozen Needle 
-  Magma Pike 
-  Dragon Scale Lance 
-  Red Steel Spear

 
-  Obsidian Lance 
-  Hellfire Harpoon 

**N.6.5** Martial Artist (Claws) 
-  Leather Gloves 
-  Bear Claws 
-  Wolf Paws 
-  Sharp Thorns 
-  Tree Bark Knuckles 
-  Wild Beast Fists 
-  Scorpion Pincers 
-  Sandstone Gauntlets 
-  Cactus Spines 
-  Mummy Wraps 
-  Golden Knuckles 
-  Ice Picks 
-  Yeti Fists 
-  Frostbite Gloves 
-  Crystal Talons 
-  Polar Paws 
-  Salamander Claws 
-  Dragon Fangs 
-  Magma Fists 
-  Burning Knuckles 
-  Demon Hands 

**N.6.6** Magic Swordsman (Enchanted Blades) 
-  Rapier 
-  Wind Blade 
-  Leaf Cutter 
-  Elven Rapier 
-  Swift Blade 
-  Whisper Edge

 
-  Mirage Rapier 
-  Heatwave Saber 
-  Dust Devil Blade 
-  Golden Epee 
-  Sun-Strike Sword 
-  Chill Spike 
-  Frozen Needle 
-  Aurora Blade 
-  Ice Queen's Rapier 
-  Zero Kelvin, Searing 
-  Saber 
-  Molten Rapier 
-  Blaze Edge 
-  Phoenix Tail 
-  Volcanic Spike 

**N.6.7** Hunter (Bows) 
-  Short Bow 
-  Oak Bow 
-  Hunter's Bow 
-  Ranger's Crossbow 
-  Vine Bow 
-  Elven Bow 
-  Bone Bow 
-  Sandstone Crossbow 
-  Scorpion Recurve 
-  Desert Wind Bow 
-  Golden Arrow 
-  Ice Crystal Bow 
-  Frostbite Crossbow 
-  Mammoth Ivory Bow 
-  Blizzard String 
-  Glacial Shot

 
-  Ash Wood Bow 
-  Flame String 
-  Magma Rock Crossbow 
-  Dragon Bone Bow 
-  Phoenix Fire Bow 

**N.6.8** Bandit (Daggers) 
-  Knife 
-  Rusty Shiv 
-  Hunter's Knife 
-  Poison Tip 
-  Thief's Shank 
-  Forest Tooth 
-  Curved Dagger 
-  Sand Shiv 
-  Scorpion Barb 
-  Tomb Blade 
-  Golden Dagger 
-  Icicle Shiv 
-  Frozen Dagger 
-  Shard of Glass 
-  Cold Steel Knife 
-  Frostbite Dirk 
-  Obsidian Knife 
-  Heated Dagger 
-  Ember Shiv 
-  Dragon Claw 
-  Hell's Tooth

 

**N.7** Skills 

**N.7.1** Swordsman 
-  Strong Attack 
-  Slash 
-  Double Slash 
-  Wide Swing 
-  Armor Break 
-  Blade Bash 
-  Focus 
-  Parry 
-  Sonic Wave 
-  Wind Slash 
-  Power Break 
-  Mind Break 
-  Berserk Stance 
-  Cross Cut 
-  Omnislash 

**N.7.2** Sorcerer 
-  Fire 
-  Fire II 
-  Fire III 
-  Ice, Ice II 
-  Ice III 
-  Thunder 
-  Thunder II 
-  Thunder III 
-  Flare 
-  Freeze 
-  Shock 
-  Magic Drain 
-  Concentrate 
-  Meteor Swarm

 

**N.7.3** Priest 
-  Heal 
-  Heal II 
-  Heal III 
-  Party Heal 
-  Cure Poison 
-  Cure Blind 
-  Cure Silence 
-  Panacea 
-  Raise 
-  Holy Light 
-  Protect, Shell 
-  Regenerate 
-  Purify 
-  Divine Intervention 

**N.7.4** Knight 
-  Provoke 
-  Shield Bash 
-  Cover, Iron Defense 
-  Guard Ally 
-  Shield Wall 
-  Fortify 
-  Sentinel 
-  Justice Strike 
-  Heavy Charge 
-  Taunt 
-  Unbreakable Will 
-  Phalanx 
-  Retribution 
-  Castle of Stone 

**N.7.5** Martial Artist

 
-  Punch 
-  Kick 
-  Triple Kick 
-  Roundhouse 
-  Chakra 
-  Meditate 
-  Pressure Point 
-  Earth Splitter 
-  Gale Palm 
-  Spirit Wave 
-  Counter 
-  Leg Sweep 
-  Fists of Fury 
-  Chi Blast 
-  Seven Star Strike 

**N.7.6** Magic Swordsman 
-  Fire Blade 
-  Ice Blade 
-  Thunder Blade 
-  Wind Blade 
-  Drain Blade 
-  Aspir Blade 
-  Magic Barrier 
-  Enchant Weapon 
-  Dispel Strike 
-  Elemental Burst 
-  Arcane Slash 
-  Spell Shield 
-  Mystic Thrust 
-  Teleport Strike 
-  Rune Breaker

 

**N.7.7** Hunter 
-  Aim 
-  Power Shot 
-  Rapid Fire 
-  Poison Arrow 
-  Sleep Arrow 
-  Blind Arrow 
-  Silence Arrow 
-  Arrow Rain 
-  Eagle Eye 
-  Beast Slayer 
-  Piercing Shot 
-  Camouflage 
-  Trap Set 
-  Snipe 
-  Hail of Arrows. 

**N.7.8** Bandit 
-  Steal 
-  Mug 
-  Sneak Attack 
-  Poison Edge 
-  Sand Throw 
-  Smoke Bomb 
-  Backstab 
-  Sprint 
-  Gold Snatch 
-  Venom Strike 
-  Shadow Step 
-  Dirty Trick 
-  Twin Daggers 
-  Lucky Strike 
-  Assassinate

 

**N.8** Status Effects 

**N.8.1** Negative States (Debuffs) 
-  Knockout 
-  Poison 
-  Blind 
-  Silence 
-  Confusion 
-  Sleep 
-  Paralysis 
-  Stun 
-  Bleed 
-  Burn 
-  Freeze 
-  Slow 
-  Curse 
-  Weakness 
-  Fear 

**N.8.2** Positive States (Buffs) 
-  Regenerate 
-  Haste 
-  Protect 
-  Shell 
-  Focus 
-  Magic Barrier 
-  Attack Up 
-  Defense Up 
-  Magic Up 
-  Agility Up 
-  Evasion Up 
-  Immortal 
-  Auto-Life 
-  Reflect

 
-  Counter Stance 

**N.9** Armor & Accessory 

**N.9.1** Shields Equippable only by Knights, Swordsmen, Priests 
-  Small Shield 
-  Buckler 
-  Round Shield 
-  Kite Shield 
-  Iron Shield 
-  Steel Shield 
-  Mythril Shield 
-  Gold Shield 
-  Wooden Lid 
-  Hunter's Buckler 
-  Bronze Shield 
-  Scale Guard 
-  Shell Buckler 
-  Ice Shield 
-  Crystal Guard 
-  Frost Shield 
-  Dragon Shield 
-  Flame Guard 
-  Obsidian Shield 
-  Aegis 

**N.9.2** Headgear 
-  Leather Cap 
-  Iron Helmet 
-  Steel Helmet 
-  Mythril Helm 
-  Full Helm 
-  Viking Helm

 
-  Dragon Helm 
-  Genji Helm 
-  Leather Helm 
-  Feathered Hat 
-  Magician's Hat 
-  Circlet, Ribbon 
-  Bandana, Turban 
-  Silk Hood 
-  Fur Hood 
-  Ice Crown 
-  Salamander Coif 
-  Royal Crown 

**N.9.3** Body Armor 
-  Cloth Tunic 
-  Leather Armor 
-  Iron Armor 
-  Steel Armor 
-  Mythril Armor 
-  Plate Mail 
-  Heavy Mail 
-  Scale Mail 
-  Glacial Mail 
-  Flame Mail 
-  Dragon Armor 
-  Traveler's Tunic 
-  Hard Leather 
-  Hunter's Vest 
-  Ninja Suit 
-  Cotton Robe 
-  Silk Robe 
-  Sorcerer's Robe 
-  Winter Robe

 
-  Lava Robe 
-  Sage's Robe 

**N.9.4** Accessories 
-  Ring of Protection 
-  Ring of Power 
-  Ring of Magic 
-  Ring of Speed 
-  Ring of Life 
-  Poison Charm 
-  Silence Amulet 
-  Blindness Glasses 
-  Paralysis Talisman 
-  Sleep Earring 
-  Fire Ring 
-  Ice Ring 
-  Thunder Ring 
-  Earth Ring 
-  Gold Ring 
-  Lucky Coin 
-  Warrior's Badge 
-  Scholar's Specs 
-  Knight's Crest 
-  Sniper's Eye

### 1.3.2 Limitations

 

**A.** Mathematical Scope The system does not currently support advanced algebra, calculus, or non-integer results (fractions/decimals). All answers are auto-generated to be integers to maintain combat flow. 

**B.** Tactile Input Disparity While the inclusion of a Virtual Numeric Keypad enables mobile playability, the lack of tactile feedback on touchscreens may result in reduced input velocity compared to physical

 keyboards. Consequently, users on mobile devices may experience a slight disadvantage in high-level "Speed Math" calculations where millisecond reaction times are critical. 

**C.** Input Method The input system utilizes the standard number row or numpad of a physical keyboard. 

**D.** Asset Fidelity The project utilizes standard 2D pixel art assets and does not focus on high-fidelity 3D rendering or physics simulations. 

**E.** Peer-to-Peer Latency Sensitivity The multiplayer feature relies on the stability of the host ’ s internet connection. As the system utilizes a direct P2P handshake, high latency or packet loss on the host side may result in desynchronization of the Math Timer for connected clients. 

**F.** Volatile Session Architecture The multiplayer system is stateless (no central dedicated server). If the host application is terminated, the game session dissolves immediately for all connected clients; state recovery for guest clients is not supported in this version.

# 3.0 Technical Background

## 3.1 Development

### 3.1.1 Hardware

 

**A.** Personal Computers and Laptops The proponents will primarily use personal computers (PCs), desktop computers, and laptops for documentation, system design, testing, and development of the proposed project.

### 3.1.2 Software

 

**A.** Frontend 

**A.1** RPG Maker MZ RPG Maker MZ will be used in the core application development to construct the visual environment, manage the database of enemies and items, and script game events. We utilize this engine because its built-in architecture provides a stable framework for standard RPG mechanics (like inventory and movement) while allowing for the injection of custom JavaScript plugins to create the unique "Math Battle System. 

**A.2** HTML5 / WebGL HTML5 and WebGL will be used in the web-based deployment build of the project. We utilize these technologies to enable hardware- accelerated 2D graphics rendering directly within client web browsers, ensuring the game runs smoothly on school computers and mobile devices without requiring the user to install native software. 

**A.3** Cascading Style Sheets (CSS) CSS will be used as the web container (index.html) that wraps the game engine. We utilize CSS to handle the responsive scaling of the game canvas across different screen sizes and to precisely position the "Virtual Keypad" overlay, ensuring the interface remains usable on touch-screen devices.

 

**B.** Backend 

**B.1** JavaScript (ES6) JavaScript will serve as the core programming language for developing custom plugins. It will be used in the backend development phase to program the logic of the "Math Battle System," "Adaptive Difficulty Algorithm," and "P2P Multiplayer Framework" because it is the native scripting language of RPG Maker MZ, allowing the proponents to override default engine behaviors without external dependencies. 

**B.2** Visual Studio Code (VS Code) Visual Studio Code will be the primary Integrated Development Environment (IDE) used for writing, debugging, and managing the JavaScript codebase. It will be utilized in the coding phase because its robust extension ecosystem (such as ESLint and Git integration) streamlines the management of complex plugin files and ensures code quality during the development process. 

**B.3** Node.js Node.js will be utilized during the development phase to run local server environments. It will be used to simulate server-side operations for testing the P2P multiplayer handshake and simulating network latency conditions, ensuring the connection logic is robust before deploying to the public web. 

**B.4** PeerJS PeerJS will be utilized as the WebRTC wrapper library to implement the peer-to-peer networking architecture. It will be used in the networking module to manage the generation of unique "Room Codes" and facilitate real-time data exchange between the host and connected clients because it simplifies the complex process of establishing direct connections without requiring a centralized backend server.

 

**C.** Multimedia and Asset Development Tools 

**C.1** GIMP (GNU Image Manipulation Program) GIMP will be utilized as the primary raster graphics editor for the manipulation of game assets. It will be used in the asset creation phase to perform "Hue Shifting" on default enemy sprites because its advanced color manipulation tools allow for the efficient creation of biome-specific enemy variants (e.g., Sand Slime, Magma Slime) from a single base asset. 

**C.2** Canva Canva will be utilized as the primary graphic design tool for creating the project's materials. It will be used in the design phase to create the official game logo. 

**D.** Deployment and Runtime Platform 

**D.1** NW.js (Native Executable Wrapper) NW.js will serve as the core runtime environment for the PC desktop deployment. It will be used to encapsulate the HTML5/JavaScript game engine into a standalone, native executable file (.exe) for Windows because this wrapper gives the application direct access to the local file system for save data persistence, ensuring it runs offline with native performance. 

**D.2** Modern Browsers Modern web browsers, such as Google Chrome and Microsoft Edge, serve as the runtime environment for the web-based deployment. The system uses these platforms during the testing phase to evaluate WebGL rendering performance. This testing ensures the responsiveness of the virtual keypad overlay for the users. These applications represent the standard environment for the target audience accessing the system through the web. 

**D.3** GitHub

 GitHub serves as the central cloud-based repository for the project source code. The platform manages version control and facilitates collaboration among the development team members. It stores all historical iterations of the game files to prevent data loss. . 

**D.4** Git functions as the distributed version control system for local development. The developers use this tool to track changes in the source code during the implementation phase. It allows the team to push updated code from local machines to the GitHub repository. 

**D.5** Vercel Vercel operates as the deployment and hosting platform for the web-based application. The system connects to the GitHub repository to automate the build process of the game. It provides a secure HTTPS environment which is a requirement for the WebRTC and PeerJS handshake.

### 3.1.3 Peopleware

 

**A.** The Proponents The proponents consisted of a project manager, a lead programmer, UI/UX designers, tester and graphic designers who planned, programmed, and designed the system, respectively, according to the standards agreed upon for the project. 

**B.** Capstone Adviser Mr. Jan Nichole 

**B.** Apostol provided expert guidance, valuable insights, clarifications, and recommendations to improve the project. They guided the proponents through the technicalities and documentation, provided necessary revisions, and ensured the production of a high-quality, properly formatted system.

### 3.1.4 Network

 

**A.** Local Area Network (LAN) & Cloud Staging During the development lifecycle, the proponents will conduct multiplayer testing using two distinct network configurations. First, the peer-to- peer handshake and data synchronization will be validated using multiple personal computers connected to the same local internet connection (LAN/Same Wi-Fi) to ensure low-latency performance. Second, the system will be tested with computers connected to different internet networks (WAN) to simulate real-world remote play conditions and verify the stability of the "Room Code" connection over the public internet.

## 3.2 Implementation

### 3.2.1 Hardware

 

**A.** Personal Computer or Laptop Users will be required to have a personal computer (PC), desktop, or laptop to install and use Chronicles of Arithmos. The minimum hardware requirements, based on the tested configuration, are: 
-  Processor: Intel Core i3-3220 CPU @ 3.30GHz or equivalent. 
-  Memory: 8.0 GB RAM. 
-  Graphics: Intel HD Graphics (32 MB VRAM) or better. 
-  Storage: At least 2 GB of available space (120GB SSD recommended). 
-  System Type: 64-bit operating system, x64-based processor.

 

**B.** Mobile Device (Web Access) For users accessing the application via the web browser deployment. The minimum requirements based on tested configurations are: 
-  Processor: MediaTek Dimensity 700 (Octa-core CPU up to 2.2GHz). 
-  Memory: 4 GB RAM (supports LPDDR4X). 
-  Graphics: Mali-G57 MC2 GPU. 
-  Display: 6.5" FHD+ DotDisplay (90Hz refresh rate recommended for smooth animations). 
-  Storage: 128 GB UFS 2.2 (Minimum 1GB free for browser cache). 
-  OS: Android 11 (MIUI 12) or higher.

### 3.2.2 Software

 

**A.** Operating System (OS) The minimum operating system requirement will be Windows 10 (64-bit). This specific OS environment is needed by the user because the NW.js runtime wrapper, which powers the game's executable, relies on modern 64-bit architecture and libraries that are not supported in older versions like Windows 7. For mobile users, Android 10 or iOS 14 will be required because the game's web technologies (WebGL 2.0) depend on updated kernel support found in these mobile operating systems. 

**B.** Browser Users will be required to use a web browser to access the web-deployed version via GitHub Pages. The supported web browsers will include Google Chrome, Mozilla Firefox, Microsoft Edge, and Safari. T hese browsers are needed by the user because the game's "Virtual Keypad" overlay and P2P multiplayer handshake utilize HTML5 and WebRTC standards that are only reliably implemented in these modern, Chromium-based or WebKit-based browsers.

### 3.2.3 Peopleware

 

**A.** Students (Primary End-Users) Students (Grades 4-6) will serve as the primary operators of the system. They will engage directly with the Math Battle System to solve arithmetic equations, explore the game world, and progress through the narrative. Their interaction will focus on improving calculation speed and accuracy to defeat enemies and clear procedural quests. 

**B.** Educators and Guardians (Secondary Users) Teachers and parents will act as secondary users who utilize the application as a supplementary educational tool. Educators will use the software to reinforce classroom topics (PEMDAS) or assign specific "Training Simulation" drills. Guardians will utilize the game to support home-based learning, potentially joining via the P2P Multiplayer mode to assist the primary learner in difficult combat encounters. 

**C.** General Gamers (Tertiary Users) RPG enthusiasts and casual gamers will interact with the system for entertainment purposes. These users will focus on mastering the "Performance- Based Efficacy" mechanics to achieve high-efficiency combat ratings and complete "Omega Tier" endgame challenges, interacting with the system primarily to test cognitive reaction speeds and strategic planning.

### 3.2.4 Network

 

**A.** Internet Connection The system will require a stable internet connection to function properly, particularly for the P2P multiplayer features and initial web resource loading. A minimum of 1 Mbps internet speed is needed for basic gameplay connectivity, and 5 Mbps or higher is required for optimal performance in data synchronization and asset loading to prevent desynchronization during multiplayer sessions.

# 4.0 Methodology

## 4.1 Prototyping Model

 According to GeeksforGeeks [ 4 ], the Prototyping Model is a development cycle used when specific requirements are not fully defined at the start. In this model, an early version of the software is created to gather feedback and refine the logic before building the final product. This approach allows for the testing of math mechanics early in the project life cycle. This methodology ensures that the game balance and educational goals are validated through testing instead of committing to a single code structure immediately.

*Figure No. :*

Prototyping Model The proponents have selected the Prototyping Model for this study to support the development of the proposed title that requires input to balance fun and learning. This model facilitates the creation of a product that matches the learning habits of Grade 4 to 6 students while keeping the math-to-gameplay ratio steady through several rounds of adjustment. The Prototyping Model follows a cycle consisting of the following stages:

### 4.1.1 Requirements

 In this phase, the proponents will define the project objectives, scope, and specific mathematical requirements. During this stage, information relevant to the game, specifically the necessary RPG mechanics, will be gathered and analyzed. This phase identifies the core functions and educational problems to solve, establishing a foundation for development.

### 4.1.2 Quick Design

 The second phase involves a preliminary design where the proponents will create system diagrams, such as flowcharts, to serve as a guide. These diagrams illustrate how a student will navigate the game and how math questions are triggered during a battle. This stage focuses on creating interface designs and storyboards for the game biomes to show how the system will look and how gameplay information flows .

### 4.1.3 Build Prototype

 The proponents will build an initial prototype based on the quick design using RPG Maker MZ and JavaScript. This stage involves creating a working model that includes the core Math Engine and the Peer-to-Peer (P2P) multiplayer connection. This version allows for the demonstration of the game's logic and the identification of technical issues before full development begins.

### 4.1.4 User Evaluation

 During this phase, the proponents will present the initial prototype to the Capstone Adviser, Mr. Jan Nichole 

**B.** Apostol, to evaluate the core mechanics and game logic. This internal review focuses on identifying gaps in the Math Engine and the Peer-to-Peer (P2P) connection. Feedback gathered during this stage will determine if the design aligns with the project objectives or if adjustments are necessary before proceeding with further development.

### 4.1.5 Refining Prototype

 Following the evaluation, the proponents will adjust the system based on the feedback and suggestions received. This stage involves making technical adjustments to the difficulty scaling and the user interface to ensure the software functions as planned. These adjustments will continue until the prototype is stable and matches the requirements defined in the earlier phases of the project.

### 4.1.6 Implement Product and Maintain

 In this phase, the system undergoes final testing after development is completed. Once the software is verified, the application will be deployed for user access across various platforms. The proponents will also perform regular maintenance to address technical issues and ensure the long-term stability of the game within an educational setting.

## 4.2 Requirements Specification

### 4.2.1 Operational Feasibility

 

**A.** Fishbone Diagram

 

**B.** Functional Decomposition Diagram

### 4.2.2 Technical Feasibility

 This section evaluates the hardware and software tools selected for the proposed title to ensure the project is technically achievable. The proponents focus on ensuring that all components work together without conflict and that each tool directly supports the goal of teaching arithmetic to students.

#### 4.2.2.1 Compatibility Checking

 

**A.** Hardware Compatibility The proponents will develop the game using RPG Maker MZ, which is compatible with standard personal computers having at least 8GB of RAM. Since the game is deployed via HTML5, it will run on any device with a modern web browser, including the tablets and computers typically found in school laboratories. 

**B.** Software Compatibility The proposed title system uses JavaScript to extend the game engine's features, ensuring a stable connection between the math logic and the RPG mechanics. The

 PeerJS library is utilized for multiplayer features because it is compatible with web- standard protocols, allowing students to connect directly without needing a complex central server.

#### 4.2.2.2 Relevance of the Technology

 The selection of these technologies is directly linked to the functional requirements of the proposed title and the educational goals of the study. Using JavaScript is essential because it provides the proponents with the flexibility to develop the Content-Aware Timer and the custom difficulty algorithm, which are necessary for adjusting math problems to the student's skill level. Furthermore, the integration of PeerJS is relevant to the implementation of the "Battle with Friends" mode, as it allows for direct Peer-to-Peer interaction. This facilitates social learning and peer engagement among Grade 4 to 6 students without the need for complex server management. By utilizing these specific tools, the proponents ensure that the game remains a tool for improving arithmetic skills while maintaining a balance between educational content and interactive gameplay.

### 4.2.3 Schedule Feasibility
**A.** Gantt Chart
**Table #1**
#### November 2025
* **Capstone Orientation:** Week 1
* **Grouping of Capstone Members:** Week 1
* **Planning and Brainstorming:** Week 2, Week 3, Week 4
November 2025 Gantt Chart Activities Week 1 Week 2 Week 3 Week 4 1. Capstone Orientation 2. Grouping of Capstone Members 3. P lanning and Brainstorming

**Table #2**
#### December 2025
* **Planning and Brainstorming:** Week 1, Week 2, Week 3, Week 4
* **Early Game Demo Development:** Week 2, Week 3, Week 4
December 2025 Gantt Chart Activities Week 1 Week 2 Week 3 Week 4 1. P lanning and Brainstorming 2. Early Game Demo Development

**Table #3**
#### January 2026
* **Early Game Demo Development:** Week 1, Week 2
* **Preparation for Title Defense:** Week 1, Week 2, Week 3
* **Title Defense:** Week 3
* **Capstone Adviser Consultation:** Week 3, Week 4
* **Documentation (Chapter 1):** Week 3, Week 4
January 2026 Gantt Chart Activities Week 1 Week 2 Week 3 Week 4 1. Early Game Demo Development 2. Preparation for Title Defense 3. Title Defense 4. Capstone Adviser Consultation 5. Documentation (Chapter 1)

**Table #4**
#### February 2026
* **Documentation (Chapter 2):** Week 1
* **Documentation (Chapter 3):** Week 2
* **Capstone Adviser Consultations:** Week 2, Week 3
* **Documentation (Chapter 4):** Week 2
February 2026 Gantt Chart Activities Week 1 Week 2 Week 3 Week 4 1. Documentation (Chapter 2) 2. Documentation (Chapter 3) 3. Capstone Adviser Consultations 4. Documentation (Chapter 4)


### 4.2.4 Economic Feasibility

#### 4.2.4.1 Cost and Benefit Analysis

 The cost and benefit analysis provides a breakdown of the materials required for development and the specific value each item brings to the study. The proponents have categorized these costs into fixed development expenses and variable infrastructure costs.

 Category Item Cost Benefits Hardware Proponents' Laptops ₱ 0.00 Used for coding, game design, and testing the system. Software RPG Maker MZ (2 Licenses) ₱ 4,600.00 Provides the engine for the Active Time Battle (ATB) and Math Engine logic. Hosting Hostinger Domain & Web Hosting (5 years) ₱ 12,108.00 Enables cross-platform access via ".site" domain for students at home. TOTAL Investment Required ₱ 16,708.00

#### 4.2.4.2 Cost Recovery Scheme

 The total development investment of ₱16,708.00 will be personally funded by the proponents as part of the academic requirements for the Bachelor of Science in Information Technology program. Because the proposed title is developed under an educational context and not for commercial distribution, the proponents do not plan to recover the monetary cost through direct sales or subscription fees. Instead, the return on investment is realized through the completion of the capstone requirement, the acquisition of practical development experience, and the academic credentials earned upon the successful defense of the project. The application will be distributed at no cost to students and teachers to maximize its reach and its contribution to local arithmetic literacy. If any school chooses to use the system as a supplementary classroom tool, the hosting infrastructure funded during development will continue to support access without additional expense during the five-year hosting period.

### 4.2.5 Requirements Modeling

#### 4.2.5.1 Object Modelling

 

**A.** Use Case Diagram From Capstone Manual: ▪ Input, ▪ Process, ▪ Output, ▪ Performance, ▪ Control ▪ Either of the following two (2) or combined, whichever are applicable: o Data and Process Modeling ✓ Context Diagram ✓ Data Flow Diagram ✓ System Flowchart

 ✓ Program Flowchart (highlights only) o Object Modeling ✓ Use Case Diagram ✓ Class Diagram ✓ Sequence Diagram ✓ Activity Diagram

### 4.2.6 Risk Assessment/Analysis

 The proponents have identified three main challenges for this project and have plans to handle them. First, a lack of experience with JavaScript and PeerJS could cause technical delays. To solve this, the proponents will use online tutorials and ask the Research Adviser for help if coding the multiplayer features becomes too difficult. Second, building the system that changes math difficulty might take more time than planned. The proponents will handle this by following a step-by-step schedule, building and testing small parts of the game first to catch errors early. Finally, there is a risk that students might find the game too focused on math and lose interest in playing. To prevent this, the proponents will show an early version of the game to the the proponents Capstone Adviser to ensure the gameplay and math are well-balanced. This feedback will help the proponents adjust the design so the software remains fun and useful for learning.

## 4.3 Design

### 4.3.1 Output and User-interface Design Forms

 The proponents designed the interface for Chronicles of Arithmos using a 2D pixel art style for all game assets and entities. The color scheme uses deep blue (#005385) for menu outlines and for active buttons that are currently pressed. Black (#000000) serves as the background color for all buttons and menu windows. White (# FFFFFF ) is used for all text, mathematical equations, and numerical values. The proponents selected the M+ 1m regular font for all on-screen content to ensure that mathematical problems remain readable. (Hex: #005385) (Hex: #000000) (Hex: #FFFFFF)

*Figure No. :*

Dark Blue, Black and White The proponents chose the M+ 1m regular font as it is a typeface made for clear reading with uses that range from digital signs and systems with many languages, to computer screens and tools for writing code.

*Figure No. :*

M+ 1m regular Font

## 4.4 Development

### 4.4.1 Software Specification

**Table: Software**

Specification SOFTWARE HARDWARE RPG Maker MZ (v.1.9.0) This is the main game engine. It manages the maps, character data, and visual layout of the 2D environment. HTML5 / WebGL These technologies allow the game to run in a web browser. They ensure the game works on different devices without needing a separate installer. Cascading Style Sheets (CSS) CSS controls the size of the game window. It also positions the touch controls for users on mobile devices. JavaScript (ES6) The proponents use JavaScript to program the math battle system and the multiplayer features. It adds functions that are not available in the base engine. Visual Studio Code (v.1.109) This is the text editor used for writing and organizing the JavaScript code. It helps the proponents to find and fix errors in the scripts.

 Node.js (v.24.10.0) Node.js creates a local server environment during the development phase. The proponents uses it to test how the multiplayer mode handles data. PeerJS (v.1.5.5) This library handles the peer-to-peer connection. It allows four players to connect directly using room codes without a dedicated central server. Canva Canva is the tool used for graphic design. The proponents used this software to create the official project logo.

### 4.4.2 Hardware Specification

 The proponents will use the following hardware to develop the application:

**Table No. :**

Personal Computer Hardware Specification Table No: Mobile Device Hardware Specification Operating System Windows 10 Pro 64-bit System Model MS-7C08 Processor Intel ® Pentium ® Gold G5400 @ 3.70GH Memory 16 GB RAM Graphics DirectX 12 compatible Device Model Redmi Note 13 Operating System Android 13, with MIUI 14 Processor Snapdragon 685 Octa-core Memory 8 GB RAM Display 6.67 inch FHD AMOLED

# Chapter 5.0 Summary, Conclusions, and Recommendations

 As said by DCT CCS CAPSTONE MANUAL: Conclusions should discuss what has been accomplished in the study written in the objective to see clearly all significant aspects. It may subdivided into those that are primary aesthetic., Those that announce the results of an investigating and those that present a decision concerning a course of action. Also it may be numbered with respect to problems and sub- problems in study. Recommendation should furnish future undertakings based on the analysis and conclusion of the study. It may also recommend potential applications of the study , other solutions, enhancement and/ or developments to the study. Additional suggestions from our capstone adviser on what should our chapter 5, contain and what should the proponents will do/needs or requirements or generally needed, etc:
