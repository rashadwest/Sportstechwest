# Which GitHub Credential Type to Use?

**Date:** December 18, 2025  
**Question:** Is "Git" the right one? Which should I use?

---

## ❌ NOT "Git"

**What you're seeing:**
- "Git account" with Username/Password fields
- This is for **git operations** (clone, push, pull)
- **NOT for GitHub REST API calls**

**What the workflow needs:**
- GitHub REST API calls (triggering GitHub Actions)
- HTTP Header Authentication
- Token-based auth (not username/password)

---

## ✅ ANSWER: Use "GitHub API" (If Available)

**From your list, use:**
- ✅ **"GitHub API"** ← This one!
- ❌ NOT "Git" (that's for git commands)
- ❌ NOT "GitHub OAuth2 API" (that's for OAuth flows)
- ❌ NOT "GitLab" (wrong service)

---

## 🔍 HOW TO CREATE "GitHub API" CREDENTIAL

**If "GitHub API" option exists in n8n:**

1. **Go to:** Credentials → Add Credential
2. **Search for:** "GitHub API"
3. **Select:** "GitHub API"
4. **Fill in:**
   - **Credential Name:** `github-actions-token`
   - **Token:** `YOUR_GITHUB_PAT` (your Personal Access Token)
5. **Save**

**This should provide the right authentication for GitHub REST API calls.**

---

## ⚠️ IF "GitHub API" DOESN'T WORK

**Fallback: Use "Header Auth" (Generic)**

If "GitHub API" credential type doesn't work or isn't available:

1. **Go to:** Credentials → Add Credential
2. **Search for:** "Header Auth" (or "HTTP Header Auth")
3. **Select:** "Header Auth"
4. **Fill in:**
   - **Credential Name:** `github-actions-token`
   - **Header Name:** `Authorization`
   - **Header Value:** `token YOUR_GITHUB_PAT`
5. **Save**

**This is what the workflow JSON shows it expects (`httpHeaderAuth`).**

---

## 🎯 RECOMMENDED APPROACH

**Try in this order:**

1. **First:** Try "GitHub API" credential type
   - If it works, use it!
   - It's specifically designed for GitHub

2. **If that doesn't work:** Use "Header Auth"
   - More generic but works with any HTTP API
   - This is what the workflow JSON expects

---

## 📋 WHAT THE WORKFLOW NEEDS

**The workflow makes these calls:**
- `POST https://api.github.com/repos/rashadwest/BTEBallCODE/dispatches`
- `GET https://api.github.com/repos/rashadwest/BTEBallCODE/actions/workflows/...`

**These need:**
- `Authorization: token YOUR_GITHUB_PAT` header
- Either "GitHub API" or "Header Auth" can provide this

---

## ✅ SUMMARY

**Use:** "GitHub API" (if available)  
**Or:** "Header Auth" (if GitHub API doesn't work)  
**NOT:** "Git" (that's for git commands, not API calls)

**The "Git" option you're seeing is for git operations, not GitHub API calls!**

---

**Try "GitHub API" first, then "Header Auth" if needed!** ✅

