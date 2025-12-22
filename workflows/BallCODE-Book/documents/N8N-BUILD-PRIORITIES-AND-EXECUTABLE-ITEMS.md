# n8n Build Priorities & Executable Items
## From Questions to 100% Understanding - Action Plan

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 12, 2025  
**Status:** 🎯 Ready for Implementation  
**Source:** `QUESTIONS-TO-100-PERCENT-UNDERSTANDING.md`

---

## 🚨 IMMEDIATE FIX (Do First - 3 minutes)

### Fix 1: Replace executeCommand with Code Node
**Priority:** CRITICAL - Blocks workflow execution  
**Time:** 3 minutes  
**Status:** ⏳ PENDING  
**File:** `REPLACE-WITH-CODE-NODE-NOW.md`

**What to do:**
1. Delete "Clone/Update Repository" executeCommand node
2. Add Code node with provided JavaScript code
3. Test execution
4. Verify git clone/pull works

**Impact:** Workflow will actually execute git commands instead of silently failing

---

## 🔥 CRITICAL PRIORITY (Blocking Integration)

### Build 1: URL Parameter System for Unity WebGL
**Priority:** CRITICAL  
**Status:** ⏳ NEEDS R&D  
**Dependencies:** Unity codebase access, WebGL research

**Executable Items:**
- [ ] Research Unity WebGL URL parameter handling (AIMCODE R&D)
- [ ] Determine exact URL format: `ballcode.co/play?book=1&exercise=foundation-block&source=book`
- [ ] Implement URL parameter parsing in Unity (BallCODEStarter.cs or new script)
- [ ] Handle missing/invalid parameters gracefully
- [ ] Test parameter passing from website to game
- [ ] Document parameter format and validation rules

**n8n Integration:**
- n8n can generate correct URLs when triggering game
- n8n can validate URL format before deployment
- n8n can test URL parameter passing

**Estimated Time:** 4-6 hours (R&D + implementation)

---

### Build 2: Exercise Data Structure & Loading System
**Priority:** CRITICAL  
**Status:** ⏳ NEEDS R&D  
**Dependencies:** Unity codebase analysis, JSON structure design

**Executable Items:**
- [ ] Analyze current exercise loading mechanism (GitHub code review)
- [ ] Design unified exercise data structure (JSON format)
- [ ] Create exercise data storage system (StreamingAssets, Resources, or ScriptableObjects)
- [ ] Implement exercise loading in GameModeManager.cs
- [ ] Create exercise completion detection system
- [ ] Implement exercise progress tracking
- [ ] Test exercise loading for all game modes (Tutorial, Coding, Math, Chess, Freeplay)

**n8n Integration:**
- n8n can generate exercise JSON files from level templates
- n8n can validate exercise data structure
- n8n can update exercise data automatically
- n8n can create new exercises from templates

**Estimated Time:** 6-8 hours (R&D + implementation)

---

### Build 3: Game Mode System Enhancement
**Priority:** CRITICAL  
**Status:** ⏳ PARTIAL (modes exist, need integration)  
**Dependencies:** Current game modes: Tutorial, Coding, Math, Chess, Freeplay

**Executable Items:**
- [ ] Document all game modes and their differences
- [ ] Implement mode switching system (currently requires main menu)
- [ ] Create mode-specific exercise mapping
- [ ] Implement book-to-mode connection (books unlock game modes)
- [ ] Add mode selection from URL parameters
- [ ] Test all mode transitions

**n8n Integration:**
- n8n can generate mode-specific exercises
- n8n can validate mode configurations
- n8n can test mode switching

**Estimated Time:** 4-6 hours

---

### Build 4: Error Handling & Guardrails System
**Priority:** CRITICAL  
**Status:** ⏳ NEEDS DEVELOPMENT  
**Dependencies:** All integration points

**Executable Items:**
- [ ] Implement error handling in BallCODEStarter.cs
- [ ] Create guardrails to prevent skipping steps
- [ ] Add error logging system (AIMCODE logging)
- [ ] Implement graceful degradation for missing data
- [ ] Create error recovery mechanisms
- [ ] Test error scenarios (missing params, failed loads, etc.)

**n8n Integration:**
- n8n can monitor error logs
- n8n can trigger fixes automatically
- n8n can test error scenarios

**Estimated Time:** 6-8 hours

---

## ⚠️ HIGH PRIORITY (Important for Quality)

### Build 5: Level Creation Automation
**Priority:** HIGH  
**Status:** ⏳ READY (templates exist)  
**Dependencies:** Level templates, video assets

**Executable Items:**
- [ ] Create level generation workflow in n8n
- [ ] Use level templates (book1_coding_1_2.json, etc.)
- [ ] Automate level creation from book data
- [ ] Generate Math levels (easier - no videos needed)
- [ ] Generate Coding levels (need videos)
- [ ] Generate Chess levels (hardest - save for last)

**n8n Integration:**
- n8n workflow: "Create New Level"
  - Input: Book number, exercise type, move description
  - Process: Generate JSON from template
  - Output: Level JSON file ready for Unity
- n8n can batch create multiple levels
- n8n can validate level structure

**Estimated Time:** 2-3 hours (workflow creation) + ongoing level generation

**User Input Needed:**
- Move descriptions for each level
- Video selection (or AI can suggest which move/hands)

---

### Build 6: Feedback System Enhancement
**Priority:** HIGH  
**Status:** ⏳ NEEDS DEVELOPMENT  
**Dependencies:** Current feedback system (only "nice shot!" exists)

**Executable Items:**
- [ ] Design feedback system for all game modes
- [ ] Implement step-by-step feedback (currently only Tutorial has this)
- [ ] Add learning feedback ("You learned X today")
- [ ] Create feedback for block coding validation
- [ ] Add feedback for exercise completion
- [ ] Test feedback across all modes

**n8n Integration:**
- n8n can generate feedback messages
- n8n can update feedback content
- n8n can test feedback triggers

**Estimated Time:** 4-6 hours

---

### Build 7: Book-to-Game Transition Enhancement
**Priority:** HIGH  
**Status:** ⏳ NEEDS DEVELOPMENT  
**Dependencies:** URL parameter system, exercise system

**Executable Items:**
- [ ] Design "Try the Exercise" button flow
- [ ] Show preview of book + exercise connection
- [ ] Implement seamless transition (currently new window)
- [ ] Add loading states
- [ ] Create failure handling (safety net)
- [ ] Test transition flow

**n8n Integration:**
- n8n can test transition URLs
- n8n can validate exercise connections
- n8n can monitor transition success rates

**Estimated Time:** 3-4 hours

---

### Build 8: UI/UX Improvements
**Priority:** HIGH  
**Status:** ⏳ NEEDS DEVELOPMENT  
**Dependencies:** Unity UI system

**Executable Items:**
- [ ] Improve UI/UX for better game feel
- [ ] Make it feel like a game at all times (not school)
- [ ] Add visual polish
- [ ] Improve user instructions
- [ ] Test UI improvements

**n8n Integration:**
- n8n can track UI/UX metrics
- n8n can A/B test UI changes

**Estimated Time:** Ongoing (iterative)

---

## 📊 MEDIUM PRIORITY (Nice to Know)

### Build 9: Build Process Automation & Testing
**Priority:** MEDIUM  
**Status:** ⏳ PARTIAL (builds exist, testing needed)  
**Dependencies:** Current build system

**Executable Items:**
- [ ] Add automated testing after hourly builds
- [ ] Implement build verification system
- [ ] Create build artifact management
- [ ] Add build rollback capability
- [ ] Implement build error detection and logging
- [ ] Test build process end-to-end

**n8n Integration:**
- n8n can trigger build tests
- n8n can verify build success
- n8n can rollback failed builds
- n8n can log build metrics

**Estimated Time:** 4-6 hours

---

### Build 10: Monitoring & Logging System
**Priority:** MEDIUM  
**Status:** ⏳ NEEDS DEVELOPMENT  
**Dependencies:** Database setup (exists but not used)

**Executable Items:**
- [ ] Set up logging system (AIMCODE logging)
- [ ] Implement error tracking
- [ ] Create monitoring dashboard
- [ ] Add performance metrics
- [ ] Test logging system

**n8n Integration:**
- n8n can aggregate logs
- n8n can trigger alerts
- n8n can generate reports

**Estimated Time:** 3-4 hours

---

## 🎯 ROADMAP ITEMS (Future Features)

### Roadmap 1: Progress Tracking & Dashboard
**Priority:** ROADMAP  
**Status:** ⏳ PLANNED  
**User Request:** "Put this on the roadmap"

**Features:**
- Daily streaks tracking
- Learning progress tracking
- Exercise completion tracking
- Book completion tracking
- Comprehensive dashboard

**n8n Integration:**
- n8n can update progress data
- n8n can generate progress reports
- n8n can trigger progress notifications

---

### Roadmap 2: Data Collection for Research
**Priority:** ROADMAP  
**Status:** ⏳ PLANNED  
**User Request:** "I would love to save student data for research purposes with consent"

**Features:**
- Consent system
- Data collection system
- Research data storage
- Privacy compliance

**n8n Integration:**
- n8n can process consent
- n8n can anonymize data
- n8n can export research data

---

### Roadmap 3: Python Mode Implementation
**Priority:** ROADMAP  
**Status:** ⏳ PLANNED  
**User Request:** "It was just a thought to make this more practical for serious programmers"

**Features:**
- Python code execution system
- Python runtime integration
- Python code validation
- Python feedback system

**n8n Integration:**
- n8n can generate Python exercises
- n8n can validate Python code
- n8n can test Python execution

---

### Roadmap 4: Building Game Mode
**Priority:** ROADMAP - TOP PRIORITY  
**Status:** ⏳ PLANNED  
**User Request:** "Save this to memory and lets create a plan around this. Make sure we lock this in and put it on the roadmap. It is a top priority because I think it gives students the ability to become architecture types."

**Features:**
- Court building game mode
- Block-by-block building system
- Architecture-focused gameplay
- Creative construction tools

**n8n Integration:**
- n8n can generate building challenges
- n8n can validate building structures
- n8n can track building progress

---

### Roadmap 5: Seamless Window Integration
**Priority:** ROADMAP  
**Status:** ⏳ PLANNED  
**User Request:** "Put this on the roadmap and make it seamless"

**Features:**
- Same-window game loading (currently new window)
- Seamless book-to-game transition
- Integrated experience

**n8n Integration:**
- n8n can test window integration
- n8n can monitor transition performance

---

## 📋 n8n WORKFLOW PRIORITIES

### Priority 1: Fix Current Workflow (IMMEDIATE)
- [x] Identify executeCommand issue
- [ ] Replace with Code node
- [ ] Test workflow execution
- [ ] Verify git operations work

### Priority 2: Level Creation Workflow (HIGH VALUE)
- [ ] Create "Generate Level" workflow
- [ ] Input: Book, exercise type, move description
- [ ] Process: Template → JSON generation
- [ ] Output: Level JSON file
- [ ] Test level generation

### Priority 3: Exercise Data Management Workflow
- [ ] Create "Update Exercise Data" workflow
- [ ] Validate exercise structure
- [ ] Update exercise files
- [ ] Test exercise loading

### Priority 4: Build Testing Workflow
- [ ] Create "Test Build" workflow
- [ ] Trigger after builds
- [ ] Verify build success
- [ ] Log build metrics

### Priority 5: Error Monitoring Workflow
- [ ] Create "Monitor Errors" workflow
- [ ] Aggregate error logs
- [ ] Trigger alerts
- [ ] Generate error reports

---

## 🎯 EXECUTION ORDER

### Week 1: Critical Fixes
1. **Day 1:** Fix executeCommand → Code node (3 min)
2. **Day 1-2:** URL Parameter System R&D + Implementation (4-6 hours)
3. **Day 2-3:** Exercise Data Structure R&D + Implementation (6-8 hours)
4. **Day 3-4:** Error Handling System (6-8 hours)

### Week 2: High Priority Builds
5. **Day 1-2:** Level Creation Automation (2-3 hours workflow + ongoing)
6. **Day 2-3:** Feedback System Enhancement (4-6 hours)
7. **Day 3-4:** Book-to-Game Transition (3-4 hours)
8. **Day 4-5:** UI/UX Improvements (ongoing)

### Week 3: Medium Priority & Automation
9. **Day 1-2:** Build Testing System (4-6 hours)
10. **Day 2-3:** Monitoring & Logging (3-4 hours)
11. **Day 3-5:** n8n Workflow Enhancements

---

## 📊 PROGRESS TRACKING

### Current Status
- **Immediate Fix:** ⏳ 0% (needs execution)
- **Critical Priority:** ⏳ 0% (needs R&D)
- **High Priority:** ⏳ 20% (some templates exist)
- **Medium Priority:** ⏳ 10% (foundation exists)
- **Roadmap Items:** 📋 Planned

### Success Metrics
- ✅ Workflow executes successfully
- ✅ Levels can be generated automatically
- ✅ Exercises load correctly
- ✅ URL parameters work
- ✅ Error handling prevents crashes
- ✅ Feedback system guides users
- ✅ Build process is reliable

---

## 🔍 R&D REQUIREMENTS (AIMCODE)

**Items needing research before implementation:**
1. Unity WebGL URL parameter handling
2. Exercise data structure best practices
3. Game mode switching mechanisms
4. Error handling patterns in Unity WebGL
5. Feedback system design patterns
6. Build testing methodologies
7. Logging systems for Unity WebGL

**Research Method:** AIMCODE R&D Protocol
- Search for peer-reviewed solutions
- Find Unity-specific best practices
- Identify proven patterns
- Document findings
- Apply to implementation

---

## ✅ NEXT ACTIONS

### Immediate (Today):
1. Fix executeCommand → Code node (3 minutes)
2. Review this document with user
3. Confirm priorities

### Short-term (This Week):
4. Start R&D on URL parameter system
5. Begin exercise data structure design
6. Create level generation workflow

### Medium-term (Next 2 Weeks):
7. Complete critical priority builds
8. Implement high priority features
9. Set up monitoring and logging

---

**Version:** 1.0  
**Created:** December 12, 2025  
**Status:** Ready for Execution


