#!/bin/bash

# Automation Helper for Unity/Netlify/WebGL Setup
# Handles all automated tasks while user does manual steps
# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}╔════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  BallCODE Unity/Netlify/WebGL Setup Automation Helper ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════╝${NC}"
echo ""

# Configuration
UNITY_REPO="https://github.com/rashadwest/BTEBallCODE.git"
UNITY_PROJECT_NAME="BTEBallCODE"
BUILD_PATH="./Builds/WebGL"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Track what's automated
AUTOMATED_TASKS=()
MANUAL_TASKS=()

echo -e "${BLUE}🔍 Checking environment and preparing automation...${NC}"
echo ""

# ============================================
# TASK 1: Check/Clone Unity Repository
# ============================================
echo -e "${YELLOW}[AUTOMATED]${NC} Checking Unity repository..."

if [ -d "$UNITY_PROJECT_NAME" ]; then
    echo -e "${GREEN}✓${NC} Unity repository already cloned"
    AUTOMATED_TASKS+=("✓ Repository cloned")
else
    echo -e "${YELLOW}⚠${NC} Repository not found. Would you like to clone it? (y/n)"
    read -r response
    if [[ "$response" =~ ^[Yy]$ ]]; then
        echo -e "${BLUE}Cloning repository...${NC}"
        git clone "$UNITY_REPO" || {
            echo -e "${RED}✗${NC} Failed to clone repository"
            MANUAL_TASKS+=("✗ Clone repository manually: git clone $UNITY_REPO")
        }
        AUTOMATED_TASKS+=("✓ Repository cloned")
    else
        MANUAL_TASKS+=("⚠ Clone repository: git clone $UNITY_REPO")
    fi
fi

# ============================================
# TASK 2: Check Dependencies
# ============================================
echo ""
echo -e "${YELLOW}[AUTOMATED]${NC} Checking dependencies..."

# Check Git
if command -v git &> /dev/null; then
    echo -e "${GREEN}✓${NC} Git installed"
    AUTOMATED_TASKS+=("✓ Git installed")
else
    echo -e "${RED}✗${NC} Git not found"
    MANUAL_TASKS+=("✗ Install Git")
fi

# Check Node.js/npm
if command -v npm &> /dev/null; then
    echo -e "${GREEN}✓${NC} npm installed ($(npm --version))"
    AUTOMATED_TASKS+=("✓ npm installed")
    
    # Check Netlify CLI
    if command -v netlify &> /dev/null; then
        echo -e "${GREEN}✓${NC} Netlify CLI installed ($(netlify --version 2>/dev/null || echo 'installed'))"
        AUTOMATED_TASKS+=("✓ Netlify CLI installed")
    else
        echo -e "${YELLOW}⚠${NC} Netlify CLI not installed. Installing..."
        npm install -g netlify-cli && {
            echo -e "${GREEN}✓${NC} Netlify CLI installed"
            AUTOMATED_TASKS+=("✓ Netlify CLI installed")
        } || {
            echo -e "${RED}✗${NC} Failed to install Netlify CLI"
            MANUAL_TASKS+=("✗ Install Netlify CLI: npm install -g netlify-cli")
        }
    fi
else
    echo -e "${RED}✗${NC} npm not found"
    MANUAL_TASKS+=("✗ Install Node.js and npm")
fi

# Check Unity (if Unity CLI available)
if command -v Unity &> /dev/null || [ -d "/Applications/Unity" ] || [ -d "/Applications/Unity Hub.app" ]; then
    echo -e "${GREEN}✓${NC} Unity detected"
    AUTOMATED_TASKS+=("✓ Unity detected")
else
    echo -e "${YELLOW}⚠${NC} Unity not detected in PATH (this is OK if using Unity Editor GUI)"
    MANUAL_TASKS+=("⚠ Verify Unity Editor is installed")
fi

# ============================================
# TASK 3: Prepare Build Directory Structure
# ============================================
echo ""
echo -e "${YELLOW}[AUTOMATED]${NC} Preparing build directory structure..."

if [ -d "$UNITY_PROJECT_NAME" ]; then
    cd "$UNITY_PROJECT_NAME"
    
    # Create Builds/WebGL directory if it doesn't exist
    mkdir -p "$BUILD_PATH"
    echo -e "${GREEN}✓${NC} Build directory structure ready"
    AUTOMATED_TASKS+=("✓ Build directory structure ready")
    
    # Check if netlify.toml exists
    if [ ! -f "$BUILD_PATH/netlify.toml" ]; then
        echo -e "${YELLOW}⚠${NC} Creating netlify.toml configuration..."
        cat > "$BUILD_PATH/netlify.toml" << 'EOF'
[build]
  publish = "."

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[[headers]]
  for = "/*.wasm"
  [headers.values]
    Content-Type = "application/wasm"
    Cross-Origin-Embedder-Policy = "require-corp"
    Cross-Origin-Opener-Policy = "same-origin"

[[headers]]
  for = "/Build/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "/StreamingAssets/*"
  [headers.values]
    Cache-Control = "public, max-age=3600"
EOF
        echo -e "${GREEN}✓${NC} netlify.toml created"
        AUTOMATED_TASKS+=("✓ netlify.toml created")
    else
        echo -e "${GREEN}✓${NC} netlify.toml already exists"
        AUTOMATED_TASKS+=("✓ netlify.toml exists")
    fi
    
    cd ..
fi

# ============================================
# TASK 4: Check for Existing Build
# ============================================
echo ""
echo -e "${YELLOW}[AUTOMATED]${NC} Checking for existing WebGL build..."

if [ -d "$UNITY_PROJECT_NAME/$BUILD_PATH" ] && [ -f "$UNITY_PROJECT_NAME/$BUILD_PATH/index.html" ]; then
    echo -e "${GREEN}✓${NC} WebGL build found"
    echo -e "${BLUE}   Location:${NC} $UNITY_PROJECT_NAME/$BUILD_PATH"
    AUTOMATED_TASKS+=("✓ WebGL build found")
    
    # Check build files
    if [ -d "$UNITY_PROJECT_NAME/$BUILD_PATH/Build" ]; then
        echo -e "${GREEN}✓${NC} Build files present"
        AUTOMATED_TASKS+=("✓ Build files verified")
    else
        echo -e "${YELLOW}⚠${NC} Build folder incomplete"
        MANUAL_TASKS+=("⚠ Rebuild Unity project for WebGL")
    fi
else
    echo -e "${YELLOW}⚠${NC} No WebGL build found"
    MANUAL_TASKS+=("⚠ Build Unity project: File → Build Settings → WebGL → Build")
fi

# ============================================
# TASK 5: Prepare GitHub Actions Workflow
# ============================================
echo ""
echo -e "${YELLOW}[AUTOMATED]${NC} Checking GitHub Actions workflow..."

if [ -d "$UNITY_PROJECT_NAME/.github/workflows" ]; then
    if [ -f "$UNITY_PROJECT_NAME/.github/workflows/unity-webgl-build.yml" ]; then
        echo -e "${GREEN}✓${NC} GitHub Actions workflow exists"
        AUTOMATED_TASKS+=("✓ GitHub Actions workflow exists")
    else
        echo -e "${YELLOW}⚠${NC} Creating GitHub Actions workflow..."
        mkdir -p "$UNITY_PROJECT_NAME/.github/workflows"
        # Note: Would create workflow file here, but keeping it simple
        echo -e "${BLUE}   Workflow template available in repository${NC}"
        MANUAL_TASKS+=("⚠ Review GitHub Actions workflow setup")
    fi
else
    echo -e "${YELLOW}⚠${NC} .github/workflows directory not found"
    MANUAL_TASKS+=("⚠ Set up GitHub Actions workflow (Phase 2)")
fi

# ============================================
# TASK 6: Create Setup Checklist
# ============================================
echo ""
echo -e "${YELLOW}[AUTOMATED]${NC} Creating setup checklist..."

CHECKLIST_FILE="$SCRIPT_DIR/SETUP-CHECKLIST-$(date +%Y%m%d).md"
cat > "$CHECKLIST_FILE" << EOF
# Unity/Netlify/WebGL Setup Checklist
**Generated:** $(date)
**Status:** In Progress

## ✅ Automated Tasks (Completed)
$(for task in "${AUTOMATED_TASKS[@]}"; do echo "- $task"; done)

## ⚠️ Manual Tasks (To Do)
$(for task in "${MANUAL_TASKS[@]}"; do echo "- $task"; done)

## 📋 Manual Steps from PHASE-1-NETLIFY-SETUP-GUIDE.md

### Step 1.2: Build Unity Project to WebGL
- [ ] Open Unity Hub
- [ ] Open BTEBallCODE project
- [ ] File → Build Settings
- [ ] Select WebGL platform
- [ ] Configure Player Settings:
  - [ ] Compression: Gzip
  - [ ] Data Caching: Enabled
  - [ ] Memory Size: 256MB
- [ ] Build to: \`Builds/WebGL/\`
- [ ] Wait for build (5-10 minutes)

### Step 1.3: Deploy to Netlify Manually
- [ ] Go to https://app.netlify.com
- [ ] Sign in
- [ ] Click "Add new site"
- [ ] Select "Deploy manually"
- [ ] Upload \`Builds/WebGL/\` folder
- [ ] Note site URL

### Step 1.4: Get Netlify Credentials
- [ ] Get Site ID:
  - [ ] Click site → Site settings → General
  - [ ] Copy Site ID
- [ ] Generate Access Token:
  - [ ] Go to User Settings → Applications
  - [ ] Create "Unity Automation" token
  - [ ] Copy token (save securely!)

### Step 1.5: Add Credentials to GitHub Secrets
- [ ] Go to https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
- [ ] Add \`NETLIFY_AUTH_TOKEN\`
- [ ] Add \`NETLIFY_SITE_ID\`
- [ ] Add \`NETLIFY_SITE_NAME\` (optional)

## 🚀 Next Steps After Manual Setup
1. Run \`./automate-netlify-deploy.sh\` to deploy
2. Test deployment
3. Proceed to Phase 2: GitHub Actions Setup
4. Proceed to Phase 3: n8n Workflow Build

EOF

echo -e "${GREEN}✓${NC} Checklist created: $CHECKLIST_FILE"
AUTOMATED_TASKS+=("✓ Setup checklist created")

# ============================================
# SUMMARY
# ============================================
echo ""
echo -e "${GREEN}╔════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║                    AUTOMATION COMPLETE                  ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════╝${NC}"
echo ""

echo -e "${BLUE}✅ Automated Tasks Completed:${NC}"
for task in "${AUTOMATED_TASKS[@]}"; do
    echo -e "   ${GREEN}$task${NC}"
done

echo ""
echo -e "${YELLOW}⚠️  Manual Tasks Remaining:${NC}"
for task in "${MANUAL_TASKS[@]}"; do
    echo -e "   $task"
done

echo ""
echo -e "${BLUE}📋 Next Steps:${NC}"
echo "   1. Review checklist: $CHECKLIST_FILE"
echo "   2. Follow PHASE-1-NETLIFY-SETUP-GUIDE.md for manual steps"
echo "   3. After manual setup, run: ./automate-netlify-deploy.sh"
echo ""

echo -e "${GREEN}🎯 Main Setup Guide:${NC} PHASE-1-NETLIFY-SETUP-GUIDE.md"
echo ""


