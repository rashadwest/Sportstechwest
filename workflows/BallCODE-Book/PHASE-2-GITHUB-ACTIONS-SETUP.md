# Phase 2: GitHub Actions Workflow Setup
## Verify/Create GitHub Actions Workflow for Automated Builds

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Purpose:** Set up GitHub Actions to automatically build Unity WebGL and deploy to Netlify  
**Repository:** `rashadwest/BTEBallCODE`  
**Status:** Ready to verify/create

---

## Step 2.1: Check if Workflow File Exists

**File Location:** `.github/workflows/unity-webgl-build.yml` in BTEBallCODE repository

### Check Locally (If Repository Cloned)

```bash
cd /path/to/BTEBallCODE
ls -la .github/workflows/unity-webgl-build.yml
```

### Check on GitHub

1. Go to: https://github.com/rashadwest/BTEBallCODE
2. Navigate to: `.github/workflows/` folder
3. Look for: `unity-webgl-build.yml`

**If file exists:** Proceed to Step 2.2 (Verify Configuration)  
**If file doesn't exist:** Proceed to Step 2.3 (Create Workflow)

---

## Step 2.2: Verify Existing Workflow Configuration

**If workflow file exists, verify:**

1. **Workflow triggers correctly:**
   - `workflow_dispatch` (manual trigger)
   - `repository_dispatch` (for n8n triggering)
   - `push` on main branch

2. **Secrets are referenced:**
   - `NETLIFY_AUTH_TOKEN`
   - `NETLIFY_SITE_ID`
   - `NETLIFY_SITE_NAME` (optional)

3. **Unity version matches:**
   - Check `unityVersion: 2021.3.15f1` (or your Unity version)

4. **Build path is correct:**
   - `buildsPath: Builds/WebGL`

**Checkpoint:** Workflow file exists and is properly configured

---

## Step 2.3: Create Workflow File (If Not Exists)

**If workflow doesn't exist, create it:**

### Option A: Create via GitHub Web Interface

1. **Go to Repository:**
   - https://github.com/rashadwest/BTEBallCODE

2. **Create Workflow File:**
   - Click "Add file" → "Create new file"
   - Path: `.github/workflows/unity-webgl-build.yml`
   - Copy the workflow content (see below)

3. **Commit:**
   - Commit message: "Add Unity WebGL build and deploy workflow"
   - Click "Commit new file"

### Option B: Create Locally and Push

1. **Create Directory:**
   ```bash
   cd /path/to/BTEBallCODE
   mkdir -p .github/workflows
   ```

2. **Create Workflow File:**
   ```bash
   # Copy workflow content to .github/workflows/unity-webgl-build.yml
   ```

3. **Commit and Push:**
   ```bash
   git add .github/workflows/unity-webgl-build.yml
   git commit -m "Add Unity WebGL build and deploy workflow"
   git push origin main
   ```

---

## Workflow File Content

**File:** `.github/workflows/unity-webgl-build.yml`

```yaml
name: Unity WebGL Build and Deploy

on:
  workflow_dispatch:  # Manual trigger
  repository_dispatch:  # Triggered by n8n
    types: [unity-build]
  push:
    branches: [ main ]
    paths:
      - 'Unity-Scripts/**'
      - 'Assets/**'
      - 'ProjectSettings/**'
      - '.github/workflows/unity-webgl-build.yml'

jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    
    steps:
    - name: Checkout repository
      uses: actions/checkout@v4
      with:
        fetch-depth: 0
        
    - name: Cache Unity Library
      uses: actions/cache@v3
      with:
        path: Library
        key: Library-${{ runner.os }}-${{ hashFiles('Assets/**', 'Packages/**', 'ProjectSettings/**') }}
        restore-keys: |
          Library-${{ runner.os }}-
          
    - name: Setup Unity
      uses: game-ci/unity-setup@v1
      with:
        unityVersion: 2021.3.15f1
        
    - name: Build Unity WebGL
      uses: game-ci/unity-builder@v4
      env:
        UNITY_LICENSE: ${{ secrets.UNITY_LICENSE }}
      with:
        targetPlatform: WebGL
        buildName: BallCODE-WebGL
        buildsPath: Builds/WebGL
        buildMethod: Custom
        customBuildPath: Assets/Editor/BuildScript.cs
        
    - name: Upload build artifacts
      uses: actions/upload-artifact@v4
      with:
        name: webgl-build
        path: Builds/WebGL
        retention-days: 7
        
    - name: Deploy to Netlify
      uses: nwtgck/actions-netlify@v2.0
      with:
        publish-dir: './Builds/WebGL'
        production-deploy: true
        github-token: ${{ secrets.GITHUB_TOKEN }}
        deploy-message: "Deploy from GitHub Actions - ${{ github.event.head_commit.message || 'Automated build' }}"
        enable-pull-request-comment: false
        enable-commit-comment: false
      env:
        NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
        NETLIFY_SITE_ID: ${{ secrets.NETLIFY_SITE_ID }}
      continue-on-error: false
      
    - name: Notify completion
      if: always()
      uses: actions/github-script@v7
      with:
        script: |
          const status = '${{ job.status }}' === 'success' ? '✅ Success' : '❌ Failed';
          const message = `Unity WebGL Build ${status}\n\nSite: https://${{ secrets.NETLIFY_SITE_NAME || 'ballcode-game' }}.netlify.app\nCommit: ${{ github.sha }}\nTriggered by: ${{ github.event_name }}`;
          
          console.log(message);
```

**Note:** Adjust `unityVersion` to match your Unity project version if different.

---

## Step 2.4: Verify Secrets Are Configured

**From Phase 1, verify these secrets exist:**

1. **Go to Repository Settings:**
   - https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions

2. **Verify Secrets:**
   - [ ] `NETLIFY_AUTH_TOKEN` - Exists
   - [ ] `NETLIFY_SITE_ID` - Exists
   - [ ] `NETLIFY_SITE_NAME` - Exists (optional)

3. **Add UNITY_LICENSE (If Needed):**
   - If using Unity Cloud Build, add `UNITY_LICENSE` secret
   - Otherwise, workflow may use Unity Personal license

**Checkpoint:** All required secrets are configured

---

## Step 2.5: Test Workflow

**Test the workflow manually:**

1. **Go to Actions Tab:**
   - https://github.com/rashadwest/BTEBallCODE/actions

2. **Select Workflow:**
   - Click "Unity WebGL Build and Deploy"

3. **Run Workflow:**
   - Click "Run workflow" button
   - Select branch: `main`
   - Click "Run workflow"

4. **Monitor Execution:**
   - Watch workflow run
   - Check each step completes
   - Verify build succeeds
   - Verify deployment to Netlify succeeds

**Checkpoint:** Workflow runs successfully end-to-end

---

## Verification Checklist

- [ ] Workflow file exists at `.github/workflows/unity-webgl-build.yml`
- [ ] Workflow triggers configured (workflow_dispatch, repository_dispatch, push)
- [ ] Unity version matches project
- [ ] Build path is correct (`Builds/WebGL`)
- [ ] `NETLIFY_AUTH_TOKEN` secret exists
- [ ] `NETLIFY_SITE_ID` secret exists
- [ ] `NETLIFY_SITE_NAME` secret exists (optional)
- [ ] Workflow test run succeeds
- [ ] Build completes successfully
- [ ] Deployment to Netlify completes successfully

---

## Troubleshooting

### Workflow Not Appearing
- Check file is in `.github/workflows/` folder
- Verify file has `.yml` or `.yaml` extension
- Check file is committed to repository

### Build Fails
- Check Unity version compatibility
- Verify `UNITY_LICENSE` secret if required
- Check build logs for specific errors

### Deployment Fails
- Verify Netlify secrets are correct
- Check Site ID matches your Netlify site
- Verify build output exists at `Builds/WebGL`

### Secrets Not Found
- Double-check secret names match exactly
- Verify secrets are in correct repository
- Check you're looking at "Actions" secrets, not "Dependabot"

---

## Next Steps

Once Phase 2 is complete:
- ✅ Proceed to Phase 3: n8n Workflow Build
- ✅ Workflow is ready to be triggered by n8n

---

**Copyright © 2025 Rashad West. All Rights Reserved.**


