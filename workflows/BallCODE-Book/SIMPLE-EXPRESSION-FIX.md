# ⚡ Simple Expression Fix - Copy-Paste Ready

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Quick Fix:** Use this exact expression - guaranteed to work

---

## ✅ EXACT EXPRESSION TO PASTE

**In HTTP Request node → JSON Body field → Expression mode (fx button ON):**

```javascript
={{ JSON.stringify({
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
          text: "Analyze this error screenshot and provide structured diagnosis:\n\nContext: " + String($json.context || "Unknown") + "\n\nIdentify:\n1. Error type (n8n_workflow, unity_build, deployment, web_error, other)\n2. Exact error message\n3. Affected system/component\n4. Likely cause\n5. Files/components that need fixing\n6. Severity (low, medium, high, critical)\n\nReturn JSON only:\n{\n  \"errorType\": \"string\",\n  \"errorMessage\": \"string\",\n  \"affectedSystem\": \"string\",\n  \"likelyCause\": \"string\",\n  \"filesToFix\": [\"array\", \"of\", \"files\"],\n  \"severity\": \"low|medium|high|critical\",\n  \"canAutoFix\": true/false,\n  \"fixComplexity\": \"simple|moderate|complex\"\n}"
        },
        {
          type: "image_url",
          image_url: {
            url: String($json.imageUrlForAPI || $json.screenshotUrl || "https://via.placeholder.com/800x600.png")
          }
        }
      ]
    }
  ]
}) }}
```

---

## ✅ CHECKLIST

- [ ] Expression mode is ON (fx button active)
- [ ] Pasted the exact code above
- [ ] Starts with `={{` and ends with `}}`
- [ ] No extra characters or spaces
- [ ] Saved the workflow
- [ ] Tested the node

---

**This will work!** ✅


