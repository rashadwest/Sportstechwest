# 🚀 Get Unity Build Orchestrator Working - Step-by-Step

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Priority:** 🔴 CRITICAL - #1 Most Important Workflow  
**Time:** 10-15 minutes  
**Status:** Ready to Activate

---

## ✅ STEP 1: Verify Workflow is Imported (2 minutes)

**Check in n8n:**
1. Open: `http://192.168.1.226:5678`
2. Look for workflow: **"AIMCODE (Demis) - Unity Build Orchestrator (13 nodes, MAC GUARDED)"**
3. If not found: Import `n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json`

---

## ✅ STEP 2: Activate Workflow (30 seconds)

**In n8n UI:**
1. Open the Unity Build Orchestrator workflow
2. Click the **"Active" toggle** (top-right corner)
3. Toggle should turn **green/blue** (ON)
4. Workflow is now active!

**Note:** The workflow shows `"active": false` in the JSON - this needs to be toggled ON in the UI.

---

## ✅ STEP 3: Set Environment Variables (3 minutes)

**Required Environment Variables:**
- `GITHUB_REPO_OWNER` - Your GitHub username (e.g., "rashadwest")
- `GITHUB_REPO_NAME` - Your repository name (e.g., "BTEBallCODE")
- `GITHUB_WORKFLOW_FILE` - Workflow filename (e.g., "unity-webgl-build.yml")
- `NETLIFY_SITE_ID` - Your Netlify site ID
- `NETLIFY_SITE_NAME` - Your Netlify site name (e.g., "ballcode-game")
- `N8N_INSTANCE_ROLE` - Set to "prod" on Pi (or "dev" on Mac)

**How to Set:**
1. In n8n UI, go to **Settings** → **Environment Variables**
2. Add each variable above
3. Or set in your n8n startup script/environment

**Quick Check:**
```bash
# SSH to Pi (if needed)
ssh pi@192.168.1.226

# Check if variables are set (if n8n is running)
# Or check n8n UI → Settings → Environment Variables
```

---

## ✅ STEP 4: Configure Credentials (3 minutes)

**Required Credentials:**

### **1. GitHub Actions Token**
- **Name:** `github-actions-token`
- **Type:** HTTP Header Auth
- **Header Name:** `Authorization`
- **Header Value:** `Bearer YOUR_GITHUB_TOKEN`
- **How to get:** GitHub → Settings → Developer settings → Personal access tokens → Generate token with `repo` scope

### **2. Netlify API Token**
- **Name:** `netlify-api-token`
- **Type:** HTTP Header Auth
- **Header Name:** `Authorization`
- **Header Value:** `Bearer YOUR_NETLIFY_TOKEN`
- **How to get:** Netlify → User settings → Applications → New access token

**In n8n:**
1. Go to **Credentials** (left sidebar)
2. Create/verify both credentials above
3. Make sure they're named exactly as shown

---

## ✅ STEP 5: Test the Workflow (2 minutes)

**Quick Test:**
```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{
    "request": "Test build from terminal",
    "branch": "main"
  }'
```

**Expected Response:**
```json
{
  "status": "ok",
  "request": "Test build from terminal",
  "triggerType": "webhook",
  "branch": "main",
  "github": {
    "status": "queued",
    "conclusion": "unknown"
  },
  "netlify": {
    "state": "building"
  },
  "message": "Build dispatched..."
}
```

---

## ✅ STEP 6: Verify End-to-End (5 minutes)

**Check Each Step:**

1. **n8n Execution:**
   - Go to n8n → Executions
   - Find your test execution
   - Should show "Success"

2. **GitHub Actions:**
   - Go to: `https://github.com/YOUR_USERNAME/YOUR_REPO/actions`
   - Should see new workflow run triggered
   - Should show "Unity WebGL Build" workflow

3. **Netlify Deployment:**
   - Go to: `https://app.netlify.com/sites/YOUR_SITE/deploys`
   - Should see new deployment
   - Should show "Building" or "Published"

---

## 🐛 TROUBLESHOOTING

### **Issue: 404 Error (Workflow Not Found)**
**Fix:**
- Workflow not activated → Toggle "Active" ON
- Workflow not imported → Import the JSON file

### **Issue: Missing Environment Variables**
**Error:** "Missing required env var(s): GITHUB_REPO_OWNER"
**Fix:**
- Set all required environment variables in n8n Settings

### **Issue: Authentication Failed**
**Error:** "401 Unauthorized" or "403 Forbidden"
**Fix:**
- Check GitHub token has `repo` scope
- Check Netlify token is valid
- Verify credentials are named correctly

### **Issue: Build Doesn't Trigger**
**Fix:**
- Check GitHub Actions workflow file exists
- Verify workflow file name matches `GITHUB_WORKFLOW_FILE`
- Check GitHub Actions is enabled for the repo

---

## ✅ VERIFICATION CHECKLIST

Before considering it "working":

- [ ] Workflow is imported in n8n
- [ ] Workflow is **Active** (toggle ON)
- [ ] All environment variables set
- [ ] GitHub credential configured
- [ ] Netlify credential configured
- [ ] Test webhook returns 200 OK
- [ ] GitHub Actions build triggers
- [ ] Netlify deployment starts
- [ ] End-to-end flow completes

---

## 🎯 QUICK START COMMANDS

**Test Immediately:**
```bash
# Test webhook
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Quick test", "branch": "main"}' | python3 -m json.tool

# Or use test script
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/test-all-webhooks.sh
# Choose option 1 (Pi)
```

---

## 📋 WHAT THIS WORKFLOW DOES

**Complete Flow:**
1. Receives webhook request (or scheduled trigger)
2. Normalizes input (request, branch, etc.)
3. Checks environment variables
4. Acquires lock (prevents overlapping builds)
5. Dispatches GitHub Actions build
6. Waits 3 minutes
7. Checks GitHub build status
8. Checks Netlify deployment status
9. Releases lock
10. Returns status report

**Time:** ~5-10 minutes end-to-end

---

**Status:** ✅ Ready to Activate  
**Next:** Follow steps 1-6 above

