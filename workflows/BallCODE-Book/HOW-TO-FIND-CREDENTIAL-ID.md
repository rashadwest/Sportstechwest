# How to Find Credential ID/Name in n8n

**Date:** December 18, 2025  
**Purpose:** Find the internal ID that workflows use

---

## 🔍 WHERE TO FIND CREDENTIAL ID

### **Method 1: Edit Credential**

1. **Go to:** Credentials (left sidebar)
2. **Click on:** "GitHub account"
3. **Look for:**
   - Field labeled **"Name"** or **"Credential Name"**
   - This is the ID the workflow uses
   - Might be at the top of the form

### **Method 2: Check Workflow Node**

1. **Open:** Unity Build Orchestrator workflow
2. **Click on:** "Dispatch GitHub Build" node
3. **Go to:** Credentials section
4. **See:** What credential it's trying to use
5. **If it shows:** "github-actions-token" → That's what it needs
6. **If it shows:** "GitHub account" → Might work if that's the ID

### **Method 3: Check URL**

1. **When editing credential:**
2. **Look at browser URL:**
   - Might show: `/credentials/12345` or `/credentials/github-actions-token`
   - The ID might be in the URL

---

## ⚠️ IMPORTANT: Display Name vs ID

**In n8n:**
- **Display Name:** "GitHub account" (what you see in list)
- **Internal ID:** Could be "GitHub account" or something else

**The workflow uses the ID, not display name!**

---

## ✅ WHAT TO DO

**If credential ID is "GitHub account":**
- The workflow looks for `github-actions-token`
- They don't match → Workflow won't find it
- **Solution:** Rename credential ID to `github-actions-token`

**If credential ID is already `github-actions-token`:**
- Perfect! It should work
- Just make sure the token is set correctly

---

## 🎯 QUICK TEST

**Easiest way to check:**

1. **Open workflow in n8n**
2. **Click on:** "Dispatch GitHub Build" node
3. **Check:** Credentials dropdown
4. **See:** What credentials are available
5. **If:** "github-actions-token" is in the list → Good!
6. **If:** Only "GitHub account" is listed → Need to rename

---

**Check the workflow node to see what credentials it can find!** ✅

