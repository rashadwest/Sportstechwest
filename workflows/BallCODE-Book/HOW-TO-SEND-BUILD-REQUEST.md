# How to Send Build Request to Your Workflow
## ELI10: Make Your Workflow Build the Game

**Date:** December 11, 2025

---

## 🎯 THE PROBLEM

When you click "Execute Workflow", it says "Workflow executed successfully" but doesn't ask you anything.

**Why:** The workflow is running, but it's using the **Scheduled Trigger** path, which has no input. It just runs with default "scheduled" data.

---

## ✅ THE SOLUTION: Use the Webhook Trigger

You need to send your build request to the **Webhook Trigger** node, not just execute the workflow directly.

---

## 📋 STEP-BY-STEP (Super Simple)

### Step 1: Get Your Webhook URL

1. Open your n8n workflow at: http://192.168.1.226:5678
2. Click on the **"Webhook Trigger (Manual/API)1"** node
3. Look for the **"Webhook URL"** - it will look like:
   ```
   http://192.168.1.226:5678/webhook/unity-dev
   ```
4. **Copy that URL**

---

### Step 2: Send the Build Request

**Option A: Using Terminal (Easiest)**

Open Terminal on your Mac and run:

```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-dev \
  -H "Content-Type: application/json" \
  -d @~/Desktop/build-request-ballcode-game.json
```

**What this does:**
- Sends a POST request (like clicking a button)
- To your webhook URL
- With the build request data from Desktop

**Option B: Using a Web Browser Tool**

1. Install a browser extension like "REST Client" or use Postman
2. Set method to: **POST**
3. URL: `http://192.168.1.226:5678/webhook/unity-dev`
4. Body: Copy contents of `build-request-ballcode-game.json`
5. Click Send

---

### Step 3: Watch It Work!

After sending the request:
1. Go back to n8n
2. You'll see the workflow running
3. Click on each node to see what it's doing
4. The "AI Analyze Request" node will see your build request
5. It will create an action plan
6. Then it will build your game!

---

## 🔍 HOW TO CHECK IF IT WORKED

### Check the "Normalize Input1" Node:
- Click on it
- Look at the OUTPUT
- Should show: `request: "Build BallCode game with organized level structure..."`
- NOT: `request: "Automated build from scheduled trigger"`

### Check the "Parse AI Response1" Node:
- Click on it
- Look at the OUTPUT
- Should show: `actionPlan` with `needsBuild: true`, `needsDeploy: true`

### Check the "Compile Completion Report" Node:
- Click on it
- Look at the OUTPUT
- Should show: `status: "success"` and `siteUrl: "https://ballcode-game.netlify.app"`

---

## 🎯 QUICK TEST

**To test if webhook is working:**

```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-dev \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build request", "triggerType": "webhook"}'
```

Then check the "Normalize Input1" node output - it should show `request: "Test build request"` instead of the default scheduled message.

---

## 📝 SUMMARY

**The Problem:**
- Clicking "Execute Workflow" uses Scheduled Trigger (no input)
- Workflow runs but doesn't know what to build

**The Solution:**
- Send POST request to Webhook URL with build request
- Workflow receives your request and builds the game

**The Command:**
```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-dev \
  -H "Content-Type: application/json" \
  -d @~/Desktop/build-request-ballcode-game.json
```

---

**That's it!** Send the request, and your workflow will build the game! 🚀


