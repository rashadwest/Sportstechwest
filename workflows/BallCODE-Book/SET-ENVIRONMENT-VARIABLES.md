# Set Environment Variables in n8n - Complete Guide

**Date:** December 18, 2025  
**Purpose:** Set GitHub PAT, Netlify Token, and Netlify Site ID in n8n

---

## ⚠️ IMPORTANT: n8n Environment Variables

**n8n does NOT have a public API for setting environment variables.**  
**You must set them in the n8n UI.**

However, I'll provide:
1. Manual steps (via UI)
2. Verification commands (to check they're set)
3. Quick reference for values

---

## 🔧 METHOD 1: Set via n8n UI (Recommended)

### Step 1: Open n8n Settings

1. Go to: http://192.168.1.226:5678
2. Click **Settings** (gear icon, top right)
3. Click **Environment Variables**

### Step 2: Add Each Variable

Click **"Add Variable"** for each:

#### **Variable 1: GITHUB_PAT**
- **Name:** `GITHUB_PAT`
- **Value:** `[paste your GitHub token here]`
- Click **Save**

#### **Variable 2: NETLIFY_AUTH_TOKEN**
- **Name:** `NETLIFY_AUTH_TOKEN`
- **Value:** `[paste your Netlify token here]`
- Click **Save**

#### **Variable 3: NETLIFY_SITE_ID**
- **Name:** `NETLIFY_SITE_ID`
- **Value:** `[paste your Netlify site ID here]`
- Click **Save**

---

## 🔍 METHOD 2: Verify Variables Are Set

After setting variables, verify they're accessible:

```bash
# Test Unity Build Orchestrator (uses these variables)
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test env vars", "branch": "main"}'
```

**If variables are set correctly:**
- Workflow will proceed past "Env Preflight" node
- No error about missing variables

**If variables are missing:**
- Response will include: `"error": "Missing required env var(s): GITHUB_PAT, ..."`

---

## 📋 QUICK REFERENCE: What You Need

### **GITHUB_PAT**
- **What:** GitHub Personal Access Token
- **Where to get:** https://github.com/settings/tokens
- **Scopes needed:** `repo`, `workflow`
- **Format:** `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### **NETLIFY_AUTH_TOKEN**
- **What:** Netlify Access Token
- **Where to get:** https://app.netlify.com/user/applications
- **Format:** `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### **NETLIFY_SITE_ID**
- **What:** Your Netlify site ID
- **Where to get:** Netlify site settings → General → Site ID
- **Format:** `abc123-def456-ghi789` (or similar)

---

## ✅ VERIFICATION SCRIPT

Run this to check if variables are set:

```bash
python scripts/verify-garvis-unity-integration.py
```

**Look for:**
- ✅ "All required environment variables are set" (if set)
- ❌ "Missing required environment variables: ..." (if not set)

---

## 🚨 TROUBLESHOOTING

### Issue: Variables not accessible in workflow

**Solution:**
1. Make sure you're setting them in the **correct n8n instance** (http://192.168.1.226:5678)
2. **Restart n8n** after setting variables (if needed)
3. Check variable names are **exactly** as shown (case-sensitive)
4. Verify no extra spaces in values

### Issue: Workflow still shows "missing variables"

**Solution:**
1. Check n8n logs for errors
2. Verify workflow is using `$env.VARIABLE_NAME` syntax
3. Test with a simple workflow first

---

**Set these 3 variables in n8n UI, then verify with the test script!** ✅

