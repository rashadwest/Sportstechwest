# Verify GitHub Credential Setup

**Date:** December 18, 2025  
**Question:** Is "GitHub API" credential type correct?

---

## ✅ YES - "GitHub API" Should Work!

**What you're creating:**
- Type: "GitHub API" ✅
- Server: `https://api.github.com` ✅
- User: `rashadwest` ✅
- Access Token: `YOUR_GITHUB_PAT` ✅

**This looks correct!**

---

## 🔍 HOW IT WORKS

**"GitHub API" credential type:**
- n8n's service-specific credential for GitHub
- Automatically formats authentication correctly
- Provides `Authorization: token YOUR_TOKEN` header
- Works with GitHub REST API calls

**The workflow will use this credential for:**
- `POST https://api.github.com/repos/rashadwest/BTEBallCODE/dispatches`
- `GET https://api.github.com/repos/rashadwest/BTEBallCODE/actions/workflows/...`

**This should work!**

---

## ⚠️ IMPORTANT: Credential Name

**Make sure the credential name matches:**

**In n8n, when creating the credential:**
- **Name:** `github-actions-token` ← Must match this exactly!

**Why:**
- The workflow JSON references: `"id": "github-actions-token"`
- If the name doesn't match, the workflow won't find it

**Check:**
- After creating, verify the credential name is exactly: `github-actions-token`
- Not: `github-api` or `github-token` or anything else

---

## ✅ VERIFICATION CHECKLIST

**Your credential should have:**
- ✅ Type: "GitHub API"
- ✅ Server: `https://api.github.com`
- ✅ User: `rashadwest`
- ✅ Access Token: `YOUR_GITHUB_PAT` (your actual token)
- ✅ **Name:** `github-actions-token` ← Critical!

**If all match, you're good!**

---

## 🧪 HOW TO TEST

**After creating the credential:**

1. **Re-import workflow** in n8n (if you modified it)
2. **Test the workflow:**
   ```bash
   curl -X POST http://192.168.1.226:5678/webhook/unity-build \
     -H "Content-Type: application/json" \
     -d '{"request": "Test credential", "branch": "main"}'
   ```

3. **Check execution:**
   - Go to n8n UI → Executions
   - See if it succeeds or fails
   - If it fails with "authentication" error, credential might need adjustment

---

## 📋 SUMMARY

**Your setup looks correct!**

- ✅ "GitHub API" credential type is fine
- ✅ Server URL is correct
- ✅ User is correct
- ✅ Access Token field is correct

**Just make sure:**
- ✅ Credential name is exactly: `github-actions-token`
- ✅ Access Token is your actual GitHub PAT (not placeholder)

**This should work!** ✅

---

**If the workflow fails, check the credential name matches exactly!**

