# Story Assets Inventory - What's Generated

**Complete breakdown of all assets created by the production pipeline**

---

## Asset Categories

### 1. Story Images (Main Content)

**Location:** `output/episode1/images/`

**Generated Files:**
- `ep1_spread1_left.png` - Left page image for spread 1
- `ep1_spread1_right.png` - Right page image for spread 1
- `ep1_spread2_left.png` - Left page image for spread 2
- `ep1_spread2_right.png` - Right page image for spread 2
- ... (continues for all spreads)

**For Episode 1 (8 spreads):**
- **Total:** 16 images (8 left pages + 8 right pages)

**Image Types by Educational Concept:**
- **Coding-focused images:** State diagrams, flowcharts, code visualizations
- **Math-focused images:** Statistics charts, calculation diagrams, math visualizations
- **AI-focused images:** AI interface mockups, HUD displays, confidence score visuals
- **General images:** Character panels, cover art, action scenes

**Specifications:**
- **Format:** PNG
- **Dimensions:** 1024x768 pixels (16:9 aspect ratio)
- **Style:** Modern children's book illustration
- **Quality:** Print-ready (300 DPI equivalent)
- **Educational Focus:** Each image optimized for its concept type (coding/math/AI)

---

### 2. Voice Audio (Narration)

**Location:** `output/episode1/audio/`

**Generated Files:**
- `ep1_spread1.mp3` - Audio narration for spread 1
- `ep1_spread2.mp3` - Audio narration for spread 2
- `ep1_spread3.mp3` - Audio narration for spread 3
- ... (continues for all spreads with audio)

**For Episode 1 (8 spreads with audio):**
- **Total:** 8 audio files

**Audio Specifications:**
- **Format:** MP3
- **Quality:** High-quality TTS (ElevenLabs or Google TTS)
- **Voice Types:**
  - Narrator (main story voice)
  - Nova (tech-savvy character voice)
  - Coach Circuit (mentor voice)
  - Arc (AI assistant voice)
- **Features:**
  - Emphasis on educational terms (state, code, math, AI)
  - Speed control (default 1.0x)
  - Natural-sounding narration

**Content:**
- Full story text narration
- Educational term emphasis
- Character dialogue (if applicable)

---

### 3. Code Examples

**Location:** `output/episode1/code_examples/`

**Generated Files:**
- `code_example_1.txt` - First code example from Skill Pit-Stop
- `code_example_2.txt` - Second code example (if multiple)

**Content per file:**
```
Language: pseudocode

if state == START:
    wait for tip-off
elif state == LIVE:
    play basketball
elif state == DEAD:
    wait for play to resume
elif state == OUTCOME:
    record result

Explanation:
This code shows how programs check the current state and take different actions based on it.
```

**For Episode 1:**
- **Total:** 1 code example file (from Skill Pit-Stop)

**Purpose:**
- Educational reference for teachers
- Can be displayed in game
- Can be used in exercises

---

### 4. Math Visualizations

**Location:** `output/episode1/math_visualizations/`

**Generated Files:**
- `math_example_1.png` - Math visualization image
- `math_example_2.png` - Additional math visualization (if multiple)

**Content:**
- Charts showing calculations
- Statistics visualizations
- Percentage displays
- Formula diagrams

**For Episode 1:**
- **Total:** 1 math visualization (Turnover Rate calculation)

**Example Content:**
- Chart showing: "3 possessions, 2 turnovers, 0 points"
- Calculation: "Turnover Rate = (2 / 3) × 100 = 66.7%"
- Visual representation of statistics

**Specifications:**
- **Format:** PNG
- **Dimensions:** 1024x768 pixels
- **Style:** Educational math chart, kid-friendly

---

### 5. AI Interface Elements

**Location:** `output/episode1/ai_elements/`

**Generated Files:**
- `ai_example_1.png` - AI interface mockup
- `ai_example_2.png` - Additional AI interface (if multiple)

**Content:**
- AI HUD displays
- Confidence score indicators
- Vision cue visualizations
- Human-AI collaboration diagrams

**For Episode 1:**
- **Total:** 1 AI interface element

**Example Content:**
- HUD showing: "State shift detected (confidence: 95%)"
- Player confirmation interface
- AI detection indicators

**Specifications:**
- **Format:** PNG
- **Dimensions:** 1024x768 pixels
- **Style:** Tech interface, age-appropriate

---

### 6. Unity ScriptableObject Asset

**Location:** `UnityProject/Assets/StoryContent/Episodes/Episode1.asset`

**Content:**
- Complete episode data structure
- All spread information
- Educational concepts (code, math, AI)
- Learning objectives
- Image references (Sprites)
- Audio clip references
- Skill Pit-Stop data
- Exercise information

**Fields Included:**
```csharp
- episodeNumber: 1
- title: "The Tip-off Trial"
- subtitle: "Learn how robots think..."
- codingConcept: "State"
- mathConcept: "Possession Statistics"
- aiConcept: "Vision Cues & State Detection"
- learningObjectives: [array of 8 objectives]
- spreads: [array of 8 StorySpread objects]
- skillPitStop: [SkillPitStopData object]
```

**Each Spread Contains:**
- `leftPageText` - Story text
- `leftPageImage` - Sprite reference
- `rightPageText` - Additional text
- `rightPageImage` - Sprite reference
- `hasExercise` - Boolean
- `exerciseName` - String
- `audioClipIndex` - Integer
- `educationalConceptType` - "coding", "math", "ai", or "general"
- `educationalHighlight` - Description of concept being taught

---

### 7. Manifest File

**Location:** `output/episode1/manifest.json`

**Content:**
```json
{
  "episodeNumber": 1,
  "title": "The Tip-off Trial",
  "educationalConcepts": {
    "codingConcept": {...},
    "mathConcept": {...},
    "aiConcept": {...}
  },
  "learningObjectives": [...],
  "spreadCount": 8,
  "imageCount": 16,
  "audioCount": 8
}
```

**Purpose:**
- Validation checklist
- Asset inventory
- Unity import verification

---

## Complete Asset List for Episode 1

### Images (16 total)
1. `ep1_spread1_left.png` - Cover/title page
2. `ep1_spread1_right.png` - Character introduction panel
3. `ep1_spread2_left.png` - Court diagram
4. `ep1_spread2_right.png` - State diagram (glitch effect)
5. `ep1_spread3_left.png` - Shadow Press Scouts scene
6. `ep1_spread3_right.png` - AI interface (Arc's HUD)
7. `ep1_spread4_left.png` - Play diagram (outlet & lanes)
8. `ep1_spread4_right.png` - Three actions diagram (climax)
9. `ep1_spread5_left.png` - State diagram (clean)
10. `ep1_spread5_right.png` - Math chart (statistics)
11. `ep1_spread6_left.png` - AI collaboration scene
12. `ep1_spread6_right.png` - Play diagram
13. `ep1_spread7_left.png` - State diagram
14. `ep1_spread7_right.png` - Sequential actions
15. `ep1_spread8_left.png` - QR code & instructions
16. `ep1_spread8_right.png` - Success celebration

### Audio (8 total)
1. `ep1_spread1.mp3` - Act I, Part 1 narration
2. `ep1_spread2.mp3` - Act I, Part 2 narration
3. `ep1_spread3.mp3` - Act II, Part 1 narration
4. `ep1_spread4.mp3` - Act II, Part 2 narration
5. `ep1_spread5.mp3` - Act III, Part 1 narration
6. `ep1_spread6.mp3` - Act III, Part 2 narration
7. `ep1_spread7.mp3` - Climax narration
8. `ep1_spread8.mp3` - Resolution narration

### Code Examples (1 total)
1. `code_example_1.txt` - State management pseudocode

### Math Visualizations (1 total)
1. `math_example_1.png` - Turnover rate calculation chart

### AI Elements (1 total)
1. `ai_example_1.png` - AI state detection interface

### Unity Assets (1 total)
1. `Episode1.asset` - Complete ScriptableObject

### Documentation (1 total)
1. `manifest.json` - Asset inventory

---

## Total Asset Count for Episode 1

- **Images:** 16 (story spreads)
- **Audio:** 8 (narration files)
- **Code Examples:** 1 (text file)
- **Math Visualizations:** 1 (image)
- **AI Elements:** 1 (image)
- **Unity Asset:** 1 (ScriptableObject)
- **Manifest:** 1 (JSON)

**Grand Total:** 29 files generated per episode

---

## Asset Sizes (Estimated)

### Images
- **Per image:** ~500KB - 2MB (PNG, 1024x768)
- **Total images:** ~8-32 MB per episode

### Audio
- **Per audio file:** ~200KB - 1MB (MP3, ~30-60 seconds)
- **Total audio:** ~1.6-8 MB per episode

### Code Examples
- **Per file:** ~1-5 KB (text)
- **Total:** ~1-5 KB per episode

### Math/AI Visualizations
- **Per visualization:** ~500KB - 2MB (PNG)
- **Total:** ~1-4 MB per episode

### Unity Asset
- **Per asset:** ~10-50 KB (ScriptableObject)
- **Total:** ~10-50 KB per episode

**Total Episode Size:** ~10-45 MB per episode

---

## Asset Organization in Unity

```
UnityProject/
└── Assets/
    └── StoryContent/
        ├── Images/
        │   └── Episode1/
        │       ├── ep1_spread1_left.png
        │       ├── ep1_spread1_right.png
        │       ├── ep1_spread2_left.png
        │       └── ... (all 16 images)
        │
        ├── Audio/
        │   └── Episode1/
        │       ├── ep1_spread1.mp3
        │       ├── ep1_spread2.mp3
        │       └── ... (all 8 audio files)
        │
        └── Episodes/
            └── Episode1.asset (ScriptableObject)
```

---

## What Each Asset Contains

### Story Images
- **Left Pages:** Story text + character art or educational diagrams
- **Right Pages:** Visual diagrams, code examples, or educational content
- **Educational Focus:** Each image optimized for its concept (coding/math/AI)

### Voice Audio
- **Content:** Full story narration
- **Emphasis:** Educational terms highlighted
- **Characters:** Different voices for different characters (if configured)

### Code Examples
- **Format:** Text files with syntax
- **Content:** Pseudocode or actual code examples
- **Purpose:** Educational reference

### Math Visualizations
- **Content:** Charts, calculations, statistics
- **Format:** PNG images
- **Purpose:** Visual math education

### AI Elements
- **Content:** Interface mockups, HUD displays
- **Format:** PNG images
- **Purpose:** Visual AI education

### Unity ScriptableObject
- **Content:** Complete episode data structure
- **References:** All images and audio
- **Purpose:** Game-ready asset

---

## Asset Quality Standards

### Images
- ✅ High resolution (1024x768 minimum)
- ✅ Consistent art style
- ✅ Age-appropriate (grades 3-8)
- ✅ Educational focus maintained
- ✅ Print-ready quality

### Audio
- ✅ High-quality TTS
- ✅ Natural-sounding narration
- ✅ Educational term emphasis
- ✅ Consistent voice across episode
- ✅ Appropriate speed and pacing

### Code Examples
- ✅ Clear syntax
- ✅ Educational explanations
- ✅ Age-appropriate complexity
- ✅ Basketball context maintained

### Math Visualizations
- ✅ Clear calculations
- ✅ Kid-friendly charts
- ✅ Educational explanations
- ✅ Basketball context maintained

### AI Elements
- ✅ Age-appropriate interfaces
- ✅ Clear confidence scores
- ✅ Educational explanations
- ✅ Basketball context maintained

---

## Asset Usage in Game

### Story Mode
- Images displayed in page turner
- Audio played during narration
- Text displayed alongside images

### Skill Pit-Stop
- Code examples displayed
- Math visualizations shown
- AI elements displayed

### Exercises
- Code examples referenced
- Math visualizations used
- AI elements referenced

---

## Asset Generation Process

1. **JSON Input:** Episode JSON with all content
2. **Image Generation:** API generates images from prompts
3. **Voice Generation:** API generates audio from text
4. **Code Processing:** Code examples saved as text
5. **Math Processing:** Math visualizations generated
6. **AI Processing:** AI interfaces generated
7. **Unity Import:** Assets copied to Unity project
8. **Asset Creation:** ScriptableObject generated

**Total Time:** ~30 minutes per episode (mostly automated)

---

## Asset Maintenance

### Version Control
- JSON files tracked in Git
- Generated assets can be regenerated
- Unity assets tracked in Git

### Updates
- Update JSON → Regenerate assets
- No manual asset editing needed
- Consistent across all episodes

---

**This is everything that gets generated for each episode!**




