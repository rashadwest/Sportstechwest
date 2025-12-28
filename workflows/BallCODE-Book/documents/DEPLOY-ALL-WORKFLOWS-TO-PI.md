# 🤖 Deploy All Workflows to Pi n8n - Automated Script

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Purpose:** Automated deployment of all BallCODE workflows to Raspberry Pi n8n instance

---

## 🚀 QUICK DEPLOY

### Run the Automated Deployment Script

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./deploy-all-workflows-to-pi.sh
```

**That's it!** The script will:
1. ✅ Check Pi n8n connection
2. ✅ Validate all workflow JSON files
3. ✅ Deploy all 5 workflows to Pi
4. ✅ Attempt to activate workflows
5. ✅ Provide deployment summary

---

## 📋 WHAT GETS DEPLOYED

The script deploys these workflows to Pi n8n:

### Phase 1 Workflows:
1. **Full Integration Workflow** - AI-driven development automation
2. **Screenshot to Fix Workflow** - Visual debugging and auto-repair

### Phase 2 Workflows:
3. **Book Content Update Workflow** - Automate book content updates
4. **Curriculum Sync Workflow** - Sync curriculum changes
5. **Game Exercise Integration Workflow** - Integrate game exercises

**Note:** Unity Build Orchestrator is already on Pi, so it's not included.

---

## 🔧 CONFIGURATION

### Pi n8n Settings

The script uses:
- **Pi URL:** `http://192.168.1.226:5678`
- **API Key:** Optional (from `.n8n-env.pi` if available)

### Customize Pi URL

Edit the script or set environment variable:
```bash
export PI_N8N_URL="http://your-pi-ip:5678"
./deploy-all-workflows-to-pi.sh
```

---

## ✅ AFTER DEPLOYMENT

### 1. Verify in n8n UI

Open Pi n8n: `http://192.168.1.226:5678`

Check:
- All workflows are imported
- Workflows are visible in "Workflows" list

### 2. Activate Workflows

For each workflow:
1. Open workflow in n8n UI
2. Toggle "Inactive" → "Active" (top-right)
3. Switch should turn green/blue

### 3. Test Workflows

```bash
# Set Pi URL
export PI_N8N_URL="http://192.168.1.226:5678"

# Test Book Content Update
curl -X POST "${PI_N8N_URL}/webhook/book-content-update" \
  -H "Content-Type: application/json" \
  -d '{"bookId": 1, "content": {"title": "Test"}, "updateType": "modify"}'

# Test Curriculum Sync
curl -X POST "${PI_N8N_URL}/webhook/curriculum-sync" \
  -H "Content-Type: application/json" \
  -d '{"changeType": "modify"}'

# Test Game Exercise Integration
curl -X POST "${PI_N8N_URL}/webhook/game-exercise-integration" \
  -H "Content-Type: application/json" \
  -d '{"exerciseType": "new", "exerciseData": {"exerciseId": "test", "bookId": 1}}'
```

---

## 🆘 TROUBLESHOOTING

### Script Fails: "Cannot connect to Pi n8n"

**Fix:**
1. Check Pi is on network: `ping 192.168.1.226`
2. Check n8n is running on Pi
3. Verify Pi IP address is correct
4. Check firewall settings

### Workflows Deploy but Not Active

**Fix:**
1. Open n8n UI: `http://192.168.1.226:5678`
2. Manually activate each workflow
3. Or use API to activate (if API key is set)

### API Key Required

**Get API Key:**
1. Open Pi n8n UI: `http://192.168.1.226:5678`
2. Settings → API
3. Generate API Key
4. Add to `.n8n-env.pi`:
   ```bash
   export N8N_API_KEY="your-api-key"
   ```

---

## 📊 DEPLOYMENT STATUS

After running the script, you'll see:

```
✅ Successful: 5
❌ Failed: 0

🎉 All workflows deployed successfully!
```

---

## 🔄 RE-DEPLOY

To update workflows:

```bash
# Re-run deployment script
./deploy-all-workflows-to-pi.sh
```

**Note:** This will create new workflow instances. To update existing workflows, you need workflow IDs.

---

## 📝 MANUAL DEPLOYMENT (Alternative)

If automated script doesn't work, deploy manually:

1. Open Pi n8n UI: `http://192.168.1.226:5678`
2. Workflows → Import from File
3. Import each workflow file:
   - `n8n-ballcode-full-integration-workflow.json`
   - `n8n-screenshot-to-fix-workflow.json`
   - `n8n-book-content-update-workflow.json`
   - `n8n-curriculum-sync-workflow.json`
   - `n8n-game-exercise-integration-workflow.json`
4. Activate each workflow

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Ready to Use



