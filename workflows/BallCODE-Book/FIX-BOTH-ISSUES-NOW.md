# 🔧 Fix Both Issues: JSON + Image URL

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Issue 1:** "JSON parameter needs to be valid JSON" (with `={{`)  
**Issue 2:** "Error while downloading image" (without `={{`)  
**Fix:** Use Code Node approach + Fix image URL  
**Fix Time:** 3 minutes

---

## 🎯 THE PROBLEMS

1. **Expression mode (`={{`):** Not producing valid JSON
2. **Fixed mode (no `={{`):** JSON works but image URL fails
3. **Image URL:** `via.placeholder.com` might not work with OpenAI

---

## ✅ THE SOLUTION: Use Code Node (Most Reliable)

### **Step 1: Add Code Node Before HTTP Request**

**Node Name:** `Prepare OpenAI Request Body`

**Code:**
```javascript
// Prepare request body as JavaScript object (more reliable than expression)
const imageUrl = $json.imageUrlForAPI || $json.screenshotUrl || "https://picsum.photos/800/600";

// Ensure URL is properly formatted
let finalImageUrl = imageUrl;
if (!finalImageUrl.startsWith('http') && !finalImageUrl.startsWith('data:')) {
  finalImageUrl = `https://${finalImageUrl}`;
}

const requestBody = {
  model: "gpt-4o",
  temperature: 0.1,
  max_tokens: 2000,
  messages: [
    {
      role: "system",
      content: "You are an expert error diagnosis system. Analyze screenshots of errors and provide structured diagnosis."
    },
    {
      role: "user",
      content: [
        {
          type: "text",
          text: `Analyze this error screenshot and provide structured diagnosis:

Context: ${$json.context || "Unknown error"}

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
}`
        },
        {
          type: "image_url",
          image_url: {
            url: finalImageUrl
          }
        }
      ]
    }
  ]
};

// Return as JSON string for HTTP Request node
return {
  json: {
    ...$json,
    apiRequestBody: JSON.stringify(requestBody),
    apiRequestBodyObject: requestBody,
    debug_imageUrl: finalImageUrl
  }
};
```

### **Step 2: Update HTTP Request Node**

**In "OpenAI API Key" HTTP Request node:**

1. **Specify Body:** Using JSON
2. **JSON Body (Expression mode):** `={{ $json.apiRequestBody }}`

**OR use Fixed mode:**
1. **Specify Body:** Using JSON  
2. **JSON Body (Fixed mode):** `={{ $json.apiRequestBody }}` (still use expression to get the string)

**Actually, use Expression mode:**
- Click **Expression** button (fx)
- Paste: `={{ $json.apiRequestBody }}`

---

## 🔧 ALTERNATIVE: Fix Image URL Issue

### **Use a Different Test Image URL:**

**Instead of:** `https://via.placeholder.com/800x600.png?text=Test`

**Use one of these:**
- `https://picsum.photos/800/600` (random image)
- `https://httpbin.org/image/png` (test PNG)
- `https://jsonplaceholder.typicode.com/photos/1` (has image URL in response)

**Or use base64 encoded image:**

```javascript
// In "Prepare Image for API" node, add base64 fallback
const base64Image = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==";
```

---

## ✅ QUICKEST FIX (2 MINUTES)

### **Option 1: Use Code Node (Recommended)**

1. **Add Code node** before HTTP Request (code above)
2. **In HTTP Request:** Use `={{ $json.apiRequestBody }}` in Expression mode
3. **Done!** ✅

### **Option 2: Fix Image URL Only**

**In "Prepare Image for API" node, change fallback:**

```javascript
// Change this line:
imageUrl = input.screenshotUrl || 'data:image/png;base64,...';

// To this:
imageUrl = input.screenshotUrl || 'https://picsum.photos/800/600';
```

---

## 🧪 TEST IT

**After fixing, test with:**

```bash
curl -X POST http://192.168.1.226:5678/webhook-test/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://picsum.photos/800/600",
    "context": "Test error"
  }'
```

**Expected:**
- ✅ No "invalid JSON" error
- ✅ No "failed to download image" error
- ✅ API processes the request

---

## 📋 CHECKLIST

- [ ] Added "Prepare OpenAI Request Body" Code node
- [ ] Code node outputs `apiRequestBody` field
- [ ] HTTP Request uses `={{ $json.apiRequestBody }}` in Expression mode
- [ ] Image URL is valid (https:// or data:)
- [ ] Tested with valid image URL

---

**Time:** 3 minutes  
**Status:** Ready to fix  
**Next:** Add Code node and update HTTP Request


