# ✅ Screenshot-to-Fix Workflow - HTTP Request Version

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 16, 2025 (Launch Day)  
**Status:** ✅ Complete - All AI Nodes Replaced with HTTP Request Nodes  
**File:** `n8n-screenshot-to-fix-workflow-HTTP.json`

---

## 🎯 WHAT WAS CHANGED

**Problem:** Custom API selection in OpenAI nodes makes it impossible to edit anything  
**Solution:** Replaced all OpenAI AI nodes with HTTP Request nodes that call OpenAI API directly

### **Nodes Replaced:**

1. **"Vision Analysis (GPT-4 Vision)"** → **"Vision Analysis (HTTP Request)"**
   - Now uses HTTP Request to call `https://api.openai.com/v1/chat/completions`
   - Uses `gpt-4o` model for vision analysis
   - Handles image URLs and base64 encoded images

2. **"Generate Fix (GPT-4)"** → **"Generate Fix (HTTP Request)"**
   - Now uses HTTP Request to call `https://api.openai.com/v1/chat/completions`
   - Uses `gpt-4` model for fix generation
   - Fully editable JSON body

### **New Nodes Added:**

3. **"Prepare Image for API"** (Code Node)
   - Prepares image data for OpenAI Vision API
   - Handles both URLs and base64 encoded images
   - Formats data correctly for API consumption

---

## 📋 COMPLETE WORKFLOW STRUCTURE

### **Node Flow (18 nodes):**

1. **Screenshot Upload Webhook** - Receives POST requests
2. **Normalize Screenshot Input** - Processes input data
3. **Prepare Image for API** - Formats image for OpenAI API
4. **Vision Analysis (HTTP Request)** - Calls OpenAI Vision API
5. **Parse Diagnosis** - Extracts diagnosis from API response
6. **Can Auto-Fix?** - Conditional check
7. **Generate Fix (HTTP Request)** - Calls OpenAI API for fix generation
8. **Parse Fix** - Extracts fix from API response
9. **Apply Fix (Update Files)** - Executes fix processor script
10. **Commit & Push Fix** - Commits changes to git
11. **Trigger Build (GitHub Actions)** - Triggers GitHub Actions build
12. **Wait for Build (5 min)** - Waits for build to complete
13. **Verify Deployment** - Checks if deployment succeeded
14. **Compile Report** - Creates completion report
15. **Send Notification** - Sends notification webhook
16. **Webhook Response** - Returns response to caller
17. **Manual Fix Required** - Handles non-auto-fixable errors

---

## 🔧 CONFIGURATION DETAILS

### **1. Vision Analysis HTTP Request Node**

**URL:** `https://api.openai.com/v1/chat/completions`  
**Method:** POST  
**Authentication:** Header Auth (Bearer token)  
**Credential Name:** "OpenAI API Key"

**Request Body:**
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
          "text": "Analyze this error screenshot and provide structured diagnosis:\n\nContext: {context}\n\nIdentify:\n1. Error type (n8n_workflow, unity_build, deployment, web_error, other)\n2. Exact error message\n3. Affected system/component\n4. Likely cause\n5. Files/components that need fixing\n6. Severity (low, medium, high, critical)\n\nReturn JSON only:\n{\n  \"errorType\": \"string\",\n  \"errorMessage\": \"string\",\n  \"affectedSystem\": \"string\",\n  \"likelyCause\": \"string\",\n  \"filesToFix\": [\"array\", \"of\", \"files\"],\n  \"severity\": \"low|medium|high|critical\",\n  \"canAutoFix\": true/false,\n  \"fixComplexity\": \"simple|moderate|complex\"\n}"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "{imageUrlForAPI}"
          }
        }
      ]
    }
  ]
}
```

**Headers:**
- `Content-Type: application/json`
- `Authorization: Bearer {OPENAI_API_KEY}` (via credentials)

---

### **2. Generate Fix HTTP Request Node**

**URL:** `https://api.openai.com/v1/chat/completions`  
**Method:** POST  
**Authentication:** Header Auth (Bearer token)  
**Credential Name:** "OpenAI API Key"

**Request Body:**
```json
{
  "model": "gpt-4",
  "temperature": 0.2,
  "max_tokens": 3000,
  "messages": [
    {
      "role": "system",
      "content": "You are an expert code fix generator. Generate precise, validated fixes for errors."
    },
    {
      "role": "user",
      "content": "Generate fix for this error:\n\nError Type: {errorType}\nError Message: {errorMessage}\nAffected System: {affectedSystem}\nLikely Cause: {likelyCause}\nFiles to Fix: {filesToFix}\n\nGenerate the exact fix needed. For n8n workflow errors, provide corrected JSON node configuration. For code errors, provide corrected code.\n\nReturn JSON:\n{\n  \"fixType\": \"workflow_json|code_file|config_file\",\n  \"filePath\": \"path/to/file\",\n  \"originalCode\": \"...\",\n  \"fixedCode\": \"...\",\n  \"explanation\": \"Why this fix works\",\n  \"validation\": \"How to verify the fix\"\n}"
    }
  ]
}
```

**Headers:**
- `Content-Type: application/json`
- `Authorization: Bearer {OPENAI_API_KEY}` (via credentials)

---

## 🔑 CREDENTIALS REQUIRED

### **1. OpenAI API Key**

**Type:** HTTP Header Auth  
**Name:** "OpenAI API Key"  
**Header Name:** `Authorization`  
**Header Value:** `Bearer {YOUR_OPENAI_API_KEY}`

**How to Set:**
1. In n8n UI, go to **Credentials**
2. Create new credential: **HTTP Header Auth**
3. Name it: **"OpenAI API Key"**
4. Header Name: `Authorization`
5. Header Value: `Bearer sk-...` (your OpenAI API key)

---

## 📝 CODE NODES EXPLAINED

### **1. Normalize Screenshot Input**

Handles different input formats:
- File uploads (binary data)
- URLs (http/https)
- Base64 encoded images

Extracts:
- `screenshotUrl` - If it's a URL
- `screenshotBase64` - If it's base64 data
- `context` - Error context/description
- `source` - Where the screenshot came from

### **2. Prepare Image for API**

Formats image data for OpenAI Vision API:
- If URL: Uses it directly
- If base64: Formats as `data:image/png;base64,{data}`
- Handles edge cases and fallbacks

### **3. Parse Diagnosis**

Extracts diagnosis from OpenAI API response:
- Handles OpenAI response format: `response.choices[0].message.content`
- Extracts JSON from markdown code blocks if present
- Creates fallback diagnosis if parsing fails

### **4. Parse Fix**

Extracts fix from OpenAI API response:
- Handles OpenAI response format
- Extracts JSON from markdown code blocks
- Creates fallback fix structure if parsing fails

---

## 🚀 IMPORT INSTRUCTIONS

### **Step 1: Import Workflow**

1. Open n8n UI: `http://192.168.1.226:5678`
2. Click **"Workflows"** → **"Import from File"**
3. Select: `n8n-screenshot-to-fix-workflow-HTTP.json`
4. Click **"Import"**

### **Step 2: Configure Credentials**

1. Open the imported workflow
2. Click on **"Vision Analysis (HTTP Request)"** node
3. Click **"Credential to connect with"**
4. Select or create **"OpenAI API Key"** credential
5. Repeat for **"Generate Fix (HTTP Request)"** node

### **Step 3: Activate Workflow**

1. Toggle **"Active"** switch (top-right)
2. Verify it turns green/blue

### **Step 4: Test**

```bash
curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://example.com/error-screenshot.png",
    "context": "Build failed with error message"
  }'
```

---

## ✅ ADVANTAGES OF HTTP REQUEST VERSION

1. **Fully Editable** - All JSON body content is editable
2. **No UI Limitations** - No custom API selection issues
3. **Direct Control** - Full control over API calls
4. **Easy Debugging** - Can see exact request/response
5. **Version Independent** - Works with any n8n version
6. **Flexible** - Easy to modify prompts and parameters

---

## 🐛 TROUBLESHOOTING

### **Error: "401 Unauthorized"**
- Check OpenAI API key is correct
- Verify credential is set up properly
- Ensure API key has proper permissions

### **Error: "Image URL not accessible"**
- For URLs: Ensure image is publicly accessible
- For base64: Check encoding is correct
- Try using a different image format

### **Error: "Failed to parse diagnosis"**
- Check OpenAI API response format
- Verify JSON structure in response
- Check Code node parsing logic

---

## 📊 WORKFLOW COMPARISON

### **Old Version (OpenAI Nodes):**
- ❌ Custom API selection - can't edit
- ❌ Limited configuration options
- ❌ Version-dependent behavior

### **New Version (HTTP Request):**
- ✅ Fully editable JSON bodies
- ✅ Complete control over API calls
- ✅ Works with any n8n version
- ✅ Easy to debug and modify

---

**Status:** ✅ Ready for Import  
**All code and structure in place**  
**Fully functional and editable**

