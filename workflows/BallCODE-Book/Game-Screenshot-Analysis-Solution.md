# Game Screenshot Analysis Solution - AIMCODE Approach

**Created:** December 2025  
**Purpose:** Systematically analyze BallCODE game screenshots to understand level mechanics  
**Methodology:** AIMCODE (CLEAR + Alpha Evolve + Research + Experts)

---

## CLEAR Framework

### C - Clarity
**Objective:** Understand how each BallCODE game level works by analyzing screenshots  
**Constraints:** 
- Cannot view images directly
- Need detailed descriptions of UI, blocks, mechanics
- Must understand progression from tutorial through advanced levels

**Format:** Structured analysis document with level-by-level breakdown  
**Audience:** For story integration and game understanding

### L - Logic
**Approach:** 
1. Use vision API to analyze screenshots systematically
2. Start with tutorial (Watson1) to understand basics
3. Progress through Watson2 and CiscoIQ levels
4. Document mechanics, progression, and patterns

**Steps:**
1. Set up vision API (OpenAI or Anthropic)
2. Analyze tutorial screenshots first
3. Analyze each level set in order
4. Document findings in structured format
5. Save to memory for future reference

### E - Examples
**Reference:** 
- BallCODE-Gameplay-Mechanics.md (block system documentation)
- Game-Analysis-Questions.md (what we need to know)
- Existing level structure from Unity scripts

**Style:** 
- Detailed, structured descriptions
- Focus on UI elements, block types, mechanics
- Document progression patterns

### A - Adaptation
**API Options:**
- OpenAI GPT-4 Vision (gpt-4o) - Most accessible
- Anthropic Claude Vision (claude-3-5-sonnet) - Alternative
- Free tier available for both (limited)

**Flexibility:**
- Can use either API
- Can analyze one directory at a time
- Can re-run analysis if needed
- Can add more context to prompts

### R - Results
**Success Criteria:**
- All screenshots analyzed and described
- Level mechanics documented
- Progression patterns identified
- Information saved to memory
- Ready to build stories based on game understanding

**Deliverables:**
- analysis_results.json (structured data)
- Updated BallCODE-Level-Mechanics-Analysis.md
- Memory saved with key mechanics

---

## Solution: Python Script with Vision API

### Created: `analyze_game_screenshots.py`

**Features:**
- ✅ Analyzes screenshots using OpenAI GPT-4 Vision or Anthropic Claude Vision
- ✅ Systematic analysis of all screenshots in a directory
- ✅ Detailed prompts focused on game mechanics
- ✅ Saves results to JSON for easy processing
- ✅ Handles errors gracefully

**AIMCODE Principles Applied:**
- **Jobs (Simplicity):** Simple command-line tool, "it just works"
- **Hassabis (Systematic):** Analyzes all levels in order, builds understanding layer by layer
- **Resnick (Building):** Creates understanding through analysis
- **Reggio (Multiple Entry Points):** Can use different APIs, different contexts
- **Zhang (Story Integration):** Understands game to build better stories

---

## How to Use

### Step 1: Install Dependencies

```bash
# Option 1: OpenAI (recommended - easier setup)
pip install openai

# Option 2: Anthropic Claude
pip install anthropic
```

### Step 2: Set API Key

```bash
# For OpenAI
export OPENAI_API_KEY="your-api-key-here"

# OR for Anthropic
export ANTHROPIC_API_KEY="your-api-key-here"
```

**Getting API Keys:**
- **OpenAI:** https://platform.openai.com/api-keys (free tier available)
- **Anthropic:** https://console.anthropic.com/ (free tier available)

### Step 3: Run Analysis

```bash
# Analyze tutorial screenshots (Watson1)
python analyze_game_screenshots.py "My Books/BallCODE_Watson1" --api openai --output watson1_analysis.json

# Analyze Watson2 levels
python analyze_game_screenshots.py "My Books/BallCODE_Watson2" --api openai --output watson2_analysis.json

# Analyze CiscoIQ levels
python analyze_game_screenshots.py "My Books/BallCODE_CiscoIQ" --api openai --output ciscoiq_analysis.json
```

### Step 4: Review Results

The script will:
1. Analyze each screenshot
2. Generate detailed descriptions
3. Save results to JSON file
4. Print progress as it works

---

## What the Analysis Captures

For each screenshot, the analysis will identify:

1. **UI Elements**
   - Basketball court with grid
   - Block coding area
   - Generated code display
   - Navigation buttons
   - Video playback viewer
   - Dribble tree system

2. **Block Types**
   - START blocks
   - DRIBBLE blocks (with clock timing)
   - BUCKET blocks
   - Conditional blocks (IF/THEN)
   - Loop blocks (REPEAT)

3. **Level Information**
   - Level name/number
   - Instructions
   - Objectives
   - Available blocks

4. **Game State**
   - Court activity
   - Player positions
   - Animations

5. **Coding Concepts**
   - What's being taught
   - Block sequences
   - Learning progression

6. **Progression Indicators**
   - Difficulty level
   - Progress tracking
   - Success states

---

## Next Steps After Analysis

1. **Review JSON Results**
   - Read through descriptions
   - Identify patterns
   - Note progression

2. **Update Documentation**
   - Fill in BallCODE-Level-Mechanics-Analysis.md
   - Document each level's mechanics
   - Identify progression patterns

3. **Save to Memory**
   - Key mechanics
   - Level progression
   - Block system details
   - UI patterns

4. **Build Stories**
   - Use game understanding to create better stories
   - Align story episodes with game levels
   - Ensure story→game integration

---

## Alternative: Manual Description

If API access is not available, you can:
1. Use free image description tools (Google Lens, etc.)
2. Manually describe each screenshot
3. I'll help structure the descriptions
4. We'll build understanding together

**Tools to Try:**
- Google Lens (mobile app)
- ImageDescriber.site (web-based)
- AI Image Describer (web-based)

---

## AIMCODE Expert Principles Applied

### Jobs (Simplicity)
- ✅ Simple command-line tool
- ✅ Clear instructions
- ✅ "It just works" approach
- ✅ Minimal setup required

### Hassabis (Systematic)
- ✅ Analyzes in order (tutorial → advanced)
- ✅ Builds understanding layer by layer
- ✅ Systematic documentation
- ✅ Deep understanding prioritized

### Resnick (Building)
- ✅ Creates understanding through analysis
- ✅ Hands-on tool (you run it)
- ✅ Builds knowledge systematically
- ✅ Learning through doing

### Reggio (Multiple Entry Points)
- ✅ Multiple API options
- ✅ Can analyze one directory at a time
- ✅ Can add custom context
- ✅ Flexible approach

### Zhang (Story Integration)
- ✅ Understands game to build stories
- ✅ Connects game mechanics to stories
- ✅ Ensures story→game alignment
- ✅ Basketball framework maintained

---

## Expected Output Format

The JSON output will look like:

```json
[
  {
    "image_path": "My Books/BallCODE_Watson1/Screenshot 2025-11-07 at 1.41.44 PM.png",
    "description": "Detailed analysis of the screenshot including UI elements, blocks, mechanics, etc.",
    "api_type": "openai",
    "model": "gpt-4o"
  },
  ...
]
```

---

## Cost Estimate

**OpenAI GPT-4 Vision:**
- ~$0.01-0.03 per image (depending on resolution)
- 35 screenshots ≈ $0.35-1.05
- Free tier: $5 credit (enough for ~150-500 images)

**Anthropic Claude Vision:**
- ~$0.003-0.015 per image
- 35 screenshots ≈ $0.10-0.50
- Free tier available

**Total Cost:** Very low (< $2 for all screenshots)

---

## Ready to Start?

1. **Get API Key** (5 minutes)
   - Sign up for OpenAI or Anthropic
   - Get free tier API key

2. **Install Library** (1 minute)
   ```bash
   pip install openai
   ```

3. **Set API Key** (1 minute)
   ```bash
   export OPENAI_API_KEY="your-key"
   ```

4. **Run Analysis** (10-15 minutes)
   ```bash
   python analyze_game_screenshots.py "My Books/BallCODE_Watson1"
   ```

5. **Review Results** (I'll help structure and save to memory)

**Total Time:** ~20 minutes to get complete game understanding!

---

**This solution follows AIMCODE principles: systematic, simple, building understanding through analysis, ready to integrate with story creation.**



