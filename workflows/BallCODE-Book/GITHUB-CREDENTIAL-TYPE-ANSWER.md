# GitHub Credential Type: Which One to Use?

**Date:** December 18, 2025  
**Question:** Is it "Git" API or something else?

---

## ✅ ANSWER: Use "Header Auth" (NOT "Git" API)

### **For GitHub in n8n:**

**Type:** "Header Auth"  
**NOT:** "Git" API  
**NOT:** "GitHub API"  
**NOT:** "GitHub OAuth2 API"

---

## 🔍 WHY "Header Auth"?

**The Unity Build Orchestrator workflow uses:**
- HTTP Request nodes to call GitHub REST API
- These need **HTTP Header Authentication**
- Not git operations (that's what "Git" API is for)

**What the workflow does:**
1. Calls `https://api.github.com/repos/.../dispatches` (REST API)
2. Needs `Authorization: token YOUR_TOKEN` header
3. This requires "Header Auth" credential type

---

## 📋 HOW TO CREATE IT

**In n8n UI:**

1. **Go to:** Credentials → Add Credential
2. **Search for:** "Header Auth"
3. **Select:** "Header Auth"
4. **Fill in:**
   - **Credential Name:** `github-actions-token`
   - **Header Name:** `Authorization`
   - **Header Value:** `token YOUR_GITHUB_PAT`
     - Replace `YOUR_GITHUB_PAT` with your actual GitHub Personal Access Token
5. **Save**

---

## ❌ NOT "Git" API

**"Git" API is for:**
- Git operations (clone, push, pull)
- Local git commands
- Not for REST API calls

**You need "Header Auth" for:**
- GitHub REST API calls
- Triggering GitHub Actions
- Checking build status

---

## ✅ SUMMARY

**Use:** "Header Auth"  
**Name:** `github-actions-token`  
**Value:** `token [YOUR_GITHUB_PAT]`

**NOT:** "Git" API  
**NOT:** "GitHub API"  
**NOT:** "GitHub OAuth2 API"

---

**Use "Header Auth" - that's what the workflow expects!** ✅

