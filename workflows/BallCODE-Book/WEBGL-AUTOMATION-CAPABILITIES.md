# WebGL Build Automation - What the Robot Can Do

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 5, 2025  
**Status:** ✅ Automation Scripts Ready

---

## 🤖 WHAT I CAN AUTOMATE

### ✅ **Fully Automated (No Manual Steps)**

1. **Check Prerequisites**
   - ✅ Verify GitHub CLI (gh) is installed
   - ✅ Check GitHub authentication status
   - ✅ Auto-login if needed
   - ✅ Verify curl is available

2. **Verify Setup**
   - ✅ Check if workflow file exists in repository
   - ✅ Verify GitHub Secrets are configured
   - ✅ List missing secrets with instructions

3. **Trigger GitHub Actions Workflow**
   - ✅ Trigger WebGL build via GitHub CLI
   - ✅ Get workflow run ID automatically
   - ✅ Provide direct link to monitor build

4. **Monitor Build Progress**
   - ✅ Poll workflow status every 30 seconds
   - ✅ Show elapsed time
   - ✅ Detect completion, failure, or cancellation
   - ✅ Timeout after 30 minutes

5. **Download Build Artifacts**
   - ✅ Download WebGL build automatically
   - ✅ Extract zip file if needed
   - ✅ Verify build files (index.html, Build folder)
   - ✅ Save to `Builds/WebGL/` directory

6. **Check Recent Builds**
   - ✅ List recent workflow runs
   - ✅ Download any completed build by ID
   - ✅ Show build status and timestamps

---

## 🛠️ AUTOMATION TOOLS AVAILABLE

### ✅ **Installed & Ready:**
- **GitHub CLI (gh)** - ✅ Installed at `/opt/homebrew/bin/gh`
- **curl** - ✅ Installed at `/usr/bin/curl`
- **bash** - ✅ Available for scripting

### ⚠️ **Not Installed (Optional):**
- **jq** - JSON parser (can work around with grep/sed)
- **Netlify CLI** - Can install if needed

---

## 📋 WHAT YOU STILL NEED TO DO MANUALLY

### **One-Time Setup (Phase 1):**

1. **Netlify Account**
   - Create account (5 minutes)
   - Get Site ID and Auth Token
   - Add to GitHub Secrets

2. **GitHub Secrets Configuration**
   - Add `NETLIFY_AUTH_TOKEN`
   - Add `NETLIFY_SITE_ID`
   - Add `UNITY_LICENSE` (if using Pro)

3. **Workflow File** (if not exists)
   - Copy `.github/workflows/unity-webgl-build.yml` to Unity repo
   - Or use `copy-workflow-to-unity-repo.sh`

### **After Build (Optional):**

1. **Test Locally**
   - `cd Builds/WebGL && python3 -m http.server 8000`
   - Open browser to test

2. **Deploy to Netlify** (if not auto-deployed)
   - Drag and drop `Builds/WebGL/` folder
   - Or use Netlify CLI: `netlify deploy --prod`

---

## 🚀 HOW TO USE THE AUTOMATION

### **Option 1: Full Automation Script**

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./automate-webgl-build.sh
```

**What it does:**
1. Checks prerequisites
2. Verifies workflow exists
3. Checks GitHub Secrets
4. Gives you 3 options:
   - **1)** Trigger new build → Wait → Download
   - **2)** Download latest completed build
   - **3)** Check status of recent builds

### **Option 2: Manual GitHub CLI Commands**

**Trigger build:**
```bash
gh workflow run unity-webgl-build.yml --repo rashadwest/BTEBallCODE --ref main
```

**Check status:**
```bash
gh run list --repo rashadwest/BTEBallCODE --workflow=unity-webgl-build.yml
```

**Download artifacts:**
```bash
gh run download <RUN_ID> --repo rashadwest/BTEBallCODE --name webgl-build --dir ./Builds/WebGL
```

### **Option 3: GitHub Web UI**

- Go to: https://github.com/rashadwest/BTEBallCODE/actions
- Click "Unity WebGL Build and Deploy"
- Click "Run workflow"
- Wait for completion
- Download artifacts manually

---

## 📊 AUTOMATION COMPARISON

| Task | Manual | Automated Script | GitHub CLI | GitHub UI |
|------|--------|------------------|------------|-----------|
| Check prerequisites | ❌ Manual | ✅ Auto | ✅ Auto | ❌ N/A |
| Verify workflow | ❌ Manual | ✅ Auto | ✅ Auto | ✅ Visual |
| Check secrets | ❌ Manual | ✅ Auto | ✅ Auto | ✅ Visual |
| Trigger build | ✅ Click | ✅ Auto | ✅ Command | ✅ Click |
| Monitor progress | ❌ Refresh | ✅ Auto poll | ✅ Command | ✅ Visual |
| Download artifacts | ❌ Manual | ✅ Auto | ✅ Command | ✅ Click |
| Extract files | ❌ Manual | ✅ Auto | ❌ Manual | ❌ Manual |
| Verify build | ❌ Manual | ✅ Auto | ❌ Manual | ❌ Manual |

**Best Option:** Automated script (`automate-webgl-build.sh`) - Does everything!

---

## 🔧 WHAT I CAN'T AUTOMATE (Yet)

### **Requires Manual Steps:**

1. **Netlify Account Creation**
   - Must create account yourself
   - Must generate auth token
   - Must add secrets to GitHub

2. **Unity Project Changes**
   - Can't edit Unity scripts automatically (would need Unity Agent Client)
   - Can't build locally without WebGL module

3. **Netlify Deployment** (if auto-deploy fails)
   - Can deploy via CLI if Netlify CLI installed
   - Otherwise manual drag-and-drop

4. **Testing Build**
   - Can start local server, but can't test in browser automatically

---

## 🎯 RECOMMENDED WORKFLOW

### **For First Time:**
1. ✅ Run `automate-webgl-build.sh` (checks everything)
2. ⚠️ Add missing GitHub Secrets if needed
3. ✅ Run script again → Option 1 (trigger new build)
4. ✅ Wait for build (script monitors automatically)
5. ✅ Build downloads automatically
6. ⚠️ Test locally (manual)
7. ⚠️ Deploy to Netlify (manual first time, then auto)

### **For Regular Builds:**
1. ✅ Run `automate-webgl-build.sh` → Option 1
2. ✅ Wait (script handles everything)
3. ✅ Done! Build is ready

### **For Quick Download:**
1. ✅ Run `automate-webgl-build.sh` → Option 2
2. ✅ Latest build downloads immediately

---

## 📝 SCRIPT LOCATIONS

- **Main Script:** `automate-webgl-build.sh`
- **Setup Helper:** `automate-setup-helper.sh`
- **Workflow Copy:** `copy-workflow-to-unity-repo.sh`
- **Netlify Deploy:** `deploy-webgl-to-netlify.sh` (if exists)

---

## 🐛 TROUBLESHOOTING

### **"gh: command not found"**
```bash
brew install gh
gh auth login
```

### **"Not authenticated"**
```bash
gh auth login
```

### **"Workflow not found"**
- Check workflow file exists: `.github/workflows/unity-webgl-build.yml`
- See `PHASE-2-GITHUB-ACTIONS-SETUP.md`

### **"Secrets missing"**
- Add via GitHub UI: Settings → Secrets → Actions
- Or via CLI: `gh secret set SECRET_NAME --repo rashadwest/BTEBallCODE`

### **"Build failed"**
- Check workflow logs: https://github.com/rashadwest/BTEBallCODE/actions
- Verify Unity version matches
- Check Unity license if using Pro

---

## ✅ SUMMARY

**What I Can Do:**
- ✅ Check everything is set up correctly
- ✅ Trigger builds automatically
- ✅ Monitor build progress
- ✅ Download artifacts automatically
- ✅ Extract and verify build files

**What You Need to Do:**
- ⚠️ One-time: Netlify account + GitHub Secrets
- ⚠️ Optional: Test build locally
- ⚠️ Optional: Deploy to Netlify (if not auto-deployed)

**Best Approach:**
1. Run `./automate-webgl-build.sh`
2. Follow the prompts
3. Done! 🎉

---

**Status:** ✅ Ready to use  
**Script:** `automate-webgl-build.sh`  
**Time Saved:** ~15 minutes per build (no manual monitoring/downloading)
