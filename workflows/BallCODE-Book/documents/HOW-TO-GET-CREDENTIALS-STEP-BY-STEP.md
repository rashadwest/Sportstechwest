# 🔐 How to Get Credentials - Step-by-Step Instructions

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 16, 2025  
**Purpose:** Detailed visual guide to get GitHub and Netlify tokens

---

## 1️⃣ GITHUB ACTIONS TOKEN

### Step 1: Go to GitHub Settings

1. Open GitHub in your browser: https://github.com
2. Click your **profile picture** (top-right corner)
3. Click **"Settings"** from the dropdown menu

### Step 2: Navigate to Developer Settings

1. In the left sidebar, scroll down to the bottom
2. Click **"Developer settings"** (at the very bottom of the sidebar)

### Step 3: Go to Personal Access Tokens

1. In the Developer settings page, you'll see two options:
   - **Fine-grained tokens** (newer)
   - **Tokens (classic)** ← **Click this one**
2. Click **"Tokens (classic)"**

### Step 4: Generate New Token

1. Click the **"Generate new token"** button
2. Select **"Generate new token (classic)"** from the dropdown

### Step 5: Configure Token

1. **Note:** Give it a name like "n8n GitHub Actions"
2. **Expiration:** Choose how long it should last (90 days, 1 year, or no expiration)
3. **Select scopes:** Check these boxes:
   - ✅ **`repo`** (Full control of private repositories)
     - This includes: `repo:status`, `repo_deployment`, `public_repo`, `repo:invite`, `security_events`
   - ✅ **`workflow`** (Update GitHub Action workflows)
4. Scroll down and click **"Generate token"** (green button at bottom)

### Step 6: Copy Token

⚠️ **IMPORTANT:** Copy the token immediately! You won't be able to see it again.

1. You'll see a page with your token (starts with `ghp_...`)
2. **Copy the entire token** (click the copy icon or select all and copy)
3. Save it somewhere safe temporarily (you'll paste it into n8n next)

---

## 2️⃣ ADD GITHUB TOKEN TO N8N

### Step 1: Open n8n Settings

1. Open Pi n8n: `http://192.168.1.226:5678`
2. Click **"Settings"** (gear icon, usually top-right or in left sidebar)

### Step 2: Go to Credentials

1. In Settings, click **"Credentials"** in the left sidebar

### Step 3: Create New Credential

1. Click **"+ Add Credential"** button (or "Create Credential")
2. Search for or find: **"HTTP Header Auth"**
3. Click on **"HTTP Header Auth"**

### Step 4: Configure HTTP Header Auth

1. **Name:** `Authorization`
2. **Value:** `Bearer YOUR_GITHUB_TOKEN`
   - Replace `YOUR_GITHUB_TOKEN` with the token you copied (starts with `ghp_...`)
   - Example: `Bearer ghp_abc123xyz789...`
3. **Credential Name:** Enter `GitHub Actions Token` (this is what you'll see in dropdowns)
4. Click **"Save"** or **"Create"**

✅ **Done!** You now have "GitHub Actions Token" credential in n8n.

---

## 3️⃣ NETLIFY API TOKEN

### Step 1: Go to Netlify

1. Open Netlify in your browser: https://app.netlify.com
2. **Log in** to your account

### Step 2: Go to User Settings

1. Click your **profile picture/avatar** (top-right corner)
2. Click **"User settings"** from the dropdown menu

### Step 3: Navigate to Applications

1. In User settings, look for **"Applications"** in the left sidebar
2. Click **"Applications"**

### Step 4: Find Personal Access Tokens

1. In the Applications page, you'll see **"OAuth"** (this is for OAuth apps, not what you need)
2. Look for **"Personal access tokens"** section (it might be below OAuth or in a different tab)
3. If you don't see it, look for:
   - A tab or section labeled **"Personal access tokens"**
   - Or a button/link that says **"New access token"** or **"Create access token"**
   - Or check if there's a dropdown/selector to switch between "OAuth" and "Personal access tokens"

### Step 5: Create Access Token

1. Once you find the Personal access tokens section, click **"New access token"** button (or "Create access token" or "Generate token")

### Step 5: Configure Token

1. **Description:** Enter something like "n8n Automation"
2. Click **"Generate token"** (or "Create")

### Step 6: Copy Token

⚠️ **IMPORTANT:** Copy the token immediately! You won't be able to see it again.

1. You'll see your token (usually a long string)
2. **Copy the entire token**
3. Save it somewhere safe temporarily

---

## 4️⃣ ADD NETLIFY TOKEN TO N8N

### Step 1: Open n8n Settings

1. Open Pi n8n: `http://192.168.1.226:5678`
2. Click **"Settings"** → **"Credentials"**

### Step 2: Create New Credential

1. Click **"+ Add Credential"**
2. Search for: **"HTTP Header Auth"**
3. Click on **"HTTP Header Auth"**

### Step 3: Configure HTTP Header Auth

1. **Name:** `Authorization`
2. **Value:** `Bearer YOUR_NETLIFY_TOKEN`
   - Replace `YOUR_NETLIFY_TOKEN` with the token you copied
   - Example: `Bearer abc123xyz789...`
3. **Credential Name:** Enter `Netlify API Token` (this is what you'll see in dropdowns)
4. Click **"Save"** or **"Create"**

✅ **Done!** You now have "Netlify API Token" credential in n8n.

---

## 5️⃣ USE CREDENTIALS IN WORKFLOWS

### In "Trigger Build (GitHub Actions)" Node:

1. Open the workflow
2. Click on **"Trigger Build (GitHub Actions)"** node
3. In **"Authentication"** section:
   - Authentication: **Generic Credential Type** ✅
   - Generic Auth Type: **Header Auth** ✅
   - **Select Credential:** Click dropdown → Choose **"GitHub Actions Token"**
4. The red warning should disappear!

### In "Check Latest Netlify Deploy" Node:

1. Open the workflow
2. Click on **"Check Latest Netlify Deploy"** node
3. In **"Authentication"** section:
   - Authentication: **Generic Credential Type** ✅
   - Generic Auth Type: **Header Auth** ✅
   - **Select Credential:** Click dropdown → Choose **"Netlify API Token"**

---

## 📋 QUICK REFERENCE

### GitHub Token:
- **URL:** https://github.com/settings/tokens
- **Direct path:** Profile → Settings → Developer settings → Tokens (classic) → Generate new token
- **Scopes needed:** `repo` and `workflow`
- **Token format:** Starts with `ghp_...`

### Netlify Token:
- **URL:** https://app.netlify.com/user/applications
- **Direct path:** Profile → User settings → Applications → New access token
- **Token format:** Long alphanumeric string

### n8n Credential Setup:
- **Type:** HTTP Header Auth
- **Name field:** `Authorization`
- **Value field:** `Bearer [YOUR_TOKEN]` (include "Bearer " prefix!)
- **Credential Name:** "GitHub Actions Token" or "Netlify API Token"

---

## 🆘 TROUBLESHOOTING

### "Invalid credentials" error:
- Make sure you included `Bearer ` (with space) before the token
- Check that you copied the entire token (no spaces or line breaks)
- Verify the token hasn't expired

### Can't find "Developer settings" in GitHub:
- Make sure you're logged into GitHub
- It's at the very bottom of the Settings sidebar
- Try scrolling down in the left sidebar

### Can't find "Applications" in Netlify:
- Make sure you're in User settings (not Team settings)
- Look in the left sidebar under User settings
- It might be under "Access tokens" or "API tokens"

---

**Version:** 1.0  
**Created:** December 16, 2025  
**Status:** ✅ Complete Step-by-Step Guide

