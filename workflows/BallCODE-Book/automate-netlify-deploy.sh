#!/bin/bash

# Netlify Deployment Automation Script
# Purpose: Deploy WebGL build to Netlify
# Usage: ./automate-netlify-deploy.sh <build-path> [site-name]

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if build path is provided
if [ -z "$1" ]; then
    echo -e "${RED}Error: Build path not provided${NC}"
    echo "Usage: ./automate-netlify-deploy.sh <build-path> [site-name]"
    echo "Example: ./automate-netlify-deploy.sh ~/Builds/WebGL ballcode-game"
    exit 1
fi

BUILD_PATH="$1"
SITE_NAME="${2:-ballcode-game}"

# Validate build path
if [ ! -d "$BUILD_PATH" ]; then
    echo -e "${RED}Error: Build path does not exist: ${BUILD_PATH}${NC}"
    exit 1
fi

# Check for required files
if [ ! -f "${BUILD_PATH}/index.html" ]; then
    echo -e "${RED}Error: index.html not found in build path${NC}"
    echo "Make sure this is a valid WebGL build directory"
    exit 1
fi

echo -e "${GREEN}Netlify Deployment Automation${NC}"
echo "=================================="
echo "Build Path: ${BUILD_PATH}"
echo "Site Name: ${SITE_NAME}"
echo ""

# Check if Netlify CLI is installed
if ! command -v netlify &> /dev/null; then
    echo -e "${YELLOW}Netlify CLI not found. Installing...${NC}"
    
    if command -v npm &> /dev/null; then
        npm install -g netlify-cli
    else
        echo -e "${RED}Error: npm not found. Please install Node.js and npm first${NC}"
        echo "Then run: npm install -g netlify-cli"
        exit 1
    fi
fi

# Check if user is logged in to Netlify
if ! netlify status &> /dev/null; then
    echo -e "${YELLOW}Not logged in to Netlify. Please log in:${NC}"
    netlify login
fi

# Create netlify.toml if it doesn't exist
NETLIFY_TOML="${BUILD_PATH}/netlify.toml"
if [ ! -f "$NETLIFY_TOML" ]; then
    echo -e "${YELLOW}Creating netlify.toml...${NC}"
    cat > "$NETLIFY_TOML" << 'EOF'
[build]
  publish = "."
  
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"

[[headers]]
  for = "/*.wasm"
  [headers.values]
    Content-Type = "application/wasm"

[[headers]]
  for = "/*.js"
  [headers.values]
    Content-Type = "application/javascript"

[[headers]]
  for = "/*.data"
  [headers.values]
    Content-Type = "application/octet-stream"
EOF
    echo -e "  ${GREEN}✓${NC} Created netlify.toml"
fi

# Deploy to Netlify
echo ""
echo -e "${YELLOW}Deploying to Netlify...${NC}"

# Check if site already exists
EXISTING_SITE=$(netlify sites:list --json 2>/dev/null | grep -o "\"name\":\"${SITE_NAME}\"" || true)

if [ -z "$EXISTING_SITE" ]; then
    echo -e "${BLUE}Creating new site: ${SITE_NAME}${NC}"
    cd "$BUILD_PATH"
    netlify deploy --prod --dir . --site "$SITE_NAME"
else
    echo -e "${BLUE}Deploying to existing site: ${SITE_NAME}${NC}"
    cd "$BUILD_PATH"
    netlify deploy --prod --dir . --site "$SITE_NAME"
fi

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}Deployment successful!${NC}"
    echo ""
    
    # Get site URL
    SITE_URL=$(netlify sites:info --json 2>/dev/null | grep -o '"url":"[^"]*"' | head -1 | cut -d'"' -f4 || echo "Check Netlify dashboard")
    
    echo -e "${BLUE}Site URL:${NC} ${SITE_URL}"
    echo ""
    echo -e "${YELLOW}Next Steps:${NC}"
    echo "1. Test the deployed site"
    echo "2. Configure custom domain (if needed)"
    echo "3. Set up environment variables (if needed)"
    echo "4. Test Story Mode → Game Mode flow"
    echo ""
else
    echo ""
    echo -e "${RED}Deployment failed!${NC}"
    echo "Check Netlify CLI output for errors"
    exit 1
fi


