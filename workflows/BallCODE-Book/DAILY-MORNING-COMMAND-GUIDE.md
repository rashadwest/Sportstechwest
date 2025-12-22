# 🌅 Daily Morning Questions - Command Guide
## How to Get Your Daily Workflow Questions Every Morning

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** January 2025  
**Purpose:** Reliable way to get daily workflow questions every morning  
**Status:** ✅ Ready to Use

---

## 🚀 QUICK START

### Option 1: Run Command (Recommended - Most Reliable)

**Basic (just questions):**
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

**What it does:**
1. Gets current date
2. Finds yesterday's summary (if available)
3. Gets n8n workflow status (if `--with-n8n` flag used)
4. Shows all 10 daily workflow questions
5. You copy and paste into chat

---

### Option 2: Say "Top of the morning" in Chat

**In Cursor chat, type:**
```
Top of the morning
```

**AI will:**
1. Check date/time
2. Get yesterday's summary
3. Run n8n status report
4. Show all 10 questions
5. Wait for your answers

**Note:** If this doesn't work reliably, use Option 1 (command) instead.

---

## 📋 WHAT YOU GET

### Standard Output Includes:

1. **Current Date** - Today's date
2. **Yesterday's Summary** - From your daily workflow file (if found)
3. **10 Daily Workflow Questions:**
   - 1️⃣ Orchestrate — Don't Multitask
   - 2️⃣ Protect Deep Work Windows
   - 3️⃣ Batch Similar Contexts
   - 4️⃣ Delegate with Context
   - 5️⃣ Use If–Then Rules
   - 6️⃣ Track Your Metrics Daily
   - 7️⃣ Automate for Clarity, Not Complexity
   - 8️⃣ Move One Domino a Day
   - 9️⃣ Audit Systems Weekly
   - 🔟 Protect Energy Like a KPI

### With `--with-n8n` Flag, Also Includes:

4. **📊 BALLCODE N8N WORKFLOW STATUS**
   - Yesterday's executions
   - Today's actions needed
   - Quick status of all 3 workflows

---

## 💡 USAGE EXAMPLES

### Example 1: Just Questions

```bash
$ python scripts/daily-morning-questions.py --morning

🌅 DAILY WORKFLOW — 2025-01-15

Yesterday's summary (2025-01-14)
----------------------------------------------------------------------
[Found yesterday's workflow file: DAILY-WORKFLOW-2025-01-14.md]

10 daily workflow questions
----------------------------------------------------------------------

1️⃣ Orchestrate — Don't Multitask

What is the ONE system/process you're orchestrating today? (Not juggling multiple things)

Answer: _________________________________

[... all 10 questions ...]

💡 Copy these questions and answer them in your chat!
   Then tell me your ONE thing focus for today.
```

---

### Example 2: With n8n Status

```bash
$ python scripts/daily-morning-questions.py --with-n8n

🌅 DAILY WORKFLOW — 2025-01-15

Yesterday's summary (2025-01-14)
----------------------------------------------------------------------
[Found yesterday's workflow file: DAILY-WORKFLOW-2025-01-14.md]

📊 BALLCODE N8N WORKFLOW STATUS
----------------------------------------------------------------------
[Shows n8n workflow status from daily-n8n-report.sh]

10 daily workflow questions
----------------------------------------------------------------------

[... all 10 questions ...]
```

---

## 🔄 DAILY WORKFLOW

### Morning Routine:

1. **Run command:**
   ```bash
   python scripts/daily-morning-questions.py --with-n8n
   ```

2. **Copy output** and paste into Cursor chat

3. **Answer the questions** in chat

4. **Tell AI your ONE thing focus** for today

5. **AI saves your answers** to `DAILY-WORKFLOW-[DATE].md`

6. **Start working** on your ONE thing

---

## 🎯 WHY THIS WORKS BETTER

### Problem with "Top of the morning" phrase:
- AI might not recognize it
- Depends on AI interpretation
- Not always reliable

### Solution with `--morning` command:
- ✅ **Always works** - Script runs reliably
- ✅ **Consistent output** - Same format every time
- ✅ **Includes n8n status** - With `--with-n8n` flag
- ✅ **Can be automated** - Can add to morning routine
- ✅ **Works offline** - Doesn't need AI to recognize phrase

---

## 📝 INTEGRATION WITH CHAT

### Step 1: Run Command
```bash
python scripts/daily-morning-questions.py --with-n8n
```

### Step 2: Copy Output
Copy the entire output from terminal

### Step 3: Paste in Chat
Paste into Cursor chat

### Step 4: Answer Questions
Answer each question in the chat

### Step 5: AI Processes
AI will:
- Save your answers to daily workflow file
- Update tracking files
- Help you focus on your ONE thing

---

## 🔧 TROUBLESHOOTING

### Issue: Script not found

**Error:** `python: can't open file 'scripts/daily-morning-questions.py'`

**Solution:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python scripts/daily-morning-questions.py --morning
```

---

### Issue: Yesterday's summary not found

**Output:** `[No yesterday's workflow file found]`

**Solution:**
- This is normal if it's your first day
- You can provide summary manually
- AI will create today's file for tomorrow

---

### Issue: n8n status not showing

**Output:** `[n8n status check failed]`

**Solution:**
- Check if n8n is running
- Verify `scripts/daily-n8n-report.sh` exists
- Run manually: `./scripts/daily-n8n-report.sh`

---

## 🚀 ALIAS (Optional)

**Add to your `~/.zshrc` or `~/.bashrc`:**

```bash
alias morning='cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book && python scripts/daily-morning-questions.py --with-n8n'
```

**Then just run:**
```bash
morning
```

---

## 📚 RELATED DOCUMENTATION

- **Command Reference:** `BALLCODE-N8N-COMMAND-REFERENCE.md`
- **Daily Workflow System:** `.cursorrules` (Daily Workflow System section)
- **n8n Status:** `scripts/daily-n8n-report.sh`

---

**Version:** 1.0  
**Created:** January 2025  
**Status:** ✅ Ready to Use

