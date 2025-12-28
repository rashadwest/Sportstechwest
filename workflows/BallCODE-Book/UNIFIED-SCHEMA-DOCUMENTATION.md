# Unified Curriculum Schema Documentation
## Single Source of Truth for All 4 Systems

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 5, 2025  
**Version:** 1.0.0  
**Status:** ✅ Schema Design Complete

---

## 🎯 PURPOSE

This unified schema is the **ONE THING** that makes everything easier:
- ✅ **Single source of truth** - All 4 systems (Website, Book, Curriculum, Game) read from same data
- ✅ **Automatic synchronization** - Update once, all systems update automatically
- ✅ **Zero manual alignment** - No more keeping systems in sync manually
- ✅ **Future-proof** - New books automatically integrate

---

## 📋 SCHEMA STRUCTURE

### Core Components

1. **Books Array** - All book data in one place
2. **Curriculum Object** - Overall curriculum structure
3. **Metadata** - Schema versioning and tracking

### Book Object Structure

Each book contains:
- **Basic Info:** id, title, slug, status
- **Concepts:** Python, AI, Math concepts taught
- **Basketball:** Skill, level, context
- **Curriculum:** Grade levels, standards, phases, learning objectives
- **Game:** Exercise integration, URL, success criteria
- **Website:** Display information, page paths
- **Content:** Story files, videos, Gumroad links
- **Progression:** Prerequisites, next book, rationale

---

## 🔄 HOW IT WORKS

### Current Flow (Before Schema)
```
Update Book 1 → Update Website manually → Update Curriculum manually → Update Game manually
(4 separate updates, risk of inconsistency)
```

### New Flow (With Schema)
```
Update Schema → All 4 systems automatically sync
(1 update, perfect consistency)
```

---

## 📊 DATA FLOW

### 1. Website Reads Schema
- Book cards pull from `books[].website.card`
- Book pages pull from `books[].website.page`
- Curriculum pathway pulls from `curriculum.pathway`
- Learning objectives pull from `books[].curriculum.learningObjectives`

### 2. Books Reference Schema
- Story content references `books[].concepts`
- "What You're Learning" pulls from `books[].curriculum`
- Exercise buttons pull from `books[].game.url`
- Next book recommendation pulls from `books[].progression.nextBook`

### 3. Curriculum Uses Schema
- Three-phase pathway from `curriculum.phases`
- Grade-level adaptations from `curriculum.gradeLevels`
- Standards alignment from `books[].curriculum.standards`
- Learning progression from `books[].progression`

### 4. Game Syncs with Schema
- Exercise IDs from `books[].game.exerciseId`
- URL parameters from `books[].game.url`
- Success criteria from `books[].game.successCriteria`
- Return flow from `books[].game.returnFlow`

---

## 🚀 API ENDPOINTS (Next Step)

Once schema is defined, create API endpoints:

### GET Endpoints
- `GET /api/books` - Get all books
- `GET /api/books/:id` - Get single book
- `GET /api/curriculum` - Get curriculum structure
- `GET /api/books/:id/next` - Get next book recommendation

### POST Endpoints
- `POST /api/books` - Create new book
- `PUT /api/books/:id` - Update book
- `POST /api/sync` - Trigger sync to all systems

### Webhooks
- `POST /webhook/update` - Notify systems of changes

---

## ✅ SUCCESS METRICS

**By end of today, you should be able to:**
1. ✅ Update Book 3 data in schema
2. ✅ Website automatically shows updated Book 3 info
3. ✅ Book 3 page automatically reflects changes
4. ✅ Curriculum pathway automatically updates
5. ✅ Game exercise automatically syncs

**Test scenario:**
```
1. Update books[2].curriculum.learningObjectives in schema
2. Website book card shows new objectives
3. Book 3 page shows updated objectives
4. Curriculum pathway reflects changes
5. Game exercise criteria updates
```

---

## 📝 USAGE EXAMPLES

### Example 1: Add New Book
```json
{
  "id": 4,
  "title": "The Function",
  "slug": "the-function",
  "status": "planned",
  // ... rest of book structure
}
```
→ All systems automatically recognize Book 4

### Example 2: Update Learning Objectives
```json
{
  "books": [{
    "id": 3,
    "curriculum": {
      "learningObjectives": [
        "NEW: Understand nested loops",
        "NEW: Apply loops to data patterns"
      ]
    }
  }]
}
```
→ All systems automatically show updated objectives

### Example 3: Change Game Exercise
```json
{
  "books": [{
    "id": 3,
    "game": {
      "exerciseId": "book3_advanced_loop",
      "url": "ballcode.co/play?book=3&exercise=advanced-loop"
    }
  }]
}
```
→ Game automatically uses new exercise, website links update

---

## 🔧 IMPLEMENTATION CHECKLIST

### Phase 1: Schema Design ✅
- [x] Define JSON schema structure
- [x] Map Book 1, 2, 3 data to schema
- [x] Include curriculum connections
- [x] Include game exercise mappings
- [x] Document schema fields

### Phase 2: API Creation (Next)
- [ ] Create API endpoint structure
- [ ] Implement GET endpoints
- [ ] Implement POST endpoints
- [ ] Add validation
- [ ] Test basic CRUD operations

### Phase 3: System Integration
- [ ] Update Website to read from API
- [ ] Update Books to reference API
- [ ] Update Curriculum to pull from API
- [ ] Update Game exercises to sync via API

### Phase 4: Automation
- [ ] Implement webhook notifications
- [ ] Set up auto-sync triggers
- [ ] Add error handling
- [ ] Create monitoring/logging

---

## 📚 RESEARCH FOUNDATION

**Applied Research Principles:**

1. **Vergel et al. (2017) - Curriculum Integration Framework:**
   - Context-based integration: Schema reflects basketball context
   - Manifestation through structure: Schema structure = integration structure

2. **Lei Ye - Technology-Curriculum Integration:**
   - Multilevel model: Schema supports multiple system levels
   - Impact on outcomes: Unified schema improves consistency

3. **Turayev - Educational Technology Integration:**
   - Time efficiency: Automation saves time
   - Skills alignment: Schema standardizes skills
   - Resource optimization: Single source reduces duplication

4. **Candia et al. - Interconnected Networks:**
   - Holistic approach: Schema connects all systems
   - Network effects: Changes propagate automatically

---

## 🎯 NEXT STEPS

1. **Review Schema** - Verify structure matches all needs
2. **Create API** - Build RESTful API endpoints
3. **Integrate Systems** - Connect all 4 systems to API
4. **Test Automation** - Verify automatic syncing works
5. **Document Usage** - Create quick reference guide

---

**Status:** ✅ Schema Design Complete  
**Next:** API Creation (Hour 2)  
**Files Created:**
- `CURRICULUM-UNIFIED-SCHEMA.json` - JSON Schema definition
- `CURRICULUM-DATA-EXAMPLE.json` - Example data with Books 1, 2, 3
- `UNIFIED-SCHEMA-DOCUMENTATION.md` - This documentation






