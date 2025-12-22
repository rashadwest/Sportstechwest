# Quick Commands - BallCODE-Book

**Date:** December 18, 2025  
**Purpose:** Quick reference for common commands

---

## 🚀 NAVIGATE TO BALLCODE-BOOK

**From anywhere:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
```

**Or use the helper script (from BallCODE-Book directory):**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./run-robot.sh env-vars
```

---

## 🤖 RUN ROBOT SCRIPTS

### **Option 1: Navigate First (Recommended)**
```bash
# Step 1: Go to BallCODE-Book
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book

# Step 2: Run script
python scripts/robot-hardcode-env-vars.py
```

### **Option 2: Use Full Path**
```bash
python /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/scripts/robot-hardcode-env-vars.py
```

### **Option 3: Use Helper Script**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./run-robot.sh env-vars
```

---

## 📋 COMMON COMMANDS

### **Set Environment Variables:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python scripts/robot-hardcode-env-vars.py
```

### **Verify Setup:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python scripts/verify-garvis-unity-integration.py
```

### **Test Integration:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python scripts/garvis-command.py \
  --one-thing "Test Unity build integration" \
  --tasks "Build Unity game"
```

---

## 🎯 QUICK ALIAS (Add to ~/.zshrc)

**Add this to your `~/.zshrc` file:**
```bash
alias ballcode='cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book'
```

**Then reload:**
```bash
source ~/.zshrc
```

**Now you can just type:**
```bash
ballcode
python scripts/robot-hardcode-env-vars.py
```

---

## ✅ VERIFY YOU'RE IN THE RIGHT PLACE

**Check:**
```bash
pwd
```

**Should show:**
```
/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
```

**List files:**
```bash
ls scripts/robot-*.py
```

**Should see:**
- `robot-hardcode-env-vars.py`
- `robot-set-n8n-env-vars.py`
- etc.

---

**Always navigate to BallCODE-Book first, then run scripts!** ✅

