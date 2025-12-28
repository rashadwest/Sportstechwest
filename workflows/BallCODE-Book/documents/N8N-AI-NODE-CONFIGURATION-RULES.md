# 🤖 n8n AI Node Configuration Rules - System & User Guidelines

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Purpose:** Clear rules for configuring OpenAI/AI nodes in n8n workflows

---

## 🎯 SYSTEM RULES (MANDATORY)

### Rule 1: OpenAI API Credentials ✅

**MUST Configure:**
- ✅ Credential name: `"openai-credentials"` or `"OpenAI API"`
- ✅ Credential ID: `"openai-credentials"` (if using ID reference)
- ✅ API Key: Must be valid OpenAI API key

**Configuration:**
```json
{
  "credentials": {
    "openAiApi": {
      "id": "openai-credentials",
      "name": "OpenAI API"
    }
  }
}
```

**Action:** Configure credentials in n8n Settings → Credentials → Add OpenAI API

---

### Rule 2: Model Selection ✅

**Standard Models:**
- ✅ **GPT-4:** For complex analysis, code generation, multi-step reasoning
- ✅ **GPT-4o:** For vision/image analysis (screenshot workflows)
- ✅ **GPT-3.5-turbo:** For simple tasks (not recommended for BallCODE)

**Configuration:**
```json
{
  "model": "gpt-4",  // or "gpt-4o" for vision
  "options": {
    "temperature": 0.2,  // Lower = more deterministic
    "maxTokens": 3000    // Adjust based on expected response length
  }
}
```

**BallCODE Standards:**
- **Full Integration:** `gpt-4` (complex analysis)
- **Screenshot Fix:** `gpt-4o` (vision analysis)
- **Code Generation:** `gpt-4` (better code quality)

---

### Rule 3: Temperature Settings ✅

**Temperature Guidelines:**
- ✅ **0.1-0.2:** Code generation, structured output, deterministic tasks
- ✅ **0.3-0.5:** Analysis, reasoning, balanced creativity
- ✅ **0.6-0.8:** Creative writing, story generation (not used in BallCODE)

**BallCODE Standards:**
- **Code/JSON Generation:** `0.2` (deterministic)
- **Analysis/Reasoning:** `0.3` (balanced)
- **Vision Analysis:** `0.1` (precise diagnosis)

---

### Rule 4: Max Tokens ✅

**Token Limits:**
- ✅ **2000 tokens:** Short responses, simple tasks
- ✅ **3000 tokens:** Standard responses, analysis
- ✅ **4000 tokens:** Complex responses, multi-step reasoning

**BallCODE Standards:**
- **Screenshot Analysis:** `2000` (diagnosis only)
- **Code Generation:** `3000` (code + explanation)
- **Full Integration Analysis:** `4000` (comprehensive action plans)

---

### Rule 5: System Prompts ✅

**MUST Include:**
- ✅ Role definition (e.g., "You are a Unity game development expert")
- ✅ Context (e.g., "Using AIMCODE methodology")
- ✅ Output format (e.g., "Return JSON only")
- ✅ Constraints (e.g., "Format as valid JSON only")

**Example:**
```json
{
  "role": "system",
  "content": "You are an expert AI development assistant using AIMCODE methodology. Your role is to analyze development prompts and create comprehensive action plans. Return JSON only. Format as valid JSON only."
}
```

---

### Rule 6: User Prompts ✅

**MUST Include:**
- ✅ Clear task description
- ✅ Required data (use `{{ $json.field }}` for n8n expressions)
- ✅ Expected output format
- ✅ Examples if needed

**Example:**
```json
{
  "role": "user",
  "content": "Development Prompt: {{ $json.prompt }}\n\nAnalyze this prompt and return JSON with:\n- analysis: { promptType, systemsAffected: [] }\n- actionPlan: { layers: [] }\n\nFormat as valid JSON only."
}
```

---

### Rule 7: Response Parsing ✅

**MUST Parse AI Responses:**
- ✅ Extract JSON from markdown (if wrapped)
- ✅ Handle parsing errors gracefully
- ✅ Provide fallback responses

**Standard Pattern:**
```javascript
const aiResponse = $input.item.json.choices?.[0]?.message?.content || '{}';
let parsed;

try {
  // Extract JSON from response (might be wrapped in markdown)
  const jsonMatch = aiResponse.match(/\{[\s\S]*\}/);
  parsed = JSON.parse(jsonMatch ? jsonMatch[0] : aiResponse);
} catch (e) {
  // Fallback if parsing fails
  parsed = {
    error: 'Failed to parse AI response',
    rawResponse: aiResponse
  };
}
```

---

## 👤 USER RULES (Best Practices)

### Rule 1: Always Test AI Nodes ✅

**Before Activating Workflow:**
1. ✅ Test AI node with sample data
2. ✅ Verify response format matches expectations
3. ✅ Check token usage (cost monitoring)
4. ✅ Verify parsing works correctly

---

### Rule 2: Monitor API Costs ✅

**Cost Management:**
- ✅ Use appropriate model (GPT-4 vs GPT-3.5)
- ✅ Set reasonable maxTokens limits
- ✅ Monitor usage in OpenAI dashboard
- ✅ Use GPT-3.5 for simple tasks (if acceptable)

---

### Rule 3: Error Handling ✅

**MUST Handle:**
- ✅ API failures (network errors, rate limits)
- ✅ Invalid responses (parsing failures)
- ✅ Missing data (null/undefined checks)
- ✅ Timeout errors

**Pattern:**
```javascript
// Always check if response exists
const aiResponse = $input.item.json.choices?.[0]?.message?.content;
if (!aiResponse) {
  return {
    json: {
      error: 'No response from AI',
      proceed: false
    }
  };
}
```

---

### Rule 4: Expression Usage ✅

**Use n8n Expressions:**
- ✅ `{{ $json.field }}` - Access current node data
- ✅ `{{ $('Node Name').item.json.field }}` - Access previous node data
- ✅ `{{ JSON.stringify($json) }}` - Convert to JSON string

**Example:**
```json
{
  "content": "Prompt: {{ $json.prompt }}\n\nSchema: {{ JSON.stringify($('Load Schema').item.json.curriculumSchema) }}"
}
```

---

### Rule 5: Response Validation ✅

**MUST Validate:**
- ✅ Response structure matches expected format
- ✅ Required fields present
- ✅ Data types correct
- ✅ No null/undefined critical fields

**Pattern:**
```javascript
// Validate response structure
if (!parsed.analysis || !parsed.actionPlan) {
  return {
    json: {
      ...$json,
      valid: false,
      error: 'AI response missing required fields',
      proceed: false
    }
  };
}
```

---

## 📋 AI NODE CONFIGURATION TEMPLATE

### Standard AI Node Structure:

```json
{
  "parameters": {
    "resource": "chat",
    "operation": "create",
    "model": "gpt-4",
    "options": {
      "temperature": 0.2,
      "maxTokens": 3000
    },
    "messages": {
      "values": [
        {
          "role": "system",
          "content": "You are an expert [ROLE]. [CONTEXT]. Return JSON only. Format as valid JSON only."
        },
        {
          "role": "user",
          "content": "Task: {{ $json.task }}\n\nData: {{ JSON.stringify($json.data) }}\n\nReturn JSON with:\n- field1: type\n- field2: type\n\nFormat as valid JSON only."
        }
      ]
    }
  },
  "credentials": {
    "openAiApi": {
      "id": "openai-credentials",
      "name": "OpenAI API"
    }
  }
}
```

---

## 🎯 BALLCODE-SPECIFIC RULES

### Rule 1: AIMCODE Methodology ✅

**MUST Include in System Prompt:**
- ✅ Reference to AIMCODE methodology
- ✅ Demis Hassabis (Alpha Evolve) approach
- ✅ Layer-by-layer thinking (L1 → L2 → L3 → L4)

**Example:**
```
"You are an expert AI development assistant using AIMCODE methodology with Demis Hassabis (Alpha Evolve) as the expert consultant. Apply systematic, layered approach (Layer 1: Foundation → Layer 2: Application → Layer 3: Integration → Layer 4: Mastery)."
```

---

### Rule 2: Curriculum Schema Context ✅

**MUST Reference:**
- ✅ Unified curriculum schema (`CURRICULUM-DATA-EXAMPLE.json`)
- ✅ 4 systems (Game, Curriculum, Book, Website)
- ✅ Integration requirements

**Example:**
```
"Use unified curriculum schema (CURRICULUM-DATA-EXAMPLE.json) as single source of truth. Ensure full integration across all 4 systems: Game, Curriculum, Book, Website."
```

---

### Rule 3: Response Format ✅

**MUST Return:**
- ✅ Valid JSON (not markdown-wrapped)
- ✅ Structured data matching expected schema
- ✅ Error handling in response structure

**Example:**
```
"Return JSON with:\n- status: string\n- data: object\n- errors: array\n\nFormat as valid JSON only. Do not wrap in markdown code blocks."
```

---

## ✅ QUICK REFERENCE

### Model Selection:
- **Complex Analysis:** `gpt-4`, temp `0.3`, tokens `4000`
- **Code Generation:** `gpt-4`, temp `0.2`, tokens `3000`
- **Vision Analysis:** `gpt-4o`, temp `0.1`, tokens `2000`

### Temperature:
- **Deterministic:** `0.1-0.2`
- **Balanced:** `0.3-0.5`
- **Creative:** `0.6-0.8` (not used in BallCODE)

### Max Tokens:
- **Short:** `2000`
- **Standard:** `3000`
- **Long:** `4000`

---

## 🚨 COMMON MISTAKES TO AVOID

### ❌ DON'T:
- ❌ Use GPT-3.5 for complex tasks
- ❌ Set temperature > 0.5 for code generation
- ❌ Forget to parse JSON from markdown
- ❌ Skip error handling
- ❌ Use hardcoded data instead of expressions
- ❌ Forget to configure credentials

### ✅ DO:
- ✅ Use GPT-4 for complex analysis
- ✅ Set temperature 0.2-0.3 for code
- ✅ Always parse and validate responses
- ✅ Handle errors gracefully
- ✅ Use n8n expressions for dynamic data
- ✅ Configure credentials before testing

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Complete Configuration Rules



