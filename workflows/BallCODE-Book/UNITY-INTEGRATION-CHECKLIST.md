# Unity Integration Checklist - What to Add
## From Current Game to Book-Integrated Game

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 4, 2025  
**Current Game:** https://ballcode.netlify.app/  
**Goal:** Add book integration functionality

---

## ✅ WHAT YOU NEED TO ADD

### Step 1: Copy Unity Scripts to Your Project (5 minutes)

**Copy these files from `Unity-Scripts/` to your Unity project:**

```
YourUnityProject/
└── Assets/
    └── Scripts/
        ├── BallCODEStarter.cs          ← ADD THIS
        ├── BookReturnHandler.cs        ← ADD THIS
        ├── GameModeManager.cs          ← ADD THIS (or modify existing)
        └── LevelDataManager.cs         ← ADD THIS (if not exists)
```

**Files to Copy:**
1. ✅ `Unity-Scripts/BallCODEStarter.cs` → `Assets/Scripts/BallCODEStarter.cs`
2. ✅ `Unity-Scripts/BookReturnHandler.cs` → `Assets/Scripts/BookReturnHandler.cs`
3. ✅ `Unity-Scripts/LevelDataManager.cs` → `Assets/Scripts/LevelDataManager.cs` (if needed)

**Note:** If you already have `GameModeManager.cs`, you'll need to **modify it** (see Step 2)

---

### Step 2: Modify Existing Scripts (10 minutes)

#### A. Modify Your GameModeManager.cs

**If you already have a GameModeManager, add these methods:**

```csharp
// Add this method to handle book exercise completion
public void OnBookExerciseComplete(int bookNumber, bool success, float score)
{
    Debug.Log($"[GameModeManager] Book exercise complete: Book {bookNumber}, Success: {success}, Score: {score}");
    
    // Call BookReturnHandler to send completion to website
    if (BookReturnHandler.Instance != null)
    {
        BookReturnHandler.Instance.OnExerciseComplete(bookNumber, success, score);
    }
    else
    {
        Debug.LogWarning("[GameModeManager] BookReturnHandler not found! Creating one...");
        GameObject returnHandlerObj = new GameObject("BookReturnHandler");
        BookReturnHandler handler = returnHandlerObj.AddComponent<BookReturnHandler>();
        handler.OnExerciseComplete(bookNumber, success, score);
    }
}

// Add this method to load level from level ID
public void LoadGameModeFromLevel(string levelId)
{
    // Your existing level loading logic here
    // This should load the level based on levelId
    // Example: LoadLevel(levelId);
    Debug.Log($"[GameModeManager] Loading level: {levelId}");
    
    // TODO: Implement your level loading logic
    // This depends on how your game loads levels
}
```

#### B. Modify Your Exercise Completion Handler

**Find where exercises complete in your game, and add:**

```csharp
// When exercise completes, check if it's from a book
int bookNumber = PlayerPrefs.GetInt("BookNumber", 0);
if (bookNumber > 0)
{
    // This is a book exercise - use book return flow
    bool success = score > passingThreshold; // Your success criteria
    gameModeManager.OnBookExerciseComplete(bookNumber, success, score);
}
else
{
    // Normal game flow (not from book)
    // Your existing completion logic
}
```

---

### Step 3: Add BookReturnHandler to Scene (2 minutes)

**In your main game scene:**

1. **Create empty GameObject:**
   - Right-click in Hierarchy → Create Empty
   - Name it: `BookReturnHandler`

2. **Add Component:**
   - Select `BookReturnHandler` GameObject
   - Add Component → Scripts → `BookReturnHandler`

3. **Verify:**
   - The script should auto-create as singleton
   - Check Console for any errors

---

### Step 4: Add BallCODEStarter to Scene (2 minutes)

**In your main game scene (or first scene that loads):**

1. **Create empty GameObject:**
   - Right-click in Hierarchy → Create Empty
   - Name it: `BallCODEStarter`

2. **Add Component:**
   - Select `BallCODEStarter` GameObject
   - Add Component → Scripts → `BallCODEStarter`

3. **Configure (if needed):**
   - Set scene names if different from defaults
   - Leave auto-start disabled (unless testing)

---

### Step 5: Add Level Data Files (5 minutes)

**Copy level JSON files to Unity project:**

```
YourUnityProject/
└── Assets/
    └── StreamingAssets/
        └── Levels/
            ├── book1_foundation_block.json    ← ADD THIS
            ├── book2_decision_crossover.json  ← ADD THIS
            └── book3_pattern_loop.json        ← ADD THIS
```

**Files to Copy:**
1. ✅ `Unity-Scripts/Levels/book1_foundation_block.json` → `Assets/StreamingAssets/Levels/`
2. ✅ `Unity-Scripts/Levels/book2_decision_crossover.json` → `Assets/StreamingAssets/Levels/`
3. ✅ `Unity-Scripts/Levels/book3_pattern_loop.json` → `Assets/StreamingAssets/Levels/`

**Note:** Create `StreamingAssets/Levels/` folder if it doesn't exist

---

### Step 6: Update WebGL Build Template (5 minutes)

**After building WebGL, update `index.html`:**

1. **Build WebGL** (File → Build Settings → Build)
2. **Open:** `Builds/WebGL/index.html`
3. **Add JavaScript bridge** (before `</body>` tag):

**Copy entire content from:** `Builds/WebGL/index-template.html`

**Or add this code:**

```html
<script>
  // Book Integration JavaScript Bridge
  function SendExerciseComplete(bookNumber, success, score) {
      console.log(`Exercise complete: Book ${bookNumber}, Success: ${success}, Score: ${score}`);
      
      if (window.parent && window.parent !== window) {
          window.parent.postMessage({
              type: 'exerciseComplete',
              book: bookNumber,
              success: success === 1,
              score: score
          }, '*');
      }
      
      var returnUrl = localStorage.getItem('bookReturnUrl') || `/books/book${bookNumber}`;
      var redirectUrl = `${returnUrl}?exercise=complete&success=${success}&score=${score}`;
      
      setTimeout(function() {
          if (window.parent && window.parent !== window) {
              window.parent.location.href = redirectUrl;
          } else {
              window.location.href = redirectUrl;
          }
      }, 2000);
  }
  
  function SetBookReturnUrl(returnUrl) {
      localStorage.setItem('bookReturnUrl', returnUrl);
      console.log(`Book return URL set: ${returnUrl}`);
  }
  
  window.SendExerciseComplete = SendExerciseComplete;
  window.SetBookReturnUrl = SetBookReturnUrl;
</script>
```

---

## 📋 COMPLETE CHECKLIST

### Unity Project Setup:
- [ ] Copy `BallCODEStarter.cs` to `Assets/Scripts/`
- [ ] Copy `BookReturnHandler.cs` to `Assets/Scripts/`
- [ ] Copy `LevelDataManager.cs` to `Assets/Scripts/` (if needed)
- [ ] Modify `GameModeManager.cs` (add book methods)
- [ ] Add `BookReturnHandler` GameObject to scene
- [ ] Add `BallCODEStarter` GameObject to scene
- [ ] Copy level JSON files to `StreamingAssets/Levels/`
- [ ] Test in Unity Editor (check Console for errors)

### WebGL Build:
- [ ] Build WebGL (File → Build Settings → Build)
- [ ] Add JavaScript bridge to `index.html`
- [ ] Copy `netlify.toml` to build folder
- [ ] Test locally (`python3 -m http.server 8000`)
- [ ] Test URL parameters (`?book=3&exercise=pattern-loop`)

### Deployment:
- [ ] Deploy to Netlify
- [ ] Test book integration end-to-end
- [ ] Verify return flow works

---

## 🔍 WHAT I NEED TO KNOW

To help you integrate, please tell me:

1. **Do you already have a GameModeManager?**
   - [ ] Yes - What's it called?
   - [ ] No - We'll use the one from Unity-Scripts

2. **How does your game load levels/exercises?**
   - [ ] From JSON files
   - [ ] From ScriptableObjects
   - [ ] Hardcoded
   - [ ] Other: _______________

3. **Where does exercise completion happen?**
   - [ ] In GameModeManager
   - [ ] In individual mode managers
   - [ ] In a separate completion handler
   - [ ] Other: _______________

4. **What's your current scene structure?**
   - [ ] Single scene with all modes
   - [ ] Separate scenes per mode
   - [ ] Main menu + game scenes
   - [ ] Other: _______________

---

## 🚀 QUICK START (If You Want to Test First)

**Minimal Integration (5 minutes):**

1. **Copy just these 2 files:**
   - `BallCODEStarter.cs`
   - `BookReturnHandler.cs`

2. **Add to scene:**
   - Add `BallCODEStarter` GameObject
   - Add `BookReturnHandler` GameObject

3. **Build WebGL:**
   - Build → Add JavaScript bridge → Test

4. **Test URL:**
   - `https://ballcode.netlify.app/?book=3&exercise=pattern-loop`

**This will at least parse the URL parameters. Full integration can come after.**

---

## 📞 NEXT STEPS

**Once you tell me:**
1. Your current game structure
2. How levels load
3. Where completion happens

**I can provide:**
- Exact code modifications needed
- Step-by-step integration guide
- Custom code for your specific setup

---

**Status:** Ready to integrate  
**Time Estimate:** 30-60 minutes (depending on your game structure)  
**Difficulty:** Easy (mostly copy/paste with small modifications)


