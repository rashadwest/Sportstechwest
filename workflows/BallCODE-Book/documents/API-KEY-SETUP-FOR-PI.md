# 🔑 API Key Setup for Pi n8n CLI Access

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** January 2025  
**Purpose:** Complete guide to set up n8n API key for CLI access on new Pi

---

## 🎯 THE PROBLEM

Your CLI scripts can't access the Pi n8n because:

1. **No API Key Configured**: The `.n8n-env` file has `N8N_API_KEY=""` (empty)
2. **Wrong URL**: `.n8n-env` points to `localhost:5678` instead of the Pi at `192.168.1.226:5678`
3. **API Key Not Created**: You need to create an API key in the Pi n8n UI first

---

## ✅ THE SOLUTION (3 Steps)

### Step 1: Get API Key from Pi n8n UI

1. **Open Pi n8n in browser:**
   ```
   http://192.168.1.226:5678
   ```

2. **Navigate to API Settings:**
   - Click **"Settings"** (gear icon, top-right or left sidebar)
   - Click **"API"** in the left sidebar
   - Click **"Create API Key"** button

3. **Copy the API Key:**
   - The key will look like: `n8n_api_xxxxxxxxxxxxx`
   - ⚠️ **IMPORTANT:** Copy it immediately - you won't see it again!

---

### Step 2: Run the Setup Script (Easiest Method)

```bash
./scripts/setup-pi-api-key.sh
```

This script will:
- ✅ Test connection to Pi n8n
- ✅ Guide you through getting the API key
- ✅ Test the API key validity
- ✅ Save it to `.n8n-env.pi`
- ✅ Update your active `.n8n-env` profile

---

### Step 3: Manual Setup (Alternative)

If you prefer to do it manually:

#### Option A: Update `.n8n-env.pi` directly

```bash
# Edit the file
nano .n8n-env.pi

# Update these lines:
export N8N_URL="http://192.168.1.226:5678"
export N8N_API_KEY="YOUR_API_KEY_HERE"
```

#### Option B: Use the setup script to switch profiles

```bash
# This will copy .n8n-env.pi to .n8n-env
./setup-n8n-terminal.sh pi
```

---

## 🧪 TESTING

After setup, test CLI access:

```bash
# Source the environment
source .n8n-env.pi

# Test API access
curl -H "X-N8N-API-KEY: $N8N_API_KEY" \
     -H "Content-Type: application/json" \
     http://192.168.1.226:5678/api/v1/workflows
```

You should see a JSON response with your workflows.

---

## 📋 WHAT EACH FILE DOES

### `.n8n-env.pi`
- **Purpose:** Configuration for Pi n8n (production)
- **Contains:** Pi URL, API key, workflow settings
- **When used:** When you run `./setup-n8n-terminal.sh pi`

### `.n8n-env`
- **Purpose:** Active configuration (currently in use)
- **Contains:** Either Pi or local Mac settings
- **When used:** Sourced by all CLI scripts

### `.n8n-env.local`
- **Purpose:** Configuration for Mac localhost n8n (testing)
- **Contains:** localhost URL, API key (if needed)
- **When used:** When you run `./setup-n8n-terminal.sh local`

---

## 🚀 USING CLI AFTER SETUP

Once the API key is set, you can use all CLI commands:

```bash
# Import workflow
./scripts/import-orchestrator-cli.sh

# Deploy workflow
./deploy-n8n-workflow.sh workflow.json

# List workflows
./n8n-list-workflows.sh

# Edit workflow
./n8n-edit-workflow.sh WORKFLOW_ID
```

---

## 🔍 TROUBLESHOOTING

### Problem: "No API key found"
**Solution:** Run `./scripts/setup-pi-api-key.sh` to set it up

### Problem: "Cannot connect to n8n"
**Solution:** 
1. Check Pi is powered on
2. Verify IP: `ping 192.168.1.226`
3. Check n8n is running: `curl http://192.168.1.226:5678/healthz`

### Problem: "API key is invalid (HTTP 401)"
**Solution:**
1. Verify you copied the entire API key
2. Check the key was created in the Pi n8n instance (not Mac)
3. Create a new API key and try again

### Problem: "Wrong n8n instance"
**Solution:**
```bash
# Switch to Pi profile
./setup-n8n-terminal.sh pi

# Or manually update .n8n-env
export N8N_URL="http://192.168.1.226:5678"
```

---

## 📝 QUICK REFERENCE

| Task | Command |
|------|---------|
| Setup API key | `./scripts/setup-pi-api-key.sh` |
| Switch to Pi profile | `./setup-n8n-terminal.sh pi` |
| Switch to Mac profile | `./setup-n8n-terminal.sh local` |
| Test API connection | `curl -H "X-N8N-API-KEY: $N8N_API_KEY" $N8N_URL/api/v1/workflows` |
| Import workflow | `./scripts/import-orchestrator-cli.sh` |

---

## ✅ CHECKLIST

- [ ] Pi n8n is accessible at `http://192.168.1.226:5678`
- [ ] API key created in Pi n8n UI (Settings → API → Create API Key)
- [ ] API key saved to `.n8n-env.pi`
- [ ] `.n8n-env` points to Pi (or run `./setup-n8n-terminal.sh pi`)
- [ ] API key tested and working
- [ ] CLI scripts can access Pi n8n

---

## 🎯 WHY THIS IS HARD

The API setup is tricky because:

1. **API Key is Hidden**: Once created, you can't see it again - must copy immediately
2. **Multiple Config Files**: `.n8n-env`, `.n8n-env.pi`, `.n8n-env.local` can be confusing
3. **Profile Switching**: Need to remember which profile is active
4. **No Default API Key**: n8n doesn't create one automatically - you must do it manually

**The setup script (`setup-pi-api-key.sh`) solves all of this!** 🎉

---

## 📞 NEXT STEPS

After API key is set:

1. **Test import:**
   ```bash
   ./scripts/import-orchestrator-cli.sh
   ```

2. **Deploy workflows:**
   ```bash
   ./deploy-n8n-workflow.sh your-workflow.json
   ```

3. **Use CLI for all n8n operations** - no more UI needed! 🚀

---

**Need help?** Check the script output - it provides detailed error messages and troubleshooting tips.

