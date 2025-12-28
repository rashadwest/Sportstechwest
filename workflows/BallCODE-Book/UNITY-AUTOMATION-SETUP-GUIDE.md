# Unity AI Automation - Complete Setup Guide
## Continuous Automated Workflow for Unity Development

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 2025  
**Status:** Complete Setup Guide  
**Purpose:** Set up fully automated Unity workflow running 24/7 on Raspberry Pi

---

## ✅ WHAT THIS DOES

This workflow automatically:
1. **Monitors for changes** (scheduled, webhook, or GitHub events)
2. **Clones/updates** Unity repository
3. **Makes AI-driven edits** to Unity project (if needed)
4. **Builds WebGL** version automatically
5. **Deploys to Netlify** automatically
6. **Sends notifications** when complete

**Runs continuously** on your Raspberry Pi n8n instance!

---

## 🎯 TRIGGER OPTIONS

### Option 1: Scheduled (Runs Automatically)
- **Every 6 hours** (configurable)
- Checks for changes and builds if needed
- Runs in background continuously

### Option 2: Webhook (Manual/API Trigger)
- Send POST request to trigger workflow
- Can be called from anywhere
- Perfect for integration with other systems

### Option 3: GitHub Webhook (Code Changes)
- Automatically triggers on code commits
- Monitors specific branches
- Builds immediately when code changes

---

## 📋 SETUP STEPS

### Step 1: Install Required Software on Raspberry Pi

```bash
# SSH into your Raspberry Pi
ssh pi@your-raspberry-pi-ip

# Update system
sudo apt update && sudo apt upgrade -y

# Install Git (if not already installed)
sudo apt install git -y

# Install Python 3 and pip
sudo apt install python3 python3-pip -y

# Install Node.js and npm (for Netlify CLI)
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# Install Netlify CLI
sudo npm install -g netlify-cli

# Install Unity (if building locally - optional)
# Note: Unity on Raspberry Pi requires special setup
# Recommended: Use GitHub Actions for builds instead
```

### Step 2: Clone Repository on Raspberry Pi

```bash
# Create projects directory
mkdir -p ~/Projects
cd ~/Projects

# Clone your Unity project repository
git clone https://github.com/rashadwest/BallCode.git BTEBallCODE

# Clone workflow repository (if not already there)
cd ~
git clone https://github.com/rashadwest/Sportstechwest.git workflows
cd workflows/BallCODE-Book
```

### Step 3: Configure Environment Variables

```bash
# Copy configuration template
cp unity-workflow-config.env unity-workflow-config.local.env

# Edit with your values
nano unity-workflow-config.local.env
```

**Fill in these values:**
```bash
# GitHub Configuration
export GITHUB_REPO_OWNER="rashadwest"
export GITHUB_REPO_NAME="BallCode"
export UNITY_REPO_URL="https://github.com/rashadwest/BallCode.git"

# Unity Project Paths (on Raspberry Pi)
export UNITY_PROJECT_PATH="/home/pi/Projects/BTEBallCODE"
export BUILD_OUTPUT_PATH="/home/pi/Builds/WebGL"
export WORKFLOW_PATH="/home/pi/workflows/BallCODE-Book"

# Netlify Configuration
export NETLIFY_SITE_NAME="ballcode-game"
export NETLIFY_SITE_ID="your-netlify-site-id"  # Get from Netlify dashboard
export NETLIFY_AUTH_TOKEN="your-netlify-auth-token"  # Generate in Netlify

# OpenAI API Key (for AI analysis)
export OPENAI_API_KEY="your-openai-api-key"

# GitHub Personal Access Token (for triggering builds)
export GITHUB_ACTIONS_TOKEN="your-github-pat"
```

**Get Netlify Site ID:**
1. Go to Netlify Dashboard
2. Select your site
3. Site settings → General → Site details
4. Copy "Site ID"

**Get Netlify Auth Token:**
1. Netlify Dashboard → User settings → Applications
2. New access token
3. Copy token

**Get GitHub Personal Access Token:**
1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Scopes: `repo`, `workflow`
4. Copy token

### Step 4: Make Scripts Executable

```bash
cd ~/workflows/BallCODE-Book

# Make scripts executable
chmod +x automate-unity-build.sh
chmod +x deploy-webgl-to-netlify.sh
chmod +x unity-ai-editor.py

# Install Python dependencies (if any)
pip3 install -r requirements.txt  # Create this if needed
```

### Step 5: Setup GitHub Actions

1. **Go to your GitHub repository:** `https://github.com/rashadwest/BallCode`

2. **Add Secrets:**
   - Settings → Secrets and variables → Actions
   - Add these secrets:
     - `NETLIFY_AUTH_TOKEN` - Your Netlify auth token
     - `NETLIFY_SITE_ID` - Your Netlify site ID
     - `NETLIFY_SITE_NAME` - Your Netlify site name (optional)
     - `UNITY_LICENSE` - Unity license (if using Unity Cloud Build)

3. **Verify workflow file exists:**
   - Check that `.github/workflows/unity-webgl-build.yml` exists
   - If not, copy it from this repository

### Step 6: Import n8n Workflow

1. **Open n8n on your Raspberry Pi:**
   - Usually: `http://raspberry-pi-ip:5678`

2. **Import workflow:**
   - Click "Workflows" → "Import from File"
   - Select `n8n-unity-automation-workflow.json`
   - Click "Import"

3. **Configure credentials in n8n:**
   
   **OpenAI API:**
   - Click "Credentials" → "Add Credential"
   - Select "OpenAI API"
   - Enter your OpenAI API key
   - Save as "OpenAI API"

   **GitHub Actions Token:**
   - Click "Credentials" → "Add Credential"
   - Select "HTTP Header Auth"
   - Header name: `Authorization`
   - Header value: `Bearer YOUR_GITHUB_TOKEN`
   - Save as "GitHub Actions Token"

   **Netlify API Token:**
   - Click "Credentials" → "Add Credential"
   - Select "HTTP Header Auth"
   - Header name: `Authorization`
   - Header value: `Bearer YOUR_NETLIFY_TOKEN`
   - Save as "Netlify API Token"

4. **Configure environment variables in n8n:**
   - Go to Settings → Environment Variables
   - Add all variables from `unity-workflow-config.local.env`
   - Or set them in each node that needs them

5. **Update workflow nodes:**
   - Open the imported workflow
   - Update each "Execute Command" node with correct paths
   - Update webhook URLs if needed
   - Test each node individually

### Step 7: Setup GitHub Webhook (Optional)

To trigger workflow automatically on code changes:

1. **Go to GitHub repository:**
   - Settings → Webhooks → Add webhook

2. **Webhook configuration:**
   - Payload URL: `http://your-raspberry-pi-ip:5678/webhook/github-webhook`
   - Content type: `application/json`
   - Events: Select "Just the push event"
   - Active: ✓

3. **Test webhook:**
   - Make a test commit
   - Check n8n workflow execution

### Step 8: Activate Workflow

1. **In n8n:**
   - Open your workflow
   - Click "Active" toggle (top right)
   - Workflow is now running!

2. **Test scheduled trigger:**
   - Wait for scheduled time (or change schedule to 1 minute for testing)
   - Check workflow executions

3. **Test webhook trigger:**
   ```bash
   curl -X POST http://your-raspberry-pi-ip:5678/webhook/unity-dev \
     -H "Content-Type: application/json" \
     -d '{"request": "Test build and deploy"}'
   ```

---

## 🔧 CONFIGURATION OPTIONS

### Change Schedule Frequency

In n8n workflow, edit "Scheduled Trigger" node:
- **Every hour:** `{ "field": "hours", "hoursInterval": 1 }`
- **Every 12 hours:** `{ "field": "hours", "hoursInterval": 12 }`
- **Every day at 2 AM:** Use cron: `0 2 * * *`
- **Every Monday at 9 AM:** Use cron: `0 9 * * 1`

### Use Local Builds vs GitHub Actions

**Option A: GitHub Actions (Recommended)**
- No Unity installation needed on Raspberry Pi
- Faster builds (cloud resources)
- Already configured in workflow

**Option B: Local Builds**
- Requires Unity installed on Raspberry Pi
- Edit workflow to use "Local Unity Build" node
- Slower but more control

### Notification Options

**Option 1: Webhook Notification**
- Set `WEBHOOK_NOTIFICATION_URL` in config
- Workflow will POST completion status

**Option 2: Email Notification**
- Add "Send Email" node in n8n
- Configure SMTP settings

**Option 3: Slack/Discord**
- Add "Slack" or "Discord" node in n8n
- Configure webhook URL

---

## 🧪 TESTING

### Test 1: Manual Webhook Trigger
```bash
curl -X POST http://your-raspberry-pi-ip:5678/webhook/unity-dev \
  -H "Content-Type: application/json" \
  -d '{
    "request": "Test automated build and deployment"
  }'
```

### Test 2: Scheduled Trigger
- Change schedule to run every 1 minute
- Wait and check workflow executions
- Verify it runs automatically

### Test 3: GitHub Webhook
- Make a test commit to repository
- Check if workflow triggers automatically
- Verify build and deployment

---

## 📊 MONITORING

### Check Workflow Status

1. **In n8n:**
   - Go to "Executions" tab
   - See all workflow runs
   - Check for errors

2. **Check logs:**
   ```bash
   # On Raspberry Pi
   tail -f ~/.n8n/logs/n8n.log
   ```

3. **Check build status:**
   - GitHub Actions: `https://github.com/rashadwest/BallCode/actions`
   - Netlify: Netlify Dashboard → Deploys

### Common Issues

**Issue: Workflow not triggering**
- Check if workflow is "Active" in n8n
- Verify webhook URLs are correct
- Check n8n logs for errors

**Issue: Build fails**
- Check GitHub Actions logs
- Verify Unity project structure
- Check Unity version compatibility

**Issue: Deployment fails**
- Verify Netlify credentials
- Check Netlify site ID
- Verify build output exists

---

## 🚀 USAGE EXAMPLES

### Example 1: Manual Trigger via API
```bash
# Trigger workflow with specific request
curl -X POST http://your-raspberry-pi-ip:5678/webhook/unity-dev \
  -H "Content-Type: application/json" \
  -d '{
    "request": "Add new enemy type to level 1"
  }'
```

### Example 2: Trigger from Another Script
```python
import requests

response = requests.post(
    'http://your-raspberry-pi-ip:5678/webhook/unity-dev',
    json={'request': 'Update game difficulty settings'}
)
print(response.json())
```

### Example 3: Trigger from GitHub Actions
```yaml
# In another workflow
- name: Trigger Unity Build
  uses: actions/github-script@v7
  with:
    script: |
      await github.request('POST /repos/rashadwest/BallCode/dispatches', {
        event_type: 'unity-build',
        client_payload: { request: 'Automated build from CI' }
      })
```

---

## ✅ VERIFICATION CHECKLIST

- [ ] n8n running on Raspberry Pi
- [ ] Workflow imported and activated
- [ ] All credentials configured in n8n
- [ ] Environment variables set
- [ ] GitHub Actions workflow file exists
- [ ] GitHub secrets configured
- [ ] Netlify credentials configured
- [ ] Scripts are executable
- [ ] Test webhook trigger works
- [ ] Test scheduled trigger works
- [ ] Test GitHub webhook works
- [ ] Build completes successfully
- [ ] Deployment completes successfully
- [ ] Notifications working

---

## 🎯 NEXT STEPS

1. **Monitor first few runs** - Watch for any errors
2. **Adjust schedule** - Set to your preferred frequency
3. **Add notifications** - Configure email/Slack/Discord
4. **Optimize** - Fine-tune based on your needs
5. **Document** - Keep notes on what works best

---

## 📚 ADDITIONAL RESOURCES

- **n8n Documentation:** https://docs.n8n.io
- **GitHub Actions:** https://docs.github.com/en/actions
- **Netlify CLI:** https://docs.netlify.com/cli/get-started/
- **Unity Build Automation:** https://docs.unity.com/ugs/en-us/manual/devops

---

**Copyright © 2025 Rashad West. All Rights Reserved.**






