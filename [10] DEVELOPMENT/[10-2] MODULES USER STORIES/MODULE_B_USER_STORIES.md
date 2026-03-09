# Module B: Math Battle System Plugin — User Stories

> The core educational feature that replaces standard RPG probability (RNG) with mental arithmetic challenges to build calculation speed.

---

## US-B-001: Math Equation Generation on Action

**As a** player,
**I want** a math equation to appear on screen every time I select a combat action (Attack, Skill, or Item),
**so that** I must solve a math problem to execute my move, reinforcing my arithmetic skills.

**Priority**: High

**Acceptance Criteria**:

- [ ] Selecting "Attack" triggers a math equation window.
- [ ] Selecting "Skill" triggers a math equation window.
- [ ] Selecting "Item" triggers a math equation window.
- [ ] The equation window is clearly visible and centered on screen.
- [ ] The equation window displays the generated problem and an input field for the answer.

---

## US-B-002: Keyboard Input for Answers

**As a** player,
**I want** to type my answer using my physical keyboard (number row or numpad),
**so that** I can input answers quickly and naturally.

**Priority**: High

**Acceptance Criteria**:

- [ ] The game captures physical keystrokes from the number row (0–9).
- [ ] The game captures physical keystrokes from the numpad (0–9).
- [ ] A "Submit" or "Enter" key confirms the answer.
- [ ] A "Backspace" or "Delete" key allows correction before submission.
- [ ] Non-numeric keys are ignored during the math input phase.

---

## US-B-003: Whole Number Answer Constraint

**As a** player,
**I want** every math equation to produce a whole number answer,
**so that** I never encounter confusing fractions or decimals in my answers.

**Priority**: High

**Acceptance Criteria**:

- [ ] All generated equations produce exact whole number (integer) answers.
- [ ] Division operations are validated at generation time to ensure no remainders.
- [ ] No fraction or decimal answer is ever produced by the equation generator.
- [ ] This constraint is enforced across all difficulty levels (Levels 1–100).

---

## US-B-004: Multiplier/Divisor Range Cap

**As a** player,
**I want** the second number in multiplication and division problems to be capped between 1 and 20,
**so that** the problems remain challenging but fair and solvable through mental math.

**Priority**: High

**Acceptance Criteria**:

- [ ] In multiplication operations, the multiplier (second operand) is always within the range of 1 to 20.
- [ ] In division operations, the divisor (second operand) is always within the range of 1 to 20.
- [ ] This cap applies universally across all difficulty levels.
- [ ] The first operand is not restricted by this cap and scales with difficulty.

---

## US-B-005: Action Outcome Based on Answer

**As a** player,
**I want** the outcome of my combat action to depend on whether I answered the math equation correctly or incorrectly,
**so that** my math performance directly impacts my battle success.

**Priority**: High

**Acceptance Criteria**:

- [ ] A correct answer results in the selected action being executed successfully.
- [ ] An incorrect answer results in the action being weakened or nullified (per Module F rules).
- [ ] A clear visual/audio cue distinguishes between correct and incorrect outcomes.
- [ ] The result is displayed before the action animation plays.
