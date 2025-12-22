# ⚡ Quick Command Reference
## All BallCODE Commands at a Glance

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** January 2025  
**Purpose:** Quick reference for all BallCODE commands  
**Status:** ✅ Active Reference

---

## 🌅 DAILY WORKFLOW

### Morning Questions
```bash
python scripts/daily-morning-questions.py --morning
```
**With n8n status:**
```bash
python scripts/daily-morning-questions.py --with-n8n
```
**Short form:**
```bash
python scripts/daily-morning-questions.py -m
```

**What it does:** Shows 10 daily workflow questions + yesterday's summary + n8n status

---

## 🎯 UNIFIED PROMPTING FRAMEWORK

### Quick Mode (5 Questions)
```bash
python scripts/ask_unified_questions.py --quick
```
**Short form:**
```bash
python scripts/ask_unified_questions.py -q
```

### Full Mode (23 Questions)
```bash
python scripts/ask_unified_questions.py --full
```
**Short form:**
```bash
python scripts/ask_unified_questions.py -f
```

**What it does:** Shows prompting framework questions before tasks

---

## 📊 N8N WORKFLOW STATUS

### Check All Workflows
```bash
./scripts/check-n8n-status.sh
```

### Daily n8n Report
```bash
./scripts/daily-n8n-report.sh
```

### Diagnose Orchestrator
```bash
./scripts/diagnose-orchestrator.sh
```

### Test Screenshot Fix
```bash
./scripts/test-screenshot-fix.sh
```

### Test All Webhooks
```bash
./scripts/test-all-webhooks.sh
```

---

## 🚀 N8N WORKFLOW TRIGGERS

### Unity Build Orchestrator
```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Build request", "branch": "main"}'
```

### Full Integration
```bash
curl -X POST http://192.168.1.226:5678/webhook/ballcode-dev \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Your development prompt", "mode": "quick"}'
```

### Screenshot Fix
```bash
curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl": "https://example.com/error.png", "context": "Error description"}'
```

---

## 📚 DOCUMENTATION

### Main References:
- **`BALLCODE-N8N-COMMAND-REFERENCE.md`** - Complete n8n workflow guide
- **`DAILY-MORNING-COMMAND-GUIDE.md`** - Daily morning questions guide
- **`UNIFIED-PROMPTING-COMMAND.md`** - Unified prompting framework guide
- **`FULL-INTEGRATION-USAGE-GUIDE.md`** - Full Integration usage
- **`SCREENSHOT-WORKFLOW-TESTING-GUIDE.md`** - Screenshot testing

---

## 💡 TYPICAL DAILY WORKFLOW

### Morning:
```bash
# 1. Get daily questions
python scripts/daily-morning-questions.py --with-n8n

# 2. Copy output and paste into chat
# 3. Answer questions in chat
```

### Before Each Task:
```bash
# Get prompting questions
python scripts/ask_unified_questions.py --quick
```

### Check Status:
```bash
# Check n8n workflows
./scripts/check-n8n-status.sh
```

---

## 🎯 COMMAND PATTERNS

### Pattern 1: Daily Morning
- **Command:** `--morning` or `-m`
- **Script:** `daily-morning-questions.py`
- **Use:** Every morning to start your day

### Pattern 2: Before Tasks
- **Command:** `--quick` or `-q` (fast) / `--full` or `-f` (comprehensive)
- **Script:** `ask_unified_questions.py`
- **Use:** Before starting any task

### Pattern 3: n8n Status
- **Command:** Various (check, diagnose, test)
- **Scripts:** `check-n8n-status.sh`, `daily-n8n-report.sh`, etc.
- **Use:** Monitor and manage n8n workflows

---

## 🔄 ALIASES (Optional)

**Add to `~/.zshrc` or `~/.bashrc`:**

```bash
# Daily workflow
alias morning='cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book && python scripts/daily-morning-questions.py --with-n8n'

# Unified prompting
alias quick='cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book && python scripts/ask_unified_questions.py --quick'
alias full='cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book && python scripts/ask_unified_questions.py --full'

# n8n status
alias n8n-status='cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book && ./scripts/check-n8n-status.sh'
```

**Then use:**
```bash
morning    # Daily questions
quick      # Quick prompting questions
full       # Full prompting questions
n8n-status # Check n8n workflows
```

---

**Version:** 1.0  
**Created:** January 2025  
**Status:** ✅ Active Reference

