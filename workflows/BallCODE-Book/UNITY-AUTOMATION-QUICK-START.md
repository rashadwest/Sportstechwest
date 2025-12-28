# Unity AI Automation - Quick Start
## Get Running in 10 Minutes

**Copyright © 2025 Rashad West. All Rights Reserved.**

---

## ⚡ QUICK SETUP (10 Minutes)

### Step 1: Import Workflow to n8n (2 min)
1. Open n8n on Raspberry Pi: `http://your-pi-ip:5678`
2. Click "Workflows" → "Import from File"
3. Select: `n8n-unity-automation-workflow.json`
4. Click "Import"

### Step 2: Configure Credentials (3 min)
In n8n, add these credentials:

**OpenAI API:**
- Credentials → Add → OpenAI API
- API Key: Your OpenAI key

**GitHub Actions Token:**
- Credentials → Add → HTTP Header Auth
- Header: `Authorization`
- Value: `Bearer YOUR_GITHUB_TOKEN`

**Netlify API Token:**
- Credentials → Add → HTTP Header Auth  
- Header: `Authorization`
- Value: `Bearer YOUR_NETLIFY_TOKEN`

### Step 3: Set Environment Variables (2 min)
In n8n Settings → Environment Variables, add:
```bash
UNITY_REPO_URL=https://github.com/rashadwest/BallCode.git
UNITY_PROJECT_PATH=/home/pi/Projects/BTEBallCODE
BUILD_OUTPUT_PATH=/home/pi/Builds/WebGL
WORKFLOW_PATH=/home/pi/workflows/BallCODE-Book
GITHUB_REPO_OWNER=rashadwest
GITHUB_REPO_NAME=BallCode
GITHUB_WORKFLOW_FILE=unity-webgl-build.yml
NETLIFY_SITE_NAME=ballcode-game
NETLIFY_SITE_ID=your-site-id
```

### Step 4: Activate Workflow (1 min)
1. Open workflow in n8n
2. Click "Active" toggle (top right)
3. Done! ✅

### Step 5: Test It (2 min)
```bash
curl -X POST http://your-pi-ip:5678/webhook/unity-dev \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build"}'
```

---

## 🎯 HOW IT WORKS

### Three Trigger Options:

1. **Scheduled** - Runs every 6 hours automatically
2. **Webhook** - Manual trigger via API call
3. **GitHub Webhook** - Auto-triggers on code commits

### Complete Flow:
```
Trigger → AI Analysis → Clone Repo → Unity Edits → Build → Deploy → Notify
```

---

## 📋 WHAT YOU NEED

- [ ] n8n running on Raspberry Pi
- [ ] GitHub repository access
- [ ] Netlify account
- [ ] OpenAI API key
- [ ] GitHub Personal Access Token
- [ ] Netlify Auth Token

---

## 🔧 CONFIGURE SCHEDULE

**Edit "Scheduled Trigger" node in n8n:**

**Every hour:**
```json
{"field": "hours", "hoursInterval": 1}
```

**Every 12 hours:**
```json
{"field": "hours", "hoursInterval": 12}
```

**Daily at 2 AM:**
```json
{"cronExpression": "0 2 * * *"}
```

---

## 🧪 TEST COMMANDS

### Test Webhook:
```bash
curl -X POST http://your-pi-ip:5678/webhook/unity-dev \
  -H "Content-Type: application/json" \
  -d '{"request": "Build and deploy latest changes"}'
```

### Check Status:
- n8n Executions tab
- GitHub Actions: `https://github.com/rashadwest/BallCode/actions`
- Netlify Dashboard

---

## 📚 FULL DOCUMENTATION

See `UNITY-AUTOMATION-SETUP-GUIDE.md` for complete setup instructions.

---

**Copyright © 2025 Rashad West. All Rights Reserved.**






