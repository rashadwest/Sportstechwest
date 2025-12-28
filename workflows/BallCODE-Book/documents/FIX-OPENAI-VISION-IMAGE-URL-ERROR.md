# 🔧 Fix OpenAI Vision Image URL Error

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Error:** "Bad request - please check your parameters"  
**Cause:** Invalid or inaccessible image URL (`https://example.com/test.png`)

---

## 🎯 THE PROBLEM

**Error Message:**
```
Bad request - please check your parameters
Error while downloading https://example.com/test.png.
```

**Root Cause:**
1. `https://example.com/test.png` is not a real image URL
2. OpenAI Vision API can't download it
3. No validation before sending to OpenAI
4. No fallback to base64 if URL fails

---

## ✅ SOLUTION: Add Image Validation & Processing Node

**Add this node BEFORE the "Vision Analysis" node:**

### Step 1: Add "Prepare Image for Vision API" Node

**Location:** After "Normalize Screenshot Input", before "Vision Analysis"

**Node Type:** Code

**Node Name:** `Prepare Image for Vision API`

**Code:**
```javascript
// Prepare Image for OpenAI Vision API
// OpenAI Vision API accepts:
// 1. Publicly accessible HTTPS URL
// 2. Base64 encoded image (data:image/png;base64,...)

const input = $input.item.json;

// Get screenshot data
let screenshotUrl = input.screenshotUrl;
let screenshotFile = input.screenshotFile;
let screenshotBase64 = input.screenshotBase64;

// Validate we have some image data
if (!screenshotUrl && !screenshotFile && !screenshotBase64) {
  throw new Error('No screenshot provided. Provide screenshotUrl, screenshotFile, or screenshotBase64');
}

// Prepare image URL for API
let imageUrlForAPI = null;

// Priority 1: Use base64 if available (most reliable)
if (screenshotBase64) {
  // Remove data URL prefix if present
  let base64Data = screenshotBase64;
  if (base64Data.includes(',')) {
    base64Data = base64Data.split(',')[1];
  }
  imageUrlForAPI = `data:image/png;base64,${base64Data}`;
}
// Priority 2: Use binary file data if available
else if (screenshotFile && screenshotFile.data) {
  let base64Data = screenshotFile.data;
  // Remove data URL prefix if present
  if (base64Data.includes(',')) {
    base64Data = base64Data.split(',')[1];
  }
  imageUrlForAPI = `data:image/png;base64,${base64Data}`;
}
// Priority 3: Use URL if valid
else if (screenshotUrl) {
  // Validate URL format
  try {
    const url = new URL(screenshotUrl);
    
    // Must be HTTPS (OpenAI requires HTTPS for security)
    if (url.protocol !== 'https:') {
      throw new Error(`Image URL must use HTTPS, not ${url.protocol}. Received: ${screenshotUrl}`);
    }
    
    // Check if it's an example/test URL (not accessible)
    if (screenshotUrl.includes('example.com') || 
        screenshotUrl.includes('placeholder') ||
        screenshotUrl.includes('test.png')) {
      throw new Error(`Invalid test URL: ${screenshotUrl}. Provide a real, publicly accessible image URL or use base64 encoding.`);
    }
    
    // URL looks valid - use it
    imageUrlForAPI = screenshotUrl;
  } catch (urlError) {
    // If URL is invalid, try to use it anyway (might be a relative path or special format)
    // But warn about it
    if (urlError.message.includes('Invalid URL')) {
      throw new Error(`Invalid image URL format: ${screenshotUrl}. Error: ${urlError.message}`);
    } else {
      throw urlError;
    }
  }
}
// No valid image found
else {
  throw new Error('No valid image data found. Provide screenshotUrl (HTTPS), screenshotFile, or screenshotBase64');
}

// Return prepared data
return {
  json: {
    ...input,
    imageUrlForAPI: imageUrlForAPI,
    imageFormat: imageUrlForAPI.startsWith('data:') ? 'base64' : 'url',
    prepared: true,
    preparedAt: new Date().toISOString()
  }
};
```

---

### Step 2: Update Vision Analysis Node

**Update the "Vision Analysis (GPT-4 Vision)" node:**

**Change the image_url parameter from:**
```
={{ $json.screenshotUrl || 'data:image/png;base64,' + $json.screenshotFile?.data }}
```

**To:**
```
={{ $json.imageUrlForAPI }}
```

**Full updated content array:**
```json
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
```

---

## 🔧 ALTERNATIVE: Quick Fix (If You Can't Add Node)

**If you can't add a new node right now, update the "Normalize Screenshot Input" node:**

**Replace the existing code with:**
```javascript
// Normalize screenshot input with validation
const input = $input.item.json;
const body = input.body || input;
const files = input.files || {};

// Extract screenshot (could be file upload or URL)
const screenshot = files.screenshot || body.screenshotUrl || body.screenshot || input.screenshotUrl || input.screenshot;
const context = body.context || input.context || 'Unknown error';
const source = body.source || input.source || 'manual_upload';

// Validate screenshot exists
if (!screenshot) {
  throw new Error('Missing screenshot: provide screenshotUrl, screenshotFile, or screenshotBase64 in request body');
}

// Prepare image URL for API
let imageUrlForAPI = null;

// Check if it's base64 data
if (typeof screenshot === 'string' && screenshot.startsWith('data:image')) {
  imageUrlForAPI = screenshot;
}
// Check if it's a valid HTTPS URL
else if (typeof screenshot === 'string' && screenshot.startsWith('http')) {
  // Validate it's not an example/test URL
  if (screenshot.includes('example.com') || screenshot.includes('test.png')) {
    throw new Error(`Invalid test URL: ${screenshot}. Provide a real, publicly accessible image URL or use base64 encoding.`);
  }
  
  // Must be HTTPS
  if (!screenshot.startsWith('https://')) {
    throw new Error(`Image URL must use HTTPS. Received: ${screenshot}`);
  }
  
  imageUrlForAPI = screenshot;
}
// Check if it's a file object
else if (typeof screenshot === 'object' && screenshot.data) {
  let base64Data = screenshot.data;
  if (base64Data.includes(',')) {
    base64Data = base64Data.split(',')[1];
  }
  imageUrlForAPI = `data:image/png;base64,${base64Data}`;
}
// Invalid format
else {
  throw new Error(`Invalid screenshot format. Provide HTTPS URL or base64 data. Received: ${typeof screenshot}`);
}

// Validate context
if (!context || context.trim() === '') {
  throw new Error('Missing context: provide error context in request body');
}

return {
  json: {
    screenshot: screenshot,
    screenshotUrl: typeof screenshot === 'string' && screenshot.startsWith('http') ? screenshot : null,
    screenshotFile: typeof screenshot === 'object' ? screenshot : null,
    screenshotBase64: typeof screenshot === 'string' && screenshot.startsWith('data:') ? screenshot : null,
    imageUrlForAPI: imageUrlForAPI, // NEW: Prepared image URL for API
    context: context,
    source: source,
    timestamp: new Date().toISOString(),
    requestId: `fix-${Date.now()}`
  }
};
```

**Then update Vision Analysis node to use:**
```
={{ $json.imageUrlForAPI }}
```

---

## 🧪 TESTING

### Test 1: Valid HTTPS URL
```bash
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://picsum.photos/800/600",
    "context": "Test error screenshot"
  }'
```
**Expected:** ✅ Should work

### Test 2: Invalid Example URL
```bash
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://example.com/test.png",
    "context": "Test error"
  }'
```
**Expected:** ❌ Clear error message about invalid test URL

### Test 3: Base64 Image
```bash
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotBase64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==",
    "context": "Test error"
  }'
```
**Expected:** ✅ Should work

### Test 4: Missing Screenshot
```bash
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{
    "context": "Test error"
  }'
```
**Expected:** ❌ Clear error message about missing screenshot

---

## 📋 IMPLEMENTATION CHECKLIST

- [ ] Add "Prepare Image for Vision API" node (or update "Normalize Screenshot Input")
- [ ] Update "Vision Analysis" node to use `$json.imageUrlForAPI`
- [ ] Test with valid HTTPS URL
- [ ] Test with invalid example URL (should error clearly)
- [ ] Test with base64 image
- [ ] Test with missing screenshot (should error clearly)
- [ ] Verify error messages are clear and actionable

---

## 🎯 WHY THIS FIXES IT

**Before:**
- Workflow sent `https://example.com/test.png` directly to OpenAI
- OpenAI tried to download it and failed
- No validation, no error handling

**After:**
- Validates image URL before sending
- Rejects example/test URLs with clear error
- Supports both URL and base64 formats
- Clear error messages for debugging

---

## 💡 TIPS

1. **Always use HTTPS URLs** - OpenAI requires HTTPS for security
2. **Use base64 for reliability** - No download needed, works every time
3. **Test URLs first** - Make sure they're publicly accessible
4. **Provide clear errors** - Helps users fix issues quickly

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Complete Fix  
**Next:** Add node and test


