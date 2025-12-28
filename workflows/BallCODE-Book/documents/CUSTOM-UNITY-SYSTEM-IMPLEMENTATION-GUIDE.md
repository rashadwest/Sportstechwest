# Custom Unity CI/CD System - Implementation Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 26, 2025  
**Status:** Ready to Implement  
**Cost:** FREE Forever

---

## 🎯 QUICK START

### **Option 1: Use Existing Script (Simplest)**
```bash
# Already exists in your codebase!
./scripts/build-unity-locally-deploy.sh
```

**This script:**
- ✅ Builds Unity WebGL locally
- ✅ Deploys to Netlify
- ✅ Uses your local Unity license (no issues!)
- ✅ FREE

---

### **Option 2: Enhanced Orchestrator (Recommended)**

**New script:** `scripts/custom-unity-build-orchestrator.py`

**Features:**
- ✅ Full build pipeline coordination
- ✅ Build verification
- ✅ Deployment automation
- ✅ n8n webhook notifications
- ✅ Build status tracking
- ✅ Error handling and retry logic

**Usage:**
```bash
# Install dependencies (one-time)
pip3 install requests

# Run build
python3 scripts/custom-unity-build-orchestrator.py
```

---

## 📋 SETUP INSTRUCTIONS

### **Step 1: Install Dependencies**

```bash
# Install Python requests library (for n8n notifications)
pip3 install requests

# Verify Netlify CLI is installed
which netlify || npm install -g netlify-cli
```

### **Step 2: Configure Environment Variables**

**For n8n notifications (optional):**
```bash
export N8N_WEBHOOK_URL="http://192.168.1.226:5678/webhook/build-status"
```

**For Netlify deployment:**
```bash
export NETLIFY_SITE_ID="your-site-id"
export NETLIFY_AUTH_TOKEN="your-auth-token"
```

**Or create `.env` file:**
```bash
cat > .env << EOF
N8N_WEBHOOK_URL=http://192.168.1.226:5678/webhook/build-status
NETLIFY_SITE_ID=your-site-id
NETLIFY_AUTH_TOKEN=your-auth-token
EOF
```

### **Step 3: Test Build**

```bash
# Test the orchestrator
python3 scripts/custom-unity-build-orchestrator.py
```

**Expected output:**
```
============================================================
Custom Unity CI/CD Build Orchestrator
============================================================
[2025-12-26 10:00:00] [INFO] Checking prerequisites...
[2025-12-26 10:00:00] [INFO] ✅ Unity Editor found: ...
[2025-12-26 10:00:00] [INFO] ✅ Unity project found: ...
[2025-12-26 10:00:01] [INFO] Starting Unity WebGL build...
[2025-12-26 10:05:00] [INFO] ✅ Unity build successful!
[2025-12-26 10:05:01] [INFO] Verifying build output...
[2025-12-26 10:05:01] [INFO] ✅ Build verified! Size: 45.2 MB
[2025-12-26 10:05:02] [INFO] Deploying to Netlify...
[2025-12-26 10:05:30] [INFO] ✅ Deployment successful! URL: https://ballcode.netlify.app
[2025-12-26 10:05:31] [INFO] Sending notification to n8n...
[2025-12-26 10:05:31] [INFO] ✅ Notification sent successfully
============================================================
Build Pipeline Summary
============================================================
Build ID: build-1735224000
Status: success
Duration: 0:05:31
============================================================
```

---

## 🔄 AUTOMATION SETUP

### **Option A: n8n Webhook Trigger (Recommended)**

**Create n8n workflow:**
1. **Webhook Trigger:** Receives GitHub webhook
2. **Execute Command:** Runs `python3 scripts/custom-unity-build-orchestrator.py`
3. **Status Notification:** Sends results to Slack/Email

**Workflow file:** `n8n-unity-custom-build-workflow.json` (to be created)

---

### **Option B: GitHub Actions Self-Hosted Runner**

**Install runner on Mac:**
```bash
# Download runner
mkdir actions-runner && cd actions-runner
curl -o actions-runner-osx-x64-2.311.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-osx-x64-2.311.0.tar.gz
tar xzf ./actions-runner-osx-x64-2.311.0.tar.gz

# Configure
./config.sh --url https://github.com/rashadwest/BTEBallCODE --token YOUR_TOKEN

# Install service
./svc.sh install
./svc.sh start
```

**Update workflow:**
```yaml
jobs:
  build:
    runs-on: self-hosted  # Uses your Mac!
    steps:
      - uses: actions/checkout@v4
      - name: Build Unity
        run: python3 scripts/custom-unity-build-orchestrator.py
```

---

### **Option C: Cron Job (Simple)**

**Schedule builds:**
```bash
# Edit crontab
crontab -e

# Add line (builds daily at 2 AM)
0 2 * * * cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book && python3 scripts/custom-unity-build-orchestrator.py >> /tmp/unity-build.log 2>&1
```

---

## 📊 COMPARISON: Options

| Feature | Simple Script | Orchestrator | Self-Hosted Runner |
|---------|--------------|--------------|-------------------|
| **Setup Time** | 0 min (exists) | 5 min | 15 min |
| **Features** | Basic | Full | Full + GitHub Integration |
| **Automation** | Manual | n8n/Cron | GitHub Actions |
| **Notifications** | None | n8n webhook | GitHub status |
| **Cost** | FREE | FREE | FREE |

---

## ✅ ADVANTAGES OF CUSTOM SYSTEM

1. **FREE Forever:** No monthly costs
2. **No License Issues:** Uses local Unity license
3. **Fast Builds:** Local is faster than cloud
4. **Full Control:** Customize everything
5. **Privacy:** All builds local
6. **Reliable:** No cloud dependencies

---

## 🚀 NEXT STEPS

1. **Test the orchestrator:**
   ```bash
   python3 scripts/custom-unity-build-orchestrator.py
   ```

2. **Set up automation:**
   - Choose: n8n webhook, self-hosted runner, or cron
   - Configure triggers
   - Test end-to-end

3. **Monitor builds:**
   - Check build logs
   - Review status files
   - Monitor n8n notifications

---

## 📋 TROUBLESHOOTING

### **Build Fails:**
- Check Unity Editor path
- Verify project path
- Check Unity license is active
- Review build logs

### **Deployment Fails:**
- Verify Netlify credentials
- Check Netlify CLI is installed
- Review deployment logs

### **Notifications Don't Work:**
- Check n8n webhook URL
- Verify network connectivity
- Check n8n workflow is active

---

## 🎯 SUMMARY

**You now have:**
- ✅ Custom Unity CI/CD system
- ✅ FREE forever
- ✅ No license issues
- ✅ Full automation capability
- ✅ Ready to use!

**Choose your approach:**
- **Quick:** Use existing `build-unity-locally-deploy.sh`
- **Enhanced:** Use new `custom-unity-build-orchestrator.py`
- **Full Automation:** Add n8n webhook or self-hosted runner

**All options are FREE and work with your local Unity license!**


