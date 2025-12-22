# Unity Automation Robot - Complete Setup
## Fully Automated "Robot" System for Unity Development

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 2025  
**Status:** Complete Setup Guide  
**Purpose:** Fully automated Unity workflow running continuously on Raspberry Pi n8n

---

## Overview

This is a **fully automated "robot"** system that handles the complete Unity development workflow:
- ✅ Clones GitHub repository
- ✅ Makes Unity edits (via AI)
- ✅ Builds to WebGL
- ✅ Deploys to Netlify
- ✅ Runs continuously 24/7

**Only reverts to manual if there's an absolute blocker.**

---

## Quick Start Guide

### Prerequisites Checklist

- [ ] GitHub repository: `rashadwest/BTEBallCODE`
- [ ] Netlify account (new or existing)
- [ ] n8n running on Raspberry Pi
- [ ] OpenAI API key
- [ ] GitHub Personal Access Token
- [ ] Unity project accessible

---

## Phase-by-Phase Setup

### Phase 1: Netlify Site Setup (One-Time Manual)

**Time:** 15-20 minutes  
**Guide:** See `PHASE-1-NETLIFY-SETUP-GUIDE.md`

**What you'll do:**
1. Clone Unity repository
2. Build Unity to WebGL (manual first time)
3. Deploy to Netlify manually
4. Get Netlify credentials (Site ID, Auth Token)
5. Add credentials to GitHub Secrets

**Result:** Netlify site created, credentials in GitHub Secrets

---

### Phase 2: GitHub Actions Workflow

**Time:** 10 minutes  
**Guide:** See `PHASE-2-GITHUB-ACTIONS-SETUP.md`

**What you'll do:**
1. Verify/create `.github/workflows/unity-webgl-build.yml`
2. Verify secrets are configured
3. Test workflow manually

**Result:** GitHub Actions ready to build and deploy automatically

---

### Phase 3: n8n Workflow Build

**Time:** 1-2 hours (building incrementally)  
**Guide:** See `PHASE-3-N8N-WORKFLOW-BUILD.md`

**What you'll build:**
1. Schedule Trigger (matches your crypto workflow)
2. Edit Fields (data setup)
3. Basic LLM Chain + OpenAI Chat Model (AI analysis)
4. Filter (conditional logic)
5. Execute Command (git operations)
6. HTTP Request (trigger GitHub Actions)
7. HTTP Request (deploy to Netlify)
8. Notifications (completion)

**Result:** Complete n8n workflow matching your proven pattern

---

## Configuration Reference

### GitHub Secrets Required

In `rashadwest/BTEBallCODE` repository:
- `NETLIFY_AUTH_TOKEN` - From Phase 1
- `NETLIFY_SITE_ID` - From Phase 1
- `NETLIFY_SITE_NAME` - Optional, from Phase 1

### n8n Credentials Required

- **OpenAI API** - For Basic LLM Chain
- **GitHub Personal Access Token** - For triggering Actions
- **Netlify Auth Token** - For deployment (optional if using CLI)

### n8n Environment Variables

```bash
UNITY_REPO_URL=https://github.com/rashadwest/BTEBallCODE.git
UNITY_PROJECT_PATH=/home/pi/Projects/BTEBallCODE
BUILD_OUTPUT_PATH=/home/pi/Builds/WebGL
WORKFLOW_PATH=/home/pi/workflows/BallCODE-Book
GITHUB_REPO_OWNER=rashadwest
GITHUB_REPO_NAME=BTEBallCODE
GITHUB_WORKFLOW_FILE=unity-webgl-build.yml
NETLIFY_SITE_ID=your-site-id
NETLIFY_SITE_NAME=ballcode-game
GITHUB_ACTIONS_TOKEN=your-github-pat
NETLIFY_AUTH_TOKEN=your-netlify-token
```

---

## Workflow Architecture

```
Schedule Trigger (every 6 hours)
    ↓
Edit Fields (set request data)
    ↓
Basic LLM Chain (AI analysis)
    ├─ OpenAI Chat Model
    ↓
Edit Fields (parse AI response)
    ↓
Filter (should proceed?)
    ↓
Execute Command (git clone/pull)
    ↓
HTTP Request (trigger GitHub Actions)
    ↓
[GitHub Actions builds Unity WebGL]
    ↓
[GitHub Actions deploys to Netlify]
    ↓
HTTP Request (verify deployment)
    ↓
Edit Fields (completion message)
    ↓
Discord/Webhook (notification)
```

---

## Testing Strategy

### Incremental Testing

Test each phase as you build:
1. **Phase 3.1:** Test Schedule Trigger + Edit Fields
2. **Phase 3.2:** Test AI integration
3. **Phase 3.3:** Test Git operations
4. **Phase 3.4:** Test Build trigger
5. **Phase 3.5:** Test Deployment
6. **Phase 3.6:** Test Notifications

### End-to-End Testing

Once all phases complete:
1. Trigger workflow manually
2. Verify complete flow works
3. Check Netlify for deployed site
4. Verify all steps complete without errors

---

## Activation

### Activate Continuous Running

1. **Set Schedule:**
   - Change Schedule Trigger to desired frequency (every 6 hours)
   - Or keep at 1 minute for testing

2. **Activate Workflow:**
   - Click "Active" toggle in n8n
   - Workflow now runs automatically

3. **Monitor:**
   - Check n8n executions tab
   - Monitor first few runs
   - Verify everything works

---

## Troubleshooting

### Schedule Trigger Not Firing
- Check workflow is "Active"
- Verify timezone settings
- Compare with your working crypto workflow trigger

### AI Analysis Fails
- Check OpenAI credentials
- Verify API key is valid
- Check prompt format

### Git Operations Fail
- Verify repository path is correct
- Check git credentials/permissions
- Verify repository exists

### Build Fails
- Check GitHub Actions logs
- Verify Unity version compatibility
- Check secrets are configured

### Deployment Fails
- Verify Netlify credentials
- Check Site ID is correct
- Verify build output exists

---

## Success Criteria

- [ ] Netlify site created and accessible
- [ ] GitHub secrets configured
- [ ] GitHub Actions workflow exists and works
- [ ] n8n workflow built with your proven pattern
- [ ] Schedule trigger fires reliably
- [ ] AI analysis works correctly
- [ ] Git operations execute successfully
- [ ] Build process triggers (GitHub Actions)
- [ ] Deployment to Netlify completes
- [ ] Notifications send on completion
- [ ] Workflow runs continuously without manual intervention

---

## Manual Intervention Points

**Only revert to manual if:**

1. **Netlify site creation fails** - Need to troubleshoot
2. **GitHub Actions workflow errors** - Need to debug
3. **n8n node configuration issues** - Need to adjust
4. **Credential/permission errors** - Need to verify access

**Otherwise:** Robot handles everything automatically.

---

## Documentation Files

- `PHASE-1-NETLIFY-SETUP-GUIDE.md` - Netlify site setup
- `PHASE-2-GITHUB-ACTIONS-SETUP.md` - GitHub Actions workflow
- `PHASE-3-N8N-WORKFLOW-BUILD.md` - n8n workflow build guide
- `UNITY-ROBOT-COMPLETE-SETUP.md` - This file (overview)

---

## Next Steps

1. **Start with Phase 1:** Follow `PHASE-1-NETLIFY-SETUP-GUIDE.md`
2. **Then Phase 2:** Follow `PHASE-2-GITHUB-ACTIONS-SETUP.md`
3. **Then Phase 3:** Follow `PHASE-3-N8N-WORKFLOW-BUILD.md` incrementally
4. **Test and activate:** Verify everything works, then activate

---

**Copyright © 2025 Rashad West. All Rights Reserved.**





