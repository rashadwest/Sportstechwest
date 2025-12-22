# Netlify Credentials - Why They're "Ready" Without Manual Setup

**Date:** December 18, 2025  
**Question:** "I did not put the netlify credentials into any nodes but it is ready."

---

## ✅ HOW IT WORKS

**You don't need to manually add credentials to nodes!**

### **The Workflow JSON Already References Credentials**

**Looking at the Unity Build Orchestrator workflow (line 191-196):**

```json
"credentials": {
  "httpHeaderAuth": {
    "id": "netlify-api-token",
    "name": "Netlify API Token"
  }
}
```

**This means:**
- ✅ The workflow JSON **already specifies** which credential to use
- ✅ When you import the workflow, n8n looks for a credential with ID `netlify-api-token`
- ✅ If that credential exists → It's automatically used
- ✅ No manual node configuration needed!

---

## 🔍 WHERE IT'S USED

**The credential is used in the "Check Latest Netlify Deploy" node:**

1. **Node:** "Check Latest Netlify Deploy (AIMCODE L3)"
2. **Type:** HTTP Request
3. **URL:** `https://api.netlify.com/api/v1/sites/{{ $env.NETLIFY_SITE_ID }}/deploys`
4. **Authentication:** Uses credential `netlify-api-token` (from workflow JSON)

**When the workflow runs:**
- n8n finds the credential by ID: `netlify-api-token`
- Automatically adds the Authorization header
- Makes the API call to Netlify
- No manual setup needed!

---

## ✅ TO VERIFY IT'S WORKING

**Check in n8n UI:**

1. **Open:** Unity Build Orchestrator workflow
2. **Click:** "Check Latest Netlify Deploy" node
3. **Look at:** Authentication section
4. **Should show:** `netlify-api-token` (if credential exists)

**If it shows the credential:**
- ✅ It's configured correctly
- ✅ Will be used automatically
- ✅ No further action needed

**If it shows "No credential" or error:**
- ⚠️ Credential doesn't exist or wrong ID
- ⚠️ Create credential with ID: `netlify-api-token`

---

## 🎯 SUMMARY

**Why it's "ready":**
- ✅ Credential is referenced in workflow JSON
- ✅ n8n automatically finds and uses it
- ✅ No manual node configuration required

**What you need:**
- ✅ Credential with ID: `netlify-api-token`
- ✅ Type: Header Auth
- ✅ Header Name: `Authorization`
- ✅ Header Value: `Bearer YOUR_NETLIFY_TOKEN`

**That's it!** The workflow handles the rest automatically.

---

**The workflow is smart - it finds credentials automatically!** ✅

