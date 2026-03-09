# Module G: Automatic Quest Generation System — User Stories

> Dynamically creates side quests to maintain replayability and encourage continued calculation practice outside of the main story.

---

## US-G-001: Procedural Quest Generation

**As a** player,
**I want** the game to automatically generate side quests based on the areas I have unlocked,
**so that** I always have fresh content to play through for extra math practice.

**Priority**: High

**Acceptance Criteria**:

- [ ] The system scans boolean flags to determine which areas are currently unlocked.
- [ ] Generated quests are relevant to the unlocked area(s) — using regional enemies and items.
- [ ] A new quest is available after completing or rejecting the current one.
- [ ] Quests are procedurally diverse (varying targets, quantities, and locations).

---

## US-G-002: Hunting Quests

**As a** player,
**I want** to receive hunting-type quests that require me to defeat a certain number of specific enemies,
**so that** I have a goal-oriented reason to engage in combat and practice math.

**Priority**: High

**Acceptance Criteria**:

- [ ] Hunting quests specify a target enemy type and a required kill count.
- [ ] The target enemy exists in the player's currently unlocked areas.
- [ ] Kill progress is tracked and displayed to the player.
- [ ] The quest completes automatically when the kill count is reached.

---

## US-G-003: Gathering Quests

**As a** player,
**I want** to receive gathering-type quests that require me to collect specific item drops,
**so that** I have item-focused objectives alongside combat practice.

**Priority**: High

**Acceptance Criteria**:

- [ ] Gathering quests specify a target item and a required quantity.
- [ ] The target item drops from enemies in the player's unlocked areas.
- [ ] Collection progress is tracked and displayed to the player.
- [ ] The quest completes automatically when the required items are collected.

---

## US-G-004: No Time Limit on Quests

**As a** player,
**I want** generated side quests to have no time limit,
**so that** I can complete them at my own pace without feeling pressured.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] No countdown timer or deadline is attached to any generated quest.
- [ ] Quests persist indefinitely until completed or rejected.
- [ ] There is no penalty for taking a long time to finish a quest.

---

## US-G-005: Quest Rejection and Re-Roll

**As a** player,
**I want** to reject a generated quest and immediately receive a new one,
**so that** I can skip quests I don't find interesting and get a fresh task.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] A "Reject" or "Decline" option is available in the quest prompt.
- [ ] Rejecting a quest flushes the current quest variables.
- [ ] A new quest is procedurally generated immediately after rejection.
- [ ] There is no limit or penalty for rejecting quests consecutively.

---

## US-G-006: Quest Rewards

**As a** player,
**I want** to receive EXP and/or Gold rewards upon completing a generated quest,
**so that** side quests contribute meaningfully to my character's progression.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] Completed quests award EXP and/or Gold based on difficulty.
- [ ] Reward amounts scale appropriately with the player's level.
- [ ] Rewards are displayed in a completion summary screen.
- [ ] Rewards are added to the player's totals automatically.
