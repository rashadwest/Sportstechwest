# ⚡ Quick Setup: HTTP Request Nodes - Get Running in 1 Hour

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 16, 2025 (Launch Day)  
**Goal:** Get both HTTP Request nodes working in 1 hour  
**Nodes:** Vision Analysis + Generate Fix

---

## 🎯 THE TWO NODES

1. **Vision Analysis (HTTP Request)** - Analyzes screenshots
2. **Generate Fix (HTTP Request)** - Generates code fixes

---

## ⚡ STEP 1: Create OpenAI API Key Credential (5 minutes)

### **In n8n UI:**

1. Go to **Credentials** (left sidebar)
2. Click **"Add Credential"**
3. Search for: **"HTTP Header Auth"**
4. Click **"HTTP Header Auth"**

### **Configure:**

**Name:** `OpenAI API Key`

**Header Name:** `Authorization`

**Header Value:** `Bearer sk-your-api-key-here`

**How to get your API key:**
- Go to: https://platform.openai.com/api-keys
- Click **"Create new secret key"**
- Copy the key (starts with `sk-`)
- Paste it after `Bearer ` in Header Value

**Example:**
```
Header Name: Authorization
Header Value: Bearer sk-proj-abc123xyz789...
```

**Click "Save"**

---

## ⚡ STEP 2: Configure Vision Analysis Node (10 minutes)

### **Node Settings:**

**Node Name:** `Vision Analysis (HTTP Request)`

**Method:** `POST`

**URL:** 
```
https://api.openai.com/v1/chat/completions
```

**Authentication:**
- Click **"Credential to connect with"**
- Select: **"OpenAI API Key"** (the one you just created)

**Body Content Type:** `JSON`

**Specify Body:** `Using JSON`

**JSON Body:**
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

**Headers:**
- Click **"Add Header"**
- **Name:** `Content-Type`
- **Value:** `application/json`

**Click "Save"**

---

## ⚡ STEP 3: Configure Generate Fix Node (10 minutes)

### **Node Settings:**

**Node Name:** `Generate Fix (HTTP Request)`

**Method:** `POST`

**URL:**
```
https://api.openai.com/v1/chat/completions
```

**Authentication:**
- Click **"Credential to connect with"**
- Select: **"OpenAI API Key"** (same one as above)

**Body Content Type:** `JSON`

**Specify Body:** `Using JSON`

**JSON Body:**
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
      "content": "Generate fix for this error:\n\nError Type: {{ $json.diagnosis.errorType }}\nError Message: {{ $json.diagnosis.errorMessage }}\nAffected System: {{ $json.diagnosis.affectedSystem }}\nLikely Cause: {{ $json.diagnosis.likelyCause }}\nFiles to Fix: {{ JSON.stringify($json.diagnosis.filesToFix) }}\n\nGenerate the exact fix needed. For n8n workflow errors, provide corrected JSON node configuration. For code errors, provide corrected code.\n\nReturn JSON:\n{\n  \"fixType\": \"workflow_json|code_file|config_file\",\n  \"filePath\": \"path/to/file\",\n  \"originalCode\": \"...\",\n  \"fixedCode\": \"...\",\n  \"explanation\": \"Why this fix works\",\n  \"validation\": \"How to verify the fix\"\n}"
    }
  ]
}
```

**Headers:**
- Click **"Add Header"**
- **Name:** `Content-Type`
- **Value:** `application/json`

**Click "Save"**

---

## ⚡ STEP 4: Verify Node Connections (2 minutes)

### **Check Flow:**

1. **Screenshot Upload Webhook** → **Normalize Screenshot Input**
2. **Normalize Screenshot Input** → **Prepare Image for API**
3. **Prepare Image for API** → **Vision Analysis (HTTP Request)** ✅
4. **Vision Analysis (HTTP Request)** → **Parse Diagnosis**
5. **Parse Diagnosis** → **Can Auto-Fix?**
6. **Can Auto-Fix?** → **Generate Fix (HTTP Request)** ✅
7. **Generate Fix (HTTP Request)** → **Parse Fix**

**If connections are missing:**
- Click and drag from output of one node to input of next node

---

## ⚡ STEP 5: Test Vision Analysis Node (5 minutes)

### **Test with Sample Data:**

1. Click on **"Vision Analysis (HTTP Request)"** node
2. Click **"Execute Node"** (or "Test step")
3. **Input Data** (paste this in test input):
```json
{
  "context": "Build failed with error",
  "imageUrlForAPI": "https://via.placeholder.com/800x600.png?text=Error+Screenshot"
}
```

4. Click **"Execute"**
5. **Expected Result:**
   - Status: `200 OK`
   - Response should have `choices[0].message.content` with diagnosis JSON

**If it fails:**
- Check API key is correct
- Verify URL is `https://api.openai.com/v1/chat/completions`
- Check headers include `Content-Type: application/json`

---

## ⚡ STEP 6: Test Generate Fix Node (5 minutes)

### **Test with Sample Data:**

1. Click on **"Generate Fix (HTTP Request)"** node
2. Click **"Execute Node"**
3. **Input Data** (paste this in test input):
```json
{
  "diagnosis": {
    "errorType": "n8n_workflow",
    "errorMessage": "Could not find property option",
    "affectedSystem": "n8n workflow import",
    "likelyCause": "Empty options object in node",
    "filesToFix": ["workflow.json"],
    "severity": "high",
    "canAutoFix": true,
    "fixComplexity": "simple"
  }
}
```

4. Click **"Execute"**
5. **Expected Result:**
   - Status: `200 OK`
   - Response should have `choices[0].message.content` with fix JSON

**If it fails:**
- Check API key is correct
- Verify URL is `https://api.openai.com/v1/chat/completions`
- Check JSON body format is correct

---

## ⚡ STEP 7: Test Full Workflow (10 minutes)

### **Test Webhook:**

```bash
curl -X POST http://192.168.1.226:5678/webhook-test/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://via.placeholder.com/800x600.png?text=Test+Error",
    "context": "Test error screenshot"
  }'
```

### **Expected Flow:**

1. ✅ Webhook receives request
2. ✅ Normalize Screenshot Input processes it
3. ✅ Prepare Image for API formats image
4. ✅ Vision Analysis calls OpenAI API
5. ✅ Parse Diagnosis extracts diagnosis
6. ✅ Can Auto-Fix? checks if fixable
7. ✅ Generate Fix calls OpenAI API (if fixable)
8. ✅ Parse Fix extracts fix
9. ✅ Webhook Response returns result

---

## 🐛 TROUBLESHOOTING

### **Error: "401 Unauthorized"**

**Problem:** API key is wrong or missing

**Fix:**
1. Check credential "OpenAI API Key" exists
2. Verify Header Value is: `Bearer sk-...` (with space after Bearer)
3. Test API key at: https://platform.openai.com/api-keys
4. Make sure key has proper permissions

---

### **Error: "400 Bad Request"**

**Problem:** JSON body format is wrong

**Fix:**
1. Check JSON is valid (use JSON validator)
2. Verify all `{{ }}` expressions are correct
3. Make sure `imageUrlForAPI` exists in input data
4. Check model name is correct (`gpt-4o` for vision, `gpt-4` for fix)

---

### **Error: "Image URL not accessible"**

**Problem:** Image URL is not publicly accessible or base64 is malformed

**Fix:**
1. For URLs: Test URL in browser first
2. For base64: Check "Prepare Image for API" node output
3. Verify image format is supported (PNG, JPG, etc.)
4. Try using a test image URL: `https://via.placeholder.com/800x600.png`

---

### **Error: "Failed to parse diagnosis"**

**Problem:** OpenAI response format changed or parsing logic is wrong

**Fix:**
1. Check "Parse Diagnosis" node code
2. Look at actual response from Vision Analysis node
3. Verify response has `choices[0].message.content`
4. Check if JSON is wrapped in markdown code blocks

---

## ✅ QUICK CHECKLIST

**Before Testing:**
- [ ] OpenAI API key credential created
- [ ] Vision Analysis node configured
- [ ] Generate Fix node configured
- [ ] Both nodes have credentials set
- [ ] Headers include `Content-Type: application/json`
- [ ] Node connections are correct

**After Testing:**
- [ ] Vision Analysis returns 200 OK
- [ ] Generate Fix returns 200 OK
- [ ] Parse Diagnosis extracts JSON correctly
- [ ] Parse Fix extracts JSON correctly
- [ ] Full workflow test succeeds

---

## 📋 COPY-PASTE CONFIGURATIONS

### **Vision Analysis - Complete JSON Body:**

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

### **Generate Fix - Complete JSON Body:**

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
      "content": "Generate fix for this error:\n\nError Type: {{ $json.diagnosis.errorType }}\nError Message: {{ $json.diagnosis.errorMessage }}\nAffected System: {{ $json.diagnosis.affectedSystem }}\nLikely Cause: {{ $json.diagnosis.likelyCause }}\nFiles to Fix: {{ JSON.stringify($json.diagnosis.filesToFix) }}\n\nGenerate the exact fix needed. For n8n workflow errors, provide corrected JSON node configuration. For code errors, provide corrected code.\n\nReturn JSON:\n{\n  \"fixType\": \"workflow_json|code_file|config_file\",\n  \"filePath\": \"path/to/file\",\n  \"originalCode\": \"...\",\n  \"fixedCode\": \"...\",\n  \"explanation\": \"Why this fix works\",\n  \"validation\": \"How to verify the fix\"\n}"
    }
  ]
}
```

---

## 🎯 SUCCESS CRITERIA

**You're done when:**
- ✅ Both nodes return 200 OK status
- ✅ Vision Analysis returns diagnosis JSON
- ✅ Generate Fix returns fix JSON
- ✅ Full workflow test completes successfully
- ✅ Webhook responds with result

---

**Time Estimate:** 45-60 minutes  
**Status:** Ready to configure  
**Next:** Follow steps 1-7 in order

