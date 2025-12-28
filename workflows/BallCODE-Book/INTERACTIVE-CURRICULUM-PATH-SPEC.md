# Interactive Curriculum Path Specification
## Visual Learning Journey (Prioritized)

**Date:** December 10, 2025  
**Status:** Roadmap Item - **PRIORITIZED**  
**Priority:** High (make sure this is something we are prioritizing)  
**Purpose:** Visual learning journey with concept mastery tracking and "What's next" guidance

---

## 🎯 GOAL

Create an interactive curriculum path that:
- Shows visual learning journey
- Tracks concept mastery
- Provides "What's next" guidance
- Displays progression through curriculum
- Integrates with all 4 systems

---

## 📊 CURRENT STATE

**What We Have:**
- ✅ Complete curriculum framework (3-phase progression)
- ✅ Learning objectives defined
- ✅ Book outlines for Books 1-7
- ✅ Schema designed (curriculum-schema.json)
- ❌ No visual curriculum path
- ❌ No concept mastery tracking
- ❌ No "What's next" guidance

**What We Need:**
- Visual learning path
- Concept mastery indicators
- Progress visualization
- Next steps recommendations
- Interactive navigation

---

## 🎨 DESIGN CONCEPT

### Visual Path:
- **Timeline View:** Horizontal path showing progression
- **Node System:** Each book/concept is a node
- **Connection Lines:** Show relationships between concepts
- **Progress Indicators:** Visual markers for completion
- **Interactive:** Click to navigate, hover for details

### Concept Mastery:
- **Color Coding:** Green (mastered), Yellow (in progress), Gray (not started)
- **Progress Bars:** Show mastery percentage
- **Skill Levels:** Beginner → Intermediate → Advanced
- **Assessment Integration:** Link to assessments

### "What's Next" Guidance:
- **Recommended Path:** Based on current progress
- **Prerequisites:** Show what's needed first
- **Alternative Paths:** Different learning routes
- **Personalized:** Based on student's pace

---

## 🔧 FEATURES

### 1. Visual Learning Journey
- **Path Visualization:** Books 1 → 2 → 3 → 4 → 5 → 6 → 7
- **Concept Flow:** Sequences → Conditionals → Loops → Functions
- **Phase Indicators:** Phase 1 (Blocks) → Phase 2 (Bridge) → Phase 3 (Python)
- **Milestone Markers:** Key achievements along the path

### 2. Concept Mastery Tracking
- **Mastery Levels:** Not Started → Learning → Practicing → Mastered
- **Progress Percentage:** How much of concept is learned
- **Assessment Scores:** Link to formative/summative assessments
- **Practice Recommendations:** What to practice next

### 3. "What's Next" Guidance
- **Next Book:** Recommended next book based on progress
- **Next Concept:** What concept to learn next
- **Practice Areas:** What needs more practice
- **Prerequisites:** What must be completed first

### 4. Interactive Navigation
- **Click to Navigate:** Click book/concept to go to it
- **Hover for Details:** See more info on hover
- **Filter Views:** Filter by phase, grade level, concept
- **Search:** Find specific concepts/books

---

## 🚀 IMPLEMENTATION PHASES

### Phase 1: Basic Path Visualization (Week 1)
- [ ] Create visual path component
- [ ] Display books in sequence
- [ ] Show completion status
- [ ] Basic interactivity

### Phase 2: Concept Mastery (Week 2)
- [ ] Add mastery tracking
- [ ] Color coding system
- [ ] Progress indicators
- [ ] Assessment integration

### Phase 3: "What's Next" Logic (Week 3)
- [ ] Recommendation engine
- [ ] Prerequisite checking
- [ ] Personalized suggestions
- [ ] Alternative paths

### Phase 4: Enhanced Features (Week 4)
- [ ] Interactive navigation
- [ ] Filter/search
- [ ] Advanced visualization
- [ ] Mobile responsive

---

## 📋 TECHNICAL SPECS

### Component Structure:
```javascript
<CurriculumPath>
  <PathVisualization>
    <BookNode book={1} status="complete" />
    <BookNode book={2} status="complete" />
    <BookNode book={3} status="next" />
    <ConnectionLine from={1} to={2} />
  </PathVisualization>
  
  <ConceptMastery>
    <ConceptCard concept="Sequences" mastery={100} />
    <ConceptCard concept="Conditionals" mastery={75} />
    <ConceptCard concept="Loops" mastery={0} />
  </ConceptMastery>
  
  <WhatsNext>
    <Recommendation type="book" id={3} />
    <Recommendation type="concept" name="Loops" />
    <PracticeArea concept="Conditionals" />
  </WhatsNext>
</CurriculumPath>
```

### Data Integration:
- **Schema:** Read from curriculum-schema.json
- **Progress:** Read from localStorage/cloud
- **Recommendations:** Calculate based on progress
- **Mastery:** Track from assessments and practice

---

## ✅ SUCCESS CRITERIA

- ✅ Visual learning path displays
- ✅ Concept mastery tracked and shown
- ✅ "What's next" recommendations work
- ✅ Interactive navigation functional
- ✅ Integrates with all 4 systems
- ✅ Updates in real-time

---

## 🔮 FUTURE ENHANCEMENTS

- Adaptive learning paths (AI-powered)
- Multiple learning styles support
- Teacher customization
- Parent progress views
- Export learning reports
- Gamification elements

---

**Status:** Roadmap Item - **PRIORITIZED**  
**Priority:** High (make sure this is prioritizing)  
**Timeline:** 4 weeks for full implementation  
**Integration:** Works with Website, Book, Curriculum, Game



