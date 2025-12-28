# 🎯 GPT-5.2 Prompts - Ready to Use

**Copy and paste these directly into your "Message a model" node**

---

## 📋 System Prompt (Role: System)

**Copy this exactly:**

```
You are an expert code fix generator and software debugging assistant. Analyze error diagnoses and generate precise, working code fixes.

**Your capabilities:**
- Understand error messages and stack traces
- Identify root causes of bugs
- Generate complete, tested code fixes
- Provide clear explanations

**Your approach:**
1. Analyze the provided error diagnosis
2. Identify the exact error and root cause
3. Generate a complete fix that addresses the root cause
4. Ensure the fix is production-ready

**Output format:**
Return valid JSON with the fix code and explanation.
```

---

## 👤 User Prompt (Role: User)

**Copy this exactly (includes n8n expressions):**

```
Analyze this error and generate a complete code fix:

**Error Diagnosis:**
{{ JSON.stringify($('Parse Diagnosis').item.json.diagnosis, null, 2) }}

**Error Details:**
- Type: {{ $('Parse Diagnosis').item.json.diagnosis.errorType }}
- Message: {{ $('Parse Diagnosis').item.json.diagnosis.errorMessage }}
- System: {{ $('Parse Diagnosis').item.json.diagnosis.affectedSystem }}
- Cause: {{ $('Parse Diagnosis').item.json.diagnosis.likelyCause }}
- Files: {{ JSON.stringify($('Parse Diagnosis').item.json.diagnosis.filesToFix) }}

**Context:**
{{ $('Normalize Screenshot Input').item.json.context }}

**Task:**
Generate a complete code fix based on the diagnosis above.

**Requirements:**
1. Analyze the error and root cause
2. Generate the exact code fix needed
3. Include file paths and specific changes
4. Explain what was wrong and how the fix resolves it
5. Ensure the fix is production-ready

**Output Format (JSON only, no markdown):**
{
  "fixCode": "the complete fixed code",
  "filePath": "path/to/file",
  "explanation": "what was wrong and how the fix works",
  "changes": ["list of specific changes"],
  "canAutoFix": true,
  "confidence": 0.95
}

Generate the fix now.
```

---

## 🔧 Alternative: Simpler User Prompt

**If the above doesn't work, use this simpler version:**

```
Error: {{ $('Parse Diagnosis').item.json.diagnosis.errorMessage }}
Type: {{ $('Parse Diagnosis').item.json.diagnosis.errorType }}
Files: {{ JSON.stringify($('Parse Diagnosis').item.json.diagnosis.filesToFix) }}
Context: {{ $('Normalize Screenshot Input').item.json.context }}

Generate a code fix in JSON:
{
  "fixCode": "the fixed code",
  "filePath": "file path",
  "explanation": "what was wrong and how to fix it",
  "canAutoFix": true
}
```

---

## ✅ Quick Setup in n8n

1. **In "Message a model" node:**
   - Click "Add message" or the "+" button
   
2. **Add System message:**
   - Role: **System**
   - Content: Paste System prompt above
   
3. **Add User message:**
   - Role: **User**
   - Content: Paste User prompt above (with n8n expressions)

4. **Select Model:**
   - Model: **GPT-5.2** or **GPT-5.2-PRO**

5. **Set Credential:**
   - Credential: **OpenAI account**

6. **Test:**
   - Click "Execute step"
   - Check OUTPUT panel

---

## 📊 Expected Output

**After execution, OUTPUT should show:**

```json
{
  "fixCode": "// Fixed code here...",
  "filePath": "path/to/file.js",
  "explanation": "The error was caused by...",
  "changes": ["Fixed variable name", "Added null check"],
  "canAutoFix": true,
  "confidence": 0.95
}
```

---

**These prompts are ready to paste directly into your node!** 🚀


