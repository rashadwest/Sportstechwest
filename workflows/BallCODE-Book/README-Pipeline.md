# BallCODE Educational Story Production Pipeline

**Automated system for creating educational stories that teach code, math, and AI concepts through basketball**

---

## Quick Start

### 1. Install Dependencies

```bash
pip install requests
```

### 2. Set Up API Keys

```bash
export STABILITY_API_KEY="your-stability-api-key"
export ELEVENLABS_API_KEY="your-elevenlabs-api-key"
```

Or create a `.env` file:
```
STABILITY_API_KEY=your-key
ELEVENLABS_API_KEY=your-key
```

### 3. Run Pipeline

```bash
python educational_pipeline.py episode1.json
```

That's it! The pipeline will:
- Generate all images (with educational focus)
- Generate all voice audio
- Process code examples
- Process math visualizations
- Process AI interface elements
- Copy assets to Unity
- Generate Unity manifest

---

## File Structure

```
BallCODE-Book/
├── episode1.json                    # Episode data (code/math/AI concepts)
├── educational_pipeline.py          # Main pipeline script
├── EducationalStoryAssetGenerator.cs # Unity Editor script
├── Story-Production-Pipeline.md     # Complete documentation
├── output/
│   └── episode1/
│       ├── images/                  # Generated images
│       ├── audio/                   # Generated audio
│       ├── code_examples/           # Code example files
│       ├── math_visualizations/     # Math charts
│       ├── ai_elements/            # AI interface mockups
│       └── manifest.json           # Unity import manifest
└── UnityProject/
    └── Assets/
        └── StoryContent/
            ├── Images/
            │   └── Episode1/
            ├── Audio/
            │   └── Episode1/
            └── Episodes/
                └── Episode1.asset
```

---

## Episode JSON Format

Each episode JSON includes:

### Educational Concepts
- **Coding Concept:** Name, description, key points, code example
- **Math Concept:** Name, description, key points, math example
- **AI Concept:** Name, description, key points, AI example

### Learning Objectives
- Array of specific learning goals

### Spreads
- Left/right page text
- Image prompts (with educational concept type)
- Audio narration (with emphasis words)

### Skill Pit-Stop
- Code examples
- Math examples
- AI examples

### Exercises
- Coding focus
- Math focus
- AI focus

---

## Unity Integration

### Step 1: Generate Assets
Run the pipeline to generate images and audio.

### Step 2: Import to Unity
1. Open Unity project
2. Menu: `BallCODE > Generate Educational Story Assets`
3. Select episode JSON file
4. Asset automatically created!

### Step 3: Use in Game
The ScriptableObject asset is ready to use in StoryModeManager.

---

## API Costs

### Image Generation (Stability AI)
- ~$0.04 per image (1024x768)
- Episode with 10 spreads: ~$0.80 (20 images)
- 12 episodes: ~$9.60

### Voice Generation (ElevenLabs)
- ~$0.30 per 1000 characters
- Episode (~5000 chars): ~$1.50
- 12 episodes: ~$18

### Total per Episode: ~$2.30
### Total for 12 Episodes: ~$27.60

---

## Educational Focus Features

✅ **Code Concepts:** Visualized through diagrams, code examples, flowcharts  
✅ **Math Concepts:** Visualized through charts, calculations, statistics  
✅ **AI Concepts:** Visualized through interfaces, confidence scores, detection cues  
✅ **Learning Objectives:** Tracked and validated  
✅ **Educational Consistency:** All episodes follow same structure  
✅ **Automated:** No manual content creation  

---

## Next Steps

1. ✅ Episode 1 JSON created
2. ✅ Pipeline script created
3. ✅ Unity integration script created
4. [ ] Set up API keys
5. [ ] Test pipeline with Episode 1
6. [ ] Create remaining episode JSONs
7. [ ] Scale to all episodes

---

## Support

For issues or questions, check:
- `Story-Production-Pipeline.md` - Complete documentation
- `episode1.json` - Example structure
- Unity Editor script comments

**Ready to scale educational content production!**




