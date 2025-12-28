# ✅ Configure Custom API Call for Vision Analysis

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 16, 2025  
**Node Version:** `typeVersion: 1` (older version)  
**Solution:** Configure "Custom API Call" to use `/v1/chat/completions` endpoint

---

## 🎯 WHY "CUSTOM API CALL" IS CORRECT

**Your workflow file shows:**
- `"typeVersion": 1` - Older OpenAI node version
- `"operation": "create"` - This maps to "Custom API Call" in older versions
- `"resource": "chat"` - For chat completions

**In typeVersion 1:**
- "Complete" = `/v1/completions` (legacy, wrong for chat models)
- "Custom API Call" = Direct API access (can use `/v1/chat/completions`)

**So "Custom API Call" is the right choice!** We just need to configure it properly.

---

## ✅ STEP-BY-STEP CONFIGURATION

### Step 1: Keep "Custom API Call" Selected

- **Operation:** Keep as "Custom API Call" ✅
- **Resource:** Keep as "Chat" ✅

---

### Step 2: Configure the Custom API Call

**After selecting "Custom API Call", you should see additional configuration fields:**

#### **Endpoint/Method:**
- **Method:** `POST`
- **Endpoint:** `/v1/chat/completions` (or just `chat/completions`)

#### **Body Configuration:**

**You need to configure the request body. Look for a "Body" or "Request Body" section.**

**Use Expression mode or JSON mode, and enter:**

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
            "url": "={{ $json.screenshotUrl || 'data:image/png;base64,' + $json.screenshotFile?.data }}"
          }
        }
      ]
    }
  ]
}
```

---

### Step 3: Configure Authentication

**The node should automatically use your OpenAI credentials, but verify:**
- **Credential:** "OpenAI account" is selected ✅
- The API key should be automatically included in the Authorization header

---

### Step 4: Headers (if needed)

**If there's a Headers section, ensure:**
- `Content-Type: application/json`

---

## 🔍 WHAT TO LOOK FOR IN THE UI

**After selecting "Custom API Call", you should see fields like:**

1. **Endpoint/Path** - Enter: `chat/completions` or `/v1/chat/completions`
2. **Method** - Should be `POST`
3. **Body** - Enter the JSON above
4. **Headers** - Should auto-populate with Content-Type
5. **Authentication** - Should use your OpenAI credential

---

## 📝 ALTERNATIVE: If UI Doesn't Show These Fields

**If the "Custom API Call" option doesn't show body/endpoint fields:**

1. **Check if there's a "Settings" tab** - Configuration might be there
2. **Look for "Additional Fields" or "Options"** - Might be collapsed
3. **Check node version** - You might need to update the node

**To update node:**
- Click on the node
- Look for "Update available" or version indicator
- Update to latest version (might give you "Create Message" option)

---

## 🧪 TEST CONFIGURATION

**After configuring:**

1. **Click "Execute step"** in the node
2. **Check the OUTPUT panel** - Should show:
   ```json
   {
     "choices": [
       {
         "message": {
           "content": "{...diagnosis JSON...}"
         }
       }
     ]
   }
   ```

3. **If it works:** The "Parse Diagnosis" node should be able to extract the diagnosis

---

## ✅ VERIFICATION

**The node is correctly configured when:**
- ✅ Operation: "Custom API Call"
- ✅ Resource: "Chat"
- ✅ Endpoint: `/v1/chat/completions` or `chat/completions`
- ✅ Body: Contains model, messages with image_url
- ✅ Authentication: Uses OpenAI credential
- ✅ Test execution returns chat completion response

---

## 🎯 WHY THIS WORKS

**"Custom API Call" in typeVersion 1:**
- Allows direct API access to OpenAI
- Can use any endpoint (including `/v1/chat/completions`)
- Gives full control over request structure
- Works with vision models (gpt-4o) when configured correctly

**This is why the workflow was configured with `"operation": "create"`** - it maps to "Custom API Call" in older node versions, which is the correct way to use chat completions with vision.

---

**Version:** 1.0  
**Created:** December 16, 2025  
**Status:** ✅ This is the correct configuration approach



