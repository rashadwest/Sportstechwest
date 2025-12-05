#!/bin/bash

# Automated Testing Script for Books Section
# Tests the books section functionality

# Copyright © 2025 Rashad West. All Rights Reserved.

GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INDEX_FILE="$SCRIPT_DIR/BallCode/index.html"

echo -e "${BLUE}=== Books Section Testing ===${NC}\n"

# Test 1: Check if index.html exists
echo -e "${BLUE}Test 1:${NC} Checking if index.html exists..."
if [ -f "$INDEX_FILE" ]; then
    echo -e "${GREEN}✓${NC} index.html found"
else
    echo -e "${RED}✗${NC} index.html not found"
    exit 1
fi

# Test 2: Check for books section
echo -e "${BLUE}Test 2:${NC} Checking for books section..."
if grep -q "books-section\|books-grid\|books-card" "$INDEX_FILE"; then
    echo -e "${GREEN}✓${NC} Books section found"
else
    echo -e "${RED}✗${NC} Books section not found"
fi

# Test 3: Check for Book 1
echo -e "${BLUE}Test 3:${NC} Checking for Book 1..."
if grep -q "Book 1\|The Foundation Block" "$INDEX_FILE"; then
    echo -e "${GREEN}✓${NC} Book 1 found"
    if grep -q "gumroad.com" "$INDEX_FILE"; then
        echo -e "${GREEN}✓${NC} Gumroad link found"
    else
        echo -e "${YELLOW}⚠${NC} Gumroad link not found"
    fi
else
    echo -e "${RED}✗${NC} Book 1 not found"
fi

# Test 4: Check for Book 2
echo -e "${BLUE}Test 4:${NC} Checking for Book 2..."
if grep -q "Book 2\|The Code of Flow" "$INDEX_FILE"; then
    echo -e "${GREEN}✓${NC} Book 2 found"
    if grep -q "Coming Soon" "$INDEX_FILE"; then
        echo -e "${YELLOW}⚠${NC} Book 2 is still 'Coming Soon'"
    else
        echo -e "${GREEN}✓${NC} Book 2 is available"
    fi
else
    echo -e "${YELLOW}⚠${NC} Book 2 not found"
fi

# Test 5: Check for images
echo -e "${BLUE}Test 5:${NC} Checking for book images..."
IMAGES_DIR="$SCRIPT_DIR/BallCode/assets/images"
if [ -d "$IMAGES_DIR" ]; then
    if [ -f "$IMAGES_DIR/book1-title-page.png" ] || [ -f "$IMAGES_DIR/book1-title-page.jpg" ]; then
        echo -e "${GREEN}✓${NC} Book 1 image found"
    else
        echo -e "${YELLOW}⚠${NC} Book 1 image not found"
    fi
    
    if [ -f "$IMAGES_DIR/book2-title-page.png" ] || [ -f "$IMAGES_DIR/book2-title-page.jpg" ]; then
        echo -e "${GREEN}✓${NC} Book 2 image found"
    else
        echo -e "${YELLOW}⚠${NC} Book 2 image not found"
    fi
else
    echo -e "${YELLOW}⚠${NC} Images directory not found"
fi

# Test 6: Check HTML structure
echo -e "${BLUE}Test 6:${NC} Checking HTML structure..."
if grep -q "books-card" "$INDEX_FILE" && grep -q "books-card-button" "$INDEX_FILE"; then
    echo -e "${GREEN}✓${NC} HTML structure looks good"
else
    echo -e "${YELLOW}⚠${NC} HTML structure may be incomplete"
fi

# Summary
echo ""
echo -e "${BLUE}=== Test Summary ===${NC}"
echo "Run 'open $INDEX_FILE' to view in browser"
echo "Or visit your live site to test purchase flow"


