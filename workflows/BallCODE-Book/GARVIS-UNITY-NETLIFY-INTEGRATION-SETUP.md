# 🔗 Garvis → Unity → Netlify Integration Setup

**Date:** December 17, 2025  
**Status:** Setup & Verification Guide  
**Goal:** Seamless integration between Garvis, Unity builds, and Netlify deployments

---

## ✅ ANSWER: Do We Need an API?

**No new API needed!** The existing n8n webhook system is sufficient:

- ✅ **Garvis Orchestrator** webhook: `/webhook/garvis`
- ✅ **Unity Build Orchestrator** webhook: `/webhook/unity-build`
- ✅ **GitHub Actions** already builds Unity
- ✅ **Netlify** already deploys from GitHub Actions

**The integration works via webhooks - no custom API required!**

---

## 🔄 HOW THE INTEGRATION WORKS

### Flow Diagram:
```
┌─────────────────────────────────────────────────────────────┐
│                    YOU / GARVIS                              │
│  (Python script or manual request)                          │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│         n8n: Garvis Orchestrator                             │
│         Webhook: POST /webhook/garvis                        │
│                                                              │
│  • Parses request                                            │
│  • Identifies systems (game/unity/build detected)            │
│  • Routes to Unity Build Orchestrator                        │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│         n8n: Unity Build Orchestrator                        │
│         Webhook: POST /webhook/unity-build                    │
│                                                              │
│  • Normalizes input                                          │
│  • Triggers GitHub Actions                                   │
│  • Monitors build status                                     │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│         GitHub Actions                                       │
│         Workflow: unity-webgl-build.yml                      │
│                                                              │
│  • Builds Unity WebGL                                        │
│  • Outputs to Builds/WebGL/                                  │
│  • Deploys to Netlify automatically                          │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│         Netlify                                              │
│         Site: ballcode-game.netlify.app                      │
│                                                              │
│  • Receives WebGL build                                      │
│  • Deploys to production                                     │
│  • Game is live!                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 SETUP CHECKLIST

### Step 1: Verify n8n Workflows Are Imported

**Required Workflows:**
1. ✅ **Garvis Orchestrator** (`n8n-garvis-orchestrator-workflow.json`)
2. ✅ **Unity Build Orchestrator** (`n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json`)

**How to Check:**
```bash
# Test Garvis Orchestrator webhook
curl -X POST http://192.168.1.226:5678/webhook/garvis \
  -H "Content-Type: application/json" \
  -d '{"one_thing": "Test Unity build", "tasks": ["Build Unity game"]}'

# Test Unity Build Orchestrator webhook
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build", "branch": "main"}'
```

**If workflows are not imported:**
1. Open n8n UI: http://192.168.1.226:5678
2. Click "Workflows" → "Import from File"
3. Import both workflow JSON files
4. Activate both workflows

---

### Step 2: Verify Environment Variables

**Required in n8n (Settings → Environment Variables):**

**For Unity Build Orchestrator:**
- `GITHUB_REPO_OWNER` = "rashadwest"
- `GITHUB_REPO_NAME` = "BTEBallCODE"
- `GITHUB_WORKFLOW_FILE` = "unity-webgl-build.yml"
- `NETLIFY_SITE_ID` = "[your-netlify-site-id]"
- `NETLIFY_SITE_NAME` = "ballcode-game"
- `N8N_INSTANCE_ROLE` = "dev" (on Mac) or "prod" (on Pi)

**For All Workflows:**
- `GITHUB_PAT` = "[github-personal-access-token]"
- `NETLIFY_AUTH_TOKEN` = "[netlify-access-token]"

**How to Check:**
```bash
# Run verification script
python scripts/robot-verify-credentials.py
```

---

### Step 3: Verify n8n Credentials

**Required Credentials in n8n UI:**

1. **GitHub Actions Token:**
   - Type: HTTP Header Auth
   - Name: `github-actions-token`
   - Header: `Authorization`
   - Value: `token YOUR_GITHUB_PAT`

2. **Netlify API Token:**
   - Type: HTTP Header Auth
   - Name: `netlify-api-token`
   - Header: `Authorization`
   - Value: `Bearer YOUR_NETLIFY_TOKEN`

**How to Check:**
- Open n8n UI → Credentials
- Verify both credentials exist and are configured

---

### Step 4: Test Integration Flow

**Option A: Via Garvis Command (Recommended)**
```bash
python scripts/garvis-command.py \
  --one-thing "Test Unity build integration" \
  --tasks "Build Unity game, Deploy to Netlify"
```

**Option B: Direct Webhook Test**
```bash
# Test Garvis Orchestrator
curl -X POST http://localhost:5678/webhook/garvis \
  -H "Content-Type: application/json" \
  -d '{
    "one_thing": "Test Unity build",
    "tasks": ["Build Unity game", "Deploy to Netlify"],
    "job_id": "test-001"
  }'
```

**Option C: Direct Unity Build Test**
```bash
# Test Unity Build Orchestrator directly
curl -X POST http://localhost:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{
    "request": "Test build from Garvis integration",
    "branch": "main",
    "jobId": "test-001"
  }'
```

---

## 🧪 VERIFICATION SCRIPT

Run this to verify everything is set up correctly:

```bash
python scripts/verify-garvis-unity-integration.py
```

**What it checks:**
- ✅ n8n is running
- ✅ Garvis Orchestrator webhook is accessible
- ✅ Unity Build Orchestrator webhook is accessible
- ✅ Environment variables are set
- ✅ Credentials are configured
- ✅ End-to-end flow works

---

## 🔧 HOW GARVIS TRIGGERS UNITY BUILDS

### Method 1: Via Garvis Command (Automatic Routing)

```bash
python scripts/garvis-command.py \
  --one-thing "Improve Unity landing page buttons" \
  --tasks "Update button UI, Build Unity game, Deploy to Netlify"
```

**What happens:**
1. Garvis Execution Engine detects "unity" or "build" in tasks
2. Maps to `unity-build` workflow
3. Calls `/webhook/unity-build` with request
4. Unity Build Orchestrator triggers GitHub Actions
5. GitHub Actions builds and deploys to Netlify

### Method 2: Direct Python Script Call

```python
import requests

n8n_url = "http://192.168.1.226:5678"

# Trigger Unity build
response = requests.post(
    f"{n8n_url}/webhook/unity-build",
    json={
        "request": "Build Unity game with UI improvements",
        "branch": "main",
        "jobId": "garvis-12345"
    }
)

print(response.json())
```

### Method 3: Via Garvis Orchestrator (Recommended for Multi-System)

```python
import requests

n8n_url = "http://192.168.1.226:5678"

# Trigger via Garvis Orchestrator (routes automatically)
response = requests.post(
    f"{n8n_url}/webhook/garvis",
    json={
        "one_thing": "Improve Unity UI",
        "tasks": ["Update buttons", "Build game", "Deploy"],
        "job_id": "garvis-12345"
    }
)

print(response.json())
```

---

## 📊 MONITORING & STATUS

### Check Build Status

**Via GitHub Actions:**
- Go to: https://github.com/rashadwest/BTEBallCODE/actions
- Check latest workflow run

**Via Netlify:**
- Go to: https://app.netlify.com
- Check latest deployment

**Via n8n:**
- Open n8n UI → Executions
- View workflow execution history

### Check Deployment URL

After successful deployment:
- Netlify URL: `https://ballcode-game.netlify.app` (or your site URL)
- GitHub Actions provides deployment URL in workflow output

---

## 🐛 TROUBLESHOOTING

### Issue: Webhook returns 404
**Solution:**
- Verify workflow is imported and activated in n8n (http://192.168.1.226:5678)
- Check webhook path matches: `/webhook/garvis` or `/webhook/unity-build`
- Verify n8n instance is accessible at http://192.168.1.226:5678

### Issue: Build doesn't trigger
**Solution:**
- Verify `GITHUB_PAT` is set and valid
- Check GitHub Actions workflow file exists: `.github/workflows/unity-webgl-build.yml`
- Verify credentials in n8n UI (http://192.168.1.226:5678)

### Issue: Netlify deployment fails
**Solution:**
- Verify `NETLIFY_AUTH_TOKEN` and `NETLIFY_SITE_ID` are set
- Check Netlify site exists and is accessible
- Verify GitHub Actions workflow has Netlify deployment step

### Issue: Garvis doesn't route to Unity
**Solution:**
- Check task keywords: must include "unity", "build", or "game"
- Verify Garvis Orchestrator workflow is active in n8n (http://192.168.1.226:5678)
- Check n8n execution logs for routing decisions

---

## ✅ SUCCESS CRITERIA

**Integration is working when:**
- ✅ Garvis command triggers Unity build
- ✅ Unity Build Orchestrator receives webhook
- ✅ GitHub Actions workflow runs
- ✅ Build completes successfully
- ✅ Netlify deployment succeeds
- ✅ Game is live on Netlify

---

## 🚀 NEXT STEPS

1. **Verify Setup:** Run verification script
2. **Test Integration:** Trigger a test build
3. **Monitor First Build:** Watch the full flow
4. **Document Issues:** Note any problems
5. **Iterate:** Fix issues and retest

---

## 📝 QUICK REFERENCE

**Webhook URLs:**
- Garvis: `http://localhost:5678/webhook/garvis`
- Unity Build: `http://localhost:5678/webhook/unity-build`

**Test Commands:**
```bash
# Test Garvis → Unity flow
python scripts/garvis-command.py --one-thing "Test" --tasks "Build Unity game"

# Test Unity Build directly
curl -X POST http://localhost:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test", "branch": "main"}'
```

**Status Checks:**
- GitHub Actions: https://github.com/rashadwest/BTEBallCODE/actions
- Netlify: https://app.netlify.com
- n8n Executions: http://localhost:5678/executions

---

**Integration is ready! Test it and move to UI/UX improvements next!** 🎮✨


