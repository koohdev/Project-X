# Appendix D: Screen Design

The following tables present the user interface (UI) specifications and visual layouts of *Chronicles of Arithmos: A 2D Role-Playing Game with Dynamic Math-Based Combat System and Adaptive Difficulty Scaling*. Each screen entry details the screen number, formal screen name, target user role, operational narrative overview, and visual mockup layout in accordance with the Dominican College of Tarlac (DCT) College of Computer Studies (CCS) Capstone Manual.

---

| Screen No.: | Screen 1 |
| :--- | :--- |
| **Screen Name:** | Title Screen Interface |
| **Target User / Role:** | Young Learner / Player / General User |
| **Narrative Overview:** | The Title Screen serves as the primary gateway and initial landing interface for *Chronicles of Arithmos*. It displays the official game title banner centered against a high-contrast fantasy castle background featuring a holy sword embedded in stone under a vibrant sky. A centered modal command box with deep blue framing (`#005385`) and dark translucency provides the primary navigation options: **New Game** (initializes a fresh campaign session and opens the character naming workflow), **Continue** (opens the saved games browser to restore recorded progress), **Options** (navigates to system configuration), and **Exit** (closes the standalone desktop executable). Users can interact via physical keyboard arrow keys with Z (confirm) and X (cancel), mouse clicks, or direct touchscreen taps. |
| **Screen Layout:** | ![Screen 1: Title Screen Interface](1%20Title%20Screen.PNG) |

---

| Screen No.: | Screen 2-1 |
| :--- | :--- |
| **Screen Name:** | System Options Menu (General & Audio Settings) |
| **Target User / Role:** | Young Learner / Player |
| **Narrative Overview:** | The System Options Menu (Page 1) allows players to configure operational behaviors and audiovisual volumes to suit their local hardware environment. Rendered as a centered modal dialog with a blurred background overlay, this menu contains customizable toggles and sliders: **Always Dash** (toggles automatic party running in exploration maps), **Command Remember** (retains cursor position in combat submenus), **Touch UI** (enables or disables on-screen touch overlays and dedicated touch buttons for mobile/tablet devices), **Show HP Gauge** (toggles visual health bars above battlers during combat), **BGM Volume** (adjusts background music volume, set by default to 60%), **BGS Volume** (adjusts ambient background sound volume, set to 40%), and **ME Volume** (adjusts music effect stingers, set to 40%). A down arrow indicator signifies additional settings, a dedicated Back arrow button is anchored at the top-right corner for touch users, and a bottom hotkey bar indicates `Z:Select` and `X:Back`. |
| **Screen Layout:** | ![Screen 2-1: System Options Menu - Page 1](2%20-%201%20Options.PNG) |

---

| Screen No.: | Screen 2-2 |
| :--- | :--- |
| **Screen Name:** | System Options Menu (Sound Effect Setting) |
| **Target User / Role:** | Young Learner / Player |
| **Narrative Overview:** | The System Options Menu (Page 2) provides granular acoustic adjustment for tactical sound effects. Scrolling down from the primary options menu reveals the **SE Volume** setting (configured to 40%). This control regulates the acoustic feedback for arithmetic inputs, countdown alert chimes, menu confirmations, critical hit sound cues, and monster damage impacts. Seamless real-time volume adjustments allow learners to maintain auditory clarity during classroom or home study sessions without external audio distortion. |
| **Screen Layout:** | ![Screen 2-2: System Options Menu - Sound Effect Setting](2%20-%202%20Options.PNG) |

---

| Screen No.: | Screen 3 |
| :--- | :--- |
| **Screen Name:** | Continue and Load Game Interface |
| **Target User / Role:** | Young Learner / Player |
| **Narrative Overview:** | The Continue and Load Game Interface allows players to retrieve and restore previously saved game states from local device storage without requiring network authentication. The top header displays the contextual query *"Which file would you like to load?"*. The selection list features a dedicated **Autosave** slot (automatically updated whenever the party transitions between regional map boundaries) alongside twenty manual save slots (e.g., **File 1**, **File 2**, **File 3**, **File 4**). Each populated slot presents rich metadata including thumbnail sprites of active party members (e.g., protagonist Alpha and companion Elara) and total accumulated playtime (e.g., `00:02:08` or `00:01:25`). A scrollable vertical viewport accommodates all twenty save slots, while an on-screen return button and standard keyboard hotkeys (`Z:Select`, `X:Back`) provide intuitive navigation. |
| **Screen Layout:** | ![Screen 3: Continue and Load Game Interface](3%20Continue%20or%20Load%20Screen.PNG) |

---

| Screen No.: | Screen 4 |
| :--- | :--- |
| **Screen Name:** | Protagonist Character Name Input Interface |
| **Target User / Role:** | Young Learner / Player |
| **Narrative Overview:** | The Protagonist Character Name Input Interface is presented upon starting a new campaign, allowing learners to personalize their lead hero. The top card displays the animated 2D anime-style face portrait of the young swordsman protagonist alongside an editable text entry field with underline placeholders and an active typing cursor (defaulting to *"Alpha"*). The lower pane renders a comprehensive 9x8 virtual alphanumeric keyboard grid containing uppercase letters (A–Z), lowercase letters (a–z), numeric digits (0–9), punctuation, and arithmetic symbols (`+`, `-`, `*`, `/`, `=`, `@`, `^`). Dedicated functional buttons include **Page** (for character set cycling) and **OK** (for name confirmation). This interface provides full dual-input compatibility, accepting direct typing from physical keyboards as well as touch tap inputs on touchscreen tablets. |
| **Screen Layout:** | ![Screen 4: Protagonist Character Name Input Interface](4%20Name%20Input%20Screen.PNG) |

---

| Screen No.: | Screen 5 |
| :--- | :--- |
| **Screen Name:** | Overworld & Interior Exploration Environment |
| **Target User / Role:** | Young Learner / Player |
| **Narrative Overview:** | The Overworld and Interior Exploration Environment displays the 2D top-down grid exploration perspective of *Chronicles of Arithmos*. The screen illustrates the detailed interior of the starting Adventurer Lodge / Headquarters rendered with custom pixel art tilesets. The layout features distinct architectural zones: a private hero bedroom (containing protagonist Alpha, a bed, desk with research books, mirror, potion shelf, and wardrobe), a tiled bathroom suite with a swimming bath and plumbing amenities, a spacious grand study with hardwood flooring, a stone hearth fireplace, a grandfather clock, floor-to-ceiling bookshelves, and a massive study table arranged with ancient scrolls, manuscripts, letters with wax seals, hourglasses, and an ink quill, as well as an adjoining kitchen area. Players navigate their avatar using physical directional keys (WASD / Arrows) or touch tap pathfinding. An anchored hamburger menu button at the top-right corner allows mobile users to open the main pause menu seamlessly without a keyboard Escape key. |
| **Screen Layout:** | ![Screen 5: Overworld & Interior Exploration Environment](5%20Game%20Example.PNG) |

---

| Screen No.: | Screen 6 |
| :--- | :--- |
| **Screen Name:** | Main System Pause Menu |
| **Target User / Role:** | Young Learner / Player |
| **Narrative Overview:** | The Main System Pause Menu serves as the central operational hub for character growth, party management, and gameplay configuration during field exploration. Accessed via the Escape/X key or the top-right touch menu icon, the interface is split into structured functional panels over a darkened map backdrop. The left panel displays a summary card for active party members, featuring the character face portrait, name (*"Alpha"*), assigned class (*"Swordsman"*), character level (*"Lv 1"*), and real-time vital gauges for Health Points (HP `544`), Magic Points (MP `41`), and Tactical Points (TP `0`). The right panel houses the vertical primary command list: **Item**, **Skill**, **Equip**, **Status**, **Formation**, **Quests**, **Options**, **Save**, and **Exit**. The bottom-right window tracks the player's accumulated Gold currency balance (`G 0`), while the bottom navigation bar displays action prompts (`Z:Select`, `X:Back`). |
| **Screen Layout:** | ![Screen 6: Main System Pause Menu](6%20Pause%20Menu.PNG) |

---

| Screen No.: | Screen 7 |
| :--- | :--- |
| **Screen Name:** | Inventory & Item Management Menu |
| **Target User / Role:** | Young Learner / Player |
| **Narrative Overview:** | The Inventory and Item Management Menu enables players to inspect, organize, and utilize consumable supplies, combat utilities, weapons, and protective armor. The top horizontal pane serves as a contextual help box that displays comprehensive item descriptions, recovery values, and operational effects. Directly beneath, an intuitive icon-driven category bar partitions the inventory into nine distinct classifications: **Field Items** (potion pouch icon), **Combat Consumables** (bomb icon), **Magical Recovery** (crystal orb icon), **Weapons** (sword icon), **Shields** (shield icon), **Headgear** (helmet icon), **Body Armor** (tunic icon), **Accessories** (ring icon), and **Key / Quest Items** (golden key icon). The lower split pane lists acquired items with numerical inventory counters. Players navigate between categories using `<<` and `>>` hotkeys or touch swipe gestures, confirming selections with `Z:Select` and canceling via `X:Back`. |
| **Screen Layout:** | ![Screen 7: Inventory & Item Management Menu](7%20Items%20Menu.PNG) |

---

| Screen No.: | Screen 8 |
| :--- | :--- |
| **Screen Name:** | Character Skills & Abilities Management Menu |
| **Target User / Role:** | Young Learner / Player |
| **Narrative Overview:** | The Character Skills and Abilities Management Menu allows players to review unlocked martial skills, tactical abilities, and class-specific spells. The top window displays contextual skill explanations detailing tactical damage output and status effects. The middle-left card displays active character data (portrait, name *"Alpha"*, class *"Swordsman"*, Lv 1, HP `544`, MP `41`, TP `0`). The middle-right panel provides skill classification tabs (e.g., **Special**, **Magic**). The lower pane lists available techniques—such as the physical sword technique **Slash**—alongside its resource consumption cost (5 TP/MP) and custom skill icon. Players can cycle between party members using Q/W keyboard shortcuts or the top-left touch arrow buttons (`<` and `>`), allowing rapid review of full party arsenals. |
| **Screen Layout:** | ![Screen 8: Character Skills & Abilities Management Menu](8%20Character%20Skills%20Menu.PNG) |

---

| Screen No.: | Screen 9 |
| :--- | :--- |
| **Screen Name:** | Character Equipment & Gear Configuration Menu |
| **Target User / Role:** | Young Learner / Player |
| **Narrative Overview:** | The Character Equipment and Gear Configuration Menu governs the arming and defensive preparation of player characters. The top pane displays item descriptions and attribute modifiers for the selected piece of gear. The left panel shows the character portrait, name, class, vital gauges, and an eight-row combat parameter matrix: **Max HP** (`544`), **Max MP** (`41`), **Attack** (`19`), **Defense** (`17`), **M.Attack** (`15`), **M.Defense** (`17`), **Agility** (`29`), and **Luck** (`27`), with dynamic comparison arrows (`->`) that calculate projected stat gains or losses in real time. The right panel displays the five canonical equipment slots: **Weapon**, **Shield**, **Head**, **Body**, and **Accessory**, accompanied by an upper **Clear** button (allowing one-click unequipping of all gear). Controls include `Shift` (unequip current slot), `Q/W` (cycle active party member), `Z:Select`, and `X:Back`. |
| **Screen Layout:** | ![Screen 9: Character Equipment & Gear Configuration Menu](9%20Character%20Equipment%20Menu.PNG) |

---

| Screen No.: | Screen 10 |
| :--- | :--- |
| **Screen Name:** | Character Status & Detailed Attributes Menu |
| **Target User / Role:** | Young Learner / Player |
| **Narrative Overview:** | The Character Status and Detailed Attributes Menu provides an exhaustive breakdown of a character's developmental statistics, experience progression, and equipment loadout. The upper window presents the character portrait, full name (*"Alpha"*), class (*"Swordsman"*), level (*"Lv 1"*), vital resource meters (HP `544`, MP `41`, TP `0`), **Current EXP** (`0`), and exact **To Next Level** numerical requirements (`50`). The middle-left panel displays core combat parameters (Attack `19`, Defense `17`, M.Attack `15`, M.Defense `17`, Agility `29`, Luck `27`). The middle-right panel lists currently equipped items across Weapon, Shield, Head, Body, and Accessory slots. The lower text container displays narrative lore, class background descriptions, and active passive traits. Party switching is supported via Q/W hotkeys or touch buttons (`<`, `>`). |
| **Screen Layout:** | ![Screen 10: Character Status & Detailed Attributes Menu](10%20Character%20Status%20Menu.PNG) |

---

| Screen No.: | Screen 11 |
| :--- | :--- |
| **Screen Name:** | Party Formation & Roster Arrangement Menu |
| **Target User / Role:** | Young Learner / Player |
| **Narrative Overview:** | The Party Formation and Roster Arrangement Menu allows players to configure party combat lineups and reposition members between frontline and backline tactical roles. The left panel displays all active combatants with full status cards: lead swordsman **Alpha** (Lv 1 Swordsman, HP `544`, MP `41`, TP `0`), elemental mage **Elara** (Lv 1 Sorcerer with wizard hat and sapphire hair, HP `297`, MP `141`, TP `0`), and ranged tracker **Thorne** (Lv 1 Hunter with feathered cap and fur collar, HP `335`, MP `70`, TP `0`). The right command panel highlights the active **Formation** mode. Selecting two character cards swaps their order in the battle queue, allowing learners to strategically position high-defense characters at the front while protecting specialized spellcasters. |
| **Screen Layout:** | ![Screen 11: Party Formation & Roster Arrangement Menu](11%20-%20Formation%20Menu.PNG) |

---

| Screen No.: | Screen 12 |
| :--- | :--- |
| **Screen Name:** | Quests & Mission Log Interface |
| **Target User / Role:** | Young Learner / Player |
| **Narrative Overview:** | The Quests and Mission Log Interface tracks active campaign progression and procedural bounty tasks generated by the Automatic Quest Generation System. Rendered as a centered two-tier parchment window, the top section (**MAIN STORY**) specifies the active narrative milestone—such as *"Go to the kitchen."*—guiding players through story-driven exploration and arithmetic dungeon progression. The bottom section (**ACTIVE COMMISSION**) tracks procedural hunting and gathering assignments accepted from Receptionist Mila (displaying *"No active commissions. (Visit an NPC to get work)"* when idle). This dual-structure log prevents task ambiguity and supports self-directed learning workflows. |
| **Screen Layout:** | ![Screen 12: Quests & Mission Log Interface](12%20Quests%20Menu.PNG) |

---

| Screen No.: | Screen 13 |
| :--- | :--- |
| **Screen Name:** | Game Save & Progress Recording Interface |
| **Target User / Role:** | Young Learner / Player |
| **Narrative Overview:** | The Game Save and Progress Recording Interface enables players to record current game states, quest milestones, character levels, and inventory data into local device storage. The header prompt asks *"Which file would you like to save to?"*. The screen presents twenty manual save slots (**File 1** through **File 20**) in addition to the designated **Autosave** slot. Populated slots display miniature character sprites representing active party members alongside precise elapsed playtime timestamps (e.g., File 1 showing Alpha and companion at `00:01:25`). Selecting a slot prompts an overwrite confirmation, ensuring safe data storage without server dependencies. The interface fully supports both keyboard controls (`Z:Select`, `X:Back`) and touchscreen taps. |
| **Screen Layout:** | ![Screen 13: Game Save & Progress Recording Interface](13%20Save%20Menu.PNG) |

---

| Screen No.: | Screen 14 |
| :--- | :--- |
| **Screen Name:** | Return to Title / Game Exit Confirmation Dialog |
| **Target User / Role:** | Young Learner / Player |
| **Narrative Overview:** | The Return to Title and Game Exit Confirmation Dialog provides a protective confirmation modal when players select the Exit command from the main pause menu. Positioned in the center of the screen with deep blue borders and a semi-transparent dark fill, the dialog presents two clear choices: **To Title** (which terminates the active gameplay session and safely returns the player to the main Title Screen) and **Cancel** (which dismisses the modal dialog and returns focus to the Pause Menu). This modal prevents accidental loss of unsaved dungeon progress and ensures deliberate session termination. |
| **Screen Layout:** | ![Screen 14: Return to Title / Game Exit Confirmation Dialog](14%20Pause%20Menu%20Exit.PNG) |

---

| Screen No.: | Screen 15 |
| :--- | :--- |
| **Screen Name:** | Tactical Battle Command Menu - Page 1 (Primary Actions) |
| **Target User / Role:** | Young Learner / Player / Co-op Player |
| **Narrative Overview:** | The Tactical Battle Command Menu (Page 1) represents the core turn-based combat screen of *Chronicles of Arithmos* during an encounter in the Plains Biome. The visual battlefield displays enemy monsters on the left side (a flying Fairy/Wasp Archer and a green Slime, both with overhead real-time HP health bars and active status icons) and the player's animated battler sprite on the right (**Garrick**, a Lv 50 Swordsman). The lower-left combatant HUD card displays Garrick's portrait, name, HP (`4,161`), MP (`468`), TP (`21`), and an illuminated action gauge signaling ready command entry. The lower-right command window (Page 1) provides four primary combat commands: **Attack** (sword icon - executes a standard strike and triggers the Math Battle challenge), **Special** (flame icon - opens martial skill submenus), **Guard** (shield icon - reduces incoming damage), and **Item** (potion bottle icon - opens combat restorative items). A down arrow signals access to secondary system commands. |
| **Screen Layout:** | ![Screen 15: Tactical Battle Command Menu - Page 1](15%20Battle%20Menu.PNG) |

---

| Screen No.: | Screen 16 |
| :--- | :--- |
| **Screen Name:** | Tactical Battle Command Menu - Page 2 (System & Tactical Actions) |
| **Target User / Role:** | Young Learner / Player / Co-op Player |
| **Narrative Overview:** | The Tactical Battle Command Menu (Page 2) provides secondary tactical options and combat system utilities. Scrolling down on the lower-right command menu reveals four additional options: **Fight** (sword slash icon - returns immediately to the primary combat actions on Page 1), **Status** (three stars icon - opens the real-time combatant inspection window), **Options** (gear icon - opens audio and visual settings mid-battle), and **Escape** (running boot icon - initiates a tactical retreat from non-boss encounters). The battlefield maintains full visibility of all enemy entities, active combatant health gauges, and character resource pools during menu transitions. |
| **Screen Layout:** | ![Screen 16: Tactical Battle Command Menu - Page 2](16%20Battle%20Menu%202nd%20page.PNG) |

---

| Screen No.: | Screen 17 |
| :--- | :--- |
| **Screen Name:** | Battle Skills & Special Abilities Selection Submenu |
| **Target User / Role:** | Young Learner / Player / Co-op Player |
| **Narrative Overview:** | The Battle Skills and Special Abilities Selection Submenu opens when selecting the Special/Skill command during combat. The top contextual banner provides immediate explanatory feedback on the highlighted technique (e.g., *"Decreases the attack of an enemy"* for **Power Break**). The lower two-column skill matrix displays unlocked techniques alongside their TP/MP resource costs and skill type icons: **Strong Attack** (15 TP), **Slash** (5 TP), **Double Slash** (20 TP), **Armor Break** (20 TP), **Blade Bash** (20 TP), **Sonic Wave** (10 TP), **Wind Slash** (15 TP), and **Power Break** (20 TP). Selecting a skill freezes all Time Progress Battle (TPB) gauges and activates the Math Battle Engine, which generates an arithmetic equation aligned with character level (Levels 1–29 addition/subtraction, Levels 30–69 multiplication/division, Levels 70–100 PEMDAS) and applies performance multipliers (2.0x critical, 1.0x normal, 0.5x weak, 0x miss) based on calculation speed and accuracy. |
| **Screen Layout:** | ![Screen 17: Battle Skills & Special Abilities Selection Submenu](17%20Battle%20Menu%20Skills.PNG) |

---

| Screen No.: | Screen 18 |
| :--- | :--- |
| **Screen Name:** | Battle Consumables & Item Selection Submenu |
| **Target User / Role:** | Young Learner / Player / Co-op Player |
| **Narrative Overview:** | The Battle Consumables and Item Selection Submenu allows players to deploy restorative potions, mana elixirs, and status curatives during active combat encounters. The top help banner explains the exact curative function of the highlighted item (e.g., *"Cures a target of Blindness."* for **Eye Drops**). The lower two-column grid displays all available battle inventory with distinct item category icons, item names, **NEW!** tags indicating recent acquisitions, and remaining stock quantities (e.g., `x90`): **Potion**, **Hi-Potion**, **Full Potion**, **Magic Water**, **Hi-Magic Water**, **Elixir**, **Antidote**, and **Eye Drops**. Selecting a restorative item opens target ally selection, allowing players to heal wounds or cure ailments caused by enemy attacks. |
| **Screen Layout:** | ![Screen 18: Battle Consumables & Item Selection Submenu](18%20Battle%20Menu%20Items.PNG) |

---

| Screen No.: | Screen 19 |
| :--- | :--- |
| **Screen Name:** | Combatant Tactical Status & Condition Submenu |
| **Target User / Role:** | Young Learner / Player / Co-op Player |
| **Narrative Overview:** | The Combatant Tactical Status and Condition Submenu enables players to inspect real-time character statistics, active buff modifiers, and status ailments during combat. Opened via the Status command on Page 2 of the battle menu, the top banner reports the general physical state (e.g., *"Status is currently normal."*). The upper inspection window displays the combatant portrait (**Garrick**), class (*"Swordsman"*), level (*"Lv 50"*), current HP (`4,161`), MP (`468`), TP (`21`), mini battler sprite, an active status badge (**Normal** with heart icon), and exact combat parameters: **Max HP** (`4,161`), **Max MP** (`468`), **Attack** (`136`), **Defense** (`95`), **M.Attack** (`74`), **M.Defense** (`88`), **Agility** (`178`), and **Luck** (`180`). Touch arrow buttons (`<` and `>`) allow cycling through all party members, empowering players to monitor status debuffs (Poison, Blind, Silence, Stun) and positive buffs (Haste, Protect, Shell) dynamically. |
| **Screen Layout:** | ![Screen 19: Combatant Tactical Status & Condition Submenu](19%20Battle%20Menu%20Status.PNG) |

---

## Guidelines for Screen Design (DCT CCS Compliance)

1. **Include All Major System Screens**: The documentation encompasses all primary operational interfaces including Title, Options, Load, Name Input, Overworld Exploration, Pause Menus, Inventory, Skills, Equipment, Status, Formation, Quests, Save, Exit Dialog, and full Battle command flows.
2. **Dedicated Purpose & User Roles**: Every screen details its precise function, system triggers, and target user demographic (Young Learner / Primary School Student / Co-op Player).
3. **High-Resolution Mockups & Captions**: All visual figures utilize clear 2D pixel art screen captures linked to their respective image assets.
4. **Institutional Layout Consistency**: Margin specifications (1.5" Left, 1.0" Right/Top/Bottom), typography (Times New Roman), and table partitioning adhere to the DCT CCS Capstone Manual standard.
