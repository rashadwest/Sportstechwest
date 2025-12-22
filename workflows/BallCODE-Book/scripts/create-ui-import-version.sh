#!/bin/bash
# Create a version for UI import (removes disabled scheduled trigger)
# Sometimes UI handles imports differently than API

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

SOURCE_FILE="n8n-unity-build-orchestrator-FIXED-V3.json"
OUTPUT_FILE="n8n-unity-build-orchestrator-UI-IMPORT.json"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📦 Create UI Import Version${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

if [ ! -f "$SOURCE_FILE" ]; then
    echo -e "${RED}❌ Source file not found: $SOURCE_FILE${NC}"
    exit 1
fi

python3 -c "
import json

with open('$SOURCE_FILE', 'r') as f:
    wf = json.load(f)

# Remove disabled scheduled trigger (might be causing UI issues)
nodes = []
removed_count = 0
for node in wf.get('nodes', []):
    # Skip disabled scheduled triggers
    if node.get('type') == 'n8n-nodes-base.scheduleTrigger' and node.get('disabled'):
        removed_count += 1
        print(f'Removed disabled scheduled trigger: {node.get(\"name\")}')
        continue
    nodes.append(node)

wf['nodes'] = nodes

# Update connections to remove references to removed node
connections = wf.get('connections', {})
if 'Scheduled Trigger (Hourly) [DISABLED ON DEV]' in connections:
    del connections['Scheduled Trigger (Hourly) [DISABLED ON DEV]']

wf['connections'] = connections

# Save
with open('$OUTPUT_FILE', 'w') as f:
    json.dump(wf, f, indent=2)

print(f'')
print(f'✅ Created UI import version')
print(f'   Removed {removed_count} disabled scheduled trigger(s)')
print(f'   Nodes: {len(nodes)} (was {len(wf.get(\"nodes\", [])) + removed_count})')
print(f'   File: $OUTPUT_FILE')
" 2>&1

if [ ! -f "$OUTPUT_FILE" ]; then
    echo -e "${RED}❌ Failed to create UI import version${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}✅ Ready for UI import!${NC}"
echo ""
echo -e "${CYAN}To import:${NC}"
echo "1. Open n8n UI: http://192.168.1.226:5678"
echo "2. Click 'Workflows' → 'Import from File'"
echo "3. Select: $OUTPUT_FILE"
echo "4. Click 'Import'"
echo ""

