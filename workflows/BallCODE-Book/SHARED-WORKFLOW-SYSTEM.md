# 🔄 Shared Workflow System - Cross-Chat Communication

**Problem Solved:** Daily workflow answers not seen by other chats

**Solution:** Centralized JSON + Markdown files that all chats read/write

---

## 📁 FILE STRUCTURE

### 1. `TODAY-WORKFLOW-DATA.json`
**Purpose:** Machine-readable data for all chats
**Location:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/TODAY-WORKFLOW-DATA.json`
**Updated:** Every session start, every progress update
**Format:** JSON (easy to parse)

### 2. `ONE-THING-TODAY.md`
**Purpose:** Human-readable ONE THING focus
**Location:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/ONE-THING-TODAY.md`
**Updated:** Every session start, when ONE THING changes
**Format:** Markdown (easy to read)

### 3. `DATE-TIME-TRACKER.md`
**Purpose:** Current date/time (DO NOT ASK USER)
**Location:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/DATE-TIME-TRACKER.md`
**Updated:** Automatically by system
**Format:** Markdown

---

## 🔄 HOW IT WORKS

### When Starting a New Chat:

1. **AI reads these files FIRST:**
   - `TODAY-WORKFLOW-DATA.json` - Get all session data
   - `ONE-THING-TODAY.md` - Get the ONE THING focus
   - `DATE-TIME-TRACKER.md` - Get current date/time

2. **AI displays:**
   - Today's ONE THING (prominently)
   - Current date/time (from file, not asking user)
   - Yesterday's completion (from JSON)
   - Critical rules (from JSON)

3. **AI applies rules:**
   - Date/time: Never ask, use file
   - Blockers: Always research solution first
   - Code: Ask if unsure about project specifics
   - Testing: End-to-end after every change

### During Work:

1. **AI updates files when:**
   - Progress is made on ONE THING
   - Blockers are resolved
   - Rules need to be added
   - Status changes

2. **AI checks files:**
   - Before starting any task
   - When encountering blockers
   - When user asks about focus

### End of Day:

1. **AI creates:**
   - `DAILY-WORKFLOW-2025-12-12.md` - Full daily log
   - Updates `TODAY-WORKFLOW-DATA.json` with completion
   - Prepares tomorrow's `ONE-THING-TODAY.md`

---

## 📋 AI PROTOCOL

### At Chat Start:
```markdown
1. Read TODAY-WORKFLOW-DATA.json
2. Read ONE-THING-TODAY.md
3. Read DATE-TIME-TRACKER.md
4. Display ONE THING prominently
5. Show date/time (from file, don't ask)
6. Show yesterday's completion
7. Show critical rules
8. Confirm focus before starting work
```

### During Work:
```markdown
1. Check ONE-THING-TODAY.md before each task
2. Update TODAY-WORKFLOW-DATA.json when progress made
3. Update ONE-THING-TODAY.md when status changes
4. Follow blocker resolution protocol
5. Follow code review protocol
6. Follow end-to-end testing protocol
```

### When Blockers Found:
```markdown
1. DO NOT just report blocker
2. Use R&D online with AIMCODE n8n
3. Find solution
4. Report solution (not just problem)
5. Update TODAY-WORKFLOW-DATA.json with resolution
```

---

## 🎯 ONE THING FOCUS SYSTEM

### How ONE THING is Tracked:

1. **Defined in:** `ONE-THING-TODAY.md`
2. **Status tracked in:** `TODAY-WORKFLOW-DATA.json`
3. **All chats check this first**
4. **All work must align with ONE THING**

### Deviation Protocol:

If user wants to work on something NOT the ONE THING:
1. AI checks `ONE-THING-TODAY.md`
2. AI asks: "This doesn't align with today's ONE THING. Should we update the ONE THING?"
3. If yes → Update both files
4. If no → Proceed but note deviation

---

## 🔧 MAINTENANCE

### Daily:
- Update `TODAY-WORKFLOW-DATA.json` with new date
- Update `ONE-THING-TODAY.md` with new ONE THING
- Archive previous day's files

### Weekly:
- Review system effectiveness
- Update protocols if needed
- Clean up old files

---

## ✅ BENEFITS

1. **No repeated questions** - Date/time saved
2. **Consistent focus** - ONE THING always visible
3. **Cross-chat continuity** - All chats see same data
4. **Rule enforcement** - Rules saved and applied
5. **Progress tracking** - Updates visible to all chats

---

**This system ensures every chat session is focused on the ONE THING and has access to all daily workflow data.**


