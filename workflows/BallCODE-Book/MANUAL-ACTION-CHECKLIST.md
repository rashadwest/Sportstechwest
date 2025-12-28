# Manual Action Checklist - What You Need to Do

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 2025  
**Status:** Ready for Your Action  
**Priority:** High → Low

---

## 🎯 YOUR ACTION ITEMS (In Priority Order)

### 🔴 CRITICAL: Phase 1 - Netlify Setup (15-20 minutes)

**Why:** This unlocks all automation. Robot can't proceed without this.

**Follow:** `PHASE-1-NETLIFY-SETUP-GUIDE.md`

#### Step 1: Create Netlify Account (5 min)
- [ ] Go to https://app.netlify.com/signup
- [ ] Sign up (email or GitHub)
- [ ] Verify email
- [ ] Log in to dashboard

#### Step 2: Get WebGL Build (10-15 min)
**Option A (Easiest - Recommended):**
- [ ] Go to GitHub: `https://github.com/rashadwest/BTEBallCODE`
- [ ] Click "Actions" tab
- [ ] Find "Unity WebGL Build" workflow
- [ ] Click "Run workflow" → "Run workflow"
- [ ] Wait 10-15 minutes for build
- [ ] Download "webgl-build" artifact
- [ ] Extract zip file

**Option B (If GitHub Actions not ready):**
- [ ] Open Unity Editor
- [ ] File → Build Settings → WebGL
- [ ] Build to `Builds/WebGL/`
- [ ] Wait 5-10 minutes

#### Step 3: Deploy to Netlify (5 min)
- [ ] Go to https://app.netlify.com
- [ ] Click "Add new site" → "Deploy manually"
- [ ] Drag and drop `Builds/WebGL/` folder
- [ ] Wait for upload
- [ ] Note your site URL (e.g., `https://random-name-12345.netlify.app`)

#### Step 4: Get Credentials (5 min)
- [ ] **Get Site ID:**
  - [ ] Click your site in Netlify
  - [ ] Settings → General
  - [ ] Copy "Site ID" (looks like: `abc123-def456-ghi789`)
  - [ ] Save it somewhere safe

- [ ] **Get Auth Token:**
  - [ ] Click profile icon (top right) → "User settings"
  - [ ] Go to "Applications" tab
  - [ ] Scroll to "Personal access tokens"
  - [ ] Click "New access token"
  - [ ] Name: "Unity Automation"
  - [ ] Click "Generate token"
  - [ ] **COPY TOKEN IMMEDIATELY** (you won't see it again!)
  - [ ] Save it securely

#### Step 5: Add to GitHub Secrets (2 min)
- [ ] Go to: `https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions`
- [ ] Click "New repository secret"
- [ ] Add `NETLIFY_AUTH_TOKEN` = (your token from Step 4)
- [ ] Add `NETLIFY_SITE_ID` = (your Site ID from Step 4)
- [ ] Add `NETLIFY_SITE_NAME` = (your site name, optional)

**✅ Checkpoint:** Phase 1 complete! Robot can now automate everything else.

---

### 🟡 HIGH: Phase 2 - GitHub Actions Verification (10 minutes)

**Why:** Ensures automated builds work

**Follow:** `PHASE-2-GITHUB-ACTIONS-SETUP.md`

- [ ] Verify workflow file exists:
  - [ ] Go to: `https://github.com/rashadwest/BTEBallCODE`
  - [ ] Check: `.github/workflows/unity-webgl-build.yml` exists
  - [ ] If missing, run: `./copy-workflow-to-unity-repo.sh`

- [ ] Test workflow:
  - [ ] Go to Actions tab
  - [ ] Click "Unity WebGL Build"
  - [ ] Click "Run workflow" → "Run workflow"
  - [ ] Watch build complete
  - [ ] Verify build succeeds

**✅ Checkpoint:** GitHub Actions working! Robot can trigger builds automatically.

---

### 🟡 HIGH: Phase 3 - n8n Workflow Initial Setup (1-2 hours)

**Why:** Sets up the automation robot

**Follow:** `PHASE-3-N8N-WORKFLOW-BUILD.md` OR use remote building

**Option A: Remote Building (Recommended - Faster)**
- [ ] Set up n8n API access:
  - [ ] Open n8n: `http://your-raspberry-pi-ip:5678`
  - [ ] Settings → API → Generate API key
  - [ ] Save to `.n8n-env` file

- [ ] Deploy workflow remotely:
  ```bash
  ./deploy-n8n-workflow.sh n8n-unity-automation-workflow.json
  ```

- [ ] Configure credentials in n8n UI:
  - [ ] Add OpenAI API credentials
  - [ ] Add GitHub Personal Access Token
  - [ ] Add Netlify Auth Token (optional)

- [ ] Set environment variables:
  - [ ] Settings → Environment Variables
  - [ ] Add variables from `unity-workflow-config.env`

- [ ] Test workflow:
  - [ ] Execute manually
  - [ ] Verify each node works
  - [ ] Activate workflow

**Option B: Manual Building (Traditional)**
- [ ] Follow `PHASE-3-N8N-WORKFLOW-BUILD.md` step-by-step
- [ ] Build nodes incrementally
- [ ] Test each node

**✅ Checkpoint:** n8n workflow ready! Robot can run continuously.

---

### 🟢 MEDIUM: Account Verification (5 minutes)

**Quick Check:**
- [ ] Netlify account active and accessible
- [ ] GitHub repo access confirmed
- [ ] OpenAI API key available (if using AI features)
- [ ] n8n running on Raspberry Pi
- [ ] All credentials saved securely

---

### 🟢 LOW: Optional Optimizations

**Only if you want:**
- [ ] Customize n8n workflow schedule
- [ ] Set up additional notifications
- [ ] Configure custom domain on Netlify
- [ ] Set up monitoring/alerting

---

## 📋 Quick Reference

### What Robot Handles (After Setup):
- ✅ All n8n workflow updates
- ✅ All deployments
- ✅ All builds (via GitHub Actions)
- ✅ All website updates
- ✅ All book uploads

### What You Do (One-Time):
- ⚠️ Phase 1: Netlify setup (15-20 min)
- ⚠️ Phase 2: GitHub Actions verification (10 min)
- ⚠️ Phase 3: n8n initial setup (1-2 hours)

**Total Manual Time:** ~2-3 hours (one-time)  
**Then:** Robot handles everything!

---

## 🚀 After Manual Setup Complete

### For Future Updates:
1. **n8n Workflows:** Ask Claude → `./deploy-n8n-workflow.sh` ✅
2. **Website:** `cd BallCode && ./deploy-ballcode-website.sh` ✅
3. **Books:** `python3 automate-book-upload.py ...` ✅
4. **Builds:** Triggered automatically ✅

**Everything else is automated!**

---

## 📞 Need Help?

**If stuck on any step:**
1. Check the detailed guide for that phase
2. Review `ROBOT-VS-MANUAL-TASKS.md` for context
3. Ask Claude for help with specific steps

**Key Documents:**
- `PHASE-1-NETLIFY-SETUP-GUIDE.md` - Detailed Netlify setup
- `PHASE-2-GITHUB-ACTIONS-SETUP.md` - GitHub Actions setup
- `PHASE-3-N8N-WORKFLOW-BUILD.md` - n8n workflow build
- `ROBOT-VS-MANUAL-TASKS.md` - Complete breakdown

---

**Copyright © 2025 Rashad West. All Rights Reserved.**




