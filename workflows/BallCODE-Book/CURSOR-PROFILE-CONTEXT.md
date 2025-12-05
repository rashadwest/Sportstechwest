# BallCODE Picture Book Project — Complete Context for Cursor Profile

**Use this file to create a dedicated Cursor profile for the BallCODE book project.**

---

## Project Overview

**Title:** BallCODE: Unlocking the Secret Code of Sport and Beyond  
**Format:** Picture book (spreads with story + visuals + game integration)  
**Target Audience:** Elementary & Middle school students (grades 3–8); teachers/parents welcome  
**Tone:** Story-first, adventurous, practical learning  
**Structure:** 12 self-contained episodes (read in any order), plus appendices

**Core Concept:** Teach kids how AI, data science, and coding work by turning basketball plays into robot-style decisions they can see, read, and play.

**Tagline:** "Learn how robots think—through the game you love."

**CRITICAL FRAMEWORK:** Basketball stories are the FRAMEWORK/VEHICLE for teaching AI, math, and coding—not the subject being taught. Every episode uses engaging basketball narratives to naturally introduce and teach these concepts. See `Basketball-Story-Framework-Guide.md` for complete framework approach.

---

## Key Principles

### Story-First Hybrid Approach
- **70% story, 30% skill inserts** (mostly story to maximize engagement)
- Each episode: Story spread → Skill Pit‑Stop (mini-lesson) → Try‑It in existing BallCODE game → Optional Mastery Lab
- CTAs placed only in Skill Pit‑Stop and end-of-chapter (never mid‑story)

### Game Integration
- **Exercises use existing BallCODE game system** (no new mini-games needed)
- Flow: Read story → Skill Pit‑Stop explains concept → QR/short URL launches Try‑It drill in game → Complete drill → Unlock next spread extras
- No-login first play → "save progress" prompt after success
- Each episode has unique drill link/QR code
- "Continue in-game" link at end of chapter for longer missions

### Picture Book Format
- Each spread = story panel + visual + QR/short URL to BallCODE game exercise
- Visuals: play diagrams, code/pseudocode diagrams, character/monster art
- Age-appropriate: 60–90s puzzles, no login required for first play

---

## Episode Structure (12 Episodes)

Each episode includes:
- **Premise** (2–3 sentences hook)
- **Story Beats** (Act I/II/III breakdown)
- **On-Court Objective** (plain language basketball goal)
- **Coding Concept** (e.g., If/Else, Loops, Functions, Arrays, Algorithms, Schemas)
- **Math Concept** (e.g., Percentages, EV, Probability, Sequences)
- **AI Mechanic** (optional: how AI helps with guardrails)
- **Climax Challenge** (single problem tying it all together)
- **Exercises** (A short, B applied, C stretch)
- **Assets** (play diagram, code diagram, images)
- **Glif Prompts** (for generating visuals)

---

## All 12 Episodes

### Episode 1: The Tip-off Trial (State & Flow)
**Premise:** Win first advantage by managing possession state from tip through transition.  
**Story Beats:**
- Act I: Meet the crew; tip-off chaos; possession changes feel like glitches.
- Act II: Shadow Press Scouts force turnovers; Nova tracks states.
- Act III: Controlled outlet → fill lanes → safe entry to set.
**On-Court Objective:** Clean transition into half-court without a turnover.  
**Coding Concept:** State (start/live/dead/outcome)  
**Math Concept:** Possession count, turnovers (basic stats)  
**AI Mechanic:** Vision cue detects state shifts; player confirms.  
**Climax Challenge:** Maintain correct state across 3 linked actions.  
**Exercises:** A) Label states in a play; B) Write state transitions; C) Handle an edge case.  
**Assets:** Court map (center circle), Scouting monsters, state diagram.  
**Glif Prompts:** Center court tip, transition lanes, state overlay.

### Episode 2: The If/Then Fork in the Key (Conditionals)
**Premise:** Beat traps using if/else reads in pick-and-roll.  
**Story Beats:** Setup in The Key; Turnover Trolls bait passes; counters unlock.  
**On-Court Objective:** Make the correct read vs trap/switch/ice.  
**Coding Concept:** If/Else decision tree (6 branches)  
**Math Concept:** Option probabilities; expected success  
**AI Mechanic:** Coverage advisor proposes 3 options with confidence.  
**Climax Challenge:** Choose and execute the best branch under time.  
**Exercises:** A) Truth table; B) Code pseudo-read; C) Add an edge-case rule.  
**Assets:** PnR diagram; decision tree visual.  
**Glif Prompts:** Painted lane with branching arrows.

### Episode 3: Loop of the Rotating Guardians (Loops)
**Premise:** Sustain perfect closeouts with rotation loops.  
**Story Beats:** Perimeter passes test timing; Rotation Wraiths exploit delays; loop discipline wins.  
**On-Court Objective:** Maintain rotation invariant across 5 passes.  
**Coding Concept:** For/While loops, invariant; break/continue  
**Math Concept:** Sequences; time-to-event  
**AI Mechanic:** Latency penalties simulate late steps.  
**Climax Challenge:** Hold the invariant; no open corner.  
**Exercises:** A) Write loop; B) Add timing check; C) Handle drive event.  
**Assets:** Shell drill diagram; timing chart.  
**Glif Prompts:** Defensive rotation ring around arc.

### Episode 4: Pattern of the Phantom Zone (Pattern Recognition)
**Premise:** Detect zone patterns and attack the seam.  
**Story Beats:** Zone Phantoms morph; crew tags cues; seam attack breaks illusions.  
**On-Court Objective:** Identify zone and hit best seam action.  
**Coding Concept:** Rule-based detectors → patterns  
**Math Concept:** Similarity/features  
**AI Mechanic:** Feature tags increase seam score.  
**Climax Challenge:** Choose correct seam within 2 passes.  
**Exercises:** A) List cues; B) Write detector rules; C) Compare two zones.  
**Assets:** 2-3 and 1-3-1 overlays; seam arrows.  
**Glif Prompts:** Phantom zone with highlighted cues.

### Episode 5: The Ledger of Possessions (Data Models)
**Premise:** Model a possession that can replay.  
**Story Beats:** Archive of Plays; Data Golems demand fields; replay proves model.  
**On-Court Objective:** Track off-ball actions to free shooter.  
**Coding Concept:** Entities, enums, state transitions  
**Math Concept:** Sets/state diagrams  
**AI Mechanic:** Auto-log actions from narration.  
**Climax Challenge:** Minimal JSON that fully replays the possession.  
**Exercises:** A) Define fields; B) Validate schema; C) Add one new field + reason.  
**Assets:** Data table; possession state chart.  
**Glif Prompts:** Ledger with court replay.

### Episode 6: The Function of Twin Screens (Functions)
**Premise:** Call sets like functions with counters.  
**Story Beats:** Hedge Hydra disrupts; counters as functions; precision wins.  
**On-Court Objective:** Choose correct counter vs hedge/switch/under.  
**Coding Concept:** Function signature; pre/postconditions  
**Math Concept:** Inputs/outputs  
**AI Mechanic:** Preconditions check; suggest counter if valid.  
**Climax Challenge:** Execute stagger → counter under pressure.  
**Exercises:** A) Spec; B) Tests; C) Add new counter.  
**Assets:** Stagger set diagram; function spec visual.  
**Glif Prompts:** Twin screens with labeled params.

### Episode 7: Roster of the Rings (Arrays/Lists)
**Premise:** Pick best five for the job using collections.  
**Story Beats:** Sprites scramble lineups; filters restore order; ranking decides.  
**On-Court Objective:** Build top-3 lineups for end-game goals.  
**Coding Concept:** Arrays/lists; filter/sort  
**Math Concept:** Combinatorics  
**AI Mechanic:** Weighted ranking with constraints.  
**Climax Challenge:** Submit top lineup + justification.  
**Exercises:** A) Filters; B) Weights; C) Tie-break strategy.  
**Assets:** Roster board; ranking table.  
**Glif Prompts:** Rings with player names/metrics.

### Episode 8: The Math of the Arc (Percentages/EV)
**Premise:** Choose shots by percentages and EV.  
**Story Beats:** Variance Viper tempts heat checks; EV plan beats streaks.  
**On-Court Objective:** Select highest EV sequence of 3 shots.  
**Coding Concept:** Simple stat pipeline  
**Math Concept:** Percentages; EV  
**AI Mechanic:** Compute EV with context weights.  
**Climax Challenge:** Beat timer with EV-positive choices.  
**Exercises:** A) Compute EV; B) Add context weight; C) Risk/variance analysis.  
**Assets:** Shot chart; EV table.  
**Glif Prompts:** Arc observatory with graphs.

### Episode 9: Algorithm of the Final Play (Algorithms)
**Premise:** Pick an end-game algorithm and test it.  
**Story Beats:** Shot Clock Titan compresses time; greedy vs dynamic; simulation decides.  
**On-Court Objective:** Generate final-shot play.  
**Coding Concept:** Algorithms (greedy/dp)  
**Math Concept:** Markov chain intuition; optimization  
**AI Mechanic:** Simulate 100 possessions; report metrics.  
**Climax Challenge:** Choose algorithm + justify via metrics.  
**Exercises:** A) Define states; B) Greedy baseline; C) DP variant.  
**Assets:** ATO board; sim metrics chart.  
**Glif Prompts:** Clock titan looming over play.

### Episode 10: The Debugging Dungeon (Debugging)
**Premise:** Fix a recurring turnover with structured debugging.  
**Story Beats:** Film caverns reveal logs; assertions catch bug; fix holds.  
**On-Court Objective:** Remove root cause of turnover pattern.  
**Coding Concept:** Trace logs, assertions, guards  
**Math Concept:** Error rates  
**AI Mechanic:** Summarize logs; propose guards.  
**Climax Challenge:** Apply 3-step fix preventing the bug.  
**Exercises:** A) Trace; B) Guard; C) Prove with test.  
**Assets:** Log sheet; before/after diagram.  
**Glif Prompts:** Gremlins fleeing from fixes.

### Episode 11: The Schema Forge (Schemas)
**Premise:** Upgrade the model to capture advantage and gravity.  
**Story Beats:** Entropy Elemental melts meaning; schema v2 restores clarity.  
**On-Court Objective:** Improve decisions using upgraded fields.  
**Coding Concept:** Schema migration  
**Math Concept:** Graphs; entropy/signal  
**AI Mechanic:** Backfill new fields from past plays.  
**Climax Challenge:** v1→v2 migration + proof of better calls.  
**Exercises:** A) Field design; B) Backfill rule; C) Evaluation metric.  
**Assets:** ERD; before/after decision map.  
**Glif Prompts:** Forge, runes for fields.

### Episode 12: The AI Oracle (End-to-End)
**Premise:** Use an assistant safely for live calls.  
**Story Beats:** Oracle tests guardrails; crew sets confidence + why + fallback; win.  
**On-Court Objective:** Integrate assistant without losing control.  
**Coding Concept:** AI-in-the-loop with guardrails  
**Math Concept:** Metrics; calibration  
**AI Mechanic:** Confidence threshold; rationale; fallback action.  
**Climax Challenge:** Win using assistant with safeguards.  
**Exercises:** A) Prompt spec; B) Failure fallback; C) Post-game calibration.  
**Assets:** Assistant UI mock; decision dashboard.  
**Glif Prompts:** Oracle's court with data aura.

---

## Character & World Bible

### Main Crew
- **Nova** (PG, protagonist): fast processor, sees the court like code; leadership arc.
- **Atlas** (Wing): strength and balance; screens and cuts with precision.
- **Pixel** (Guard): sharpshooter; pattern-spotter; comic relief.
- **Anchor** (Big): seals space; protects paint; gentle giant.
- **Coach Circuit:** mentor who translates basketball into code language.
- **Arc** (AI assistant): gives hints with confidence + why; never replaces decisions.

### Antagonists / Monsters
- **Shadow Press Scouts:** create chaos in transition; punish bad state.
- **Turnover Trolls:** bait risky passes; punish poor conditionals.
- **Rotation Wraiths:** appear where rotations are late.
- **Zone Phantoms:** morphing shapes; test pattern recognition.
- **Data Golems:** rigid rules; test modeling quality.
- **Hedge Hydra:** multi-headed screen coverage; requires counters.
- **Substitution Sprites:** scramble lineups; test constraints.
- **Variance Viper:** hot/cold streak illusions; tests EV thinking.
- **Shot Clock Titan:** compresses time; tests algorithm choice.
- **Glitch Gremlins:** hide in habits; cause repeatable errors.
- **Entropy Elemental:** dissolves meaning; tests schema quality.
- **Uncertainty Chimera:** mixes noise and signal; tests AI guardrails.

### Locations
- Data Court (central arena)
- The Key (painted lane)
- Perimeter Ramparts
- Phantom Zone (morphing defenses)
- Archive of Plays (record hall)
- Screenworks Alley
- Locker of Lineups
- Arc Observatory
- Coach's ATO Lab
- Film Caverns
- Forge of Meaning
- Oracle's Court

### World Rules (Basketball → Code)
- **Advantage Gauge:** increases with space/tempo; decreases with turnovers.
- **Gravity Field:** shooters bend defenders; stored as a rating.
- **Tempo Meter:** pace of play; affects latency and decision budgets.
- **Coding Spells:**
  - If/Else = Split Decision
  - Loop = Rotation Ritual
  - Function = Set Call
  - Array = Roster Ring
  - Schema = Meaning Map
- **AI-in-the-loop:** Arc can propose, but players decide. Always require:
  - Confidence score
  - Why explanation
  - Fallback action

### Style Notes
- **Voice:** energetic, respectful, clever; jokes land without sarcasm.
- **Teaching:** show cause/effect in the story first; summarize concepts after.
- **Consistency:** reuse terms (advantage, gravity, tempo) across episodes.

---

## Deliverables per Episode

- **1,000–1,800 word story chapter** (picture book format: shorter text, more visuals)
- **1–2 play diagrams** (basketball court with player movements)
- **1 code/pseudocode diagram** (visual representation of coding concept)
- **3 exercises** (A short, B applied, C stretch) — all use existing BallCODE game system
- **Teacher notes** (objectives, answers, variations) — for classroom pack
- **QR code + short URL** linking to Try‑It drill in game
- **Visual assets:** character/monster art, location maps, episode cover badges

---

## Production Workflow

1. **Outline** → **Draft** → **In Review** → **Edited** → **Final** → **Published**
2. Create play + code diagrams; generate Glif art per episode
3. Link exercises to existing BallCODE game system (no new mini-games)
4. Generate QR codes and short URLs for each Try‑It drill
5. Classroom pack per episode: PDF story, worksheet, diagrams

---

## Notion Structure (for production)

### Database Name
"BallCODE Story Series"

### Properties
- **Title** (Title)
- **Status** (Select): Idea, Outline, Draft, In Review, Edited, Final, Published
- **Episode #** (Number)
- **Episode Title** (Text)
- **Owner** (Person)
- **Word Count** (Number)
- **Story %** (Number 0–100)
- **Assets %** (Number 0–100) — Play Diagram, Code Diagram, Images
- **Review %** (Number 0–100) — peer/coach/QA
- **Completion %** (Formula): `round((prop("Story %") + prop("Assets %") + prop("Review %")) / 3)`
- **Pit‑Stop Ready** (Checkbox)
- **Try‑It Ready** (Checkbox)
- **Mastery Lab Ready** (Checkbox)
- **CTA Linked** (Checkbox)
- **QR Generated** (Checkbox)
- **Try‑It URL** (URL) — link to game exercise
- **Continue In‑Game URL** (URL) — link to longer mission
- **Notes** (Text)
- **Last Update** (Last edited time)

### Page Template Sections
- Premise
- Story Beats (Act I/II/III)
- On-Court Objective
- Coding Concept
- Math Concept
- AI Mechanic
- Climax Challenge
- Exercises (A/B/C)
- Assets (play diagram, code diagram, images)
- Glif Prompts
- Try‑It URL + QR code
- Mastery Lab (optional)

### Dashboard Views
- **Kanban by Status** (grouped, sort by Episode #)
- **Progress Heatmap** (Episode #, Title, Completion %, Story %, Assets %, Review %)
- **Ready to Publish** (filter: Status = Final OR Published)
- **Classroom Readiness** (filter: Mastery Lab Ready AND CTA Linked AND QR Generated)
- **Writing Queue** (filter: Status in [Outline, Draft]; sort by Word Count asc)

### Weekly Rhythm
- **Monday:** update Story %, Assets %, blockers
- **Wednesday:** review queue (In Review → Edited)
- **Friday:** publish candidates + create QR/CTAs

---

## Partner Opportunities

### IBM "Watson Coach" Edition
- In-story AI assistant named "Watson" (instead of "Arc")
- Puzzles focus on: classification, sequencing, simple stats (mean/EV), logic flows
- USP: AI hints + explain-why + "try this block" overlay
- Branding: IBM Watson logo/colors, co-branded cover

### Cisco "Packet Path" Edition
- Themed puzzles: routing choices (if/then), loops for retries, QoS priorities
- Visuals: network nodes/links mapped to basketball court positions
- "Defend the lane" ↔ "Choose best route" analogies
- USP: Network thinking as kid-friendly logic
- Branding: Cisco logo/colors, co-branded cover

### White-Label Considerations
- Partner branding skins (logo, colors, copy toggles)
- Co-branded covers and marketing materials
- Analytics tracking per partner (UTM codes)
- Privacy: COPPA/GDPR-K compliant, minimal data collection

---

## Roadmap

### Phase 1: Basketball Book (Current)
- 12 episodes with picture book format
- Integration with existing BallCODE game system
- QR codes + short URLs for Try‑It drills
- Teacher pack with Mastery Labs

### Phase 2: Soccer Edition (Next)
- Immediately after Basketball, produce Soccer edition
- Same story-first + Skill Pit‑Stop structure
- Reuse Notion database schema; change Basketball Focus → Soccer Focus
- Soccer tactics: Passing Lanes, Press Breakout, Set Pieces, Offside Line, Transition, Finishing, Shape/Spacing
- Adapt episode templates: monsters/locations/themes mapped to soccer decisions
- Keep CTAs and Mastery Labs pattern; new drills point to soccer mini-games
- Target timeline: Outline (2 weeks), Drafts (6–8 weeks), Review/Assets (3–4 weeks), Publish (2 weeks)

### Phase 3: Interactive Web Reader (Future, gated by adoption)
- Web reader where kids read story + play game inline
- Progress sync across devices
- Adaptive difficulty based on performance
- Multi-sport support (basketball, soccer, etc.)

---

## Key Files Reference

- **Plan/Outline:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Story-Series-Plan-and-Outline.md`
- **Chapter Breakdowns:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Story-Chapter-Breakdowns.md`
- **Story Premises:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Story-Premises-For-12-Episodes.md`
- **Character/World Bible:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Character-and-World-Bible.md`
- **Notion Setup Guide:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Notion-Story-Database-Setup.md`
- **Automated Commands:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Automated-Commands-Story.md`

---

## Important Notes

1. **Game System:** All exercises use existing BallCODE game system. No new mini-games need to be built.
2. **Picture Book Format:** Each spread = story panel + visual + QR/short URL to game exercise.
3. **Age Group:** Grades 3–8 (Elementary & Middle school). Keep language accessible, concepts concrete.
4. **Story-First:** 70% story, 30% skill inserts. Maximize engagement while ensuring learning.
5. **CTAs:** Only in Skill Pit‑Stop and end-of-chapter. Never interrupt story flow.
6. **Partner Ready:** Structure supports white-label branding (IBM Watson, Cisco, etc.).
7. **Notion Integration:** All production tracking happens in Notion database with progress formulas and checklists.

---

*Last Updated: January 2025*  
*Project Status: Planning/Development Phase*

