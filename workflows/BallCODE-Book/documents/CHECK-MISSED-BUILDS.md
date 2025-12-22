# Check for Missed Builds
## Verification System

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 12, 2025  
**Purpose:** Verify n8n workflow is running and no builds were missed

---

## 🔍 HOW TO CHECK FOR MISSED BUILDS

### Step 1: Check n8n Workflow Executions

1. **Open n8n UI**
2. **Go to your workflow:** "Unity AI Automation - HOURLY BUILD"
3. **Click "Executions" tab** (or view execution history)
4. **Check recent executions:**
   - Should see executions every hour (if scheduled trigger is active)
   - Check timestamps - are they running on schedule?
   - Check status - are they completing successfully?

**What to look for:**
- ✅ **Green checkmarks** = Successful executions
- ⚠️ **Yellow warnings** = Partial success or warnings
- ❌ **Red errors** = Failed executions
- ⏸️ **No executions** = Workflow might not be active

---

### Step 2: Check GitHub Actions Builds

1. **Go to your GitHub repository**
2. **Click "Actions" tab**
3. **Check recent workflow runs:**
   - Should see builds triggered by n8n
   - Check timestamps - do they match n8n executions?
   - Check status - are builds completing?

**What to look for:**
- ✅ **Green checkmarks** = Successful builds
- ⚠️ **Yellow warnings** = Build with warnings
- ❌ **Red X** = Failed builds
- ⏸️ **No recent builds** = n8n might not be triggering

---

### Step 3: Check Netlify Deployments

1. **Go to Netlify dashboard**
2. **Select your site**
3. **Check "Deploys" tab:**
   - Should see deployments after successful builds
   - Check timestamps - do they match GitHub Actions?
   - Check status - are deployments successful?

**What to look for:**
- ✅ **Published** = Successful deployment
   - ⚠️ **Building** = Currently deploying
   - ❌ **Failed** = Deployment error
   - ⏸️ **No recent deploys** = Builds might not be completing

---

## 📊 EXPECTED SCHEDULE

### If Scheduled Trigger is Set to Hourly:
- **Runs:** Every hour (e.g., 1:00, 2:00, 3:00, etc.)
- **n8n executions:** Should see 24 executions per day
- **GitHub Actions:** Should see builds triggered hourly
- **Netlify deploys:** Should see deployments after successful builds

### If Scheduled Trigger is Set to Every 6 Hours:
- **Runs:** 4 times per day (e.g., 12:00 AM, 6:00 AM, 12:00 PM, 6:00 PM)
- **n8n executions:** Should see 4 executions per day
- **GitHub Actions:** Should see 4 builds per day
- **Netlify deploys:** Should see 4 deployments per day

---

## 🐛 TROUBLESHOOTING

### Issue: No Recent Executions in n8n

**Possible Causes:**
1. **Workflow not activated** - Check if workflow is "Active" (toggle in n8n)
2. **Scheduled trigger not configured** - Check trigger settings
3. **n8n server stopped** - Check if n8n is running
4. **Timezone mismatch** - Check scheduled trigger timezone

**Fix:**
- Activate workflow in n8n
- Check scheduled trigger configuration
- Verify n8n server is running

---

### Issue: n8n Executes But No GitHub Actions Builds

**Possible Causes:**
1. **GitHub Actions not triggered** - Check "Trigger GitHub Actions Build!" node
2. **GitHub token invalid** - Check credentials
3. **Workflow file missing** - Check if GitHub Actions workflow exists
4. **Conditional logic skipping** - Check "Needs Build?" node

**Fix:**
- Check "Trigger GitHub Actions Build!" node execution
- Verify GitHub token credentials
- Check GitHub Actions workflow file exists
- Review conditional logic

---

### Issue: GitHub Actions Builds But No Netlify Deploy

**Possible Causes:**
1. **Netlify deploy not triggered** - Check "Deploy to Netlify!" node
2. **Netlify token invalid** - Check credentials
3. **Conditional logic skipping** - Check "Needs Deploy?" node
4. **Build output path wrong** - Check environment variables

**Fix:**
- Check "Deploy to Netlify!" node execution
- Verify Netlify token credentials
- Review conditional logic
- Check BUILD_OUTPUT_PATH environment variable

---

## ✅ QUICK CHECKLIST

### Daily Check (5 minutes):
- [ ] Open n8n → Check recent executions (should see hourly)
- [ ] Open GitHub → Check Actions (should see recent builds)
- [ ] Open Netlify → Check Deploys (should see recent deployments)

### Weekly Check (10 minutes):
- [ ] Review execution logs for errors
- [ ] Check build success rate
- [ ] Verify deployment success rate
- [ ] Review any failed executions

---

## 📋 AUTOMATED CHECK (Future)

**We can set up:**
- Automated daily report of missed builds
- Email/Slack notification if build fails
- Dashboard showing build status

**For now:** Manual check using steps above

---

**Version:** Build Verification Guide  
**Created:** December 12, 2025  
**Status:** Ready to Use


