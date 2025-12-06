#!/bin/bash

# Automated WebGL Build Robot
# Handles: Trigger GitHub Actions → Monitor → Download Artifacts
# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${GREEN}╔════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║     WebGL Build Automation Robot                     ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════╝${NC}"
echo ""

# Configuration
REPO_OWNER="rashadwest"
REPO_NAME="BTEBallCODE"
WORKFLOW_FILE="unity-webgl-build.yml"
BRANCH="main"
ARTIFACT_NAME="webgl-build"
DOWNLOAD_DIR="./Builds/WebGL"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# ============================================
# CHECK PREREQUISITES
# ============================================
echo -e "${CYAN}🔍 Checking prerequisites...${NC}"

# Check GitHub CLI
if ! command -v gh &> /dev/null; then
    echo -e "${RED}✗${NC} GitHub CLI (gh) not found"
    echo -e "${YELLOW}   Install: brew install gh${NC}"
    exit 1
fi
echo -e "${GREEN}✓${NC} GitHub CLI installed"

# Check GitHub authentication
if ! gh auth status &> /dev/null; then
    echo -e "${YELLOW}⚠${NC} Not authenticated with GitHub"
    echo -e "${BLUE}   Running: gh auth login${NC}"
    gh auth login
fi
echo -e "${GREEN}✓${NC} GitHub authenticated"

# Check curl
if ! command -v curl &> /dev/null; then
    echo -e "${RED}✗${NC} curl not found"
    exit 1
fi
echo -e "${GREEN}✓${NC} curl installed"

echo ""

# ============================================
# FUNCTION: Check Workflow Status
# ============================================
check_workflow_status() {
    local run_id=$1
    local status=$(gh run view "$run_id" --repo "$REPO_OWNER/$REPO_NAME" --json status --jq '.status' 2>/dev/null || echo "unknown")
    echo "$status"
}

# ============================================
# FUNCTION: Wait for Workflow Completion
# ============================================
wait_for_workflow() {
    local run_id=$1
    local max_wait=1800  # 30 minutes
    local elapsed=0
    local check_interval=30  # Check every 30 seconds
    
    echo -e "${CYAN}⏳ Waiting for build to complete...${NC}"
    echo -e "${BLUE}   Run ID: $run_id${NC}"
    echo -e "${BLUE}   Monitor: https://github.com/$REPO_OWNER/$REPO_NAME/actions/runs/$run_id${NC}"
    echo ""
    
    while [ $elapsed -lt $max_wait ]; do
        local status=$(check_workflow_status "$run_id")
        
        case "$status" in
            "completed")
                echo -e "${GREEN}✓${NC} Build completed!"
                return 0
                ;;
            "in_progress"|"queued")
                local minutes=$((elapsed / 60))
                local seconds=$((elapsed % 60))
                echo -e "${YELLOW}⏳${NC} Build in progress... (${minutes}m ${seconds}s elapsed)"
                sleep $check_interval
                elapsed=$((elapsed + check_interval))
                ;;
            "failure"|"cancelled")
                echo -e "${RED}✗${NC} Build failed or was cancelled"
                echo -e "${BLUE}   Check logs: https://github.com/$REPO_OWNER/$REPO_NAME/actions/runs/$run_id${NC}"
                return 1
                ;;
            *)
                echo -e "${YELLOW}⚠${NC} Unknown status: $status"
                sleep $check_interval
                elapsed=$((elapsed + check_interval))
                ;;
        esac
    done
    
    echo -e "${RED}✗${NC} Build timeout after 30 minutes"
    return 1
}

# ============================================
# FUNCTION: Download Artifacts
# ============================================
download_artifacts() {
    local run_id=$1
    
    echo -e "${CYAN}📥 Downloading build artifacts...${NC}"
    
    # Create download directory
    mkdir -p "$DOWNLOAD_DIR"
    
    # Download artifact
    if gh run download "$run_id" --repo "$REPO_OWNER/$REPO_NAME" --name "$ARTIFACT_NAME" --dir "$DOWNLOAD_DIR" 2>/dev/null; then
        echo -e "${GREEN}✓${NC} Artifacts downloaded to: $DOWNLOAD_DIR"
        
        # Check if we need to extract
        if [ -f "$DOWNLOAD_DIR/$ARTIFACT_NAME.zip" ]; then
            echo -e "${CYAN}📦 Extracting zip file...${NC}"
            cd "$DOWNLOAD_DIR"
            unzip -q "$ARTIFACT_NAME.zip" -d . 2>/dev/null || {
                echo -e "${YELLOW}⚠${NC} Could not extract automatically. Please extract manually."
            }
            rm -f "$ARTIFACT_NAME.zip"
            cd "$SCRIPT_DIR"
        fi
        
        # Verify build files
        if [ -f "$DOWNLOAD_DIR/index.html" ]; then
            echo -e "${GREEN}✓${NC} WebGL build verified (index.html found)"
            return 0
        else
            echo -e "${YELLOW}⚠${NC} Build downloaded but index.html not found"
            return 1
        fi
    else
        echo -e "${RED}✗${NC} Failed to download artifacts"
        echo -e "${BLUE}   Try manually: gh run download $run_id --name $ARTIFACT_NAME${NC}"
        return 1
    fi
}

# ============================================
# MAIN: Check Workflow File Exists
# ============================================
echo -e "${CYAN}🔍 Checking workflow file...${NC}"

if gh workflow list --repo "$REPO_OWNER/$REPO_NAME" | grep -q "$WORKFLOW_FILE"; then
    echo -e "${GREEN}✓${NC} Workflow file exists: $WORKFLOW_FILE"
else
    echo -e "${RED}✗${NC} Workflow file not found: $WORKFLOW_FILE"
    echo -e "${YELLOW}   Create it first (see PHASE-2-GITHUB-ACTIONS-SETUP.md)${NC}"
    exit 1
fi

# ============================================
# MAIN: Check GitHub Secrets
# ============================================
echo ""
echo -e "${CYAN}🔍 Checking GitHub Secrets...${NC}"

REQUIRED_SECRETS=("NETLIFY_AUTH_TOKEN" "NETLIFY_SITE_ID")
MISSING_SECRETS=()

for secret in "${REQUIRED_SECRETS[@]}"; do
    if gh secret list --repo "$REPO_OWNER/$REPO_NAME" | grep -q "$secret"; then
        echo -e "${GREEN}✓${NC} Secret configured: $secret"
    else
        echo -e "${YELLOW}⚠${NC} Secret missing: $secret"
        MISSING_SECRETS+=("$secret")
    fi
done

if [ ${#MISSING_SECRETS[@]} -gt 0 ]; then
    echo ""
    echo -e "${YELLOW}⚠${NC} Missing secrets detected. Build may fail."
    echo -e "${BLUE}   Add secrets: gh secret set SECRET_NAME --repo $REPO_OWNER/$REPO_NAME${NC}"
    echo -e "${BLUE}   Or add via GitHub UI: Settings → Secrets and variables → Actions${NC}"
    echo ""
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# ============================================
# MAIN: Trigger Workflow
# ============================================
echo ""
echo -e "${CYAN}🚀 Triggering GitHub Actions workflow...${NC}"

# Check if user wants to trigger or just download existing
echo ""
echo "What would you like to do?"
echo "1) Trigger new build"
echo "2) Download latest completed build"
echo "3) Check status of recent builds"
read -p "Choice (1-3): " choice

case $choice in
    1)
        echo -e "${BLUE}Triggering workflow: $WORKFLOW_FILE on branch: $BRANCH${NC}"
        
        # Trigger workflow
        RUN_ID=$(gh workflow run "$WORKFLOW_FILE" --repo "$REPO_OWNER/$REPO_NAME" --ref "$BRANCH" --json databaseId --jq '.databaseId' 2>/dev/null)
        
        if [ -z "$RUN_ID" ]; then
            # Fallback: get run ID from workflow runs
            sleep 2
            RUN_ID=$(gh run list --repo "$REPO_OWNER/$REPO_NAME" --workflow="$WORKFLOW_FILE" --limit 1 --json databaseId --jq '.[0].databaseId' 2>/dev/null)
        fi
        
        if [ -z "$RUN_ID" ] || [ "$RUN_ID" == "null" ]; then
            echo -e "${RED}✗${NC} Failed to trigger workflow or get run ID"
            echo -e "${BLUE}   Try manually: https://github.com/$REPO_OWNER/$REPO_NAME/actions/workflows/$WORKFLOW_FILE${NC}"
            exit 1
        fi
        
        echo -e "${GREEN}✓${NC} Workflow triggered!"
        echo -e "${BLUE}   Run ID: $RUN_ID${NC}"
        echo ""
        
        # Wait for completion
        if wait_for_workflow "$RUN_ID"; then
            # Download artifacts
            if download_artifacts "$RUN_ID"; then
                echo ""
                echo -e "${GREEN}╔════════════════════════════════════════════════════════╗${NC}"
                echo -e "${GREEN}║           ✅ BUILD COMPLETE!                          ║${NC}"
                echo -e "${GREEN}╚════════════════════════════════════════════════════════╝${NC}"
                echo ""
                echo -e "${CYAN}📁 Build location:${NC} $DOWNLOAD_DIR"
                echo -e "${CYAN}🌐 View run:${NC} https://github.com/$REPO_OWNER/$REPO_NAME/actions/runs/$RUN_ID"
                echo ""
                echo -e "${YELLOW}Next steps:${NC}"
                echo "  1. Test build locally: cd $DOWNLOAD_DIR && python3 -m http.server 8000"
                echo "  2. Deploy to Netlify: See PHASE-1-NETLIFY-SETUP-GUIDE.md"
            fi
        fi
        ;;
        
    2)
        echo -e "${CYAN}📥 Finding latest completed build...${NC}"
        
        # Get latest completed run
        RUN_ID=$(gh run list --repo "$REPO_OWNER/$REPO_NAME" --workflow="$WORKFLOW_FILE" --status=success --limit 1 --json databaseId --jq '.[0].databaseId' 2>/dev/null)
        
        if [ -z "$RUN_ID" ] || [ "$RUN_ID" == "null" ]; then
            echo -e "${RED}✗${NC} No completed builds found"
            echo -e "${BLUE}   Trigger a new build first (option 1)${NC}"
            exit 1
        fi
        
        echo -e "${GREEN}✓${NC} Found completed build: $RUN_ID"
        download_artifacts "$RUN_ID"
        ;;
        
    3)
        echo -e "${CYAN}📊 Recent workflow runs:${NC}"
        echo ""
        gh run list --repo "$REPO_OWNER/$REPO_NAME" --workflow="$WORKFLOW_FILE" --limit 5
        echo ""
        read -p "Enter run ID to download (or press Enter to exit): " run_id
        if [ -n "$run_id" ]; then
            download_artifacts "$run_id"
        fi
        ;;
        
    *)
        echo -e "${RED}✗${NC} Invalid choice"
        exit 1
        ;;
esac

echo ""
echo -e "${GREEN}✅ Automation complete!${NC}"
