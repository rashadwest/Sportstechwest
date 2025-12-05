# Book-Game Integration Architecture

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** November 26, 2025  
**Status:** Complete Architecture Design  
**Purpose:** Design complete integration system for books and Unity game

---

## Architecture Overview

This document defines the complete architecture for integrating BallCODE books (displayed on ballcode.co website) with Unity game exercises, enabling seamless flow: Book → Exercise → Return to Book.

---

## User Flow

### Complete Flow Diagram

```
1. Student visits ballcode.co/books/book1
   ↓
2. Student reads Book 1 content (video, text)
   ↓
3. Student clicks "Try the Exercise" button
   ↓
4. Website redirects to: ballcode.co/play?book=1&exercise=foundation-block&source=book
   ↓
5. Unity WebGL game loads
   ↓
6. BallCODEStarter.cs parses URL parameters
   ↓
7. GameModeManager loads exercise: book1_foundation_block
   ↓
8. Student completes exercise (60-90 seconds)
   ↓
9. Exercise completion triggers return flow
   ↓
10. Unity communicates completion to website
   ↓
11. Website updates UI, unlocks next section
   ↓
12. Student returns to Book 1 page with completion status
```

---

## URL Parameter System

### Parameter Format

**Base URL:** `ballcode.co/play`

**Parameters:**
- `book` - Book number (1, 2, 3)
- `exercise` - Exercise identifier (e.g., `foundation-block`, `decision-crossover`, `pattern-loop`)
- `source` - Source tracking (`book`, `story`, `direct`)
- `return` - Return URL (optional, defaults to book page)

**Example URLs:**
```
ballcode.co/play?book=1&exercise=foundation-block&source=book
ballcode.co/play?book=2&exercise=decision-crossover&source=book
ballcode.co/play?book=3&exercise=pattern-loop&source=book&return=/books/book3
```

### Parameter Parsing (Unity)

**Location:** `BallCODEStarter.cs`

**New Methods:**
```csharp
void CheckURLParameters()
{
    #if UNITY_WEBGL && !UNITY_EDITOR
    string url = Application.absoluteURL;
    
    // Check for book parameter
    if (GetURLParameter("book", out string bookStr))
    {
        int bookNumber = int.Parse(bookStr);
        string exercise = GetURLParameter("exercise", out string exerciseStr) ? exerciseStr : "";
        string source = GetURLParameter("source", out string sourceStr) ? sourceStr : "direct";
        string returnUrl = GetURLParameter("return", out string returnUrlStr) ? returnUrlStr : "";
        
        LoadBookExercise(bookNumber, exercise, source, returnUrl);
    }
    // Existing episode parameter handling...
    #endif
}

void LoadBookExercise(int bookNumber, string exercise, string source, string returnUrl)
{
    // Map book to level ID
    string levelId = GetBookLevelId(bookNumber, exercise);
    
    // Store return URL for later
    PlayerPrefs.SetString("BookReturnUrl", returnUrl);
    PlayerPrefs.SetInt("BookNumber", bookNumber);
    PlayerPrefs.SetString("ExerciseSource", source);
    
    // Load exercise via GameModeManager
    if (GameModeManager.Instance != null)
    {
        GameModeManager.Instance.LoadGameModeFromLevel(levelId);
    }
}
```

### Book-to-Level ID Mapping

**Mapping Function:**
```csharp
string GetBookLevelId(int bookNumber, string exercise)
{
    // Map book number and exercise to level ID
    Dictionary<string, string> bookLevelMap = new Dictionary<string, string>
    {
        { "1_foundation-block", "book1_foundation_block" },
        { "2_decision-crossover", "book2_decision_crossover" },
        { "3_pattern-loop", "book3_pattern_loop" }
    };
    
    string key = $"{bookNumber}_{exercise}";
    if (bookLevelMap.ContainsKey(key))
    {
        return bookLevelMap[key];
    }
    
    // Fallback: generate level ID from book number
    return $"book{bookNumber}_{exercise}";
}
```

---

## Return Flow Architecture

### Return Flow Options

**Option 1: JavaScript postMessage (Recommended)**
- Unity sends message to parent window
- Website receives message and updates UI
- No page reload required
- Better user experience

**Option 2: URL Redirect**
- Unity redirects browser to return URL
- Website reads completion status from URL
- Simpler implementation
- Requires page reload

**Recommended:** Use Option 1 (postMessage) with Option 2 as fallback

### JavaScript Communication (Unity → Website)

**Unity Script (New):**
```csharp
// Add to GameModeManager.cs or create new BookReturnHandler.cs

#if UNITY_WEBGL && !UNITY_EDITOR
using System.Runtime.InteropServices;

public class BookReturnHandler : MonoBehaviour
{
    [DllImport("__Internal")]
    private static extern void SendExerciseComplete(int bookNumber, bool success, float score);
    
    public void OnExerciseComplete(int bookNumber, bool success, float score)
    {
        #if UNITY_WEBGL && !UNITY_EDITOR
        SendExerciseComplete(bookNumber, success ? 1 : 0, score);
        #endif
    }
}
#endif
```

**JavaScript Bridge (WebGL Template):**
```javascript
// Add to Unity WebGL template index.html

var unityInstance = null;

function SendExerciseComplete(bookNumber, success, score) {
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
    
    // Option: Redirect after delay
    setTimeout(function() {
        window.location.href = redirectUrl;
    }, 2000);
}
```

### Website JavaScript Handler

**Website Script:**
```javascript
// Add to book pages (book1.html, book2.html, book3.html)

window.addEventListener('message', function(event) {
    // Verify message is from Unity game
    if (event.data && event.data.type === 'exerciseComplete') {
        var bookNumber = event.data.book;
        var success = event.data.success;
        var score = event.data.score;
        
        // Update UI
        handleExerciseComplete(bookNumber, success, score);
    }
});

function handleExerciseComplete(bookNumber, success, score) {
    // Hide exercise button
    var exerciseButton = document.getElementById('try-exercise-button');
    if (exerciseButton) {
        exerciseButton.style.display = 'none';
    }
    
    // Show completion message
    var completionMessage = document.getElementById('exercise-completion');
    if (completionMessage) {
        completionMessage.style.display = 'block';
        completionMessage.innerHTML = `
            <div class="completion-success">
                <h3>Exercise Complete!</h3>
                <p>Great job! You scored ${score}%</p>
                <p>You've unlocked the next section.</p>
            </div>
        `;
    }
    
    // Unlock next section
    unlockNextSection(bookNumber);
    
    // Save completion status
    localStorage.setItem(`book${bookNumber}_exercise_complete`, 'true');
    localStorage.setItem(`book${bookNumber}_exercise_score`, score.toString());
}

function unlockNextSection(bookNumber) {
    // Show next section that was previously hidden
    var nextSection = document.getElementById(`book${bookNumber}-next-section`);
    if (nextSection) {
        nextSection.style.display = 'block';
    }
}
```

### URL Redirect Fallback

**Unity Script:**
```csharp
void ReturnToBook(int bookNumber, bool success, float score)
{
    string returnUrl = PlayerPrefs.GetString("BookReturnUrl", $"/books/book{bookNumber}");
    string redirectUrl = $"{returnUrl}?exercise=complete&success={(success ? 1 : 0)}&score={score}";
    
    #if UNITY_WEBGL && !UNITY_EDITOR
    Application.ExternalEval($"window.location.href = '{redirectUrl}';");
    #endif
}
```

**Website Script (Read from URL):**
```javascript
// Check URL parameters on page load
window.addEventListener('DOMContentLoaded', function() {
    var urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('exercise') === 'complete') {
        var success = urlParams.get('success') === '1';
        var score = parseFloat(urlParams.get('score') || '0');
        var bookNumber = getBookNumberFromUrl(); // Extract from current URL
        
        handleExerciseComplete(bookNumber, success, score);
        
        // Clean URL
        window.history.replaceState({}, document.title, window.location.pathname);
    }
});
```

---

## Exercise Configuration

### Book Exercise LevelData

**Book 1 Exercise:**
```json
{
  "levelId": "book1_foundation_block",
  "levelName": "Foundation Block Exercise",
  "description": "Practice creating sequences with Block 1 (Pound Dribble)",
  "gameMode": "blockcoding",
  "episodeNumber": 0,
  "codingConcept": "basic_blocks_sequences",
  "exercise": {
    "exerciseType": "BlockCoding",
    "blockCoding": {
      "availableBlocks": ["START", "BLOCK_1_POUND", "ADVANCE", "REPEAT"],
      "requiredBlocks": ["BLOCK_1_POUND"],
      "targetCode": "START → BLOCK_1_POUND → BLOCK_1_POUND → BLOCK_1_POUND → ADVANCE",
      "allowCustomBlocks": false
    },
    "scoring": {
      "maxScore": 100,
      "passingScore": 70,
      "showScoreDuringExercise": false,
      "allowRetry": true,
      "maxAttempts": 3
    }
  },
  "learningObjectives": [
    "Understand that coding starts with simple, repeatable blocks",
    "Practice creating sequences by repeating foundation blocks",
    "Learn that Block 1 (Pound) can be repeated to create sequences"
  ],
  "difficultyLevel": 1,
  "isUnlocked": true
}
```

**Book 2 Exercise:**
```json
{
  "levelId": "book2_decision_crossover",
  "levelName": "Decision Crossover Exercise",
  "description": "Practice if/then conditionals with Block 2 (Crossover)",
  "gameMode": "blockcoding",
  "episodeNumber": 1,
  "codingConcept": "if_then_conditionals",
  "exercise": {
    "exerciseType": "BlockCoding",
    "blockCoding": {
      "availableBlocks": ["START", "IF", "THEN", "ELSE", "BLOCK_2_CROSSOVER", "ADVANCE"],
      "requiredBlocks": ["IF", "THEN", "BLOCK_2_CROSSOVER"],
      "targetCode": "START → IF [defender left] THEN [BLOCK_2_CROSSOVER right] ELSE [BLOCK_2_CROSSOVER left] → ADVANCE",
      "allowCustomBlocks": false
    },
    "scoring": {
      "maxScore": 100,
      "passingScore": 70,
      "showScoreDuringExercise": false,
      "allowRetry": true,
      "maxAttempts": 3
    }
  },
  "learningObjectives": [
    "Understand that coding uses if/then to make decisions",
    "Practice creating conditional sequences",
    "Learn that Block 2 (Crossover) requires reading conditions"
  ],
  "difficultyLevel": 2,
  "isUnlocked": true
}
```

**Book 3 Exercise:**
```json
{
  "levelId": "book3_pattern_loop",
  "levelName": "Pattern Loop Exercise",
  "description": "Practice loops with Block 3 (In & Out Dribble)",
  "gameMode": "blockcoding",
  "episodeNumber": 2,
  "codingConcept": "loops_repetition",
  "exercise": {
    "exerciseType": "BlockCoding",
    "blockCoding": {
      "availableBlocks": ["START", "LOOP", "REPEAT", "THEN", "BREAK", "BLOCK_3_IN_OUT", "ADVANCE"],
      "requiredBlocks": ["LOOP", "REPEAT", "BLOCK_3_IN_OUT"],
      "targetCode": "START → LOOP [BLOCK_3_IN_OUT fake] REPEAT 3, THEN [BLOCK_3_IN_OUT real] → ADVANCE",
      "allowCustomBlocks": false
    },
    "scoring": {
      "maxScore": 100,
      "passingScore": 70,
      "showScoreDuringExercise": false,
      "allowRetry": true,
      "maxAttempts": 3
    }
  },
  "learningObjectives": [
    "Understand that coding uses loops to repeat patterns",
    "Practice creating loop sequences",
    "Learn that Block 3 (In & Out) requires pattern creation and breaking"
  ],
  "difficultyLevel": 3,
  "isUnlocked": true
}
```

---

## Progress Tracking

### Local Storage (Website)

**Storage Keys:**
- `book1_exercise_complete` - Boolean
- `book1_exercise_score` - Number
- `book2_exercise_complete` - Boolean
- `book2_exercise_score` - Number
- `book3_exercise_complete` - Boolean
- `book3_exercise_score` - Number

**Usage:**
```javascript
// Check if exercise completed
function isExerciseComplete(bookNumber) {
    return localStorage.getItem(`book${bookNumber}_exercise_complete`) === 'true';
}

// Get exercise score
function getExerciseScore(bookNumber) {
    return parseFloat(localStorage.getItem(`book${bookNumber}_exercise_score`) || '0');
}

// Update UI based on completion
function updateBookPage(bookNumber) {
    if (isExerciseComplete(bookNumber)) {
        // Hide exercise button
        // Show completion message
        // Unlock next section
    }
}
```

### Server Storage (Future)

**API Endpoints (Future Implementation):**
- `POST /api/exercise/complete` - Save completion status
- `GET /api/exercise/status?book=N` - Get completion status
- `GET /api/progress` - Get all progress

**Data Structure:**
```json
{
  "userId": "user123",
  "bookProgress": [
    {
      "bookNumber": 1,
      "exerciseComplete": true,
      "exerciseScore": 85,
      "completedAt": "2025-11-26T10:00:00Z"
    }
  ]
}
```

---

## Error Handling

### URL Parameter Errors

**Missing Parameters:**
- If `book` parameter missing: Show error, redirect to books page
- If `exercise` parameter missing: Use default exercise for book
- If `source` parameter missing: Default to `direct`

**Invalid Parameters:**
- If `book` not 1, 2, or 3: Show error, redirect to books page
- If `exercise` not found: Show error, redirect to book page

### Exercise Loading Errors

**Level Not Found:**
- Log error in Unity console
- Show user-friendly error message
- Provide "Return to Book" button

**Game Mode Not Available:**
- Fallback to alternative exercise type
- Show message: "Exercise loading, please wait..."
- Redirect to book page if timeout

### Return Flow Errors

**JavaScript Communication Fails:**
- Fallback to URL redirect
- Log error for debugging
- Show completion message on book page

**Return URL Invalid:**
- Default to books page
- Log error for debugging
- Show completion message

---

## Security Considerations

### URL Parameter Validation

- Validate all URL parameters
- Sanitize input to prevent injection
- Limit parameter values to expected ranges

### Cross-Origin Communication

- Verify message origin in postMessage handler
- Use specific target origin (not '*') in production
- Validate Unity game domain

### Progress Storage

- Validate localStorage data
- Sanitize score values
- Handle storage quota exceeded errors

---

## Implementation Checklist

### Phase 1: Unity Extensions
- [ ] Extend BallCODEStarter.cs with book parameter parsing
- [ ] Add GetBookLevelId() mapping function
- [ ] Create BookReturnHandler.cs for JavaScript communication
- [ ] Add return URL storage (PlayerPrefs)
- [ ] Test URL parameter parsing

### Phase 2: Exercise Levels
- [ ] Create Book 1 exercise LevelData JSON
- [ ] Create Book 2 exercise LevelData JSON
- [ ] Create Book 3 exercise LevelData JSON
- [ ] Add levels to LevelDataManager
- [ ] Test exercise loading

### Phase 3: Return Flow
- [ ] Add JavaScript bridge to Unity WebGL template
- [ ] Implement postMessage communication
- [ ] Add URL redirect fallback
- [ ] Test return flow end-to-end

### Phase 4: Website Integration
- [ ] Add exercise buttons to book pages
- [ ] Implement JavaScript message handler
- [ ] Add completion status display
- [ ] Implement progress tracking (localStorage)
- [ ] Test complete flow

---

## Testing Plan

### Unit Tests
- [ ] URL parameter parsing
- [ ] Book-to-level ID mapping
- [ ] Exercise loading
- [ ] Return URL generation

### Integration Tests
- [ ] Book page → Unity game flow
- [ ] Exercise completion → Return flow
- [ ] Progress tracking
- [ ] Error handling

### End-to-End Tests
- [ ] Complete flow: Book 1 → Exercise → Return
- [ ] Complete flow: Book 2 → Exercise → Return
- [ ] Complete flow: Book 3 → Exercise → Return
- [ ] Multiple exercises in sequence
- [ ] Error scenarios

---

## Summary

This architecture provides:
- ✅ Complete URL parameter system
- ✅ Book-to-exercise mapping
- ✅ Return flow (JavaScript + URL redirect)
- ✅ Exercise configuration
- ✅ Progress tracking
- ✅ Error handling
- ✅ Security considerations

**Ready for implementation in Phases 3 and 4.**

---

**Document Status:** Complete  
**Last Updated:** November 26, 2025  
**Next Review:** After implementation


