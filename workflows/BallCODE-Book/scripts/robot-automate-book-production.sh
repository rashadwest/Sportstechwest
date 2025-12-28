#!/bin/bash
# Robot Automation: Book Production
# Auto-generates book pages from content and syncs with curriculum

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
echo -e "${BLUE}🤖 Robot: Book Production Automation${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check if BallCode directory exists
BALLCODE_DIR="BallCode"
if [ ! -d "$BALLCODE_DIR" ]; then
    echo -e "${RED}❌ BallCode directory not found${NC}"
    exit 1
fi

cd "$BALLCODE_DIR"

# Check for curriculum schema
CURRICULUM_SCHEMA="../CURRICULUM-DATA-EXAMPLE.json"
if [ ! -f "$CURRICULUM_SCHEMA" ]; then
    echo -e "${YELLOW}⚠️  Curriculum schema not found${NC}"
    echo -e "${CYAN}   Creating basic book pages...${NC}"
else
    echo -e "${GREEN}✅ Found curriculum schema${NC}"
    echo -e "${CYAN}   Syncing books with curriculum...${NC}"
fi

# Create books directory if it doesn't exist
BOOKS_DIR="books"
mkdir -p "$BOOKS_DIR"

# Function to generate book page
generate_book_page() {
    local book_num=$1
    local book_name=$2
    
    local page_file="$BOOKS_DIR/book${book_num}.html"
    
    echo -e "${CYAN}📖 Generating Book ${book_num} page...${NC}"
    
    cat > "$page_file" << EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book ${book_num}: ${book_name} - BallCODE</title>
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
    
    <main class="book-page">
        <h1>Book ${book_num}: ${book_name}</h1>
        
        <section class="what-youre-learning">
            <h2>What You're Learning</h2>
            <div id="learning-objectives">
                <!-- Loaded from curriculum schema -->
            </div>
        </section>
        
        <section class="book-content">
            <h2>Story</h2>
            <div id="book-content">
                <!-- Story content loaded from curriculum schema -->
            </div>
        </section>
        
        <section class="book-exercises">
            <h2>Practice Exercises</h2>
            <div id="exercises">
                <!-- Exercises loaded from curriculum schema -->
            </div>
        </section>
        
        <section class="what-you-learned">
            <h2>What You Learned</h2>
            <div id="learned-content">
                <!-- Summary loaded from curriculum schema -->
            </div>
        </section>
        
        <section class="next-book">
            <h2>Continue Learning</h2>
            <div id="next-book-recommendation">
                <!-- Next book recommendation loaded from curriculum schema -->
            </div>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2025 BallCODE. All rights reserved.</p>
    </footer>
    
    <script src="/assets/js/book-loader.js"></script>
</body>
</html>
EOF

    echo -e "${GREEN}✅ Book ${book_num} page created${NC}"
}

# Generate pages for Books 1-3
generate_book_page 1 "Foundation"
generate_book_page 2 "Decision"
generate_book_page 3 "Pattern"

echo ""
echo -e "${CYAN}🔄 Syncing with curriculum schema...${NC}"

# Create book loader script if it doesn't exist
JS_DIR="assets/js"
mkdir -p "$JS_DIR"

cat > "$JS_DIR/book-loader.js" << 'EOF'
// Book Content Loader
// Loads book content from curriculum schema API

document.addEventListener('DOMContentLoaded', function() {
    const bookNum = window.location.pathname.match(/book(\d+)/)?.[1];
    if (!bookNum) return;
    
    // Load book data from API
    fetch(`/api/book/${bookNum}`)
        .then(response => response.json())
        .then(data => {
            // Populate learning objectives
            const learningEl = document.getElementById('learning-objectives');
            if (learningEl && data.learningObjectives) {
                learningEl.innerHTML = data.learningObjectives.map(obj => 
                    `<li>${obj}</li>`
                ).join('');
            }
            
            // Populate book content
            const contentEl = document.getElementById('book-content');
            if (contentEl && data.content) {
                contentEl.innerHTML = data.content;
            }
            
            // Populate exercises
            const exercisesEl = document.getElementById('exercises');
            if (exercisesEl && data.exercises) {
                exercisesEl.innerHTML = data.exercises.map(ex => 
                    `<div class="exercise">
                        <h3>${ex.title}</h3>
                        <p>${ex.description}</p>
                        <a href="${ex.gameUrl}" class="btn btn-primary">Play Exercise</a>
                    </div>`
                ).join('');
            }
            
            // Populate learned content
            const learnedEl = document.getElementById('learned-content');
            if (learnedEl && data.learned) {
                learnedEl.innerHTML = data.learned;
            }
            
            // Populate next book
            const nextBookEl = document.getElementById('next-book-recommendation');
            if (nextBookEl && data.nextBook) {
                nextBookEl.innerHTML = `
                    <p>${data.nextBook.description}</p>
                    <a href="${data.nextBook.url}" class="btn btn-primary">Continue to Book ${data.nextBook.number}</a>
                `;
            }
        })
        .catch(error => {
            console.error('Error loading book content:', error);
        });
});
EOF

echo -e "${GREEN}✅ Book loader script created${NC}"

# Deploy changes
echo ""
echo -e "${CYAN}🚀 Deploying book pages...${NC}"

if [ -f "deploy-ballcode-website.sh" ]; then
    ./deploy-ballcode-website.sh
    echo -e "${GREEN}✅ Book pages deployed${NC}"
else
    echo -e "${YELLOW}⚠️  Deploy script not found - changes ready for manual deploy${NC}"
    echo -e "${CYAN}   Run: git add . && git commit -m 'Add book production pages' && git push${NC}"
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Book Production Automation Complete${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"


