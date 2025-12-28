# Garvis Request: Push Book 1 Curriculum to Game
## Book 1 Coding Game Integration

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Status:** Ready for Garvis Execution

---

**ONE Thing:** Push Book 1 curriculum (Foundation Block) to the Unity game as the Book 1 coding game, and integrate it with the website UI/UX.

**Tasks:**
1. Update Unity level data - Ensure book1_foundation_block.json matches curriculum (add bucket blocks, update direction codes)
2. Integrate with website - Add "Try the Exercise" button on Book 1 page that links to the game
3. Configure URL parameters - Set up ?book=1&exercise=foundation-block&source=book routing
4. Design UI/UX positioning - Determine where/how the coding game appears on Book 1 page
5. Test integration - Verify exercise loads correctly and returns to book page

---

## 📊 BOOK 1 CURRICULUM DATA

### Exercise Details:
- **Exercise ID:** `book1_foundation_block`
- **Exercise Name:** Foundation Block Challenge
- **Game Mode:** Block Coding
- **URL:** `ballcode.co/play?book=1&exercise=foundation-block&source=book`

### Available Blocks (Updated):
- START block
- POUND DRIBBLE block (with direction codes: S, R, L, B, etc.)
- BUCKET block (with type selector: Layup, Dunk, Step Back, Floater, Pull Up Jump Shot, etc.)
- END block

### Target Code:
```
START → POUND DRIBBLE (S) → POUND DRIBBLE (S) → POUND DRIBBLE (S) → BUCKET [LAYUP] → END
```

### Success Criteria:
- Complete 3 successful sequences
- Use foundation blocks correctly
- Break the press using sequences
- Score with a bucket

---

## 🎨 UI/UX POSITIONING OPTIONS

### Option 1: Prominent Exercise Button (Recommended)
**Location:** Top of Book 1 page, after story introduction
**Design:**
```
[Book 1 Content]
  ↓
[Large "Try the Exercise" Button - Orange, Prominent]
  ↓
[More Book Content]
```

**Pros:**
- Clear call-to-action
- Easy to find
- Encourages immediate practice

### Option 2: Sidebar Exercise Panel
**Location:** Right sidebar, always visible while scrolling
**Design:**
```
[Book Content] | [Exercise Panel]
                | [Try Exercise Button]
                | [Progress Indicator]
                | [What You'll Learn]
```

**Pros:**
- Always accessible
- Doesn't interrupt reading flow
- Can show progress

### Option 3: Embedded Game Preview
**Location:** Within book content, after key concept explanation
**Design:**
```
[Concept Explanation]
  ↓
[Small Game Preview/Embed]
  ↓
[Full Exercise Button]
  ↓
[More Content]
```

**Pros:**
- Contextual placement
- Shows what exercise looks like
- Natural flow

### Option 4: Bottom CTA Section
**Location:** End of book content, before next book
**Design:**
```
[All Book Content]
  ↓
[Exercise CTA Section]
  [Try the Exercise Button]
  [What You'll Practice]
  [Success Criteria]
```

**Pros:**
- Natural completion flow
- Full context before exercise
- Clear next step

---

## 🔧 TECHNICAL REQUIREMENTS

### Unity Game Integration:
- Parse URL parameters: `book=1&exercise=foundation-block&source=book`
- Load `book1_foundation_block` level
- Configure block coding mode
- Support direction codes (S, R, L, B, etc.)
- Support bucket blocks with type selector
- Return to book page on completion

### Website Integration:
- Add exercise button to Book 1 page (`/books/book1`)
- Link to: `ballcode.co/play?book=1&exercise=foundation-block&source=book&return=/books/book1`
- Handle return flow from game
- Show completion status
- Update progress indicators

### Data Updates Needed:
1. **Unity Level File:** `Unity-Scripts/Levels/book1_foundation_block.json`
   - Update to use BUCKET instead of ADVANCE
   - Add direction codes to blocks
   - Update target code

2. **Website:** `BallCode/books/book1.html`
   - Add exercise button
   - Add integration JavaScript
   - Handle completion flow

3. **Curriculum Schema:** `curriculum-schema.json`
   - Verify Book 1 game data matches

---

## 📝 UI/UX DECISION NEEDED

**Question:** Which UI/UX positioning option should we use?

**Recommendation:** Option 1 (Prominent Exercise Button) - Simple, clear, effective

**Alternative:** Option 2 (Sidebar Panel) - If we want always-visible exercise access

---

## ✅ SUCCESS CRITERIA

1. ✅ Book 1 exercise loads correctly in Unity game
2. ✅ Exercise button appears on Book 1 website page
3. ✅ Clicking button opens game with correct exercise
4. ✅ Completing exercise returns to book page
5. ✅ Completion status is displayed
6. ✅ UI/UX positioning is clear and intuitive

---

## 🚀 GARVIS EXECUTION PLAN

1. **Analyze current state** - Review existing Book 1 integration
2. **Update Unity level** - Modify `book1_foundation_block.json` with bucket blocks
3. **Update website** - Add exercise button and integration code
4. **Test flow** - Verify end-to-end integration works
5. **Deploy** - Push changes to game and website
6. **Document** - Update integration documentation

---

**Ready for Garvis execution!**


