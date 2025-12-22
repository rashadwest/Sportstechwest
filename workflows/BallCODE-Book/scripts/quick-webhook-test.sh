#!/bin/bash
# Quick Webhook Test - All Webhooks at Once
# Copyright © 2025 Rashad West. All Rights Reserved.

N8N_URL="${N8N_URL:-http://192.168.1.226:5678}"

echo "🧪 Testing all webhooks at ${N8N_URL} (using test URLs)..."
echo ""

# 1. Unity Build
echo "1️⃣  Unity Build..."
curl -s -X POST "${N8N_URL}/webhook-test/unity-build" -H "Content-Type: application/json" -d '{"request":"Test","branch":"main"}' | head -c 100 && echo " ✅" || echo " ❌"

# 2. Full Integration
echo "2️⃣  Full Integration..."
curl -s -X POST "${N8N_URL}/webhook-test/ballcode-dev" -H "Content-Type: application/json" -d '{"prompt":"Test","mode":"quick"}' | head -c 100 && echo " ✅" || echo " ❌"

# 3. Screenshot Fix
echo "3️⃣  Screenshot Fix..."
curl -s -X POST "${N8N_URL}/webhook-test/screenshot-fix" -H "Content-Type: application/json" -d '{"screenshotUrl":"test","context":"test"}' | head -c 100 && echo " ✅" || echo " ❌"

echo ""
echo "✅ All webhooks tested (using /webhook-test/ URLs)"

