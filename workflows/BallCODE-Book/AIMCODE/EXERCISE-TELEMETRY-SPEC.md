## Exercise Telemetry Spec (Pilot)

### Scope (Pilot 3 Exercises)
- E1: Possession State Tracker (Episode 1)
- E2: Conditional Reads Drill (Episode 2)
- E3: Loop Timing Lanes (Episode 3)

### Events
- exercise_started {exercise_id, episode, user_id?, ts}
- exercise_completed {exercise_id, success, attempts, duration_ms, ts}
- step_event {exercise_id, step_id, outcome, duration_ms, ts}

### Metrics
- Success rate = completed(success=true)/started
- Time-to-completion (p50, p90)
- Attempts per completion (mean)

### Privacy
- Aggregate only; no PII stored in repo
- Export CSV summary weekly for BML review

### Mapping
- E1 → Story-first score correlation (episode PR)
- E2/E3 → Difficulty calibration notes



