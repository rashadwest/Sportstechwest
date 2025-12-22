# 🔧 n8n OpenAI Node Fix - 404 Error

**Date:** December 6, 2025  
**Issue:** OpenAI node returning 404 "resource not found" error  
**Status:** ✅ FIXED

---

## 🎯 **THE PROBLEM**

**Error Message:**
```
The resource you are requesting could not be found.
This is a chat model and not supported in the v1/completions endpoint. 
Did you mean to use v1/chat/completions?
```

**Root Cause:**
- The OpenAI node was using **"Complete" operation** (old `/v1/completions` endpoint)
- But `gpt-4` is a **chat model** that requires `/v1/chat/completions` endpoint
- The node configuration didn't explicitly specify the resource/operation type

---

## ✅ **THE FIX**

Updated the workflow JSON to explicitly use the **Chat** resource:

**Changed:**
```json
{
  "parameters": {
    "model": "gpt-4",
    "options": { ... },
    "messages": { ... }
  }
}
```

**To:**
```json
{
  "parameters": {
    "resource": "chat",           // ← ADDED: Explicitly use chat resource
    "operation": "create",         // ← ADDED: Use create operation for chat
    "model": "gpt-4",
    "options": { ... },
    "messages": { ... }
  }
}
```

---

## 📋 **HOW TO APPLY THE FIX IN n8n UI**

If you need to fix it manually in the n8n interface:

### **Step 1: Open the "AI Analyze Request" Node**

1. Open your n8n workflow
2. Click on the **"AI Analyze Request"** node

### **Step 2: Change Resource and Operation**

1. **Resource:** Change from `Text` to `Chat`
2. **Operation:** Change from `Complete` to `Create` (or `Generate a Chat Completion`)

### **Step 3: Verify Model**

- **Model:** Should remain `gpt-4` (or `gpt-4-turbo`)

### **Step 4: Verify Messages**

- The messages structure should remain the same:
  - System message
  - User message with variables

### **Step 5: Save and Test**

1. Click **"Save"** in n8n
2. Click **"Execute Workflow"** to test
3. The error should be resolved

---

## 🔍 **VERIFICATION**

After applying the fix:

1. **Execute the workflow manually**
2. **Check the "AI Analyze Request" node output:**
   - Should show successful response
   - Should contain JSON action plan
   - No 404 errors

3. **Check the "Parse AI Response" node:**
   - Should successfully parse the AI response
   - Should extract action plan JSON

---

## 📝 **ALTERNATIVE: Update Node Version**

If the fix above doesn't work, you may need to:

1. **Update the OpenAI node:**
   - The warning says: "New node version available: get the latest version"
   - Click the node → Check for updates
   - Update to latest version (1.1 or higher)

2. **Reconfigure after update:**
   - Set Resource: `Chat`
   - Set Operation: `Create` or `Generate a Chat Completion`
   - Model: `gpt-4`
   - Messages: Keep your existing messages

---

## 🎯 **WHY THIS HAPPENED**

- **Old API:** `/v1/completions` - for text completion models (deprecated)
- **New API:** `/v1/chat/completions` - for chat models (GPT-4, GPT-3.5-turbo)
- **GPT-4** is a chat model, so it requires the chat/completions endpoint
- The n8n node defaulted to "Complete" operation, which uses the old endpoint

---

## ✅ **STATUS**

- ✅ Workflow JSON updated with correct resource/operation
- ✅ Ready to import into n8n
- ✅ Should resolve 404 error

**Next Step:** Import the updated workflow JSON into n8n, or manually update the node settings as described above.



