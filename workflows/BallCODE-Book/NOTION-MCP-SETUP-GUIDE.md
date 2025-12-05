# Notion MCP Setup Guide for Cursor

**Purpose:** Set up Notion MCP server in Cursor to sync daily workflow files to your Notion workspace.

---

## 🚀 Quick Setup Steps

### Step 1: Get Notion Integration Token

1. Go to [Notion Integrations](https://www.notion.so/my-integrations)
2. Click **"+ New integration"**
3. Name it: **"Cursor MCP Integration"**
4. Select your workspace
5. Set capabilities:
   - ✅ **Read content**
   - ✅ **Insert content**
   - ✅ **Update content**
6. Click **"Submit"**
7. **Copy the "Internal Integration Token"** (starts with `secret_`)

### Step 2: Share Pages/Databases with Integration

1. In Notion, go to the page/database you want to use
2. Click **"..."** (three dots) → **"Connections"**
3. Search for **"Cursor MCP Integration"**
4. Click to connect it
5. Repeat for any pages/databases you want to access

### Step 3: Configure MCP in Cursor

**Option A: Using Cursor Settings (if available)**

1. Open Cursor Settings (Cmd/Ctrl + ,)
2. Search for "MCP" or "Model Context Protocol"
3. Add new MCP server:
   - **Name:** `notion`
   - **Command:** `npx -y @modelcontextprotocol/server-notion`
   - **Environment Variables:**
     - `NOTION_API_KEY`: Your integration token from Step 1

**Option B: Manual Configuration File**

Create or edit `~/.cursor/mcp.json` (or Cursor's MCP config location):

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-notion"
      ],
      "env": {
        "NOTION_API_KEY": "your-secret-token-here"
      }
    }
  }
}
```

**Option C: Using Notion's Official MCP**

According to Notion's documentation, the official MCP URL is:
- **URL:** `https://mcp.notion.com/mcp`

You may need to configure OAuth through Notion's settings:
1. Go to Notion → Settings → Connections
2. Select "Notion MCP"
3. Complete OAuth flow

---

## ✅ Verify Setup

Once configured, test the connection by asking in Cursor:

```
Can you list my Notion databases using Notion MCP?
```

If it works, you'll see your databases listed.

---

## 📋 Commands to Sync Daily Workflow to Notion

### Command 1: Create Daily Productivity Database

```
Use Notion MCP to create a new database with these properties:

Database Name: "Daily Productivity System"

Properties:
- Date (Date) - Primary date field
- ONE System Focus (Text) - What system/process am I focusing on?
- Deep Work Window (Text) - Start and end times
- ONE Domino (Text) - The ONE task that makes everything easier
- Domino Why (Text) - Why this domino matters
- Context Type (Select): Finance/Admin, Creative/Content, Technical/Development, Communication, Review/Planning
- Energy Level (Number) - 1-10 scale
- Focus Time Target (Number) - Hours
- Focus Time Actual (Number) - Hours achieved
- Context Switches (Number) - Actual switches (target ≤3)
- Delegations Created (Number) - Number of tasks delegated
- Domino Status (Select): Not Started, In Progress, Completed
- Reflection Notes (Text) - What worked, what didn't, what to change
- Tomorrow Domino (Text) - Next day's ONE domino

Return the database ID and URL.
```

### Command 2: Create Daily Workflow Template Page

```
Use Notion MCP to create a new page in the "Daily Productivity System" database with:

Title: "Daily Workflow Template"
Date: [Today's date]

Then add this content structure:

# Daily Workflow Template

## 🚨 PRE-WORK CHECKLIST

### 1️⃣ Orchestrate — Don't Multitask
- [ ] What ONE system/process am I focusing on today?
- [ ] What is the ownership structure?
- [ ] What automation is in place?
- [ ] What accountability exists?

### 2️⃣ Protect Deep Work Windows
- [ ] When is my 2-3 hour Deep Work window today?
- [ ] Have I blocked this time?
- [ ] What distractions will I eliminate?

### 3️⃣ Batch Similar Contexts
- [ ] What context blocks have I planned today?
- [ ] How many context switches am I planning? (Target: ≤3)

### 4️⃣ Delegate with Context
- [ ] What am I delegating today?
  - Task 1: Goal, Metric, Escalation
  - Task 2: Goal, Metric, Escalation
  - Task 3: Goal, Metric, Escalation

### 5️⃣ Use If–Then Rules
- [ ] What automated behaviors am I using today?

### 6️⃣ Track Your Metrics Daily
- [ ] Focus Time Target: ___ hours
- [ ] Delegations Created Target: ___
- [ ] Context Switches Target: ≤ ___

### 7️⃣ Automate for Clarity
- [ ] What repetitive work am I automating?
- [ ] What am I reserving my time for?

### 8️⃣ Move One Domino a Day
- [ ] What is the ONE task today?
- [ ] Why is this the domino?
- [ ] When will I complete it?

### 9️⃣ Audit Systems Weekly
- [ ] Is today an audit day?
- [ ] What systems need review?

### 🔟 Protect Energy Like a KPI
- [ ] What is my energy level right now? (1-10)
- [ ] What rest/reset do I need?

## 📋 DAILY EXECUTION LOG

### Deep Work Window Results
- Actual Start: ___
- Actual End: ___
- Focus Time Achieved: ___ hours
- What was accomplished: ___

### Context Blocks Completed
- [ ] Finance Block
- [ ] Creative/Marketing Block
- [ ] Technical/Development Block
- [ ] Communication Block
- [ ] Review/Planning Block

### ONE Domino Status
- [ ] ✅ COMPLETED
- [ ] ⏳ IN PROGRESS
- [ ] ❌ NOT STARTED
- Impact: ___

## 📊 END OF DAY METRICS

### Focus Time
- Target: ___ hours
- Actual: ___ hours
- Gap: ___

### Delegations Created
- Target: ___
- Actual: ___
- Gap: ___

### Context Switches
- Target: ≤ ___
- Actual: ___
- Gap: ___

### Energy Level
- Morning: ___ /10
- Afternoon: ___ /10
- Evening: ___ /10

### Reflection Notes
- What worked well? ___
- What didn't work? ___
- What will I change tomorrow? ___

## 🎯 TOMORROW'S PREVIEW

### Tomorrow's ONE Domino
- Task: ___
- Why it matters: ___

### Tomorrow's Deep Work Window
- Time: ___ to ___
- Focus: ___

Return the page URL.
```

### Command 3: Create Today's Daily Entry

```
Use Notion MCP to create a new page in the "Daily Productivity System" database with:

Title: "Daily Workflow - [Today's Date]"
Date: [Today's date]
ONE System Focus: [Your answer]
Deep Work Window: [Start time] to [End time]
ONE Domino: [Your ONE domino task]
Context Type: [Selected from options]
Energy Level: [1-10]

Then copy the template structure from the "Daily Workflow Template" page and fill in today's details.
```

### Command 4: Update Daily Entry with End-of-Day Metrics

```
Use Notion MCP to update the page "Daily Workflow - [Today's Date]" in the "Daily Productivity System" database:

Update these properties:
- Focus Time Actual: [Hours achieved]
- Context Switches: [Actual number]
- Delegations Created: [Number created]
- Domino Status: [Not Started/In Progress/Completed]

Then update the "Reflection Notes" section with:
- What worked well: [Your notes]
- What didn't work: [Your notes]
- What will I change tomorrow: [Your notes]
```

---

## 🔄 Daily Workflow Sync Process

### Morning Routine
1. Run **Command 3** to create today's entry
2. Fill in pre-work checklist
3. Set your ONE domino and metrics

### End of Day Routine
1. Run **Command 4** to update today's entry
2. Fill in end-of-day metrics
3. Add reflection notes
4. Set tomorrow's domino

---

## 📚 Additional Resources

- **Notion MCP Documentation:** https://developers.notion.com/docs/mcp
- **Notion API Documentation:** https://developers.notion.com/reference
- **Your Local Files:**
  - `START-HERE-DAILY-WORKFLOW.md` - Quick start template
  - `DAILY-WORKFLOW-TEMPLATE.md` - Complete checklist
  - `PRE-WORK-QUESTIONNAIRE.md` - Detailed questionnaire

---

## 🎯 Next Steps

1. **Set up Notion MCP** using Step 1-3 above
2. **Create the database** using Command 1
3. **Create the template** using Command 2
4. **Start using it daily** with Commands 3-4

---

**Note:** If you encounter issues with MCP setup, you can also use the Notion API directly with Python scripts, or use third-party tools like MarkFlow or mk-notes for Markdown-to-Notion syncing.



