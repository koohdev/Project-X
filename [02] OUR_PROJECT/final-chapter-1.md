# 1.0 Introduction

## 1.1 Project Context

RPG or role-playing games is a kind of video game where the gamer or the player moves through a story, completes missions and battles hostile elements. The core mechanics of these games include exploration of the environment, character progression and combat. Traditional role playing games often use random chance to determine the outcome of combat. This brings an element of luck when deciding the winner.

Game based learning is an educational method that combines game mechanics with academic lessons. This teaching method uses systems of points, grades, and rewards to deliver information. Instead of standard lectures or drilling exercises, the system provides education directly to the learners through immersive play.

Placing RPG games into the learning environment aims to increase the focus of the students and improve their test results. Academic activities, such as solving basic arithmetic operations and practicing PEMDAS rules under the DepEd MATATAG curriculum, are incorporated into a virtual fantasy world. The MATATAG curriculum strictly focuses on building foundational mathematics skills for primary students [1]. Furthermore, data shows that children aged 9 to 12 frequently use mobile phones and digital screens as their primary tools for learning and entertainment [2]. Placing these math exercises inside a familiar digital game softens the psychological difficulties of the students. This virtual environment reduces the anxiety levels linked with strict time limited tests [3]. In spite of these benefits, educational games do not have it so easy.

In spite of these benefits, educational games do not have it so easy. An informal phenomenon, also known as the chocolate covered broccoli effect, occurs when creators of games with an educational theme carefully hide routine educational activities behind the veneer of superficial aesthetic elements [4]. Under these conditions, the education does not interact with the fundamental gameplay loop. When players feel an activity is just a hidden test, it lowers their natural desire to play. Furthermore, games with a single difficulty level fail to keep the attention of students. According to the rules of Flow theory, fast learners get bored when a game is too easy. At the same time, slow learners get frustrated when a game is too hard [5].

To overcome these barriers, educational role playing games must bring the learning goals into the main game mechanics. This ensures that the academic tasks become the determining factor for victory. The adaptive difficulty scaling matches the changing skill of the learner. The system must use this to maintain the best level of challenge. As a result, this creates a state of flow that removes boredom and frustration.

Educational RPGs must mix learning into the core gameplay to solve these issues. School exercises should act as the main factor to decide success in the game. It should not act as a separate layered activity. Systems must also use adaptive difficulty scaling to adjust the challenge based on the current skill of the player. Balancing the game difficulty keeps students in a mental state called flow. This flow state prevents boredom and frustration.

The proposed project is a 2D turn based Role Playing Game. Standard RPGs use random chance to decide combat results. This project will feature a custom math battle system instead. The success of attacks, blocks, and skills in this system will depend completely on the player. They must solve math equations under a time limit.

The approach overcomes the shortcoming of traditional mathematics drills by converting them into combat system mechanisms. Players perform primitive arithmetic tasks, including addition, subtraction, multiplication, and division, along with more complicated intermediate steps like PEMDAS. These operations are carried out to improve the mind in both speed and accuracy of mental mathematics. Furthermore, the system provides immediate physical rewards for mental hard work. Players manage to solve the numerical problems successfully, achieve the next character level, and eliminate boss enemies.

The mathematical activities are considered part of the main game loop in the project. In the game, progression requires the delivery of accurate mathematical answers which hence make players always engage in mathematical skills throughout play. This building creates a space that is specifically targeted to support the practice of mathematics.

The proposed game is given the title of the game is Chronicles of Arithmos. The proponents will build the project using RPG Maker MZ, a 2-dimensional engine designed to create turn-based role-playing games. The completed work shall be in the form of an application to run on windows platforms and a web browser and have a virtual number keypad to support touchscreen tools.

Educational games often do not provide the player with long-term engagement because of the so-called Chocolate Covered Broccoli effect. Under these conditions, game makers obstruct traditional academic exercises with aesthetics related to the game, which leads to the learning mechanics that do not interact with the main game. As a result, the learners will know about the disguised drills, and the motivation will be lowered. Permanent challenge roads also discourage players, the fast learners see the material as inadequately challenging and lose interest as well as the slow learners feel discouraged. The lack of replay value also reduces the reasons to play the game multiple times. Chronicles of Arithmos aims to solve these problems by using three main features: a math battle engine, a changing difficulty scale, and automatic enemy scaling.

Chronicles of Arithmos aims to solve the specific challenges of separated learning, fixed difficulty, and low replay value. The arithmetic combat engine solves the separated learning issue. This engine acts as the main determinant for success in combat and is never an independent activity. A difficulty tracking subsystem solves the static difficulty problem. It automatically changes the math equations to match the player at their exact level. Moreover, the game solves the low replay value using an automatic quest system. The game creates new quests automatically depending on the parts of the map explored by the player. This maintains a sense of novelty without the game developers doing manual mission design.

Reducing mathematics anxiety among primary school students in Grade 4 to 6 is the major aim of this project. These specific learners are usually 9 to 12 years old. Skagerlund et al. (2024) define this condition as a feeling of tension and fear that stops problem solving [6]. The tension comes in the form of a massive mental block. Students show lower academic results even when they actually have the needed intelligence and skills. Gokce and Guner (2024) also state that extreme mathematics anxiety consumes a massive section of working memory capacity [7]. This leads to students wasting mental resources to process negative emotions. They will then have less mental energy left to solve the actual math problems.

Placing math operations into a fantasy game world creates a low stakes environment. This setting lowers the negative emotional reactions linked to normal classroom activities. Players get real time feedback when playing a game. A successful calculation will result in an in combat Critical Hit and will act as a tangible reward. This instant reinforcement redefines the attitude of the learner towards mathematics from a source of stress into a source of confidence (Maryana et al., 2024) [8].

The inability to answer a mathematical problem appears as a Game Over screen instead of a failing grade so that students can do the calculations over and over again without the consequences of actual failure in the real world. Every in-game town contains a Training Hall, which facilitates a stress-free study method; players are able to train to achieve speed in calculations and combat controls by using a Training Dummy with maximum health, and end the lessons at their own will.

## 1.2 Objectives

### 1.2.1 General Objective

The primary objective of this project is to design and develop Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling.

### 1.2.2 Specific Objectives

1. *To implement battle mechanics.*
   This module will serve as the base structure for the custom math integration. It will include a time based battle system, turn ordering, and character stat management for Health (HP), Mana (MP), and Tactical Points (TP). Additionally, the game will feature a tutorial sequence in the opening area where mentor characters will teach the basics of combat. To provide a continuous fail-safe for skill development, every town will feature at least one training hall where the player will be able to fight a training dummy to practice their combat and mathematical calculation skills. The user will interact with this module by inputting combat commands and managing their party's health, mana and tactical points during encounters.

2. *To develop a Math Battle System plugin.*
   This module will serve as the core educational feature of the game. It will replace standard chance based combat where random probability decides if an attack hits or misses with direct math challenges. The user will interact with this module by using a keyboard to solve generated math equations within a visual interface to successfully execute their in game actions.

3. *To implement a Level-Based Difficulty System.*
   This module will automatically adjust the complexity of the math equations based on the character's current level. It will change the amount of numbers in an equation, the types of math operators used, and the size of the numbers. To provide a risk-free environment for users to practice these mechanics, the game will feature designated Training Halls in every town. The user will interact with this module by solving math problems that dynamically increase in difficulty during normal gameplay, or by engaging a Training Dummy with infinite health. During these practice encounters, users can choose fixed-level dummies to practice specific equation types or a scaling dummy that matches their current party level, exiting the session at any time by clicking the "Escape" combat command.

4. *To engineer a "Content Aware" Timer System.*
   This module will serve as the time limit during combat. It will automatically calculate the amount of time given to the player based on the equation's complexity, the total number of digits, and the types of math operators used. Users will use this feature by typing their math answers before the countdown clock runs out.

5. *To integrate an Enemy Auto Scaling System.*
   This module will change enemy stats like health and attack power to match the average level of the players party. Doing this will keep battles balanced in all map areas. Because of this, the proponents will not have to make copy pasted versions of the exact same monsters. Players will experience this system when they fight enemies that get stronger as their own characters level up.

6. *To create a Performance Based Reward Mechanism.*
   This module will handle the main combat rewards. It will check how fast and accurate the math answer is to find the result of an action. The system gives a double effect (2.0x) for a fast and correct answer. A slow but correct answer gives a normal effect. A fast but wrong answer gives half the effect (0.5x). A slow and wrong answer makes the move fail completely. Players get these exact results during combat. They trigger the results by typing the math answer on the screen.

7. *To develop an Automatic Quest Generation system.*
   This module will build side quests on its own. It will check the exact monsters and items inside unlocked map areas. The proponents will not write every single mission by hand. The system will make the tasks. Players will talk to Receptionist Mila to use this feature. She will give the party new tasks to hunt monsters or collect items.

8. *To implement a Peer to Peer (P2P) Multiplayer Connection.*
   This module will run the cooperative gameplay feature. It will link players together directly. Users will not create online accounts to play together. Players will talk to Portal Keeper Alden to access this feature. He will let them create a unique room code to host a game. He will also let them type a code to join the match of another player.

9. *To integrate a Saving System.*
   This module saves game data in local files. Moving maps makes auto checkpoints. It has manual save spots. Players pick a slot to save. They can load old data to play again.

10. *To engineer a Level Based Progression System.*
    This modules will handle the game speed. It moves stages and triggers story events. Proponents unlock harder math when character levels go up. Users go through Foundational then Intermediate then Advanced stages. Harder math and new map areas or biomes show the progress.

11. *To implement a Mobile Input System.*
    This module will check if the user is playing the game on a touch screen device. When the math input box opens in battle, the system will show a Virtual Numeric Keypad right of the screen. This will let the player tap on screen number buttons to send their answers. Players will use this feature by tapping the virtual keypad on their mobile phones to solve math problems during combat.

12. *To integrate diverse Game Assets and Entities.*
    This module will serve as the main world building structure by providing a collection of pixel art maps, background music, sound effects, enemies, and equipment. Users will engage with this module by exploring distinct areas such as forests, deserts, tundras, and volcanos, listening to location specific audio, defeating the specific enemies found in those locations, and equipping different weapons, armor, and accessories.

## 1.3 Scope and Limitations

### 1.3.1 Scope

1. *Standard Role-Playing Game (RPG) Combat Mechanics*  
   The user interacts with this module by using a computer mouse or trackpad to click through visual combat menus (such as "Attack," "Skills," or "Items"), explicitly selecting actions to manage their party's health and mana during encounters. The scope of the proposed project includes core combat mechanics structured around:
   - **Time Progress Battle (TPB):** This module will feature a visible "Action Gauge" for each combatant that fills based on their Speed or Agility stat. The game will utilize a wait-based system to automatically freeze all of these action gauges the exact moment the math input window appears on the screen. This full stop of the battle timers will make sure that enemies cannot take their turns. They will not be able to attack while the player solves the math problem and types the answer.
   - **Turn Structure:** Players will know it is their turn when the Action Gauge of their character fills up. During this phase, they will use a computer mouse to click through the combat menus. The player will choose from options like Attack, Skills, or Items to manage the health and mana of the party. Battles will follow a clear order. A player will pick an action first. The system will then check the math answer.
   - **Resource Management:** Players will track three point pools. HP shows the damage a character takes. If HP hits zero the unit is out. Players use MP for magic. TP is for combat skills.

2. *Math Battle System Plugin*  
   This module or part is the main gameplay loop for Chronicles of Arithmos. The game switches to this system when a player meets an enemy and picks a battle command. The player must solve a math equation before the time limit ends to finish their move. The system changes the difficulty of this math problem to match the current level of the user. Players will type whole number answers into the screen using the number row or numpad of the keyboard. They will then press the Enter key to attack before the clock runs out.

3. *Level Based Difficulty System*  
   This module will automatically scale the complexity of the generated math equations based on the character's current level. The user will interact with this module by visually reading the generated equations on the screen and mentally calculating answers for problems that automatically increase in term counts and operator types as their character levels up. Furthermore, this module will govern the mathematical generation for safe-practice Training Halls located in every town. The user will interact with this feature by engaging a Training Dummy, which possesses infinite Health Points (HP) and serves solely as a target for calculation practice. Users will choose between two types of targets. A fixed level dummy will give math problems for a set difficulty rank. A dynamic dummy will make equations that match the current average level of the party. Because the dummy cannot be defeated, the user will interact with the visual combat menu by clicking the "Escape" button to manually exit the training session. The math difficulty will follow a level based order:
   - **Player Levels 1–29 (Basics):** The game will make math problems that use addition and subtraction with two values. For example: `15 + 7`.
   - **Player Levels 30–69 (Intermediate):** The game will introduce Multiplication and Division operations. For example: `12 * 4`.
   - **Player Levels 70–100 (Advanced):** The game will generate three part equations utilizing the full PEMDAS rules (Parentheses, Exponents, Multiplication, Division, Addition, Subtraction). For example: `(10 + 5) * 2`.

4. *"Content Aware" Timer System*  
   This module will use a changing timer to decide how much time players get to answer. The system will check the difficulty of the math equation. It will count the total digits and look at the symbols. It will give extra time for harder math like multiplication and division. The game will also add bonus seconds for problems with larger numbers. The input box will stay on the screen even if the clock hits zero. Players must still type an answer to move forward. However, the system will mark any late answer as slow. This happens even if the math is correct. Players will watch a countdown bar during battles. They will type their answers on a keyboard or touch screen before the time runs out.

5. *Enemy Auto Scaling System*  
   This module will change enemy stats in the background. It will update Health Points (HP) and Attack power (ATK). It will also update Experience Points (EXP) and Gold rewards in real time. These numbers will change to match the average level of the party. Players will see this change during combat. Users will start battles by touching visible monster graphics. They will also start random fights while exploring the map. The health and attack values of the monsters will match the strength of the team during these fights.

6. *Performance Based Reward Mechanism*  
   This module will run the combat math. It will check the speed and accuracy of the math answer. This action will find the exact result of a move. Players will type their answers using fast keystrokes or screen taps. The game will give visual and sound feedback. This feedback will depend on the final speed and accuracy of the user. This rule will apply to all battle commands. The math check will give the following results based on the performance of the player:
   - Correct and rapid answers will apply a 2.0x critical multiplier to the action's overall effect.
   - Correct but slow answers will execute the action at its normal, base value.
   - Fast but wrong answers will apply a 0.5x penalty to the final effect of the action.
   - Incorrect and slow answers will result in complete action nullification, causing the selected move to fail entirely.

7. *Automatic Quest Generation system*  
   This module will run a system to build quests on its own. It will check the details of all the map areas the player has already opened. Chronicles of Arithmos will look at the monsters and items inside these biomes or locations. It will use this data to make new hunting and gathering tasks. These new missions will not have a time limit. Because of this, players can finish them at any point during the game. When a quest is accepted, the system will save it in the Quests tab so the user can track their progress. If a quest is rejected, the game will remove it and create a different task during the next conversation. Players will use this feature by clicking the map to walk their character toward Receptionist Mila. They will click on her to open the menu, and then they will click to accept or reject the new side quests.

8. *Peer-to-Peer (P2P) Multiplayer Framework*  
   This module will handle the cooperative multiplayer gameplay. It will use direct connections with text based room codes. The game will allow drop in combat, which means the system will automatically merge the party of a joining player with the party of the host. Players will use this feature by talking to an NPC. Players will click the Host Room button to make a room code for their game. They will click the Join Room button from the exact same character to enter another match. They will then type the code of a friend to join the room.

9. *Save*  
   This module will save game progress into local files on the device. The system will give users 20 manual save slots. It will also have one auto save function. A player can pick a slot that already has old data. The game will then replace that old file with the new progress. The auto save feature will also rewrite its own specific slot every time the character reaches a new checkpoint. Players will use this feature by opening the Save screen from the main menu. They will click a specific slot to manually record their progress. They will also trigger the automatic saves just by clicking to move their character through map exits.

10. *Level Based Progression*  
    This module will set up the stages of player growth. It will give specific rewards after players win battles and explore the map. Players will use this feature by fighting monsters or finishing quests to earn the rewards listed below:
    - **Experience Points (EXP):** Gaining EXP will raise the level of the character. The lowest amount a player can get from a low level monster is 10 points (Level 1 Slime). The game will limit the highest possible reward from an end game boss to 99,999 points.
    - **Gold (Currency):** Players will collect this money when they beat enemies and finish quests. The minimum gold drop from a basic enemy is 5 G, while the maximum reward from a high-tier boss or elite quest is 50,000 G. This currency is used to buy new equipment and items from merchants.
    - **Story Milestones:** Updates the "Story Progress", allowing the game to unlock higher-level maps.

11. *Mobile Detection System and Virtual Numeric Keypad*  
    This module will automatically detect if the user is on a mobile device. When the math input window opens during combat, the system will display a Virtual Numeric Keypad directly next to it on the screen. The user will interact with this module on supported mobile devices by physically tapping the on-screen number buttons and the "Submit" button to enter math answers.

12. *Game Assets and Entities*  
    This module will serve as the main world-building structure by providing a collection of pixel art maps, background music, sound effects, enemies, and equipment. The user will interact with this module by exploring distinct areas such as forests, deserts, tundras, and volcanos, defeating area specific enemies, and equipping various weapons, armor, and accessories. These assets will include:

    - **Character Roster:** This includes the main characters that the player will talk to, fight alongside, or receive quests from to move the story forward:
      - *Bron*
      - *Martha*
      - *Lily*
      - *Kael*
      - *Elara*
      - *Garrick*
      - *Sylas*
      - *Isolde*
      - *Thorne*
      - *Lyra*
      - *Fenrin*
      - *Elder Tobias*
      - *Merchant Oryn*
      - *Receptionist Mila*
      - *Bard Jareth*
      - *Captain Valerius*
      - *Professor Haze*
      - *Innkeeper Gorm*
      - *Blacksmith Rurik*
      - *Widow Claire*
      - *Farmer Ben*
      - *Alchemist Vanya*
      - *Librarian Estel*
      - *Guard Captain Aris*
      - *Fisherman Old Tom*
      - *Street Urchin Pip*
      - *Nobleman Caelus*
      - *Priestess Anara*
      - *Hunter Kaelen*
      - *Portal Keeper Alden*
      - *The Numeromancer*

    - **Background NPCs:** Generic townspeople and villagers used to fill up the maps to make the game world feel alive and busy:
      - *Townsman 1–5 (Male)*
      - *Townswoman 1–5 (Female)*
      - *Playing Boy 1–2*
      - *Playing Girl 1–2*
      - *Market Shopper 1–3*
      - *Tavern Patron 1–4*
      - *Knight*
      - *Farmhand 1–2*
      - *Stable Boy*
      - *Washerwoman*
      - *Street Sweeper*
      - *Beggar 1–2*
      - *Strolling Couple (Man/Woman)*
      - *Academy Student 1–4*
      - *Visiting Merchant*
      - *Visiting Noble*
      - *Lost Tourist*
      - *Drunkard*
      - *Gossiping Lady 1–2*
      - *Running Messenger*
      - *Sleeping Guard*
      - *Fishing Boy*
      - *Old Cat Lady*
      - *Street Performer*
      - *Watching Crowd Member*

    - **Enemies:**
      - *Plains & Forest Biome:* Slime, Rat, Bat, Spider, Hornet, Wolf, Bear, Treant, Goblin, Goblin Archer, Goblin Shaman, Orc, Bandit, Bandit Leader, Crow, Snake, Fairy, Mandrake, Wild Boar, Forest Golem.
      - *Desert Biome:* Sand Slime, Scorpion, Giant Scorpion, Cactus, Sand Worm, Mummy, Skeleton Warrior, Skeleton Mage, Desert Wolf, Lamia, Basilisk, Gargoyle, Sand Golem, Vulture, Sphinx, Desert Rogue, Ant Lion, Dust Spirit, Ancient Scarab, Pharaoh’s Guard.
      - *Tundra & Frost Biome:* Ice Slime, Snow Wolf, Polar Bear, Ice Bat, Snow Spirit, Yeti, Ice Golem, Crystal Spider, Frost Giant, White Tiger, Corrupted Penguin, Ice Drake, Frozen Knight, Winter Wisp, Wendigo, Frost Mage, Glacial Turtle, Snow Harpy, Ice Elemental, Fenrir.
      - *Volcano & Fire Biome:* Magma Slime, Fire Spirit, Imp, Demon, Succubus, Cerberus, Lava Golem, Fire Bat, Salamander, Dragon Hatchling, Red Dragon, Efreet, Phoenix, Iron Giant, Dark Knight, Cultist, Fire Elemental, Minotaur, Chimera, Demon Lord.
      - *General & Dungeon:* Training Dummy, Ghost, Zombie, Vampire, Vampire Bat, Mimic, Shadow, Will-o'-the-Wisp, Animated Armor, Flying Sword, Magic Pot, Gazer, Ogre, Troll, Warlock, Necromancer, Reaper, Chaos Cloud, Number Eater, Equation Spirit, The Unknown.

    - **Items:**
      - *Consumable Items (Recovery & Utility):* Potion, Hi-Potion, Full Potion, Magic Water, Hi-Magic Water, Elixir, Antidote, Eye Drops, Echo Herb, Stimulant, Potent Stimulant, Panacea, Dispel Herb, Escape Rope, Repel Spray.
      - *Stat Boosters (Permanent Upgrades):* HP Up, MP Up, Strength Seed, Defense Seed, Magic Seed, Agility Seed, Luck Seed, Skill Book.
      - *Monster Loot & Drops:*
        - *Plains/Forest:* Green Gel, Rat Tail, Bat Wing, Sticky Web, Insect Wing, Wolf Pelt, Bear Claw, Living Branch, Goblin Cloth, Shaman Bead, Orc Tusk, Stolen Coin Purse, Shiny Feather, Snake Skin, Fairy Dust, Mandrake Root, Boar Meat, Ancient Bark.
        - *Desert:* Yellow Gel, Scorpion Stinger, Cactus Flower, Sand Essence, Old Bandage, Bone Fragment, Skull, Dry Fur, Snake Scale, Petrified Eye, Stone Wing, Sandstone Block, Vulture Beak, Riddle Tablet, Scarab Shell, Golden Fragment.
        - *Tundra:* Blue Gel, White Fur, Thick Hide, Ice Crystal, Snowflake Core, Yeti Horn, Permafrost Shard, Crystal Leg, Frost Metal, Corrupted Feather, Drake Scale, Cold Wisp, Frozen Heart, Ice Turtle Shell, Harpy Feather, Wolf Fang.
        - *Volcano:* Red Gel, Ember, Imp Wing, Demon Horn, Succubus Cloth, Hellhound Fang, Obsidian Shard, Fire Gland, Dragon Tooth, Red Scale, Djinn Lamp, Phoenix Ash, Iron Scraps, Dark Armor Piece, Forbidden Page, Chimera Tail, Infernal Core.
        - *General:* Ectoplasm, Rotten Flesh, Vampire Fang, Unknown Fluid, Spirit Dust, Haunted Metal, Ceramic Shard, Evil Eye, Ogre Club, Magic Powder, Tattered Robe, Chaos Mote, Arithmetic Essence, Void Fragment.

    - **Class Roster:** Swordsman, Sorcerer, Priest, Knight, Martial Artist, Magic Swordsman, Hunter, Bandit.

    - **Weapons:**
      - *Swordsman (Swords):* Long Sword, Woodcutter's Blade, Wolf Fang Sword, Forest Cutter, Bandit's Edge, Verdant Blade, Sand Scimitar, Scorpion Tail, Dune Blade, Sun-Scorched Sword, Ancient Khopesh, Ice Brand, Glacial Edge, Frostbite Sword, Crystal Saber, Blizzard Blade, Magma Blade, Dragon Bone Sword, Infernal Edge, Flame Tongue, Phoenix Feather Sword.
      - *Sorcerer (Staves):* Oak Staff, Briar Rod, Druid's Staff, Faerie Wand, Root Staff, Nature's Call, Sandstone Rod, Mirage Staff, Cobra Head Staff, Sun Rod, Sphinx Cane, Icicle Rod, Snowflake Staff, Hailstorm Wand, Permafrost Cane, Frozen Core Staff, Ember Rod, Ash Staff, Dragon Breath Wand, Core Magma Staff, Hellfire Rod.
      - *Priest (Maces):* Wooden Mace, Oak Club, Spirit Mace, Blessed Branch, Mossy Hammer, Guardian's Cudgel, Golden Scepter, Sandstone Hammer, Sun Disc Mace, Tomb Guardian Club, Sacred Ankh, Crystal Mace, Hailstone Hammer, Frozen Scepter, Polar Club, Divine Ice Mace, Obsidian Mace, Lava Rock Hammer, Cleansing Fire Club, Forge Master's Hammer, Phoenix Down Mace.
      - *Knight (Spears):* Short Spear, Hunter's Spear, Boar Tusk Lance, Forest Guard Pike, Wooden Pike, Leaf-Blade Spear, Scorpion Stinger, Desert Pike, Bronze Lance, Sandpiercer, Pharaoh's Guard, Ice Shard Lance, Glacier Pike, Tundra Harpoon, Frost Wyrm Spear, Frozen Needle, Magma Pike, Dragon Scale Lance, Red Steel Spear, Obsidian Lance, Hellfire Harpoon.
      - *Martial Artist (Claws):* Leather Gloves, Bear Claws, Wolf Paws, Sharp Thorns, Tree Bark Knuckles, Wild Beast Fists, Scorpion Pincers, Sandstone Gauntlets, Cactus Spines, Mummy Wraps, Golden Knuckles, Ice Picks, Yeti Fists, Frostbite Gloves, Crystal Talons, Polar Paws, Salamander Claws, Dragon Fangs, Magma Fists, Burning Knuckles, Demon Hands.
      - *Magic Swordsman (Enchanted Blades):* Rapier, Wind Blade, Leaf Cutter, Elven Rapier, Swift Blade, Whisper Edge, Mirage Rapier, Heatwave Saber, Dust Devil Blade, Golden Epee, Sun-Strike Sword, Chill Spike, Frozen Needle, Aurora Blade, Ice Queen's Rapier, Zero Kelvin, Searing Saber, Molten Rapier, Blaze Edge, Phoenix Tail, Volcanic Spike.
      - *Hunter (Bows):* Short Bow, Oak Bow, Hunter's Bow, Ranger's Crossbow, Vine Bow, Elven Bow, Bone Bow, Sandstone Crossbow, Scorpion Recurve, Desert Wind Bow, Golden Arrow, Ice Crystal Bow, Frostbite Crossbow, Mammoth Ivory Bow, Blizzard String, Glacial Shot, Ash Wood Bow, Flame String, Magma Rock Crossbow, Dragon Bone Bow, Phoenix Fire Bow.
      - *Bandit (Daggers):* Knife, Rusty Shiv, Hunter's Knife, Poison Tip, Thief's Shank, Forest Tooth, Curved Dagger, Sand Shiv, Scorpion Barb, Tomb Blade, Golden Dagger, Icicle Shiv, Frozen Dagger, Shard of Glass, Cold Steel Knife, Frostbite Dirk, Obsidian Knife, Heated Dagger, Ember Shiv, Dragon Claw, Hell's Tooth.

    - **Skills:**
      - *Swordsman:* Strong Attack, Slash, Double Slash, Wide Swing, Armor Break, Blade Bash, Focus, Parry, Sonic Wave, Wind Slash, Power Break, Mind Break, Berserk Stance, Cross Cut, Omnislash.
      - *Sorcerer:* Fire, Fire II, Fire III, Ice, Ice II, Ice III, Thunder, Thunder II, Thunder III, Flare, Freeze, Shock, Magic Drain, Concentrate, Meteor Swarm.
      - *Priest:* Heal, Heal II, Heal III, Party Heal, Cure Poison, Cure Blind, Cure Silence, Panacea, Raise, Holy Light, Protect, Shell, Regenerate, Purify, Divine Intervention.
      - *Knight:* Provoke, Shield Bash, Cover, Iron Defense, Guard Ally, Shield Wall, Fortify, Sentinel, Justice Strike, Heavy Charge, Taunt, Unbreakable Will, Phalanx, Retribution, Castle of Stone.
      - *Martial Artist:* Punch, Kick, Triple Kick, Roundhouse, Chakra, Meditate, Pressure Point, Earth Splitter, Gale Palm, Spirit Wave, Counter, Leg Sweep, Fists of Fury, Chi Blast, Seven Star Strike.
      - *Magic Swordsman:* Fire Blade, Ice Blade, Thunder Blade, Wind Blade, Drain Blade, Aspir Blade, Magic Barrier, Enchant Weapon, Dispel Strike, Elemental Burst, Arcane Slash, Spell Shield, Mystic Thrust, Teleport Strike, Rune Breaker.
      - *Hunter:* Aim, Power Shot, Rapid Fire, Poison Arrow, Sleep Arrow, Blind Arrow, Silence Arrow, Arrow Rain, Eagle Eye, Beast Slayer, Piercing Shot, Camouflage, Trap Set, Snipe, Hail of Arrows.
      - *Bandit:* Steal, Mug, Sneak Attack, Poison Edge, Sand Throw, Smoke Bomb, Backstab, Sprint, Gold Snatch, Venom Strike, Shadow Step, Dirty Trick, Twin Daggers, Lucky Strike, Assassinate.

    - **Status Effects:**
      - *Negative States (Debuffs):* Knockout, Poison, Blind, Silence, Confusion, Sleep, Paralysis, Stun, Bleed, Burn, Freeze, Slow, Curse, Weakness, Fear.
      - *Positive States (Buffs):* Regenerate, Haste, Protect, Shell, Focus, Magic Barrier, Attack Up, Defense Up, Magic Up, Agility Up, Evasion Up, Immortal, Auto-Life, Reflect, Counter Stance.

    - **Armor & Accessories:**
      - *Shields (Equippable only by Knights, Swordsmen, Priests):* Small Shield, Buckler, Round Shield, Kite Shield, Iron Shield, Steel Shield, Mythril Shield, Gold Shield, Wooden Lid, Hunter's Buckler, Bronze Shield, Scale Guard, Shell Buckler, Ice Shield, Crystal Guard, Frost Shield, Dragon Shield, Flame Guard, Obsidian Shield, Aegis.
      - *Headgear:* Leather Cap, Iron Helmet, Steel Helmet, Mythril Helm, Full Helm, Viking Helm, Dragon Helm, Genji Helm, Leather Helm, Feathered Hat, Magician's Hat, Circlet, Ribbon, Bandana, Turban, Silk Hood, Fur Hood, Ice Crown, Salamander Coif, Royal Crown.
      - *Body Armor:* Cloth Tunic, Leather Armor, Iron Armor, Steel Armor, Mythril Armor, Plate Mail, Heavy Mail, Scale Mail, Glacial Mail, Flame Mail, Dragon Armor, Traveler's Tunic, Hard Leather, Hunter's Vest, Ninja Suit, Cotton Robe, Silk Robe, Sorcerer's Robe, Winter Robe, Lava Robe, Sage's Robe.
      - *Accessories:* Ring of Protection, Ring of Power, Ring of Magic, Ring of Speed, Ring of Life, Poison Charm, Silence Amulet, Blindness Glasses, Paralysis Talisman, Sleep Earring, Fire Ring, Ice Ring, Thunder Ring, Earth Ring, Gold Ring, Lucky Coin, Warrior's Badge, Scholar's Specs, Knight's Crest, Sniper's Eye.

    - **Background Music (BGM):**
      - *Battle & Boss Themes:* Battle1, Battle2, Battle3, Battle4, Battle5, Battle6, Battle7, Boss1, Boss2, Boss3, Boss4, Boss5.
      - *Towns & Safe Zones:* Town1, Town2, Town3, Town4, Town5, Town6, Town7, Castle1, Castle2.
      - *Exploration (Overworld & Dungeons):* Field1, Field2, Field3, Field4, Dungeon1, Dungeon2, Dungeon3, Dungeon4, Dungeon5, Dungeon6, Dungeon7, Dungeon8, Ship1, Ship2, Ship3.
      - *Story & Cutscenes:* Scene1, Scene2, Scene3, Scene4, Scene5, Scene6, Theme1, Theme2, Theme3, Theme4, Theme5, Theme6.

### 1.3.2 Limitations

1. *Mathematical Scope and Generation Limits*  
   The system does not currently support advanced algebra, calculus, or non-integer results (fractions/decimals). To maintain combat flow, the math generator is strictly restricted so that all division problems calculate to exact whole numbers, avoiding fractions or decimals entirely. Furthermore, the system imposes a hard limit on the multiplier and the divisor (the second number in any multiplication or division problem), capping them at a range of 1 to 20. This number limit applies to all battles in the game. It also covers the multi part math problems in higher levels.

2. *Input Handling Differences*  
   The Virtual Numeric Keypad lets the game run on touch screens. Tapping a flat screen does not give the physical feedback of real keys.

3. *Input Method*  
   Input uses number rows or numpads on keyboards. Proponents give mobile users a Virtual Numeric Keypad. Input speed changes depending on the device.

4. *Asset Fidelity*  
   Chronicles of Arithmos uses 2D pixel art from RPG Maker MZ. Proponents do not use 3D models or hard physics, since RPG Maker MZ is for 2D pixel games.

5. *Peer to Peer Latency Sensitivity*  
   The multiplayer is based on the internet connection of the host. The intended project will utilize direct peer-to-peer communications instead. Slow internet connection on the host side may cause the Math Timer to stop or result in other players who are involved in the multiplayer feature to be disconnected.

6. *Host Dependent Connection*  
   Since the project will utilize the peer-to-peer (P2P) architecture, there will be no node that manages a list of games or sessions. When the host shuts down the application or loses its connection, the whole game experience will be ended for everyone. Under these conditions, the participants are not able to re-use the old room code and continue their game, but have to start a new game session.

7. *Local Only Save Data*  
   Proponents use local files for the save system on the player device. No login or cloud database exists. There is no cloud sync. A player cannot switch from a PC to a phone. They must move the files manually to do this.
