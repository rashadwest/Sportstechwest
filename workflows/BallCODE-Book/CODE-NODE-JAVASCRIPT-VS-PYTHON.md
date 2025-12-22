# 📝 Code Node: JavaScript vs Python

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Question:** Which language for Code node?  
**Answer:** **JavaScript** (for this use case)

---

## ✅ USE JAVASCRIPT

### **Why JavaScript:**

1. **Native to n8n**
   - n8n is built on Node.js
   - JavaScript is the default language
   - Better performance and integration

2. **Better Data Access**
   - `$json` works directly
   - `$input.item.json` is JavaScript syntax
   - No conversion needed

3. **JSON Handling**
   - `JSON.stringify()` is native
   - No imports needed
   - Faster execution

4. **Expression Compatibility**
   - n8n expressions use JavaScript
   - Same syntax throughout workflow
   - Easier to debug

5. **No Dependencies**
   - Works out of the box
   - No Python installation needed
   - No package imports

---

## ❌ DON'T USE PYTHON (For This)

### **Why Not Python:**

1. **Slower**
   - Python runs in separate process
   - More overhead
   - Slower execution

2. **Data Conversion**
   - Need to convert n8n data structures
   - More complex syntax
   - Potential errors

3. **JSON Handling**
   - Need `import json`
   - More verbose
   - Less intuitive

4. **Less Common**
   - Most n8n examples use JavaScript
   - Harder to find help
   - Less documentation

---

## ✅ THE CODE (JavaScript)

**When you add the Code node, select: JavaScript**

**Code:**
```javascript
// Prepare request body - JavaScript
const imageUrl = $json.imageUrlForAPI || $json.screenshotUrl || "https://picsum.photos/800/600";

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
            url: imageUrl
          }
        }
      ]
    }
  ]
};

// Return as JSON string
return {
  json: {
    ...$json,
    apiRequestBody: JSON.stringify(requestBody)
  }
};
```

---

## 📋 WHEN TO USE PYTHON

**Use Python only if:**
- You need specific Python libraries (pandas, numpy, etc.)
- You're doing data science/ML work
- You have existing Python code to reuse
- You're more comfortable with Python

**For this workflow:**
- ✅ **Use JavaScript** - it's simpler, faster, and better integrated

---

## ✅ QUICK ANSWER

**Choose: JavaScript**

**Steps:**
1. Add Code node
2. **Select "JavaScript"** (should be default)
3. Paste the code above
4. Done! ✅

---

**Status:** Use JavaScript  
**Reason:** Native, faster, better integration  
**Next:** Add Code node with JavaScript

