# Module D: "Content-Aware" Timer System — User Stories

> Calculates the dynamic countdown timer allowed for the player to input their answer based on the specific math problem generated.

---

## US-D-001: Dynamic Timer Display

**As a** player,
**I want** to see a visible countdown timer while solving a math equation,
**so that** I know how much time I have left to submit my answer.

**Priority**: High

**Acceptance Criteria**:

- [ ] A countdown timer is displayed prominently alongside the math equation window.
- [ ] The timer counts down in real-time (seconds and/or a progress bar).
- [ ] The timer starts the moment the math equation appears on screen.
- [ ] A visual or audio warning triggers when time is running low (e.g., last 3 seconds).

---

## US-D-002: Timer Scaled to Equation Complexity

**As a** player,
**I want** the timer duration to be automatically calculated based on the equation's complexity,
**so that** I get a fair amount of time proportional to the difficulty of the problem.

**Priority**: High

**Acceptance Criteria**:

- [ ] The base time is calculated using the formula: `Equation length / Number of digits`.
- [ ] Longer and more complex equations receive more time.
- [ ] Simpler equations (e.g., `3 + 5`) receive less time.
- [ ] The timer calculation is invisible to the player — they only see the final countdown.

---

## US-D-003: Bonus Time for Complex Operators

**As a** player,
**I want** extra time added to my countdown when the equation includes multiplication or division,
**so that** I am given fair extra time for harder operations.

**Priority**: High

**Acceptance Criteria**:

- [ ] Equations containing `*` receive a defined bonus time addition.
- [ ] Equations containing `/` receive a defined bonus time addition.
- [ ] Equations with exceptionally large numbers receive additional bonus time.
- [ ] Bonus time stacks if multiple conditions apply (e.g., large numbers AND division).

---

## US-D-004: Slow Input Penalty

**As a** player,
**I want** to be penalized for answering after the timer expires,
**so that** I am motivated to solve equations quickly and build speed.

**Priority**: High

**Acceptance Criteria**:

- [ ] If the timer reaches zero before an answer is submitted, the input is auto-registered as "slow."
- [ ] A "slow" correct answer is treated differently from a "rapid" correct answer (per Module F rules).
- [ ] A "slow" incorrect answer results in the worst outcome (complete miss, per Module F rules).
- [ ] A clear visual/audio cue communicates the "slow" penalty to the player.

---

## US-D-005: Timer Freeze Synchronization

**As a** player,
**I want** the math timer to be the only active countdown during the equation window,
**so that** no other game timers or gauges interfere with my focus.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] The math countdown timer is the sole active timer when the equation window is open.
- [ ] All Action Gauges are frozen (per Module A integration) during the timer countdown.
- [ ] No enemy actions execute while the math timer is running.
- [ ] The timer resumes normal game state upon expiry or answer submission.
