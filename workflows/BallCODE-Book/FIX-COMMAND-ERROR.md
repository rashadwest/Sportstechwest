# Fix: "can't open file" Error

**Date:** December 18, 2025  
**Problem:** Running script from wrong directory

---

## ❌ THE ERROR

```bash
python scripts/robot-set-n8n-env-vars.py
python: can't open file '/Users/rashadwest/scripts/robot-set-n8n-env-vars.py': [Errno 2] No such file or directory
```

**Why it happened:**
- You ran the command from your home directory (`~`)
- The script is in the BallCODE-Book directory
- Python looked for `~/scripts/robot-set-n8n-env-vars.py` (doesn't exist)

---

## ✅ THE SOLUTION

### **Option 1: Navigate First (Easiest)**

```bash
# Step 1: Go to BallCODE-Book directory
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book

# Step 2: Run the script
python scripts/robot-hardcode-env-vars.py
```

**Note:** Use `robot-hardcode-env-vars.py` (not `robot-set-n8n-env-vars.py`) since SSH access isn't available.

---

### **Option 2: Use Full Path**

```bash
python /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/scripts/robot-hardcode-env-vars.py
```

---

### **Option 3: Use Helper Script**

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./run-robot.sh env-vars
```

---

## 🎯 QUICK REFERENCE

**Always navigate to BallCODE-Book first:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
```

**Then run scripts:**
```bash
python scripts/robot-hardcode-env-vars.py
python scripts/verify-garvis-unity-integration.py
python scripts/garvis-command.py --one-thing "Test" --tasks "Build Unity game"
```

---

## 📝 ADD ALIAS (Recommended)

**Add to `~/.zshrc`:**
```bash
echo 'alias ballcode="cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book"' >> ~/.zshrc
source ~/.zshrc
```

**Then use:**
```bash
ballcode
python scripts/robot-hardcode-env-vars.py
```

---

**The key is: Always `cd` to BallCODE-Book first!** ✅

