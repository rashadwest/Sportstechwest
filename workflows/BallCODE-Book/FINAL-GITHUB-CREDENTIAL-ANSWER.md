# Final Answer: Which GitHub Credential Type?

**Date:** December 18, 2025  
**Question:** I see "Git", "GitHub API", etc. - which one?

---

## 🎯 THE ANSWER

**The workflow expects: "Header Auth"**

**But if you only see these options:**
- Git
- GitHub API
- GitHub OAuth2 API
- GitLab API
- GitLab OAuth2 API

**Try this order:**

### **Option 1: Look for "Header Auth" (Best)**

**In n8n credential types, search for:**
- "Header Auth"
- "HTTP Header Auth"
- "Bearer Auth"
- "Custom Auth"

**If you find it:**
- Use "Header Auth"
- Name: `github-actions-token`
- Header Name: `Authorization`
- Header Value: `token YOUR_GITHUB_PAT`

---

### **Option 2: Try "GitHub API" (If Header Auth Not Available)**

**If "Header Auth" isn't in the list, try "GitHub API":**

1. **Select:** "GitHub API"
2. **Fill in:**
   - Name: `github-actions-token`
   - Token: `YOUR_GITHUB_PAT`
3. **Test:** See if it works

**"GitHub API" might provide header auth automatically.**

---

### **Option 3: Use "Git" (Last Resort - May Not Work)**

**If nothing else works:**

1. **Select:** "Git"
2. **Fill in:**
   - Username: `rashadwest` (your GitHub username)
   - Password: `YOUR_GITHUB_PAT` (use token as password)
3. **Test:** May work for some operations

**⚠️ Warning:** "Git" is for git commands, not API calls. This might not work for triggering GitHub Actions.

---

## 🔍 WHAT THE WORKFLOW ACTUALLY NEEDS

**The workflow makes HTTP requests to:**
- `https://api.github.com/repos/rashadwest/BTEBallCODE/dispatches`
- `https://api.github.com/repos/rashadwest/BTEBallCODE/actions/workflows/...`

**These need:**
- HTTP Header: `Authorization: token YOUR_GITHUB_PAT`
- This is what "Header Auth" provides

---

## ✅ RECOMMENDED APPROACH

1. **First:** Search for "Header Auth" in credential types
   - If found → Use it (this is what workflow expects)

2. **Second:** Try "GitHub API"
   - If Header Auth not available
   - May work if it provides header auth

3. **Third:** Check if workflow works
   - Test the workflow
   - If it fails, try different credential type

---

## 📋 QUICK REFERENCE

**Best:** "Header Auth" (or "HTTP Header Auth")  
**Alternative:** "GitHub API" (if Header Auth not available)  
**Not ideal:** "Git" (for git commands, not API calls)

**The workflow JSON shows it expects `httpHeaderAuth` type.**

---

**Try "Header Auth" first, then "GitHub API" if needed!** ✅

