# Integration Guide - TikTok Animated Reviews

This guide shows how to integrate the animated review system with your existing TikTok reaction automation.

## 🔄 Integration Flow

```
Existing Reaction Automation
    ↓
Script Generation (your voice)
    ↓
NEW: Animated Review System
    ├─→ Generate Voice Audio
    ├─→ Animate Character
    ├─→ Apply Lip-Sync
    └─→ Compose Final Video
    ↓
Final Video Output
    ↓
Existing Publishing Automation
    ↓
YouTube, TikTok, Twitter, LinkedIn
```

## 📋 Integration Steps

### Step 1: Update Reaction Workflow

Modify your existing reaction workflow to include the animated review system:

```python
# In your reaction automation script
from workflows.tiktok_animated_reviews.src.pipeline import ReviewPipeline

def create_animated_review(tiktok_video_path, script_path):
    """Create animated review video."""
    pipeline = ReviewPipeline(config_path="config/my_config.json")
    output_path = pipeline.process(
        tiktok_video_path=tiktok_video_path,
        script_path=script_path
    )
    return output_path
```

### Step 2: Update n8n Workflow

Add a new node to your n8n workflow after script generation:

**Node: Generate Animated Review**
- Type: Code node
- Input: TikTok video URL, reaction script
- Output: Final animated review video path

```javascript
// n8n Code Node
const { ReviewPipeline } = require('./workflows/tiktok-animated-reviews/src/pipeline');

const pipeline = new ReviewPipeline({
  config_path: './config/my_config.json'
});

const outputPath = pipeline.process(
  $input.item.json.tiktok_video_path,
  $input.item.json.script_path
);

return {
  json: {
    animated_review_path: outputPath,
    ...$input.item.json
  }
};
```

### Step 3: Update Publishing Workflow

Modify your publishing workflow to use the animated review video instead of the original:

```python
# In your publishing automation
def publish_review(animated_review_path, script_data):
    """Publish animated review to platforms."""
    # Use animated_review_path instead of original video
    upload_to_youtube(animated_review_path)
    upload_to_tiktok(animated_review_path)
    # ... etc
```

## 🔧 Configuration Integration

### Option 1: Separate Config File

Keep animated review config separate:

```json
// config/animated_review_config.json
{
  "character": { ... },
  "voice": { ... },
  "composition": { ... }
}
```

### Option 2: Merge with Existing Config

Add animated review settings to your existing config:

```json
// config/reaction_config.json
{
  "reaction": { ... },
  "publishing": { ... },
  "animated_review": {
    "character": { ... },
    "voice": { ... },
    "composition": { ... }
  }
}
```

## 🎯 Workflow Integration Points

### Point 1: After Script Generation

```python
# After generating reaction script
script_path = generate_reaction_script(tiktok_video_url)

# NEW: Generate animated review
animated_video_path = create_animated_review(
    tiktok_video_path=download_tiktok_video(tiktok_video_url),
    script_path=script_path
)

# Continue with publishing
publish_video(animated_video_path)
```

### Point 2: Before Publishing

```python
# Before publishing
if use_animated_review:
    video_path = animated_video_path
else:
    video_path = original_video_path

publish_video(video_path)
```

## 📝 Example Integration Script

```python
"""
Complete integration example
"""
import os
from pathlib import Path
from workflows.tiktok_animated_reviews.src.pipeline import ReviewPipeline

def process_reaction_with_animation(tiktok_video_url, script_text):
    """Complete workflow with animated review."""
    
    # Step 1: Download TikTok video
    tiktok_video_path = download_tiktok_video(tiktok_video_url)
    
    # Step 2: Save script
    script_path = save_script(script_text)
    
    # Step 3: Generate animated review
    pipeline = ReviewPipeline(config_path="config/animated_review_config.json")
    animated_video_path = pipeline.process(
        tiktok_video_path=tiktok_video_path,
        script_path=script_path
    )
    
    # Step 4: Publish
    publish_to_platforms(animated_video_path)
    
    return animated_video_path
```

## 🔄 Automation Integration

### n8n Workflow Structure

```
1. Trigger (Webhook/Manual)
   ↓
2. Extract TikTok Video Info
   ↓
3. Generate Reaction Script
   ↓
4. NEW: Generate Animated Review
   ├─→ Generate Voice Audio
   ├─→ Animate Character
   ├─→ Apply Lip-Sync
   └─→ Compose Video
   ↓
5. Upload to YouTube
   ↓
6. Cross-post to Social Media
   ↓
7. Create Blog Post
   ↓
8. Notification
```

### n8n Node Configuration

**Node: Generate Animated Review**

```json
{
  "name": "Generate Animated Review",
  "type": "n8n-nodes-base.code",
  "parameters": {
    "jsCode": "const { ReviewPipeline } = require('./workflows/tiktok-animated-reviews/src/pipeline');\n\nconst pipeline = new ReviewPipeline({\n  config_path: './config/animated_review_config.json'\n});\n\nconst outputPath = pipeline.process(\n  $input.item.json.tiktok_video_path,\n  $input.item.json.script_path\n);\n\nreturn {\n  json: {\n    animated_review_path: outputPath,\n    ...$input.item.json\n  }\n};"
  }
}
```

## 🎨 Customization Options

### Conditional Animation

Only use animation for certain videos:

```python
def should_use_animation(tiktok_video_url, script_text):
    """Determine if animation should be used."""
    # Example: Use animation for videos longer than 60 seconds
    video_duration = get_video_duration(tiktok_video_url)
    return video_duration > 60

if should_use_animation(tiktok_video_url, script_text):
    video_path = create_animated_review(tiktok_video_path, script_path)
else:
    video_path = original_video_path
```

### Multiple Character Options

Use different characters for different content:

```python
def get_character_config(content_type):
    """Get character config based on content type."""
    if content_type == "sports_tech":
        return "config/character_sports_tech.json"
    elif content_type == "analytics":
        return "config/character_analytics.json"
    else:
        return "config/character_default.json"
```

## 🚀 Testing Integration

### Test Workflow

1. **Test with Sample Video**
   ```bash
   python test_integration.py \
     --tiktok-video "test_video.mp4" \
     --script "test_script.txt"
   ```

2. **Verify Output**
   - Check video is generated
   - Verify character appears correctly
   - Check audio sync
   - Validate video quality

3. **Test Publishing**
   - Upload to test YouTube channel
   - Verify cross-posting works
   - Check blog post generation

## 📊 Monitoring

### Track Metrics

- Animation generation time
- Voice synthesis quality
- Sync accuracy
- Final video quality
- Publishing success rate

### Error Handling

```python
try:
    animated_video_path = create_animated_review(tiktok_video_path, script_path)
except Exception as e:
    logger.error(f"Animation failed: {e}")
    # Fallback to original video
    animated_video_path = tiktok_video_path
```

## 🔧 Troubleshooting

### Common Issues

1. **Character not appearing**
   - Check character file path
   - Verify character format is supported
   - Check video composition settings

2. **Voice not syncing**
   - Verify voice API key
   - Check voice ID is correct
   - Test voice synthesis separately

3. **Video composition fails**
   - Check video resolutions match
   - Verify FFmpeg is installed
   - Check output directory permissions

## 📝 Next Steps

1. ✅ Set up configuration
2. ✅ Test with sample video
3. ✅ Integrate with existing workflow
4. ✅ Test end-to-end
5. ✅ Deploy to production

---

**Framework**: JAEDS (Jobs + Alpha Evolve + Demis + Superhero CV)  
**Status**: 🚀 Ready for Integration

