# AIMCODE Website Integration Plan
## Building ballcode.co Using AIMCODE Methodology

**Purpose:** Integrate stories, games, and learning into a cohesive website experience  
**Framework:** AIMCODE five pillars guide every design decision  
**Status:** Active Development

---

## Core Principle

**The website should feel like a natural extension of the learning experience, not a separate tool.**

Following AIMCODE:
- **Zhang:** Story-first presentation (basketball framework visible)
- **Resnick:** Hands-on building activities accessible
- **Reggio:** Multiple entry points (story, game, code, visual)
- **Hassabis:** Systematic progression visible
- **Jobs:** Simple, beautiful, "it just works"

---

## Website Architecture (AIMCODE-Based)

### Main Navigation Structure:

```
ballcode.co/
├── Home (Landing Page)
│   └── AIMCODE: Beautiful, inspiring (Reggio + Jobs)
│
├── Episodes (Story Hub)
│   ├── Episode 1: The Tip-off Trial
│   ├── Episode 2: The If/Then Fork
│   ├── Episode 3: Loop of the Rotating Guardians
│   └── ... (all 12 episodes)
│   └── AIMCODE: Story-first, multiple entry points (Zhang + Reggio)
│
├── Play (Game Hub)
│   ├── Training Mode
│   ├── Math Mode
│   ├── Coding Mode
│   └── AIMCODE: Hands-on building (Resnick)
│
├── Learn (Learning Hub)
│   ├── Concepts (AI, Math, Coding)
│   ├── Progress Tracking
│   └── AIMCODE: Systematic progression (Hassabis)
│
└── Teachers (Resource Hub)
    ├── Guides
    ├── Career Connections
    └── AIMCODE: Multiple resources (Reggio)
```

---

## Episode Page Design (AIMCODE Integration)

### Page Structure:

```html
┌─────────────────────────────────────────────────┐
│ EPISODE [X]: [TITLE]                           │
├─────────────────────────────────────────────────┤
│                                                 │
│ 1. STORY SECTION (Zhang)                       │
│    ├── Video/Audio Recording                   │
│    ├── Story Text (optional)                   │
│    └── Basketball Framework Clear              │
│                                                 │
│ 2. BUILDING ACTIVITIES (Resnick)               │
│    ├── Block Coding Exercise                   │
│    ├── Hands-On Challenge                      │
│    └── Python Transition                       │
│                                                 │
│ 3. MULTIPLE ENTRY POINTS (Reggio)             │
│    ├── [Story] Button                          │
│    ├── [Game] Button                           │
│    ├── [Code] Button                           │
│    └── [Visual] Button                         │
│                                                 │
│ 4. SYSTEMATIC PROGRESSION (Hassabis)           │
│    ├── "Builds on Episode [X-1]"               │
│    ├── "Next: Episode [X+1]"                   │
│    └── Progress Indicator                       │
│                                                 │
│ 5. SIMPLE DESIGN (Jobs)                        │
│    ├── Clean Interface                         │
│    ├── Intuitive Navigation                    │
│    └── "It Just Works"                         │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## Implementation by AIMCODE Pillar

### 1. Zhang (Story-First Presentation)

**Design Principles:**
- Story content is primary, not secondary
- Basketball framework visible immediately
- Concepts emerge naturally through story

**Implementation:**
```html
<section class="story-section">
    <!-- Video/Audio Player (Primary) -->
    <div class="story-player">
        <video controls>
            <source src="/episodes/episode1.mp4">
        </video>
    </div>
    
    <!-- Story Text (Optional, Expandable) -->
    <div class="story-text">
        <button class="toggle-text">Read Story Text</button>
        <div class="text-content" style="display: none;">
            <!-- Story content here -->
        </div>
    </div>
    
    <!-- Basketball Framework Highlight -->
    <div class="basketball-context">
        <h3>Basketball Situation</h3>
        <p>[Basketball problem and context]</p>
    </div>
</section>
```

**Features:**
- Video/audio player prominent
- Basketball context always visible
- Story-first layout (not sidebar)

---

### 2. Resnick (Constructionist Activities)

**Design Principles:**
- Building activities are accessible, not hidden
- Block coding interface is prominent
- Students can create immediately

**Implementation:**
```html
<section class="building-activities">
    <h2>Try It Yourself</h2>
    
    <!-- Block Coding Exercise -->
    <div class="block-coding-exercise">
        <h3>Block Coding Challenge</h3>
        <div class="block-interface">
            <!-- Drag-and-drop block interface -->
            <div class="block-library">
                <!-- Available blocks -->
            </div>
            <div class="block-workspace">
                <!-- Student's block program -->
            </div>
        </div>
        <button class="run-code">Run Your Code</button>
    </div>
    
    <!-- Hands-On Challenge -->
    <div class="hands-on-challenge">
        <h3>Hands-On Challenge</h3>
        <p>[Challenge description]</p>
        <button class="start-challenge">Start Challenge</button>
    </div>
    
    <!-- Python Transition -->
    <div class="python-transition">
        <h3>See It in Python</h3>
        <button class="show-python">Show Python Code</button>
        <div class="python-code" style="display: none;">
            <!-- Python code equivalent -->
        </div>
    </div>
</section>
```

**Features:**
- Block coding interface embedded
- Immediate feedback
- Python transition available
- "Create, not consume" emphasis

---

### 3. Reggio (Multiple Entry Points)

**Design Principles:**
- Multiple ways to engage
- Student choice in navigation
- Beautiful, inspiring design

**Implementation:**
```html
<section class="entry-points">
    <h2>Choose Your Path</h2>
    
    <div class="entry-cards">
        <!-- Story Mode -->
        <div class="entry-card story-mode">
            <div class="card-icon">📖</div>
            <h3>Story Mode</h3>
            <p>Read and experience the adventure</p>
            <button class="enter-mode">Enter Story Mode</button>
        </div>
        
        <!-- Game Mode -->
        <div class="entry-card game-mode">
            <div class="card-icon">🎮</div>
            <h3>Game Mode</h3>
            <p>Practice in the interactive game</p>
            <button class="enter-mode">Enter Game Mode</button>
        </div>
        
        <!-- Code Mode -->
        <div class="entry-card code-mode">
            <div class="card-icon">💻</div>
            <h3>Code Mode</h3>
            <p>Build and create with blocks</p>
            <button class="enter-mode">Enter Code Mode</button>
        </div>
        
        <!-- Visual Mode -->
        <div class="entry-card visual-mode">
            <div class="card-icon">🎨</div>
            <h3>Visual Mode</h3>
            <p>See diagrams and illustrations</p>
            <button class="enter-mode">Enter Visual Mode</button>
        </div>
    </div>
</section>
```

**Features:**
- Beautiful card-based design
- Clear visual indicators
- Student choice emphasized
- All modes accessible

---

### 4. Hassabis (Systematic Progression)

**Design Principles:**
- Progression visible
- Connections to previous/next clear
- Deep understanding prioritized

**Implementation:**
```html
<section class="progression">
    <h2>Your Learning Journey</h2>
    
    <!-- Progress Indicator -->
    <div class="progress-tracker">
        <div class="episode-progress">
            <div class="progress-bar">
                <div class="progress-fill" style="width: 25%;"></div>
            </div>
            <p>Episode 1 of 12</p>
        </div>
    </div>
    
    <!-- Builds On -->
    <div class="builds-on">
        <h3>Builds On</h3>
        <p>This episode builds on foundational concepts.</p>
        <a href="/episodes/episode0" class="review-link">Review Foundation</a>
    </div>
    
    <!-- Next Episode -->
    <div class="next-episode">
        <h3>Next: Episode 2</h3>
        <p>Learn about conditionals and decision-making.</p>
        <a href="/episodes/episode2" class="next-link">Continue Journey</a>
    </div>
    
    <!-- Concept Map -->
    <div class="concept-map">
        <h3>Concept Connections</h3>
        <div class="concept-visualization">
            <!-- Visual map of connected concepts -->
        </div>
    </div>
</section>
```

**Features:**
- Progress tracking
- Clear progression path
- Concept connections visible
- Deep understanding emphasized

---

### 5. Jobs (Simple, Beautiful Design)

**Design Principles:**
- Simple interface
- Intuitive navigation
- "It just works"

**Implementation:**
```html
<!-- Clean, Minimal Design -->
<style>
.episode-page {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.story-section {
    margin-bottom: 3rem;
}

.building-activities {
    margin-bottom: 3rem;
}

.entry-points {
    margin-bottom: 3rem;
}

.progression {
    margin-bottom: 3rem;
}

/* Simple, Beautiful Buttons */
button {
    background: #007AFF;
    color: white;
    border: none;
    padding: 1rem 2rem;
    border-radius: 8px;
    font-size: 1rem;
    cursor: pointer;
    transition: background 0.2s;
}

button:hover {
    background: #0056CC;
}

/* Clean Typography */
h1, h2, h3 {
    font-weight: 600;
    line-height: 1.2;
}

p {
    line-height: 1.6;
    color: #333;
}
</style>
```

**Features:**
- Clean, minimal design
- Intuitive navigation
- Fast loading
- Mobile-responsive
- Accessible

---

## Website Features by AIMCODE

### Story Integration (Zhang)
- ✅ Video/audio player prominent
- ✅ Story text available
- ✅ Basketball context always visible
- ✅ Story-first layout

### Building Activities (Resnick)
- ✅ Block coding interface embedded
- ✅ Hands-on challenges accessible
- ✅ Python transition available
- ✅ Immediate feedback

### Multiple Entry Points (Reggio)
- ✅ Story mode accessible
- ✅ Game mode accessible
- ✅ Code mode accessible
- ✅ Visual mode accessible
- ✅ Beautiful card-based design

### Systematic Progression (Hassabis)
- ✅ Progress tracking
- ✅ Episode connections visible
- ✅ Concept map available
- ✅ Deep understanding emphasized

### Simple Design (Jobs)
- ✅ Clean interface
- ✅ Intuitive navigation
- ✅ Fast loading
- ✅ Mobile-responsive
- ✅ "It just works"

---

## Technical Implementation

### File Structure:

```
ballcode.co/
├── index.html (Home)
├── episodes/
│   ├── index.html (Episodes list)
│   ├── episode1.html
│   ├── episode2.html
│   └── ...
├── play/
│   ├── index.html (Game hub)
│   ├── training.html
│   ├── math.html
│   └── coding.html
├── learn/
│   ├── index.html (Learning hub)
│   ├── concepts.html
│   └── progress.html
├── teachers/
│   ├── index.html (Teacher resources)
│   ├── guides.html
│   └── careers.html
└── assets/
    ├── css/
    │   ├── main.css
    │   └── episode.css
    ├── js/
    │   ├── block-coding.js
    │   └── progress.js
    └── images/
        └── (episode images)
```

### CSS Framework (Jobs - Simple):

```css
/* AIMCODE Design System */
:root {
    --primary: #007AFF;
    --secondary: #5856D6;
    --success: #34C759;
    --warning: #FF9500;
    --danger: #FF3B30;
    --background: #F2F2F7;
    --text: #000000;
    --text-secondary: #8E8E93;
}

/* Simple, Clean Typography */
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    line-height: 1.6;
    color: var(--text);
    background: var(--background);
}

/* Beautiful Cards (Reggio) */
.card {
    background: white;
    border-radius: 12px;
    padding: 2rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    transition: transform 0.2s, box-shadow 0.2s;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 16px rgba(0,0,0,0.15);
}

/* Simple Buttons (Jobs) */
.btn {
    background: var(--primary);
    color: white;
    border: none;
    padding: 1rem 2rem;
    border-radius: 8px;
    font-size: 1rem;
    cursor: pointer;
    transition: background 0.2s;
}

.btn:hover {
    background: #0056CC;
}
```

### JavaScript (Resnick - Interactive):

```javascript
// Block Coding Interface
class BlockCodingInterface {
    constructor() {
        this.blocks = [];
        this.workspace = document.querySelector('.block-workspace');
    }
    
    addBlock(blockType) {
        // Add block to workspace
        // Enable drag-and-drop
        // Provide immediate feedback
    }
    
    runCode() {
        // Execute block program
        // Show results
        // Provide feedback
    }
}

// Progress Tracking (Hassabis)
class ProgressTracker {
    constructor() {
        this.episodes = [];
        this.currentEpisode = 1;
    }
    
    updateProgress(episode, completed) {
        // Update progress
        // Save to localStorage
        // Update UI
    }
    
    getProgress() {
        // Return progress data
        // Show concept connections
    }
}
```

---

## Integration Checklist

### For Each Episode Page:

**Zhang (Story):**
- [ ] Video/audio player prominent
- [ ] Basketball context visible
- [ ] Story-first layout

**Resnick (Building):**
- [ ] Block coding interface embedded
- [ ] Hands-on challenge accessible
- [ ] Python transition available

**Reggio (Multiple Entry Points):**
- [ ] Story mode button
- [ ] Game mode button
- [ ] Code mode button
- [ ] Visual mode button

**Hassabis (Progression):**
- [ ] Progress indicator
- [ ] "Builds on" section
- [ ] "Next episode" section
- [ ] Concept map

**Jobs (Design):**
- [ ] Clean interface
- [ ] Intuitive navigation
- [ ] Mobile-responsive
- [ ] Fast loading

---

## Next Steps

### Phase 1: Foundation (Week 1)
1. Create episode page template
2. Implement story section (Zhang)
3. Implement building activities (Resnick)
4. Basic navigation structure

### Phase 2: Multiple Entry Points (Week 2)
1. Implement entry point cards (Reggio)
2. Connect to game mode
3. Connect to code mode
4. Connect to visual mode

### Phase 3: Progression (Week 3)
1. Implement progress tracking (Hassabis)
2. Create concept map
3. Add episode connections
4. Deep understanding features

### Phase 4: Polish (Week 4)
1. Design refinement (Jobs)
2. Mobile optimization
3. Performance optimization
4. Testing and refinement

---

## Success Metrics

**Zhang (Story):**
- Story engagement time
- Video/audio completion rate
- Basketball context understanding

**Resnick (Building):**
- Block coding exercise completion
- Hands-on challenge participation
- Python transition usage

**Reggio (Multiple Entry Points):**
- Entry point distribution
- Student choice patterns
- Engagement across modes

**Hassabis (Progression):**
- Episode completion rate
- Concept connection understanding
- Deep learning indicators

**Jobs (Design):**
- Page load time (< 3 seconds)
- Mobile usage
- User satisfaction
- "It just works" feedback

---

**Status:** Framework ready, implementation in progress  
**Framework:** AIMCODE methodology guides all design decisions  
**Next Action:** Begin Phase 1 implementation



