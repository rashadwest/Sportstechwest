# Quick Start: BallCODE Educational Story Pipeline

**Get your automated story production system running in 5 minutes!**

---

## Step 1: Install Python Dependencies

```bash
pip install requests
```

---

## Step 2: Get API Keys

### Image Generation (Choose one):
- **Stability AI:** https://platform.stability.ai/ (Free tier available)
- **Replicate:** https://replicate.com/ (Pay as you go)

### Voice Synthesis (Choose one):
- **ElevenLabs:** https://elevenlabs.io/ (Best quality, character voices)
- **Google Cloud TTS:** https://cloud.google.com/text-to-speech (Cheaper alternative)

---

## Step 3: Set Up API Keys

### Option A: Environment Variables
```bash
export STABILITY_API_KEY="your-key-here"
export ELEVENLABS_API_KEY="your-key-here"
```

### Option B: Config File
Copy `config.example.json` to `config.json` and add your keys:
```json
{
  "image_api_key": "your-stability-api-key",
  "voice_api_key": "your-elevenlabs-api-key"
}
```

---

## Step 4: Run Pipeline

```bash
python educational_pipeline.py episode1.json
```

**That's it!** The pipeline will:
- ✅ Generate all images (with educational focus)
- ✅ Generate all voice audio
- ✅ Process code examples
- ✅ Process math visualizations  
- ✅ Process AI interface elements
- ✅ Copy assets to Unity
- ✅ Generate Unity manifest

---

## Step 5: Import to Unity

1. Open Unity project
2. Menu: `BallCODE > Generate Educational Story Assets`
3. Select `episode1.json`
4. Asset automatically created!

---

## What You Get

### Generated Assets
- **Images:** `output/episode1/images/` (all spreads)
- **Audio:** `output/episode1/audio/` (all narration)
- **Code Examples:** `output/episode1/code_examples/`
- **Math Visualizations:** `output/episode1/math_visualizations/`
- **AI Elements:** `output/episode1/ai_elements/`

### Unity Asset
- **ScriptableObject:** `Assets/StoryContent/Episodes/Episode1.asset`
- Ready to use in StoryModeManager!

---

## Troubleshooting

### "API key not found"
- Make sure you set environment variables or created `config.json`
- Check that keys are correct

### "Image generation failed"
- Check API key is valid
- Check you have API credits/quota
- Try a different provider

### "Unity asset not found"
- Make sure images/audio are in Unity project
- Check file paths match Unity structure
- Run Unity Editor script again

---

## Next Episode

To create Episode 2:
1. Create `episode2.json` (copy structure from `episode1.json`)
2. Update episode number, title, concepts
3. Run: `python educational_pipeline.py episode2.json`
4. Import to Unity

**Scale to 12 episodes easily!**

---

## Cost Estimate

- **Episode 1:** ~$2.30 (images + voice)
- **12 Episodes:** ~$27.60 total
- **Much cheaper than manual creation!**

---

**Ready to scale your educational content production! 🚀**




