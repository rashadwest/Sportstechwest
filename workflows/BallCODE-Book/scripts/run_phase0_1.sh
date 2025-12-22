#!/bin/bash
# Phase 0.1 Execution Script - Immediate Chat Lag Fixes
# Runs all Phase 0.1 scripts in sequence

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$PROJECT_ROOT"

echo "=========================================="
echo "Phase 0.1: Immediate Chat Lag Fixes"
echo "=========================================="
echo ""

# Step 1: Clear Chat Cache
echo "Step 1/3: Clearing chat cache..."
echo "----------------------------------------"
python3 scripts/clear_chat_cache.py
echo ""

# Step 2: Configure File Watchers
echo "Step 2/3: Optimizing file watchers..."
echo "----------------------------------------"
python3 scripts/configure_cursor_watchers.py
echo ""

# Step 3: Audit Extensions
echo "Step 3/3: Auditing extensions..."
echo "----------------------------------------"
python3 scripts/extension_audit.py
echo ""

echo "=========================================="
echo "Phase 0.1 Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Review extension_audit.json recommendations"
echo "2. Disable non-essential heavy extensions in Cursor"
echo "3. Update all extensions to latest versions"
echo "4. RESTART CURSOR (Cmd+Q, then reopen)"
echo "5. Test chat responsiveness"
echo ""
echo "If lag persists, continue to Phase 0.2 (Performance Monitoring)"

