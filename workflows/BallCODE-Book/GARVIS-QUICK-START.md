# Garvis Quick Start
## Get Started in 30 Seconds

**Garvis = BallCODE's AI Assistant (Like Iron Man's Jarvis)**

---

## 🚀 Quick Start

### Method 1: Command Line (Fastest)

```bash
python scripts/garvis-command.py \
  --one-thing "Your ONE thing here" \
  --tasks "Task 1, Task 2, Task 3"
```

**Example:**
```bash
python scripts/garvis-command.py \
  --one-thing "Complete Book 2 story" \
  --tasks "Write story, Update curriculum, Deploy website"
```

**What happens:**
1. Garvis creates job
2. Garvis starts working
3. You walk away
4. Garvis completes everything
5. You return to done work

---

### Method 2: Chat (Easiest)

In Cursor chat, just say:
```
Garvis: Complete Book 2 story, update curriculum, deploy website
```

Garvis immediately:
- Acknowledges
- Starts working
- Completes everything
- Notifies you when done

---

### Method 3: File-Based (For Complex Requests)

1. Edit `GARVIS-REQUEST.md`:
```markdown
# Garvis Request

**ONE Thing:** Complete Book 2 story

**Tasks:**
1. Write story
2. Update curriculum
3. Deploy website
```

2. Run:
```bash
python scripts/garvis-command.py --file GARVIS-REQUEST.md
```

---

## 📊 Check Status

```bash
# List recent jobs
python scripts/garvis-command.py --list

# Check specific job
python scripts/garvis-command.py --status garvis-abc12345

# View dashboard
python scripts/garvis-dashboard.py
```

---

## ⚠️ If Garvis Asks a Question

```bash
# See what Garvis needs
python scripts/garvis-escalation.py --list

# Answer the question
python scripts/garvis-escalation.py --resolve garvis-abc12345 "Your answer"
```

---

## 🎯 Remember

**Garvis is autonomous:**
- You give ONE thing + tasks
- You walk away
- Garvis completes everything
- You return to done work

**That's it! Set it and forget it.**

---

**For more details:** See `GARVIS-SYSTEM-GUIDE.md`


