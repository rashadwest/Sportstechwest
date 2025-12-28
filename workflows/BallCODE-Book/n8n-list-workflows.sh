#!/bin/bash
# List all n8n workflows with IDs
# Useful for finding workflow IDs to edit

# Copyright © 2025 Rashad West. All Rights Reserved.

TEMP_DIR="/tmp/n8n-list-$$"
mkdir -p "$TEMP_DIR"
trap "rm -rf $TEMP_DIR" EXIT

echo "📋 Exporting all workflows to get IDs..."
echo ""

if n8n export:workflow --all --output="$TEMP_DIR" --separate --pretty 2>/dev/null; then
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "📊 Available Workflows:"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    
    for file in "$TEMP_DIR"/*.json; do
        if [ -f "$file" ]; then
            WORKFLOW_ID=$(python3 -c "import json, sys; wf = json.load(open('$file')); print(wf.get('id', 'unknown'))" 2>/dev/null || echo "unknown")
            WORKFLOW_NAME=$(python3 -c "import json, sys; wf = json.load(open('$file')); print(wf.get('name', 'Unknown'))" 2>/dev/null || echo "Unknown")
            NODE_COUNT=$(python3 -c "import json, sys; wf = json.load(open('$file')); print(len(wf.get('nodes', [])))" 2>/dev/null || echo "0")
            ACTIVE=$(python3 -c "import json, sys; wf = json.load(open('$file')); print('✅' if wf.get('active', False) else '⏸️')" 2>/dev/null || echo "?")
            
            echo "  $ACTIVE $WORKFLOW_NAME"
            echo "     ID: $WORKFLOW_ID"
            echo "     Nodes: $NODE_COUNT"
            echo "     Edit: ./n8n-edit-workflow.sh $WORKFLOW_ID"
            echo ""
        fi
    done
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
else
    echo "❌ Failed to export workflows"
    echo "   Make sure n8n is running"
    exit 1
fi




