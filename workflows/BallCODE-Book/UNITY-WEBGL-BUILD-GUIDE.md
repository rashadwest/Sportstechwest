# Unity WebGL Build Guide - Quick Steps
## Build & Deploy with Book Integration

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 4, 2025  
**Status:** Ready to Build  
**Time:** ~15-20 minutes

---

## ✅ WHAT YOU HAVE

### Unity Scripts (Already in GitHub):
- ✅ `BallCODEStarter.cs` - URL parameter parsing
- ✅ `BookReturnHandler.cs` - JavaScript communication
- ✅ `GameModeManager.cs` - Return flow
- ✅ `LevelDataManager.cs` - Book exercise loading
- ✅ Level JSON files in `Unity-Scripts/Levels/`

### JavaScript Bridge (Template Ready):
- ✅ `Builds/WebGL/index-template.html` - Complete bridge code

---

## 🚀 QUICK BUILD STEPS

### Step 1: Open Unity Project (5 minutes)

1. **Open Unity Hub**
2. **Open your BallCODE Unity project**
3. **Wait for Unity to load** (check Console for errors)

### Step 2: Verify Scripts Are Added (2 minutes)

**Check these scripts exist in your project:**
- `Assets/Scripts/BallCODEStarter.cs`
- `Assets/Scripts/BookReturnHandler.cs`
- `Assets/Scripts/GameModeManager.cs`
- `Assets/Scripts/LevelDataManager.cs`

**If missing, copy from:**
```
Unity-Scripts/BallCODEStarter.cs → Assets/Scripts/
Unity-Scripts/BookReturnHandler.cs → Assets/Scripts/
Unity-Scripts/GameModeManager.cs → Assets/Scripts/
Unity-Scripts/LevelDataManager.cs → Assets/Scripts/
```

### Step 3: Build WebGL (5-10 minutes)

1. **File → Build Settings**
2. **Select WebGL** platform
3. **Click "Switch Platform"** (if not already WebGL)
4. **Player Settings** (click "Player Settings" button):
   - **Company Name:** Your company
   - **Product Name:** BallCODE Game
   - **WebGL Settings:**
     - Compression: **Gzip** (recommended)
     - Data Caching: **Enabled**
     - Memory Size: **256MB** (or adjust if needed)
5. **Click "Build"**
6. **Choose folder:** `Builds/WebGL/` (create if doesn't exist)
7. **Wait for build** (5-10 minutes depending on project size)

### Step 4: Add JavaScript Bridge (2 minutes)

**After build completes:**

1. **Open:** `Builds/WebGL/index.html`
2. **Find:** `</body>` tag (near end of file)
3. **Before `</body>`, add this code:**

```html
<!-- Book Integration JavaScript Bridge -->
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

**Or simply copy entire content from:** `Builds/WebGL/index-template.html`

### Step 5: Copy Netlify Config (1 minute)

1. **Copy:** `Builds/WebGL/netlify.toml` to `Builds/WebGL/` (if not already there)
2. **Verify it exists** in the build folder

### Step 6: Test Locally (2 minutes)

1. **Open Terminal:**
   ```bash
   cd Builds/WebGL
   python3 -m http.server 8000
   ```

2. **Open browser:** `http://localhost:8000`

3. **Test URL parameters:**
   - `http://localhost:8000?book=3&exercise=deception-loop&source=book&return=/books/book3`
   - Game should load with book exercise

4. **Test exercise completion:**
   - Complete an exercise in game
   - Should redirect back to book page

### Step 7: Deploy to Netlify (5 minutes)

**Option A: Netlify Dashboard (Easiest)**
1. Go to [netlify.com](https://netlify.com)
2. Sign up/login
3. Click "Add new site" → "Deploy manually"
4. Drag and drop `Builds/WebGL/` folder
5. Wait for deployment (~2 minutes)
6. Done! Site is live

**Option B: Netlify CLI**
```bash
# Install CLI (if not installed)
npm install -g netlify-cli

# Login
netlify login

# Deploy
cd Builds/WebGL
netlify deploy --prod
```

---

## 📋 CHECKLIST

### Before Building:
- [ ] Unity project opens without errors
- [ ] All Unity scripts are in project
- [ ] WebGL platform selected
- [ ] Player settings configured

### After Building:
- [ ] `Builds/WebGL/index.html` exists
- [ ] `Builds/WebGL/Build/` folder exists
- [ ] JavaScript bridge added to `index.html`
- [ ] `netlify.toml` copied to build folder
- [ ] Tested locally

### After Deployment:
- [ ] Game loads on Netlify
- [ ] URL parameters work (`?book=3&exercise=...`)
- [ ] Exercise completion redirects work
- [ ] No console errors

---

## 🐛 TROUBLESHOOTING

### Build Fails:
- Check Console for errors
- Ensure all scripts compile
- Try "Clean Build" option

### JavaScript Bridge Not Working:
- Verify function is before `</body>` tag
- Check browser console for errors
- Ensure Unity calls `Application.ExternalCall("SendExerciseComplete", ...)`

### URL Parameters Not Working:
- Verify `BallCODEStarter.cs` has `CheckURLParameters()` method
- Check WebGL build includes the script
- Test in browser console: `Application.absoluteURL`

---

## 📞 QUICK REFERENCE

**Build Location:** `Builds/WebGL/`  
**JavaScript Bridge:** Copy from `index-template.html`  
**Netlify Config:** `netlify.toml` (already configured)  
**Test Locally:** `python3 -m http.server 8000`  
**Deploy:** Netlify dashboard or CLI

---

**Total Time:** ~15-20 minutes  
**Difficulty:** Easy (mostly copy/paste)  
**Status:** Ready to build! 🚀


