#!/bin/bash

# Unity WebGL to Netlify Deployment Script
# Deploys WebGL build to Netlify with book integration support

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
UNITY_BUILD_PATH="./Builds/WebGL"
NETLIFY_SITE_NAME="${NETLIFY_SITE_NAME:-ballcode-game}"

echo -e "${GREEN}BallCODE WebGL to Netlify Deployment${NC}"
echo "=========================================="
echo "Build Path: ${UNITY_BUILD_PATH}"
echo "Site Name: ${NETLIFY_SITE_NAME}"
echo ""

# Check if build exists
if [ ! -d "$UNITY_BUILD_PATH" ]; then
    echo -e "${RED}Error: WebGL build not found at ${UNITY_BUILD_PATH}${NC}"
    echo ""
    echo "Please build Unity project first:"
    echo "  1. Open Unity project"
    echo "  2. File → Build Settings → WebGL"
    echo "  3. Build to: ${UNITY_BUILD_PATH}"
    exit 1
fi

# Check for required files
if [ ! -f "${UNITY_BUILD_PATH}/index.html" ]; then
    echo -e "${RED}Error: index.html not found in build${NC}"
    exit 1
fi

if [ ! -d "${UNITY_BUILD_PATH}/Build" ]; then
    echo -e "${RED}Error: Build folder not found${NC}"
    exit 1
fi

# Check if Netlify CLI is installed
if ! command -v netlify &> /dev/null; then
    echo -e "${YELLOW}Netlify CLI not found. Installing...${NC}"
    
    if command -v npm &> /dev/null; then
        npm install -g netlify-cli
    else
        echo -e "${RED}Error: npm not found. Please install Node.js and npm first${NC}"
        exit 1
    fi
fi

# Check if logged in to Netlify
if ! netlify status &> /dev/null; then
    echo -e "${YELLOW}Not logged in to Netlify. Please log in:${NC}"
    netlify login
fi

# Copy netlify.toml if it doesn't exist
if [ ! -f "${UNITY_BUILD_PATH}/netlify.toml" ]; then
    echo -e "${YELLOW}Copying netlify.toml...${NC}"
    cp "./Builds/WebGL/netlify.toml" "${UNITY_BUILD_PATH}/netlify.toml" 2>/dev/null || {
        echo -e "${YELLOW}Creating default netlify.toml...${NC}"
        cat > "${UNITY_BUILD_PATH}/netlify.toml" << 'EOF'
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
EOF
    }
fi

# Verify JavaScript bridge is in index.html
if ! grep -q "SendExerciseComplete" "${UNITY_BUILD_PATH}/index.html"; then
    echo -e "${YELLOW}Warning: JavaScript bridge not found in index.html${NC}"
    echo "The book integration return flow may not work."
    echo "See WEBGL-NETLIFY-DEPLOYMENT-GUIDE.md for instructions."
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Deploy to Netlify
echo ""
echo -e "${YELLOW}Deploying to Netlify...${NC}"
cd "$UNITY_BUILD_PATH"

# Check if site exists
if netlify sites:list --json 2>/dev/null | grep -q "\"name\":\"${NETLIFY_SITE_NAME}\""; then
    echo -e "${BLUE}Deploying to existing site: ${NETLIFY_SITE_NAME}${NC}"
    netlify deploy --prod --site "$NETLIFY_SITE_NAME"
else
    echo -e "${BLUE}Creating new site: ${NETLIFY_SITE_NAME}${NC}"
    netlify deploy --prod --dir . --site "$NETLIFY_SITE_NAME"
fi

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✓ Deployment successful!${NC}"
    echo ""
    
    # Get site URL
    SITE_URL=$(netlify sites:info --json 2>/dev/null | grep -o '"url":"[^"]*"' | head -1 | cut -d'"' -f4 || echo "Check Netlify dashboard")
    
    echo -e "${BLUE}Site URL:${NC} https://${NETLIFY_SITE_NAME}.netlify.app"
    echo ""
    echo -e "${YELLOW}Next Steps:${NC}"
    echo "1. Test the deployed game:"
    echo "   https://${NETLIFY_SITE_NAME}.netlify.app?book=1&exercise=foundation-block"
    echo ""
    echo "2. Update book page links to point to:"
    echo "   https://${NETLIFY_SITE_NAME}.netlify.app"
    echo ""
    echo "3. Test complete flow:"
    echo "   Book page → Exercise → Return to Book"
    echo ""
    echo "4. Configure custom domain (optional):"
    echo "   Netlify Dashboard → Domain Management"
    echo ""
else
    echo ""
    echo -e "${RED}✗ Deployment failed!${NC}"
    echo "Check Netlify CLI output for errors"
    exit 1
fi


