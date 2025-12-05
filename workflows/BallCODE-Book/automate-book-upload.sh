#!/bin/bash

# Automated Book Upload Script
# Automates the process of adding a new book to the website

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== BallCODE Book Upload Automation ===${NC}"
echo ""

# Configuration
BOOK_NUMBER=$1
BOOK_TITLE=$2
BOOK_DESCRIPTION=$3
GUMROAD_URL=$4
THUMBNAIL_PATH=$5
PRICE=${6:-5}

# Validate inputs
if [ -z "$BOOK_NUMBER" ] || [ -z "$BOOK_TITLE" ] || [ -z "$GUMROAD_URL" ]; then
    echo -e "${RED}Error: Missing required parameters${NC}"
    echo "Usage: ./automate-book-upload.sh <book-number> <book-title> <description> <gumroad-url> [thumbnail-path] [price]"
    echo ""
    echo "Example:"
    echo "./automate-book-upload.sh 2 \"The Code of Flow\" \"Learn if/then logic through basketball\" \"https://gumroad.com/l/xyz\" \"./book2-thumbnail.png\" 5"
    exit 1
fi

# Set default description if not provided
if [ -z "$BOOK_DESCRIPTION" ]; then
    BOOK_DESCRIPTION="Learn AI, Math, and Coding through basketball stories."
fi

# Paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WEBSITE_DIR="$SCRIPT_DIR/BallCode"
INDEX_FILE="$WEBSITE_DIR/index.html"
IMAGES_DIR="$WEBSITE_DIR/assets/images"
THUMBNAIL_NAME="book${BOOK_NUMBER}-title-page.png"

echo -e "${BLUE}Book Number:${NC} $BOOK_NUMBER"
echo -e "${BLUE}Book Title:${NC} $BOOK_TITLE"
echo -e "${BLUE}Gumroad URL:${NC} $GUMROAD_URL"
echo -e "${BLUE}Price:${NC} \$$PRICE"
echo ""

# Step 1: Copy thumbnail image
if [ -n "$THUMBNAIL_PATH" ] && [ -f "$THUMBNAIL_PATH" ]; then
    echo -e "${BLUE}Step 1:${NC} Copying thumbnail image..."
    cp "$THUMBNAIL_PATH" "$IMAGES_DIR/$THUMBNAIL_NAME"
    echo -e "${GREEN}✓${NC} Thumbnail copied to $IMAGES_DIR/$THUMBNAIL_NAME"
else
    echo -e "${YELLOW}⚠${NC} No thumbnail provided. Using fallback image."
fi

# Step 2: Update index.html
echo -e "${BLUE}Step 2:${NC} Updating website HTML..."

# Create the book card HTML
BOOK_CARD=$(cat <<EOF
              <!-- Book ${BOOK_NUMBER}: ${BOOK_TITLE} -->
              <div class="books-card">
                <div class="books-card-thumbnail">
                  <img src="/assets/images/${THUMBNAIL_NAME}" alt="Book ${BOOK_NUMBER}: ${BOOK_TITLE}" />
                  <span class="books-card-badge">Available</span>
                  <span class="books-card-play">▶</span>
                </div>
                <div class="books-card-content">
                  <div class="books-card-title-wrapper">
                    <img src="/assets/images/${THUMBNAIL_NAME}" 
                         alt="Book ${BOOK_NUMBER}: ${BOOK_TITLE}" 
                         class="books-card-title-image"
                         onerror="this.style.display='none'; this.nextElementSibling.style.display='block';" />
                    <h3 class="books-card-title books-card-title-fallback" style="display: none;">Book ${BOOK_NUMBER}: ${BOOK_TITLE}</h3>
                  </div>
                  <p class="books-card-text">${BOOK_DESCRIPTION}</p>
                  
                  <div class="books-card-includes">
                    <p class="books-card-includes-title">📚 What's Included:</p>
                    <ul class="books-card-includes-list">
                      <li>Interactive video book</li>
                      <li>Game access password (instant delivery)</li>
                      <li>Curriculum level #${BOOK_NUMBER} unlock</li>
                    </ul>
                  </div>
                  
                  <p class="books-card-price">\$${PRICE}</p>
                  <a href="${GUMROAD_URL}" target="_blank" class="books-card-button">Buy Book ${BOOK_NUMBER} →</a>
                  
                  <details class="books-card-access-info">
                    <summary class="books-card-access-summary">🎮 How to Access After Purchase</summary>
                    <div class="books-card-access-details">
                      <ol>
                        <li>Get password instantly on thank you page</li>
                        <li>Click "Access Game Now" (or go to ballcode.netlify.app)</li>
                        <li>Sign up or log in to the game</li>
                        <li>Navigate to: <strong>Ballcode mode → Curriculum → Play → #${BOOK_NUMBER}</strong></li>
                        <li>Enter your password to unlock the level</li>
                      </ol>
                    </div>
                  </details>
                </div>
              </div>
EOF
)

# Check if Book 2 "Coming Soon" exists and replace it, or add new book
if grep -q "Book ${BOOK_NUMBER}:.*Coming Soon" "$INDEX_FILE"; then
    echo -e "${BLUE}Found 'Coming Soon' placeholder for Book ${BOOK_NUMBER}, replacing...${NC}"
    # Use Python for more reliable HTML replacement
    python3 <<PYTHON_SCRIPT
import re

with open("$INDEX_FILE", "r") as f:
    content = f.read()

# Find and replace the Coming Soon book card
pattern = r'(<!-- Book ' + str($BOOK_NUMBER) + r':.*?Coming Soon.*?</div>\s*</div>)'
replacement = '''$BOOK_CARD'''

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open("$INDEX_FILE", "w") as f:
    f.write(new_content)

print("✓ Replaced Coming Soon placeholder")
PYTHON_SCRIPT
else
    echo -e "${BLUE}Adding new book card to books grid...${NC}"
    # Add before closing books-grid div
    sed -i.bak "/<\/div>\s*<\/div>\s*<\/section>/i\\
$BOOK_CARD
" "$INDEX_FILE"
fi

echo -e "${GREEN}✓${NC} Website HTML updated"

# Step 3: Git operations
echo -e "${BLUE}Step 3:${NC} Preparing git commit..."

cd "$WEBSITE_DIR"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo -e "${YELLOW}⚠${NC} Git not initialized. Skipping git operations."
    echo -e "${BLUE}Next steps:${NC}"
    echo "1. Initialize git: git init"
    echo "2. Add remote: git remote add origin <your-repo-url>"
    echo "3. Commit and push manually"
    exit 0
fi

# Check git status
if ! git diff --quiet || ! git diff --cached --quiet || [ -n "$(git ls-files --others --exclude-standard)" ]; then
    echo -e "${BLUE}Staging changes...${NC}"
    git add index.html
    [ -f "$IMAGES_DIR/$THUMBNAIL_NAME" ] && git add "$IMAGES_DIR/$THUMBNAIL_NAME"
    
    echo -e "${BLUE}Committing changes...${NC}"
    git commit -m "Add Book ${BOOK_NUMBER}: ${BOOK_TITLE} to website"
    
    echo -e "${GREEN}✓${NC} Changes committed"
    echo ""
    echo -e "${YELLOW}⚠${NC} Ready to push. Run manually:"
    echo "  cd $WEBSITE_DIR"
    echo "  git push origin main"
else
    echo -e "${BLUE}No changes to commit${NC}"
fi

# Step 4: Summary
echo ""
echo -e "${GREEN}=== Upload Complete ===${NC}"
echo -e "${BLUE}Book ${BOOK_NUMBER}:${NC} ${BOOK_TITLE}"
echo -e "${BLUE}Status:${NC} Available"
echo -e "${BLUE}Price:${NC} \$${PRICE}"
echo -e "${BLUE}Gumroad:${NC} ${GUMROAD_URL}"
echo ""
echo -e "${BLUE}Files Modified:${NC}"
echo "  - $INDEX_FILE"
[ -f "$IMAGES_DIR/$THUMBNAIL_NAME" ] && echo "  - $IMAGES_DIR/$THUMBNAIL_NAME"
echo ""
echo -e "${BLUE}Next Steps:${NC}"
echo "1. Review changes: git diff"
echo "2. Push to GitHub: git push origin main"
echo "3. Verify on live site"
echo "4. Test purchase flow"


