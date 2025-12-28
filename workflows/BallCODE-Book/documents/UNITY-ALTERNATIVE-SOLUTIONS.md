# Unity CI/CD Alternative Solutions - Complete Guide

**Date:** December 24, 2025  
**Problem:** Unity Personal license doesn't work in GitHub Actions CI/CD  
**Goal:** Find alternative solutions that work NOW

---

## 🎯 KEY FINDING FROM RESEARCH

**From game.ci documentation:**
> "Unity Personal License: Activate Unity on a local machine using Unity Hub, locate the `.ulf` file, extract the serial from it, and store the serial along with Unity credentials in your CI/CD environment variables."

**This means:**
- ✅ Personal licenses CAN work in CI/CD
- ✅ Need to extract serial from local `.ulf` file
- ✅ Use serial + credentials in GitHub Secrets

---

## ✅ SOLUTION 1: Extract Serial from Local License File (BEST OPTION)

### **How It Works:**
1. **Activate Unity locally** (already done in Unity Hub)
2. **Find `.ulf` file** on your Mac
3. **Extract serial number** from the file
4. **Add to GitHub Secrets** as `UNITY_SERIAL`
5. **Build works in GitHub Actions!**

### **Step-by-Step:**

#### **Step 1: Find License File**

**On Mac, license files are at:**
- `/Library/Application Support/Unity/`
- OR `~/Library/Application Support/Unity/`

**Let's check:**
```bash
ls -la "/Library/Application Support/Unity/"*.ulf
ls -la ~/Library/Application\ Support/Unity/*.ulf 2>/dev/null
```

#### **Step 2: Extract Serial Number**

**Open `.ulf` file in text editor:**
- Look for `<Serial>` tag
- Copy the serial number (format: `XXXX-XXXX-XXXX-XXXX-XXXX-XXXX`)

#### **Step 3: Add to GitHub Secrets**

1. **Go to:** https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
2. **Add secret:**
   - Name: `UNITY_SERIAL`
   - Value: Serial number from `.ulf` file
3. **Keep existing secrets:**
   - `UNITY_EMAIL` (already added)
   - `UNITY_PASSWORD` (already added)

#### **Step 4: Test Build**

**Trigger GitHub Actions build - it should work!**

**This is the BEST solution - works immediately!**

---

## ✅ SOLUTION 2: Build Locally, Deploy Automatically

### **How It Works:**
1. **Build Unity on your Mac** (no license issues)
2. **Automatically deploy to Netlify** via script
3. **Trigger via webhook** or GitHub push

### **Setup:**

#### **Step 1: Create Local Build Script**

```bash
#!/bin/bash
# Build Unity WebGL locally and deploy to Netlify

UNITY_PATH="/Applications/Unity/Hub/Editor/2021.3.45f2/Unity.app/Contents/MacOS/Unity"
PROJECT_PATH="/Users/rashadwest/BTEBallCODE"
BUILD_PATH="$PROJECT_PATH/Builds/WebGL"

# Build Unity WebGL
"$UNITY_PATH" -quit -batchmode -projectPath "$PROJECT_PATH" -buildTarget WebGL -buildPath "$BUILD_PATH"

# Deploy to Netlify
cd "$PROJECT_PATH"
netlify deploy --prod --dir="$BUILD_PATH"
```

#### **Step 2: Trigger from GitHub (Optional)**

**Use n8n webhook:**
- GitHub push → n8n webhook → Run script on Mac
- OR: Manual trigger when needed

**This works but requires your Mac to be running.**

---

## ✅ SOLUTION 3: Unity Cloud Build (Free for Personal)

### **How It Works:**
1. **Connect GitHub repository** to Unity Cloud Build
2. **Unity handles license automatically**
3. **Builds trigger on push**
4. **Deploys to Netlify** (or other hosting)

### **Setup:**

1. **Go to:** https://unity.com/products/unity-cloud-build
2. **Sign in** with Unity ID
3. **Connect GitHub repository**
4. **Configure build settings:**
   - Platform: WebGL
   - Unity version: 2021.3.45f2
   - Build target: WebGL
5. **Set up deployment:**
   - Deploy to Netlify
   - OR download build and deploy manually

**This is free for Personal licenses and handles license automatically!**

---

## ✅ SOLUTION 4: Self-Hosted GitHub Actions Runner

### **How It Works:**
1. **Install GitHub Actions runner** on your Mac
2. **Runner uses local Unity** (no license issues)
3. **Builds run on your Mac** instead of GitHub servers
4. **Deploys automatically** to Netlify

### **Setup:**

1. **Install GitHub Actions runner:**
   - Go to: https://github.com/rashadwest/BTEBallCODE/settings/actions/runners
   - Click "New self-hosted runner"
   - Follow instructions for macOS

2. **Configure runner:**
   - Install Unity on Mac (already done)
   - Runner uses local Unity installation
   - No license file needed (uses local activation)

3. **Update workflow:**
   - Change `runs-on: ubuntu-latest` to `runs-on: self-hosted`
   - Use local Unity path

**This works but requires your Mac to be running 24/7 (or when builds needed).**

---

## 🎯 RECOMMENDED ORDER

### **1. Try Solution 1 First (Extract Serial from .ulf file)**
- ✅ Works immediately
- ✅ No infrastructure changes
- ✅ Uses existing GitHub Actions
- ✅ **This is the BEST solution!**

### **2. If Solution 1 doesn't work: Try Solution 3 (Unity Cloud Build)**
- ✅ Free for Personal licenses
- ✅ Automatic license handling
- ✅ No local machine needed
- ✅ Professional CI/CD solution

### **3. If you need more control: Try Solution 2 (Local Build Script)**
- ✅ Full control over build process
- ✅ Works with local Unity
- ⚠️ Requires Mac to be running

### **4. If you want self-hosted: Try Solution 4 (Self-Hosted Runner)**
- ✅ Uses local Unity
- ✅ Full control
- ⚠️ Requires Mac running 24/7

---

## 📋 QUICK START: Solution 1 (Extract Serial)

**Let's try this NOW:**

1. **Find license file:**
   ```bash
   find ~/Library -name "*.ulf" 2>/dev/null
   find /Library -name "*.ulf" 2>/dev/null
   ```

2. **Open file and extract serial:**
   - Look for `<Serial>` tag
   - Copy serial number

3. **Add to GitHub Secrets:**
   - Name: `UNITY_SERIAL`
   - Value: Serial from file

4. **Test build!**

**This should work immediately!**

---

## ✅ SUMMARY

**Best Solutions (in order):**

1. **✅ Extract serial from local `.ulf` file** (BEST - works immediately)
2. **✅ Unity Cloud Build** (Free, automatic license)
3. **✅ Local build script** (Full control, requires Mac running)
4. **✅ Self-hosted GitHub Actions runner** (Full control, requires Mac 24/7)

**Let's try Solution 1 first - it should work right away!**


