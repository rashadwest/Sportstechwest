# n8n Credential Types Guide

**Date:** December 18, 2025  
**Purpose:** Identify correct credential types for GitHub and Netlify

---

## 🔍 CREDENTIAL TYPES NEEDED

### **For GitHub:**

**Option 1: Header Auth (Recommended)**
- **Type:** "Header Auth"
- **Name:** `github-actions-token` (or any name)
- **Header Name:** `Authorization`
- **Header Value:** `token YOUR_GITHUB_PAT`
- **Used by:** Unity Build Orchestrator (calls GitHub API)

**Option 2: GitHub API**
- **Type:** "GitHub API"
- **Name:** `github-api`
- **Token:** `YOUR_GITHUB_PAT`
- **Used by:** If workflow uses GitHub API nodes

**Recommendation:** Use **"Header Auth"** - it's what Unity Build Orchestrator expects.

---

### **For Netlify:**

**Option 1: Header Auth (Recommended)**
- **Type:** "Header Auth"
- **Name:** `netlify-api-token` (or any name)
- **Header Name:** `Authorization`
- **Header Value:** `Bearer YOUR_NETLIFY_TOKEN`
- **Used by:** Unity Build Orchestrator (calls Netlify API)

**Option 2: Netlify API**
- **Type:** "Netlify API"
- **Name:** `netlify-api`
- **Token:** `YOUR_NETLIFY_TOKEN`
- **Used by:** If workflow uses Netlify API nodes

**Recommendation:** Use **"Header Auth"** - it's what Unity Build Orchestrator expects.

---

## 🔍 ABOUT "__n8n_BLANK_VALUE"

**What it is:**
- This is n8n's placeholder for empty credential values
- Appears when a credential exists but has no value set
- Common when credentials are created but not configured

**What to do:**
1. **If you see this:** The credential exists but needs values
2. **Edit the credential:** Add your actual token
3. **Or delete and recreate:** Start fresh with correct values

---

## ✅ CHECKLIST: Do You Already Have Credentials?

**Check in n8n UI:**
1. Go to: http://192.168.1.226:5678
2. Click **Credentials** (left sidebar)
3. Look for:
   - `github-actions-token` or similar GitHub credential
   - `netlify-api-token` or similar Netlify credential

**If they exist:**
- ✅ Check if they have values (not `__n8n_BLANK_VALUE`)
- ✅ If blank: Edit and add your tokens
- ✅ If have values: You're good!

**If they don't exist:**
- Create new credentials (see below)

---

## 🛠️ HOW TO CREATE CREDENTIALS

### **Step 1: Open Credentials**

1. Go to: http://192.168.1.226:5678
2. Click **Credentials** (left sidebar)
3. Click **Add Credential**

### **Step 2: Create GitHub Credential**

1. Search for: **"Header Auth"**
2. Click **"Header Auth"**
3. Fill in:
   - **Credential Name:** `github-actions-token`
   - **Header Name:** `Authorization`
   - **Header Value:** `token YOUR_GITHUB_PAT` (replace YOUR_GITHUB_PAT with actual token)
4. Click **Save**

### **Step 3: Create Netlify Credential**

1. Click **Add Credential** again
2. Search for: **"Header Auth"**
3. Click **"Header Auth"**
4. Fill in:
   - **Credential Name:** `netlify-api-token`
   - **Header Name:** `Authorization`
   - **Header Value:** `Bearer YOUR_NETLIFY_TOKEN` (replace YOUR_NETLIFY_TOKEN with actual token)
5. Click **Save**

---

## 🎯 QUICK REFERENCE

**GitHub:**
- Type: **Header Auth**
- Name: `github-actions-token`
- Value: `token [YOUR_GITHUB_PAT]`

**Netlify:**
- Type: **Header Auth**
- Name: `netlify-api-token`
- Value: `Bearer [YOUR_NETLIFY_TOKEN]`

---

**If credentials UI is also blocked, we'll need to use system-level environment variables instead.** ✅


