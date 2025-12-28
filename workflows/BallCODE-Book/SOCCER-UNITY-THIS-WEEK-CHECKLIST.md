# Soccer Unity Foundation - This Week Checklist
## Day-by-Day Action Plan

**Week:** December 2025 (This Week)  
**Goal:** Foundation setup for soccer Unity project  
**Status:** 🚀 Ready to Execute

---

## 🎯 WEEK OVERVIEW

**Objective:** Get Unity project ready for soccer development
- Extract sport-agnostic framework
- Create soccer module structure
- Basic soccer environment working

---

## 📅 DAY-BY-DAY PLAN

### **DAY 1: Project Access & Setup**

#### Morning (2-3 hours):
- [ ] **Locate Unity Project**
  - [ ] Find project location
  - [ ] Document path: `_________________`
  - [ ] Verify access method
  - [ ] Test opening project

- [ ] **Verify Unity Setup**
  - [ ] Check Unity version (need: 2021.3+ or 2022.3+)
  - [ ] Current version: `_________________`
  - [ ] Install correct version if needed
  - [ ] Open project successfully

- [ ] **Check Dependencies**
  - [ ] TextMeshPro installed
  - [ ] WebGL support installed
  - [ ] Required packages verified
  - [ ] Project builds successfully

#### Afternoon (2-3 hours):
- [ ] **Create Folder Structure**
  ```bash
  Assets/Scripts/Sport/
  Assets/Scripts/Soccer/
  Assets/Scenes/Soccer/
  Assets/Prefabs/Soccer/
  ```

- [ ] **Document Current Structure**
  - [ ] List all basketball scripts
  - [ ] Document dependencies
  - [ ] Identify integration points
  - [ ] Create architecture diagram

**End of Day 1 Goal:** Unity project accessible, structure documented

---

### **DAY 2: Framework Extraction**

#### Morning (2-3 hours):
- [ ] **Create Sport-Agnostic Base**
  - [ ] Create `SportGameManager.cs` (abstract base class)
  - [ ] Create `ISportCommand.cs` (interface)
  - [ ] Create `SportLevelData.cs` (base class)
  - [ ] Test compilation

- [ ] **Review Basketball Code**
  - [ ] Identify basketball-specific code
  - [ ] List what needs extraction
  - [ ] Plan refactoring approach

#### Afternoon (2-3 hours):
- [ ] **Refactor GameModeManager**
  - [ ] Extract sport-agnostic logic
  - [ ] Create `BasketballGameManager` (inherits base)
  - [ ] Update `GameModeManager` to use base
  - [ ] Test basketball still works

**End of Day 2 Goal:** Sport-agnostic framework extracted, basketball refactored

---

### **DAY 3: Basketball Refactoring**

#### Morning (2-3 hours):
- [ ] **Move Basketball Code**
  - [ ] Create `Basketball/` folder
  - [ ] Move basketball scripts
  - [ ] Update namespaces
  - [ ] Fix references

- [ ] **Refactor PythonCodingManager**
  - [ ] Extract sport-agnostic command system
  - [ ] Create `BasketballCommands` class
  - [ ] Update `PythonCodingManager` to use commands
  - [ ] Test functionality

#### Afternoon (2-3 hours):
- [ ] **Update Level System**
  - [ ] Add `sport` field to `LevelData`
  - [ ] Update level loading logic
  - [ ] Test level loading
  - [ ] Verify basketball levels work

**End of Day 3 Goal:** Basketball code refactored, all tests pass

---

### **DAY 4: Soccer Module Creation**

#### Morning (2-3 hours):
- [ ] **Create SoccerGameManager**
  - [ ] Create `SoccerGameManager.cs`
  - [ ] Inherit from `SportGameManager`
  - [ ] Implement base methods
  - [ ] Basic initialization working

- [ ] **Create SoccerCommands**
  - [ ] Create `SoccerCommands.cs`
  - [ ] Implement `ISportCommand` interface
  - [ ] Create basic commands (dribble, pass, shoot)
  - [ ] Connect to PythonCodingManager

#### Afternoon (2-3 hours):
- [ ] **Create Soccer Scene**
  - [ ] New scene: `SoccerGame.unity`
  - [ ] Add empty GameObject: `SoccerGameManager`
  - [ ] Add `SoccerGameManager` component
  - [ ] Scene loads successfully

**End of Day 4 Goal:** Soccer module created, scene functional

---

### **DAY 5: Soccer Environment**

#### Morning (2-3 hours):
- [ ] **Create SoccerField**
  - [ ] Create `SoccerField.cs` script
  - [ ] Create field GameObject (plane or 3D model)
  - [ ] Add goals (left and right)
  - [ ] Add center circle
  - [ ] Create prefab

- [ ] **Create SoccerBall**
  - [ ] Create `SoccerBall.cs` script
  - [ ] Create ball GameObject (sphere)
  - [ ] Add Rigidbody component
  - [ ] Add physics material
  - [ ] Create prefab

#### Afternoon (2-3 hours):
- [ ] **Create SoccerPlayer**
  - [ ] Create `SoccerPlayer.cs` script
  - [ ] Create player GameObject (capsule or model)
  - [ ] Add movement script
  - [ ] Add ball interaction
  - [ ] Create prefab

- [ ] **Assemble Soccer Scene**
  - [ ] Add SoccerField to scene
  - [ ] Add SoccerBall to scene
  - [ ] Add SoccerPlayer to scene
  - [ ] Test basic scene
  - [ ] Can switch between basketball/soccer

**End of Day 5 Goal:** Basic soccer environment working

---

## ✅ WEEK 1 SUCCESS CRITERIA

### Must Have:
- [ ] Unity project accessible
- [ ] Sport-agnostic framework extracted
- [ ] Basketball code refactored (still works)
- [ ] Soccer module structure created
- [ ] Basic soccer scene functional

### Nice to Have:
- [ ] Soccer field visible
- [ ] Soccer ball physics working
- [ ] Soccer player movement working
- [ ] Can switch between sports

---

## 🚨 BLOCKERS & SOLUTIONS

### Blocker 1: Unity Project Not Found
**Solution:**
- Check common locations
- Ask developer for location
- Set up new project if needed

### Blocker 2: Unity Version Mismatch
**Solution:**
- Install required version
- Or update project to current version
- Test compatibility

### Blocker 3: Missing Dependencies
**Solution:**
- Install via Package Manager
- Check project settings
- Verify build works

### Blocker 4: Code Dependencies Unclear
**Solution:**
- Review existing scripts
- Document architecture
- Ask developer for clarification

---

## 📝 DAILY NOTES TEMPLATE

### Day 1 Notes:
```
Unity Project Location: _________________
Unity Version: _________________
Issues Found: _________________
Solutions: _________________
```

### Day 2 Notes:
```
Framework Extraction: _________________
Basketball Code Review: _________________
Refactoring Plan: _________________
```

### Day 3 Notes:
```
Basketball Refactoring: _________________
Tests Passed: _________________
Issues: _________________
```

### Day 4 Notes:
```
Soccer Module Created: _________________
Scene Setup: _________________
Working: _________________
```

### Day 5 Notes:
```
Soccer Environment: _________________
Physics Working: _________________
Ready for Week 2: _________________
```

---

## 🎯 READY FOR WEEK 2

### Checklist:
- [ ] Foundation complete
- [ ] Framework extracted
- [ ] Soccer module created
- [ ] Basic environment working
- [ ] Documentation updated

### Week 2 Goals:
- Build soccer game mechanics
- Create soccer levels
- Integrate with content system

---

**Status:** 🚀 Ready to Start  
**Priority:** HIGH - Foundation for 3-month timeline  
**Start Date:** Today


