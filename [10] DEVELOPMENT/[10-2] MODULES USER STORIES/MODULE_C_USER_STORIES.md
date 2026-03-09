# Module C: Level-Based Difficulty System — User Stories

> Automatically scales the complexity of generated math equations to match the player's progression through the game.

---

## US-C-001: Basic Operations (Levels 1–29)

**As a** player at Levels 1–29,
**I want** to encounter only Addition and Subtraction equations using two numbers,
**so that** I can build foundational arithmetic skills before facing harder operations.

**Priority**: High

**Acceptance Criteria**:

- [ ] At Levels 1–29, only `+` and `-` operators are used in generated equations.
- [ ] Equations consist of exactly two operands (e.g., `15 + 7`, `23 - 9`).
- [ ] No multiplication, division, or parentheses appear at this tier.
- [ ] Subtraction results are never negative (the first operand is always ≥ the second).

---

## US-C-002: Intermediate Operations (Levels 30–69)

**As a** player at Levels 30–69,
**I want** Multiplication and Division to be introduced into my math equations,
**so that** the challenge scales with my progression and I practice a wider range of operations.

**Priority**: High

**Acceptance Criteria**:

- [ ] At Levels 30–69, equations may include `+`, `-`, `*`, and `/` operators.
- [ ] Equations consist of two operands (e.g., `12 * 4`, `60 / 5`).
- [ ] Division equations always produce whole number answers (no remainders or decimals).
- [ ] The multiplier/divisor (second operand) remains capped at 1–20 (per Module B constraints).

---

## US-C-003: Advanced Operations (Levels 70–100)

**As a** player at Levels 70–100,
**I want** to face full PEMDAS (order of operations) equations with parentheses,
**so that** I am challenged with composite, multi-step math problems.

**Priority**: High

**Acceptance Criteria**:

- [ ] At Levels 70–100, equations may include parentheses and multiple operators.
- [ ] Equations follow standard PEMDAS order of operations (e.g., `(10 + 5) * 2`).
- [ ] Generated PEMDAS equations always resolve to whole number answers.
- [ ] The equation complexity increases gradually within this range.

---

## US-C-004: Seamless Difficulty Transition

**As a** player,
**I want** the transition between difficulty tiers to happen automatically as I level up,
**so that** I don't need to manually adjust settings and the challenge grows naturally.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] Crossing from Level 29 to Level 30 automatically introduces `*` and `/` operations.
- [ ] Crossing from Level 69 to Level 70 automatically introduces PEMDAS equations.
- [ ] No player action or menu toggle is required to change difficulty.
- [ ] The transition is immediate upon leveling up mid-session.

---

## US-C-005: Training Dummy Variable Equations

**As a** player,
**I want** the Training Dummy in the Training Hall to generate equations that match my current party level,
**so that** I can practice relevant problems safely.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] Training Dummy equations scale to match the active party's average level.
- [ ] A Level 35 party encounters `*` and `/` equations from the Training Dummy.
- [ ] A Level 75 party encounters PEMDAS equations from the Training Dummy.
- [ ] The Training Dummy follows the same tier rules (Levels 1–29, 30–69, 70–100).

---

## US-C-006: Training Dummy Fixed-Level Equations

**As a** player,
**I want** an option to set the Training Dummy to a fixed difficulty level,
**so that** I can practice specific tiers of math problems regardless of my current level.

**Priority**: Low

**Acceptance Criteria**:

- [ ] A setting or option allows choosing a fixed equation level for the Training Dummy.
- [ ] The fixed level overrides the variable (party-level) default.
- [ ] Players can select any level range (Basics, Intermediate, Advanced).
- [ ] The setting can be toggled back to the default (variable) mode at any time.
