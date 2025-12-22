# n8n Netlify Deployment Automation
## One Webhook Call = Push to GitHub + Deploy to Netlify

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 20, 2025  
**Status:** ✅ Ready to Use

---

## 🎯 THE SOLUTION

**Problem:** GitHub not showing pushes, want effortless Netlify deployment  
**Solution:** n8n workflow that handles everything automatically

---

## ✅ WHAT WAS FIXED

### 1. **Git Remote Fixed**
- **Before:** `JuddCMelvin/BallCode.git`
- **After:** `rashadwest/BTEBallCODE.git` ✅
- **Result:** Pushes now go to correct repo

### 2. **n8n Workflow Created**
- **File:** `n8n-netlify-deploy-workflow.json`
- **Webhook:** `POST /webhook/deploy-netlify`
- **Flow:** Webhook → Parse → Git Push → Netlify Trigger → Done

---

## 🚀 HOW IT WORKS

### **Simple Webhook Call:**
```bash
curl -X POST http://192.168.1.226:5678/webhook/deploy-netlify \
  -H "Content-Type: application/json" \
  -d '{"commitMessage": "Book 2 curriculum integration"}'
```

**What Happens:**
1. ✅ n8n receives webhook
2. ✅ Parses commit message
3. ✅ Pushes to GitHub (`rashadwest/BTEBallCODE`)
4. ✅ Triggers Netlify build hook
5. ✅ Returns success response

**Result:** GitHub updated + Netlify deploying automatically

---

## ⚙️ SETUP (One-Time, 5 Minutes)

### **Step 1: Import Workflow to n8n**

1. Go to: `http://192.168.1.226:5678` (Pi n8n)
2. Click: **"Workflows"** → **"Import from File"**
3. Select: `n8n-netlify-deploy-workflow.json`
4. Click: **"Import"**

### **Step 2: Set Netlify Build Hook**

1. Go to: https://app.netlify.com
2. Select site: **ballcode.co**
3. Go to: **Site Settings** → **Build & deploy** → **Build hooks**
4. Create build hook (if not exists)
5. Copy URL

### **Step 3: Add to n8n Environment**

**On Pi n8n:**
```bash
# SSH to Pi or use n8n UI
# Add environment variable:
NETLIFY_BUILD_HOOK="https://api.netlify.com/build_hooks/YOUR_HOOK_ID"
```

**Or set in n8n workflow:**
- Edit "Trigger Netlify Build" node
- Update URL field with your build hook

### **Step 4: Activate Workflow**

1. In n8n UI, click **"Active"** toggle
2. Workflow is now live!

---

## 📋 USAGE

### **Option 1: Webhook Call (Recommended)**
```bash
curl -X POST http://192.168.1.226:5678/webhook/deploy-netlify \
  -H "Content-Type: application/json" \
  -d '{"commitMessage": "Book 2 curriculum integration"}'
```

### **Option 2: Simple Script**
```bash
# Create: scripts/deploy-via-n8n.sh
curl -X POST http://192.168.1.226:5678/webhook/deploy-netlify \
  -H "Content-Type: application/json" \
  -d "{\"commitMessage\": \"$1\"}"
```

**Usage:**
```bash
./scripts/deploy-via-n8n.sh "Book 2 curriculum integration"
```

### **Option 3: From AI/Code**
```javascript
// Call from any code
fetch('http://192.168.1.226:5678/webhook/deploy-netlify', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ commitMessage: 'Deploy update' })
});
```

---

## ✅ WHAT GETS DEPLOYED

**The workflow:**
1. Stages all changes in `BallCode/` directory
2. Commits with your message
3. Pushes to `rashadwest/BTEBallCODE` (main branch)
4. Triggers Netlify build hook
5. Netlify deploys automatically

**Result:**
- ✅ GitHub shows new commit
- ✅ Netlify starts building
- ✅ Site updates in 1-3 minutes

---

## 🔧 TROUBLESHOOTING

### **Git Push Fails:**
- Check git credentials in n8n
- Verify repo permissions
- Check network connection

### **Netlify Not Triggering:**
- Verify `NETLIFY_BUILD_HOOK` is set
- Check build hook URL is correct
- Verify build hook still exists in Netlify

### **No Changes Detected:**
- This is normal if nothing changed
- Workflow will still trigger Netlify (if configured)

---

## 🎯 RECOMMENDED WORKFLOW

### **After Making Changes:**
```bash
# 1. Make your changes (edit files)

# 2. Deploy via n8n (one command)
curl -X POST http://192.168.1.226:5678/webhook/deploy-netlify \
  -H "Content-Type: application/json" \
  -d '{"commitMessage": "Book 2 curriculum integration"}'

# 3. Wait 1-3 minutes

# 4. Check: https://ballcode.co
```

**That's it!** No manual git commands needed.

---

## 📊 ADVANTAGES

### **vs Manual Git Push:**
- ✅ One command instead of multiple
- ✅ Automatic Netlify trigger
- ✅ Can be called from anywhere
- ✅ Integrated with n8n automation

### **vs Script:**
- ✅ Runs on Pi (24/7 available)
- ✅ Can be triggered from webhooks
- ✅ Integrated with other workflows
- ✅ Centralized automation

---

## 🔗 INTEGRATION

### **Can Be Called From:**
- ✅ Direct webhook call
- ✅ Other n8n workflows
- ✅ Scripts/automation
- ✅ AI assistants
- ✅ Any HTTP client

### **Can Trigger:**
- ✅ After curriculum updates
- ✅ After book content changes
- ✅ After website updates
- ✅ Scheduled deployments
- ✅ Manual deployments

---

## ✅ STATUS

**Workflow Created:** ✅ `n8n-netlify-deploy-workflow.json`  
**Git Remote Fixed:** ✅ `rashadwest/BTEBallCODE`  
**Setup Required:** ⏳ Import to n8n + Set build hook (5 minutes)  
**Ready to Use:** ✅ Yes (after setup)

---

**Next:** Import workflow to n8n and set up Netlify build hook!

