# Credential Field Names - Clarified

**Date:** December 18, 2025  
**Purpose:** Clarify which field is which in n8n credentials

---

## 🔍 CREDENTIAL FIELD NAMES EXPLAINED

**When creating/editing a "Header Auth" credential in n8n:**

### **1. Name/ID Field:**
- **What it is:** The credential identifier that workflows reference
- **Example:** `github-actions-token`
- **This is what the workflow looks for!**
- **Location:** Usually at the top of the credential form

### **2. Header Name Field:**
- **What it is:** The HTTP header name to use
- **Example:** `Authorization`
- **This is the actual HTTP header name**

### **3. Header Value Field:**
- **What it is:** The value to put in that header
- **Example:** `token YOUR_GITHUB_PAT` or `Bearer YOUR_NETLIFY_TOKEN`
- **This is your actual token/secret**

---

## ✅ CORRECT SETUP

### **GitHub Credential (`github-actions-token`):**

```
Name/ID: github-actions-token  ← Workflow looks for this!
Header Name: Authorization     ← HTTP header name
Header Value: token YOUR_ACTUAL_GITHUB_PAT  ← Your token
```

### **Netlify Credential (`netlify-api-token`):**

```
Name/ID: netlify-api-token     ← Workflow looks for this!
Header Name: Authorization     ← HTTP header name
Header Value: Bearer YOUR_ACTUAL_NETLIFY_TOKEN  ← Your token
```

---

## ⚠️ WHAT YOU MIGHT HAVE DONE

**If you mixed them up:**
- Used "Header Name" for the credential ID → Workflow won't find it
- Used "Name/ID" for the header name → Wrong header will be sent

**But that's okay!** We'll test and see what works.

---

## 🧪 TESTING WILL REVEAL

**When we test:**
- If credentials are found → Name/ID is correct ✅
- If API calls succeed → Header Name/Value is correct ✅
- If errors occur → We'll know which field needs fixing

---

**Don't worry - testing will show us what works!** ✅


