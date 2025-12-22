# Unity Automation Robot System - Memory Reference
## Fully Automated "Robot" for Unity Development Workflow

**Copyright © 2025 Rashad West. All Rights Reserved.**

**System Name:** Unity Automation Robot  
**Purpose:** Fully automated Unity development workflow (Clone → Edit → Build → Deploy)  
**Location:** Raspberry Pi n8n instance  
**Status:** Documentation complete, ready for implementation

---

## System Overview

This is a **fully automated "robot"** system that handles the complete Unity development workflow without manual intervention:

1. **Clones GitHub repository** (`rashadwest/BTEBallCODE`)
2. **Makes Unity edits** (via AI analysis)
3. **Builds to WebGL** (via GitHub Actions)
4. **Deploys to Netlify** (automatically)
5. **Runs continuously** (every 6 hours via Schedule Trigger)

**Only reverts to manual if there's an absolute blocker.**

---

## Key Components

### 1. Netlify Site
- **Purpose:** Host Unity WebGL build
- **Setup:** One-time manual setup (Phase 1)
- **Credentials:** Site ID, Auth Token stored in GitHub Secrets
- **Status:** Needs to be created

### 2. GitHub Actions Workflow
- **File:** `.github/workflows/unity-webgl-build.yml` in BTEBallCODE repo
- **Purpose:** Automated Unity WebGL build and Netlify deployment
- **Triggers:** Manual, repository_dispatch (n8n), push to main
- **Status:** File exists, needs to be copied to Unity repo

### 3. n8n Workflow
- **Location:** Raspberry Pi n8n instance
- **Pattern:** Matches user's working crypto workflow pattern
- **Nodes:** Schedule Trigger → Edit Fields → Basic LLM Chain → Execute Command → HTTP Request
- **Status:** Needs to be built incrementally

---

## Workflow Architecture

```
Schedule Trigger (every 6 hours, matches crypto workflow)
    ↓
Edit Fields (set initial request data - like Edit Fields1)
    ↓
Basic LLM Chain (AI analysis - like crypto workflow)
    ├─ OpenAI Chat Model (connected as Model input)
    ↓
Edit Fields (parse AI response)
    ↓
Filter (conditional logic - like Filter node)
    ↓
Execute Command (git clone/pull - like Execute Command)
    ↓
HTTP Request (trigger GitHub Actions build)
    ↓
[GitHub Actions: Build Unity WebGL → Deploy to Netlify]
    ↓
HTTP Request (verify deployment)
    ↓
Edit Fields (completion message)
    ↓
Discord/Webhook (notification - like Discord node)
```

---

## Configuration Requirements

### GitHub Secrets (in BTEBallCODE repo)
- `NETLIFY_AUTH_TOKEN` - Netlify access token
- `NETLIFY_SITE_ID` - Netlify site ID
- `NETLIFY_SITE_NAME` - Site name (optional)

### n8n Credentials
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

## Implementation Phases

### Phase 1: Netlify Site Setup (Manual - User Does This)
- **Guide:** `PHASE-1-NETLIFY-SETUP-GUIDE.md`
- **Time:** 15-20 minutes
- **Status:** Waiting for user to complete

### Phase 2: GitHub Actions Workflow
- **Guide:** `PHASE-2-GITHUB-ACTIONS-SETUP.md`
- **Script:** `copy-workflow-to-unity-repo.sh`
- **Time:** 10 minutes
- **Status:** Ready to implement

### Phase 3: n8n Workflow Build
- **Guide:** `PHASE-3-N8N-WORKFLOW-BUILD.md`
- **Pattern:** Matches user's crypto workflow
- **Time:** 1-2 hours (incremental)
- **Status:** Ready to build

---

## Key Files

### Documentation
- `PHASE-1-NETLIFY-SETUP-GUIDE.md` - Netlify setup
- `PHASE-2-GITHUB-ACTIONS-SETUP.md` - GitHub Actions setup
- `PHASE-3-N8N-WORKFLOW-BUILD.md` - n8n workflow build
- `UNITY-ROBOT-COMPLETE-SETUP.md` - Complete overview
- `ROBOT-SETUP-STATUS.md` - Current status tracking

### Scripts
- `copy-workflow-to-unity-repo.sh` - Copy workflow to Unity repo
- `automate-unity-build.sh` - Build Unity to WebGL
- `deploy-webgl-to-netlify.sh` - Deploy to Netlify

### Configuration
- `.github/workflows/unity-webgl-build.yml` - GitHub Actions workflow
- `unity-workflow-config.env` - Environment variables template
- `n8n-unity-automation-workflow.json` - n8n workflow reference

---

## Testing Strategy

### Incremental Testing
Test each phase as built:
1. Phase 3.1: Schedule Trigger + Edit Fields
2. Phase 3.2: AI integration
3. Phase 3.3: Git operations
4. Phase 3.4: Build trigger
5. Phase 3.5: Deployment
6. Phase 3.6: Notifications

### End-to-End Testing
Once complete:
1. Trigger workflow manually
2. Verify complete flow works
3. Check Netlify for deployed site
4. Verify all steps complete without errors

---

## Activation

### Activate Continuous Running
1. Set Schedule Trigger to desired frequency (every 6 hours)
2. Activate workflow in n8n
3. Monitor first few runs
4. Verify everything works

---

## Troubleshooting Reference

### Schedule Trigger Not Firing
- Check workflow is "Active"
- Verify timezone settings
- Compare with working crypto workflow trigger

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
- [ ] n8n workflow built with proven pattern
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
1. Netlify site creation fails
2. GitHub Actions workflow errors
3. n8n node configuration issues
4. Credential/permission errors

**Otherwise:** Robot handles everything automatically.

---

## Memory Format for AI Assistant

**When user mentions "Unity robot" or "Unity automation":**

This refers to the fully automated Unity development workflow system running on Raspberry Pi n8n. The system:
- Uses Schedule Trigger (matches user's crypto workflow pattern)
- Uses Basic LLM Chain + OpenAI Chat Model (matches user's pattern)
- Uses Execute Command nodes (matches user's pattern)
- Automatically: clones repo → AI edits → builds WebGL → deploys to Netlify
- Runs continuously every 6 hours
- Only requires manual intervention for blockers

**Key files:**
- Phase guides: `PHASE-1-NETLIFY-SETUP-GUIDE.md`, `PHASE-2-GITHUB-ACTIONS-SETUP.md`, `PHASE-3-N8N-WORKFLOW-BUILD.md`
- Status: `ROBOT-SETUP-STATUS.md`
- Overview: `UNITY-ROBOT-COMPLETE-SETUP.md`

**Current status:** Documentation complete, waiting for Phase 1 (Netlify setup) to be completed by user.

---

**Copyright © 2025 Rashad West. All Rights Reserved.**





