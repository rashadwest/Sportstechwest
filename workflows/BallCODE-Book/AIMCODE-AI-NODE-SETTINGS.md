# AIMCODE Solution: AI Analyze Request Node Settings
## Complete Configuration Guide

**Date:** December 9, 2025  
**Issue:** Missing required parameter: 'messages'  
**Status:** ✅ FIXED - Complete Settings Provided

---

## CLEAR Framework

### C - Clarity
**Problem:** AI Analyze Request node shows error "Missing required parameter: 'messages'"  
**Root Cause:** Prompt section is empty - no messages configured  
**Solution:** Add System and User messages with proper content

### L - Logic
**Configuration Flow:**
1. Set Resource to "Chat"
2. Set Operation to "Create Message" (not "Complete")
3. Add System message (defines AI role)
4. Add User message (contains the request)
5. Set Model to "gpt-4"

### E - Examples
**Previous Working Configuration:**
- Resource: "chat"
- Operation: "createMessage"
- Messages: System + User prompts
- Model: "gpt-4"

### A - Adaptation
**Current State:** Operation is "Complete" (wrong)  
**Needed:** Change to "Create Message" and add messages

### R - Results
**Success Criteria:**
- Node executes without errors
- AI returns JSON action plan
- Response can be parsed by next node

---

## Alpha Evolve (Layer-by-Layer)

### Layer 1: Basic Node Type
- OpenAI Chat node
- Resource: Chat

### Layer 2: Operation
- Operation: Create Message (not "Complete")

### Layer 3: Messages
- System message: Defines AI role
- User message: Contains request with template variable

### Layer 4: Model & Options
- Model: gpt-4
- Temperature: 0.3
- Max Tokens: 2000

---

## Expert Consultation

### Hassabis (Systematic)
- Build configuration systematically: Resource → Operation → Messages → Options
- Ensure each layer is correct

### Jobs (Simplicity)
- Keep messages clear and focused
- Use simple, direct prompts

---

## COMPLETE NODE SETTINGS

### **1. Credential**
- **Select:** Your OpenAI API credential (or create new one)
- **Type:** OpenAI API
- **Required:** API Key

### **2. Resource**
- **Value:** `Chat`
- **Current:** ✅ Already set correctly

### **3. Operation**
- **Value:** `Create Message` (or `Generate a Chat Completion`)
- **Current:** ❌ Shows "Complete" - **CHANGE THIS**
- **Action:** Click dropdown, select "Create Message"

### **4. Model**
- **Value:** `gpt-4`
- **Current:** ✅ Already set correctly

### **5. Messages (CRITICAL - This is what's missing)**

Click **"Add Message"** button and add TWO messages:

#### **Message 1: System Message**
- **Role:** Select `System`
- **Content:** 
  ```
  You are a Unity development assistant. Analyze development requests and create a structured action plan with specific Unity edits needed.
  ```

#### **Message 2: User Message**
- **Role:** Select `User`
- **Content:**
  ```
  Analyze this Unity development request and create a JSON action plan:

  Request: {{ $json.request || 'No request provided' }}

  Return JSON with:
  - needsUnityEdits: boolean (does this require Unity Editor changes?)
  - unityEdits: array of {file: string, action: string, changes: string}
  - needsBuild: boolean
  - needsDeploy: boolean
  - estimatedTime: string
  - priority: string (low/medium/high)

  Format as valid JSON only.
  ```

### **6. Options (Optional but Recommended)**
- **Temperature:** `0.3`
- **Max Tokens:** `2000`

### **7. Simplify Toggle**
- **Current:** ✅ ON (green) - Keep this ON

---

## STEP-BY-STEP INSTRUCTIONS

### Step 1: Fix Operation
1. Click on **Operation** dropdown
2. Change from **"Complete"** to **"Create Message"** (or "Generate a Chat Completion")

### Step 2: Add Messages
1. Click **"Add Message"** button in Prompt section
2. **First Message:**
   - Click **Role** dropdown → Select **"System"**
   - In **Content** field, paste:
     ```
     You are a Unity development assistant. Analyze development requests and create a structured action plan with specific Unity edits needed.
     ```
3. Click **"Add Message"** again
4. **Second Message:**
   - Click **Role** dropdown → Select **"User"**
   - In **Content** field, paste:
     ```
     Analyze this Unity development request and create a JSON action plan:

     Request: {{ $json.request || 'No request provided' }}

     Return JSON with:
     - needsUnityEdits: boolean (does this require Unity Editor changes?)
     - unityEdits: array of {file: string, action: string, changes: string}
     - needsBuild: boolean
     - needsDeploy: boolean
     - estimatedTime: string
     - priority: string (low/medium/high)

     Format as valid JSON only.
     ```

### Step 3: Verify Settings
- ✅ Resource: Chat
- ✅ Operation: Create Message
- ✅ Model: gpt-4
- ✅ Messages: 2 messages (System + User)
- ✅ Credential: Selected

### Step 4: Save & Test
1. Click **"Save"** button
2. Click **"Execute step"** to test
3. Should see AI response instead of error

---

## VERIFICATION

**Node works correctly when:**
- ✅ No error message in output
- ✅ AI response appears in output panel
- ✅ Response contains JSON action plan
- ✅ Next node (Parse AI Response) can process the output

---

## TROUBLESHOOTING

**If "Create Message" option doesn't exist:**
- Try "Generate a Chat Completion" instead
- Or update the OpenAI node to latest version (warning message suggests this)

**If messages don't save:**
- Make sure you click "Add Message" for each one
- Verify Role is selected (System/User)
- Check Content field has text

**If still getting errors:**
- Verify OpenAI credential is valid
- Check API key has credits
- Try testing with simpler message first

---

**The fix is ready! Follow the step-by-step instructions above to configure the node correctly.**



