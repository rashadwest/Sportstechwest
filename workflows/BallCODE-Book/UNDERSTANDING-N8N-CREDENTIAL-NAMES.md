# Understanding n8n Credential Names

**Date:** December 18, 2025  
**Clarification:** How credential names work in n8n

---

## 🔍 HOW N8N CREDENTIALS WORK

**In n8n, credentials have:**
1. **Display Name** - What you see in the list (e.g., "GitHub account")
2. **Internal ID** - What workflows reference (this is what matters!)

**The workflow looks for credentials by their ID/name, not display name.**

---

## ✅ YOUR CURRENT SETUP

### **"GitHub account" (GitHub API type):**
- **Display Name:** "GitHub account"
- **Fields:** User: `rashadwest`, Access Token: `YOUR_PAT`
- **Question:** What is its internal ID/name?

### **"Netlify account" (Netlify API type):**
- **Display Name:** "Netlify account"
- **Fields:** Token: `YOUR_TOKEN`
- **Question:** What is its internal ID/name?

### **"Header Auth account" (Header Auth type):**
- **Display Name:** "Header Auth account"
- **Fields:** (You mentioned no header section visible - might need to check)
- **Question:** What is its internal ID/name?

---

## 🎯 WHAT THE WORKFLOW NEEDS

**The workflow JSON references:**
```json
"credentials": {
  "httpHeaderAuth": {
    "id": "github-actions-token",  ← This is the ID it looks for
    "name": "GitHub Actions Token"
  }
}
```

**So the credential must have ID: `github-actions-token`**

---

## 🔍 HOW TO CHECK CREDENTIAL ID/NAME

**In n8n UI:**

1. **Go to:** Credentials
2. **Click on:** "GitHub account"
3. **Look for:**
   - A field labeled "Name" or "Credential Name"
   - Or check the URL - it might show the ID
   - Or look in the credential details

**The ID/name is usually:**
- The same as the display name (if you didn't change it)
- Or a separate field when creating/editing

---

## ⚠️ POTENTIAL ISSUE

**"GitHub API" credential type:**
- Might work if n8n can map it to `httpHeaderAuth`
- But the workflow specifically looks for `httpHeaderAuth` type
- If "GitHub API" doesn't provide header auth, it won't work

**"Header Auth" credential type:**
- This is what the workflow expects
- But needs to be named `github-actions-token`

---

## ✅ SOLUTION

### **Option 1: Check if "GitHub API" Works**

**Test it:**
1. Make sure "GitHub account" has ID/name: `github-actions-token`
2. Test the workflow
3. If it works → Great!
4. If it fails → Use Option 2

### **Option 2: Create "Header Auth" Credentials (Recommended)**

**Since you already have "Header Auth account":**

1. **Edit "Header Auth account":**
   - Check its name/ID
   - If it's not `github-actions-token`, rename it
   - Configure:
     - Header Name: `Authorization`
     - Header Value: `token YOUR_GITHUB_PAT`

2. **For Netlify:**
   - Create new "Header Auth" credential
   - Name/ID: `netlify-api-token`
   - Header Name: `Authorization`
   - Header Value: `Bearer YOUR_NETLIFY_TOKEN`

---

## 📋 QUICK CHECKLIST

**To verify your setup:**

1. **Check credential IDs:**
   - "GitHub account" → ID should be `github-actions-token`
   - "Netlify account" → ID should be `netlify-api-token`

2. **If IDs don't match:**
   - Rename them in n8n
   - Or create new ones with correct IDs

3. **Test workflow:**
   - Run a test execution
   - Check if credentials are found

---

## 🧪 TEST COMMAND

**After checking/renaming credentials:**

```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test credentials", "branch": "main"}'
```

**Check execution in n8n:**
- If succeeds → Credentials are correct!
- If fails → Check error message for credential issues

---

**Check the credential ID/name in n8n - that's what the workflow uses!** ✅

