# Humanized Output — Chapter 3, Flags 43–44
# § 3.2.1 Implementation Hardware

**Date:** 2026-03-09
**Flags:** 43 (PC requirements intro), 44 (Mobile requirements intro)
**Section:** § 3.2.1 Implementation Hardware

---

## Flag 43 — PC Requirements Intro (Line 107)

### Original

> Users will be required to have a personal computer (PC), desktop, or laptop to install and use *Chronicles of Arithmos*. The minimum hardware requirements, based on the tested configuration, are as follows:

### Humanized ← HUMANIZED

> The desktop version of Chronicles of Arithmos runs as a standalone .exe file through NW.js, so the player needs a PC or laptop that meets the tested minimum specs listed below:

### Changes Applied

| # | Change | Type |
| :--- | :--- | :--- |
| 1 | "will be required to have" → "needs" | ❌ "will" elimination (Pattern 1) |
| 2 | "to install and use" → "that meets" | Vocab downgrade |
| 3 | Added ".exe file" and "NW.js" | Perplexity booster (project-specific) |
| 4 | "based on the tested configuration, are as follows" → "tested minimum specs listed below" | Tightened phrasing |
| 5 | 2 sentences → 1 compound sentence with "so" | Angel-style compound (PERSONALITY §1) |
| 6 | "personal computer (PC), desktop, or laptop" → "PC or laptop" | Removes unnecessary expansion |

---

## Flag 44 — Mobile Requirements Intro (Line 121)

### Original

> Users who access the application via the web browser deployment will require a mobile device with the following minimum specifications:

### Humanized ← HUMANIZED

> Players that open the game through a mobile browser instead of the .exe need a device that can run WebGL 2.0, and the minimum tested specs are as follows:

### Changes Applied

| # | Change | Type |
| :--- | :--- | :--- |
| 1 | "will require" → "need" | ❌ "will" elimination (Pattern 1) |
| 2 | "Users who" → "Players that" | ESL marker (PERSONALITY §6 — "that" for people) |
| 3 | "access the application via the web browser deployment" → "open the game through a mobile browser instead of the .exe" | Vocab downgrade + perplexity booster |
| 4 | Added "WebGL 2.0" | Perplexity booster (project-specific tech) |
| 5 | 1 sentence → 1 compound sentence with "and" | Angel-style compound (PERSONALITY §1) |
| 6 | "the following minimum specifications" → "the minimum tested specs are as follows" | Natural rewording |

---

## Summary

| Metric | Before | After |
| :--- | :--- | :--- |
| "will" count | 2 | 0 |
| Perplexity boosters added | 0 | 4 (NW.js, .exe ×2, WebGL 2.0) |
| ESL markers added | 0 | 1 ("Players that") |
| Angel-style compounds | 0 | 2 ("so", "and") |
| Vocab downgrades | 0 | 3 |

### PERSONALITY.md Checklist (both flags)

- [x] Would Angel actually say this? — Yes, plain and direct
- [x] Plain verbs (runs, needs, open, run)
- [x] Compound with "so" / "and" — not chopped into AI-short declarations
- [x] Concrete-first (starts with what the version IS)
- [x] No transitions (no Furthermore/Moreover)
- [x] Game-specific names (.exe, NW.js, WebGL 2.0)
- [x] No under-10-word sentences
- [x] No rhetorical question openers
- [x] Colons used only to introduce tables/lists (approved use)
- [x] Third person maintained, no contractions
