# Automated Commands — BallCODE Story Series (Claude + Notion MCP)

Copy/paste each block into Claude Desktop with Notion MCP connected. Run sequentially.

---

## 1) Create the Story Database
```
Use Notion MCP to create a new database with these properties:

Database Name: "BallCODE Story Series"

Properties:
- Title (Title)
- Status (Select): Idea, Outline, Draft, In Review, Edited, Final, Published
- Episode # (Number)
- Episode Title (Text)
- Act Structure (Multi-select): Setup, Confrontation, Resolution
- Setting (Text)
- Monster/Villain (Text)
- Basketball Focus (Select): PnR, Closeout, Transition, Press Break, Zone Attack, Post, Off-ball, Rebounding, Free Throws, End-Game
- Coding Concept (Select): Conditionals, Loops, Functions, Arrays, Maps, Algorithms, Debugging, Schemas, State, Events, Optimization, AI-in-the-loop
- Math Concept (Select): Percentages, Probability, EV, Sequences, Statistics, Combinatorics, Graphs, Bayes, Regression, Optimization
- AI Mechanic (Select): Prompting, Tool-use, Retrieval, Classification, Simulation, Vision, Confidence
- Learning Objectives (Text)
- Plot Summary (Text)
- Climax Challenge (Text)
- Exercises (Text)
- Assets Needed (Multi-select): Court art, Monster art, Play diagram, Code diagram, Cover, Badge
- Glif Prompts (Text)
- Word Count (Number)
- Completion % (Number)
- Date Started (Date)
- Date Completed (Date)

Return the database ID and URL.
```

---

## 2) Create Episode Pages (Shell + Template Body)

For each episode below, create a new page with the given properties and set the page body to the provided template content.

### Episode 1 — The Tip-off Trial (Intro)
```
Use Notion MCP to create a new page in the "BallCODE Story Series" database with:
Title: "Episode 1: The Tip-off Trial"
Status: Outline
Episode #: 1
Episode Title: "The Tip-off Trial"
Setting: "Data Court — Center Circle"
Monster/Villain: "Shadow Press Scouts"
Basketball Focus: Transition
Coding Concept: State
Math Concept: Statistics
Learning Objectives: "Understand state and possession flow; introduce world + crew"

Then replace the page body with the Episode Template from `/workflows/BallCODE-Book/Notion-Story-Database-Setup.md`, filling Premise and Story Beats to match the episode.
```

### Episode 2 — The If/Then Fork in the Key (Conditionals)
```
Use Notion MCP to create a new page in the "BallCODE Story Series" database with:
Title: "Episode 2: The If/Then Fork in the Key"
Status: Outline
Episode #: 2
Episode Title: "The If/Then Fork in the Key"
Setting: "The Key — Painted Lane"
Monster/Villain: "Turnover Trolls"
Basketball Focus: PnR
Coding Concept: Conditionals
Math Concept: Probability
Learning Objectives: "Model reads as if/then; handle traps and late switches"

Then replace the page body with the Episode Template content adapted to this story.
```

### Episode 3 — Loop of the Rotating Guardians (Loops)
```
Use Notion MCP to create a new page in the "BallCODE Story Series" database with:
Title: "Episode 3: Loop of the Rotating Guardians"
Status: Outline
Episode #: 3
Setting: "Perimeter Ramparts"
Monster/Villain: "Rotation Wraiths"
Basketball Focus: Closeout
Coding Concept: Loops
Math Concept: Sequences
Learning Objectives: "Practice reps and timing; event loops on catch/drive/help"

Set page body to template content adapted to this story.
```

### Episode 4 — Pattern of the Phantom Zone (Patterns)
```
Use Notion MCP to create a new page in the "BallCODE Story Series" database with:
Title: "Episode 4: Pattern of the Phantom Zone"
Status: Outline
Episode #: 4
Basketball Focus: Zone Attack
Coding Concept: Pattern Recognition
Math Concept: Similarity/feature intuition
```

### Episode 5 — The Ledger of Possessions (Data/State)
```
Use Notion MCP to create a new page ... Episode #: 5 ...
Basketball Focus: Off-ball
Coding Concept: Data Models
Math Concept: Sets/State diagrams
```

### Episode 6 — The Function of Twin Screens (Functions)
```
Use Notion MCP to create a new page ... Episode #: 6 ...
Basketball Focus: Offensive Sets
Coding Concept: Functions
Math Concept: Inputs/Outputs
```

### Episode 7 — Roster of the Rings (Arrays/Lists)
```
Use Notion MCP to create a new page ... Episode #: 7 ...
Basketball Focus: Lineups/Matchups
Coding Concept: Arrays/Lists
Math Concept: Combinatorics
```

### Episode 8 — The Math of the Arc (Percentages)
```
Use Notion MCP to create a new page ... Episode #: 8 ...
Basketball Focus: Shooting
Coding Concept: Stats Pipeline
Math Concept: Percentages/EV basics
```

### Episode 9 — Algorithm of the Final Play (Algorithms)
```
Use Notion MCP to create a new page ... Episode #: 9 ...
Basketball Focus: ATO/End-game
Coding Concept: Algorithms
Math Concept: Markov chains/Optimization
```

### Episode 10 — The Debugging Dungeon (Debugging)
```
Use Notion MCP to create a new page ... Episode #: 10 ...
Basketball Focus: Film Review
Coding Concept: Debugging
Math Concept: Error analysis
```

### Episode 11 — The Schema Forge (Schemas)
```
Use Notion MCP to create a new page ... Episode #: 11 ...
Basketball Focus: System Upgrade
Coding Concept: Schemas
Math Concept: Graphs/Entropy
```

### Episode 12 — The AI Oracle (End-to-End)
```
Use Notion MCP to create a new page ... Episode #: 12 ...
Basketball Focus: Integrated Game Plan
Coding Concept: AI-in-the-loop
Math Concept: Metrics/Calibration
```

---

## 3) Link All Episodes in the Series Overview
```
Use Notion MCP to create a new page in the "BallCODE Story Series" database titled:
"Series Overview: BallCODE — Unlocking the Secret Code of Sport and Beyond"
Status: Outline
Episode #: 0

Then add a Table of Contents linking episodes 1–12 via @ mentions, plus production views guidance.
```

---

## Notes
- Use `/workflows/BallCODE-Book/Story-Premises-For-12-Episodes.md` to fill Premise/Beats.
- Use `/workflows/BallCODE-Book/Character-and-World-Bible.md` for names, locations, rules.






