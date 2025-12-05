# Phase 1: Netlify Site Setup Guide
## One-Time Manual Setup to Establish Netlify Site

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Purpose:** Create Netlify site manually to get credentials for automation  
**Time:** 15-20 minutes  
**Status:** Manual steps required

---

## Step 1.1: Clone Unity Repository (If Not Already)

**Location:** Your local machine or Raspberry Pi

```bash
# Clone the Unity repository
git clone https://github.com/rashadwest/BTEBallCODE.git
cd BTEBallCODE
```

**Checkpoint:** Repository cloned locally

---

## Step 1.2: Build Unity Project to WebGL (Manual First Time)

**Purpose:** Create WebGL build files for deployment

### Option A: Build in Unity Editor

1. **Open Unity Project:**
   - Open Unity Hub
   - Open the BTEBallCODE project

2. **Configure Build Settings:**
   - File → Build Settings
   - Select **WebGL** platform
   - Click "Switch Platform" (if needed)

3. **Player Settings:**
   - Click "Player Settings"
   - Configure:
     - **Company Name:** Your company
     - **Product Name:** BallCODE Game
     - **WebGL Settings:**
       - Compression: **Gzip** (recommended)
       - Data Caching: **Enabled**
       - Memory Size: **256MB** (or adjust if needed)

4. **Build:**
   - Click "Build"
   - Choose folder: `Builds/WebGL/` (create if doesn't exist)
   - Wait for build (5-10 minutes depending on project size)

**Checkpoint:** WebGL build created in `Builds/WebGL/` folder

### Option B: Use Automated Build Script

If you have Unity CLI available:

```bash
cd /path/to/BTEBallCODE
/path/to/automate-unity-build.sh /path/to/BTEBallCODE
```

**Checkpoint:** Build folder contains:
- `index.html`
- `Build/` folder (with .wasm, .js, .data files)
- Other WebGL files

---

## Step 1.3: Deploy to Netlify Manually

**Purpose:** Create Netlify site and get credentials

1. **Go to Netlify:**
   - Open: https://app.netlify.com
   - Sign in to your account

2. **Create New Site:**
   - Click "Add new site" (top right)
   - Select "Deploy manually"

3. **Upload Build Files:**
   - Drag and drop the `Builds/WebGL/` folder
   - OR click "Browse to upload" and select the folder
   - Wait for upload to complete

4. **Site Created:**
   - Netlify will create a site with a random name
   - Example: `random-name-12345.netlify.app`
   - Note the site URL

**Checkpoint:** Netlify site created and accessible

---

## Step 1.4: Get Netlify Credentials

### Get Site ID

1. **In Netlify Dashboard:**
   - Click on your newly created site
   - Click "Site settings" (gear icon or in top menu)

2. **Navigate to General:**
   - Click "General" in left sidebar
   - Scroll to "Site details" section

3. **Copy Site ID:**
   - Find "Site ID" (long alphanumeric string)
   - Example: `a1b2c3d4-e5f6-7890-abcd-ef1234567890`
   - Copy this value

**Checkpoint:** Site ID copied

### Generate Access Token

1. **Go to User Settings:**
   - Click your profile/account (bottom left: "R Rashad West")
   - OR go directly to: https://app.netlify.com/user/applications

2. **Create New Token:**
   - Click "New access token"
   - Name: "Unity Automation" (or any descriptive name)
   - Click "Generate token"

3. **Copy Token:**
   - **IMPORTANT:** Copy the token immediately
   - You won't be able to see it again
   - Save it securely

**Checkpoint:** Access token generated and saved

### Note Site Name/URL

- Site URL: `https://your-site-name.netlify.app`
- Site Name: The name Netlify assigned (or you can rename it)

**Checkpoint:** Site information noted

---

## Step 1.5: Add Credentials to GitHub Secrets

**Purpose:** Store Netlify credentials securely for GitHub Actions

1. **Go to GitHub Repository:**
   - Navigate to: https://github.com/rashadwest/BTEBallCODE
   - Click "Settings" tab

2. **Navigate to Secrets:**
   - Left sidebar: "Secrets and variables" → "Actions"
   - Click "Secrets" tab (not "Variables")

3. **Add NETLIFY_AUTH_TOKEN:**
   - Click "New repository secret"
   - Name: `NETLIFY_AUTH_TOKEN`
   - Value: (paste your Netlify access token from Step 1.4)
   - Click "Add secret"

4. **Add NETLIFY_SITE_ID:**
   - Click "New repository secret" again
   - Name: `NETLIFY_SITE_ID`
   - Value: (paste your Site ID from Step 1.4)
   - Click "Add secret"

5. **Add NETLIFY_SITE_NAME (Optional):**
   - Click "New repository secret" again
   - Name: `NETLIFY_SITE_NAME`
   - Value: (your site name, e.g., `ballcode-game`)
   - Click "Add secret"

**Checkpoint:** All Netlify credentials added to GitHub Secrets

---

## Verification Checklist

- [ ] Unity repository cloned locally
- [ ] WebGL build created successfully
- [ ] Build folder contains `index.html` and `Build/` folder
- [ ] Netlify site created and accessible
- [ ] Site ID copied
- [ ] Access token generated and saved
- [ ] Site name/URL noted
- [ ] `NETLIFY_AUTH_TOKEN` added to GitHub Secrets
- [ ] `NETLIFY_SITE_ID` added to GitHub Secrets
- [ ] `NETLIFY_SITE_NAME` added to GitHub Secrets (optional)

---

## Next Steps

Once Phase 1 is complete:
- ✅ Proceed to Phase 2: GitHub Actions Workflow Setup
- ✅ Then Phase 3: n8n Workflow Build

---

## Troubleshooting

### Build Fails
- Check Unity version compatibility
- Verify WebGL build target is selected
- Check Unity console for errors

### Netlify Upload Fails
- Verify build folder structure is correct
- Check file sizes (Netlify has limits)
- Try uploading individual files if folder is too large

### Can't Find Site ID
- Make sure you're in Site settings → General
- Scroll down to "Site details" section
- Site ID is a long string, not the site name

### Token Not Working
- Verify token was copied correctly
- Check token hasn't expired
- Generate a new token if needed

---

**Copyright © 2025 Rashad West. All Rights Reserved.**

