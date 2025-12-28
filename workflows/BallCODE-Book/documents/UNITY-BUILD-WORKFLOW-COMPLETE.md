# 🎮 Unity Build Workflow - Complete

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 23, 2025  
**Status:** ✅ Complete Workflow Created

---

## ✅ WHAT WAS CREATED

### **New Workflow Script: `garvis-unity-build-workflow.py`**

A comprehensive Python workflow that orchestrates the entire Unity build process:

1. **Trigger Build** - Triggers Unity build via n8n webhook
2. **Monitor Build** - Monitors GitHub Actions build status
3. **Verify Deployment** - Verifies Netlify deployment
4. **Report Status** - Reports to central status system

---

## 🎯 FEATURES

### **1. Trigger Build**
- Triggers Unity build via n8n webhook (`/webhook/unity-build`)
- Handles build skipping (if build is locked)
- Reports trigger status centrally

### **2. Monitor Build**
- Finds build for commit SHA or run ID
- Monitors build status in real-time
- Checks every 30 seconds (configurable)
- Maximum wait time: 30 minutes (configurable)
- Reports completion status

### **3. Verify Deployment**
- Checks Netlify site accessibility
- Verifies HTTP response codes
- Reports deployment status

### **4. Full Workflow**
- Combines all steps: Trigger → Monitor → Verify
- Handles errors gracefully
- Reports status at each step

---

## 📋 USAGE

### **Trigger Build:**
```bash
python scripts/garvis-unity-build-workflow.py --trigger
```

### **Monitor Build:**
```bash
# Monitor latest build
python scripts/garvis-unity-build-workflow.py --monitor

# Monitor specific commit
python scripts/garvis-unity-build-workflow.py --monitor --commit abc1234

# Monitor specific run ID
python scripts/garvis-unity-build-workflow.py --monitor --run-id 123456789
```

### **Verify Deployment:**
```bash
python scripts/garvis-unity-build-workflow.py --verify
```

### **Full Workflow:**
```bash
# Complete workflow (trigger + monitor + verify)
python scripts/garvis-unity-build-workflow.py --full

# With custom request message
python scripts/garvis-unity-build-workflow.py --full --request "Build with Book 1-3 levels"
```

---

## 🔄 WORKFLOW INTEGRATION

### **Integration with Garvis Deploy:**
```python
# In garvis-deploy.py, after pushing game levels:
from scripts.garvis_unity_build_workflow import full_workflow

if game_result.get("status") == "success":
    build_result = full_workflow(
        request="Garvis: Build after level push",
        branch="main"
    )
```

### **Integration with n8n:**
- Uses existing n8n webhook: `/webhook/unity-build`
- Compatible with Unity Build Orchestrator workflow
- No changes needed to n8n workflows

### **Integration with GitHub Actions:**
- Monitors existing GitHub Actions workflow
- Works with `.github/workflows/unity-webgl-build.yml`
- No changes needed to GitHub Actions

---

## 📊 STATUS REPORTING

### **Central Status File:**
All workflow steps report to `garvis_status.json`:

```json
{
  "last_updated": "2025-12-23T10:30:00",
  "components": {
    "unity_build_trigger": {
      "status": "triggered",
      "message": "Unity build triggered successfully",
      "timestamp": "2025-12-23T10:30:00"
    },
    "unity_build_monitor": {
      "status": "completed",
      "conclusion": "success",
      "run_id": "123456789",
      "wait_time": 450
    },
    "unity_deployment": {
      "status": "success",
      "site_url": "https://ballcode.netlify.app",
      "http_code": 200
    }
  },
  "overall": "success"
}
```

---

## 🎯 WORKFLOW STEPS

### **Step 1: Trigger Build**
1. Sends POST request to n8n webhook
2. Handles connection errors gracefully
3. Reports trigger status
4. Returns build trigger result

### **Step 2: Monitor Build**
1. Gets latest commit SHA (if not provided)
2. Finds GitHub Actions run for commit
3. Monitors build status (queued → in_progress → completed)
4. Checks every 30 seconds
5. Reports completion status

### **Step 3: Verify Deployment**
1. Checks Netlify site accessibility
2. Verifies HTTP response codes
3. Reports deployment status

---

## ⚙️ CONFIGURATION

### **Environment Variables:**
- `N8N_BASE_URL` - n8n base URL (default: `http://192.168.1.226:5678`)
- `GITHUB_TOKEN` - GitHub token (for build tracking)

### **Configurable Constants:**
- `MAX_WAIT_TIME` - Maximum wait time for build (default: 1800s / 30 min)
- `CHECK_INTERVAL` - Check interval for build status (default: 30s)
- `GAME_REPO` - Unity repository (default: `rashadwest/BTEBallCODE`)

---

## 🔧 ERROR HANDLING

### **Trigger Errors:**
- Connection errors → Reports error, suggests checking n8n
- Timeout errors → Reports timeout
- Build skipped → Reports skip reason

### **Monitor Errors:**
- Commit not found → Reports error
- Build not found → Reports pending status
- Timeout → Reports timeout after max wait time

### **Verify Errors:**
- Site not accessible → Reports error
- HTTP errors → Reports warning with status code

---

## 📈 BENEFITS

1. **Automated** - Complete workflow automation
2. **Monitored** - Real-time build monitoring
3. **Verified** - Automatic deployment verification
4. **Reported** - Central status reporting
5. **Integrated** - Works with existing systems

---

## 🎯 USAGE EXAMPLES

### **Example 1: Quick Build**
```bash
# Trigger build and monitor
python scripts/garvis-unity-build-workflow.py --trigger
python scripts/garvis-unity-build-workflow.py --monitor
```

### **Example 2: Full Automation**
```bash
# Complete workflow
python scripts/garvis-unity-build-workflow.py --full
```

### **Example 3: Monitor Specific Build**
```bash
# After pushing code, monitor that specific commit
python scripts/garvis-unity-build-workflow.py --monitor --commit $(git rev-parse HEAD)
```

---

## 🔄 INTEGRATION WITH GARVIS DEPLOY

The workflow can be integrated into `garvis-deploy.py`:

```python
# After deploying game levels:
if game_result.get("status") == "success":
    from garvis_unity_build_workflow import full_workflow
    
    build_result = full_workflow(
        request="Garvis: Build after level deployment",
        branch="main"
    )
```

---

## ✅ STATUS

**Workflow Created:** ✅  
**Integration:** ✅ Ready  
**Testing:** ⏳ Ready for testing  
**Documentation:** ✅ Complete

---

**Report Generated:** December 23, 2025  
**Status:** ✅ Complete - Ready to Use!


