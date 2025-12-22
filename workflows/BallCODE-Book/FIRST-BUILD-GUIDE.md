# 🚀 First Build Guide - Trigger Your Workflow

**Date:** December 11, 2025  
**Status:** Ready to trigger first build!

---

## 🎯 QUICK START - 3 Ways to Trigger

### Option 1: Use Script (Easiest) ⭐

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./trigger-first-build.sh "First build - Initial deployment"
```

**Or with custom message:**
```bash
./trigger-first-build.sh "Your custom build message here"
```

---

### Option 2: Manual Webhook (Terminal)

```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-dev \
  -H "Content-Type: application/json" \
  -d '{"request": "First build - Initial deployment"}'
```

---

### Option 3: n8n UI (Visual) ⭐ RECOMMENDED FOR FIRST TIME

1. **Open n8n:** http://192.168.1.226:5678
2. **Open your workflow** (Unity AI Automation)
3. **Click "Execute Workflow" button** (top right, orange button)
4. **Watch it run** in real-time
5. **Check results** after completion

**Why this is best for first time:**
- ✅ See each step execute
- ✅ Catch any errors immediately
- ✅ Understand what's happening
- ✅ Verify everything works

---

## 📊 WHAT HAPPENS WHEN YOU TRIGGER

Your workflow will execute these steps:

1. **Normalize Input** - Processes trigger data
2. **AI Analyze Request** - Analyzes what needs to be done
3. **Parse AI Response** - Extracts action plan
4. **Needs Unity Edits?** - Checks if Unity changes needed
5. **Get Git Variables** - Gets branch, repo info
6. **Git Pull Latest** - Pulls latest code
7. **Git Commit & Push** - Commits and pushes changes
8. **Needs Build?** - Checks if build needed
9. **Trigger GitHub Actions** - Starts build process
10. **Wait for Build** - Waits 5 minutes for build
11. **Needs Deploy?** - Checks if deployment needed
12. **Deploy to Netlify** - Deploys to Netlify
13. **Send Notification** - Sends completion notification
14. **Completion Report** - Creates final report

---

## ✅ BEFORE YOU TRIGGER - Quick Checklist

- [ ] n8n is running (check: http://192.168.1.226:5678)
- [ ] Workflow is active in n8n (toggle should be ON)
- [ ] Credentials are set up (GitHub, OpenAI, Netlify)
- [ ] Environment variables are set (UNITY_REPO_URL, etc.)
- [ ] Unity repo is accessible
- [ ] GitHub Actions workflow is configured

---

## 🔍 MONITOR THE BUILD

### In n8n UI:
1. Go to **Executions** tab
2. Click on your execution
3. Watch each node execute
4. Check for any errors

### In Terminal:
```bash
# Check n8n executions
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./check-n8n-executions.sh
```

### In GitHub:
1. Go to: https://github.com/rashadwest/BallCode/actions
2. Check for triggered workflow runs
3. Monitor build progress

---

## 🐛 TROUBLESHOOTING

### "Connection refused" or "Can't connect"
- Check if n8n is running: `curl http://192.168.1.226:5678/healthz`
- Verify n8n URL is correct
- Check if workflow is active

### "Workflow not found"
- Make sure workflow is imported in n8n
- Check workflow name matches
- Verify webhook path is correct: `unity-dev`

### "Credentials error"
- Check credentials in n8n UI
- Verify GitHub token is valid
- Verify OpenAI API key is set
- Verify Netlify token is set

### "Git operations failed"
- Check Unity repo path is correct
- Verify Git credentials are set
- Check if repo is accessible

---

## 📝 EXPECTED RESULTS

### Success Indicators:
- ✅ All nodes show green checkmarks in n8n
- ✅ GitHub Actions workflow runs
- ✅ Build completes successfully
- ✅ Netlify deployment succeeds
- ✅ Notification sent

### What You'll See:
1. **n8n execution** shows all nodes completed
2. **GitHub commit** with automated message
3. **GitHub Actions** build running
4. **Netlify** deployment active
5. **Notification** received (if configured)

---

## 🎯 NEXT STEPS AFTER FIRST BUILD

1. **Verify build works:**
   - Check Netlify site is live
   - Test the deployed application
   - Verify all features work

2. **Check scheduled trigger:**
   - Verify it's set to run every 6 hours
   - Fix warnings if needed (2 min fix)

3. **Set up monitoring:**
   - Check execution history regularly
   - Set up notifications if needed
   - Monitor GitHub Actions

4. **Optimize if needed:**
   - Adjust build times
   - Fine-tune AI prompts
   - Optimize workflow logic

---

## 🚀 READY TO GO!

**Choose your method:**
- ⭐ **First time:** Use n8n UI (Option 3) - See everything
- ⚡ **Quick trigger:** Use script (Option 1) - Fastest
- 🔧 **Custom:** Use curl (Option 2) - Most control

**Good luck with your first build!** 🎉

---

**Script:** `./trigger-first-build.sh`  
**n8n URL:** http://192.168.1.226:5678  
**Webhook Path:** `unity-dev`


