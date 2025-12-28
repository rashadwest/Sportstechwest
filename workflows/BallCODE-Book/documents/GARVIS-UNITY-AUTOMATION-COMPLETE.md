# Garvis Unity Build & Deploy Automation

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 26, 2025  
**Status:** ✅ **AUTOMATION READY** - Garvis can execute this

---

## 🎯 GARVIS AUTOMATION CAPABILITY

**Yes! @Garvis can automate the entire Unity build and deployment process.**

**Script Created:** `scripts/garvis-unity-build-deploy.py`

---

## 🚀 HOW GARVIS EXECUTES THIS

### **Command for Garvis:**

```bash
python3 /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/scripts/garvis-unity-build-deploy.py
```

**Or from project root:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python3 scripts/garvis-unity-build-deploy.py
```

---

## 📋 WHAT GARVIS AUTOMATES

### **Step 1: Prerequisites Check** ✅
- Verifies Unity installation
- Checks project exists
- Validates BuildScript exists

### **Step 2: Unity Build** ✅
- Executes Unity WebGL build
- Uses BuildScript.BuildWebGL method
- Monitors build progress (15-20 min)
- Handles timeouts and errors

### **Step 3: Build Verification** ✅
- Checks build output exists
- Verifies index.html present
- Calculates build size

### **Step 4: Netlify Deployment** ✅
- Checks for Netlify CLI
- Deploys automatically if CLI available
- Falls back to manual instructions if not

---

## 🔧 INTEGRATION WITH N8N

**Garvis can trigger this via n8n:**

### **Option 1: Direct Python Execution**
```json
{
  "type": "n8n-nodes-base.executeCommand",
  "parameters": {
    "command": "python3 /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/scripts/garvis-unity-build-deploy.py"
  }
}
```

### **Option 2: Shell Script Wrapper**
```json
{
  "type": "n8n-nodes-base.executeCommand",
  "parameters": {
    "command": "cd /Users/rashadwest/BTEBallCODE && ./scripts/emergency-local-build.sh"
  }
}
```

---

## 📊 GARVIS WORKFLOW

**Complete Automation Flow:**

```
Garvis Trigger
    ↓
Check Prerequisites
    ├─ Unity ✅
    ├─ Project ✅
    └─ BuildScript ✅
    ↓
Build Unity WebGL (15-20 min)
    ├─ Execute BuildScript
    ├─ Monitor Progress
    └─ Verify Output
    ↓
Deploy to Netlify
    ├─ Check Netlify CLI
    ├─ Deploy if available
    └─ Manual instructions if not
    ↓
Report Status
    ├─ Success ✅
    └─ Errors ❌
```

---

## 🎯 GARVIS COMMANDS

### **Full Build & Deploy:**
```bash
python3 scripts/garvis-unity-build-deploy.py
```

### **Build Only (Shell Script):**
```bash
cd /Users/rashadwest/BTEBallCODE
./scripts/emergency-local-build.sh
```

---

## 📝 OUTPUT & LOGGING

**Garvis Script Provides:**
- ✅ Timestamped logs
- ✅ Progress updates
- ✅ Error messages
- ✅ Build size reporting
- ✅ Deployment status

**Log Format:**
```
[2025-12-26 12:00:00] [INFO] Checking prerequisites...
[2025-12-26 12:00:01] [INFO] ✅ Unity found: 2021.3.10f1
[2025-12-26 12:00:02] [INFO] 🔨 Building Unity WebGL...
[2025-12-26 12:15:30] [INFO] ✅ Build verified: /Users/rashadwest/BTEBallCODE/Builds/WebGL
[2025-12-26 12:15:31] [INFO] 📦 Build size: 61.0 MB
[2025-12-26 12:15:32] [INFO] 🚀 Deploying to Netlify...
[2025-12-26 12:16:00] [INFO] ✅ Deployment successful!
```

---

## 🔄 SCHEDULING WITH GARVIS

**Garvis can schedule this:**
- Daily builds
- On-demand builds
- After code changes
- Scheduled maintenance builds

**Example n8n Schedule:**
- Trigger: Daily at 2 AM
- Action: Execute Garvis Unity build script
- Notification: Report status

---

## ✅ SUCCESS CRITERIA

**Build Successful:**
- Exit code: 0
- Build output exists
- index.html present
- Build size > 0

**Deployment Successful:**
- Netlify CLI: Returns success
- Manual: User confirms

---

## 🚨 ERROR HANDLING

**Garvis Script Handles:**
- ✅ Missing Unity installation
- ✅ Missing project files
- ✅ Build failures
- ✅ Timeout errors
- ✅ Netlify CLI missing
- ✅ Deployment failures

**All errors are logged with clear messages.**

---

## 📋 MANUAL FALLBACK

**If Netlify CLI not available:**
- Script provides manual deployment instructions
- Build is still successful
- User can deploy manually via Netlify dashboard

---

## 🎯 GARVIS INTEGRATION POINTS

**1. n8n Workflow Node:**
- Execute Command node
- Run Python script
- Monitor output

**2. Garvis Orchestrator:**
- Schedule builds
- Trigger on events
- Report status

**3. Notification System:**
- Success notifications
- Error alerts
- Build status updates

---

## ✅ STATUS

**Automation Ready:**
- ✅ Python script created
- ✅ Error handling implemented
- ✅ Logging system in place
- ✅ Netlify deployment support
- ✅ Manual fallback provided

**Garvis can now:**
- ✅ Execute builds automatically
- ✅ Monitor build progress
- ✅ Deploy to Netlify
- ✅ Report status
- ✅ Handle errors gracefully

---

**Status:** ✅ **FULLY AUTOMATED** - Garvis can execute this end-to-end!

**Next:** Integrate with n8n workflow for scheduled/triggered builds

