# 🌐 Consistent Website Deployment Plan - Garvis Integration

**Date:** December 17, 2025  
**Status:** 📋 Complete Automation Plan  
**Purpose:** Ensure consistent, automated website deployments via Garvis + n8n + 24/7 Pi

---

## 🎯 GOAL

**Consistent website pushes that:**
- ✅ Happen automatically when content changes
- ✅ Run 24/7 via Pi infrastructure
- ✅ Integrate with Garvis autonomous system
- ✅ Deploy reliably every time
- ✅ Update website when game/curriculum/book changes

---

## 🏗️ CURRENT INFRASTRUCTURE

### **What We Have:**

1. **✅ Deployment Script:** `BallCode/deploy-ballcode-website.sh`
   - Pushes to GitHub
   - Can trigger Netlify build hook
   - Manual execution currently

2. **✅ n8n Website Auto-Update Workflow:** `n8n-website-auto-update-workflow.json`
   - Webhook: `/webhook/website-update`
   - Handles content, curriculum, book updates
   - Can deploy to Netlify

3. **✅ Netlify Build Hook Setup:**
   - Documentation exists
   - Can be triggered via API
   - Automatic deployment after GitHub push

4. **✅ GitHub Repository:**
   - `JuddCMelvin/BallCode` (correct repo)
   - Connected to Netlify
   - Auto-deploy enabled (or can be)

---

## 🔄 INTEGRATED DEPLOYMENT ARCHITECTURE

### **The Complete Flow:**

```
┌─────────────────────────────────────────────────────────────┐
│  CONTENT CHANGES (Game/Curriculum/Book/Website)             │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│  Garvis Orchestrator (Workflow #2)                          │
│  Identifies: website needs update                           │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│  Website Auto-Update Workflow (n8n)                        │
│  Webhook: POST /webhook/website-update                      │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  • Parses update request                            │  │
│  │  • Determines what needs updating                   │  │
│  │  • Updates website files (HTML/CSS/JS)              │  │
│  │  • Commits changes to GitHub                        │  │
│  │  • Triggers Netlify deployment                     │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│  GitHub Push (Automatic)                                   │
│  Repository: JuddCMelvin/BallCode                           │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│  Netlify Deployment (Automatic)                            │
│  Method 1: Build Hook (Immediate)                          │
│  Method 2: Auto-Deploy (GitHub webhook)                    │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│  Website Live (1-3 minutes)                                │
│  https://ballcode.co                                        │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 DEPLOYMENT METHODS

### **Method 1: n8n Workflow (Recommended - 24/7 Pi)**

**Workflow:** `n8n-website-auto-update-workflow.json`

**How It Works:**
1. Garvis triggers webhook: `POST /webhook/website-update`
2. n8n workflow runs on Pi (24/7 available)
3. Workflow updates website files
4. Commits and pushes to GitHub
5. Triggers Netlify build hook
6. Website deploys automatically

**Benefits:**
- ✅ Runs 24/7 on Pi
- ✅ Fully automated
- ✅ Integrated with Garvis
- ✅ Error handling built-in
- ✅ Progress tracking

**Setup:**
- Import workflow to n8n
- Configure GitHub credentials
- Configure Netlify build hook
- Activate workflow

---

### **Method 2: GitHub Actions (Alternative)**

**File:** `.github/workflows/website-deploy.yml`

**How It Works:**
1. Code pushed to GitHub
2. GitHub Actions workflow triggers
3. Builds website (if needed)
4. Deploys to Netlify automatically

**Benefits:**
- ✅ Runs in cloud (no local resources)
- ✅ Automatic on every push
- ✅ Free for public repos

**Setup:**
- Create GitHub Actions workflow
- Configure Netlify secrets
- Enable on push to main

---

### **Method 3: Netlify Auto-Deploy (Simplest)**

**How It Works:**
1. Code pushed to GitHub
2. Netlify detects push (via webhook)
3. Automatically rebuilds and deploys

**Benefits:**
- ✅ Simplest setup
- ✅ No additional scripts needed
- ✅ Works automatically

**Setup:**
- Connect Netlify to GitHub repo
- Enable "Auto-deploy" in Netlify
- Done!

---

## 🚀 RECOMMENDED SOLUTION: HYBRID APPROACH

### **Best of All Worlds:**

```
┌─────────────────────────────────────────────────────────────┐
│  PRIMARY: n8n Workflow (24/7 Pi)                           │
│  - Handles Garvis-triggered updates                        │
│  - Runs on Pi infrastructure                               │
│  - Full control and error handling                         │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│  FALLBACK: Netlify Auto-Deploy                              │
│  - Catches any direct GitHub pushes                        │
│  - Backup deployment method                                 │
│  - Ensures nothing is missed                                │
└─────────────────────────────────────────────────────────────┘
```

**Why This Works:**
- ✅ Primary: n8n handles all Garvis updates (controlled, tracked)
- ✅ Fallback: Netlify auto-deploy catches manual pushes (safety net)
- ✅ Consistent: Website always updates, no matter how code gets pushed

---

## ⚙️ IMPLEMENTATION PLAN

### **Phase 1: Setup Netlify Auto-Deploy (5 minutes)**

**Step 1: Verify Netlify Connection**
1. Go to: https://app.netlify.com
2. Find site: `ballcode.co`
3. Go to: **Site settings** → **Build & deploy** → **Continuous Deployment**
4. Verify: Connected to `JuddCMelvin/BallCode` repository
5. Verify: **Auto-deploy** is enabled

**Step 2: Create Build Hook (For n8n)**
1. Go to: **Build hooks** section
2. Click: **"Add build hook"**
3. Name: `Garvis Website Deploy`
4. Branch: `main`
5. Copy build hook URL
6. Store in n8n environment: `NETLIFY_WEBSITE_BUILD_HOOK`

---

### **Phase 2: Enhance n8n Website Workflow (30 minutes)**

**Current Workflow:** `n8n-website-auto-update-workflow.json`

**Enhancements Needed:**

1. **Add GitHub Push Node:**
   - After updating files
   - Commit changes
   - Push to `JuddCMelvin/BallCode` repo

2. **Add Netlify Build Hook Trigger:**
   - After successful GitHub push
   - Call Netlify build hook
   - Verify deployment started

3. **Add Deployment Monitoring:**
   - Poll Netlify API for deployment status
   - Wait for completion
   - Report success/failure

4. **Add Schedule Trigger (Optional):**
   - Daily check for pending updates
   - Ensures nothing is missed
   - Runs on Pi 24/7

**Updated Workflow Structure:**
```
1. Webhook Trigger (/webhook/website-update)
2. Parse Website Update
3. Route: Update Content?
4. Route: Update Curriculum Pages?
5. Route: Update Book Pages?
6. Update Content (if needed)
7. Update Curriculum Pages (if needed)
8. Update Book Pages (if needed)
9. Aggregate Results
10. Commit to GitHub (NEW)
11. Push to GitHub (NEW)
12. Trigger Netlify Build Hook (NEW)
13. Monitor Deployment (NEW)
14. Generate Report
15. Respond to Webhook
```

---

### **Phase 3: Integrate with Garvis (Tomorrow)**

**Garvis Integration Points:**

1. **When Game Updates:**
   - Garvis → Unity Build Orchestrator → Game deployed
   - Garvis → Website Auto-Update → Website updated with game links

2. **When Curriculum Updates:**
   - Garvis → Full Integration → Curriculum schema updated
   - Garvis → Website Auto-Update → Curriculum pages regenerated

3. **When Book Updates:**
   - Garvis → Book Content Update → Book files updated
   - Garvis → Website Auto-Update → Book pages updated

4. **Automatic Trigger:**
   - After any system update
   - Garvis automatically calls `/webhook/website-update`
   - Website stays in sync automatically

---

## 📋 CONSISTENCY STRATEGIES

### **Strategy 1: Automatic on Every Change**

**How:**
- Every Garvis update triggers website deployment
- No manual intervention needed
- Website always reflects latest content

**Implementation:**
- Garvis Orchestrator calls website webhook after each system update
- n8n workflow handles deployment automatically

---

### **Strategy 2: Scheduled Consistency Checks**

**How:**
- Daily scheduled check (via n8n Schedule Trigger)
- Compares website content with source systems
- Updates if discrepancies found

**Implementation:**
- Schedule Trigger: Daily at 2 AM
- Checks: Game links, curriculum pages, book pages
- Updates: Only if changes detected

---

### **Strategy 3: Build Queue System**

**How:**
- Queue deployments to prevent conflicts
- Process one at a time
- Ensure consistent state

**Implementation:**
- n8n workflow uses lock mechanism (like Unity Build Orchestrator)
- Prevents overlapping deployments
- Ensures clean deployments

---

## 🔧 CONFIGURATION CHECKLIST

### **n8n Environment Variables:**

- [ ] `GITHUB_PAT` - GitHub Personal Access Token
- [ ] `GITHUB_WEBSITE_REPO` - `JuddCMelvin/BallCode`
- [ ] `NETLIFY_WEBSITE_BUILD_HOOK` - Build hook URL
- [ ] `NETLIFY_WEBSITE_SITE_ID` - Netlify site ID (optional)
- [ ] `NETLIFY_WEBSITE_AUTH_TOKEN` - Netlify auth token (optional)

### **n8n Credentials:**

- [ ] GitHub HTTP Header Auth (for API calls)
- [ ] Netlify HTTP Header Auth (for API calls)

### **Netlify Settings:**

- [ ] Continuous Deployment enabled
- [ ] Connected to `JuddCMelvin/BallCode` repo
- [ ] Build hook created: `Garvis Website Deploy`
- [ ] Auto-deploy enabled for `main` branch

---

## 📊 DEPLOYMENT TRIGGERS

### **Automatic Triggers:**

1. **Garvis System Updates:**
   - Game changes → Website update
   - Curriculum changes → Website update
   - Book changes → Website update
   - Website content changes → Website update

2. **Direct GitHub Pushes:**
   - Manual git push → Netlify auto-deploy
   - Script-based push → Netlify auto-deploy
   - Any push to `main` → Netlify auto-deploy

3. **Scheduled Checks:**
   - Daily at 2 AM → Consistency check
   - Updates if needed → Website update

---

## ✅ SUCCESS CRITERIA

**Consistent Website Pushes When:**
- ✅ Any Garvis update happens → Website deploys automatically
- ✅ Any GitHub push happens → Website deploys automatically
- ✅ Daily consistency check → Website stays in sync
- ✅ Zero manual intervention needed
- ✅ Website always reflects latest content

**Monitoring:**
- ✅ Deployment logs in n8n
- ✅ Netlify deployment history
- ✅ GitHub commit history
- ✅ End-of-day deployment reports

---

## 🚀 QUICK START (Tomorrow)

### **Step 1: Verify Netlify Auto-Deploy (5 min)**
```bash
# Check if auto-deploy is enabled
# Go to: https://app.netlify.com → Site settings → Build & deploy
```

### **Step 2: Create Build Hook (5 min)**
```bash
# In Netlify: Build hooks → Add build hook
# Name: "Garvis Website Deploy"
# Copy URL
```

### **Step 3: Update n8n Workflow (30 min)**
- Add GitHub push node
- Add Netlify build hook trigger
- Add deployment monitoring
- Test workflow

### **Step 4: Integrate with Garvis (1 hour)**
- Update Garvis Orchestrator to call website webhook
- Test end-to-end flow
- Verify automatic deployments

---

## 🔗 RELATED DOCUMENTS

- `GARVIS-N8N-ESSENTIAL-INFRASTRUCTURE.md` - n8n infrastructure
- `n8n-website-auto-update-workflow.json` - Website workflow
- `BallCode/deploy-ballcode-website.sh` - Deployment script
- `BallCode/NETLIFY-AUTO-DEPLOY-SETUP.md` - Netlify setup guide

---

**Consistent website pushes via 24/7 Pi infrastructure!** 🌐✨

