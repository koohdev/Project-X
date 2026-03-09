# Module K: Mobile Detection System and Virtual Numeric Keypad — User Stories

> Ensures accessibility on touch-screen interfaces by detecting the environment and providing a virtual input method.

---

## US-K-001: Automatic Touch Screen Detection

**As a** player on a mobile or tablet device,
**I want** the game to automatically detect that I am on a touch-screen device,
**so that** it can provide an appropriate input method without me needing to configure anything.

**Priority**: High

**Acceptance Criteria**:

- [ ] The system runs an environment check on game launch (`Touch screen == true`).
- [ ] Detection is automatic with no manual toggle required from the player.
- [ ] The detection correctly identifies mobile phones and tablets.
- [ ] Desktop/laptop users with physical keyboards are not affected by this system.

---

## US-K-002: Virtual Numeric Keypad Display

**As a** player on a touch-screen device,
**I want** a Virtual Numeric Keypad to appear on screen alongside the math equation,
**so that** I can tap numbers to input my answer without a physical keyboard.

**Priority**: High

**Acceptance Criteria**:

- [ ] A virtual keypad UI layer renders adjacent to the math equation window.
- [ ] The keypad displays buttons for digits 0–9.
- [ ] The keypad includes a "Submit" / "Enter" button to confirm the answer.
- [ ] The keypad includes a "Backspace" / "Delete" button to correct input.
- [ ] The keypad layout is intuitive and follows standard calculator/numpad arrangement.

---

## US-K-003: Virtual Keypad Button Mapping

**As a** player using the Virtual Keypad,
**I want** each virtual button to map directly to the same function as a physical keyboard key,
**so that** my gameplay experience is identical whether I use touch or keyboard input.

**Priority**: High

**Acceptance Criteria**:

- [ ] Virtual button "0" maps to physical key `0` (and so on for 1–9).
- [ ] Virtual "Enter" maps to the same submit action as the physical Enter/Return key.
- [ ] Virtual "Backspace" maps to the same delete action as the physical Backspace key.
- [ ] All Module B and Module F mechanics (correctness, speed) behave identically via virtual input.

---

## US-K-004: Keypad Does Not Obstruct Equation

**As a** player using the Virtual Keypad,
**I want** the keypad to be positioned so it does not overlap or obscure the math equation or timer,
**so that** I can read the problem and see the countdown while inputting my answer.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] The virtual keypad is positioned below or beside the equation window, never overlapping.
- [ ] The math equation, input field, and countdown timer remain fully visible.
- [ ] The layout adapts cleanly to common mobile screen sizes and orientations.
- [ ] No critical gameplay UI is hidden behind the virtual keypad.

---

## US-K-005: Keypad Only Appears When Needed

**As a** player on a touch-screen device,
**I want** the Virtual Keypad to appear only during math input phases and disappear otherwise,
**so that** it does not clutter the screen during exploration or cutscenes.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] The virtual keypad is hidden during non-math gameplay (exploration, menus, dialogue).
- [ ] The virtual keypad appears automatically when the math equation window opens.
- [ ] The virtual keypad disappears automatically when the math window closes.
- [ ] The transition (appear/disappear) is smooth and non-jarring.
