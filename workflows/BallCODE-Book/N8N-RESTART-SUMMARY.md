# n8n Restart Summary

**Date:** December 10, 2025  
**Status:** Environment variables set, restart needed

---

## 🔍 CURRENT SITUATION

**n8n Location:** Running remotely on `192.168.1.226:5678` (Raspberry Pi)

**Environment Variables:** ✅ Set in local database (`~/.n8n/database.sqlite`)

**Important Note:** If n8n is running on a remote device, it may have its own database. The environment variables need to be set on the remote device's database.

---

## ✅ WHAT WAS DONE

1. ✅ Fixed workflow code (no longer throws error)
2. ✅ Set environment variables in local n8n database
3. ✅ Created restart script (`restart-n8n.sh`)

---

## 🔄 TO RESTART n8n

### If n8n is on Remote Device (192.168.1.226)

**Option 1: SSH and Restart**
```bash
# SSH to the device
ssh pi@192.168.1.226

# Find n8n process
ps aux | grep n8n | grep -v grep

# Restart n8n (depends on how it's running)
# If systemd service:
sudo systemctl restart n8n

# If running manually:
pkill -f n8n
n8n start
```

**Option 2: Set Variables on Remote Device**
The environment variables need to be set in the remote device's database:
- Remote database: `~/.n8n/database.sqlite` (on the Raspberry Pi)
- Use the same Python script on the remote device

### If n8n is Running Locally

Use the restart script:
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./restart-n8n.sh
```

---

## 📋 ENVIRONMENT VARIABLES SET

**Local Database:**
- UNITY_REPO_URL = `https://github.com/rashadwest/BallCode.git`
- UNITY_PROJECT_PATH = `/Users/rashadwest/BTEBallCODE`
- WORKFLOW_PATH = `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book`
- UNITY_EXECUTABLE = `/opt/unity/Editor/Unity`

**Note:** If n8n is remote, these paths may need to be adjusted for the remote device (e.g., `/home/pi/...` instead of `/Users/rashadwest/...`)

---

## 🧪 TESTING THE WORKFLOW

1. **Import the workflow:**
   - The workflow file is on your Desktop: `n8n-unity-automation-workflow-FINAL-WORKING.json`
   - Import it into n8n UI

2. **Verify environment variables:**
   - Go to n8n UI → Settings → Environment Variables
   - Check that `UNITY_REPO_URL` and `UNITY_PROJECT_PATH` are set

3. **Test the workflow:**
   - Trigger the workflow
   - It should no longer error about missing environment variables

---

## ⚠️ IMPORTANT NOTES

1. **Remote vs Local:**
   - If n8n is running remotely, the environment variables need to be set on the remote device
   - The local database update won't affect the remote n8n instance

2. **Path Differences:**
   - Local paths: `/Users/rashadwest/...`
   - Remote paths (Raspberry Pi): `/home/pi/...`
   - Make sure paths match the device where n8n is running

3. **Workflow File:**
   - The fixed workflow is: `n8n-unity-automation-workflow-FINAL-WORKING.json`
   - It's been updated to handle missing environment variables gracefully

---

## ✅ NEXT STEPS

1. ✅ Workflow file is ready (on Desktop)
2. ⏳ Restart n8n (on remote device if needed)
3. ⏳ Import workflow into n8n
4. ⏳ Test the workflow
5. ⏳ Verify environment variables are loaded

---

**Status:** Ready to test! 🚀


