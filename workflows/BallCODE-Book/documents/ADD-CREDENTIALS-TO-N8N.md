# ✅ Add GitHub & Netlify Credentials to n8n

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 16, 2025  
**Status:** You have the tokens - now add them to n8n!

---

## 🎯 QUICK STEPS

### Step 1: Open n8n Settings

1. Open Pi n8n: `http://192.168.1.226:5678`
2. Click **"Settings"** (gear icon, usually top-right or left sidebar)
3. Click **"Credentials"** in the left sidebar

---

## 2️⃣ ADD GITHUB ACTIONS TOKEN

### Step 1: Create New Credential

1. Click **"+ Add Credential"** button (top-right)
2. Search for: **"HTTP Header Auth"**
3. Click on **"HTTP Header Auth"**

### Step 2: Fill in the Fields

1. **Name:** `Authorization`
2. **Value:** `Bearer YOUR_GITHUB_TOKEN`
   - Replace `YOUR_GITHUB_TOKEN` with your actual GitHub token
   - **Important:** Include the word `Bearer` followed by a space, then your token
   - Example: `Bearer ghp_abc123xyz789...`
3. **Credential Name:** `GitHub Actions Token`
   - This is the name you'll see in dropdowns
4. Click **"Save"** or **"Create"**

✅ **GitHub credential created!**

---

## 3️⃣ ADD NETLIFY API TOKEN

### Step 1: Create New Credential

1. Click **"+ Add Credential"** button again
2. Search for: **"HTTP Header Auth"**
3. Click on **"HTTP Header Auth"**

### Step 2: Fill in the Fields

1. **Name:** `Authorization`
2. **Value:** `Bearer YOUR_NETLIFY_TOKEN`
   - Replace `YOUR_NETLIFY_TOKEN` with your actual Netlify token
   - **Important:** Include the word `Bearer` followed by a space, then your token
   - Example: `Bearer abc123xyz789...`
3. **Credential Name:** `Netlify API Token`
   - This is the name you'll see in dropdowns
4. Click **"Save"** or **"Create"**

✅ **Netlify credential created!**

---

## 4️⃣ USE CREDENTIALS IN WORKFLOWS

### For "Trigger Build (GitHub Actions)" Node:

1. Open your workflow (Unity Build Orchestrator)
2. Click on **"Trigger Build (GitHub Actions)"** node
3. Scroll to **"Authentication"** section
4. **Select Credential:** Click the dropdown → Choose **"GitHub Actions Token"**
5. The red warning should disappear! ✅

### For "Check Latest Netlify Deploy" Node:

1. In the same workflow, click on **"Check Latest Netlify Deploy"** node
2. Scroll to **"Authentication"** section
3. **Select Credential:** Click the dropdown → Choose **"Netlify API Token"**

### For "Dispatch GitHub Build" Node:

1. Click on **"Dispatch GitHub Build (AIMCODE L2)"** node
2. Scroll to **"Authentication"** section
3. **Select Credential:** Click the dropdown → Choose **"GitHub Actions Token"**

### For "Check Latest GitHub Run" Node:

1. Click on **"Check Latest GitHub Run (AIMCODE L3)"** node
2. Scroll to **"Authentication"** section
3. **Select Credential:** Click the dropdown → Choose **"GitHub Actions Token"**

---

## 📋 VERIFICATION CHECKLIST

After adding credentials:

- [ ] GitHub Actions Token credential created in n8n
- [ ] Netlify API Token credential created in n8n
- [ ] "Trigger Build (GitHub Actions)" node has credential selected
- [ ] "Check Latest Netlify Deploy" node has credential selected
- [ ] "Dispatch GitHub Build" node has credential selected
- [ ] "Check Latest GitHub Run" node has credential selected
- [ ] No red warnings in any nodes

---

## 🆘 TROUBLESHOOTING

### Credential doesn't appear in dropdown:
- Make sure you saved the credential
- Refresh the workflow page
- Check that the credential name matches exactly

### Still getting authentication errors:
- Verify the token value includes `Bearer ` (with space)
- Check that you copied the entire token (no extra spaces)
- Make sure the token hasn't expired

---

**Version:** 1.0  
**Created:** December 16, 2025  
**Status:** ✅ Ready to Use



