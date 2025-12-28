# Book 3 Plan — Embedded Micro-Exercises + Game Drill Mapping

**Book:** 3 — The Pattern (In & Out Dribble) / The Deception Loop  
**Core concept:** Loops and repetition (pattern → expectation → break)  
**Target:** Short chapter book (1,200–1,800 words)  

---

## ELI10 goal
Kids should feel this loop:

1) Read a story moment
2) Do a tiny coding exercise right there in the book
3) Play the matching drill in the game
4) Come back to the book knowing what happened and why

---

## Non-negotiables (AIMCODE CLEAR)
- **Basketball-first**: story drives the skill (no “today we learn loops” openings)
- **Micro-exercises are small** (30–120 seconds)
- **Every micro-exercise maps to a game drill** (same concept, real practice)
- **Reuse existing Book 3 game URL** (no extra routing needed initially)

---

## Base game drill URL (Book 3)
- Base: `ballcode.co/play?book=3&exercise=deception-loop&source=book`
- **Implementation note:** For now, treat drills as **steps/variants** inside the same exercise using `&step=`.

---

## ID conventions (stable + reusable)
- **Book micro-exercise ID:** `B3-A{act}-S{scene}-E{num}`
- **Game drill ID:** `G-B3-A{act}-S{scene}-D{num}`

---

## The 7 micro-exercises + drill mapping (single source of truth)

| Micro ID | Act/Scene | Skill spotlight | Student prompt (in-book) | Expected answer (teacher-facing) | Game drill ID | Game URL |
|---|---|---|---|---|---|---|
| B3-A1-S1-E1 | Act I / Scene 1 | Repetition | In Nova’s pattern, which move repeats 3 times? | Fake left | G-B3-A1-S1-D1 | `ballcode.co/play?book=3&exercise=deception-loop&source=book&step=1` |
| B3-A1-S1-E2 | Act I / Scene 1 | Counting repeats | If Nova repeats a fake 3 times, how many fakes happened? | 3 | G-B3-A1-S1-D2 | `ballcode.co/play?book=3&exercise=deception-loop&source=book&step=2` |
| B3-A2-S1-E1 | Act II / Scene 1 | Loops (Blocks) | Fill the blank: `REPEAT [ ____ ] 3 TIMES, THEN [go right]` | fake left | G-B3-A2-S1-D1 | `ballcode.co/play?book=3&exercise=deception-loop&source=book&step=3` |
| B3-A2-S1-E2 | Act II / Scene 1 | Trace loops (Python preview) | How many times does `fake_left()` run? `for i in range(3): fake_left()` | 3 | G-B3-A2-S1-D2 | `ballcode.co/play?book=3&exercise=deception-loop&source=book&step=4` |
| B3-A2-S1-E3 | Act II / Scene 1 | Debugging repeats | Story needs 3 fakes but code uses `range(2)`. What should it be? | change to `range(3)` | G-B3-A2-S1-D3 | `ballcode.co/play?book=3&exercise=deception-loop&source=book&step=5` |
| B3-A3-S1-E1 | Act III / Scene 1 | Pattern choice | Which pattern best matches Book 3? A) 1 fake B) 3 fakes C) 10 fakes | B | G-B3-A3-S1-D1 | `ballcode.co/play?book=3&exercise=deception-loop&source=book&step=6` |
| B3-A3-S1-E2 | Act III / Scene 1 | Parameterize loops | Update the loop to repeat 4 times (blocks or Python). | repeatCount=4 / `range(4)` | G-B3-A3-S1-D2 | `ballcode.co/play?book=3&exercise=deception-loop&source=book&step=7` |

---

## Curriculum linkage (Phase 1 → 2 → 3)
For each micro-exercise:
- **Phase 1 (Blocks):** show the loop as a repeat block + count
- **Phase 2 (Bridge):** show side-by-side block ↔ `for i in range(n)`
- **Phase 3 (Python):** show (or write, for older learners) the loop code

Grade simplification:
- **Grades 3–5:** focus on pattern + counting + blocks; Python is “look only.”
- **Grades 6–8:** blocks + bridge + simple Python writing for the loop.

---

## Production checklist (Book 3)

### Book writing checklist
- [ ] Act I written (sets conflict + introduces repetition)
- [ ] Act I includes B3-A1-S1-E1 and B3-A1-S1-E2 in the right place
- [ ] Act II written (teaches loop pattern + why it works)
- [ ] Act II includes B3-A2-S1-E1/E2/E3
- [ ] Act III written (applies loop under pressure)
- [ ] Act III includes B3-A3-S1-E1/E2
- [ ] Each micro-exercise is under 120 seconds
- [ ] Each micro-exercise has an obvious match to its game drill

### Game drill checklist (design-ready)
- [ ] Deception Loop Challenge supports `step=1..7` (or equivalent internal progression)
- [ ] Step 1–2: repetition recognition + counting
- [ ] Step 3: block-loop completion
- [ ] Step 4: trace loop count
- [ ] Step 5: fix wrong repeat count
- [ ] Step 6: choose best pattern
- [ ] Step 7: change repeat count to 4

### Integration checklist (later execution)
- [ ] Website Book 3 page links to base URL (and optionally step)
- [ ] Game return flow returns to Book 3 page with success + score
- [ ] Book page unlocks the next section on success

---

## Notes (keep it simple now)
- We are not creating multiple separate game URLs yet; we keep a single Book 3 exercise and treat each drill as a step.
- When the return-flow/progress system is finalized, these micro IDs become the unit of tracking (what was completed, when, with what score).


