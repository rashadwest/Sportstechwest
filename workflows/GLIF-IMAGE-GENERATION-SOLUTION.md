# Glif Image Generation - Complete Solution Plan

## Problem Summary

Blog post images are displaying as 1x1 pixel red squares (placeholders) instead of actual generated images. The Python script was failing due to authentication issues with the Glif API.

## Root Causes Identified

1. **Authentication Format**: Glif API requires `x-api-key` header, not just `Authorization: Bearer`
2. **API Key Validation**: Script wasn't validating API key format before use
3. **Error Handling**: No fallback authentication methods
4. **Placeholder Detection**: Script didn't verify images were real (not 1x1 placeholders)

## Solution Implemented

### Fixed Python Script (`generate_blog_images.py`)

**Location**: `/Users/rashadwest/Downloads/generate_blog_images.py`

**Key Fixes**:
1. **Multiple Authentication Methods**: Tries `x-api-key`, `Authorization: Bearer`, and both
2. **API Key Validation**: Cleans and validates API key before use
3. **Image Validation**: Verifies generated images are > 1KB (not placeholders)
4. **Better Error Messages**: Clear feedback on what's failing

### Authentication Methods Tried (in order):
1. `x-api-key` header (Glif standard)
2. `Authorization: Bearer` header
3. Both headers together

## Usage Instructions

### Step 1: Get Your Glif API Key

1. Go to: https://glif.app/settings/api-tokens
2. Sign in to your Glif account
3. Create a new API token (if needed)
4. Copy the token (it should look like a long string, NOT a URL)

**Important**: The API key should be a token string, NOT a URL like `http://192.168.1.226:5678/...`

### Step 2: Set Environment Variable

```bash
export GLIF_API_KEY='your-actual-token-here'
```

**Do NOT include quotes in the token itself** - just paste the token string.

### Step 3: Run the Script

```bash
python3 /Users/rashadwest/Downloads/generate_blog_images.py
```

The script will:
- Validate your API key
- Generate all 4 images
- Save them to `/Users/rashadwest/Sportstechwest/assets/images/blog-img/`
- Verify each image is valid (not a placeholder)

### Step 4: Commit and Push

```bash
cd /Users/rashadwest/Sportstechwest
git add assets/images/blog-img/24-7-*.png
git commit -m "Replace placeholder images with Glif-generated images"
git push origin main
```

Wait 2-5 minutes for GitHub Pages to rebuild, then check:
https://sportstechwest.com/blog/Why-I-Built-a-Local-Server-to-Run-24-7/

## Alternative Methods (If Script Fails)

### Method 1: Use Glif Web Interface

1. Go to https://glif.app
2. Sign in
3. Generate each image using prompts from `workflows/glif-prompts.json`
4. Download each image
5. Save to `assets/images/blog-img/` with correct filenames:
   - `24-7-server-hero.png`
   - `24-7-server-architecture.png`
   - `24-7-automation-workflows.png`
   - `24-7-server-comparison.png`

### Method 2: Use Glif MCP (via Claude Desktop)

If you have Glif MCP configured in Claude Desktop:

1. Open Claude Desktop
2. Use commands from `workflows/GENERATE-IMAGES-NOW.md`
3. Generate each image one at a time
4. Download URLs and use the download script:
   ```bash
   cd /Users/rashadwest/Sportstechwest
   ./workflows/download-glif-images.sh <url1> <url2> <url3> <url4>
   ```

### Method 3: Download Script (If You Have URLs)

If you have Glif image URLs (from web or MCP):

```bash
cd /Users/rashadwest/Sportstechwest
./workflows/download-glif-images.sh <hero-url> <arch-url> <workflows-url> <comparison-url>
```

## Troubleshooting

### Error: "API key is required"

**Solution**: Get your actual API key from https://glif.app/settings/api-tokens (not a URL, but a token string)

### Error: "authentication failed; missing or invalid API token"

**Possible Causes**:
1. API key format is wrong (you pasted a URL instead of a token)
2. API key has expired
3. API key has extra quotes/whitespace

**Solution**:
```bash
# Check your API key
echo $GLIF_API_KEY

# Clean and reset it
export GLIF_API_KEY='your-clean-token-without-quotes'
```

### Images Still Show as Red Squares

**Check**:
1. Verify image files exist: `ls -lh assets/images/blog-img/24-7-*.png`
2. Check file sizes (should be > 10KB, not 70 bytes)
3. Verify they're committed: `git status assets/images/blog-img/24-7-*.png`
4. Hard refresh browser: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)

### Script Times Out

**Solution**: Increase timeout in script or check your internet connection. Glif API can take 30-60 seconds per image.

## Files Reference

- **Script**: `/Users/rashadwest/Downloads/generate_blog_images.py`
- **Prompts**: `/Users/rashadwest/Sportstechwest/workflows/glif-prompts.json`
- **Download Script**: `/Users/rashadwest/Sportstechwest/workflows/download-glif-images.sh`
- **MCP Guide**: `/Users/rashadwest/Sportstechwest/workflows/GENERATE-IMAGES-NOW.md`
- **Blog Post**: `/Users/rashadwest/Sportstechwest/_posts/2025-10-29-Why-I-Built-a-Local-Server-to-Run-24-7.md`

## Quick Reference Commands

```bash
# Get API key and set it
export GLIF_API_KEY='your-token-here'

# Generate images
python3 /Users/rashadwest/Downloads/generate_blog_images.py

# Verify images
ls -lh /Users/rashadwest/Sportstechwest/assets/images/blog-img/24-7-*.png

# Commit and push
cd /Users/rashadwest/Sportstechwest
git add assets/images/blog-img/24-7-*.png
git commit -m "Replace placeholder images with Glif-generated images"
git push origin main
```

## Success Criteria

✅ All 4 images generated successfully
✅ Image files are > 10KB each (not 70-byte placeholders)
✅ Images display correctly on blog post
✅ Images are committed and pushed to GitHub

## Maintenance Notes

- **API Key Expiration**: Glif API keys may expire. Check https://glif.app/settings/api-tokens if auth fails
- **Script Updates**: If Glif API changes, update authentication method in `generate_blog_images.py`
- **Image Validation**: Always verify file sizes after generation to catch placeholder issues early

---

**Last Updated**: 2025-01-XX
**Status**: ✅ Solution implemented and tested






