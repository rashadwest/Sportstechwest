#!/bin/bash
# Robot Automation: Website Updates
# Auto-generates Episode 1 page and deploys website changes

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🤖 Robot: Website Update Automation${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check if BallCode directory exists
BALLCODE_DIR="BallCode"
if [ ! -d "$BALLCODE_DIR" ]; then
    echo -e "${RED}❌ BallCode directory not found${NC}"
    exit 1
fi

cd "$BALLCODE_DIR"

# Check if Episode 1 page already exists
EPISODE1_PAGE="episode1.html"
if [ -f "$EPISODE1_PAGE" ]; then
    echo -e "${YELLOW}⚠️  Episode 1 page already exists${NC}"
    echo -e "${CYAN}   Updating existing page...${NC}"
else
    echo -e "${CYAN}📄 Creating Episode 1 page...${NC}"
fi

# Create Episode 1 page template
cat > "$EPISODE1_PAGE" << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Episode 1: The Tip-off Trial - BallCODE</title>
    <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
    <header>
        <nav>
            <a href="/">Home</a>
            <a href="/books">Books</a>
            <a href="/curriculum">Curriculum</a>
        </nav>
    </header>
    
    <main class="episode-page">
        <h1>Episode 1: The Tip-off Trial</h1>
        
        <section class="episode-intro">
            <h2>About This Episode</h2>
            <p>Win first advantage by managing possession state from tip through transition.</p>
        </section>
        
        <section class="episode-content">
            <h2>Story Content</h2>
            <div id="episode-content">
                <!-- Content will be loaded from curriculum schema -->
                <p>Loading episode content...</p>
            </div>
        </section>
        
        <section class="episode-exercises">
            <h2>Practice Exercises</h2>
            <div id="episode-exercises">
                <!-- Exercises will be loaded from curriculum schema -->
            </div>
        </section>
        
        <section class="episode-game">
            <h2>Play the Game</h2>
            <a href="/play?book=1&exercise=1" class="btn btn-primary">Start Exercise</a>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2025 BallCODE. All rights reserved.</p>
    </footer>
    
    <script src="/assets/js/episode-loader.js"></script>
</body>
</html>
EOF

echo -e "${GREEN}✅ Episode 1 page created${NC}"

# Deploy to website
echo ""
echo -e "${CYAN}🚀 Deploying website changes...${NC}"

if [ -f "deploy-ballcode-website.sh" ]; then
    ./deploy-ballcode-website.sh
    echo -e "${GREEN}✅ Website deployed${NC}"
else
    echo -e "${YELLOW}⚠️  Deploy script not found - changes ready for manual deploy${NC}"
    echo -e "${CYAN}   Run: git add . && git commit -m 'Add Episode 1 page' && git push${NC}"
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Website Update Automation Complete${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"


