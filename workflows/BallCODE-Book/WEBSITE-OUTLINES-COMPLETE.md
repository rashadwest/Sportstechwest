# Complete Website Outlines - Ready to Build
## All Structures and Outlines Needed for ballcode.co

**Purpose:** Consolidated document with all website outlines, structures, and implementation guides  
**Status:** Ready for Development  
**Target:** ballcode.co website

---

## 🏗️ Website Architecture Outline

### Main Site Structure

```
ballcode.co/
├── Home (Landing Page)
│   └── AIMCODE: Beautiful, inspiring (Reggio + Jobs)
│
├── Episodes (Story Hub)
│   ├── index.html (Episodes list)
│   ├── episode1.html - Episode 1: The Tip-off Trial
│   ├── episode2.html - Episode 2: The If/Then Fork
│   ├── episode3.html - Episode 3: Loop of the Rotating Guardians
│   └── ... (all 12 episodes)
│
├── Play (Game Hub)
│   ├── index.html (Game hub)
│   ├── training.html
│   ├── math.html
│   └── coding.html
│
├── Learn (Learning Hub)
│   ├── index.html (Learning hub)
│   ├── concepts.html
│   └── progress.html
│
├── Teachers (Resource Hub)
│   ├── index.html (Teacher resources)
│   ├── guides.html
│   └── careers.html
│
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

---

## 📄 Episode Page Structure Outline

### Page Sections (In Order)

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
│ 5. CAREER CONNECTIONS                          │
│    ├── Career Spotlight                        │
│    ├── Career Cards (3-5 careers)              │
│    ├── Career Activity                         │
│    └── Discussion Questions                    │
│                                                 │
│ 6. TEACHER RESOURCES                          │
│    ├── Teacher Guide Download                  │
│    ├── Answer Keys                             │
│    └── Assessment Rubrics                      │
│                                                 │
│ 7. SIMPLE DESIGN (Jobs)                       │
│    ├── Clean Interface                         │
│    ├── Intuitive Navigation                    │
│    └── "It Just Works"                         │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 🎯 Implementation Priority Outline

### Phase 1: Critical for Pilot School (Do First - This Week)

1. **Episode 1 Story Page** - `ballcode.co/episode1`
   - Complete Episode 1 story (all 3 acts)
   - Skill Pit-Stop mini-lesson
   - Exercise links
   - Mobile-friendly reading experience
   - Clean, professional design

2. **Contact Information**
   - Add email address
   - Add phone number (if applicable)
   - Contact form
   - Response time information

3. **Navigation Menu**
   - Home
   - About
   - Episode 1 (link to story page)
   - For Teachers (resources)
   - Pilot Program
   - Contact

4. **Fix Sign-Up Button**
   - Remove placeholder redirect
   - Link to working destination

5. **Episode 1 Quick Access on Homepage**
   - Prominent button/link
   - Direct to Episode 1 page

**Timeline:** Complete by Friday (5 days) to send package

---

### Phase 2: Important Improvements (Next Week)

6. **"For Teachers" Section**
   - URL: `ballcode.co/teachers`
   - Teacher Guide download
   - Onboarding Guide
   - Exercise worksheets
   - Answer keys
   - Curriculum alignment
   - Support information

7. **Mobile Responsiveness**
   - Test and fix issues
   - Ensure Episode 1 works on mobile
   - Touch-friendly buttons
   - Readable text on small screens

8. **Image Loading Issues**
   - Audit and fix broken images
   - Optimize file sizes
   - Add alt text for accessibility

**Timeline:** Complete within 1-2 weeks

---

### Phase 3: Nice to Have (Future)

9. **Pilot Program Page**
   - Information about pilot program
   - Application process
   - What schools get (FREE)
   - How to apply/contact

10. **FAQ Section**
    - Rewrite content
    - Add new questions
    - Organize by category

**Timeline:** Can wait if needed

---

## 📋 Episode Page Content Structure

### Section 1: Header
- Logo
- Navigation
- Title: "Episode [X]: [Title]"
- Episode info (target audience, duration, learning focus)

### Section 2: Story Section (Zhang)
- Video/Audio Player (Primary)
- Story Text (Optional, Expandable)
- Basketball Framework Highlight
- Basketball Situation Context

### Section 3: Building Activities (Resnick)
- Block Coding Exercise
  - Block library
  - Block workspace
  - Run code button
- Hands-On Challenge
  - Challenge description
  - Start challenge button
- Python Transition
  - Show Python code button
  - Python code equivalent

### Section 4: Multiple Entry Points (Reggio)
- Story Mode Card
  - Icon
  - Description
  - Enter button
- Game Mode Card
  - Icon
  - Description
  - Enter button
- Code Mode Card
  - Icon
  - Description
  - Enter button
- Visual Mode Card
  - Icon
  - Description
  - Enter button

### Section 5: Systematic Progression (Hassabis)
- Progress Tracker
  - Progress bar
  - Episode count (X of 12)
- Builds On Section
  - Previous episode link
  - Review foundation link
- Next Episode Section
  - Next episode link
  - Continue journey button
- Concept Map
  - Visual map of connected concepts

### Section 6: Career Connections
- Career Spotlight
  - Featured career
  - Description
  - Connection to episode
- Career Cards (3-5 careers)
  - Career name
  - Description
  - Skills needed
  - Education path
  - Links to IBM SkillsBuild
- Career Activity
  - Activity instructions
  - Discussion questions

### Section 7: Teacher Resources
- Teacher Guide Download
- Answer Keys
- Assessment Rubrics
- Exercise Worksheets
- Support Information

### Section 8: Footer
- Contact info
- Social links (if applicable)
- Copyright
- Navigation links

---

## 🎨 Design System Outline

### Color Palette (AIMCODE Design System)

```css
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
```

### Typography

```css
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    line-height: 1.6;
    color: var(--text);
    background: var(--background);
}
```

### Component Styles

- **Cards:** White background, rounded corners, shadow, hover effects
- **Buttons:** Primary color, rounded, padding, hover states
- **Navigation:** Clean, minimal, mobile-responsive
- **Forms:** Clean inputs, clear labels, helpful error messages

---

## 🔧 Technical Implementation Outline

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
    │   ├── main.css (shared styles)
    │   └── episode.css (episode-specific)
    ├── js/
    │   ├── block-coding.js
    │   ├── progress.js
    │   └── episode-interactions.js
    └── images/
        └── (episode images, logos, etc.)
```

### CSS Organization

- **Shared styles:** Common across all pages
- **Episode-specific:** Can override per episode
- **Responsive:** Mobile-first approach
- **Print styles:** For PDF generation

### JavaScript Features

- Progress tracking (localStorage)
- Timestamp jumping in videos
- Interactive career cards
- Reading time estimation
- Share functionality
- Block coding interface

---

## 📝 Content Requirements Outline

### For Each Episode Page

1. **Recording**
   - Video or audio file/URL
   - Hosting: YouTube, Vimeo, or self-hosted
   - Embed code ready

2. **Story Content**
   - Complete story (all 3 acts)
   - Text version (optional)
   - Basketball context

3. **Skill Pit-Stop**
   - Educational content
   - Concept explanation
   - Examples

4. **Career Connections**
   - From `Episode-[X]-Career-Connections.md`
   - 3-5 careers per episode
   - Activity instructions
   - Discussion questions

5. **Teacher Resources**
   - Teacher Guide link
   - Answer keys
   - Assessment rubrics
   - Exercise worksheets

---

## 🚀 Quick Start Implementation Outline

### Day 1 (Today)
1. Fix contact information (15 min)
2. Fix sign-up button (15 min)
3. Start Episode 1 page development (2-3 hours)

### Day 2-3
1. Complete Episode 1 page
2. Deploy and test
3. Add navigation menu

### Day 4
1. Create "For Teachers" page
2. Add Episode 1 link to homepage
3. Final testing

### Day 5 (Friday)
1. Final review
2. Send package to pilot school
3. Include website URLs

---

## ✅ Implementation Checklist

### Episode 1 Page Checklist

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

**Career Connections:**
- [ ] Career spotlight
- [ ] Career cards (3-5)
- [ ] Career activity
- [ ] Discussion questions

**Teacher Resources:**
- [ ] Teacher Guide download
- [ ] Answer keys
- [ ] Assessment rubrics

---

## 📊 Success Metrics Outline

### Zhang (Story)
- Story engagement time
- Video/audio completion rate
- Basketball context understanding

### Resnick (Building)
- Block coding exercise completion
- Hands-on challenge participation
- Python transition usage

### Reggio (Multiple Entry Points)
- Entry point distribution
- Student choice patterns
- Engagement across modes

### Hassabis (Progression)
- Episode completion rate
- Concept connection understanding
- Deep learning indicators

### Jobs (Design)
- Page load time (< 3 seconds)
- Mobile usage
- User satisfaction
- "It just works" feedback

---

## 🔗 Integration Points Outline

### Recording Integration

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

### Career Connections Integration

- Pulls from `Episode-[X]-Career-Connections.md`
- Displays 3-5 careers per episode
- Includes activity instructions
- Discussion questions
- Links to IBM SkillsBuild resources

### Teacher Resources Integration

- Links to all teacher guides
- Download links for PDFs
- Answer keys
- Assessment rubrics
- Support information

---

## 📱 Mobile Optimization Outline

### Responsive Features
- Mobile-friendly navigation (hamburger menu)
- Responsive video/audio players
- Touch-friendly buttons
- Readable text on small screens
- Optimized images
- Fast loading

### Testing Requirements
- Test on iPhone/Android
- Test on tablets
- Test on various screen sizes
- Check touch interactions

---

## ⚡ Performance Optimization Outline

### Best Practices
1. **Lazy Loading:** Load videos only when needed
2. **Image Optimization:** Compress images, use WebP
3. **CSS Minification:** Minify CSS files
4. **Caching:** Set proper cache headers
5. **CDN:** Use CDN for static assets

### Metrics to Monitor
- Page load time (< 3 seconds)
- Video load time
- Mobile performance
- User engagement

---

## 🎯 Next Steps Summary

### Immediate (Today)
1. Review this outline document
2. Start with Episode 1 page (highest priority)
3. Fix contact information
4. Fix sign-up button

### This Week
1. Complete Episode 1 page
2. Add navigation menu
3. Create "For Teachers" page
4. Test mobile responsiveness

### As Content Becomes Available
1. Add recording embeds to each episode page
2. Integrate Career Connections for each episode
3. Link resources and materials
4. Test and polish

---

## 📚 Reference Documents

### Planning Documents
- `AIMCODE-WEBSITE-INTEGRATION.md` - Complete website architecture
- `Website-Integration-Plan.md` - Tech stack and integration plan
- `WEBSITE-UPDATE-ACTION-PLAN.md` - Action plan for updates
- `EPISODE-1-PAGE-IMPLEMENTATION.md` - Episode 1 implementation guide

### Content Documents
- `Episode-1-For-Pilot-School.md` - Episode 1 story content
- `Episode-1-Teacher-Guide.md` - Teacher resources
- `Pilot-School-Onboarding-Guide.md` - Onboarding guide
- `WRITING-GUIDE-BOOK-1.md` - Writing guide for stories

### Templates
- `Simple-Website-Template.html` - Base template for Episode 1
- `Episode-Page-Template-Enhanced.html` - Enhanced episode template

---

**Status:** All outlines ready for implementation  
**Priority:** Start with Phase 1 (Episode 1 page, contact, navigation)  
**Timeline:** Phase 1 complete by Friday for pilot school package



