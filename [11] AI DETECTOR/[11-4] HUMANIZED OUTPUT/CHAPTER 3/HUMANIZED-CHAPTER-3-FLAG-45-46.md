# Humanized Output — Flags 45, 46
## § 3.2.2 Implementation Software — OS & Browsers

**Source file:** `[04] OUR_PROJECT/[COA]-CHAPTER-3.md`
**Target lines:** Lines 137, 141
**Date:** 2026-03-09
**Workflow:** `/humanize-writing`

---

## Original Text

**Flag 45 — Operating System (Line 137):**
```
The minimum operating system requirement will be Windows 10 (64-bit). This OS environment is needed because the NW.js runtime wrapper, which powers the game's executable, relies on modern 64-bit system components that are not supported in older versions like Windows 7. For mobile users, Android 10 or iOS 14 will be required because the game's web technologies (WebGL 2.0) depend on updated support found in these mobile operating systems.
```

**Flag 46 — Modern Browsers (Line 141):**
```
Users will be required to use a modern web browser to access the web-deployed version via GitHub Pages. To align with the development environment, the supported browsers will specifically include Chromium-based web browsers such as Google Chrome and Microsoft Edge. These browsers are required because the game's Virtual Numeric Keypad overlay, WebGL rendering, and Peer-to-Peer (P2P) Multiplayer Framework handshake utilize HTML5 and Web Real-Time Communication (WebRTC) standards that are most reliably implemented within these browsers.
```

---

## Humanized Text

**Flag 45 — Operating System:**
```
The minimum operating system for the desktop version is Windows 10 (64-bit) because NW.js, which packages the game as an .exe file, needs 64-bit system components that older versions like Windows 7 do not have. Mobile users need at least Android 10 or iOS 14 since the browser version of the game runs on WebGL 2.0, and older mobile systems do not support it.
```

**Flag 46 — Modern Browsers:**
```
The web-deployed version on GitHub Pages needs a modern Chromium-based browser, specifically Google Chrome or Microsoft Edge, because the game's Virtual Numeric Keypad and P2P Multiplayer handshake through PeerJS both depend on HTML5 and WebRTC support. These two browsers handle WebGL rendering and the Room Code connection most consistently, which is why the proponents chose them as the supported platforms.
```

---

## Change Log

### Patterns Fixed

| Category | Before | After |
| :--- | :--- | :--- |
| "will" count (combined) | 4 ("will be" ×2, "will be required", "will specifically include") | 0 |
| "utilize" | 1 | 0 |
| AI filler transitions ("To align with the development environment") | 1 | 0 |
| Rule of Three (parallel noun phrases) | 1 ("...overlay, ...rendering, and ...handshake") | 0 — collapsed to 2 features |
| Template setups ("This OS environment is needed because") | 1 | 0 |
| Elevated phrases ("relies on modern 64-bit system components", "depend on updated support found in these mobile operating systems", "most reliably implemented within these browsers") | 3 | 0 |
| "Users will be required to use" (redundant) | 1 | 0 — restructured |
| Perplexity boosters added | 0 new | 4 new (`.exe`, PeerJS, Room Code, "which is why") |

### Before / After Comparison

**Flag 45:**
> BEFORE: "The minimum operating system requirement will be Windows 10 (64-bit). This OS environment is needed because the NW.js runtime wrapper, which powers the game's executable, relies on modern 64-bit system components that are not supported in older versions like Windows 7. For mobile users, Android 10 or iOS 14 will be required because the game's web technologies (WebGL 2.0) depend on updated support found in these mobile operating systems."

> AFTER: "The minimum operating system for the desktop version is Windows 10 (64-bit) because NW.js, which packages the game as an .exe file, needs 64-bit system components that older versions like Windows 7 do not have. Mobile users need at least Android 10 or iOS 14 since the browser version of the game runs on WebGL 2.0, and older mobile systems do not support it."

**Flag 46:**
> BEFORE: "Users will be required to use a modern web browser to access the web-deployed version via GitHub Pages. To align with the development environment, the supported browsers will specifically include Chromium-based web browsers such as Google Chrome and Microsoft Edge. These browsers are required because the game's Virtual Numeric Keypad overlay, WebGL rendering, and Peer-to-Peer (P2P) Multiplayer Framework handshake utilize HTML5 and Web Real-Time Communication (WebRTC) standards that are most reliably implemented within these browsers."

> AFTER: "The web-deployed version on GitHub Pages needs a modern Chromium-based browser, specifically Google Chrome or Microsoft Edge, because the game's Virtual Numeric Keypad and P2P Multiplayer handshake through PeerJS both depend on HTML5 and WebRTC support. These two browsers handle WebGL rendering and the Room Code connection most consistently, which is why the proponents chose them as the supported platforms."

### Key Changes Per Flag

**Flag 45:**
1. Merged 3 sentences → 2 compound sentences: "...requirement will be Windows 10 (64-bit). This OS environment is needed because..." → "...is Windows 10 (64-bit) because NW.js, which packages the game as an .exe file, needs..."
2. "will be" × 2 → present tense: "is", "need"
3. "relies on modern 64-bit system components that are not supported" → "needs 64-bit system components that older versions...do not have" — plain, Angel-level
4. "depend on updated support found in these mobile operating systems" → "runs on WebGL 2.0, and older mobile systems do not support it" — concrete + blunt ending
5. `.exe` added as perplexity booster; "since" used as Angel's justification connector

**Flag 46:**
1. Collapsed 3 sentences → 2: merged the opener and browser list into one compound sentence
2. "Users will be required to use" → "needs" — eliminated redundancy and "will"
3. "To align with the development environment" (filler) → dropped entirely
4. "utilize" → restructured to avoid the word entirely ("depend on")
5. Rule of Three broken: "...overlay, ...rendering, and ...handshake" → collapsed Virtual Numeric Keypad and P2P handshake as two items
6. "most reliably implemented within these browsers" → "most consistently, which is why the proponents chose them" — Angel phrasing + reasoning
7. Perplexity: PeerJS, Room Code added

### Academic Compliance Check

- [x] No first person / "the team"
- [x] No contractions
- [x] 2 complete sentences per paragraph (within 2–5 range)
- [x] No banned Cat 1A words (utilize, engage, leverage, facilitate)
- [x] No banned Cat 7 words (efficient, effective, innovative)
- [x] "will" = 0 occurrences
- [x] No rhetorical question openers
- [x] No colon setup-payoff
- [x] No Rule of Three
- [x] No -ing tail clauses
- [x] User's manual edit (macOS removal) preserved

### Estimated Turnitin Impact

Flags 45–46 are 🟡 Medium priority — two consecutive paragraphs in one sliding window. Eliminating 4× "will", 1× "utilize", the Rule of Three, and the filler transition cleans up the entire § 3.2.2 Software section. **Estimated impact: ~1–2% score reduction.**
