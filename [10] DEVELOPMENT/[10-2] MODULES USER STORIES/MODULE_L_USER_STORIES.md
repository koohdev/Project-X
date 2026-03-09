# Module L: Game Assets and Entities — User Stories

> The databasing of all world-building structures: visual maps, BGM, SFX, class parameters, items, enemies, and skills required to bring the narrative and systems to life.

---

## US-L-001: Character Roster Access

**As a** player,
**I want** to encounter and recruit from a roster of 30+ main story characters and companions throughout my journey,
**so that** I have a diverse selection of party members to build my team with.

**Priority**: High

**Acceptance Criteria**:

- [ ] At least 30 main story characters and companions are implemented in the game database.
- [ ] Characters are introduced through story events, quests, or specific locations.
- [ ] Each character has unique sprites, portraits, stats, and a defined class.
- [ ] Recruited characters are available for party selection.

---

## US-L-002: NPC Population

**As a** player,
**I want** to see townspeople, guards, and merchants populating the game world,
**so that** the environments feel alive, immersive, and populated.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] Towns and hubs are populated with background NPCs (townspeople, guards).
- [ ] Merchant NPCs offer buy/sell functionality for items and equipment.
- [ ] NPCs have dialogue when interacted with.
- [ ] NPC placement is contextually appropriate (guards at gates, merchants in shops).

---

## US-L-003: Biome-Specific Enemies

**As a** player,
**I want** to encounter different enemies depending on which biome I am exploring,
**so that** each region feels unique and offers varied combat experiences.

**Priority**: High

**Acceptance Criteria**:

- [ ] Plains & Forest Biome has its own dedicated set of enemies.
- [ ] Desert Biome has its own dedicated set of enemies.
- [ ] Tundra & Frost Biome has its own dedicated set of enemies.
- [ ] Volcano & Fire Biome has its own dedicated set of enemies.
- [ ] General & Dungeon areas have their own dedicated set of enemies.
- [ ] Each enemy has unique sprites, stats, drop tables, and behavior.

---

## US-L-004: Consumable Items

**As a** player,
**I want** access to consumable items (recovery potions, utility items) that I can use during and outside of battle,
**so that** I can manage my party's health and resources strategically.

**Priority**: High

**Acceptance Criteria**:

- [ ] Recovery items restore HP, MP, or cure status effects when used.
- [ ] Utility items provide tactical advantages (e.g., escape tools, buffs).
- [ ] All consumable items are stored in the player's inventory with quantity tracking.
- [ ] Consumable items can be purchased from merchant NPCs or dropped by enemies.

---

## US-L-005: Stat Booster Items

**As a** player,
**I want** to find permanent stat booster items,
**so that** I can enhance my characters beyond their natural leveling growth.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] Stat booster items permanently increase a specific stat (ATK, DEF, SPD, etc.).
- [ ] Each booster is a one-time-use item consumed on application.
- [ ] Stat increases are reflected immediately in the character's status screen.
- [ ] Boosters are obtainable through rare drops, quests, or hidden locations.

---

## US-L-006: Monster Loot and Drops

**As a** player,
**I want** enemies to drop loot items when defeated,
**so that** I can collect materials for quests, crafting, or selling.

**Priority**: High

**Acceptance Criteria**:

- [ ] Each enemy type has a defined drop table with associated drop rates.
- [ ] Loot items are added to the player's inventory after battle.
- [ ] Drop tables include both common and rare items.
- [ ] Dropped items are displayed in the post-battle results screen.

---

## US-L-007: Class System (8 Classes)

**As a** player,
**I want** characters to belong to one of 8 distinct classes, each with unique strengths and equipment,
**so that** I can build a diverse party with complementary roles and abilities.

**Priority**: High

**Acceptance Criteria**:

- [ ] The following 8 classes are implemented: Swordsman, Sorcerer, Priest, Knight, Martial Artist, Magic Swordsman, Hunter, Bandit.
- [ ] Each class has unique base stats and growth curves.
- [ ] Each class has access to its own dedicated weapon type.
- [ ] Each class has unique combat skills (per L.7).
- [ ] Class information is viewable in the status/party menu.

---

## US-L-008: Class-Specific Weapons (160+)

**As a** player,
**I want** each class to have a wide variety of class-specific weapons available (160+ total),
**so that** I can upgrade my characters' equipment throughout the game.

**Priority**: High

**Acceptance Criteria**:

- [ ] Swordsman: Uses Swords.
- [ ] Sorcerer: Uses Staves.
- [ ] Priest: Uses Maces.
- [ ] Knight: Uses Spears.
- [ ] Martial Artist: Uses Claws.
- [ ] Magic Swordsman: Uses Enchanted Blades.
- [ ] Hunter: Uses Bows.
- [ ] Bandit: Uses Daggers.
- [ ] A total of 160+ unique weapons exist across all classes.
- [ ] Weapons have varying stats (ATK, special effects) and can be equipped from the menu.

---

## US-L-009: Class-Specific Skills

**As a** player,
**I want** each class to have dedicated combat skills tailored to their role,
**so that** each class plays differently in battle and offers unique tactical options.

**Priority**: High

**Acceptance Criteria**:

- [ ] Each of the 8 classes has a unique set of skills.
- [ ] Skills are learned at specific levels or through story progression.
- [ ] Skills consume MP or TP to use.
- [ ] Skill effects are appropriate to the class fantasy (e.g., Priests heal, Sorcerers cast AoE).

---

## US-L-010: Debuff Status Effects

**As a** player,
**I want** enemies to be able to inflict debuff status effects on my characters (and vice versa),
**so that** battles have tactical depth and require strategic counterplay.

**Priority**: High

**Acceptance Criteria**:

- [ ] Damage-over-Time (DoT) effects are implemented: Poison, Bleed, Burn.
- [ ] DoT effects deal damage at defined intervals (e.g., each turn).
- [ ] Action restriction effects are implemented: Sleep, Paralysis, Freeze.
- [ ] Restriction effects prevent the afflicted character from acting for their duration.
- [ ] Status effect icons are displayed on the battle HUD next to affected characters.
- [ ] Status effects have a defined duration or can be cured with items/skills.

---

## US-L-011: Buff Status Effects

**As a** player,
**I want** to apply buff status effects to my characters,
**so that** I can temporarily enhance performance or gain defensive advantages.

**Priority**: High

**Acceptance Criteria**:

- [ ] Stat booster buffs temporarily increase ATK, DEF, SPD, or other stats.
- [ ] Auto-Life revival logic: If a character with Auto-Life is KO'd, they automatically revive with partial HP.
- [ ] Magic Reflection logic: Incoming magic attacks are reflected back to the caster.
- [ ] Buff icons are displayed on the battle HUD next to buffed characters.
- [ ] Buffs have a defined duration (number of turns or until a trigger event).

---

## US-L-012: World Maps and Biomes

**As a** player,
**I want** to explore visually distinct world maps across 5 biomes,
**so that** the game world feels expansive, varied, and immersive.

**Priority**: High

**Acceptance Criteria**:

- [ ] At least 5 visually distinct biomes are implemented (Plains/Forest, Desert, Tundra/Frost, Volcano/Fire, General/Dungeon).
- [ ] Each biome has unique tilesets, environmental art, and map layouts.
- [ ] Maps are navigable with clear entry/exit points and transitions.
- [ ] Biomes are unlocked progressively through story milestones (per Module J).

---

## US-L-013: Background Music (BGM) and Sound Effects (SFX)

**As a** player,
**I want** each area and battle to have appropriate background music and sound effects,
**so that** the game is immersive and engaging on an auditory level.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] Each biome/town/dungeon has dedicated background music.
- [ ] Battle scenes have dedicated combat BGM.
- [ ] Sound effects are present for attacks, skills, item usage, UI navigation, and level-ups.
- [ ] BGM transitions smoothly between exploration and combat.
