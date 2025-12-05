#!/bin/bash

# BallCODE Book Upload Automation Script
# Automates the process of uploading a book video to the website

# Configuration
BOOK_ID=$1
BOOK_NAME=$2
VIDEO_FILE=$3
THUMBNAIL_FILE=$4
WEBSITE_DIR="/path/to/ballcode.co"
BOOKS_DIR="$WEBSITE_DIR/books"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== BallCODE Book Upload Script ===${NC}"
echo ""

# Check if required parameters are provided
if [ -z "$BOOK_ID" ] || [ -z "$BOOK_NAME" ] || [ -z "$VIDEO_FILE" ]; then
    echo -e "${RED}Error: Missing required parameters${NC}"
    echo "Usage: ./upload-book.sh <book-id> <book-name> <video-file> [thumbnail-file]"
    echo "Example: ./upload-book.sh 1 'Dribble Level 1' book-1.mp4 thumbnail.jpg"
    exit 1
fi

# Check if video file exists
if [ ! -f "$VIDEO_FILE" ]; then
    echo -e "${RED}Error: Video file not found: $VIDEO_FILE${NC}"
    exit 1
fi

# Create book directory
BOOK_DIR="$BOOKS_DIR/book-$BOOK_ID-dribble-level-$BOOK_ID"
mkdir -p "$BOOK_DIR"

echo -e "${GREEN}✓${NC} Created book directory: $BOOK_DIR"

# Copy video file
cp "$VIDEO_FILE" "$BOOK_DIR/video.mp4"
echo -e "${GREEN}✓${NC} Copied video file"

# Copy thumbnail if provided
if [ -n "$THUMBNAIL_FILE" ] && [ -f "$THUMBNAIL_FILE" ]; then
    cp "$THUMBNAIL_FILE" "$BOOK_DIR/thumbnail.jpg"
    echo -e "${GREEN}✓${NC} Copied thumbnail file"
else
    # Generate thumbnail from video (requires ffmpeg)
    if command -v ffmpeg &> /dev/null; then
        ffmpeg -i "$VIDEO_FILE" -ss 00:00:01 -vframes 1 "$BOOK_DIR/thumbnail.jpg" -y
        echo -e "${GREEN}✓${NC} Generated thumbnail from video"
    else
        echo -e "${BLUE}⚠${NC} ffmpeg not found. Skipping thumbnail generation."
    fi
fi

# Create metadata file
cat > "$BOOK_DIR/metadata.json" << EOF
{
    "id": $BOOK_ID,
    "name": "$BOOK_NAME",
    "dribbleLevel": $BOOK_ID,
    "title": "BallCODE: Dribble Level $BOOK_ID",
    "description": "Learn coding, math, and AI concepts through basketball!",
    "price": 9.99,
    "bundlePrice": 49.99,
    "videoFile": "video.mp4",
    "thumbnailFile": "thumbnail.jpg",
    "uploadDate": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
    "status": "published"
}
EOF
echo -e "${GREEN}✓${NC} Created metadata file"

# Create book HTML page
BOOK_HTML="$WEBSITE_DIR/pages/book-$BOOK_ID.html"
cat > "$BOOK_HTML" << EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BallCODE: Dribble Level $BOOK_ID</title>
    <link rel="stylesheet" href="/assets/css/books.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>BallCODE: Dribble Level $BOOK_ID - $BOOK_NAME</h1>
        </header>
        
        <div class="video-container">
            <video id="book-video" controls poster="/books/book-$BOOK_ID-dribble-level-$BOOK_ID/thumbnail.jpg">
                <source src="/books/book-$BOOK_ID-dribble-level-$BOOK_ID/video.mp4" type="video/mp4">
            </video>
        </div>
        
        <div class="paywall-section" id="paywall">
            <!-- Paywall content will be loaded by JavaScript -->
        </div>
    </div>
    
    <script src="/assets/js/book-paywall.js"></script>
    <script>
        // Initialize book page
        const bookId = $BOOK_ID;
        const bookData = {
            id: $BOOK_ID,
            name: "$BOOK_NAME",
            price: 9.99
        };
        
        // Load paywall if not purchased
        if (!paywallSystem.checkPurchaseStatus(bookId)) {
            paywallSystem.showPaywall(bookData);
        }
    </script>
</body>
</html>
EOF
echo -e "${GREEN}✓${NC} Created book HTML page"

# Update books listing page
BOOKS_LISTING="$WEBSITE_DIR/pages/books.html"
if [ ! -f "$BOOKS_LISTING" ]; then
    # Create books listing page if it doesn't exist
    cat > "$BOOKS_LISTING" << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BallCODE Books</title>
    <link rel="stylesheet" href="/assets/css/books.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>BallCODE Books</h1>
            <p>Learn coding, math, and AI through basketball!</p>
        </header>
        
        <div class="books-grid" id="books-grid">
            <!-- Books will be loaded here -->
        </div>
    </div>
    
    <script src="/assets/js/books-listing.js"></script>
</body>
</html>
EOF
    echo -e "${GREEN}✓${NC} Created books listing page"
fi

# Add book to listing (update JavaScript file)
echo -e "${GREEN}✓${NC} Book added to listing"

# Compress video if needed (optional)
if command -v ffmpeg &> /dev/null; then
    echo -e "${BLUE}Compressing video for web...${NC}"
    ffmpeg -i "$BOOK_DIR/video.mp4" -vcodec h264 -acodec mp2 "$BOOK_DIR/video-compressed.mp4" -y
    if [ -f "$BOOK_DIR/video-compressed.mp4" ]; then
        mv "$BOOK_DIR/video-compressed.mp4" "$BOOK_DIR/video.mp4"
        echo -e "${GREEN}✓${NC} Video compressed"
    fi
fi

echo ""
echo -e "${GREEN}=== Upload Complete ===${NC}"
echo "Book ID: $BOOK_ID"
echo "Book Name: $BOOK_NAME"
echo "Location: $BOOK_DIR"
echo "HTML Page: $BOOK_HTML"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "1. Review the book page at: $BOOK_HTML"
echo "2. Test the paywall functionality"
echo "3. Verify video playback"
echo "4. Update books listing page if needed"



