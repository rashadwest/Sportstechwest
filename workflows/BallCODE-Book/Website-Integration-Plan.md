# Website Integration Plan
## Tech Stack Adjustments for Recording-Based Episodes + Career Connections

**Goal:** Update ballcode.co to support recorded episodes and Career Connections integration  
**Timeline:** While you record, I'll prepare the site structure  
**Approach:** Modular, scalable, professional

---

## What I'm Building

### 1. Enhanced Episode Page Template
- ✅ **Created:** `Episode-Page-Template-Enhanced.html`
- Supports video/audio recordings
- Career Connections section integrated
- Teacher resources section
- Student materials section
- Responsive design
- Professional styling

### 2. Site Structure Updates Needed

#### New Pages to Create:
1. **Episode Pages** (12 pages)
   - `/episode1` - Episode 1: The Tip-off Trial
   - `/episode2` - Episode 2: The If/Then Fork in the Key
   - `/episode3` - Episode 3: Loop of the Rotating Guardians
   - ... (continue for all 12)

2. **Career Connections Hub**
   - `/careers` - Overview of all career connections
   - Links to each episode's career section

3. **Teacher Resources Hub**
   - `/teachers` - All teacher resources
   - Links to guides, answer keys, materials

4. **Episodes Index**
   - `/episodes` - List of all episodes
   - Progress tracking (optional)
   - Filter by concept

---

## Implementation Steps

### Step 1: Update Episode 1 Page (Priority)
**File:** Use `Episode-Page-Template-Enhanced.html` as base

**What to Update:**
1. Replace `[YOUR_VIDEO_EMBED_URL]` with actual video URL
2. Fill in episode-specific content:
   - Episode number and title
   - Learning focus
   - Story content (if including text version)
   - Skill Pit-Stop content
3. Add Career Connections from `Episode-1-Teacher-Guide.md`
4. Add links to resources

**Time:** 30-60 minutes

---

### Step 2: Create Career Connections Component
**Reusable component for all episodes**

**Structure:**
```html
<div class="career-connections">
    <!-- Career spotlight -->
    <!-- Career cards (3-5 careers) -->
    <!-- Career activity -->
    <!-- Discussion questions -->
</div>
```

**Data Source:**
- `Episode-[X]-Career-Connections.md` files
- Can be dynamically loaded or hardcoded per episode

---

### Step 3: Add Recording Support
**Video/Audio embedding**

**Options:**
1. **YouTube Embed** (Recommended)
   - Upload recordings to YouTube
   - Embed using iframe
   - Free hosting, analytics available

2. **Vimeo Embed**
   - Professional option
   - Better privacy controls
   - Paid plans available

3. **Direct Video Hosting**
   - Host on your server/CDN
   - More control
   - Requires storage/bandwidth

4. **Audio-Only Option**
   - HTML5 audio player
   - Lighter weight
   - Faster loading

---

### Step 4: Navigation Updates
**Add to main site navigation:**

```html
<nav>
    <a href="/">Home</a>
    <a href="/episodes">Episodes</a>
    <a href="/teachers">For Teachers</a>
    <a href="/careers">Career Connections</a>
    <a href="/contact">Contact</a>
</nav>
```

---

### Step 5: Teacher Resources Section
**New page: `/teachers`**

**Include:**
- Links to all teacher guides
- Career Connections materials
- Answer keys
- Assessment rubrics
- Download links for PDFs

---

## Technical Details

### File Structure
```
ballcode.co/
├── index.html (homepage)
├── episode1.html
├── episode2.html
├── ...
├── episode12.html
├── episodes/
│   └── index.html (episodes list)
├── teachers/
│   └── index.html (teacher resources)
├── careers/
│   └── index.html (career connections hub)
└── assets/
    ├── css/
    │   └── episode-styles.css (shared styles)
    ├── js/
    │   └── episode-interactions.js (optional)
    └── images/
        └── (episode images, logos, etc.)
```

### CSS Organization
- **Shared styles:** Common across all episodes
- **Episode-specific:** Can override per episode
- **Responsive:** Mobile-first approach
- **Print styles:** For PDF generation

### JavaScript (Optional Enhancements)
- Progress tracking (localStorage)
- Timestamp jumping in videos
- Interactive career cards
- Reading time estimation
- Share functionality

---

## Integration with Career Connections

### How It Works:

1. **Each Episode Page Includes:**
   - Recording (video/audio)
   - Story content (if text version)
   - Skill Pit-Stop
   - **Career Connections section** (NEW)
   - Exercises
   - Teacher resources

2. **Career Connections Section:**
   - Pulls from `Episode-[X]-Career-Connections.md`
   - Displays 3-5 careers
   - Includes activity instructions
   - Discussion questions
   - Links to IBM SkillsBuild resources

3. **Career Connections Hub:**
   - Overview page showing all careers across episodes
   - Filter by career type
   - Filter by coding concept
   - Links to specific episodes

---

## Recording Integration

### Video Embed Options:

**YouTube (Recommended):**
```html
<iframe 
    src="https://www.youtube.com/embed/[VIDEO_ID]" 
    frameborder="0" 
    allowfullscreen>
</iframe>
```

**Vimeo:**
```html
<iframe 
    src="https://player.vimeo.com/video/[VIDEO_ID]" 
    frameborder="0" 
    allowfullscreen>
</iframe>
```

**HTML5 Video (Self-hosted):**
```html
<video controls>
    <source src="/videos/episode1.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>
```

**Audio (Alternative):**
```html
<audio controls>
    <source src="/audio/episode1.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
</audio>
```

---

## Mobile Optimization

### Responsive Features:
- ✅ Mobile-friendly navigation (hamburger menu)
- ✅ Responsive video/audio players
- ✅ Touch-friendly buttons
- ✅ Readable text on small screens
- ✅ Optimized images
- ✅ Fast loading

### Testing:
- Test on iPhone/Android
- Test on tablets
- Test on various screen sizes
- Check touch interactions

---

## Performance Optimization

### Best Practices:
1. **Lazy Loading:** Load videos only when needed
2. **Image Optimization:** Compress images, use WebP
3. **CSS Minification:** Minify CSS files
4. **Caching:** Set proper cache headers
5. **CDN:** Use CDN for static assets

### Metrics to Monitor:
- Page load time (< 3 seconds)
- Video load time
- Mobile performance
- User engagement

---

## Content Management

### For Each Episode, You'll Provide:
1. **Recording:** Video or audio file/URL
2. **Story Content:** Text version (optional)
3. **Skill Pit-Stop:** Educational content
4. **Career Connections:** From my integration files

### I'll Create:
1. **HTML Page:** Using enhanced template
2. **Career Section:** Integrated from Career Connections doc
3. **Resource Links:** Teacher guides, exercises, etc.
4. **Navigation:** Updated site navigation

---

## Deployment Options

### Option 1: Static HTML (Simplest)
- Upload HTML files to server
- Works with any hosting
- Easy to update
- No database needed

### Option 2: CMS Integration
- WordPress: Create custom post type
- Other CMS: Use template as component
- Easier content management
- More features available

### Option 3: Static Site Generator
- Jekyll, Hugo, Next.js
- Generate from markdown
- Version control friendly
- Fast performance

---

## Next Steps (My Tasks)

### Immediate (Today):
1. ✅ Create enhanced episode template
2. ✅ Create integration plan document
3. [ ] Update Episode 1 page with Career Connections
4. [ ] Create Career Connections hub page structure

### This Week:
1. [ ] Create template for all 12 episodes
2. [ ] Build Career Connections component
3. [ ] Create teacher resources page
4. [ ] Update navigation structure
5. [ ] Test responsive design

### As You Record:
1. [ ] Add recording embeds to each episode page
2. [ ] Integrate Career Connections for each episode
3. [ ] Link resources and materials
4. [ ] Test and polish

---

## Questions to Answer

1. **Hosting:** Where is ballcode.co hosted? (WordPress, static HTML, etc.)
2. **Recording Hosting:** Where will recordings be hosted? (YouTube, Vimeo, self-hosted?)
3. **CMS:** Do you use a CMS or static HTML?
4. **Branding:** Colors, fonts, logo - should I match existing site?
5. **Priority:** Which episodes should I prioritize?

---

## Success Criteria

**By End of 6 Days:**
- ✅ Enhanced episode template ready
- ✅ Episode 1 page updated with Career Connections
- ✅ Recording integration working
- ✅ Career Connections section functional
- ✅ Teacher resources accessible
- ✅ Mobile-responsive
- ✅ Professional appearance
- ✅ Ready for content (recordings)

---

**Status:** Template created, ready to integrate your recordings! 🚀



