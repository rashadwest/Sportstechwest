# Phase 3: n8n Workflow Build Guide
## Build Unity Automation Workflow Matching Your Crypto Pattern

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Purpose:** Build n8n workflow using your proven crypto workflow pattern  
**Location:** n8n on Raspberry Pi  
**Pattern:** Schedule Trigger → Edit Fields → Basic LLM Chain → Execute Command → etc.

---

## Overview: Workflow Structure

**Matching your working crypto workflow pattern:**

```
Schedule Trigger (like your crypto workflow)
    ↓
Edit Fields (set initial data - like your Edit Fields1)
    ↓
Basic LLM Chain (AI analysis - like your workflow)
    ├─ OpenAI Chat Model (connected as Model input)
    ↓
Edit Fields (parse AI response)
    ↓
Filter (should proceed? - like your Filter node)
    ↓
Execute Command (git clone/pull - like your Execute Command)
    ↓
HTTP Request (trigger GitHub Actions OR Execute Command for local build)
    ↓
HTTP Request (deploy to Netlify OR Execute Command for Netlify CLI)
    ↓
Edit Fields (completion message)
    ↓
Discord/Webhook (notification - like your Discord node)
```

---

## Phase 3.1: Foundation - Schedule Trigger + Edit Fields

### Step 3.1.1: Create New Workflow

1. **Open n8n:**
   - Mac: `n8n-dev` then `http://localhost:5678`
   - Raspberry Pi: `http://your-pi-ip:5678`

2. **Create Workflow:**
   - Click "Workflows" → "New Workflow"
   - Name: `Unity AI Automation`
   - Save

**Checkpoint:** Workflow created

---

### Step 3.1.2: Add Schedule Trigger

1. **Add Node:**
   - Click "+" to add node
   - Search: "Schedule Trigger"
   - Add node

2. **Configure (Match Your Crypto Workflow):**
   - **Rule Type:** Interval
   - **Interval:** Every 6 hours
   - **OR use Cron:** `0 */6 * * *` (every 6 hours)
   - **For Testing:** Set to 1 minute initially

3. **Test:**
   - Activate workflow
   - Wait for trigger time
   - Check execution tab
   - Verify trigger fires

**Checkpoint:** Schedule Trigger fires reliably

---

### Step 3.1.3: Add Edit Fields Node

1. **Add Node:**
   - Click "+" after Schedule Trigger
   - Search: "Edit Fields"
   - Add node

2. **Configure (Like Your Edit Fields1):**
   - **Mode:** Manual
   - **Add Fields:**
     - `request`: `"Automated Unity build and deploy"`
     - `triggerType`: `"scheduled"`
     - `timestamp`: `{{ $now }}`

3. **Connect:**
   - Connect Schedule Trigger → Edit Fields

4. **Test:**
   - Execute workflow manually
   - Check Edit Fields output
   - Verify data structure

**Checkpoint:** Data flows through Edit Fields correctly

---

## Phase 3.2: AI Integration - Basic LLM Chain + OpenAI

### Step 3.2.1: Add Basic LLM Chain Node

1. **Add Node:**
   - Click "+" after Edit Fields
   - Search: "Basic LLM Chain"
   - Add node

2. **Configure:**
   - **Prompt:** 
     ```
     Analyze this Unity development request: {{ $json.request }}
     
     Return JSON only with this structure:
     {
       "needsBuild": true/false,
       "needsDeploy": true/false,
       "estimatedTime": "15 minutes",
       "priority": "medium"
     }
     ```

3. **Connect:**
   - Edit Fields → Basic LLM Chain

**Checkpoint:** Basic LLM Chain node added

---

### Step 3.2.2: Add OpenAI Chat Model Node

1. **Add Node:**
   - Click "+" to add new node
   - Search: "OpenAI Chat Model"
   - Add node

2. **Configure:**
   - **Model:** `gpt-3.5-turbo` (or `gpt-4`)
   - **Temperature:** `0.3`
   - **Max Tokens:** `500`
   - **Credentials:** Select your OpenAI API credentials

3. **Connect to Basic LLM Chain:**
   - Connect OpenAI Chat Model to Basic LLM Chain
   - **Connection Type:** "Model" input (like your crypto workflow)
   - Drag from OpenAI Chat Model → Basic LLM Chain (Model input)

4. **Test:**
   - Execute workflow
   - Check Basic LLM Chain output
   - Verify AI response

**Checkpoint:** AI analysis works correctly

---

### Step 3.2.3: Add Edit Fields to Parse AI Response

1. **Add Node:**
   - Click "+" after Basic LLM Chain
   - Search: "Edit Fields"
   - Add node

2. **Configure:**
   - **Mode:** Manual
   - **Add Fields:**
     - `actionPlan`: `{{ $json.output }}` (or whatever LLM Chain outputs)
     - `shouldProceed`: `{{ $json.actionPlan.needsBuild || $json.actionPlan.needsDeploy }}`

3. **Connect:**
   - Basic LLM Chain → Edit Fields

4. **Test:**
   - Check parsed data
   - Verify actionPlan structure

**Checkpoint:** AI response parsed correctly

---

### Step 3.2.4: Add Filter Node

1. **Add Node:**
   - Click "+" after Edit Fields
   - Search: "Filter"
   - Add node

2. **Configure (Like Your Filter Node):**
   - **Condition:**
     - **Field:** `shouldProceed`
     - **Operation:** equals
     - **Value:** `true`

3. **Connect:**
   - Edit Fields → Filter

4. **Test:**
   - Test with different AI responses
   - Verify Filter routes correctly

**Checkpoint:** Filter works correctly

---

## Phase 3.3: Git Operations - Execute Command

### Step 3.3.1: Add Execute Command for Git

1. **Add Node:**
   - Click "+" after Filter
   - Search: "Execute Command"
   - Add node

2. **Configure (Like Your Execute Command Pattern):**
   - **Command:** `bash`
   - **Arguments:**
     ```bash
     -c "if [ -d '{{ $env.UNITY_PROJECT_PATH }}' ]; then cd '{{ $env.UNITY_PROJECT_PATH }}' && git pull; else git clone {{ $env.UNITY_REPO_URL }} {{ $env.UNITY_PROJECT_PATH }}; fi"
     ```

3. **Connect:**
   - Filter → Execute Command

4. **Test:**
   - Verify git operations work
   - Check command output

**Checkpoint:** Git operations work correctly

---

## Phase 3.4: Build Process - Trigger GitHub Actions

### Step 3.4.1: Add HTTP Request to Trigger GitHub Actions

1. **Add Node:**
   - Click "+" after Execute Command
   - Search: "HTTP Request"
   - Add node

2. **Configure:**
   - **Method:** POST
   - **URL:** 
     ```
     https://api.github.com/repos/{{ $env.GITHUB_REPO_OWNER }}/{{ $env.GITHUB_REPO_NAME }}/actions/workflows/{{ $env.GITHUB_WORKFLOW_FILE }}/dispatches
     ```
   - **Authentication:** Header Auth
   - **Header Name:** `Authorization`
   - **Header Value:** `Bearer {{ $env.GITHUB_ACTIONS_TOKEN }}`
   - **Additional Headers:**
     - `Accept`: `application/vnd.github.v3+json`
   - **Body (JSON):**
     ```json
     {
       "ref": "main"
     }
     ```

3. **Connect:**
   - Execute Command → HTTP Request

4. **Test:**
   - Trigger build
   - Check GitHub Actions
   - Verify workflow runs

**Checkpoint:** GitHub Actions triggered successfully

---

## Phase 3.5: Deployment - Deploy to Netlify

### Step 3.5.1: Add HTTP Request for Netlify Deploy

1. **Add Node:**
   - Click "+" after HTTP Request (GitHub Actions)
   - Search: "HTTP Request"
   - Add node

2. **Configure:**
   - **Method:** POST
   - **URL:** 
     ```
     https://api.netlify.com/api/v1/sites/{{ $env.NETLIFY_SITE_ID }}/deploys
     ```
   - **Authentication:** Header Auth
   - **Header Name:** `Authorization`
   - **Header Value:** `Bearer {{ $env.NETLIFY_AUTH_TOKEN }}`
   - **Additional Headers:**
     - `Content-Type`: `application/json`
   - **Body (JSON):**
     ```json
     {
       "dir": "{{ $env.BUILD_OUTPUT_PATH }}"
     }
     ```

   **Note:** This assumes GitHub Actions already built and deployed. If deploying from local build, use Execute Command with Netlify CLI instead.

3. **Connect:**
   - HTTP Request (GitHub Actions) → HTTP Request (Netlify)

4. **Test:**
   - Verify deployment
   - Check Netlify dashboard

**Checkpoint:** Deployment works correctly

---

## Phase 3.6: Notifications - Completion Message

### Step 3.6.1: Add Edit Fields for Completion

1. **Add Node:**
   - Click "+" after HTTP Request (Netlify)
   - Search: "Edit Fields"
   - Add node

2. **Configure:**
   - **Mode:** Manual
   - **Add Fields:**
     - `status`: `"success"`
     - `message`: `"Unity workflow completed successfully"`
     - `siteUrl`: `"https://{{ $env.NETLIFY_SITE_NAME }}.netlify.app"`
     - `timestamp`: `{{ $now }}`

3. **Connect:**
   - HTTP Request (Netlify) → Edit Fields

**Checkpoint:** Completion message prepared

---

### Step 3.6.2: Add Discord/Webhook Notification

1. **Add Node:**
   - Click "+" after Edit Fields
   - Search: "Discord" (or "HTTP Request" for webhook)
   - Add node

2. **Configure:**
   - **Discord:** Configure webhook URL and message
   - **OR HTTP Request:** POST to notification webhook

3. **Connect:**
   - Edit Fields → Discord/Webhook

4. **Test:**
   - Verify notifications send

**Checkpoint:** Notifications work correctly

---

## Phase 3.7: Configuration - Credentials & Environment Variables

### Step 3.7.1: Configure n8n Credentials

**Credentials needed:**

1. **OpenAI API:**
   - Credentials → Add → OpenAI API
   - Enter your OpenAI API key
   - Save

2. **GitHub Personal Access Token:**
   - Credentials → Add → HTTP Header Auth
   - Header: `Authorization`
   - Value: `Bearer YOUR_GITHUB_TOKEN`
   - Save

3. **Netlify Auth Token (if using API):**
   - Credentials → Add → HTTP Header Auth
   - Header: `Authorization`
   - Value: `Bearer YOUR_NETLIFY_TOKEN`
   - Save

**Checkpoint:** All credentials configured

---

### Step 3.7.2: Set Environment Variables

**In n8n Settings → Environment Variables, add:**

```bash
UNITY_REPO_URL=https://github.com/rashadwest/BTEBallCODE.git
UNITY_PROJECT_PATH=/home/pi/Projects/BTEBallCODE
BUILD_OUTPUT_PATH=/home/pi/Builds/WebGL
WORKFLOW_PATH=/home/pi/workflows/BallCODE-Book
GITHUB_REPO_OWNER=rashadwest
GITHUB_REPO_NAME=BTEBallCODE
GITHUB_WORKFLOW_FILE=unity-webgl-build.yml
NETLIFY_SITE_ID=your-site-id-from-phase-1
NETLIFY_SITE_NAME=ballcode-game
GITHUB_ACTIONS_TOKEN=your-github-pat
NETLIFY_AUTH_TOKEN=your-netlify-token
```

**Checkpoint:** All environment variables set

---

## Testing Checklist

### Phase 3.1: Foundation
- [ ] Schedule Trigger fires
- [ ] Edit Fields outputs correct data

### Phase 3.2: AI Integration
- [ ] Basic LLM Chain receives input
- [ ] OpenAI Chat Model connected correctly
- [ ] AI analysis returns valid JSON
- [ ] Edit Fields parses response
- [ ] Filter routes correctly

### Phase 3.3: Git Operations
- [ ] Execute Command runs git operations
- [ ] Repository cloned/updated successfully

### Phase 3.4: Build Process
- [ ] HTTP Request triggers GitHub Actions
- [ ] Build starts successfully

### Phase 3.5: Deployment
- [ ] Netlify deployment triggered
- [ ] Site updates successfully

### Phase 3.6: Notifications
- [ ] Completion message created
- [ ] Notifications send successfully

---

## Troubleshooting n8n Issues

**⚠️ If you encounter ANY issues with n8n workflows, refer to:**

📖 **`N8N_WORKFLOW_DEVELOPMENT_GUIDE.md`** - Complete troubleshooting and debugging guide

This guide contains:
- ✅ Systematic debugging methodology (5-step process)
- ✅ Common patterns and solutions
- ✅ Expression evaluation fixes
- ✅ Field name handling
- ✅ Node configuration audits
- ✅ Data flow verification
- ✅ Workflow corrector tools (Python scripts)
- ✅ Best practices for n8n development

**When to use this guide:**
- Workflow doesn't execute
- Node connections fail
- Expression evaluation errors
- Data flow issues
- Credential problems
- Field name mismatches
- Complex expression failures

**Quick reference:** See the "Troubleshooting Guide" section in `N8N_WORKFLOW_DEVELOPMENT_GUIDE.md` for specific issues.

---

## Next Steps

Once Phase 3 is complete:
- ✅ Proceed to Phase 4: Testing & Validation
- ✅ Then Phase 5: Activate Continuous Running

---

**Copyright © 2025 Rashad West. All Rights Reserved.**

