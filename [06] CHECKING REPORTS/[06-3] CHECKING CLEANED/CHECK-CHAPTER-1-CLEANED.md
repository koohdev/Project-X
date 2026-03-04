# 1.0 Introduction

## 1.1 Project Context

The proposed project will be a 2D turn-based Role-Playing Game (RPG). While standard RPGs use random chance to decide combat outcomes, this game will implement a custom math battle system. In this system, the outcome of attacks, defenses, and skills will depend directly on the player's ability to solve math equations under a time limit.

This approach will address the problem of repetitive math drills by turning them into a combat system. It will help players practice the transition from basic math, like addition and subtraction, to intermediate operations, like PEMDAS. By doing this, the system will build mental math speed and precision. It will also provide direct rewards for mental effort, allowing players to level up and defeat bosses when they solve math problems correctly.

The project will integrate math exercises directly into its gameplay mechanics. Because advancing in the game will depend on answering math equations correctly, players will continuously practice their calculation skills as they play. This setup will create a purely interactive environment for arithmetic practice.

To achieve the goals described above, the proposed game will be named Chronicles of Arithmos. The system will be developed using RPG Maker MZ, a 2D game development engine designed for creating turn-based role-playing games. The game will function as a standalone application that players will be able to launch on Windows computers and web browsers. It will also feature a Virtual Numeric Keypad so it will be accessible on touch-screen devices.

Educational games often fail to retain player interest because of the "Chocolate-Covered Broccoli" effect [1]. This occurs when developers take a standard, repetitive school task and place it behind game graphics. Because the learning mechanics are poorly integrated with the actual gameplay, students may recognize they are simply completing a disguised drill and lose motivation. Games with static difficulty curves may also discourage players; if a game's difficulty does not adapt, students who learn at a faster pace may find the content insufficiently challenging and lose focus, while those who struggle may find it too difficult and become frustrated [2].

Games with limited replay value may also offer reduced incentive for students to return. Chronicles of Arithmos will address these issues through three integrated systems. First, the math battle system will function as the primary variable that determines an action's output, rather than being a separate mini-game layered on top. Second, the system will feature a Level-Based Difficulty System that automatically scales the complexity of the equations to match the player's current character level. Third, to maintain replayability without manual content creation, the system will use an Automatic Quest Generation system that builds new tasks from the player's unlocked content.

The primary purpose of this project will be to reduce Mathematics Anxiety among Grade 4–6 students. Richardson and Suinn (1972) defined this as "a feeling of tension and anxiety that interferes with the manipulation of numbers" [3]. This phenomenon creates a psychological barrier; when students experience this tension, they will struggle to perform well in academics regardless of their actual aptitude or intelligence. Ashcraft (2002) further suggested that high math anxiety occupies a student's working memory capacity [4]. This means that because the student's brain is actively processing fear and worry, there is less mental energy left available to actually solve the math problem.

By gamifying these math operations within a low-stakes, fantasy context, the game will aim to reduce the negative emotional responses usually associated with classroom drills. The system will provide a direct feedback loop where a correct calculation will result in a tangible in-game "Critical Hit." Seeing direct success will provide rewarding reinforcement, which may shift the learner's association with arithmetic from tension to confidence (Gee, 2003) [5]. By providing a setting where failure will simply result in a "Game Over" screen rather than a failing grade, students will be able to practice without fear. To further support this low-stakes learning, every town will feature a Training Hall where players can practice their calculation speed and combat mechanics against a Training Dummy with infinite health, allowing them to manually exit the practice session at any time.

The game will also feature an Enemy Auto-Scaling System to maintain combat challenge regardless of the user's current level. Additionally, it will include a Peer-to-Peer (P2P) Multiplayer mode that will allow cooperative learning and social interaction among players.

The story will begin in the Plains of Origin, where the protagonist will awaken to find the world filled with "Anomalies," which are chaos fractures caused by the breakdown of world laws. Guided by Bron, a main mentor character for physical combat, and Martha, a main mentor character for magical theory, the player will complete a tutorial. The player will learn that their younger sister, Lily, who serves as the central narrative driver, has been afflicted by a curse. To cure her, the player must restore the world's logic.

The protagonist will travel across four distinct biomes, each guarded by a corrupted elemental force. They will recover fragments from the Forest Golem, the Pharaoh's Guard, the Fenrir wolf, and the Demon Lord. The journey will lead to the Void Dimension, where the player will confront The Numeromancer, the source of the chaos and final antagonist of the game, utilizing both combat and math skills to stabilize the realm.

To complete this journey, the player will recruit a diverse party of allies. Kael will join as a knight companion. Elara will be recruited as a sorceress companion. Garrick will serve as a heavily armored tank companion. Sylas will join as a rogue companion. Isolde will be recruited as a healer companion. Thorne will serve as a ranger companion. Lyra will join as a magic swordsman companion. Fenrin will be recruited as a monk companion.

The narrative and mechanics will be supported by key side characters. Elder Tobias will provide the initial story quests. Merchant Oryn will sell general goods. Receptionist Mila will act as a procedural quest hub. Bard Jareth will offer healing interactions. Captain Valerius will provide locations on where to go next. Professor Haze will unlock advanced skills for the player. Innkeeper Gorm will run establishments that restore the party's health and mana. Blacksmith Rurik will provide equipment upgrades. Widow Claire will offer a specific side quest. Farmer Ben, Nobleman Caelus, and Fisherman Old Tom will provide background flavor dialogue. Alchemist Vanya will sell potions. Librarian Estel will explain the game's lore and backstory. Guard Captain Aris will patrol the towns. Street Urchin Pip will give hints about hidden items. Priestess Anara will remove negative status effects. Hunter Kaelen will scout and provide map information. Portal Keeper Alden will allow the player to either host or join a multiplayer room. The towns will be further populated by generic, non-mechanical NPCs to provide atmosphere, including Townsmen, Townswomen, Playing Children, Market Shoppers, Tavern Patrons, Castle Guards, Farmhands, Stable Boys, Washerwomen, Street Sweepers, Beggars, Strolling Couples, Academy Students, Visiting Merchants, Nobles, Tourists, Drunkards, Gossiping Ladies, Messengers, Guards, Fishers, Old Ladies, Street Performers, and Crowd Members.

To complement this visual atmosphere and help reduce the anxiety associated with traditional math drills, the game will utilize a comprehensive suite of thematic background music. These audio tracks will dynamically shift between peaceful town melodies, intense battle anthems, and atmospheric dungeon themes to maintain player engagement and keep the user in a state of optimal flow.

The game world will feature distinct environmental biomes with specific enemies and loot. The Plains and Forests will serve as lush starter zones. In this biome, the Slime will drop Green Gel. The Rat will drop a Rat Tail. The Bat will drop a Bat Wing. The Spider will drop a Sticky Web. The Hornet will drop an Insect Wing. The Wolf will drop a Wolf Pelt. The Bear will drop a Bear Claw. The Treant will drop a Living Branch. The Goblin and Goblin Archer will drop Goblin Cloth. The Goblin Shaman will drop Shaman Beads. The Orc will drop an Orc Tusk. The Bandit and Bandit Leader will drop a Stolen Coin Purse. The Crow will drop a Shiny Feather. The Snake will drop Snake Skin. The Fairy will drop Fairy Dust. The Mandrake will drop a Mandrake Root. The Wild Boar will drop Boar Meat. The Forest Golem will drop Ancient Bark.

The Deserts will serve as harsh drylands. The Sand Slime will drop Yellow Gel. The Scorpion and Giant Scorpion will drop Scorpion Stingers. The Cactus will drop a Cactus Flower. The Sand Worm, Ant Lion, and Dust Spirit will drop Sand Essence. The Mummy will drop an Old Bandage. The Skeleton Warrior will drop a Bone Fragment, and the Skeleton Mage will drop a Skull. The Desert Wolf will drop Dry Fur. The Lamia will drop a Snake Scale. The Basilisk will drop a Petrified Eye. The Gargoyle will drop a Stone Wing. The Sand Golem will drop a Sandstone Block. The Vulture will drop a Vulture Beak. The Sphinx will drop a Riddle Tablet. The Ancient Scarab will drop a Scarab Shell. The Desert Rogue and Pharaoh's Guard will drop Golden Fragments.

The Tundra and Frost regions will serve as frozen expanses. The Ice Slime will drop Blue Gel. The Snow Wolf will drop a Wolf Fang. The Polar Bear will drop Thick Hide. The Ice Bat and White Tiger will drop White Fur. The Snow Spirit and Winter Wisp will drop Cold Wisps. The Yeti will drop a Yeti Horn. The Ice Golem will drop a Permafrost Shard. The Crystal Spider will drop a Crystal Leg. The Frost Giant and Frozen Knight will drop Frost Metal. The Corrupted Penguin will drop a Corrupted Feather. The Ice Drake will drop a Drake Scale. The Wendigo and Frost Mage will drop Frozen Hearts. The Glacial Turtle will drop an Ice Turtle Shell. The Snow Harpy will drop a Harpy Feather. The Ice Elemental will drop an Ice Crystal. The Fenrir will drop a Snowflake Core.

The Volcano and Fire zones will be the most dangerous as a harsh wasteland. The Magma Slime will drop Red Gel. The Fire Spirit and Fire Elemental will drop Embers. The Imp will drop an Imp Wing. The Demon and Minotaur will drop Demon Horns. The Succubus will drop Succubus Cloth. The Cerberus will drop a Hellhound Fang. The Lava Golem will drop an Obsidian Shard. The Fire Bat will drop a Fire Gland. The Salamander and Dragon Hatchling will drop Red Scales. The Red Dragon will drop a Dragon Tooth. The Efreet will drop a Djinn Lamp. The Phoenix will drop Phoenix Ash. The Iron Giant will drop Iron Scraps. The Dark Knight will drop Dark Armor Pieces. The Cultist will drop a Forbidden Page. The Chimera will drop a Chimera Tail. The Demon Lord will drop an Infernal Core.

Dungeons throughout the game will provide rare encounters and high-tier loot. The Ghost and Shadow will drop Ectoplasm. The Zombie will drop Rotten Flesh. The Vampire and Vampire Bat will drop Vampire Fangs. The Mimic and Magic Pot will drop Unknown Fluid. The Will-o'-the-Wisp will drop Spirit Dust. The Animated Armor and Flying Sword will drop Haunted Metal. The Gazer will drop an Evil Eye. The Ogre and Troll will drop Ogre Clubs. The Warlock will drop Magic Powder. The Necromancer will drop a Tattered Robe. The Reaper will drop a Chaos Mote. The Ceramic Shard will drop randomly in general dungeons. The Chaos Cloud, Number Eater, Equation Spirit, and The Unknown will drop Arithmetic Essences and Void Fragments.

The item database will support gameplay with various consumables. Potions, Hi-Potions, and Full Potions will restore health. Magic Waters, Hi-Magic Waters, and Elixirs will restore mana or both health and mana. Antidotes, Eye Drops, Echo Herbs, Stimulants, Potent Stimulants, Panaceas, and Dispel Herbs will cure negative status ailments. Escape Ropes and Repel Sprays will help players avoid or leave battles. Permanent stat boosters like HP Up, MP Up, Strength Seeds, Defense Seeds, Magic Seeds, Agility Seeds, Luck Seeds, and Skill Books will permanently upgrade a character's core attributes.

Players will choose from eight distinct character classes, each with access to a specialized weapon arsenal that will expand as the player progresses. The Swordsman class will wield swords. The Long Sword will be a standard issue blade. The Woodcutter's Blade will be a simple cutting tool. The Wolf Fang Sword will be an animal-themed blade. The Forest Cutter will be a nature themed sword. The Bandit's Edge will be a thief's blade. The Verdant Blade will be a green sword. The Sand Scimitar will be a desert curved sword. The Scorpion Tail will be a stinger-shaped sword. The Dune Blade will be a sandy sword. The Sun-Scorched Sword will be a heat-themed sword. The Ancient Khopesh will be an old desert blade. The Ice Brand will be a cold-forged sword. The Glacial Edge will be a frozen sword. The Frostbite Sword will be a chilling blade. The Crystal Saber will be a crystalline sword. The Blizzard Blade will be a winter themed sword. The Magma Blade will be a molten sword. The Dragon Bone Sword will be crafted from dragon remains. The Infernal Edge will be a demonic blade. The Flame Tongue will be a fire-forged sword. The Phoenix Feather Sword will be a legendary fiery sword.

The Sorcerer class will wield staves and rods. The Oak Staff will be a basic wooden staff. The Briar Rod will be a thorny stick. The Druid's Staff will be a nature themed pole. The Faerie Wand will be a small magical stick. The Root Staff will be made of tree roots. Nature's Call will be an earth-themed staff. The Sandstone Rod will be a desert-forged staff. The Mirage Staff will be an illusion-themed rod. The Cobra Head Staff will be shaped like a snake. The Sun Rod will be a light-themed staff. The Sphinx Cane will be an ancient desert cane. The Icicle Rod will be made of ice. The Snowflake Staff will be a frost-themed pole. The Hailstorm Wand will be a winter-themed wand. The Permafrost Cane will be an enduring cold cane. The Frozen Core Staff will be a deeply chilled staff. The Ember Rod will be a smoldering stick. The Ash Staff will be made from burnt wood. The Dragon Breath Wand will be a dragon-themed wand. The Core Magma Staff will be a molten pole. The Hellfire Rod will be a demonic fiery staff.

The Priest class will wield maces and canes. The Wooden Mace will be a simple blunt weapon. The Oak Club will be a sturdy wooden stick. The Spirit Mace will be a spiritually aligned blunt weapon. The Blessed Branch will be a holy wooden stick. The Mossy Hammer will be an overgrown blunt weapon. The Guardian's Cudgel will be a protective club. The Golden Scepter will be an ornate rod. The Sandstone Hammer will be a desert crafted mallet. The Sun Disc Mace will be a light-themed weapon. The Tomb Guardian Club will be an ancient blunt weapon. The Sacred Ankh will be a cross shaped holy relic. The Crystal Mace will be a crystalline blunt weapon. The Hailstone Hammer will be a frozen mallet. The Frozen Scepter will be an icy rod. The Polar Club will be a cold weather club. The Divine Ice Mace will be a holy frozen weapon. The Obsidian Mace will be a dark volcanic weapon. The Lava Rock Hammer will be a molten mallet. The Cleansing Fire Club will be a fiery blunt weapon. The Forge Master's Hammer will be a heavy smithing tool. The Phoenix Down Mace will be a legendary healing blunt weapon.

The Knight class will wield spears and lances. The Short Spear will be a basic reach weapon. The Hunter's Spear will be a basic hunting tool. The Boar Tusk Lance will be an animal-themed spear. The Forest Guard Pike will be a woodland spear. The Wooden Pike will be a lightweight reach weapon. The Leaf-Blade Spear will be a nature themed polearm. The Scorpion Stinger will be a desert themed spear. The Desert Pike will be a sandy polearm. The Bronze Lance will be a metallic reach weapon. The Sandpiercer will be a desert lance. The Pharaoh's Guard will be an ancient royal spear. The Ice Shard Lance will be a frozen reach weapon. The Glacier Pike will be a heavy cold polearm. The Tundra Harpoon will be a hunting spear for the cold. The Frost Wyrm Spear will be a dragon themed ice lance. The Frozen Needle will be a sharp icy spear. The Magma Pike will be a molten polearm. The Dragon Scale Lance will be a heavy reptilian spear. The Red Steel Spear will be a crimson metallic lance. The Obsidian Lance will be a dark volcanic spear. The Hellfire Harpoon will be a demonic fiery spear.

The Martial Artist class will wield claws and knuckles. The Leather Gloves will be basic hand protection. The Bear Claws will be animal-themed fist weapons. The Wolf Paws will be lupine hand gear. The Sharp Thorns will be spiky hand wraps. The Tree Bark Knuckles will be wooden fist weapons. The Wild Beast Fists will be feral gloves. The Scorpion Pincers will be desert-themed claws. The Sandstone Gauntlets will be heavy rocky gloves. The Cactus Spines will be prickly hand weapons. The Mummy Wraps will be ancient cloth bindings. The Golden Knuckles will be ornate metallic fist weapons. The Ice Picks will be sharp frozen claws. The Yeti Fists will be heavy snowy gloves. The Frostbite Gloves will be chilling hand gear. The Crystal Talons will be magical glass claws. The Polar Paws will be cold-weather animal gloves. The Salamander Claws will be fiery hand weapons. The Dragon Fangs will be reptilian fist weapons. The Magma Fists will be molten hand gear. The Burning Knuckles will be flaming fist weapons. The Demon Hands will be dark supernatural claws.

The Magic Swordsman class will wield enchanted blades and rapiers. The Rapier will be a thrusting sword. The Wind Blade will be a gust-themed sword. The Leaf Cutter will be a nature-themed rapier. The Elven Rapier will be a mystical thrusting sword. The Swift Blade will be a lightweight sword. The Whisper Edge will be a silent blade. The Mirage Rapier will be an illusionary sword. The Heatwave Saber will be a desert-themed blade. The Dust Devil Blade will be a sandy thrusting sword. The Golden Epee will be an ornate rapier. The Sun-Strike Sword will be a bright blade. The Chill Spike will be a cold-themed thrusting sword. The Frozen Needle will be an icy rapier. The Aurora Blade will be a light-themed cold sword. The Ice Queen's Rapier will be a royal frozen blade. Zero Kelvin will be an ultimate freezing sword. The Searing Saber will be a hot blade. The Molten Rapier will be a liquid fire sword. The Blaze Edge will be a flaming blade. The Phoenix Tail will be a fiery magical sword. The Volcanic Spike will be a molten thrusting sword.

The Hunter class will wield bows. The Short Bow will be a basic ranged weapon. The Oak Bow will be a standard wooden bow. The Hunter's Bow will be a tool for tracking. The Ranger's Crossbow will be a mechanical ranged weapon. The Vine Bow will be a nature-themed weapon. The Elven Bow will be a mystical archery tool. The Bone Bow will be made from skeletal remains. The Sandstone Crossbow will be a desert-themed mechanical bow. The Scorpion Recurve will be an animal-themed desert bow. The Desert Wind Bow will be a sandy ranged weapon. The Golden Arrow will be an ornate projectile weapon. The Ice Crystal Bow will be a frozen ranged weapon. The Frostbite Crossbow will be a chilling mechanical bow. The Mammoth Ivory Bow will be a heavy prehistoric weapon. The Blizzard String will be a winter-themed bow. The Glacial Shot will be a heavy frozen weapon. The Ash Wood Bow will be a burnt wooden bow. The Flame String will be a fiery ranged weapon. The Magma Rock Crossbow will be a molten mechanical bow. The Dragon Bone Bow will be a reptilian ranged weapon. The Phoenix Fire Bow will be a legendary flaming bow.

The Bandit class will wield daggers and knives. The Knife will be a simple utility blade. The Rusty Shiv will be an old, degraded dagger. The Hunter's Knife will be an animal-skinning tool. The Poison Tip will be a toxic dagger. The Thief's Shank will be a rogue's blade. The Forest Tooth will be a woodland dagger. The Curved Dagger will be a swept blade. The Sand Shiv will be a desert-themed knife. The Scorpion Barb will be an animal-themed desert dagger. The Tomb Blade will be an ancient knife. The Golden Dagger will be an ornate short blade. The Icicle Shiv will be a frozen knife. The Frozen Dagger will be a cold short blade. The Shard of Glass will be an improvised sharp tool. The Cold Steel Knife will be a pristine metallic dagger. The Frostbite Dirk will be a chilling short blade. The Obsidian Knife will be a dark volcanic dagger. The Heated Dagger will be a hot short blade. The Ember Shiv will be a smoldering knife. The Dragon Claw will be a reptilian short blade. The Hell's Tooth will be a demonic dagger.

Combat skills will be specifically tailored to each character class. For the Swordsman, Strong Attack will deliver a heavy physical strike. Slash will execute a basic sword technique. Double Slash will hit the enemy twice in succession. Wide Swing will deal physical damage to all enemies. Armor Break will damage an enemy and lower their defense. Blade Bash will strike with the flat of the blade with a chance to stun. Focus will increase the critical hit rate. Parry will greatly increase evasion. Sonic Wave will deal ranged wind damage. Wind Slash will perform a wind elemental physical attack. Power Break will damage an enemy and lower their attack. Mind Break will damage an enemy and lower their magic attack. Berserk Stance will increase attack but lower defense. Cross Cut will perform two intersecting slashes. Omnislash will execute rapid strikes against random targets.

For the Sorcerer, Fire, Fire II, and Fire III will deal varying levels of fire magic damage to one enemy. Ice, Ice II, and Ice III will deal varying levels of ice magic damage. Thunder, Thunder II, and Thunder III will deal varying levels of lightning magic damage. Flare will deal massive non-elemental magic damage. Freeze will deal ice damage with a high chance to stun. Shock will deal lightning damage with a chance to paralyze. Magic Drain will absorb mana from the target. Concentrate will drastically multiply magic attack for the next spell. Meteor Swarm will deal massive fire and earth damage to all enemies.

For the Priest, Heal, Heal II, and Heal III will restore varying amounts of health to an ally. Party Heal will restore health to the entire party. Cure Poison, Cure Blind, and Cure Silence will remove specific status ailments. Panacea will remove all negative status effects from one ally. Raise will revive a knocked-out ally. Holy Light will deal light magic damage to undead enemies. Protect will increase an ally's physical defense. Shell will increase an ally's magic defense. Regenerate will grant continuous health regeneration. Purify will damage an enemy and remove their buffs. Divine Intervention will fully heal the party and revive all dead allies.

For the Knight, Provoke will force enemies to target the player. Shield Bash will deal physical damage with a chance to stun. Cover will allow the knight to take damage in place of a low-health ally. Iron Defense will greatly increase defense. Guard Ally will protect a selected ally from all physical attacks. Shield Wall will increase the entire party's defense. Fortify will reduce damage taken by the user while skipping their turn. Sentinel will counter attack whenever hit physically. Justice Strike will deal damage based on the user's current defense. Heavy Charge will deliver a high damage but low-precision strike. Taunt will lower enemy attack but direct them to target the user. Unbreakable Will will grant immunity to status ailments. Phalanx will increase physical and magic defense for the user. Retribution will reflect a portion of physical damage back to the attacker. Castle of Stone will make the party immune to all damage for a turn.

For the Martial Artist, Punch and Kick will deal basic blunt damage. Triple Kick will hit a target multiple times. Roundhouse will hit all enemies with physical damage. Chakra will restore the user's health and cure basic ailments. Meditate will restore the user's tactical points. Pressure Point will ignore enemy defense. Earth Splitter will perform an earth elemental physical attack. Gale Palm will perform a wind elemental strike that pushes the turn order back. Spirit Wave will deal ranged non-elemental damage. Counter will provide a high chance to counter-attack physical hits. Leg Sweep will carry a chance to lower enemy agility. Fists of Fury will deliver rapid punches to one target. Chi Blast will use the player's health to deal massive damage. Seven Star Strike will deliver heavy hits with guaranteed criticals.

For the Magic Swordsman, Fire Blade, Ice Blade, Thunder Blade, and Wind Blade will add specific elements to physical attacks. Drain Blade will damage an enemy and restore the user's health. Aspir Blade will damage enemy mana to restore the user's mana. Magic Barrier will grant magic reflection to the user. Enchant Weapon will buff an ally's weapon with fire. Dispel Strike will remove enemy buffs on hit. Elemental Burst will consume all mana to deal damage. Arcane Slash will deal magic damage capable of critical hits. Spell Shield will grant immunity to the next magic spell received. Mystic Thrust will pierce magical defenses. Teleport Strike will execute a high evasion attack. Rune Breaker will deal massive non-elemental magic slash damage to foes.

For the Hunter, Aim will guarantee the next attack will hit and critically strike. Power Shot will deal high damage after a charge turn. Rapid Fire will shoot multiple arrows at random targets. Poison Arrow, Sleep Arrow, Blind Arrow, and Silence Arrow will inflict specific status ailments on hit. Arrow Rain will deal physical damage to all enemies. Eagle Eye will increase precision and critical rate. Beast Slayer will deal massive damage against animals. Piercing Shot will ignore enemy defense. Camouflage will lower the user's aggro. Trap Set will damage enemies who physically attack the user. Snipe will deal high damage to low-health enemies. Hail of Arrows will deal heavy damage to all enemies and lower their agility.

For the Bandit, Steal will temporarily reduce an enemy's core statistics while granting those same stat boosts to the user. Mug will deal physical damage while simultaneously draining the enemy's statistics. Sneak Attack will deal high damage if used at the start of battle. Poison Edge will add a toxic effect to the dagger. Sand Throw will inflict blindness on one enemy. Smoke Bomb will provide a high chance to flee battle or blind all enemies. Backstab will provide a high critical chance. Sprint will greatly increase agility. Gold Snatch will steal coins from the enemy. Venom Strike will deal heavy damage to poisoned targets. Shadow Step will drastically increase evasion. Dirty Trick will carry a chance to stun the enemy. Twin Daggers will hit twice. Lucky Strike will scale damage based on the luck stat. Assassinate will carry a chance to instantly kill non-boss enemies.

Combat will also be affected by various positive and negative status effects. The negative states will act as debuffs. Knockout will prevent characters from acting until revived. Poison will cause continuous damage at the end of every turn. Blind will greatly reduce physical attack precision. Silence will prevent the usage of all magic skills. Confusion will force characters to attack random targets. Sleep will prevent characters from acting until they take damage. Paralysis will force the character to skip their turn entirely. Stun will make characters flinch and lose their current turn. Bleed will deal physical damage over time and reduce healing received. Burn will deal fire damage over time and lower attack power. Freeze will prevent action until physical damage shatters the ice. Slow will reduce agility, filling the action gauge much slower. Curse will double mana costs and prevent health regeneration. Weakness will lower all elemental resistances. Fear will prevent the use of special tactical skills.

The positive states will act as buffs. Regenerate will restore a portion of health at the end of every turn. Haste will double agility to fill the action gauge faster. Protect will reduce physical damage taken. Shell will reduce magic damage taken. Focus will increase the critical hit rate. Magic Barrier will nullify the next magical attack received. Attack Up, Defense Up, Magic Up, and Agility Up will increase physical attack, physical defense, magic attack, and speed respectively. Evasion Up will add a chance to dodge physical attacks. Immortal will prevent health from dropping below one. Auto-Life will automatically revive a dead character once. Reflect will bounce magic spells back at the caster. Counter Stance will guarantee a counter-attack against physical hits.

Equipment options will further customize gameplay by providing stat boosts and elemental resistances. Shields will provide various defensive benefits. Small Shields and Round Shields will provide basic protection. Bucklers will be lightweight shields. Kite Shields, Iron Shields, and Steel Shields will provide larger coverage and metal protection. Mythril Shields will be made of lightweight magical metal. Gold Shields will be highly decorative. Wooden Lids will be improvised village shields. Hunter's Bucklers will not hinder movement. Bronze Shields will be durable desert alloys. Scale Guards will resist fire. Shell Bucklers will resist water. Ice Shields will reduce ice damage. Crystal Guards will reflect minor spells. Frost Shields will chill physical attackers. Dragon Shields and Flame Guards will reduce fire damage. Obsidian Shields will be unbreakable dark shields. The Aegis will be the ultimate shield preventing instant death.

Headgear will provide additional defense and stat bonuses when equipped. Leather Caps, Leather Helms, Iron Helmets, and Steel Helmets will provide varying degrees of physical protection. Mythril Helms will offer high defense with low weight. Full Helms will cover the entire head. Viking Helms will have horns. Dragon Helms will resist fire. Genji Helms will be legendary armor. Feathered Hats will be stylish. Magician's Hats will be pointy magic gear. Circlets will be simple metal bands. Ribbons will prevent status ailments. Bandanas will be worn by thieves. Turbans will protect against desert heat. Silk Hoods and Fur Hoods will provide climate and magic resistance. Ice Crowns and Salamander Coifs will provide elemental resistance. Royal Crowns will offer high overall stats.

Body armor will serve as the character's main defensive equipment to reduce overall incoming damage. Cloth Tunics and Traveler's Tunics will be basic clothing. Leather Armor and Hard Leather will be light protection. Iron Armor, Steel Armor, Plate Mail, and Heavy Mail will be heavy metal plating. Mythril Armor will be made of magical metal. Scale Mail will use flexible overlapping scales. Glacial Mail and Flame Mail will resist extreme temperatures. Dragon Armor will be the ultimate elemental resistance gear. Hunter's Vests and Ninja Suits will provide camouflage and agility. Cotton Robes, Silk Robes, Sorcerer's Robes, and Sage's Robes will provide magical protection for spellcasters. Winter Robes and Lava Robes will provide elemental resistance for casters.

Accessories will provide specific utility benefits. Rings of Protection, Power, Magic, Speed, and Life will increase their respective core statistics. Poison Charms, Silence Amulets, Blindness Glasses, Paralysis Talismans, and Sleep Earrings will prevent specific status ailments. Fire, Ice, Thunder, and Earth Rings will reduce elemental damage taken. Gold Rings and Lucky Coins will increase post-battle rewards. Warrior's Badges will offer counter-attacks. Scholar's Specs will reveal enemy stats. Knight's Crests will start battles with defensive buffs. Sniper's Eyes will greatly increase precision.

## 1.2 Objectives

### 1.2.1 General Objective

The primary objective of this project is to design and develop Chronicles of Arithmos: A 2D Role Playing Game with Dynamic Math Based Combat System and Adaptive Difficulty Scaling.

### 1.2.2 Specific Objectives

**A.** To implement battle mechanics.
This module will serve as the base structure for the custom math integration. It will include a time-based battle system, turn ordering, and character stat management for Health (HP), Mana (MP), and Tactical Points (TP). Additionally, the game will feature a tutorial sequence in the opening area where mentor characters will teach the basics of combat. To provide a continuous fail-safe for skill development, every town will feature at least one training hall where the player will be able to fight a training dummy to practice their combat and mathematical calculation skills. The user will interact with this module by inputting combat commands and managing their party's health, mana and tactical points during encounters.

**B.** To develop a Math Battle System plugin.
This module will serve as the core educational feature of the game. It will replace standard chance-based combat where random probability decides if an attack hits or misses with direct math challenges. The user will interact with this module by using a keyboard to solve generated math equations within a visual interface to successfully execute their in-game actions.

**C.** To implement a Level-Based Difficulty System.
This module will automatically adjust the complexity of the math equations based on the character's current level. It will change the amount of numbers in an equation, the types of math operators used, and the size of the numbers. To provide a risk-free environment for users to practice these mechanics, the game will feature designated Training Halls in every town. The user will interact with this module by solving math problems that dynamically increase in difficulty during normal gameplay, or by engaging a Training Dummy with infinite health. During these practice encounters, users can choose fixed-level dummies to practice specific equation types or a scaling dummy that matches their current party level, exiting the session at any time by clicking the "Escape" combat command.

**D.** To engineer a "Content-Aware" Timer System.
This module will serve as the time limit during combat. It will automatically calculate the amount of time given to the player based on the equation's complexity, the total number of digits, and the types of math operators used. The user will utilize this module by inputting their answers before the countdown expires.

**E.** To integrate an Enemy Auto-Scaling System.
This module will automatically adjust enemy statistics, such as health and attack power, to match the party's average level. This system will maintain combat difficulty across all geographical areas without requiring the manual creation of duplicate enemies. The user will engage with this module by fighting opponents whose strength dynamically scales to match their current progression.

**F.** To create a Performance-Based Reward Mechanism.
This module will act as the primary combat reward system by calculating the outcome of an action based on the speed and correctness of the provided answer. It will apply double damage (2.0x) for rapid and correct answers, normal damage for slow but correct answers, half damage (0.5x) for rapid but incorrect answers, and a missed attack for slow and incorrect answers. Users will engage with this module by inputting their math answers to receive direct combat results based on their performance.

**G.** To develop an Automatic Quest Generation system.
This module will automatically build side quests by checking the specific enemies and items found across all geographical areas the player has unlocked, creating new tasks without requiring them to be manually written. The user will engage with this module by interacting with Receptionist Mila to accept these generated tasks to hunt monsters or gather items.

**H.** To implement a Peer-to-Peer (P2P) Multiplayer Connection.
This module will provide the cooperative gameplay feature by establishing a direct connection between players without requiring them to create online accounts. Users will engage with this module by interacting with Portal Keeper Alden to generate a unique room code to host a game or to type in a code to join another player's game.

**I.** To integrate a Save System.
This module will record game progress into local files using automatic checkpoints when moving between maps and dedicated manual save slots. Users will engage with this module by manually saving their current progress into these slots and loading their previous data to continue playing.

**J.** To engineer a Level-Based Progression System.
This module will structure the educational flow of the game by managing the transition between gameplay stages and triggering story events. It will unlock harder math operators as the characters reach higher levels. The user will interact with this module by progressing through the Foundational, Intermediate, and Advanced stages, which will be seen in the scaling difficulty of the generated math equations during combat and the unlocking of new areas.

**K.** To implement a Mobile Input System.
This module will detect whether the user is accessing the game from a touch-screen device. When the math input window opens during combat, the system will display a Virtual Numeric Keypad directly on the screen, allowing the player to tap on-screen number buttons to submit their answers. Users will engage with this module by physically tapping the virtual keypad on supported mobile devices to input math answers during battle.

**L.** To integrate diverse Game Assets and Entities.
This module will serve as the main world building structure by providing a collection of pixel art maps, background music, sound effects, enemies, and equipment. Users will engage with this module by exploring distinct areas such as forests, deserts, tundras, and volcanos, listening to location specific audio, defeating the specific enemies found in those locations, and equipping different weapons, armor, and accessories.

## 1.3 Scope and Limitations

### 1.3.1 Scope

**A.** Standard Role-Playing Game (RPG) Combat Mechanics
The user interacts with this module by using a computer mouse or trackpad to click through visual combat menus (such as "Attack," "Skills," or "Items"), explicitly selecting actions to manage their party's health and mana during encounters. The scope of the proposed project includes core combat mechanics structured around:

**A.1** Time Progress Battle (TPB)
This module will feature a visible "Action Gauge" for each combatant that fills based on their Speed or Agility stat. The game will utilize a wait-based system to automatically freeze all of these action gauges the exact moment the math input window appears on the screen. This complete pause of the battle timers will guarantee that enemies cannot take their turns or attack while the player calculates and types their answer.

**A.2** Turn Structure
Players will know it is their turn when their character's visual Action Gauge completely fills up. During this phase, the user will interact with the module by using a computer mouse or trackpad to click through visual combat menus. They will choose from options such as "Attack," "Skills," or "Items" to manage their party's health and mana. Overall, combat will follow a specific order of steps: first, the player will select their action; second, the system will check their math answer; and third, the game will execute the chosen action.

**A.3** Resource Management
Players will manage three primary pools during combat. Health Points (HP) will determine how much damage a character can take before they are knocked out. Mana Points (MP) will be spent to cast magical spells. Tactical Points (TP) will be used to execute special combat skills.

**B.** Math Battle System Plugin.
The scope includes a core gameplay loop designed to build skills through repetition and reward. Upon encountering an enemy and selecting an action, the game switches to the Math Battle System. The player must solve the generated equation (scaled to their level) within the time limit to execute the action. The user interacts by utilizing the physical keyboard's number row or numpad to type whole-number answers into the screen and pressing the "Enter" key to attack before the visual timer runs out.

**C.** Level-Based Difficulty System
This module will automatically scale the complexity of the generated math equations based on the character's current level. The user will interact with this module by visually reading the generated equations on the screen and mentally calculating answers for problems that automatically increase in term counts and operator types as their character levels up. Furthermore, this module will govern the mathematical generation for safe-practice Training Halls located in every town. The user will interact with this feature by engaging a Training Dummy, which possesses infinite Health Points (HP) and serves solely as a target for calculation practice. The user can select a fixed-level dummy to generate equations locked to a specific difficulty tier, or a dynamic dummy that generates equations matching the party's current average level. Because the dummy cannot be defeated, the user will interact with the visual combat menu by clicking the "Escape" button to manually exit the training session. The mathematical difficulty will strictly follow a level-based progression:

**C.1** Player Levels 1-29 (Basics): The system will generate equations using Addition and Subtraction with two numbers. For example: 15 + 7.

**C.2** Player Levels 30-69 (Intermediate): The system will introduce Multiplication and Division operations. For example: 12 * 4.

**C.3** Player Levels 70-100 (Advanced): The system will generate three-part equations utilizing the full PEMDAS rule set (Parentheses, Exponents, Multiplication, Division, Addition, Subtraction). For example: (10 + 5) * 2.

**D.** "Content-Aware" Timer System:
This module will utilize a dynamic timer that calculates the allowed answer window based on the complexity of the generated equation, the total digit length, and the types of math operators used. It will award extra time bonuses for more complex operations, such as multiplication and division, or for equations containing larger values. If the timer reaches zero, the math input window will remain open on the screen and will still require an input to proceed. However, the system will automatically register any subsequently submitted answer as "slow," regardless of whether it is correct or incorrect. The user will interact with this module by visually monitoring a countdown bar during combat and typing their answers on a keyboard or touchscreen before the calculated time expires.

**E.** Enemy Auto-Scaling System
This module will function as a background process that automatically adjusts enemy statistics, specifically Health Points (HP), Attack power (ATK), Experience Points (EXP), and Gold rewards, in real-time based on the active party's average level. The user will interact with this module by engaging in combat sequences that are initiated by either walking their character into visible enemy sprites or by triggering random encounters while roaming the map. During these battles, the user will fight against opponents that automatically adjust their health and attack values to match the party.

**F.** Performance-Based Reward Mechanism
This module will feature a combat calculation step where the specific outcome of an action is directly determined by the input speed and correctness of the provided answer. The user will interact with this module by reacting with their keystrokes or screen taps to input their answers, receiving direct visual and sound feedback based on their final speed and correctness. This calculation will apply to all combat commands, including attacks and healing spells, resulting in the following outcomes based on the player's performance:

Correct and rapid answers will apply a 2.0x critical multiplier to the action's overall effect.
Correct but slow answers will execute the action at its normal, base value.
Incorrect but rapid answers will apply a 0.5x penalty to the action's overall effect.
Incorrect and slow answers will result in complete action nullification, causing the selected move to fail entirely.

**G.** To develop an Automatic Quest Generation system
This module will feature a quest engine that automatically scans the details of all areas the player has currently unlocked. It will utilize the specific enemies and items found within these accessible locations to generate relevant hunting and gathering objectives. These generated tasks will not impose a time limit, allowing the player to complete them at any point during their playthrough. If a quest is accepted, the system will record it in the Quests tab, where the player can check their quests progression. If a quest is rejected, the system will discard it and generate a new objective during the next interaction. The user will interact with this module by clicking on the map to move their character toward Receptionist Mila, clicking on her to open the interface, and clicking to accept or reject the automatically generated side quests.

**H.** Peer-to-Peer (P2P) Multiplayer Framework
The scope of the proposed project incorporates Networked Cooperative Gameplay using direct connections with text-based Room Codes. It allows drop-in combat where a joining player's party merges with the host's party dynamically. The user interacts with this module by interacting with an NPC and clicking the "Host Room" button to generate a "Room Code" for hosting a game, or typing a friend's code after clicking the "Join Room" button from the same NPC to join their game.

**I.** Save System
This module will record game progress by storing data as local files directly on the user's device. The system will feature 20 manual save slots and a dedicated Autosave function. If a player selects a save slot that already contains data, the system will completely overwrite the old file with the current progress. The Autosave function will also continuously overwrite its specific slot each time the player reaches a new checkpoint. The user will interact with this module by navigating to the "Save" screen via the main menu and clicking to select a specific slot to manually record their progress, or by clicking to move their character through map exits to trigger the automatic checkpoints.

**J.** Level-Based Progression
This module will establish the phases of player progression by providing specific rewards following successful combat and exploration. The user will interact with this module by participating in combat or completing quests to earn the following progression rewards:

**J.1** Experience Points (EXP): Accumulating EXP increases the character's level. The minimum obtainable EXP from a single low-level source is 10 points (Level 1 Slime), while the maximum possible gain from an endgame boss is capped at 99,999 points.

**J.2** Gold (Currency): Acquired via enemy defeats and quest completion. The minimum gold drop from a basic enemy is 5 G, while the maximum reward from a high-tier boss or elite quest is 50,000 G. This currency is used to buy new equipment and items from merchants.

**J.3** Story Milestones: Updates the "Story Progress", allowing the game to unlock higher-level maps.

**K.** Mobile Detection System and Virtual Numeric Keypad
This module will automatically detect if the user is on a mobile device. When the math input window opens during combat, the system will display a Virtual Numeric Keypad directly next to it on the screen. The user will interact with this module on supported mobile devices by physically tapping the on-screen number buttons and the "Submit" button to enter math answers.

**L.** Game Assets and Entities
This module will serve as the main world-building structure by providing a collection of pixel art maps, background music, sound effects, enemies, and equipment. The user will interact with this module by exploring distinct areas such as forests, deserts, tundras, and volcanos, defeating area specific enemies, and equipping various weapons, armor, and accessories. These assets will include:

**L.1** Character Roster
This includes the main characters that the player will talk to, fight alongside, or receive quests from to move the story forward

- Bron
- Martha
- Lily
- Kael
- Elara
- Garrick
- Sylas
- Isolde
- Thorne
- Lyra
- Fenrin
- Elder Tobias
- Merchant Oryn
- Receptionist Mila
- Bard Jareth
- Captain Valerius
- Professor Haze
- Innkeeper Gorm
- Blacksmith Rurik
- Widow Claire
- Farmer Ben
- Alchemist Vanya
- Librarian Estel
- Guard Captain Aris
- Fisherman Old Tom
- Street Urchin Pip
- Nobleman Caelus
- Priestess Anara
- Hunter Kaelen
- Portal Keeper Alden
- The Numeromancer

**L.2** Background NPCs
This includes the generic townspeople and villagers used to fill up the maps to make the game world feel alive and busy.

- Townsman 1-5 (Male)
- Townswoman 1-5 (Female)
- Playing Boy 1-2
- Playing Girl 1-2
- Market Shopper 1-3
- Tavern Patron 1-4
- Castle Guard 1-4
- Farmhand 1-2
- Stable Boy
- Washerwoman
- Street Sweeper
- Beggar 1-2
- Strolling Couple (Man/Woman)
- Academy Student 1-4
- Visiting Merchant
- Visiting Noble
- Lost Tourist
- Drunkard
- Gossiping Lady 1-2
- Running Messenger
- Sleeping Guard
- Fishing Boy
- Old Cat Lady
- Street Performer
- Watching Crowd Member

**L.3** Enemies
This includes the enemies that the user may encounter during their playthrough.

**L.3.1** Plains & Forest Biome:

- Slime
- Rat
- Bat
- Spider
- Hornet
- Wolf
- Bear
- Treant
- Goblin
- Goblin Archer
- Goblin Shaman
- Orc, Bandit
- Bandit Leader
- Crow
- Snake
- Fairy
- Mandrake
- Wild Boar
- Forest Golem

**L.3.2** Desert Biome:

- Sand Slime
- Scorpion
- Giant Scorpion
- Cactus
- Sand Worm
- Mummy
- Skeleton Warrior
- Skeleton Mage
- Desert Wolf
- Lamia, Basilisk
- Gargoyle
- Sand Golem
- Vulture, Sphinx
- Desert Rogue
- Ant Lion
- Dust Spirit
- Ancient Scarab
- Pharaoh's Guard

**L.3.3** Tundra & Frost Biome

- Ice Slime
- Snow Wolf
- Polar Bear
- Ice Bat
- Snow Spirit
- Yeti
- Ice Golem
- Crystal Spider
- Frost Giant
- White Tiger
- Corrupted Penguin
- Ice Drake
- Frozen Knight
- Winter Wisp
- Wendigo
- Frost Mage
- Glacial Turtle
- Snow Harpy
- Ice Elemental
- Fenrir

**L.3.4** Volcano & Fire Biome

- Magma Slime
- Fire Spirit
- Imp
- Demon
- Succubus
- Cerberus
- Lava Golem
- Fire Bat
- Salamander
- Dragon Hatchling
- Red Dragon
- Efreet
- Phoenix
- Iron Giant
- Dark Knight
- Cultist
- Fire Elemental
- Minotaur
- Chimera
- Demon Lord

**L.3.5** General & Dungeon

- Training Dummy
- Ghost
- Zombie
- Vampire
- Vampire Bat
- Mimic
- Shadow
- Will-o'-the-Wisp
- Animated Armor
- Flying Sword
- Magic Pot
- Gazer
- Ogre
- Troll
- Warlock
- Necromancer
- Reaper
- Chaos Cloud
- Number Eater
- Equation Spirit
- The Unknown

**L.4** Items
This includes the items that the user may receive from either buying from shops, completing quests or being dropped as loot from enemies during their playthrough.

**L.4.1** Consumable Items (Recovery & Utility)

- Potion
- Hi-Potion
- Full Potion
- Magic Water
- Hi-Magic Water
- Elixir, Antidote
- Eye Drops
- Echo Herb
- Stimulant
- Potent Stimulant
- Panacea
- Dispel Herb
- Escape Rope
- Repel Spray

**L.4.2** Stat Boosters (Permanent Upgrades)

- HP Up
- MP Up
- Strength Seed
- Defense Seed
- Magic Seed
- Agility Seed
- Luck Seed
- Skill Book

**L.4.3** Monster Loot & Drops — Plains/Forest

- Green Gel
- Rat Tail
- Bat Wing
- Sticky Web
- Insect Wing
- Wolf Pelt
- Bear Claw
- Living Branch
- Goblin Cloth
- Shaman Bead
- Orc Tusk
- Stolen Coin Purse
- Shiny Feather
- Snake Skin
- Fairy Dust
- Mandrake Root
- Boar Meat
- Ancient Bark

**L.4.4** Monster Loot & Drops — Desert

- Yellow Gel
- Scorpion Stinger
- Cactus Flower
- Sand Essence
- Old Bandage
- Bone Fragment
- Skull
- Dry Fur
- Snake Scale
- Petrified Eye
- Stone Wing
- Sandstone Block
- Vulture Beak
- Riddle Tablet
- Scarab Shell
- Golden Fragment

**L.4.5** Monster Loot & Drops — Tundra

- Blue Gel
- White Fur
- Thick Hide
- Ice Crystal
- Snowflake Core
- Yeti Horn
- Permafrost Shard
- Crystal Leg
- Frost Metal
- Corrupted Feather
- Drake Scale
- Cold Wisp
- Frozen Heart
- Ice Turtle Shell
- Harpy Feather
- Wolf Fang

**L.4.6** Monster Loot & Drops — Volcano

- Red Gel
- Ember
- Imp Wing
- Demon Horn
- Succubus Cloth
- Hellhound Fang
- Obsidian Shard
- Fire Gland
- Dragon Tooth
- Red Scale
- Djinn Lamp
- Phoenix Ash
- Iron Scraps
- Dark Armor Piece
- Forbidden Page
- Chimera Tail
- Infernal Core

**L.4.7** Monster Loot & Drops — General

- Ectoplasm
- Rotten Flesh
- Vampire Fang
- Unknown Fluid
- Spirit Dust
- Haunted Metal
- Ceramic Shard
- Evil Eye
- Ogre Club
- Magic Powder
- Tattered Robe
- Chaos Mote
- Arithmetic Essence
- Void Fragment

**L.5** Class Roster:

- Swordsman
- Sorcerer
- Priest
- Knight
- Martial Artist
- Magic Swordsman
- Hunter
- Bandit

**L.6** Weapons

**L.6.1** Swordsman (Swords)

- Long Sword
- Woodcutter's Blade
- Wolf Fang Sword
- Forest Cutter
- Bandit's Edge
- Verdant Blade
- Sand Scimitar
- Scorpion Tail
- Dune Blade
- Sun-Scorched Sword
- Ancient Khopesh
- Ice Brand
- Glacial Edge
- Frostbite Sword
- Crystal Saber
- Blizzard Blade
- Magma Blade
- Dragon Bone Sword
- Infernal Edge
- Flame Tongue
- Phoenix Feather Sword

**L.6.2** Sorcerer (Staves)

- Oak Staff
- Briar Rod
- Druid's Staff
- Faerie Wand
- Root Staff
- Nature's Call
- Sandstone Rod
- Mirage Staff
- Cobra Head Staff
- Sun Rod
- Sphinx Cane
- Icicle Rod
- Snowflake Staff
- Hailstorm Wand
- Permafrost Cane
- Frozen Core Staff
- Ember Rod
- Ash Staff
- Dragon Breath Wand
- Core Magma Staff
- Hellfire Rod

**L.6.3** Priest (Maces)

- Wooden Mace
- Oak Club
- Spirit Mace
- Blessed Branch
- Mossy Hammer
- Guardian's Cudgel
- Golden Scepter
- Sandstone Hammer
- Sun Disc Mace
- Tomb Guardian Club
- Sacred Ankh
- Crystal Mace
- Hailstone Hammer
- Frozen Scepter
- Polar Club
- Divine Ice Mace
- Obsidian Mace
- Lava Rock Hammer
- Cleansing Fire Club
- Forge Master's Hammer
- Phoenix Down Mace

**L.6.4** Knight (Spears)

- Short Spear
- Hunter's Spear
- Boar Tusk Lance
- Forest Guard Pike
- Wooden Pike
- Leaf-Blade Spear
- Scorpion Stinger
- Desert Pike
- Bronze Lance
- Sandpiercer
- Pharaoh's Guard
- Ice Shard Lance
- Glacier Pike
- Tundra Harpoon
- Frost Wyrm Spear
- Frozen Needle
- Magma Pike
- Dragon Scale Lance
- Red Steel Spear
- Obsidian Lance
- Hellfire Harpoon

**L.6.5** Martial Artist (Claws)

- Leather Gloves
- Bear Claws
- Wolf Paws
- Sharp Thorns
- Tree Bark Knuckles
- Wild Beast Fists
- Scorpion Pincers
- Sandstone Gauntlets
- Cactus Spines
- Mummy Wraps
- Golden Knuckles
- Ice Picks
- Yeti Fists
- Frostbite Gloves
- Crystal Talons
- Polar Paws
- Salamander Claws
- Dragon Fangs
- Magma Fists
- Burning Knuckles
- Demon Hands

**L.6.6** Magic Swordsman (Enchanted Blades)

- Rapier
- Wind Blade
- Leaf Cutter
- Elven Rapier
- Swift Blade
- Whisper Edge
- Mirage Rapier
- Heatwave Saber
- Dust Devil Blade
- Golden Epee
- Sun-Strike Sword
- Chill Spike
- Frozen Needle
- Aurora Blade
- Ice Queen's Rapier
- Zero Kelvin
- Searing Saber
- Molten Rapier
- Blaze Edge
- Phoenix Tail
- Volcanic Spike

**L.6.7** Hunter (Bows)

- Short Bow
- Oak Bow
- Hunter's Bow
- Ranger's Crossbow
- Vine Bow
- Elven Bow
- Bone Bow
- Sandstone Crossbow
- Scorpion Recurve
- Desert Wind Bow
- Golden Arrow
- Ice Crystal Bow
- Frostbite Crossbow
- Mammoth Ivory Bow
- Blizzard String
- Glacial Shot
- Ash Wood Bow
- Flame String
- Magma Rock Crossbow
- Dragon Bone Bow
- Phoenix Fire Bow

**L.6.8** Bandit (Daggers)

- Knife
- Rusty Shiv
- Hunter's Knife
- Poison Tip
- Thief's Shank
- Forest Tooth
- Curved Dagger
- Sand Shiv
- Scorpion Barb
- Tomb Blade
- Golden Dagger
- Icicle Shiv
- Frozen Dagger
- Shard of Glass
- Cold Steel Knife
- Frostbite Dirk
- Obsidian Knife
- Heated Dagger
- Ember Shiv
- Dragon Claw
- Hell's Tooth

**L.7** Skills

**L.7.1** Swordsman

- Strong Attack
- Slash
- Double Slash
- Wide Swing
- Armor Break
- Blade Bash
- Focus
- Parry
- Sonic Wave
- Wind Slash
- Power Break
- Mind Break
- Berserk Stance
- Cross Cut
- Omnislash

**L.7.2** Sorcerer

- Fire
- Fire II
- Fire III
- Ice
- Ice II
- Ice III
- Thunder
- Thunder II
- Thunder III
- Flare
- Freeze
- Shock
- Magic Drain
- Concentrate
- Meteor Swarm

**L.7.3** Priest

- Heal
- Heal II
- Heal III
- Party Heal
- Cure Poison
- Cure Blind
- Cure Silence
- Panacea
- Raise
- Holy Light
- Protect
- Shell
- Regenerate
- Purify
- Divine Intervention

**L.7.4** Knight

- Provoke
- Shield Bash
- Cover
- Iron Defense
- Guard Ally
- Shield Wall
- Fortify
- Sentinel
- Justice Strike
- Heavy Charge
- Taunt
- Unbreakable Will
- Phalanx
- Retribution
- Castle of Stone

**L.7.5** Martial Artist

- Punch
- Kick
- Triple Kick
- Roundhouse
- Chakra
- Meditate
- Pressure Point
- Earth Splitter
- Gale Palm
- Spirit Wave
- Counter
- Leg Sweep
- Fists of Fury
- Chi Blast
- Seven Star Strike

**L.7.6** Magic Swordsman

- Fire Blade
- Ice Blade
- Thunder Blade
- Wind Blade
- Drain Blade
- Aspir Blade
- Magic Barrier
- Enchant Weapon
- Dispel Strike
- Elemental Burst
- Arcane Slash
- Spell Shield
- Mystic Thrust
- Teleport Strike
- Rune Breaker

**L.7.7** Hunter

- Aim
- Power Shot
- Rapid Fire
- Poison Arrow
- Sleep Arrow
- Blind Arrow
- Silence Arrow
- Arrow Rain
- Eagle Eye
- Beast Slayer
- Piercing Shot
- Camouflage
- Trap Set
- Snipe
- Hail of Arrows

**L.7.8** Bandit

- Steal
- Mug
- Sneak Attack
- Poison Edge
- Sand Throw
- Smoke Bomb
- Backstab
- Sprint
- Gold Snatch
- Venom Strike
- Shadow Step
- Dirty Trick
- Twin Daggers
- Lucky Strike
- Assassinate

**L.8** Status Effects

**L.8.1** Negative States (Debuffs)

- Knockout
- Poison
- Blind
- Silence
- Confusion
- Sleep
- Paralysis
- Stun
- Bleed
- Burn
- Freeze
- Slow
- Curse
- Weakness
- Fear

**L.8.2** Positive States (Buffs)

- Regenerate
- Haste
- Protect
- Shell
- Focus
- Magic Barrier
- Attack Up
- Defense Up
- Magic Up
- Agility Up
- Evasion Up
- Immortal
- Auto-Life
- Reflect
- Counter Stance

**L.9** Armor & Accessory

**L.9.1** Shields
Equippable only by Knights, Swordsmen, Priests

- Small Shield
- Buckler
- Round Shield
- Kite Shield
- Iron Shield
- Steel Shield
- Mythril Shield
- Gold Shield
- Wooden Lid
- Hunter's Buckler
- Bronze Shield
- Scale Guard
- Shell Buckler
- Ice Shield
- Crystal Guard
- Frost Shield
- Dragon Shield
- Flame Guard
- Obsidian Shield
- Aegis

**L.9.2** Headgear

- Leather Cap
- Iron Helmet
- Steel Helmet
- Mythril Helm
- Full Helm
- Viking Helm
- Dragon Helm
- Genji Helm
- Leather Helm
- Feathered Hat
- Magician's Hat
- Circlet
- Ribbon
- Bandana
- Turban
- Silk Hood
- Fur Hood
- Ice Crown
- Salamander Coif
- Royal Crown

**L.9.3** Body Armor

- Cloth Tunic
- Leather Armor
- Iron Armor
- Steel Armor
- Mythril Armor
- Plate Mail
- Heavy Mail
- Scale Mail
- Glacial Mail
- Flame Mail
- Dragon Armor
- Traveler's Tunic
- Hard Leather
- Hunter's Vest
- Ninja Suit
- Cotton Robe
- Silk Robe
- Sorcerer's Robe
- Winter Robe
- Lava Robe
- Sage's Robe

**L.9.4** Accessories

- Ring of Protection
- Ring of Power
- Ring of Magic
- Ring of Speed
- Ring of Life
- Poison Charm
- Silence Amulet
- Blindness Glasses
- Paralysis Talisman
- Sleep Earring
- Fire Ring
- Ice Ring
- Thunder Ring
- Earth Ring
- Gold Ring
- Lucky Coin
- Warrior's Badge
- Scholar's Specs
- Knight's Crest
- Sniper's Eye

**L.10** Background Music (BGM)

**L.10.1** Battle & Boss Themes

- Battle1
- Battle2
- Battle3
- Battle4
- Battle5
- Battle6
- Battle7
- Boss1
- Boss2
- Boss3
- Boss4
- Boss5

**L.10.2** Towns & Safe Zones

- Town1
- Town2
- Town3
- Town4
- Town5
- Town6
- Town7
- Castle1
- Castle2

**L.10.3** Exploration (Overworld & Dungeons)

- Field1
- Field2
- Field3
- Field4
- Dungeon1
- Dungeon2
- Dungeon3
- Dungeon4
- Dungeon5
- Dungeon6
- Dungeon7
- Dungeon8
- Ship1
- Ship2
- Ship3

**L.10.4** Story & Cutscenes

- Scene1
- Scene2
- Scene3
- Scene4
- Scene5
- Scene6
- Theme1
- Theme2
- Theme3
- Theme4
- Theme5
- Theme6

### 1.3.2 Limitations

**A.** Mathematical Scope and Generation Limits
The system does not currently support advanced algebra, calculus, or non-integer results (fractions/decimals). To maintain combat flow, the math generator is strictly restricted so that all division problems calculate to exact whole numbers, avoiding fractions or decimals entirely. Furthermore, the system imposes a hard limit on the multiplier and the divisor (the second number in any multiplication or division problem), capping them at a range of 1 to 20. This specific numerical limitation applies universally to every combat encounter, including multi-part equations at higher levels.

**B.** Tactile Input Disparity
While the inclusion of a Virtual Numeric Keypad enables mobile playability, the lack of tactile feedback on touchscreens may result in reduced input velocity compared to physical keyboards. Consequently, users on mobile devices may experience a slight disadvantage in high-level "Speed Math" calculations where millisecond reaction times are critical.

**C.** Input Method
The input system utilizes the standard number row or numpad of a physical keyboard. On mobile and touch-screen devices, the system provides a Virtual Numeric Keypad as the primary input method. This limitation means that input speed may vary depending on the device used.

**D.** Asset Fidelity
The project utilizes standard 2D pixel art assets and does not focus on high-fidelity 3D rendering or physics simulations.

**E.** Peer-to-Peer Latency Sensitivity
The multiplayer feature relies on the stability of the host's internet connection. As the system utilizes a direct P2P handshake, high latency or packet loss on the host side may result in desynchronization of the Math Timer for connected clients.

**F.** Volatile Session Architecture
The multiplayer system is stateless (no central dedicated server). If the host application is terminated, the game session dissolves immediately for all connected clients; state recovery for guest clients is not supported in this version.

## REFERENCES

[1] B. Bruckman, "The 'Chocolate-Covered Broccoli' Problem," International Journal of Game-Based Learning, vol. 3, no. 2, pp. 1-15, 2013. [Online]. Available: <https://www.google.com/search?q=https://www.researchgate.net/publication/220968132_The_Chocolate-Covered_Broccoli_Problem>

[2] M. Csikszentmihalyi, Flow: The Psychology of Optimal Experience. New York, NY: Harper & Row, 1990. [Online]. Available: <https://www.HarperCollins.com/products/flow-mihaly-csikszentmihalyi>

[3] F. C. Richardson and R. M. Suinn, "The Mathematics Anxiety Rating Scale: Psychometric data," Journal of Counseling Psychology, vol. 19, no. 6, pp. 551–554, 1972. [Online]. Available: <https://www.google.com/search?q=https://psycnet.apa.org/record/1973-09757-001>

[4] M. H. Ashcraft, "Math anxiety: Personal, educational, and cognitive consequences," Current Directions in Psychological Science, vol. 11, no. 5, pp. 181–185, 2002. [Online]. Available: <https://journals.sagepub.com/doi/10.1111/1467-8721.00196>

[5] J. P. Gee, What Video Games Have to Teach Us About Learning and Literacy. New York, NY: Palgrave Macmillan, 2003. [Online]. Available: <https://www.google.com/search?q=https://link.springer.com/book/10.1007/978-1-137-52660-3>
