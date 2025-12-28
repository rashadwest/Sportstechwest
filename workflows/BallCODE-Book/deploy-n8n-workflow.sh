#!/bin/bash
# Deploy n8n workflow remotely via API
# Usage: ./deploy-n8n-workflow.sh <workflow.json> [workflow-id]

set -e  # Exit on error

WORKFLOW_FILE="$1"
WORKFLOW_ID="$2"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if workflow file provided
if [ -z "$WORKFLOW_FILE" ]; then
  echo -e "${RED}❌ Error: Workflow file required${NC}"
  echo "Usage: ./deploy-n8n-workflow.sh <workflow.json> [workflow-id]"
  echo ""
  echo "Examples:"
  echo "  # Create new workflow"
  echo "  ./deploy-n8n-workflow.sh n8n-unity-automation-workflow.json"
  echo ""
  echo "  # Update existing workflow"
  echo "  ./deploy-n8n-workflow.sh n8n-unity-automation-workflow.json abc123"
  exit 1
fi

# Check if file exists
if [ ! -f "$WORKFLOW_FILE" ]; then
  echo -e "${RED}❌ Error: Workflow file not found: $WORKFLOW_FILE${NC}"
  exit 1
fi

# Load environment variables
if [ -f .env ]; then
  source .env
elif [ -f .n8n-env ]; then
  source .n8n-env
fi

# Check required environment variables
if [ -z "$N8N_URL" ]; then
  echo -e "${YELLOW}⚠️  N8N_URL not set. Using default: http://localhost:5678${NC}"
  N8N_URL="http://localhost:5678"
fi

# Validate JSON before deployment
echo -e "${YELLOW}📋 Validating workflow JSON...${NC}"
if ! python3 -m json.tool "$WORKFLOW_FILE" > /dev/null 2>&1; then
  echo -e "${RED}❌ Error: Invalid JSON in workflow file${NC}"
  echo "Run: python3 -m json.tool $WORKFLOW_FILE"
  exit 1
fi
echo -e "${GREEN}✅ JSON is valid${NC}"

# Check for placeholder values
echo -e "${YELLOW}🔍 Checking for placeholder values...${NC}"
if grep -q "YOUR_\|PLACEHOLDER\|your-email\|your-api-key" "$WORKFLOW_FILE"; then
  echo -e "${YELLOW}⚠️  Warning: Found placeholder values in workflow${NC}"
  echo "   Review the workflow file before deploying"
  read -p "   Continue anyway? (y/n) " -n 1 -r
  echo
  if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    exit 1
  fi
else
  echo -e "${GREEN}✅ No placeholder values found${NC}"
fi

# Build API request
API_URL="$N8N_URL/api/v1/workflows"
HEADERS=(-H "Content-Type: application/json")

# Add API key if provided
if [ -n "$N8N_API_KEY" ]; then
  HEADERS+=(-H "X-N8N-API-KEY: $N8N_API_KEY")
elif [ -n "$N8N_BASIC_AUTH" ]; then
  HEADERS+=(-u "$N8N_BASIC_AUTH")
else
  echo -e "${YELLOW}⚠️  Warning: No authentication configured${NC}"
  echo "   Set N8N_API_KEY or N8N_BASIC_AUTH environment variable"
  read -p "   Continue without authentication? (y/n) " -n 1 -r
  echo
  if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    exit 1
  fi
fi

# Deploy workflow
if [ -z "$WORKFLOW_ID" ]; then
  # Create new workflow
  echo -e "${YELLOW}🚀 Creating new workflow...${NC}"
  RESPONSE=$(curl -s -w "\n%{http_code}" -X POST "$API_URL" \
    "${HEADERS[@]}" \
    -d @"$WORKFLOW_FILE")
  
  HTTP_CODE=$(echo "$RESPONSE" | tail -n1)
  BODY=$(echo "$RESPONSE" | sed '$d')
  
  if [ "$HTTP_CODE" -eq 200 ] || [ "$HTTP_CODE" -eq 201 ]; then
    echo -e "${GREEN}✅ Workflow created successfully!${NC}"
    echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY"
    
    # Extract workflow ID if possible
    WORKFLOW_ID=$(echo "$BODY" | python3 -c "import sys, json; print(json.load(sys.stdin).get('id', ''))" 2>/dev/null || echo "")
    if [ -n "$WORKFLOW_ID" ]; then
      echo -e "${GREEN}📝 Workflow ID: $WORKFLOW_ID${NC}"
      echo "   Save this ID for future updates"
    fi
  else
    echo -e "${RED}❌ Error creating workflow (HTTP $HTTP_CODE)${NC}"
    echo "$BODY"
    exit 1
  fi
else
  # Update existing workflow
  echo -e "${YELLOW}🔄 Updating workflow $WORKFLOW_ID...${NC}"
  
  # First, get existing workflow to merge settings
  EXISTING=$(curl -s -X GET "$API_URL/$WORKFLOW_ID" \
    "${HEADERS[@]}" 2>/dev/null || echo "{}")
  
  RESPONSE=$(curl -s -w "\n%{http_code}" -X PUT "$API_URL/$WORKFLOW_ID" \
    "${HEADERS[@]}" \
    -d @"$WORKFLOW_FILE")
  
  HTTP_CODE=$(echo "$RESPONSE" | tail -n1)
  BODY=$(echo "$RESPONSE" | sed '$d')
  
  if [ "$HTTP_CODE" -eq 200 ]; then
    echo -e "${GREEN}✅ Workflow updated successfully!${NC}"
    echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY"
  else
    echo -e "${RED}❌ Error updating workflow (HTTP $HTTP_CODE)${NC}"
    echo "$BODY"
    exit 1
  fi
fi

# Summary
echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Deployment Complete!${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "Next steps:"
echo "  1. Open n8n UI: $N8N_URL"
if [ -n "$WORKFLOW_ID" ]; then
  echo "  2. Find workflow ID: $WORKFLOW_ID"
fi
echo "  3. Verify workflow structure"
echo "  4. Test execution"
echo "  5. Configure credentials if needed"
echo ""




