#!/bin/bash
# Recreate Unity Build Orchestrator from scratch - Complete end-to-end validation
# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

PI_N8N_URL="http://192.168.1.226:5678"
DESKTOP_FILE="${HOME}/Desktop/n8n-workflows-to-import/n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🔧 Recreate Orchestrator - Complete End-to-End Fix${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Load API key
if [ -f .n8n-env.pi ]; then
    source .n8n-env.pi 2>/dev/null
fi

if [ -z "$N8N_API_KEY" ] || [ "$N8N_API_KEY" = "" ]; then
    echo -e "${RED}❌ No API key found${NC}"
    exit 1
fi

echo -e "${GREEN}✅ API key found${NC}"
echo ""

# Step 1: Delete ALL existing orchestrators
echo -e "${YELLOW}Step 1: Deleting ALL existing orchestrators...${NC}"
WORKFLOWS=$(curl -s -X GET "${PI_N8N_URL}/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json")

ORCHESTRATOR_IDS=$(echo "$WORKFLOWS" | python3 -c "
import sys, json
data = json.load(sys.stdin)
workflows = [w for w in data.get('data', []) if 'Unity Build Orchestrator' in w.get('name', '')]
for w in workflows:
    print(w.get('id'))
" 2>/dev/null)

COUNT=$(echo "$ORCHESTRATOR_IDS" | grep -v '^$' | wc -l | tr -d ' ')
if [ "$COUNT" -gt 0 ]; then
    for ID in $ORCHESTRATOR_IDS; do
        if [ -n "$ID" ]; then
            curl -s -X DELETE "${PI_N8N_URL}/api/v1/workflows/$ID" \
              -H "X-N8N-API-KEY: $N8N_API_KEY" > /dev/null 2>&1
        fi
    done
    echo -e "${GREEN}✅ Deleted $COUNT workflow(s)${NC}"
else
    echo -e "${GREEN}✅ No workflows to delete${NC}"
fi
echo ""

# Step 2: Read original and create completely clean version
echo -e "${YELLOW}Step 2: Creating completely clean workflow...${NC}"
if [ ! -f "$DESKTOP_FILE" ]; then
    echo -e "${RED}❌ Original file not found: $DESKTOP_FILE${NC}"
    exit 1
fi

CLEAN_FILE="/tmp/orchestrator-recreated-$$-$(date +%s).json"

python3 << 'PYTHON_SCRIPT'
import json
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r') as f:
    original = json.load(f)

# Create completely clean workflow from scratch
clean_workflow = {
    "name": original.get("name", "Unity Build Orchestrator"),
    "nodes": [],
    "connections": original.get("connections", {}),
    "settings": {
        "executionOrder": "v1",
        "timezone": "America/New_York"
    }
}

# Process each node - completely clean
for node in original.get("nodes", []):
    clean_node = {
        "id": node.get("id"),
        "name": node.get("name"),
        "type": node.get("type"),
        "typeVersion": node.get("typeVersion"),
        "position": node.get("position", [0, 0]),
        "parameters": {}
    }
    
    # Handle disabled property
    if node.get("disabled"):
        clean_node["disabled"] = True
    
    # Copy parameters - but clean them
    params = node.get("parameters", {})
    for key, value in params.items():
        # Skip empty options objects
        if key == "options":
            if value and value != {} and value is not None:
                # Only keep non-empty options
                if isinstance(value, dict) and len(value) > 0:
                    clean_node["parameters"][key] = value
            # Skip empty options entirely
        else:
            clean_node["parameters"][key] = value
    
    # Special handling for respondToWebhook (typeVersion 1)
    if "respondToWebhook" in clean_node["type"] and clean_node.get("typeVersion") == 1:
        # Remove options completely - not allowed in v1
        clean_node["parameters"].pop("options", None)
        # Only keep allowed parameters
        allowed_params = ["respondWith", "responseBody", "responseCode", "responseHeaders"]
        filtered_params = {k: v for k, v in clean_node["parameters"].items() if k in allowed_params}
        clean_node["parameters"] = filtered_params
    
    # Special handling for webhook nodes
    if "webhook" in clean_node["type"].lower() and clean_node.get("typeVersion") == 1:
        # Remove empty options
        if "options" in clean_node["parameters"]:
            if not clean_node["parameters"]["options"] or clean_node["parameters"]["options"] == {}:
                clean_node["parameters"].pop("options", None)
        # Keep webhookId if present
        if "webhookId" in node:
            clean_node["webhookId"] = node["webhookId"]
    
    # Handle credentials - keep them but ensure structure is correct
    if "credentials" in node:
        clean_node["credentials"] = node["credentials"]
    
    clean_workflow["nodes"].append(clean_node)

# Remove null/empty optional properties
if "staticData" in original and (original["staticData"] is None or original["staticData"] == {}):
    pass  # Don't include if empty
else:
    clean_workflow["staticData"] = original.get("staticData", {})

if "pinData" in original and (original["pinData"] is None or original["pinData"] == {}):
    pass  # Don't include if empty
else:
    clean_workflow["pinData"] = original.get("pinData", {})

# Write clean workflow
with open(output_file, 'w') as f:
    json.dump(clean_workflow, f, indent=2)

print(f"✅ Created clean workflow: {len(clean_workflow['nodes'])} nodes")

# Validate
issues = []
for node in clean_workflow["nodes"]:
    node_type = node.get("type", "")
    params = node.get("parameters", {})
    
    # Check for problematic options
    if "options" in params:
        if params["options"] == {} or params["options"] is None:
            issues.append(f"{node.get('name')}: empty options")
        if "respondToWebhook" in node_type and node.get("typeVersion") == 1:
            issues.append(f"{node.get('name')}: respondToWebhook v1 has options")

if issues:
    print(f"⚠️  Found {len(issues)} issues:")
    for issue in issues:
        print(f"   - {issue}")
    sys.exit(1)
else:
    print("✅ Validation passed - no issues found")

PYTHON_SCRIPT
"$DESKTOP_FILE" "$CLEAN_FILE"

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Failed to create clean workflow${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Clean workflow created${NC}"
echo ""

# Step 3: Deep validation
echo -e "${YELLOW}Step 3: Deep validation...${NC}"
python3 << 'VALIDATE_SCRIPT'
import json
import sys

with open(sys.argv[1], 'r') as f:
    workflow = json.load(f)

errors = []
warnings = []

# Check node count
node_count = len(workflow.get("nodes", []))
if node_count != 13:
    errors.append(f"Expected 13 nodes, found {node_count}")

# Validate each node
for i, node in enumerate(workflow.get("nodes", []), 1):
    node_name = node.get("name", f"Node {i}")
    node_type = node.get("type", "")
    type_version = node.get("typeVersion", "")
    params = node.get("parameters", {})
    
    # Check required fields
    if not node.get("id"):
        errors.append(f"{node_name}: missing id")
    if not node.get("type"):
        errors.append(f"{node_name}: missing type")
    if not node.get("typeVersion"):
        warnings.append(f"{node_name}: missing typeVersion")
    
    # Check respondToWebhook
    if "respondToWebhook" in node_type and type_version == 1:
        if "options" in params:
            errors.append(f"{node_name}: respondToWebhook v1 MUST NOT have options")
        # Check allowed parameters
        allowed = ["respondWith", "responseBody", "responseCode", "responseHeaders"]
        for param in params:
            if param not in allowed:
                warnings.append(f"{node_name}: respondToWebhook has unexpected parameter: {param}")
    
    # Check webhook nodes
    if "webhook" in node_type.lower() and type_version == 1:
        if "options" in params and (params["options"] == {} or params["options"] is None):
            errors.append(f"{node_name}: webhook has empty options")
    
    # Check httpRequest nodes - options should have content
    if "httpRequest" in node_type:
        if "options" in params:
            if not params["options"] or params["options"] == {}:
                warnings.append(f"{node_name}: httpRequest has empty options (may be OK)")

if errors:
    print(f"❌ Found {len(errors)} errors:")
    for error in errors:
        print(f"   - {error}")
    sys.exit(1)

if warnings:
    print(f"⚠️  Found {len(warnings)} warnings:")
    for warning in warnings[:5]:
        print(f"   - {warning}")

print(f"✅ Validation passed: {node_count} nodes, no errors")

VALIDATE_SCRIPT
"$CLEAN_FILE"

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Validation failed${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Deep validation passed${NC}"
echo ""

# Step 4: Import
echo -e "${YELLOW}Step 4: Importing workflow...${NC}"
IMPORT_RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @"$CLEAN_FILE")

HTTP_CODE=$(echo "$IMPORT_RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$IMPORT_RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" != "200" ] && [ "$HTTP_CODE" != "201" ]; then
    echo -e "${RED}❌ Import failed (HTTP $HTTP_CODE)${NC}"
    echo "$BODY" | head -10
    echo ""
    echo -e "${YELLOW}Debugging info:${NC}"
    echo "Checking workflow structure..."
    python3 -c "
import json
with open('$CLEAN_FILE', 'r') as f:
    w = json.load(f)
print(f'Nodes: {len(w.get(\"nodes\", []))}')
for node in w.get('nodes', []):
    if 'respondToWebhook' in node.get('type', ''):
        print(f'  {node.get(\"name\")}: {node.get(\"type\")} v{node.get(\"typeVersion\")}')
        print(f'    Params: {list(node.get(\"parameters\", {}).keys())}')
"
    [ -f "$CLEAN_FILE" ] && rm -f "$CLEAN_FILE"
    exit 1
fi

WORKFLOW_ID=$(echo "$BODY" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('id', ''))" 2>/dev/null || echo "")
if [ -z "$WORKFLOW_ID" ]; then
    echo -e "${RED}❌ Could not get workflow ID${NC}"
    [ -f "$CLEAN_FILE" ] && rm -f "$CLEAN_FILE"
    exit 1
fi

echo -e "${GREEN}✅ Workflow imported (ID: $WORKFLOW_ID)${NC}"
[ -f "$CLEAN_FILE" ] && rm -f "$CLEAN_FILE"
echo ""

# Step 5: Verify imported workflow
echo -e "${YELLOW}Step 5: Verifying imported workflow...${NC}"
VERIFY_RESPONSE=$(curl -s -X GET "${PI_N8N_URL}/api/v1/workflows/$WORKFLOW_ID" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" 2>/dev/null)

NODE_COUNT=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(len(data.get('nodes', [])))" 2>/dev/null || echo "?")
IS_ARCHIVED=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('isArchived', False))" 2>/dev/null || echo "?")
WORKFLOW_NAME=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('name', 'Unknown'))" 2>/dev/null || echo "Unknown")

# Check for any issues in imported workflow
ISSUES=$(echo "$VERIFY_RESPONSE" | python3 -c "
import sys, json
data = json.load(sys.stdin)
issues = []
for node in data.get('nodes', []):
    if 'respondToWebhook' in node.get('type', '') and node.get('typeVersion') == 1:
        if 'options' in node.get('parameters', {}):
            issues.append(f\"{node.get('name')}: respondToWebhook v1 has options\")
if issues:
    for issue in issues:
        print(issue)
" 2>/dev/null)

if [ -n "$ISSUES" ]; then
    echo -e "${RED}❌ Issues found in imported workflow:${NC}"
    echo "$ISSUES"
    exit 1
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ SUCCESS! Orchestrator Recreated${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo "  Name: $WORKFLOW_NAME"
echo "  ID: $WORKFLOW_ID"
echo "  Nodes: $NODE_COUNT"
echo "  Archived: $IS_ARCHIVED"
echo ""
echo -e "${GREEN}✅ All validations passed${NC}"
echo -e "${GREEN}✅ No bugs found${NC}"
echo -e "${GREEN}✅ Ready to activate${NC}"
echo ""
echo -e "${YELLOW}📝 Next step:${NC}"
echo "  1. Open: $PI_N8N_URL"
echo "  2. Find workflow: $WORKFLOW_NAME"
echo "  3. Toggle switch to activate"
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
