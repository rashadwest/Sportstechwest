#!/bin/bash

# Simple Netlify Deployment - One Command
# Copyright © 2025 Rashad West. All Rights Reserved.

# Usage: ./deploy-to-netlify.sh [commit message]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WEBSITE_DIR="$SCRIPT_DIR/../BallCode"

cd "$WEBSITE_DIR"

# Check if there are changes
if git diff --quiet && git diff --cached --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
    echo "✅ No changes to deploy"
    exit 0
fi

# Commit message
COMMIT_MSG="${1:-Deploy to Netlify: $(date +'%Y-%m-%d %H:%M:%S')}"

echo "🚀 Deploying to Netlify..."
echo ""

# Stage, commit, push
git add -A
git commit -m "$COMMIT_MSG" || echo "No changes to commit"
git push origin main

echo ""
echo "✅ Pushed to GitHub"

# Trigger Netlify if build hook is set
if [ -n "$NETLIFY_BUILD_HOOK" ]; then
    echo "🔔 Triggering Netlify deployment..."
    curl -X POST -d {} "$NETLIFY_BUILD_HOOK" > /dev/null 2>&1 && echo "✅ Netlify build triggered" || echo "⚠️  Netlify hook failed (check NETLIFY_BUILD_HOOK)"
fi

echo ""
echo "✅ Deployment complete!"
echo "📝 Site will update in 1-3 minutes: https://ballcode.co"

