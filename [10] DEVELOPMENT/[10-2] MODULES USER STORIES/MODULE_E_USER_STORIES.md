# Module E: Enemy Auto-Scaling System — User Stories

> Maintains difficulty across all geographical areas by automatically adjusting enemy stats based on the player's party level.

---

## US-E-001: Enemy Stats Scale to Party Level

**As a** player,
**I want** enemy base stats (Max HP, ATK) to automatically adjust relative to my party's average level when a battle starts,
**so that** combat remains challenging regardless of which area I visit.

**Priority**: High

**Acceptance Criteria**:

- [ ] Enemy `Max HP` is recalculated relative to the active party's average level upon each battle start.
- [ ] Enemy `ATK` is recalculated relative to the active party's average level upon each battle start.
- [ ] A Level 50 party encounters harder enemies than a Level 10 party, even in the same zone.
- [ ] The scaling formula runs silently in the background with no visible indicator to the player.

---

## US-E-002: EXP Drops Scale to Party Level

**As a** player,
**I want** enemies to drop EXP rewards proportional to my party's level,
**so that** I always earn meaningful experience regardless of the area.

**Priority**: High

**Acceptance Criteria**:

- [ ] Enemy `EXP drop` values are recalculated based on the party's average level.
- [ ] Low-level areas still grant progression-relevant EXP to high-level parties.
- [ ] EXP scaling does not exceed the hard cap defined in Module J (99,999 EXP).
- [ ] EXP values are displayed correctly in the battle results screen.

---

## US-E-003: Gold Drops Scale to Party Level

**As a** player,
**I want** enemies to drop Gold rewards proportional to my party's level,
**so that** I can still earn useful currency from fights in any region.

**Priority**: High

**Acceptance Criteria**:

- [ ] Enemy `Gold drop` values are recalculated based on the party's average level.
- [ ] Low-level areas still provide economy-relevant Gold to high-level parties.
- [ ] Gold scaling does not exceed the hard cap defined in Module J (50,000 G).
- [ ] Gold values are displayed correctly in the battle results screen.

---

## US-E-004: Prevent Trivial Early-Area Encounters

**As a** player,
**I want** early-game enemies to remain a reasonable challenge even when I return at a high level,
**so that** no area in the game becomes completely trivial or irrelevant.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] Returning to a Level 1 area at Level 80 does not result in one-hit kills against every enemy.
- [ ] Scaled enemies have appropriate HP and ATK to require at least partial engagement with the math system.
- [ ] The scaling does not make early enemies harder than endgame enemies.
- [ ] The scaling preserves relative difficulty differences between world regions.
