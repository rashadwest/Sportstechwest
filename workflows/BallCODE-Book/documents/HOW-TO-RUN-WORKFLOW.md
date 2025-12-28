# How to Run Unity Build Workflow

**Date:** December 24, 2025

---

## 🚀 HOW TO TRIGGER THE WORKFLOW

### **Method 1: Manual Trigger (Recommended for Testing)**

**Step 1: Go to Workflow Page**
- URL: https://github.com/rashadwest/BTEBallCODE/actions/workflows/unity-webgl-build.yml
- (I'll open this for you)

**Step 2: Click "Run workflow"**
- On the right side, you'll see a blue button: **"Run workflow"**
- Click it!

**Step 3: Select Branch**
- A dropdown will appear
- Select: **"main"** (should be default)

**Step 4: Click "Run workflow"**
- Click the green **"Run workflow"** button
- Workflow will start immediately!

**Step 5: Watch It Run**
- You'll see a new workflow run appear
- Click on it to see the build progress
- Watch the logs in real-time!

---

### **Method 2: Automatic Trigger (On Push)**

**The workflow runs automatically when:**
- ✅ You push changes to `main` branch
- ✅ Changes are in these paths:
  - `Unity-Scripts/**`
  - `Assets/**`
  - `ProjectSettings/**`
  - `.github/workflows/unity-webgl-build.yml`

**To trigger automatically:**
```bash
# Make any change and push
cd /Users/rashadwest/BTEBallCODE
git add .
git commit -m "Trigger build"
git push origin main
```

---

## 📋 WHAT HAPPENS WHEN IT RUNS

**The workflow will:**
1. ✅ Checkout your code
2. ✅ Setup Unity 2021.3.15f1
3. ✅ Activate Unity license (using email/password)
4. ✅ Build Unity WebGL project
5. ✅ Verify build output
6. ✅ Upload build artifacts
7. ✅ Deploy to Netlify
8. ✅ Verify deployment

**Total time:** ~5-10 minutes

---

## 🔍 HOW TO WATCH THE BUILD

**After clicking "Run workflow":**

1. **You'll see a new run appear** (at the top of the list)
2. **Click on it** to see details
3. **Watch each step:**
   - Green checkmark ✅ = Step succeeded
   - Yellow circle ⏳ = Step running
   - Red X ❌ = Step failed

4. **Click on a step** to see logs
5. **Watch for errors** in the logs

---

## ⚠️ IF IT FAILS

**Check the logs:**
1. Click on the failed step
2. Scroll through the logs
3. Look for error messages (usually in red)
4. Common issues:
   - License activation failed
   - Compilation errors
   - Missing files
   - Build errors

**Then we can fix it together!**

---

## ✅ QUICK START

**Right now:**
1. I opened the workflow page for you
2. Click **"Run workflow"** (blue button on right)
3. Select **"main"** branch
4. Click **"Run workflow"** (green button)
5. Watch it build!

---

## 🎯 SUMMARY

**To run workflow:**
1. Go to workflow page (I opened it)
2. Click "Run workflow"
3. Select "main"
4. Click "Run workflow"
5. Watch it run!

**That's it!** 🚀


