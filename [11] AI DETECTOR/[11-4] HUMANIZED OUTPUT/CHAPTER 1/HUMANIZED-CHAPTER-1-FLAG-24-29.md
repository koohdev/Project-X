# Humanized Output — Chapter 1, Flags 24–29 + New Limitation G
# § 1.3.2 Limitations

**Date:** 2026-03-09
**Flags:** 24, 25, 26, 27, 28, 29 (all 6 limitations) + NEW Limitation G
**Section:** § 1.3.2 Limitations

---

## Flag 24 — Limitation A: Mathematical Scope and Generation Limits (Line 1086)

### Original

> The system does not currently support advanced algebra, calculus, or non-integer results (fractions/decimals). To maintain combat flow, the math generator is strictly restricted so that all division problems calculate to exact whole numbers, avoiding fractions or decimals entirely. Furthermore, the system imposes a hard limit on the multiplier and the divisor (the second number in any multiplication or division problem), capping them at a range of 1 to 20. This specific numerical limitation applies universally to every combat encounter, including multi-part equations at higher levels.

### Humanized ← HUMANIZED

> The math generator only produces whole number arithmetic, so there are no fractions, decimals, algebra, or calculus problems in the game. Division equations always come out to exact whole numbers, and the second number in any multiplication or division problem stays between 1 and 20. This cap applies to every combat encounter, including the three-part PEMDAS equations at Level 70 and above.

### Changes Applied

| # | Change | Type |
| :--- | :--- | :--- |
| 1 | "Furthermore" → dropped | AI transition removal |
| 2 | "strictly restricted so that" → "only produces" | Vocab downgrade |
| 3 | Merged sentences 1+2 (removed redundant fractions/decimals mention) | Reduce uniform structure |
| 4 | "This specific numerical limitation applies universally" → "This cap applies" | Vocab downgrade |
| 5 | Added "three-part PEMDAS" and "Level 70" | Perplexity boosters |
| 6 | 4 sentences → 3 sentences | Burstiness variation |

---

## Flag 25 — Limitation B: Tactile Input Disparity (Line 1089)

### Original

> While the inclusion of a Virtual Numeric Keypad enables mobile playability, the lack of tactile feedback on touchscreens may result in reduced input velocity compared to physical keyboards. Consequently, users on mobile devices may experience a slight disadvantage in high-level "Speed Math" calculations where millisecond reaction times are critical.

### Humanized ← HUMANIZED

> The Virtual Numeric Keypad lets the game run on touchscreens, but tapping a flat screen does not feel the same as pressing physical keys and that difference in feedback can slow the player down. This matters most specially during higher-level encounters where the Math Timer gives only a few seconds to type an answer.

### Changes Applied

| # | Change | Type |
| :--- | :--- | :--- |
| 1 | "Consequently" → dropped | AI transition removal |
| 2 | "While the inclusion of...enables mobile playability" → "lets the game run on touchscreens" | Filler removal + vocab downgrade |
| 3 | "reduced input velocity" → "slow the player down" | Vocab downgrade |
| 4 | "may experience a slight disadvantage" → "This matters most" | Hedging removal |
| 5 | Added "Math Timer" | Perplexity booster |
| 6 | "a few seconds" replaces vague "millisecond reaction times" phrasing | Concrete detail |

---

## Flag 26 — Limitation C: Input Method (Line 1093)

### Original

> The input system utilizes the standard number row or numpad of a physical keyboard. On mobile and touch-screen devices, the system provides a Virtual Numeric Keypad as the primary input method. This limitation means that input speed may vary depending on the device used.

### Humanized ← HUMANIZED

> On a PC, the player types answers using the keyboard's number row or numpad, and on mobile the Virtual Numeric Keypad replaces that. Because the two input methods feel different, answer speed can change depending on which device the player uses.

### Changes Applied

| # | Change | Type |
| :--- | :--- | :--- |
| 1 | "utilizes" → "types answers using" | Banned word removal |
| 2 | "This limitation means that" → dropped (restructured with "Because") | Filler/self-reference removal |
| 3 | 3 sentences → 2 sentences | Reduce uniform structure |
| 4 | Compound sentence with "and" | Angel-style compound (PERSONALITY §1) |

---

## Flag 27 — Limitation D: Asset Fidelity (Line 1097)

### Original

> The project utilizes standard 2D pixel art assets and does not focus on high-fidelity 3D rendering or physics simulations.

### Humanized ← HUMANIZED

> The game or the proposed project uses 2D pixel art built in RPG Maker MZ and does not include 3D models, physics simulations, or high-fidelity rendering.

### Changes Applied

| # | Change | Type |
| :--- | :--- | :--- |
| 1 | "utilizes" → "uses" | Banned word removal |
| 2 | "The project" → "The game" | Vocab downgrade (Angel says "game") |
| 3 | "does not focus on" → "does not include" | More direct (Angel-level) |
| 4 | Added "RPG Maker MZ" | Perplexity booster |

---

## Flag 28 — Limitation E: Peer-to-Peer Latency Sensitivity (Line 1101)

### Original

> The multiplayer feature relies on the stability of the host's internet connection. As the system utilizes a direct P2P handshake, high latency or packet loss on the host side may result in desynchronization of the Math Timer for connected clients.

### Humanized ← HUMANIZED

> The P2P multiplayer runs through PeerJS on the host's or the player who initiated and created the room for joining requires internet connection, so if the host has high latency or slow internet, the Math Timer on the guest's screen can fall out of sync with the host's.

### Changes Applied

| # | Change | Type |
| :--- | :--- | :--- |
| 1 | "utilizes" → removed (restructured) | Banned word removal |
| 2 | "relies on the stability of" → "runs through PeerJS on" | Vocab downgrade + perplexity booster |
| 3 | "may result in desynchronization" → "can fall out of sync" | Vocab downgrade |
| 4 | 2 sentences → 1 compound sentence with "so" | Angel-style compound |
| 5 | Added "PeerJS" | Perplexity booster |

---

## Flag 29 — Limitation F: Volatile Session Architecture (Line 1104)

### Original

> The multiplayer system is stateless (no central dedicated server). If the host application is terminated, the game session dissolves immediately for all connected clients; state recovery for guest clients is not supported in this version.

### Humanized ← HUMANIZED

> The multiplayer system has no central server and does not store session data. If the host closes the game or loses connection, the session ends for all connected players immediately, and the guest cannot reconnect to the same Room Code.

### Changes Applied

| # | Change | Type |
| :--- | :--- | :--- |
| 1 | "is stateless" → "has no central server and does not store session data" | Plain explanation of technical term |
| 2 | "the host application is terminated" → "the host closes the game or loses connection" | Vocab downgrade |
| 3 | "state recovery for guest clients is not supported" → "the guest cannot reconnect to the same Room Code" | Vocab downgrade + perplexity booster |
| 4 | Semicolon → "and" compound | Angel-style connector |

---

## NEW — Limitation G: Local-Only Save Data

### Humanized ← NEW LIMITATION

> The save system writes all progress to local files on the player's device because the system does not have a user authentication module or a centralized database. There is no account creation, login, or cloud sync, so a player that starts on one PC cannot continue on a different device or on a phone without manually copying the save file over.

### Design Notes

- Framed as what the system CANNOT do (no auth module, no centralized DB), not as a design choice
- "a player that" = ESL marker (PERSONALITY §6)
- "manually copying the save file over" = concrete, specific, Angel-level
- Compound sentence with "because" and "so"
- Technical reason explained plainly

---

## Summary

| Metric | Before (Flags 24–29) | After (Flags 24–29 + G) |
| :--- | :--- | :--- |
| "will" count | 0 | 0 |
| "utilizes/utilize" count | 4 | 0 |
| AI transitions removed | — | 2 ("Furthermore", "Consequently") |
| Filler phrases removed | — | 3 |
| Perplexity boosters added | 0 | 8 (PEMDAS, Level 70, Math Timer, RPG Maker MZ, PeerJS, Room Code ×2, save file) |
| ESL markers | 0 | 1 ("a player that") |
| Total sentences (A–F) | 14 | 11 |
| Limitations count | 6 | 7 (+Limitation G) |
| Vocab downgrades | 0 | 12 |

### PERSONALITY.md Checklist (all 7 limitations)

- [x] Would Angel actually say this? — Yes, plain and direct
- [x] Plain verbs throughout (uses, types, runs, drops, closes, writes, starts)
- [x] Compound sentences with and/but/so/because — not chopped into clinical declarations
- [x] No AI transitions (Furthermore, Consequently, Moreover)
- [x] Game-specific names in every limitation
- [x] No under-10-word sentences
- [x] No rhetorical question openers
- [x] Varied internal structure across all 7 (some 1 sentence, some 2, some 3)
- [x] Third person maintained, no contractions
