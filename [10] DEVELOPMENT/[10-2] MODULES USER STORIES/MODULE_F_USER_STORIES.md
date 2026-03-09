# Module F: Performance-Based Reward Mechanism — User Stories

> Calculates the direct mechanical outcome of a selected action based on the player's input speed and correctness.

---

## US-F-001: Critical Hit (Correct & Rapid)

**As a** player,
**I want** to deal a 2.0× critical hit when I answer a math equation correctly and quickly (before the timer expires),
**so that** fast and accurate mental math is rewarded with maximum combat effectiveness.

**Priority**: High

**Acceptance Criteria**:

- [ ] A correct answer submitted before the timer expires applies a 2.0× multiplier to the action's base effect.
- [ ] A distinct "Critical Hit" visual/audio cue plays to signal the bonus.
- [ ] The critical multiplier applies to Attack damage, Skill effects, and Item usage alike.
- [ ] The damage number or effect value visually reflects the 2.0× amplification.

---

## US-F-002: Normal Hit (Correct & Slow)

**As a** player,
**I want** my action to execute at normal (1.0×) capacity when I answer correctly but after the timer expires,
**so that** correctness is still valued even if I am slow.

**Priority**: High

**Acceptance Criteria**:

- [ ] A correct answer submitted after the timer expires applies a 1.0× (normal) multiplier.
- [ ] A standard hit visual/audio cue plays (no critical fanfare).
- [ ] The action executes as designed with no bonus or penalty.
- [ ] The player can clearly distinguish this outcome from a Critical Hit visually.

---

## US-F-003: Weak Hit (Incorrect & Rapid)

**As a** player,
**I want** my action to execute at reduced (0.5×) power when I answer incorrectly but quickly,
**so that** I am penalized for wrong answers but not completely punished if I at least responded fast.

**Priority**: High

**Acceptance Criteria**:

- [ ] An incorrect answer submitted before the timer expires applies a 0.5× penalty multiplier.
- [ ] A "Weak Hit" or "Glancing Blow" visual/audio cue communicates the penalty.
- [ ] The action still partially executes (damage is dealt, but at half effect).
- [ ] The player sees the reduced damage number clearly.

---

## US-F-004: Complete Miss (Incorrect & Slow)

**As a** player,
**I want** my action to be completely nullified (0.0× / Miss) when I answer incorrectly and slowly,
**so that** the consequence of failing both accuracy and speed is a total loss of turn.

**Priority**: High

**Acceptance Criteria**:

- [ ] An incorrect answer submitted after the timer expires results in a complete miss / fail.
- [ ] A "Miss" or "Fail" visual/audio cue clearly communicates the result.
- [ ] No damage is dealt, no skill effect activates, and no item is consumed.
- [ ] The character's turn is fully wasted with no partial benefit.

---

## US-F-005: Clear Result Tier Feedback

**As a** player,
**I want** each of the four result tiers to have distinct and immediately recognizable visual/audio feedback,
**so that** I always understand how my math performance affected the outcome.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] Critical Hit (2.0×): Unique flashy animation + sound effect + distinct damage color.
- [ ] Normal Hit (1.0×): Standard animation + standard sound effect.
- [ ] Weak Hit (0.5×): Muted/diminished animation + penalty sound effect.
- [ ] Miss (0.0×): Whiff animation + failure sound effect + "MISS" text display.
- [ ] The result tier is displayed before the action animation begins.
