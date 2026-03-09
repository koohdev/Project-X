# Module J: Level-Based Progression — User Stories

> Establishes the phases of progression by providing rewards following successful combat and completing quests, controlling the game's pacing and math difficulty timeline.

---

## US-J-001: Experience Points (EXP) Progression

**As a** player,
**I want** to earn Experience Points (EXP) after winning battles and completing quests,
**so that** my characters can level up and grow stronger over time.

**Priority**: High

**Acceptance Criteria**:

- [ ] EXP is awarded after each successful battle based on enemies defeated.
- [ ] EXP thresholds start at 10 EXP for basic/early encounters.
- [ ] EXP thresholds scale up to a hard cap of 99,999 EXP for endgame bosses.
- [ ] Characters level up automatically when cumulative EXP reaches the next threshold.
- [ ] A level-up notification displays stat increases and any new unlocks.

---

## US-J-002: Gold (Currency) Progression

**As a** player,
**I want** to earn Gold as currency from battle victories and quest rewards,
**so that** I can purchase items, equipment, and services from in-game merchants.

**Priority**: High

**Acceptance Criteria**:

- [ ] Gold is awarded after each successful battle based on enemies defeated.
- [ ] Gold drops start at 5 G for basic/early encounters.
- [ ] Gold drops scale up to a hard cap of 50,000 G for endgame encounters.
- [ ] The player's total Gold is displayed on the inventory/menu screen.
- [ ] Gold can be spent at merchant NPCs for items and equipment.

---

## US-J-003: Story Milestone Unlocks

**As a** player,
**I want** new maps and higher-level stages to unlock when I reach specific story milestones,
**so that** the game world expands at a pace that matches the narrative and my skill growth.

**Priority**: High

**Acceptance Criteria**:

- [ ] Story milestones are triggered via in-game switches/variables (e.g., defeating a boss, completing a quest chain).
- [ ] Reaching a milestone unlocks access to new map areas.
- [ ] Unlocked areas introduce higher-level enemies and harder math equations (per Module C tiers).
- [ ] A clear in-game notification signals when a new area is unlocked.

---

## US-J-004: Level Cap Enforcement

**As a** player,
**I want** a maximum level cap to exist,
**so that** the game maintains balance and the math difficulty system doesn't break from over-grinding.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] A defined maximum level cap (e.g., Level 100) prevents further leveling.
- [ ] Upon reaching the cap, excess EXP is not accumulated.
- [ ] The player is notified when the cap is reached.
- [ ] All game systems (math scaling, enemy scaling) function correctly at the level cap.

---

## US-J-005: Gold Cap Enforcement

**As a** player,
**I want** a maximum Gold cap to exist,
**so that** the game's economy remains balanced.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] A defined maximum Gold cap prevents accumulation beyond the limit.
- [ ] Upon reaching the cap, excess Gold drops are not added.
- [ ] The player is notified when the Gold cap is reached.
- [ ] The cap does not prevent the player from spending Gold to make room.

---

## US-J-006: Anti-Overgrinding Safeguard

**As a** player,
**I want** progression gating through story milestones to prevent me from breaking the math difficulty curve by overgrinding in early areas,
**so that** the game's educational pacing remains intact.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] Certain math difficulty tiers only unlock through story progression, not just level alone.
- [ ] A player cannot access Level 70+ PEMDAS equations without reaching the required milestone.
- [ ] EXP grinding alone cannot bypass the narrative-gated content.
- [ ] The system provides natural incentives to progress the story rather than grind indefinitely.
