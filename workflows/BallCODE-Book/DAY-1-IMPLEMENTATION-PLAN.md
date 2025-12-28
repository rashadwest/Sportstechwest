# Day 1 Implementation Plan: Unified Curriculum Schema
## THE ONE THING: Schema Foundation

**Date:** December 10, 2025  
**Focus:** Implement active schema that connects all 4 systems  
**Timeline:** Today (4-6 hours)  
**Methodology:** AIMCODE

---

## 🎯 AIMCODE ANALYSIS

### C - Clarity
**What:** Create an active `curriculum-schema.json` file that all 4 systems can read from  
**Why:** This is the foundation - without it, systems can't talk to each other  
**Impact:** Unlocks seamless book-to-game links, curriculum mapping, progress tracking

### L - Logic
- ✅ Schema structure already designed (`CURRICULUM-DATA-EXAMPLE.json`)
- ✅ Book 1 data exists and is complete
- ✅ Level 1 data exists (`book1_foundation_block.json`)
- ✅ Just need to create active file and connect systems
- **No blockers - just implementation work**

### E - Examples
**Input:**
- `CURRICULUM-DATA-EXAMPLE.json` (template)
- Book 1 content (complete)
- Level 1 JSON (`Unity-Scripts/Levels/book1_foundation_block.json`)

**Output:**
- `curriculum-schema.json` (active file)
- JavaScript function to read schema
- Test: Can link Book 1 → Level 1 via schema

### A - Adaptation
- Start with Book 1 + Level 1 only (prove concept)
- Use simple JSON file (no database needed)
- Add to website first (easiest to test)
- Can expand to all books/levels later

### R - Results
**Success = Can answer these questions via schema:**
1. "What game level goes with Book 1?" → Returns `book1_foundation_block`
2. "What book teaches this curriculum concept?" → Returns Book 1
3. "What's the game URL for Book 1?" → Returns game launch URL
4. "What curriculum concept does Level 1 teach?" → Returns "Sequences"

---

## 📋 TASKS BREAKDOWN

### Task 1: Create Active Schema File (30 min)

**What:**
- Copy `CURRICULUM-DATA-EXAMPLE.json` → `curriculum-schema.json`
- Populate with Book 1 data (already exists in example)
- Add Level 1 mapping to Book 1
- Ensure all required fields are present

**Files to Create/Modify:**
- `curriculum-schema.json` (new active file)
- Location: Root of project (same as example file)

**Schema Structure Needed:**
```json
{
  "books": [
    {
      "id": 1,
      "title": "The Foundation Block",
      "game": {
        "exerciseId": "book1_foundation_block",
        "url": "ballcode.co/play?book=1&exercise=foundation-block"
      },
      "curriculum": { ... }
    }
  ],
  "levels": [
    {
      "id": "book1_foundation_block",
      "bookId": 1,
      "curriculumConcept": "Sequences",
      "gameUrl": "..."
    }
  ]
}
```

**Success Criteria:**
- ✅ File exists at `curriculum-schema.json`
- ✅ Book 1 data complete
- ✅ Level 1 mapped to Book 1
- ✅ JSON is valid (can parse)

---

### Task 2: Create Schema Reader Function (45 min)

**What:**
- Create JavaScript function to read schema
- Functions needed:
  - `getBookById(id)` → Returns book data
  - `getLevelByBookId(bookId)` → Returns level for book
  - `getBookByLevelId(levelId)` → Returns book for level
  - `getGameUrl(bookId)` → Returns game URL for book

**Files to Create:**
- `BallCode/netlify/functions/curriculum-schema.js` (or similar)
- Or: `BallCode/assets/js/schema-reader.js` (client-side)

**Function Examples:**
```javascript
// Load schema
const schema = await fetch('/curriculum-schema.json').then(r => r.json());

// Get book by ID
function getBookById(id) {
  return schema.books.find(b => b.id === id);
}

// Get level for book
function getLevelByBookId(bookId) {
  return schema.levels.find(l => l.bookId === bookId);
}

// Get game URL
function getGameUrl(bookId) {
  const book = getBookById(bookId);
  return book?.game?.url || null;
}
```

**Success Criteria:**
- ✅ Functions can read schema file
- ✅ Can get Book 1 data
- ✅ Can get Level 1 for Book 1
- ✅ Can get game URL for Book 1
- ✅ Functions tested in browser console

---

### Task 3: Connect Schema to Website (60 min)

**What:**
- Add schema reader to Book 1 page
- Use schema to get game URL dynamically
- Test that Book 1 page can access schema data

**Files to Modify:**
- Book 1 page HTML/JS (find in `BallCode/` directory)
- Add script tag to load schema reader
- Update "Play Game" button to use schema URL

**Implementation:**
```html
<!-- On Book 1 page -->
<script src="/assets/js/schema-reader.js"></script>
<script>
  // Get game URL from schema
  const gameUrl = getGameUrl(1);
  document.getElementById('play-game-btn').href = gameUrl;
</script>
```

**Success Criteria:**
- ✅ Book 1 page loads schema
- ✅ "Play Game" button uses schema URL
- ✅ Can see schema data in browser console
- ✅ Button works (even if game not embedded yet)

---

### Task 4: Connect Schema to Level Data (45 min)

**What:**
- Verify Level 1 JSON has curriculum concept field
- Update Level 1 JSON if needed to match schema
- Test that schema can find level by curriculum concept

**Files to Check/Modify:**
- `Unity-Scripts/Levels/book1_foundation_block.json`
- Add `curriculumConcept` field if missing
- Add `bookId` field if missing

**Level JSON Structure:**
```json
{
  "levelId": "book1_foundation_block",
  "bookId": 1,
  "curriculumConcept": "Sequences",
  "title": "Foundation Block Challenge",
  ...existing level data...
}
```

**Success Criteria:**
- ✅ Level 1 JSON has curriculum fields
- ✅ Schema can find level by concept
- ✅ Schema can link level to book
- ✅ JSON is valid

---

### Task 5: Test Schema Integration (30 min)

**What:**
- Test all schema functions
- Test Book 1 → Level 1 link
- Test curriculum concept lookup
- Document any issues

**Test Cases:**
1. ✅ Load schema file → Success
2. ✅ Get Book 1 → Returns correct data
3. ✅ Get Level 1 for Book 1 → Returns correct level
4. ✅ Get game URL for Book 1 → Returns URL
5. ✅ Find level by curriculum concept → Returns Level 1
6. ✅ Find book by level ID → Returns Book 1

**Success Criteria:**
- ✅ All test cases pass
- ✅ No errors in console
- ✅ Schema is working end-to-end
- ✅ Ready for Day 2 (game embedding)

---

## 📁 FILE STRUCTURE

```
BallCODE-Book/
├── curriculum-schema.json          ← NEW: Active schema file
├── CURRICULUM-DATA-EXAMPLE.json     ← Reference (keep)
├── BallCode/
│   ├── assets/
│   │   └── js/
│   │       └── schema-reader.js    ← NEW: Schema reading functions
│   └── [book pages]                 ← MODIFY: Add schema integration
└── Unity-Scripts/
    └── Levels/
        └── book1_foundation_block.json  ← MODIFY: Add curriculum fields
```

---

## ✅ COMPLETION CHECKLIST

### Phase 1: Schema File (30 min)
- [ ] Create `curriculum-schema.json`
- [ ] Copy Book 1 data from example
- [ ] Add Level 1 mapping
- [ ] Validate JSON structure
- [ ] Test JSON parsing

### Phase 2: Schema Reader (45 min)
- [ ] Create `schema-reader.js`
- [ ] Implement `getBookById()`
- [ ] Implement `getLevelByBookId()`
- [ ] Implement `getGameUrl()`
- [ ] Test functions in console

### Phase 3: Website Integration (60 min)
- [ ] Find Book 1 page file
- [ ] Add schema reader script
- [ ] Update "Play Game" button
- [ ] Test button uses schema URL
- [ ] Verify in browser

### Phase 4: Level Data Update (45 min)
- [ ] Check Level 1 JSON structure
- [ ] Add `curriculumConcept` field
- [ ] Add `bookId` field
- [ ] Validate JSON
- [ ] Test schema can find level

### Phase 5: Testing (30 min)
- [ ] Test all schema functions
- [ ] Test Book → Level link
- [ ] Test curriculum lookup
- [ ] Document results
- [ ] Mark Day 1 complete

**Total Time:** ~3.5 hours (with buffer: 4-6 hours)

---

## 🚨 POTENTIAL ISSUES & SOLUTIONS

### Issue 1: Can't find Book 1 page file
**Solution:** Search for "Foundation Block" or "book1" in BallCode directory

### Issue 2: Schema file location unclear
**Solution:** Put in root (same as example), or in `BallCode/data/` if website needs it there

### Issue 3: Level JSON structure different than expected
**Solution:** Adapt schema to match existing structure, or update level JSON

### Issue 4: CORS errors loading schema
**Solution:** Put schema in `BallCode/data/` or use Netlify function to serve it

### Issue 5: Game URL format unknown
**Solution:** Use placeholder URL for now, update in Day 2 when we know exact format

---

## 🎯 SUCCESS METRICS

**By end of Day 1, you should be able to:**

1. ✅ Open browser console on Book 1 page
2. ✅ Type: `getBookById(1)` → See Book 1 data
3. ✅ Type: `getLevelByBookId(1)` → See Level 1 data
4. ✅ Type: `getGameUrl(1)` → See game URL
5. ✅ Click "Play Game" button → Uses schema URL (even if game not embedded yet)

**If all 5 work → Day 1 is complete! ✅**

---

## 📝 NOTES

- **Keep it simple:** Only Book 1 + Level 1 for now
- **Test frequently:** After each task, test that it works
- **Document issues:** Note any problems for Day 2
- **Don't perfect it:** Get it working, refine later

---

## 🚀 NEXT STEPS (Day 2 Preview)

Once Day 1 is complete:
- Day 2 will use schema to embed game in Book 1 page
- Day 2 will use `getGameUrl(1)` to get the URL
- Day 2 will test seamless book-to-game flow

**Day 1 unlocks Day 2!**

---

**Status:** Ready to start  
**Priority:** HIGH (Foundation for everything)  
**Estimated Time:** 4-6 hours  
**Dependencies:** None (can start immediately)



