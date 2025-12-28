# Video Upload Process for Levels
## Best Way to Add Videos to Game Levels

**Date:** December 10, 2025  
**Status:** Ready to Implement  
**Purpose:** Clear process for adding videos to levels

---

## 🔍 CURRENT PROCESS ANALYSIS

### What I Found:

#### 1. **Book Video Upload (Existing):**
- ✅ `BOOK-UPLOAD-SCRIPT.sh` - Uploads book videos to website
- ✅ `WEEKLY-BOOK-UPLOAD-AUTOMATION.md` - Book upload process
- ✅ Process: Video file → Copy to website → Embed in HTML
- ✅ Format: MP4
- ✅ Location: Website directory

#### 2. **Level Video Structure (Current):**
- ✅ Level JSON has `videoPath` field (currently empty: `""`)
- ✅ Unity expects videos in `StreamingAssets` or `Resources` folder
- ✅ Video path format: Relative to Unity project
- ❌ No videos currently connected to levels

#### 3. **Video Frame Extraction (Existing):**
- ✅ `extract_frames.py` - Extracts frames from videos
- ✅ `video_frames/` directory - Contains extracted PNG frames
- ✅ Used for analysis/preview

---

## 🎯 BEST APPROACH: TWO OPTIONS

### Option 1: Unity StreamingAssets (Recommended)

**Best for:** Game levels that need video playback in Unity

**Process:**
1. **Store videos in Unity project:**
   ```
   BTEBallCODE/
   └── Assets/
       └── StreamingAssets/
           └── Videos/
               ├── book1/
               │   ├── foundation_block_pound.mp4
               │   └── foundation_block_sequence.mp4
               └── book2/
                   └── decision_crossover.mp4
   ```

2. **Update level JSON:**
   ```json
   {
     "videoPath": "Videos/book1/foundation_block_pound.mp4",
     "videoConfig": {
       "autoPlay": true,
       "startTime": 0.0,
       "endTime": 3.0,
       "pausePoints": [0.5, 1.0, 1.5]
     }
   }
   ```

3. **Unity loads video:**
   - Unity reads from `StreamingAssets/Videos/`
   - Video plays in game
   - Can pause at `pausePoints`

**Pros:**
- ✅ Works directly in Unity
- ✅ No external hosting needed
- ✅ Full control
- ✅ Can pause/seek easily

**Cons:**
- ⚠️ Increases Unity build size
- ⚠️ Videos must be in Unity project

---

### Option 2: External Hosting (YouTube/Vimeo/CDN)

**Best for:** Large videos, web deployment, easier updates

**Process:**
1. **Upload videos to hosting:**
   - YouTube (public/unlisted)
   - Vimeo (private with password)
   - CDN (AWS S3, CloudFront, etc.)

2. **Update level JSON:**
   ```json
   {
     "videoPath": "https://youtube.com/watch?v=ABC123",
     "videoConfig": {
       "autoPlay": true,
       "startTime": 0.0,
       "endTime": 3.0,
       "pausePoints": [0.5, 1.0, 1.5]
     }
   }
   ```

3. **Unity loads video:**
   - Unity fetches from URL
   - Video plays in game
   - May need custom player for pause points

**Pros:**
- ✅ Smaller Unity build
- ✅ Easy to update videos
- ✅ Better for web deployment
- ✅ Can use existing hosting

**Cons:**
- ⚠️ Requires internet connection
- ⚠️ May need custom video player
- ⚠️ Less control over playback

---

## 🚀 RECOMMENDED PROCESS (Option 1 - StreamingAssets)

### Step-by-Step: Adding Video to Level

#### Step 1: Prepare Video File

**Requirements:**
- Format: `.mp4` (H.264 codec recommended)
- Resolution: 720p or 1080p
- Duration: Match level sequence (typically 3-10 seconds)
- Content: Shows the dribble sequence for the level

**Example:**
- Level: `book1_foundation_block`
- Video: Shows pound → pound → pound → advance
- File: `foundation_block_sequence.mp4`
- Duration: ~3 seconds

---

#### Step 2: Organize Video Files

**Create directory structure in Unity project:**
```
BTEBallCODE/
└── Assets/
    └── StreamingAssets/
        └── Videos/
            ├── book1/
            │   ├── foundation_block_sequence.mp4
            │   ├── multiple_dribbles.mp4
            │   └── long_sequences.mp4
            ├── book2/
            │   └── decision_crossover.mp4
            └── tutorials/
                ├── pound_tutorial.mp4
                └── crossover_tutorial.mp4
```

**Naming Convention:**
- Use level ID or descriptive name
- Format: `[level_name]_[description].mp4`
- Examples:
  - `foundation_block_sequence.mp4`
  - `multiple_dribbles.mp4`
  - `pound_tutorial.mp4`

---

#### Step 3: Update Level JSON

**Edit level JSON file:**
```json
{
  "levelId": "book1_foundation_block",
  "levelName": "Foundation Block Exercise",
  "videoPath": "Videos/book1/foundation_block_sequence.mp4",
  "videoConfig": {
    "autoPlay": true,
    "loop": false,
    "playbackSpeed": 1.0,
    "allowSeeking": true,
    "startTime": 0.0,
    "endTime": 3.0,
    "pausePoints": [0.5, 1.0, 1.5, 2.0],
    "analysisPoints": [
      {
        "timestamp": 0.5,
        "description": "This is Block 1: Pound Dribble",
        "codeEquivalent": "BLOCK_1_POUND",
        "question": "What move is this?",
        "correctAnswers": ["Pound", "Block 1"]
      },
      {
        "timestamp": 1.0,
        "description": "Repeat Block 1",
        "codeEquivalent": "BLOCK_1_POUND",
        "question": "How many times do we pound?",
        "correctAnswers": ["3", "Three"]
      }
    ]
  },
  "strategy": {
    "steps": [
      {
        "stepNumber": 1,
        "action": "Start with Block 1 (Pound Dribble)",
        "codeEquivalent": "START → BLOCK_1_POUND",
        "timing": 0.5,
        "videoTimestamp": 0.5
      },
      {
        "stepNumber": 2,
        "action": "Repeat Block 1",
        "codeEquivalent": "BLOCK_1_POUND",
        "timing": 1.0,
        "videoTimestamp": 1.0
      }
    ]
  }
}
```

**Key Changes:**
- `videoPath`: Set to video file path
- `endTime`: Set to video duration
- `pausePoints`: Add timestamps for each move
- `analysisPoints`: Add questions/descriptions at key moments
- `strategy.steps[].videoTimestamp`: Match timing to video

---

#### Step 4: Map Video Timestamps to Dribble Sequence

**For each step in `strategy.steps[]`:**

1. **Watch the video** and identify when each move happens
2. **Note the timestamp** (e.g., 0.5s, 1.0s, 1.5s)
3. **Update `timing`** to match video timestamp
4. **Add `videoTimestamp`** field (optional, for clarity)

**Example Mapping:**
```
Video Timeline:
0.0s - Start position
0.5s - First pound dribble  ← Step 1
1.0s - Second pound dribble ← Step 2
1.5s - Third pound dribble   ← Step 3
2.0s - Advance forward       ← Step 4
```

**JSON:**
```json
"steps": [
  {
    "stepNumber": 1,
    "timing": 0.5,
    "videoTimestamp": 0.5
  },
  {
    "stepNumber": 2,
    "timing": 1.0,
    "videoTimestamp": 1.0
  }
]
```

---

#### Step 5: Test in Unity

**In Unity:**
1. Load the level
2. Video should play automatically (if `autoPlay: true`)
3. Video should pause at `pausePoints`
4. Verify timestamps match moves
5. Test playback controls

---

## 📋 QUICK REFERENCE: Video Upload Checklist

### For Each Level:

- [ ] **Video file prepared:**
  - [ ] Format: `.mp4`
  - [ ] Shows correct dribble sequence
  - [ ] Duration matches level
  - [ ] Quality: 720p or 1080p

- [ ] **Video file placed:**
  - [ ] In `Assets/StreamingAssets/Videos/[book]/`
  - [ ] Named correctly (matches level)
  - [ ] File accessible

- [ ] **Level JSON updated:**
  - [ ] `videoPath` set to correct path
  - [ ] `endTime` set to video duration
  - [ ] `pausePoints` added (at each move)
  - [ ] `analysisPoints` added (if needed)
  - [ ] `strategy.steps[].timing` matches video

- [ ] **Tested:**
  - [ ] Video loads in Unity
  - [ ] Video plays correctly
  - [ ] Pause points work
  - [ ] Timestamps match moves

---

## 🎬 VIDEO CREATION GUIDELINES

### What Each Video Should Show:

**For Block Coding Levels:**
- Clear demonstration of the dribble sequence
- Each move visible and distinct
- Smooth transitions between moves
- Shows the exact sequence from `targetCode`

**For Math Levels:**
- Shows moves being counted
- Clear visual of numbers/points
- Demonstrates the math concept

**For Tutorial Levels:**
- Step-by-step instruction
- Close-up of the move
- Multiple angles (if helpful)
- Clear explanation

---

## 🔧 AUTOMATION OPTIONS

### Option A: Manual Process (Current)

**Steps:**
1. Create/edit video file
2. Place in `StreamingAssets/Videos/`
3. Update level JSON manually
4. Test in Unity

**Time:** ~10-15 minutes per level

---

### Option B: n8n Automation (Future)

**n8n can:**
- [ ] Accept video file upload
- [ ] Place video in correct directory
- [ ] Update level JSON with video path
- [ ] Extract video duration automatically
- [ ] Generate pause points (if timestamps provided)
- [ ] Test video loading

**Time:** ~2-3 minutes per level (after setup)

---

## 📁 RECOMMENDED DIRECTORY STRUCTURE

```
BTEBallCODE/
└── Assets/
    └── StreamingAssets/
        ├── Levels/              (Level JSON files)
        │   ├── book1_foundation_block.json
        │   └── book1_coding_1_2.json
        └── Videos/               (Video files)
            ├── book1/
            │   ├── foundation_block_sequence.mp4
            │   ├── multiple_dribbles.mp4
            │   └── long_sequences.mp4
            ├── book2/
            │   └── decision_crossover.mp4
            ├── math/
            │   ├── count_pounds.mp4
            │   └── add_moves.mp4
            └── tutorials/
                ├── pound_tutorial.mp4
                └── crossover_tutorial.mp4
```

---

## ✅ NEXT STEPS

### Immediate Actions:

1. **Create Videos directory:**
   ```bash
   mkdir -p BTEBallCODE/Assets/StreamingAssets/Videos/book1
   mkdir -p BTEBallCODE/Assets/StreamingAssets/Videos/book2
   mkdir -p BTEBallCODE/Assets/StreamingAssets/Videos/tutorials
   ```

2. **Prepare video files:**
   - Record or locate videos for each level
   - Ensure they show the correct sequence
   - Export as `.mp4`

3. **Place videos:**
   - Copy videos to appropriate directories
   - Use clear naming convention

4. **Update level JSON:**
   - Set `videoPath` for each level
   - Add `pausePoints` and `analysisPoints`
   - Match `timing` to video timestamps

5. **Test:**
   - Load level in Unity
   - Verify video plays
   - Check pause points work

---

## 🎯 SUMMARY

**Best Approach:** Unity StreamingAssets (Option 1)

**Process:**
1. Place videos in `Assets/StreamingAssets/Videos/`
2. Update level JSON with `videoPath`
3. Map video timestamps to dribble sequence
4. Test in Unity

**Format:**
- File: `.mp4` (H.264)
- Path: `Videos/book1/foundation_block_sequence.mp4`
- Duration: Match level sequence (3-10 seconds)

**Next:** Start with one level, test process, then scale

---

**Status:** Ready to implement  
**Recommended:** Start with `book1_foundation_block` level  
**Timeline:** ~15 minutes per level (manual) or ~3 minutes (automated)



