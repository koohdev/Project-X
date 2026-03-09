# Module A: Standard Role-Playing Game (RPG) Combat Mechanics — User Stories

> This module establishes the foundational logic, timing, and resource pools for all battle scenes in *Chronicles of Arithmos*.

---

## US-A-001: Action Gauge Display

**As a** player,
**I want** to see a visible Action Gauge that fills based on my character's Speed/Agility stat,
**so that** I can anticipate when my turn is coming and plan my actions accordingly.

**Priority**: High

**Acceptance Criteria**:

- [ ] Each party member has a dedicated Action Gauge visible on the battle HUD.
- [ ] The fill rate of the gauge is proportional to the character's Speed/Agility stat.
- [ ] When the gauge is full, the character's command menu opens automatically.
- [ ] The gauge visually resets to zero after the character completes their action.

---

## US-A-002: Gauge Freeze During Math Input

**As a** player,
**I want** all enemy Action Gauges to freeze the instant a math equation appears on screen,
**so that** I am not attacked while I am focused on solving the problem.

**Priority**: High

**Acceptance Criteria**:

- [ ] All enemy Action Gauges pause the exact millisecond the math input window opens.
- [ ] Enemy gauges remain frozen until the player submits an answer or the timer expires.
- [ ] Ally gauges (other party members) also pause during the math window.
- [ ] Gauges resume at their previous fill level once the math window closes.

---

## US-A-003: Turn Sequence Execution

**As a** player,
**I want** combat to follow a clear three-step sequence (Select Action → Solve Math → Execute Action),
**so that** I understand the flow of battle and know what to expect at each step.

**Priority**: High

**Acceptance Criteria**:

- [ ] After a character's gauge fills, a command menu appears (Select Action).
- [ ] Upon selecting an action (Attack, Skill, Item), a math equation is presented (Solve Math).
- [ ] After the math result is evaluated, the action executes with the appropriate outcome (Execute Action).
- [ ] The sequence is consistent and unbreakable — no step can be skipped.

---

## US-A-004: HP Tracking

**As a** player,
**I want** to see my characters' Health Points (HP) displayed during battle,
**so that** I know when a character is in danger and needs healing.

**Priority**: High

**Acceptance Criteria**:

- [ ] Each party member's current HP and max HP are displayed numerically on the battle HUD.
- [ ] HP decreases visually in real-time when damage is received.
- [ ] HP increases visually in real-time when healing is received.
- [ ] When HP reaches 0, the character enters a "KO" state and is unable to act.

---

## US-A-005: MP Tracking

**As a** player,
**I want** to see my characters' Mana Points (MP) displayed during battle,
**so that** I can manage my skill usage and know when I need to conserve or restore mana.

**Priority**: High

**Acceptance Criteria**:

- [ ] Each party member's current MP and max MP are displayed numerically on the battle HUD.
- [ ] MP decreases when a skill is used successfully.
- [ ] Skills that cost more MP than available are grayed out or disabled in the command menu.
- [ ] MP can be restored via items or specific skills.

---

## US-A-006: TP Tracking

**As a** player,
**I want** to see my characters' Tactical Points (TP) displayed during battle,
**so that** I can plan when to use powerful TP-based abilities.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] Each party member's current TP and max TP are displayed on the battle HUD.
- [ ] TP accumulates through a defined mechanic (e.g., taking damage, dealing damage, or completing math quickly).
- [ ] TP-based actions are only available when sufficient TP has been accumulated.
- [ ] TP resets or carries over between battles as designed.

---

## US-A-007: Training Hall Practice

**As a** player,
**I want** to access a Training Hall where I can fight a Training Dummy,
**so that** I can practice math equations and combat mechanics safely without risking a Game Over.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] A Training Hall location is accessible from at least one in-game town or hub.
- [ ] The Training Dummy has infinite HP and cannot be defeated.
- [ ] Combat with the Training Dummy follows the same three-step sequence as regular battles.
- [ ] An "Escape" command is available at all times to exit the Training Hall battle manually.
- [ ] No EXP or Gold is rewarded from Training Dummy fights.
