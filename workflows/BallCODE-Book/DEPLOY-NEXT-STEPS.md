# Deploy Next Steps: Set n8n Environment Variables

**Date:** December 10, 2025  
**Status:** ✅ Script Created  
**Action Required:** Run script to set environment variables

---

## 🎯 WHAT NEEDS TO BE DONE

Set these environment variables in n8n:
1. **UNITY_REPO_URL** - Your GitHub repository URL
2. **UNITY_PROJECT_PATH** - Local path where project should be cloned

---

## ✅ AUTOMATED SCRIPT CREATED

**File:** `set-n8n-env-vars.py`

### Option 1: Run with Values (Recommended)

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python3 set-n8n-env-vars.py "https://github.com/YOUR_USERNAME/YOUR_REPO.git" "/path/to/project"
```

**Replace:**
- `YOUR_USERNAME/YOUR_REPO` with your actual GitHub repo
- `/path/to/project` with your local project path

### Option 2: Run Interactively

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python3 set-n8n-env-vars.py
```

Then enter values when prompted.

---

## 🔧 IF n8n IS ON REMOTE SERVER (Raspberry Pi)

### Step 1: SSH into Remote Server

```bash
ssh user@raspberry-pi-ip
```

### Step 2: Copy Script to Remote Server

```bash
# From your local machine
scp set-n8n-env-vars.py user@raspberry-pi-ip:~/
```

### Step 3: Run Script on Remote Server

```bash
# On remote server
python3 set-n8n-env-vars.py "https://github.com/YOUR_USERNAME/YOUR_REPO.git" "/path/to/project"
```

---

## 📋 MANUAL METHOD (Alternative)

If script doesn't work, set via n8n UI:

1. **Open n8n** in browser
2. **Go to:** Settings → Environment Variables
3. **Click:** Add Variable
4. **Add:**
   - **Key:** `UNITY_REPO_URL`
   - **Value:** Your GitHub repo URL (e.g., `https://github.com/user/repo.git`)
5. **Add:**
   - **Key:** `UNITY_PROJECT_PATH`
   - **Value:** Local path (e.g., `/Users/rashadwest/project`)
6. **Save**

---

## 🔄 RESTART n8n (Required)

After setting variables, restart n8n:

### If n8n is Local:

```bash
# Find n8n process
ps aux | grep n8n | grep -v grep

# Kill and restart (adjust based on how you run n8n)
# If using npm:
pkill -f n8n
n8n start

# If using systemd:
sudo systemctl restart n8n
```

### If n8n is on Remote Server:

```bash
# SSH into server
ssh user@raspberry-pi-ip

# Restart n8n service
sudo systemctl restart n8n
# OR
pkill -f n8n && n8n start
```

---

## ✅ VERIFY VARIABLES ARE SET

### Method 1: Check in n8n UI

1. **Go to:** Settings → Environment Variables
2. **Verify** both variables are listed

### Method 2: Test Workflow

1. **Run workflow** again
2. **Check "Get Git Variables" node output**
3. **Should see:**
   - `repoUrlSet: true`
   - `projectPathSet: true`
   - `error: null`

---

## 🎯 EXPECTED RESULTS

After setting variables and restarting n8n:

✅ **"Get Git Variables" node:**
- `repoUrlSet: true`
- `projectPathSet: true`
- No error messages

✅ **"Should Clone Repository?" node:**
- Takes `true` path (if repo doesn't exist)
- Runs clone/pull operations

✅ **"Commit & Push Changes" node:**
- Actually performs git operations (if conditions met)
- No longer shows "skipped" when variables are set

---

## 📝 NOTES

- **Database Location:** `~/.n8n/database.sqlite`
- **Restart Required:** n8n must be restarted for changes to take effect
- **Remote Server:** If n8n is on Raspberry Pi, set variables there, not locally

---

**Status:** ✅ Script ready  
**Next Step:** Run `python3 set-n8n-env-vars.py` with your values  
**Result:** Workflow will perform actual git operations



