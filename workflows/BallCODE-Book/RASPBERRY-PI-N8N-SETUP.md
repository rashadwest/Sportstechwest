# 🔧 Raspberry Pi n8n .env Setup

**Important:** You have TWO n8n instances:
- ❌ **Local (Mac):** http://localhost:5678 - Wrong one!
- ✅ **Remote (Pi):** http://192.168.1.226:5678 - **This is the one you want!**

---

## 🎯 QUICK SETUP (Automated)

### Run the Setup Script:

```bash
cd ~/Desktop
./set-env-on-raspberry-pi.sh
```

**This will:**
1. SSH into Raspberry Pi
2. Find n8n directory on Pi
3. Create/update `.env` file
4. Add environment variables
5. Restart n8n on Pi

---

## 📋 MANUAL SETUP (If You Prefer)

### Step 1: SSH into Raspberry Pi

```bash
ssh pi@192.168.1.226
```

### Step 2: Find n8n Directory

**On the Pi, find where n8n is installed:**

```bash
# Check common locations
ls -la ~/.n8n
ls -la ~/n8n

# Or find where n8n process is running
ps aux | grep n8n
```

### Step 3: Create .env File

**In the n8n directory on Pi, create `.env` file:**

```bash
cd ~/.n8n  # or wherever n8n is on Pi
nano .env  # or use your preferred editor
```

### Step 4: Add Environment Variables

**Paste this into the `.env` file:**

```bash
# Unity Automation Environment Variables
UNITY_REPO_URL=https://github.com/rashadwest/BallCode.git
UNITY_PROJECT_PATH=/Users/rashadwest/BTEBallCODE
WORKFLOW_PATH=/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
```

**Save the file** (Ctrl+X, then Y, then Enter in nano)

### Step 5: Restart n8n on Pi

**If n8n is running as a service:**
```bash
sudo systemctl restart n8n
```

**If using PM2:**
```bash
pm2 restart n8n
```

**If running manually:**
```bash
# Find and kill n8n process
pkill -f n8n
# Then restart however you normally start it
```

### Step 6: Verify

**Test from your Mac:**
```bash
curl http://192.168.1.226:5678/healthz
```

Should return: `OK` or `{"status":"ok"}`

---

## 🔍 ONE-LINE COMMAND (Quick Method)

**Copy and paste this entire command:**

```bash
ssh pi@192.168.1.226 "cat > ~/.n8n/.env << 'EOF'
UNITY_REPO_URL=https://github.com/rashadwest/BallCode.git
UNITY_PROJECT_PATH=/Users/rashadwest/BTEBallCODE
WORKFLOW_PATH=/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
EOF
sudo systemctl restart n8n"
```

**This will:**
1. SSH into Pi
2. Create `.env` file
3. Add variables
4. Restart n8n

---

## ✅ VERIFY IT WORKED

**After restarting n8n on Pi:**

1. **Open n8n on Pi:**
   - Go to: http://192.168.1.226:5678
   - (NOT localhost:5678!)

2. **Test in workflow:**
   - Execute "Get Git Variables" node
   - Should show: `repoUrlSet: true, projectPathSet: true`

3. **Test variable access:**
   - Add Code node
   - Type: `{{ $env.UNITY_REPO_URL }}`
   - Should show: `https://github.com/rashadwest/BallCode.git`

---

## 🐛 TROUBLESHOOTING

### Can't SSH into Pi?

**Check:**
1. Pi is on and accessible: `ping 192.168.1.226`
2. SSH is enabled on Pi
3. You have SSH keys set up (or know the password)

### Variables Not Working?

**On the Pi, check:**
1. `.env` file exists: `cat ~/.n8n/.env`
2. File has correct values
3. n8n was restarted after creating `.env`
4. n8n is reading from the right directory

### Wrong n8n Instance?

**Make sure you're using:**
- ✅ http://192.168.1.226:5678 (Raspberry Pi)
- ❌ NOT http://localhost:5678 (your Mac)

---

## 📋 SUMMARY

**What to do:**
1. ✅ Set `.env` file on **Raspberry Pi** (not your Mac)
2. ✅ Restart n8n on **Raspberry Pi**
3. ✅ Use n8n at **http://192.168.1.226:5678** (not localhost)

**Quick command:**
```bash
./set-env-on-raspberry-pi.sh
```

---

**Status:** Ready to set up on Raspberry Pi  
**Action:** Run script or use one-line command  
**Time:** 2 minutes


