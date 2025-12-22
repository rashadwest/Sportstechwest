# 🔐 Complete Credentials & Configuration Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 16, 2025  
**Purpose:** Step-by-step guide for all credentials and node configurations

---

## 1️⃣ CREDENTIALS NEEDED

### Required Credentials for All Workflows:

#### **OpenAI API** (Required for 2 workflows)
- **Used by:**
  - BallCODE Full Integration - AI Analyze Prompt node
  - Screenshot-to-Fix - Vision Analysis node
  - Screenshot-to-Fix - Generate Fix node
- **How to get:**
  1. Go to: https://platform.openai.com/api-keys
  2. Click "Create new secret key"
  3. Copy the key
- **How to add in n8n:**
  1. Settings → Credentials → Add Credential
  2. Type: **OpenAI API**
  3. API Key: Paste your key
  4. Save

#### **GitHub Actions Token** (Required for 2 workflows)
- **Used by:**
  - Unity Build Orchestrator - Dispatch GitHub Build node
  - Unity Build Orchestrator - Check Latest GitHub Run node
  - Screenshot-to-Fix - Trigger Build node
- **How to get:**
  1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
  2. Generate new token (classic)
  3. Scopes needed:
     - `repo` (full control of private repositories)
     - `workflow` (update GitHub Action workflows)
  4. Copy the token
- **How to add in n8n:**
  1. Settings → Credentials → Add Credential
  2. Type: **HTTP Header Auth**
  3. Name: `Authorization`
  4. Value: `Bearer YOUR_GITHUB_TOKEN` (replace YOUR_GITHUB_TOKEN)
  5. Save
  6. Name it: "GitHub Actions Token"

#### **Netlify API Token** (Required for 1 workflow)
- **Used by:**
  - Unity Build Orchestrator - Check Latest Netlify Deploy node
- **How to get:**
  1. Netlify → User settings → Applications → New access token
  2. Copy the token
- **How to add in n8n:**
  1. Settings → Credentials → Add Credential
  2. Type: **HTTP Header Auth**
  3. Name: `Authorization`
  4. Value: `Bearer YOUR_NETLIFY_TOKEN` (replace YOUR_NETLIFY_TOKEN)
  5. Save
  6. Name it: "Netlify API Token"

---

## 2️⃣ OPENAI NODE USER MESSAGE (Vision Analysis)

### For "Vision Analysis (GPT-4 Vision)" Node:

**The user message needs TWO parts:**

#### **Part 1: Text Content**
In the "Content" field, you need to add BOTH text AND image. Here's how:

1. Click the **"Add Message"** button (if you don't see a user message)
2. Set Role to **"User"**
3. In the Content field, you need to use **Expression mode** (click "Expression" button)

**Use this expression:**
```javascript
={{ [
  {
    type: "text",
    text: "Analyze this error screenshot and provide structured diagnosis:\n\nContext: " + $json.context + "\n\nIdentify:\n1. Error type (n8n_workflow, unity_build, deployment, web_error, other)\n2. Exact error message\n3. Affected system/component\n4. Likely cause\n5. Files/components that need fixing\n6. Severity (low, medium, high, critical)\n\nReturn JSON only:\n{\n  \"errorType\": \"string\",\n  \"errorMessage\": \"string\",\n  \"affectedSystem\": \"string\",\n  \"likelyCause\": \"string\",\n  \"filesToFix\": [\"array\", \"of\", \"files\"],\n  \"severity\": \"low|medium|high|critical\",\n  \"canAutoFix\": true/false,\n  \"fixComplexity\": \"simple|moderate|complex\"\n}"
  },
  {
    type: "image_url",
    image_url: {
      url: $json.screenshotUrl || ('data:image/png;base64,' + ($json.screenshotFile?.data || ''))
    }
  }
] }}
```

**OR if Expression mode doesn't work, use Fixed mode with this:**
```
Analyze this error screenshot and provide structured diagnosis:

Context: {{ $json.context }}

Identify:
1. Error type (n8n_workflow, unity_build, deployment, web_error, other)
2. Exact error message
3. Affected system/component
4. Likely cause
5. Files/components that need fixing
6. Severity (low, medium, high, critical)

Return JSON only:
{
  "errorType": "string",
  "errorMessage": "string",
  "affectedSystem": "string",
  "likelyCause": "string",
  "filesToFix": ["array", "of", "files"],
  "severity": "low|medium|high|critical",
  "canAutoFix": true/false,
  "fixComplexity": "simple|moderate|complex"
}
```

**Then add the image separately:**
- Look for an "Add Image" or "Attach" button in the user message section
- Or add image URL in a separate field if available

---

## 3️⃣ TRIGGER BUILD (GitHub Actions) NODE CONFIGURATION

### For "Trigger Build (GitHub Actions)" Node:

**Configuration:**

1. **Method:** `POST` ✅ (already set)

2. **URL:** 
   ```
   https://api.github.com/repos/{{ $env.GITHUB_REPO_OWNER }}/{{ $env.GITHUB_REPO_NAME }}/actions/workflows/{{ $env.GITHUB_WORKFLOW_FILE }}/dispatches
   ```
   ✅ (already set - uses environment variables)

3. **Authentication:**
   - Set to: **Generic Credential Type** ✅
   - Generic Auth Type: **Header Auth** ✅
   - **Select Credential:** Choose **"GitHub Actions Token"** (the credential you created above)
   - ⚠️ **This is the red warning you see - you need to select the credential!**

4. **Send Headers:** ON ✅

5. **Specify Headers:** "Using Fields Below" ✅

6. **Header Parameters:**
   - Click "Add Header" or expand Header Parameters
   - Add:
     - **Name:** `Accept`
     - **Value:** `application/vnd.github.v3+json`

7. **Send Body:** ON ✅

8. **Body Parameters:**
   - Add:
     - **Name:** `ref`
     - **Value:** `main`

---

## 📋 QUICK CHECKLIST

### Credentials Setup:
- [ ] OpenAI API key created and added to n8n
- [ ] GitHub Personal Access Token created (with `repo` and `workflow` scopes)
- [ ] GitHub Actions Token credential created in n8n (HTTP Header Auth)
- [ ] Netlify API Token created and added to n8n (HTTP Header Auth)

### Node Configurations:
- [ ] Vision Analysis node: User message configured (text + image)
- [ ] Trigger Build node: GitHub Actions Token credential selected
- [ ] Trigger Build node: Header Parameters configured (Accept header)
- [ ] Trigger Build node: Body Parameters configured (ref: main)

---

## 🆘 TROUBLESHOOTING

### "Select Credential" warning in Trigger Build node:
**Fix:** 
1. Make sure you created the "GitHub Actions Token" credential first
2. Click the dropdown
3. Select "GitHub Actions Token"
4. Warning should disappear

### Vision Analysis node not working:
**Fix:**
- Make sure model is set to `gpt-4o` (supports vision)
- User message must include both text AND image
- Use Expression mode if Fixed mode doesn't support image

### OpenAI node "Missing required parameter: 'messages'":
**Fix:**
- Make sure both System and User messages are added
- Click "Add Message" for each one
- Verify Role is set correctly (System/User)

---

**Version:** 1.0  
**Created:** December 16, 2025  
**Status:** ✅ Complete Guide


