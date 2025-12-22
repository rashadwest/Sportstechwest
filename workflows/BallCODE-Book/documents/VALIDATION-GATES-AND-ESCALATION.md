# Validation Gates + Escalation Rules (BallCODE Fully Integrated System)

**Purpose:** Define pass/fail checks so the robot can build, deploy, and report with near-zero human intervention.

## How gates work
- **Green (PASS):** robot proceeds automatically.
- **Yellow (WARN):** robot proceeds but logs + notifies.
- **Red (FAIL):** robot stops and escalates to human.

## Gate 1 — Book Packet Validity
**Input:** `documents/BOOK-PACKET-TEMPLATE.json` shape (or equivalent packet).

**PASS when:**
- Required fields exist: `packet_version`, `book.book_number`, `book.title`, `book.description`, `book.grade_bands`, `commerce.channel_priority`

**WARN when:**
- Optional fields missing (assets/game links) but not required for the current release.

**FAIL when:**
- JSON is invalid
- Required fields missing/empty

**Escalate message:**
- "Book packet invalid: missing [field]. Provide corrected packet or fill required metadata."

---

## Gate 2 — Assets & Paths
**PASS when:**
- Any referenced local asset paths exist (thumbnail/video if provided)

**WARN when:**
- Asset paths are omitted (we can proceed with fallback visuals)

**FAIL when:**
- Asset paths are provided but files do not exist

**Escalate message:**
- "Missing assets referenced by packet: [paths]."

---

## Gate 3 — Curriculum Schema Integrity
**Source of truth:** `curriculum-schema.json`

**PASS when:**
- File exists and is valid JSON
- Schema contains the book entry or can be updated deterministically

**WARN when:**
- Schema exists but missing optional enrichment fields

**FAIL when:**
- File missing or invalid JSON

**Escalate message:**
- "Curriculum schema missing/invalid; cannot safely update integrations."

---

## Gate 4 — Game Level Data Integrity
**Source of truth:** `Unity-Scripts/Levels/`

**PASS when:**
- Any `game.levels[].level_id` referenced in the packet exists as a JSON file (or is generated in the same run)

**WARN when:**
- Packet omits level list (book can still publish; game deep links may be incomplete)

**FAIL when:**
- Packet references level IDs that cannot be found or generated

**Escalate message:**
- "Game level JSON missing for referenced level_id(s): [ids]."

---

## Gate 5 — Website Publish Readiness
**Source of truth:** `BallCode/index.html` + assets folder

**PASS when:**
- `BallCode/index.html` exists
- Book card insertion logic succeeds OR placeholder replacement succeeds

**WARN when:**
- Insertion point not found but no destructive changes were made

**FAIL when:**
- Website files missing
- Update operation would be destructive or inconsistent

**Escalate message:**
- "Website publish gate failed (index.html missing or insertion point not found)."

---

## Gate 6 — Build/Deploy Health (automation confidence)
**Signals:** GitHub Actions + Netlify deploy status

**PASS when:**
- Latest GitHub Actions run succeeded AND latest Netlify deploy is in a success state

**WARN when:**
- Credentials not configured (cannot verify automatically)

**FAIL when:**
- Latest build/deploy is failing OR missed schedule exceeds threshold

**Escalate message:**
- "Build/deploy health is RED. Fix build before publishing new content."

---

## Gate 7 — Analytics/Telemetry Backend Readiness (Supabase blocker)
**Goal:** avoid shipping telemetry features against a mismatched DB schema.

**PASS when:**
- Required columns exist in Supabase (example blocker: missing cache columns)

**WARN when:**
- Telemetry is disabled for this release (ship content without telemetry)

**FAIL when:**
- Telemetry is required for the pilot/school deliverable AND DB schema is not ready

**Escalate message:**
- "Supabase schema mismatch. Apply SQL migration to add missing columns before enabling telemetry."

---

## Automation hook
- Use `scripts/validate-release.py` as the robot’s pre-flight check.
- n8n should run validation before any deploy step.

