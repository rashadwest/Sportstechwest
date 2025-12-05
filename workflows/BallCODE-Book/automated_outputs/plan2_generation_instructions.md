# Plan 2: Visual Asset Generation Instructions

**Status:** Prompts Extracted - Ready for Generation  
**Completion:** 50% (Automation ready, images pending)

---

## Overview

Three visual assets need to be generated for Episode 1: The Tip-off Trial. All prompts have been extracted and are ready for use.

---

## Asset 1: Court Map (Center Circle)

**Priority:** 1 (Highest - needed for story context)

### Glif Prompt
```
Basketball court diagram showing center circle, transition lanes, and half-court line. Stylized with subtle tech/digital elements - grid lines, code-like patterns, blue accents. Clean, modern, kid-friendly illustration. Top-down view.
```

### Technical Specifications
- **Format:** Vector (SVG) or high-res raster (PNG)
- **Dimensions:** 1200x800px minimum (digital), 300 DPI (print)
- **Style:** Clean, modern, kid-friendly
- **Color Scheme:** Traditional court colors (wood/tan) with blue accents

### Generation Steps
1. Copy the Glif prompt above
2. Open your preferred tool (Glif, Midjourney, DALL-E, Stability AI)
3. Paste the prompt
4. Set dimensions to 1200x800px (or higher for print)
5. Generate and save as `court_map.png`

---

## Asset 2: Shadow Press Scouts (Monster Art)

**Priority:** 2 (Needed for story)

### Glif Prompt
```
Shadowy basketball players, dark shifting figures with tech/code elements visible in their shadows. Menacing but kid-friendly villains. Multiple figures (3-5) creating chaos on a basketball court. Dark colors (black, dark gray, dark purple) with subtle blue tech accents. Athletic, lean silhouettes. Cool video game enemy aesthetic, not scary.
```

### Technical Specifications
- **Format:** Vector (SVG) or high-res raster (PNG)
- **Dimensions:** 1200x1200px minimum (digital), 300 DPI (print)
- **Style:** Dark, shadowy, but kid-friendly
- **Transparency:** May need transparent background for overlays

### Generation Steps
1. Copy the Glif prompt above
2. Open your preferred tool
3. Paste the prompt
4. Set dimensions to 1200x1200px (square format)
5. Generate and save as `shadow_press_scouts.png`

---

## Asset 3: State Diagram (Code Visualization)

**Priority:** 3 (Needed for Skill Pit-Stop)

### Glif Prompt
```
Flowchart diagram showing four basketball states: START, LIVE, DEAD, OUTCOME. Color-coded boxes with basketball icons. Arrows showing state transitions. Clean, educational, kid-friendly design. Modern flowchart aesthetic with basketball theme.
```

### Technical Specifications
- **Format:** Vector (SVG) preferred for scalability
- **Dimensions:** 1000x800px minimum (digital), 300 DPI (print)
- **Style:** Clean, modern, educational
- **Text:** Clear, readable labels

### Color Coding
- **START:** Yellow/Gold (beginning)
- **LIVE:** Green (active, go!)
- **DEAD:** Red (stopped)
- **OUTCOME:** Blue (result)

### Generation Steps
1. Copy the Glif prompt above
2. Open your preferred tool
3. Paste the prompt
4. Set dimensions to 1000x800px (or higher)
5. Generate and save as `state_diagram.png`

---

## Automated Generation (If API Keys Available)

If you have API keys for Stability AI or other services:

1. Set environment variable: `export STABILITY_API_KEY="your-key-here"`
2. Run the generator script:
   ```bash
   python automated_outputs/plan2_visual_generator.py
   ```
3. Images will be generated automatically in `automated_outputs/visuals/`

---

## Manual Generation (No API Keys)

### Option 1: Use Glif
1. Visit glif.app
2. Create new generation
3. Paste the prompt
4. Adjust settings as needed
5. Generate and download

### Option 2: Use Midjourney
1. Join Midjourney Discord
2. Use `/imagine` command
3. Paste the prompt
4. Generate and upscale
5. Download result

### Option 3: Use DALL-E
1. Visit OpenAI DALL-E
2. Enter the prompt
3. Generate image
4. Download result

### Option 4: Use Stability AI
1. Visit platform.stability.ai
2. Use text-to-image
3. Paste the prompt
4. Set dimensions
5. Generate and download

---

## File Organization

After generation, organize files as follows:

```
automated_outputs/
├── visuals/
│   ├── court_map.png
│   ├── shadow_press_scouts.png
│   └── state_diagram.png
└── plan2_visual_prompts.json (already created)
```

---

## Next Steps

1. **Generate images** using one of the methods above
2. **Review images** for quality and consistency
3. **Integrate into Episode 1 document** (next phase)
4. **Create print-ready versions** (300 DPI)
5. **Create digital-optimized versions** (web-friendly sizes)

---

## Status

- ✅ Prompts extracted and structured
- ✅ Generation scripts created
- ✅ Instructions documented
- ⏳ Images pending generation
- ⏳ Integration pending

**Current Completion:** 50% (Automation ready, images need generation)




