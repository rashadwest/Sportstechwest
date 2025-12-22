# 🔧 Fix: "you must provide a model parameter" Error

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Error:** `"you must provide a model parameter"`  
**Cause:** Send Body is OFF + No Authentication  
**Fix Time:** 5 minutes

---

## 🎯 THE PROBLEM

Looking at your HTTP Request node:
- ❌ **Send Body:** OFF (this is why model parameter is missing)
- ❌ **Authentication:** None (OpenAI requires API key)
- ❌ **Send Headers:** OFF (needed for authentication)

---

## ✅ QUICK FIX (5 MINUTES)

### **Step 1: Turn ON Send Body (1 minute)**

1. In your HTTP Request node, find **"Send Body"**
2. **Toggle it ON** (switch should turn blue/orange)
3. **Body Content Type:** Select `JSON`
4. **Specify Body:** Select `Using JSON`

### **Step 2: Add JSON Body (2 minutes)**

Click in the **JSON Body** field and paste this:

```json
{
  "model": "gpt-4o",
  "temperature": 0.1,
  "max_tokens": 2000,
  "messages": [
    {
      "role": "system",
      "content": "You are an expert error diagnosis system. Analyze screenshots of errors and provide structured diagnosis."
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Analyze this error screenshot and provide structured diagnosis:\n\nContext: {{ $json.context }}\n\nIdentify:\n1. Error type (n8n_workflow, unity_build, deployment, web_error, other)\n2. Exact error message\n3. Affected system/component\n4. Likely cause\n5. Files/components that need fixing\n6. Severity (low, medium, high, critical)\n\nReturn JSON only:\n{\n  \"errorType\": \"string\",\n  \"errorMessage\": \"string\",\n  \"affectedSystem\": \"string\",\n  \"likelyCause\": \"string\",\n  \"filesToFix\": [\"array\", \"of\", \"files\"],\n  \"severity\": \"low|medium|high|critical\",\n  \"canAutoFix\": true/false,\n  \"fixComplexity\": \"simple|moderate|complex\"\n}"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "={{ $json.imageUrlForAPI }}"
          }
        }
      ]
    }
  ]
}
```

**Important:** This includes the `"model": "gpt-4o"` parameter that OpenAI requires!

---

### **Step 3: Set Up Authentication (2 minutes)**

#### **A. Create Credential (if you don't have it):**

1. Click **"Credential to connect with"** dropdown
2. Click **"Create New"** or **"+"** button
3. Search for: **"HTTP Header Auth"**
4. Click it

#### **B. Configure Credential:**

**Name:** `OpenAI API Key`

**Header Name:** `Authorization`

**Header Value:** `Bearer sk-your-api-key-here`

**How to get API key:**
- Go to: https://platform.openai.com/api-keys
- Click **"Create new secret key"**
- Copy the key (starts with `sk-`)
- Paste it after `Bearer ` (note the space!)

**Example:**
```
Header Name: Authorization
Header Value: Bearer sk-proj-abc123xyz789...
```

**Click "Save"**

#### **C. Select Credential in Node:**

1. Back in your HTTP Request node
2. Click **"Authentication"** dropdown
3. Select: **"HTTP Header Auth"**
4. Click **"Credential to connect with"**
5. Select: **"OpenAI API Key"** (the one you just created)

---

### **Step 4: Turn ON Send Headers (30 seconds)**

1. Find **"Send Headers"** toggle
2. **Turn it ON** (switch should turn blue/orange)
3. This ensures the Authorization header is sent

**OR** add header manually:
1. Click **"Options"** → **"Add option"** → **"Headers"**
2. Click **"Add Header"**
3. **Name:** `Content-Type`
4. **Value:** `application/json`

---

## ✅ VERIFICATION CHECKLIST

After making these changes, verify:

- [ ] **Send Body:** ON (blue/orange)
- [ ] **Body Content Type:** JSON
- [ ] **Specify Body:** Using JSON
- [ ] **JSON Body:** Contains `"model": "gpt-4o"`
- [ ] **Authentication:** HTTP Header Auth
- [ ] **Credential:** OpenAI API Key (selected)
- [ ] **Send Headers:** ON (or Content-Type header added)

---

## 🧪 TEST IT

1. Click **"Execute step"** button (orange button top-right)
2. **Expected Result:** Status 200 OK with response containing `choices[0].message.content`

**If you still get an error:**
- Check API key is correct (test at https://platform.openai.com/api-keys)
- Verify Header Value is exactly: `Bearer sk-...` (with space after Bearer)
- Make sure JSON body is valid (no syntax errors)

---

## 📋 COMPLETE NODE CONFIGURATION SUMMARY

**Method:** POST  
**URL:** `https://api.openai.com/v1/chat/completions`  
**Authentication:** HTTP Header Auth → OpenAI API Key  
**Send Body:** ON  
**Body Content Type:** JSON  
**Specify Body:** Using JSON  
**JSON Body:** (paste the JSON above)  
**Send Headers:** ON (or add Content-Type header manually)

---

## 🐛 IF STILL NOT WORKING

### **Error: "401 Unauthorized"**
- API key is wrong or missing
- Check credential Header Value is: `Bearer sk-...`
- Verify API key works at https://platform.openai.com/api-keys

### **Error: "400 Bad Request"**
- JSON body has syntax error
- Check all quotes are correct
- Verify `{{ }}` expressions are valid
- Make sure `model` parameter is present

### **Error: "Image URL not accessible"**
- For Vision Analysis, image URL must be accessible
- Test URL in browser first
- Or use base64 encoded image

---

**Time to Fix:** 5 minutes  
**Status:** Ready to test  
**Next:** Execute the node and verify it works!

