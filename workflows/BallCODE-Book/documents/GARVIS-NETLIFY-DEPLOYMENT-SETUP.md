# Garvis Netlify Deployment Setup - Complete Integration
## Seamless Website & Game Deployment via Garvis

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 22, 2025  
**Status:** 🚀 **SETTING UP GARVIS FOR SEAMLESS DEPLOYMENT**

---

## 🎯 GOAL

**Make Garvis handle ALL Netlify deployments seamlessly:**
- ✅ Website deployments (rashadwest/BallCode)
- ✅ Game deployments (rashadwest/BTEBallCODE)
- ✅ Automatic triggering on code changes
- ✅ Status reporting and notifications
- ✅ Error handling and retry logic

---

## 🔧 GARVIS DEPLOYMENT SYSTEM

### **System Architecture:**

```
Garvis Command → Garvis Orchestrator → 
  ├─ Website Deployment (Netlify API)
  └─ Game Deployment (Unity Build → Netlify)
```

### **Components:**

1. **Garvis Execution Engine** - Handles deployment requests
2. **Garvis Orchestrator (n8n)** - Routes to appropriate deployment
3. **Netlify API Integration** - Direct website deployment
4. **Unity Build Orchestrator** - Game builds and deployment

---

## 🚀 SETUP STEPS

### **Step 1: Configure Netlify API in Garvis**

**Add to Garvis environment or n8n credentials:**

```bash
# Netlify API Credentials
NETLIFY_AUTH_TOKEN=your_netlify_token_here
NETLIFY_SITE_ID_WEBSITE=your_website_site_id
NETLIFY_SITE_ID_GAME=your_game_site_id
```

**Get Netlify Token:**
1. Go to: https://app.netlify.com/user/applications
2. Click: "New access token"
3. Name: "Garvis Automation"
4. Copy token

**Get Site IDs:**
1. Website site → Settings → General → Site ID
2. Game site → Settings → General → Site ID

---

### **Step 2: Update Garvis Orchestrator Workflow**

**Add Netlify Deployment Nodes:**

1. **Website Deployment Node:**
   - Type: HTTP Request
   - Method: POST
   - URL: `https://api.netlify.com/api/v1/sites/{{$env.NETLIFY_SITE_ID_WEBSITE}}/deploys`
   - Headers: `Authorization: Bearer {{$env.NETLIFY_AUTH_TOKEN}}`
   - Body: `{"branch": "main"}`

2. **Game Deployment Node:**
   - Calls: Unity Build Orchestrator (already exists)
   - Unity Build → GitHub Actions → Netlify (automatic)

---

### **Step 3: Create Garvis Deployment Command**

**Usage:**

```bash
# Deploy website
python scripts/garvis-command.py \
  --one-thing "Deploy website to Netlify" \
  --tasks "Push to GitHub, Trigger Netlify deploy, Verify deployment"

# Deploy game
python scripts/garvis-command.py \
  --one-thing "Deploy game to Netlify" \
  --tasks "Push levels to GitHub, Trigger Unity build, Deploy to Netlify"

# Deploy both
python scripts/garvis-command.py \
  --one-thing "Deploy website and game" \
  --tasks "Deploy website, Deploy game, Verify both"
```

---

## 📋 GARVIS DEPLOYMENT WORKFLOWS

### **Workflow 1: Website Deployment**

**Trigger:** Garvis command or webhook

**Steps:**
1. Garvis receives deployment request
2. Checks if changes exist in GitHub
3. If changes exist → Push to GitHub (if needed)
4. Trigger Netlify deployment via API
5. Monitor deployment status
6. Report completion

**n8n Workflow:**
- Webhook: `/webhook/garvis-deploy-website`
- HTTP Request: Netlify API
- Status Check: Poll until complete
- Response: Deployment status

---

### **Workflow 2: Game Deployment**

**Trigger:** Garvis command or webhook

**Steps:**
1. Garvis receives deployment request
2. Routes to Unity Build Orchestrator
3. Unity Build Orchestrator triggers GitHub Actions
4. GitHub Actions builds Unity WebGL
5. Auto-deploys to Netlify
6. Report completion

**n8n Workflow:**
- Webhook: `/webhook/garvis-deploy-game`
- Calls: Unity Build Orchestrator (`/webhook/unity-build`)
- Status Check: Monitor GitHub Actions
- Response: Build and deployment status

---

### **Workflow 3: Full System Deployment**

**Trigger:** Garvis command

**Steps:**
1. Deploy website
2. Deploy game
3. Verify both
4. Report combined status

---

## 🔄 AUTOMATIC DEPLOYMENT

### **Option A: GitHub Webhook → Garvis**

**Setup:**
1. GitHub repository → Settings → Webhooks
2. Add webhook: `http://192.168.1.226:5678/webhook/github`
3. Events: Push to main branch
4. Garvis receives webhook → Auto-deploys

### **Option B: File Watcher → Garvis**

**Setup:**
1. Garvis file watcher monitors BallCode directory
2. Detects changes
3. Auto-triggers deployment
4. Reports status

---

## 📊 STATUS MONITORING

**Garvis tracks:**
- Deployment status
- Build logs
- Error messages
- Deployment time
- Success/failure

**Reports:**
- Real-time status
- Completion notifications
- Error alerts
- Deployment history

---

## 🎯 QUICK START

**Deploy website now via Garvis:**

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python scripts/garvis-command.py \
  --one-thing "Deploy website to Netlify" \
  --tasks "Connect to Netlify API, Trigger deployment, Verify status"
```

**Or use webhook:**

```bash
curl -X POST http://192.168.1.226:5678/webhook/garvis \
  -H "Content-Type: application/json" \
  -d '{
    "one_thing": "Deploy website to Netlify",
    "tasks": ["Connect to Netlify API", "Trigger deployment", "Verify status"],
    "system": "website"
  }'
```

---

## ✅ VERIFICATION

**After setup, verify:**

1. **Garvis can trigger deployments:**
   ```bash
   python scripts/garvis-command.py --test-deploy
   ```

2. **Check n8n workflows:**
   - Garvis Orchestrator active
   - Netlify API nodes configured
   - Webhooks responding

3. **Test deployment:**
   - Trigger via Garvis
   - Check Netlify dashboard
   - Verify site updates

---

**Version:** 1.0  
**Created:** December 22, 2025  
**Status:** Setup in Progress


