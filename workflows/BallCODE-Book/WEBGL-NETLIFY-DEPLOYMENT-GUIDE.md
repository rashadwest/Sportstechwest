# WebGL + Netlify Deployment Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** November 26, 2025  
**Status:** Complete Deployment Guide  
**Purpose:** Deploy Unity WebGL build to Netlify with book integration support

---

## Overview

This guide covers deploying the Unity WebGL build to Netlify with full support for book-game integration, including:
- JavaScript bridge for exercise completion communication
- URL parameter handling for book exercises
- Return flow to website after exercise completion

---

## Prerequisites

1. **Unity Project** with WebGL build capability
2. **Netlify Account** (free tier works)
3. **Netlify CLI** installed (`npm install -g netlify-cli`)
4. **Unity WebGL Build** ready (or instructions to create one)

---

## Step 1: Unity WebGL Build Configuration

### Build Settings

1. **Open Unity Project**
2. **File → Build Settings**
3. **Select WebGL** as platform
4. **Player Settings** → Configure:

**WebGL Settings:**
- **Compression Format:** Gzip (recommended) or Brotli
- **Data Caching:** Enabled
- **Memory Size:** Adjust based on your game (default 256MB usually works)
- **Code Optimization:** Size or Speed (Size recommended for web)

**Publishing Settings:**
- **Template:** Default (or custom if you have one)
- **Decompression Fallback:** Enabled (for older browsers)

### Include Book Integration Scripts

Ensure these scripts are included in the build:
- ✅ `BallCODEStarter.cs` (with book parameter support)
- ✅ `GameModeManager.cs` (with return flow)
- ✅ `BookReturnHandler.cs` (JavaScript communication)
- ✅ `LevelDataManager.cs` (for loading book exercises)
- ✅ All LevelData JSON files in `StreamingAssets/Levels/`

### Build Output

**Build Location:** `YourUnityProject/Builds/WebGL/`

**Required Files:**
- `index.html` (main entry point)
- `Build/` folder (contains .wasm, .js, .data files)
- `StreamingAssets/` folder (contains LevelData JSON files)

---

## Step 2: Add JavaScript Bridge to WebGL Build

### Update Unity WebGL Template

The WebGL build needs a JavaScript bridge function for book integration. You need to modify the `index.html` in your WebGL build.

**Location:** `Builds/WebGL/index.html`

**Add this JavaScript function** (before closing `</body>` tag):

```html
<script>
// Book Integration JavaScript Bridge
// This function is called by Unity's Application.ExternalCall

function SendExerciseComplete(bookNumber, success, score) {
    console.log(`Exercise complete: Book ${bookNumber}, Success: ${success}, Score: ${score}`);
    
    // Send message to parent window (if in iframe)
    if (window.parent && window.parent !== window) {
        window.parent.postMessage({
            type: 'exerciseComplete',
            book: bookNumber,
            success: success === 1,
            score: score
        }, '*');
    }
    
    // Also try URL redirect as fallback
    var returnUrl = localStorage.getItem('bookReturnUrl') || `/books/book${bookNumber}`;
    var redirectUrl = `${returnUrl}?exercise=complete&success=${success}&score=${score}`;
    
    // Redirect after short delay to allow message to be sent
    setTimeout(function() {
        if (window.parent && window.parent !== window) {
            // If in iframe, try to redirect parent
            window.parent.location.href = redirectUrl;
        } else {
            // If not in iframe, redirect current window
            window.location.href = redirectUrl;
        }
    }, 2000);
}

// Store return URL when game loads (called from Unity)
function SetBookReturnUrl(returnUrl) {
    localStorage.setItem('bookReturnUrl', returnUrl);
    console.log(`Book return URL set: ${returnUrl}`);
}

// Make functions globally available
window.SendExerciseComplete = SendExerciseComplete;
window.SetBookReturnUrl = SetBookReturnUrl;
</script>
```

### Alternative: Custom WebGL Template

If you want a cleaner solution, create a custom WebGL template:

1. **Copy Default Template:**
   - From: `Unity/Editor/Data/PlaybackEngines/WebGLSupport/BuildTools/WebGLTemplates/Default/`
   - To: `YourUnityProject/Assets/WebGLTemplates/Custom/`

2. **Modify `index.html`** in your custom template
3. **In Unity:** Player Settings → WebGL → Template → Select "Custom"

---

## Step 3: Netlify Configuration

### Create/Update netlify.toml

**Location:** `Builds/WebGL/netlify.toml`

```toml
[build]
  # Publish the WebGL build directory
  publish = "."

# Redirect all routes to index.html (for SPA routing)
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

# Headers for security
[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "SAMEORIGIN"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"

# Headers for WebGL files
[[headers]]
  for = "/*.wasm"
  [headers.values]
    Content-Type = "application/wasm"
    Cross-Origin-Embedder-Policy = "require-corp"
    Cross-Origin-Opener-Policy = "same-origin"

[[headers]]
  for = "/*.js"
  [headers.values]
    Content-Type = "application/javascript"
    Cross-Origin-Embedder-Policy = "require-corp"

[[headers]]
  for = "/*.data"
  [headers.values]
    Content-Type = "application/octet-stream"

[[headers]]
  for = "/*.unityweb"
  [headers.values]
    Content-Type = "application/octet-stream"

# Cache static assets
[[headers]]
  for = "/Build/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "/StreamingAssets/*"
  [headers.values]
    Cache-Control = "public, max-age=3600"
```

---

## Step 4: Deploy to Netlify

### Option A: Netlify CLI (Recommended)

```bash
# 1. Install Netlify CLI (if not installed)
npm install -g netlify-cli

# 2. Login to Netlify
netlify login

# 3. Navigate to WebGL build directory
cd YourUnityProject/Builds/WebGL

# 4. Initialize site (first time only)
netlify init

# 5. Deploy
netlify deploy --prod
```

### Option B: Netlify Dashboard

1. **Go to Netlify Dashboard:** https://app.netlify.com
2. **Add New Site** → **Deploy manually**
3. **Drag and drop** your `Builds/WebGL` folder
4. **Deploy**

### Option C: Git Integration

1. **Push WebGL build to GitHub** (in a separate branch or folder)
2. **Connect repository** in Netlify
3. **Set build settings:**
   - Build command: (leave empty)
   - Publish directory: `Builds/WebGL` (or wherever your build is)

---

## Step 5: Configure Site URL

### Get Your Netlify URL

After deployment, you'll get a URL like:
- `https://ballcode-game.netlify.app`

### Update Website Links

Update your book pages to point to the Netlify URL:

**In `books/book1.html` (and book2.html, book3.html):**

```html
<!-- Change this: -->
<a href="/play?book=1&exercise=foundation-block&source=book&return=/books/book1">

<!-- To this: -->
<a href="https://ballcode-game.netlify.app/play?book=1&exercise=foundation-block&source=book&return=/books/book1">
```

**Or use relative path if on same domain:**
```html
<a href="https://ballcode-game.netlify.app?book=1&exercise=foundation-block&source=book&return=/books/book1">
```

---

## Step 6: Test the Integration

### Test Checklist

1. **URL Parameter Parsing:**
   - Visit: `https://ballcode-game.netlify.app?book=1&exercise=foundation-block`
   - Verify: Game loads with Book 1 exercise

2. **Exercise Loading:**
   - Verify: Exercise loads correctly
   - Verify: LevelData is accessible

3. **Exercise Completion:**
   - Complete an exercise
   - Verify: JavaScript function is called
   - Verify: Message sent to parent window (if in iframe)

4. **Return Flow:**
   - Verify: Redirects to book page
   - Verify: URL parameters include completion status
   - Verify: Book page shows completion message

5. **End-to-End Flow:**
   - Start from book page
   - Click "Try the Exercise"
   - Complete exercise
   - Verify: Returns to book page with completion status

---

## Troubleshooting

### Issue: WebGL Build Not Loading

**Solutions:**
- Check browser console for errors
- Verify `.wasm` files are served with correct MIME type
- Check Netlify headers configuration
- Verify CORS settings if loading from different domain

### Issue: JavaScript Function Not Found

**Solutions:**
- Verify `SendExerciseComplete` function is in `index.html`
- Check browser console for errors
- Verify function is called from Unity (check Unity console)

### Issue: Return Flow Not Working

**Solutions:**
- Check `BookReturnHandler.cs` is included in build
- Verify JavaScript function is called
- Check browser console for postMessage errors
- Verify return URL is stored in PlayerPrefs

### Issue: LevelData Not Loading

**Solutions:**
- Verify JSON files are in `StreamingAssets/Levels/`
- Check file paths in LevelDataManager
- Verify files are included in build
- Check browser Network tab for 404 errors

---

## Advanced Configuration

### Custom Domain

1. **In Netlify Dashboard:**
   - Site Settings → Domain Management
   - Add custom domain: `play.ballcode.co`
   - Follow DNS configuration instructions

2. **Update Book Links:**
   - Change links to use custom domain
   - Update return URLs accordingly

### Environment Variables

If you need different settings for dev/prod:

**In Netlify Dashboard:**
- Site Settings → Environment Variables
- Add variables like:
  - `UNITY_GAME_URL` = `https://ballcode-game.netlify.app`
  - `BOOK_RETURN_BASE` = `https://ballcode.co/books`

### Performance Optimization

**Enable Brotli Compression:**
- Netlify automatically compresses, but verify in build settings
- Unity WebGL supports Brotli (better than Gzip)

**CDN Configuration:**
- Netlify uses global CDN automatically
- Verify assets are cached properly

---

## Deployment Script

Create a deployment script to automate the process:

**`deploy-webgl.sh`:**

```bash
#!/bin/bash

# Unity WebGL to Netlify Deployment Script

UNITY_BUILD_PATH="./Builds/WebGL"
NETLIFY_SITE_NAME="ballcode-game"

echo "Deploying WebGL build to Netlify..."

# Check if build exists
if [ ! -d "$UNITY_BUILD_PATH" ]; then
    echo "Error: WebGL build not found at $UNITY_BUILD_PATH"
    echo "Please build Unity project first"
    exit 1
fi

# Deploy to Netlify
cd "$UNITY_BUILD_PATH"
netlify deploy --prod --site "$NETLIFY_SITE_NAME"

if [ $? -eq 0 ]; then
    echo "Deployment successful!"
    echo "Site URL: https://${NETLIFY_SITE_NAME}.netlify.app"
else
    echo "Deployment failed!"
    exit 1
fi
```

**Usage:**
```bash
chmod +x deploy-webgl.sh
./deploy-webgl.sh
```

---

## Quick Reference

### Netlify Commands

```bash
# Login
netlify login

# Deploy
netlify deploy --prod

# View site info
netlify sites:info

# View logs
netlify logs
```

### Unity Build Commands

```bash
# Build WebGL (using Unity CLI)
Unity -batchmode -quit -projectPath /path/to/project -buildTarget WebGL -buildPath /path/to/build
```

### Testing Locally

```bash
# Serve WebGL build locally
cd Builds/WebGL
python3 -m http.server 8000

# Open in browser
open http://localhost:8000
```

---

## Next Steps

1. ✅ Build Unity WebGL with book integration scripts
2. ✅ Add JavaScript bridge to index.html
3. ✅ Configure netlify.toml
4. ✅ Deploy to Netlify
5. ✅ Update book page links
6. ✅ Test complete flow
7. ✅ Configure custom domain (optional)

---

**Document Status:** Complete  
**Last Updated:** November 26, 2025  
**Ready for:** Deployment


