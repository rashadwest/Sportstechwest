# 🔧 Fix Vision Analysis Node - Using Custom API Call

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 16, 2025  
**Issue:** Only "Complete" and "Custom API Call" options available  
**Solution:** Configure "Custom API Call" for chat completions with vision

---

## 🎯 THE PROBLEM

**Available Options:**
- ❌ "Complete" - Uses `/v1/completions` (legacy, doesn't work with chat models)
- ✅ "Custom API Call" - Manual configuration (can work with chat models)

**Why "Complete" doesn't work:**
- It's for legacy models like `text-davinci-003`
- Chat models (gpt-4, gpt-4o) need `/v1/chat/completions` endpoint
- That's why you get: "This is not a chat model and thus not supported in the v1/chat/completions endpoint"

---

## ✅ SOLUTION: Configure Custom API Call

### Step 1: Set Operation to "Custom API Call"

1. **Operation:** Select "Custom API Call"
2. **Resource:** Keep as "Chat" ✅

---

### Step 2: Configure Custom API Call

**After selecting "Custom API Call", you should see additional fields:**

#### **Endpoint:**
```
POST /v1/chat/completions
```

#### **Method:**
```
POST
```

#### **Body (JSON):**
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

## 🔄 ALTERNATIVE: Use HTTP Request Node Instead

If "Custom API Call" is too complex, **replace the OpenAI node with an HTTP Request node**:

### Step 1: Delete Current OpenAI Node
- Delete "Vision Analysis (GPT-4 Vision)" node

### Step 2: Add HTTP Request Node

**Configuration:**

**Method:** `POST`

**URL:**
```
https://api.openai.com/v1/chat/completions
```

**Authentication:**
- Type: `Header Auth`
- Name: `Authorization`
- Value: `Bearer {{ $credentials.openAiApi.apiKey }}`

**Headers:**
- `Content-Type`: `application/json`

**Body (JSON):**
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

## 📝 CHECK YOUR N8N VERSION

**If you only have "Complete" and "Custom API Call":**
- Your n8n version might be older
- Or the OpenAI node version is outdated

**Check n8n version:**
- Look at bottom of n8n UI
- Or check: `http://192.168.1.226:5678/healthz`

**If version is < 1.0:**
- Consider updating n8n
- Or use HTTP Request node workaround above

---

## ✅ RECOMMENDED APPROACH

**For simplicity, use HTTP Request node:**
1. ✅ More control
2. ✅ Works with any n8n version
3. ✅ Easier to debug
4. ✅ Direct API access

**Steps:**
1. Delete OpenAI node
2. Add HTTP Request node
3. Configure as shown above
4. Connect to "Parse Diagnosis" node
5. Test

---

## 🧪 TEST AFTER FIXING

```bash
curl -X POST "http://192.168.1.226:5678/webhook-test/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl": "https://example.com/test.png", "context": "Test error"}'
```

---

**Version:** 1.0  
**Created:** December 16, 2025  
**Status:** ✅ Ready to Use


