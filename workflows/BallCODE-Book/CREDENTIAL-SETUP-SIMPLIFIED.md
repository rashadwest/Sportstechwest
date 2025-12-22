# Credential Setup - Simplified Guide

**Date:** December 18, 2025  
**Status:** Waiting for developer, but let's get credentials ready

---

## 🎯 THE SIMPLE ANSWER

**You have credentials, but we need to verify they're named correctly.**

---

## ✅ WHAT YOU HAVE

1. **"GitHub account"** (GitHub API type)
   - User: `rashadwest` ✅
   - Access Token: Set ✅
   - **Need to check:** Is the credential ID `github-actions-token`?

2. **"Netlify account"** (Netlify API type)
   - Token: Set ✅
   - **Need to check:** Is the credential ID `netlify-api-token`?

3. **"Header Auth account"** (Header Auth type)
   - **Need to check:** What's its ID? What's configured?

---

## 🔍 EASIEST WAY TO CHECK

**Open the workflow in n8n:**

1. **Go to:** Workflows → Unity Build Orchestrator
2. **Click on:** "Dispatch GitHub Build" node
3. **Look at:** Credentials dropdown/field
4. **See:** What credentials are listed

**If you see:**
- ✅ `github-actions-token` in the list → Good!
- ❌ Only "GitHub account" → Need to rename or create new

**Same for Netlify node.**

---

## ✅ IF CREDENTIALS DON'T MATCH

**Option 1: Rename (if possible)**
- Edit "GitHub account"
- Change its name/ID to: `github-actions-token`
- Save

**Option 2: Create New (Recommended)**
- Create new "Header Auth" credential
- Name: `github-actions-token`
- Header Name: `Authorization`
- Header Value: `token YOUR_GITHUB_PAT`
- Save

**Do same for Netlify:**
- Create "Header Auth" credential
- Name: `netlify-api-token`
- Header Name: `Authorization`
- Header Value: `Bearer YOUR_NETLIFY_TOKEN`

---

## 🎯 WHY "HEADER AUTH" IS BETTER

**"Header Auth" type:**
- ✅ What the workflow expects (`httpHeaderAuth`)
- ✅ More flexible
- ✅ Works with any HTTP API
- ✅ Explicit control over headers

**"GitHub API" type:**
- ⚠️ Might work, but workflow expects `httpHeaderAuth`
- ⚠️ Less control
- ⚠️ May not be compatible

---

## 📋 RECOMMENDED: Create Header Auth Credentials

**While waiting for developer:**

1. **Create GitHub credential:**
   - Type: "Header Auth"
   - Name: `github-actions-token`
   - Header Name: `Authorization`
   - Header Value: `token YOUR_GITHUB_PAT`

2. **Create Netlify credential:**
   - Type: "Header Auth"
   - Name: `netlify-api-token`
   - Header Name: `Authorization`
   - Header Value: `Bearer YOUR_NETLIFY_TOKEN`

**This matches what the workflow expects exactly!**

---

## 🧪 TEST AFTER SETUP

```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test credentials", "branch": "main"}'
```

**Check execution - should succeed if credentials are correct!**

---

**Create "Header Auth" credentials with correct names - that's the safest approach!** ✅

