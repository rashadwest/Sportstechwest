# Credential vs Header Configuration - Important Difference

**Date:** December 18, 2025  
**Issue:** Understanding the difference between credentials and manual headers

---

## 🔍 WHAT I SEE IN YOUR SCREENSHOT

**You're configuring:**
- A node (possibly "Execute: Curriculum Sy...")
- Using "GitHub API" type
- Manual header with:
  - **Name:** `github-actions-token` ✅
  - **Value:** `token YOUR_GITHUB_PAT` (placeholder)

---

## ⚠️ IMPORTANT: CREDENTIAL vs HEADER

**The workflow expects a CREDENTIAL, not a manual header!**

### **What the workflow needs:**

Looking at the workflow JSON (lines 126-131):
```json
"credentials": {
  "httpHeaderAuth": {
    "id": "github-actions-token",  ← This is a CREDENTIAL ID
    "name": "GitHub Actions Token"
  }
}
```

**The workflow uses:**
- **Node Type:** HTTP Request (not GitHub API node)
- **Authentication:** `httpHeaderAuth` credential
- **Credential ID:** `github-actions-token`

---

## ✅ WHAT YOU NEED TO DO

### **Option 1: Use HTTP Request Node (Recommended)**

**The workflow node "Dispatch GitHub Build" should be:**
1. **Node Type:** HTTP Request
2. **Authentication:** Generic Credential Type → Header Auth
3. **Credential:** Select `github-actions-token` from dropdown
4. **No manual headers needed** - credential adds it automatically

### **Option 2: If Using GitHub API Node**

**If you're configuring a different node:**
- The manual header approach might work
- But the workflow specifically uses HTTP Request with credentials
- Make sure the node you're configuring is the right one

---

## 🎯 CHECK: WHICH NODE ARE YOU CONFIGURING?

**The workflow has these GitHub-related nodes:**
1. **"Dispatch GitHub Build (AIMCODE L2)"** - HTTP Request node
2. **"Check Latest GitHub Run (AIMCODE L3)"** - HTTP Request node

**Both use:**
- HTTP Request node type
- `httpHeaderAuth` credential
- Credential ID: `github-actions-token`

---

## ✅ CORRECT SETUP

**For "Dispatch GitHub Build" node:**

1. **Node Type:** HTTP Request ✅
2. **Method:** POST
3. **URL:** `https://api.github.com/repos/{{ $env.GITHUB_REPO_OWNER }}/{{ $env.GITHUB_REPO_NAME }}/dispatches`
4. **Authentication:** Generic Credential Type
5. **Generic Auth Type:** Header Auth
6. **Credential:** `github-actions-token` (select from dropdown)
7. **Headers:** Only `Accept: application/vnd.github.v3+json` (not Authorization - that comes from credential)

**The credential should be:**
- **Type:** Header Auth
- **ID/Name:** `github-actions-token`
- **Header Name:** `Authorization`
- **Header Value:** `token YOUR_ACTUAL_GITHUB_PAT`

---

## 🔍 WHAT TO CHECK

**In n8n:**
1. **Open:** Unity Build Orchestrator workflow
2. **Click:** "Dispatch GitHub Build" node
3. **Check:**
   - Is it an HTTP Request node? ✅
   - Does it have Authentication section?
   - Is credential `github-actions-token` selected?
   - Are there manual Authorization headers? (Shouldn't need them)

**If you see manual headers with `github-actions-token`:**
- That's a different approach
- The workflow expects credentials instead
- Remove manual headers, use credential dropdown

---

## 📋 SUMMARY

**Your screenshot shows:**
- Manual header configuration ✅ (name is correct)
- But workflow expects credential-based auth

**What to do:**
1. Make sure you're editing the right node ("Dispatch GitHub Build")
2. Use credential dropdown, not manual headers
3. Create/select `github-actions-token` credential (Header Auth type)
4. Remove manual Authorization header (credential adds it)

---

**The workflow uses credentials, not manual headers - make sure you're using the credential dropdown!** ✅


