#!/bin/bash

# Cursor Evidence Collection Script
# Purpose: Collect evidence for legal/regulatory purposes
# Usage: ./collect-cursor-evidence.sh

set -e  # Exit on error

echo "=========================================="
echo "Cursor Evidence Collection Script"
echo "=========================================="
echo ""

# Get current date
DATE=$(date +%Y-%m-%d)
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)

# Create evidence directory
EVIDENCE_DIR="CURSOR-EVIDENCE"
mkdir -p "$EVIDENCE_DIR"
mkdir -p "$EVIDENCE_DIR/settings-screenshots"
mkdir -p "$EVIDENCE_DIR/legal-documents"

echo "✅ Created evidence directory: $EVIDENCE_DIR"
echo ""

# Repository information
REPO_PATH="/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book"
cd "$REPO_PATH" || exit 1

echo "📊 Collecting repository statistics..."
echo ""

# File counts
echo "Counting files..."
TOTAL_FILES=$(find . -type f ! -path "./.git/*" ! -path "./node_modules/*" ! -path "./venv/*" ! -path "./$EVIDENCE_DIR/*" | wc -l | tr -d ' ')
MD_FILES=$(find . -name "*.md" ! -path "./.git/*" ! -path "./$EVIDENCE_DIR/*" | wc -l | tr -d ' ')
PY_FILES=$(find . -name "*.py" ! -path "./.git/*" ! -path "./$EVIDENCE_DIR/*" | wc -l | tr -d ' ')
CS_FILES=$(find . -name "*.cs" ! -path "./.git/*" ! -path "./$EVIDENCE_DIR/*" | wc -l | tr -d ' ')
JS_FILES=$(find . -name "*.js" ! -path "./.git/*" ! -path "./$EVIDENCE_DIR/*" | wc -l | tr -d ' ')
JSON_FILES=$(find . -name "*.json" ! -path "./.git/*" ! -path "./$EVIDENCE_DIR/*" | wc -l | tr -d ' ')

# Create summary file
SUMMARY_FILE="$EVIDENCE_DIR/CODEBASE-INVENTORY-LEGAL.txt"
cat > "$SUMMARY_FILE" << EOF
========================================
CODEBASE INVENTORY FOR LEGAL PURPOSES
========================================

Generated: $DATE $TIMESTAMP
Repository: BallCODE-Book
Repository Path: $REPO_PATH

FILE STATISTICS:
---------------
Total Files: $TOTAL_FILES
Markdown Files (.md): $MD_FILES
Python Files (.py): $PY_FILES
C# Files (.cs): $CS_FILES
JavaScript Files (.js): $JS_FILES
JSON Files (.json): $JSON_FILES

ACTIVITY PERIOD:
---------------
Start Date: 2024-09-04 (first commit)
End Date: $(date +%Y-%m-%d) (today)
Total Days: [Calculate from git history]

GIT HISTORY:
------------
Total Commits: $(git log --all --format="%H" | wc -l | tr -d ' ')
First Commit: $(git log --all --format="%ai" | tail -1)
Last Commit: $(git log --all --format="%ai" | head -1)

CURSOR EVIDENCE:
---------------
.cursorrules File: $(test -f .cursorrules && echo "EXISTS ($(wc -l < .cursorrules) lines)" || echo "NOT FOUND")
Cursor References: $(grep -r -i "cursor" --include="*.md" . 2>/dev/null | wc -l | tr -d ' ') mentions in documentation

PURPOSE:
--------
This inventory is collected for legal/regulatory purposes to document
the codebase that may have been used by Cursor Data, Inc. for AI
model training.

LEGAL NOTICE:
-------------
This inventory is prepared for potential legal action, regulatory
complaints, and data protection requests under GDPR, CCPA, and other
applicable privacy laws.

========================================
EOF

echo "✅ Created summary: $SUMMARY_FILE"
echo ""

# Export git history
echo "📜 Exporting git history..."
GIT_HISTORY="$EVIDENCE_DIR/git-history.txt"
git log --all --format="%ai|%H|%an|%s" > "$GIT_HISTORY"
echo "✅ Exported git history: $GIT_HISTORY ($(wc -l < "$GIT_HISTORY" | tr -d ' ') commits)"
echo ""

# Export file list
echo "📁 Exporting file list..."
FILE_LIST="$EVIDENCE_DIR/file-list.txt"
find . -type f ! -path "./.git/*" ! -path "./node_modules/*" ! -path "./venv/*" ! -path "./$EVIDENCE_DIR/*" | sort > "$FILE_LIST"
echo "✅ Exported file list: $FILE_LIST ($(wc -l < "$FILE_LIST" | tr -d ' ') files)"
echo ""

# Copy .cursorrules if exists
if [ -f .cursorrules ]; then
    echo "📋 Copying .cursorrules..."
    cp .cursorrules "$EVIDENCE_DIR/.cursorrules"
    echo "✅ Copied .cursorrules ($(wc -l < .cursorrules | tr -d ' ') lines)"
    echo ""
else
    echo "⚠️  .cursorrules not found"
    echo ""
fi

# Find all Cursor-related files
echo "🔍 Finding Cursor-related files..."
CURSOR_FILES="$EVIDENCE_DIR/cursor-related-files.txt"
find . -type f \( -name "*cursor*" -o -name ".cursorrules" \) ! -path "./.git/*" ! -path "./$EVIDENCE_DIR/*" > "$CURSOR_FILES" 2>/dev/null || echo "No Cursor-specific files found" > "$CURSOR_FILES"
echo "✅ Found Cursor-related files: $CURSOR_FILES"
echo ""

# Search for Cursor mentions in documentation
echo "📝 Searching for Cursor mentions..."
CURSOR_MENTIONS="$EVIDENCE_DIR/cursor-mentions.txt"
grep -r -i "cursor" --include="*.md" --include="*.txt" . 2>/dev/null | grep -v "^\./$EVIDENCE_DIR" > "$CURSOR_MENTIONS" || echo "No Cursor mentions found" > "$CURSOR_MENTIONS"
echo "✅ Found Cursor mentions: $CURSOR_MENTIONS ($(wc -l < "$CURSOR_MENTIONS" | tr -d ' ') lines)"
echo ""

# Create file type breakdown
echo "📊 Creating file type breakdown..."
FILE_BREAKDOWN="$EVIDENCE_DIR/file-type-breakdown.txt"
cat > "$FILE_BREAKDOWN" << EOF
File Type Breakdown
==================

Markdown (.md):     $MD_FILES files
Python (.py):       $PY_FILES files
C# (.cs):           $CS_FILES files
JavaScript (.js):   $JS_FILES files
JSON (.json):       $JSON_FILES files
Other:              $((TOTAL_FILES - MD_FILES - PY_FILES - CS_FILES - JS_FILES - JSON_FILES)) files

Total:              $TOTAL_FILES files
EOF
echo "✅ Created file breakdown: $FILE_BREAKDOWN"
echo ""

# Create activity timeline
echo "📅 Creating activity timeline..."
TIMELINE="$EVIDENCE_DIR/activity-timeline.txt"
git log --all --format="%ai|%s" --date=iso | head -50 > "$TIMELINE"
echo "✅ Created activity timeline: $TIMELINE"
echo ""

# Check for copyright notices
echo "©️  Checking for copyright notices..."
COPYRIGHT_CHECK="$EVIDENCE_DIR/copyright-notices.txt"
grep -r -i "copyright" --include="*.md" --include="*.py" --include="*.cs" --include="*.js" . 2>/dev/null | grep -v "^\./$EVIDENCE_DIR" > "$COPYRIGHT_CHECK" || echo "No copyright notices found" > "$COPYRIGHT_CHECK"
echo "✅ Checked copyright notices: $COPYRIGHT_CHECK"
echo ""

# Create README for evidence directory
README="$EVIDENCE_DIR/README.md"
cat > "$README" << 'EOF'
# Cursor Evidence Collection

This directory contains evidence collected for legal/regulatory purposes
regarding potential use of this codebase by Cursor Data, Inc. for AI model
training.

## Contents

- `CODEBASE-INVENTORY-LEGAL.txt` - Complete codebase inventory
- `git-history.txt` - Complete git commit history
- `file-list.txt` - Complete list of all files
- `file-type-breakdown.txt` - Breakdown by file type
- `activity-timeline.txt` - Timeline of repository activity
- `cursor-related-files.txt` - Files specifically related to Cursor
- `cursor-mentions.txt` - Documentation mentioning Cursor
- `copyright-notices.txt` - Copyright notices found in codebase
- `.cursorrules` - Cursor configuration file (if exists)
- `settings-screenshots/` - Screenshots of Cursor settings (add manually)
- `legal-documents/` - Cursor Terms of Service, Privacy Policy (add manually)

## Purpose

This evidence is collected for:
- GDPR data access requests
- CCPA data disclosure requests
- Regulatory complaints
- Potential legal action
- Documentation of codebase state

## Legal Notice

This evidence is prepared for legal/regulatory purposes under applicable
privacy laws including GDPR, CCPA, and other data protection regulations.

## Next Steps

1. Review all collected evidence
2. Add screenshots of Cursor settings to `settings-screenshots/`
3. Download and save Cursor's Terms of Service and Privacy Policy to `legal-documents/`
4. Use this evidence in formal requests to Cursor
5. Include in regulatory complaints if needed
6. Provide to legal counsel if pursuing legal action

## Generated

Generated: [DATE]
Repository: BallCODE-Book
Path: /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
EOF

# Update README with actual date
sed -i '' "s/\[DATE\]/$DATE/g" "$README"

echo "✅ Created README: $README"
echo ""

# Create hash file for integrity
echo "🔐 Creating integrity checksums..."
CHECKSUMS="$EVIDENCE_DIR/checksums.txt"
find "$EVIDENCE_DIR" -type f ! -name "checksums.txt" -exec shasum -a 256 {} \; > "$CHECKSUMS"
echo "✅ Created checksums: $CHECKSUMS"
echo ""

# Final summary
echo "=========================================="
echo "✅ EVIDENCE COLLECTION COMPLETE"
echo "=========================================="
echo ""
echo "Evidence collected in: $EVIDENCE_DIR/"
echo "Total files collected: $(find "$EVIDENCE_DIR" -type f | wc -l | tr -d ' ')"
echo ""
echo "Next Steps:"
echo "1. Review $SUMMARY_FILE"
echo "2. Add Cursor settings screenshots to $EVIDENCE_DIR/settings-screenshots/"
echo "3. Download Cursor's legal documents to $EVIDENCE_DIR/legal-documents/"
echo "4. Use evidence in formal requests to Cursor"
echo ""
echo "See CURSOR-ACCOUNTABILITY-QUICK-START.md for next steps"
echo ""




