# Quick Check: Credential Names

**Date:** December 18, 2025  
**Critical:** Workflow needs exact credential names

---

## 🎯 CRITICAL CHECK

**The workflow looks for credentials by exact name:**

### **GitHub Credential:**
- **Must be named:** `github-actions-token`
- **Your credential:** "GitHub account"
- **Action:** Check if you can rename it, or verify the workflow can find it

### **Netlify Credential:**
- **Must be named:** `netlify-api-token`
- **Your credential:** "Netlify account"
- **Action:** Check if you can rename it, or verify the workflow can find it

---

## 🔍 HOW TO CHECK

**In n8n UI:**

1. **Go to:** Credentials
2. **Click on:** "GitHub account"
3. **Check:** What is the exact name? (might be different from display name)
4. **Check:** Can you edit/rename it?

**Same for Netlify account.**

---

## ✅ IF NAMES DON'T MATCH

**Option 1: Rename (if possible)**
- Edit credential
- Change name to match exactly
- Save

**Option 2: Create New**
- Create new credential with correct name
- Use correct type ("Header Auth" for both)
- Delete old one if not needed

---

## 🧪 TEST

**After fixing names, test:**

```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test credential names", "branch": "main"}'
```

**Check execution in n8n:**
- If it succeeds → Names are correct!
- If it fails with "credential not found" → Names don't match

---

**Check the credential names in n8n UI!** ✅


