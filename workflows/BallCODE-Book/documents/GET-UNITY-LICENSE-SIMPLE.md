# Simple Guide: Get Unity License for GitHub Actions

**Date:** December 24, 2025  
**Method:** Use Unity Hub (Easiest)

---

## 🎯 EASIEST METHOD: Use Unity Hub

### **Step 1: Open Unity Hub**

1. **Launch Unity Hub:**
   - Click Unity Hub icon in Applications
   - Or: `open -a "Unity Hub"`

---

### **Step 2: Get License Info**

1. **Click Settings (Gear Icon):**
   - Top right of Unity Hub window
   - Or: Unity Hub menu → Preferences

2. **Click "Licenses" Tab:**
   - Left sidebar in Settings window
   - You'll see your active license(s)

3. **View License Details:**
   - You'll see license type (usually "Personal")
   - Serial number is displayed (if available)
   - License status

---

### **Step 3: Get Serial Number**

**Option A: Serial Number Visible**
- Copy the serial number shown
- Format: `XXXX-XXXX-XXXX-XXXX-XXXX-XXXX`

**Option B: Generate License File**
1. In Unity Hub, click **"Manage License"** button
2. Follow prompts to activate/generate license
3. License file will be created at:
   ```
   ~/Library/Application Support/Unity/Unity_lic.ulf
   ```

---

## 🎯 METHOD 2: Get License File Directly

### **If License File Exists:**

**Check these locations:**
```bash
# Location 1 (most common)
~/Library/Application Support/Unity/Unity_lic.ulf

# Location 2 (alternative)
~/.unity3d/Unity_lic.ulf

# Location 3 (older versions)
~/Library/Preferences/com.unity3d.UnityEditor5.x.plist
```

**Open in Finder:**
1. Press `Cmd + Shift + G` in Finder
2. Type: `~/Library/Application Support/Unity/`
3. Look for `Unity_lic.ulf` file
4. Open it with TextEdit
5. Copy all contents

---

## 🎯 METHOD 3: Generate License via Unity Editor

### **If No License File Exists:**

1. **Open Unity Editor:**
   ```bash
   open -a Unity\ Hub /Users/rashadwest/BTEBallCODE
   ```

2. **Unity will prompt for license:**
   - If first time opening, Unity will ask to activate
   - Follow activation steps
   - License file will be created automatically

3. **After activation:**
   - License file created at: `~/Library/Application Support/Unity/Unity_lic.ulf`
   - Copy file contents

---

## 📋 ADD TO GITHUB SECRETS

### **Step 1: Go to GitHub**

1. **Navigate to:**
   ```
   https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
   ```

2. **Or manually:**
   - Go to repository: https://github.com/rashadwest/BTEBallCODE
   - Click **Settings** (top right)
   - Click **Secrets and variables** → **Actions**

---

### **Step 2: Add Secret**

**For License File (Recommended):**
1. Click **New repository secret**
2. **Name:** `UNITY_LICENSE`
3. **Secret:** Paste entire contents of `Unity_lic.ulf` file
4. Click **Add secret**

**OR For Serial Number:**
1. Click **New repository secret**
2. **Name:** `UNITY_SERIAL`
3. **Secret:** Paste your Unity serial number
4. Click **Add secret**

---

## ✅ QUICK CHECKLIST

- [ ] Open Unity Hub
- [ ] Go to Settings → Licenses
- [ ] Copy serial number OR generate license file
- [ ] Go to GitHub repository settings
- [ ] Navigate to Secrets → Actions
- [ ] Add secret: `UNITY_LICENSE` or `UNITY_SERIAL`
- [ ] Paste license info
- [ ] Save secret
- [ ] Trigger new build

---

## 🔗 DIRECT LINKS

**GitHub Secrets:**
```
https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
```

**Unity Hub:**
- Applications → Unity Hub
- Or: `open -a "Unity Hub"`

**License File Location:**
```
~/Library/Application Support/Unity/Unity_lic.ulf
```

---

**Start with Unity Hub - it's the easiest way to get your license info!**


