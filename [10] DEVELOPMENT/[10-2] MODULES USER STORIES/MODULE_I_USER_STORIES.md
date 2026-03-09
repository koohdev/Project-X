# Module I: Save System — User Stories

> Manages persistent local data storage, securing user progress via manual slots and automated checkpoints.

---

## US-I-001: Manual Save Slots

**As a** player,
**I want** access to 20 manual save slots where I can save my progress at will,
**so that** I can maintain multiple save points and return to any of them later.

**Priority**: High

**Acceptance Criteria**:

- [ ] The save menu presents 20 numbered save slots.
- [ ] Each slot shows relevant metadata (e.g., play time, party level, location name).
- [ ] The player can save to any empty slot by selecting it.
- [ ] Empty slots are clearly distinguishable from occupied ones.

---

## US-I-002: Save Slot Overwrite

**As a** player,
**I want** to overwrite an existing save slot with my current progress,
**so that** I can reuse slots without running out of space.

**Priority**: High

**Acceptance Criteria**:

- [ ] Selecting an occupied save slot prompts a confirmation dialog ("Overwrite this save?").
- [ ] Confirming overwrites the slot with the current game state.
- [ ] Cancelling returns to the save menu without changes.
- [ ] The overwritten save's metadata updates to reflect the new save state.

---

## US-I-003: Load Game from Save Slot

**As a** player,
**I want** to load my game from any occupied save slot,
**so that** I can resume play from a previously saved point.

**Priority**: High

**Acceptance Criteria**:

- [ ] The load menu displays all 20 slots with their metadata.
- [ ] Selecting an occupied slot loads the game state from that save.
- [ ] The game resumes at the exact location, party status, and progression of the save.
- [ ] A loading confirmation or transition screen is shown during the load process.

---

## US-I-004: Autosave on Map Transitions

**As a** player,
**I want** the game to automatically save my progress in a dedicated autosave slot whenever I cross a map transition checkpoint,
**so that** I have a recent backup even if I forget to save manually.

**Priority**: High

**Acceptance Criteria**:

- [ ] A dedicated autosave slot (Slot 21 or labeled "Autosave") exists separately from the 20 manual slots.
- [ ] The autosave triggers automatically upon crossing map transition checkpoints.
- [ ] The autosave overwrites the previous autosave each time it triggers.
- [ ] The autosave process runs in the background without interrupting gameplay.
- [ ] A small on-screen indicator (e.g., save icon) briefly appears during autosave.

---

## US-I-005: Load from Autosave

**As a** player,
**I want** to load my game from the autosave slot,
**so that** I can recover from unexpected shutdowns or mistakes using the most recent checkpoint.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] The autosave slot is accessible from the load menu alongside manual slots.
- [ ] The autosave slot is clearly labeled (e.g., "Autosave" or marked with an icon).
- [ ] Loading from autosave restores the game state from the last map transition.
- [ ] The autosave slot cannot be manually overwritten or deleted by the player.
