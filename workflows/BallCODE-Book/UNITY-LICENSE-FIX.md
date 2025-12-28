# Fix: "command not found: -serial"

**Problem:** The command is being split incorrectly by zsh.

---

## ✅ SOLUTION: Use the Script (Easiest!)

**I created a script for you. Here's how to use it:**

### Step 1: Edit the Script
```bash
nano /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/activate-unity-license.sh
```

**Or open it in your editor:**
```bash
open -a "TextEdit" /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/activate-unity-license.sh
```

### Step 2: Replace These Lines
Find these lines in the script:
```bash
UNITY_EMAIL="YOUR-EMAIL@example.com"  # ← REPLACE THIS
UNITY_PASSWORD="YOUR-PASSWORD"         # ← REPLACE THIS
```

**Replace with your actual email and password:**
```bash
UNITY_EMAIL="your-actual-email@example.com"
UNITY_PASSWORD="your-actual-password"
```

### Step 3: Save and Run
```bash
/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/activate-unity-license.sh
```

---

## ✅ ALTERNATIVE: One-Line Command (If Script Doesn't Work)

**Copy this ENTIRE line (all on one line, no breaks):**

```bash
/Applications/Unity/Hub/Editor/2021.3.10f1/Unity.app/Contents/MacOS/Unity -quit -batchmode -serial -username 'YOUR-EMAIL' -password 'YOUR-PASSWORD'
```

**Replace:**
- `YOUR-EMAIL` → Your Unity account email (keep the quotes)
- `YOUR-PASSWORD` → Your Unity account password (keep the quotes)

**Example:**
```bash
/Applications/Unity/Hub/Editor/2021.3.10f1/Unity.app/Contents/MacOS/Unity -quit -batchmode -serial -username 'rashad@example.com' -password 'mypassword123'
```

---

## ⚠️ COMMON MISTAKES

**Wrong (missing quotes):**
```bash
-username rashad@example.com
```

**Right (with quotes):**
```bash
-username 'rashad@example.com'
```

**Wrong (line break):**
```bash
/Applications/Unity/... -serial
-username 'email'
```

**Right (all one line):**
```bash
/Applications/Unity/... -serial -username 'email' -password 'pass'
```

---

## 🎯 RECOMMENDED: Use the Script!

The script is safer and easier. Just edit it and run it!


