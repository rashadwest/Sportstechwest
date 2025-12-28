# 📝 GPT-5.2 Prompts for Screenshot-to-Fix Workflow

**Model:** GPT-5.2 (or GPT-5.2-PRO)  
**Node:** Message a model  
**Purpose:** Generate code fixes from screenshot analysis

---

## 🔧 System Prompt (Role: System)

```
You are an expert code fix generator and software debugging assistant. Your role is to analyze error screenshots and diagnostic information, then generate precise, working code fixes.

**Your capabilities:**
- Analyze visual errors in screenshots
- Understand error messages and stack traces
- Identify root causes of bugs
- Generate complete, tested code fixes
- Provide clear explanations of what was wrong and how the fix works

**Your approach:**
1. Carefully analyze the provided screenshot and diagnosis
2. Identify the exact error or issue
3. Determine the root cause
4. Generate a complete fix that addresses the root cause
5. Ensure the fix is production-ready and follows best practices

**Output format:**
- Return valid JSON with the fix code and explanation
- Include file paths and line numbers if applicable
- Provide clear, actionable fixes
- Explain what was wrong and why the fix works
```

---

## 👤 User Prompt (Role: User)

```
Screenshot Analysis:
{{ $('Parse Diagnosis').item.json.diagnosis }}

Error Details:
- Error Type: {{ $('Parse Diagnosis').item.json.diagnosis.errorType }}
- Error Message: {{ $('Parse Diagnosis').item.json.diagnosis.errorMessage }}
- Affected System: {{ $('Parse Diagnosis').item.json.diagnosis.affectedSystem }}
- Likely Cause: {{ $('Parse Diagnosis').item.json.diagnosis.likelyCause }}
- Files to Fix: {{ $('Parse Diagnosis').item.json.diagnosis.filesToFix }}

Screenshot Context:
{{ $('Normalize Screenshot Input').item.json.context }}

**Task:**
Generate a complete code fix based on the screenshot analysis above. 

**Requirements:**
1. Analyze the error and root cause
2. Generate the exact code fix needed
3. Include file paths and specific changes
4. Explain what was wrong and how the fix resolves it
5. Ensure the fix is production-ready

**Output Format (JSON):**
{
  "fixCode": "the complete fixed code",
  "filePath": "path/to/file",
  "explanation": "what was wrong and how the fix works",
  "changes": ["list of specific changes made"],
  "canAutoFix": true/false,
  "confidence": 0.0-1.0
}

Generate the fix now.
```

---

## 🎯 Alternative: Simplified User Prompt

If the above is too complex, use this simpler version:

```
Analyze this error and generate a fix:

Error: {{ $('Parse Diagnosis').item.json.diagnosis.errorMessage }}
Type: {{ $('Parse Diagnosis').item.json.diagnosis.errorType }}
Files: {{ $('Parse Diagnosis').item.json.diagnosis.filesToFix }}

Screenshot shows: {{ $('Normalize Screenshot Input').item.json.context }}

Generate a complete code fix in JSON format:
{
  "fixCode": "the fixed code",
  "filePath": "file path",
  "explanation": "what was wrong and how to fix it",
  "canAutoFix": true
}
```

---

## 📋 Configuration Summary

**Node Settings:**
- **Model:** GPT-5.2 or GPT-5.2-PRO
- **Resource:** Text
- **Operation:** Message a Model
- **Credential:** OpenAI account (with valid API key)

**Prompt Structure:**
1. **System Role:** Expert code fix generator
2. **User Role:** Error details + screenshot context + fix request

**Input Data:**
- From "Parse Diagnosis" node: Error analysis
- From "Normalize Screenshot Input" node: Screenshot context

**Output:**
- JSON with fix code, file path, explanation
- Can be used by next node to apply the fix

---

## ✅ Quick Setup Steps

1. **Add System Prompt:**
   - Click "Add message" or "+"
   - Role: **System**
   - Content: Paste System prompt above

2. **Add User Prompt:**
   - Click "Add message" or "+"
   - Role: **User**
   - Content: Paste User prompt above (with n8n expressions)

3. **Select Model:**
   - Model: **GPT-5.2** or **GPT-5.2-PRO**

4. **Set Credential:**
   - Credential: **OpenAI account** (with API key)

5. **Test:**
   - Click "Execute step"
   - Check OUTPUT panel for generated fix

---

**These prompts will make GPT-5.2 analyze the screenshot and generate precise code fixes!** 🚀


