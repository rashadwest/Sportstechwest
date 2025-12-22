#!/bin/bash

# Check Netlify API Access
# Tests what Netlify sites you have access to

echo "============================================================"
echo "Check Netlify API Access"
echo "============================================================"
echo ""

# Check if token is provided
if [ -z "$NETLIFY_TOKEN" ]; then
  echo "⚠️  NETLIFY_TOKEN environment variable not set"
  echo ""
  echo "To use this script:"
  echo "1. Get your Netlify token from: https://app.netlify.com/user/applications"
  echo "2. Run: export NETLIFY_TOKEN='your-token-here'"
  echo "3. Run this script again"
  echo ""
  echo "Or provide token directly:"
  echo "NETLIFY_TOKEN='your-token' $0"
  echo ""
  exit 1
fi

echo "Testing Netlify API access..."
echo ""

# Get list of sites
echo "Fetching your Netlify sites..."
RESPONSE=$(curl -s -w "\nHTTP_STATUS:%{http_code}" \
  -H "Authorization: Bearer $NETLIFY_TOKEN" \
  https://api.netlify.com/api/v1/sites)

HTTP_STATUS=$(echo "$RESPONSE" | grep "HTTP_STATUS" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_STATUS/d')

echo "HTTP Status: $HTTP_STATUS"
echo ""

if [ "$HTTP_STATUS" = "200" ]; then
  echo "✅ Successfully connected to Netlify API!"
  echo ""
  
  # Parse sites
  SITE_COUNT=$(echo "$BODY" | jq '. | length' 2>/dev/null || echo "0")
  
  if [ "$SITE_COUNT" = "0" ] || [ -z "$SITE_COUNT" ]; then
    echo "ℹ️  No sites found (or API response format different)"
    echo ""
    echo "Full response:"
    echo "$BODY" | jq '.' 2>/dev/null || echo "$BODY"
  else
    echo "Found $SITE_COUNT site(s):"
    echo ""
    
    # List sites with IDs
    echo "$BODY" | jq -r '.[] | "Site: \(.name)\n  URL: \(.url)\n  Site ID: \(.site_id)\n  Owner: \(.account_name // "unknown")\n"' 2>/dev/null
    
    if [ $? -ne 0 ]; then
      echo "Could not parse sites. Full response:"
      echo "$BODY" | jq '.' 2>/dev/null || echo "$BODY"
    else
      echo ""
      echo "✅ You can use any of these Site IDs in your workflow!"
      echo ""
      echo "To update workflow:"
      echo "1. Copy a Site ID from above"
      echo "2. Run: python scripts/robot-hardcode-env-vars.py"
      echo "3. Enter the Site ID when prompted"
    fi
  fi
elif [ "$HTTP_STATUS" = "401" ]; then
  echo "❌ Unauthorized - Check your Netlify token"
  echo "Get token from: https://app.netlify.com/user/applications"
elif [ "$HTTP_STATUS" = "403" ]; then
  echo "❌ Forbidden - Token may not have correct permissions"
else
  echo "⚠️  Unexpected response: $HTTP_STATUS"
  echo "Response: $BODY"
fi

echo ""
echo "============================================================"

