# Video Integration Explanation
## Understanding Current Levels & Video Needs

**Date:** December 10, 2025  
**Status:** Needs Clarification  
**Goal:** Understand how videos connect to levels and what's needed for development

---

## 🔍 CURRENT STATE ANALYSIS

### What I Can See:

#### 1. **Level JSON Structure:**
All levels have:
- ✅ `videoPath` field (but currently empty: `""`)
- ✅ `videoConfig` settings (autoPlay, loop, playbackSpeed, startTime, endTime, pausePoints, analysisPoints)
- ✅ `strategy.steps` with dribble sequences and timing
- ❌ **No actual video files connected**

#### 2. **Video Files Available:**
- ✅ `video_frames/` directory with 163 PNG frame images
- ✅ Video frame extraction suggests videos exist
- ❌ **Videos not linked to levels in JSON**

#### 3. **Level Structure:**
Each level has:
- **Dribble Sequence:** Defined in `strategy.steps[]`
- **Timing:** Each step has `timing` (0.0, 0.5, 1.0, etc.)
- **Code Equivalent:** Each step has `codeEquivalent` (e.g., "BLOCK_1_POUND")
- **Player Positions:** Some levels have positions, most are empty arrays

---

## 🎯 WHAT'S NEEDED FOR DEVELOPMENT

### Critical Understanding Needed:

#### 1. **Video-to-Level Connection:**
**Question:** How should videos connect to levels?

**Current Structure:**
```json
{
  "videoPath": "",  // ← Currently empty!
  "videoConfig": {
    "autoPlay": true,
    "startTime": 0.0,
    "endTime": -1.0,
    "pausePoints": [],
    "analysisPoints": []
  }
}
```

**What We Need to Know:**
- Where are the video files stored? (path structure)
- What format? (.mp4, .mov, .webm?)
- How should `videoPath` be formatted?
- Example: `"videoPath": "Videos/book1_foundation_pound.mp4"`?

---

#### 2. **Dribble Sequence Mapping:**
**Question:** How does the video show the dribble sequence?

**Current Structure:**
```json
"strategy": {
  "steps": [
    {
      "stepNumber": 1,
      "action": "Start with Block 1 (Pound Dribble)",
      "codeEquivalent": "START → BLOCK_1_POUND",
      "timing": 0.0,  // ← Video timestamp?
      "playerPositions": []
    },
    {
      "stepNumber": 2,
      "action": "Repeat Block 1",
      "codeEquivalent": "BLOCK_1_POUND",
      "timing": 0.5,  // ← Video timestamp?
      "playerPositions": []
    }
  ]
}
```

**What We Need to Know:**
- Does `timing` correspond to video timestamp?
- Should video pause at each `timing` point?
- How do we show "you need to do this particular move"?
- Should video highlight/show specific dribbles?

---

#### 3. **Video Content Requirements:**
**Question:** What should each video show?

**For Each Level, We Need:**
- **Video showing the dribble sequence**
- **Clear demonstration of each move**
- **Connection to coding exercise**

**Example for Book 1 Foundation Block:**
- Video shows: Pound dribble → Pound dribble → Pound dribble → Advance
- At 0.0s: Start position
- At 0.5s: First pound dribble
- At 1.0s: Second pound dribble
- At 1.5s: Third pound dribble
- At 2.0s: Advance forward

**What We Need to Know:**
- Do you have videos for each level?
- What moves does each video show?
- How long are the videos?
- Should videos be trimmed to specific sequences?

---

## 📋 WHAT NEEDS TO BE EXPLAINED

### 1. **Video File Organization:**
**Questions:**
- Where are video files stored? (directory structure)
- What naming convention? (e.g., `book1_foundation_pound.mp4`)
- How many videos do you have?
- Are videos organized by book/level?

**Example Structure Needed:**
```
Videos/
  ├── book1/
  │   ├── foundation_block_pound.mp4
  │   ├── foundation_block_sequence.mp4
  │   └── ...
  ├── book2/
  │   ├── decision_crossover.mp4
  │   └── ...
  └── ...
```

---

### 2. **Video-to-Level Mapping:**
**Questions:**
- Which video goes with which level?
- Does one level = one video, or multiple videos?
- Should videos be split by dribble type or full sequence?

**Mapping Needed:**
```
book1_foundation_block.json → Videos/book1/foundation_block_pound.mp4
book1_math_foundation.json → Videos/book1/math_counting.mp4
book2_decision_crossover.json → Videos/book2/crossover_decision.mp4
```

---

### 3. **Dribble Sequence in Video:**
**Questions:**
- How does the video demonstrate the dribble sequence?
- Should video pause at each step?
- Should video highlight specific moves?
- How do we show "you need to do this particular move"?

**Example Flow:**
1. Video plays showing full sequence
2. At each `timing` point, video pauses
3. Highlight shows: "This is Block 1 (Pound Dribble)"
4. Student sees: "You need to do this move"
5. Video continues to next step

---

### 4. **Coding Exercise Connection:**
**Questions:**
- How does video connect to coding exercise?
- Should video show before exercise (instruction)?
- Should video show during exercise (reference)?
- Should video show after exercise (comparison)?

**Example Flow:**
1. **Before Exercise:** Video shows what to do
2. **During Exercise:** Video available as reference
3. **After Exercise:** Video shows correct sequence for comparison

---

## 🎬 PROPOSED VIDEO INTEGRATION STRUCTURE

### Option 1: One Video Per Level (Full Sequence)
```json
{
  "videoPath": "Videos/book1/foundation_block_sequence.mp4",
  "videoConfig": {
    "autoPlay": true,
    "startTime": 0.0,
    "endTime": 5.0,  // Full sequence
    "pausePoints": [0.5, 1.0, 1.5],  // Pause at each dribble
    "analysisPoints": [
      {
        "timestamp": 0.5,
        "description": "First pound dribble",
        "codeEquivalent": "BLOCK_1_POUND"
      },
      {
        "timestamp": 1.0,
        "description": "Second pound dribble",
        "codeEquivalent": "BLOCK_1_POUND"
      }
    ]
  }
}
```

**Pros:**
- Simple: One video per level
- Shows full sequence
- Easy to understand

**Cons:**
- May need to trim videos
- Longer videos

---

### Option 2: Multiple Videos Per Level (Per Move)
```json
{
  "videoPath": "Videos/book1/foundation_block_pound.mp4",  // Main video
  "videoConfig": {
    "autoPlay": true,
    "startTime": 0.0,
    "endTime": -1.0,
    "pausePoints": [0.5, 1.0, 1.5],
    "moveVideos": [  // Additional videos for each move
      {
        "move": "BLOCK_1_POUND",
        "videoPath": "Videos/book1/pound_dribble_demo.mp4",
        "timestamp": 0.5
      }
    ]
  }
}
```

**Pros:**
- Can show individual moves in detail
- More flexible
- Can reuse move videos

**Cons:**
- More complex
- More files to manage

---

### Option 3: Video Segments (Trimmed Clips)
```json
{
  "videoPath": "Videos/book1/foundation_block_full.mp4",
  "videoConfig": {
    "autoPlay": true,
    "segments": [  // Video segments for each step
      {
        "stepNumber": 1,
        "startTime": 0.0,
        "endTime": 0.5,
        "codeEquivalent": "START → BLOCK_1_POUND",
        "description": "First pound dribble"
      },
      {
        "stepNumber": 2,
        "startTime": 0.5,
        "endTime": 1.0,
        "codeEquivalent": "BLOCK_1_POUND",
        "description": "Second pound dribble"
      }
    ]
  }
}
```

**Pros:**
- One video file
- Clear segments
- Easy to navigate

**Cons:**
- Need to define segments
- More complex structure

---

## 🎯 RECOMMENDED APPROACH

### Simple Approach (Recommended):
1. **One video per level** showing the full dribble sequence
2. **Video pauses at each step** (using `pausePoints`)
3. **Clear highlights** showing which move to do
4. **Connection to code blocks** (show code equivalent at each pause)

**Example:**
```json
{
  "levelId": "book1_foundation_block",
  "videoPath": "Videos/book1/foundation_block_sequence.mp4",
  "videoConfig": {
    "autoPlay": true,
    "startTime": 0.0,
    "endTime": 3.0,
    "pausePoints": [0.5, 1.0, 1.5, 2.0],  // Pause at each move
    "analysisPoints": [
      {
        "timestamp": 0.5,
        "description": "This is Block 1: Pound Dribble",
        "codeEquivalent": "BLOCK_1_POUND",
        "question": "What move is this?",
        "correctAnswers": ["Pound", "Block 1", "Pound Dribble"]
      },
      {
        "timestamp": 1.0,
        "description": "Repeat Block 1",
        "codeEquivalent": "BLOCK_1_POUND",
        "question": "How many times do we pound?",
        "correctAnswers": ["3", "Three", "3 times"]
      }
    ]
  },
  "strategy": {
    "steps": [
      {
        "stepNumber": 1,
        "action": "Start with Block 1 (Pound Dribble)",
        "codeEquivalent": "START → BLOCK_1_POUND",
        "timing": 0.5,  // Matches video timestamp
        "videoTimestamp": 0.5  // Explicit video time
      }
    ]
  }
}
```

---

## 📝 QUESTIONS FOR CLARIFICATION

### 1. **Video Files:**
- [ ] Where are video files stored? (path)
- [ ] What format? (.mp4, .mov, .webm?)
- [ ] How many videos do you have?
- [ ] Are videos organized by book/level?

### 2. **Video Content:**
- [ ] What does each video show? (full sequence, individual moves?)
- [ ] How long are videos? (seconds)
- [ ] Do videos need to be trimmed?

### 3. **Dribble Sequence:**
- [ ] How does video demonstrate the sequence?
- [ ] Should video pause at each step?
- [ ] How do we show "you need to do this particular move"?

### 4. **Coding Exercise:**
- [ ] When should video play? (before, during, after exercise?)
- [ ] How does video connect to coding blocks?
- [ ] Should video highlight specific moves?

### 5. **Level Mapping:**
- [ ] Which video goes with which level?
- [ ] One video per level, or multiple?
- [ ] Should we create a mapping document?

---

## 🚀 NEXT STEPS

### Immediate Actions:
1. **Get video file information:**
   - Location/path
   - Format
   - Naming convention
   - Count

2. **Create video-to-level mapping:**
   - Which video → which level
   - Document mapping

3. **Define video integration structure:**
   - Choose approach (Option 1, 2, or 3)
   - Update level JSON files with video paths
   - Test video playback

4. **Test dribble sequence connection:**
   - Verify timing matches video
   - Test pause points
   - Test move highlighting

---

## 📋 TEMPLATE FOR VIDEO INTEGRATION

### Level JSON with Video:
```json
{
  "levelId": "book1_foundation_block",
  "levelName": "Foundation Block Exercise",
  "description": "Practice creating sequences with Block 1 (Pound Dribble).",
  "gameMode": "blockcoding",
  "videoPath": "Videos/book1/foundation_block_sequence.mp4",  // ← ADD THIS
  "videoConfig": {
    "autoPlay": true,
    "loop": false,
    "playbackSpeed": 1.0,
    "allowSeeking": true,
    "startTime": 0.0,
    "endTime": 3.0,  // ← Video length
    "pausePoints": [0.5, 1.0, 1.5, 2.0],  // ← Pause at each move
    "analysisPoints": [
      {
        "timestamp": 0.5,
        "description": "This is Block 1: Pound Dribble",
        "codeEquivalent": "BLOCK_1_POUND",
        "question": "What move is this?",
        "correctAnswers": ["Pound", "Block 1"]
      }
    ]
  },
  "strategy": {
    "steps": [
      {
        "stepNumber": 1,
        "action": "Start with Block 1 (Pound Dribble)",
        "codeEquivalent": "START → BLOCK_1_POUND",
        "timing": 0.5,  // ← Matches video timestamp
        "videoTimestamp": 0.5,  // ← Explicit video time
        "playerPositions": []
      }
    ]
  }
}
```

---

**Status:** Waiting for video information and clarification  
**Next:** Get video file details and create mapping  
**Priority:** High - Needed for level development


