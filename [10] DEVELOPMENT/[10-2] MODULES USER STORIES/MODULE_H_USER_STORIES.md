# Module H: Peer-to-Peer (P2P) Multiplayer Framework — User Stories

> Enables drop-in cooperative gameplay without centralized server accounts, allowing players to cooperatively solve math puzzles and fight bosses together.

---

## US-H-001: Room Code Generation (Host)

**As a** host player,
**I want** to generate a text-based Room Code when I create a multiplayer session,
**so that** I can share it with a friend to let them join my game.

**Priority**: High

**Acceptance Criteria**:

- [ ] A "Host Game" or "Create Room" option is accessible from the in-game menu.
- [ ] The system generates a unique, text-based Room Code upon session creation.
- [ ] The Room Code is displayed clearly on screen for the host to share.
- [ ] The Room Code remains active as long as the host session is running.

---

## US-H-002: Join via Room Code (Client)

**As a** joining player,
**I want** to enter a Room Code to connect directly to a host's game session,
**so that** I can join cooperative play without needing a separate account or server login.

**Priority**: High

**Acceptance Criteria**:

- [ ] A "Join Game" or "Enter Code" option is accessible from the in-game menu.
- [ ] The player can type or paste the Room Code using keyboard input.
- [ ] A successful connection merges the joining player's party into the host's game.
- [ ] An error message is displayed if the code is invalid or the host is unavailable.

---

## US-H-003: Cooperative Boss Battles

**As a** player in a multiplayer session,
**I want** to fight bosses cooperatively with my partner,
**so that** we can both solve math equations and contribute to the fight together.

**Priority**: High

**Acceptance Criteria**:

- [ ] Both the host and client participate in the same battle simultaneously.
- [ ] Each player receives their own math equations to solve during their turns.
- [ ] Both players' actions contribute to the shared battle state (boss HP, etc.).
- [ ] Combat follows the same three-step sequence (Select → Solve → Execute) for each player.

---

## US-H-004: Real-Time State Synchronization

**As a** player in a multiplayer session,
**I want** the game state (HP, positions, battle progress) to stay synchronized between both players,
**so that** we both see the same game state and can coordinate effectively.

**Priority**: High

**Acceptance Criteria**:

- [ ] Changes to HP, MP, TP are reflected on both clients in near real-time.
- [ ] Battle damage, healing, and status effects are synchronized.
- [ ] Player positions and map progress are synced between host and client.
- [ ] Desynchronization is handled gracefully (e.g., resyncing on mismatch).

---

## US-H-005: Session Dissolution on Host Disconnect

**As a** joining player,
**I want** to understand that the session will end immediately if the host disconnects,
**so that** I am not confused when the multiplayer session terminates unexpectedly.

**Priority**: Medium

**Acceptance Criteria**:

- [ ] If the host application closes, the session terminates immediately for all connected clients.
- [ ] The client receives a clear message: "Host has disconnected. Session ended."
- [ ] The client is returned to their own single-player game state safely.
- [ ] No data corruption occurs on the client side due to abrupt disconnection.

---

## US-H-006: Known Limitation — Timer Desync Warning

**As a** joining player,
**I want** to be aware that high host latency may cause math timer desyncs,
**so that** I can account for potential timing inconsistencies during cooperative play.

**Priority**: Low

**Acceptance Criteria**:

- [ ] A warning message or tooltip about potential timer desyncs is shown before joining.
- [ ] If significant latency is detected, a subtle on-screen indicator is displayed.
- [ ] Timer desync does not cause crashes or game-breaking errors.
- [ ] The timer penalty system (Module F) makes best-effort adjustments for latency.
