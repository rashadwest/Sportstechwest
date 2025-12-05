#!/bin/bash
# Download Glif images and save to correct paths
# Usage: ./download-glif-images.sh <hero-url> <arch-url> <workflows-url> <comparison-url>

if [ $# -ne 4 ]; then
  echo "Usage: ./download-glif-images.sh <hero-url> <arch-url> <workflows-url> <comparison-url>"
  echo ""
  echo "Example:"
  echo "./download-glif-images.sh https://glif.app/... https://glif.app/... https://glif.app/... https://glif.app/..."
  exit 1
fi

BLOG_DIR="/Users/rashadwest/Sportstechwest"
IMG_DIR="$BLOG_DIR/assets/images/blog-img"

# Create directory if it doesn't exist
mkdir -p "$IMG_DIR"

echo "📥 Downloading images..."

# Download each image
curl -L "$1" -o "$IMG_DIR/24-7-server-hero.png" && echo "✅ Hero image saved" || echo "❌ Failed to download hero image"
curl -L "$2" -o "$IMG_DIR/24-7-server-architecture.png" && echo "✅ Architecture image saved" || echo "❌ Failed to download architecture image"
curl -L "$3" -o "$IMG_DIR/24-7-automation-workflows.png" && echo "✅ Workflows image saved" || echo "❌ Failed to download workflows image"
curl -L "$4" -o "$IMG_DIR/24-7-server-comparison.png" && echo "✅ Comparison image saved" || echo "❌ Failed to download comparison image"

echo ""
echo "📦 Next steps:"
echo "  cd $BLOG_DIR"
echo "  git add assets/images/blog-img/24-7-*.png"
echo "  git commit -m 'Replace placeholder images with Glif-generated images'"
echo "  git push origin main"
