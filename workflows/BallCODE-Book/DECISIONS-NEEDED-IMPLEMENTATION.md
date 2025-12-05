# Decisions Needed: Rules Document Implementation
**Date:** December 2025  
**Purpose:** Clear decision points before implementing rules additions

---

## Quick Summary

**✅ Ready to Implement (5 items):** Can proceed immediately  
**⚠️ Decisions Needed (11 items):** Need your input before proceeding  
**📋 Total Recommendations:** 5 major additions evaluated

---

## ✅ Ready to Implement (No Decisions Needed)

These can be added to the rules document immediately:

### 1. Execution Instructions - Basic Structure
- Add section on how to run Python scripts
- Add section on how to run Unity scripts
- Document entry points
- **Note:** Will handle README redundancy decision separately

### 2. Execution Verification - Checklist Items
- Add "Code runs successfully" to checklist
- Add "Output verified" to checklist
- Add "Environment requirements documented" to checklist
- **Note:** Will handle automation decision separately

### 3. Cross-Platform Documentation
- Document Mac/Linux/Windows differences
- Add platform detection guidance
- **Status:** Can implement immediately

### 4. Error Message Standards
- Require clear error messages
- Require recovery suggestions
- **Status:** Can implement immediately

### 5. Entry Point Documentation
- Document main entry points
- List required arguments
- Provide usage examples
- **Status:** Can implement immediately

---

## ⚠️ Decisions Needed (Your Input Required)

### Decision Set 1: Dependency Management (4 decisions)

#### Decision 1.1: Optional Dependencies Approach
**Context:** Some scripts have optional dependencies (e.g., `analyze_game_screenshots.py` can use OpenAI OR Anthropic)

**Options:**
- **Option A:** requirements.txt with optional extras
  - Format: `pip install -e ".[openai]"` or `pip install -e ".[anthropic]"`
  - Pros: Standard Python practice, flexible
  - Cons: More complex setup, requires setup.py
  
- **Option B:** Separate requirements files
  - Format: `requirements-openai.txt`, `requirements-anthropic.txt`
  - Pros: Clear separation, simple
  - Cons: Multiple files to maintain
  
- **Option C:** Document in comments, let user choose
  - Format: Comments in script, user installs manually
  - Pros: Simplest, no automation
  - Cons: Manual process, easy to miss

**Your Decision:** [ ] Option A  [ ] Option B  [ ] Option C

---

#### Decision 1.2: Multiple Dependency Sets
**Context:** Different scripts need different dependencies (video processing vs. API calls vs. automation)

**Options:**
- **Option A:** One requirements.txt with all dependencies
  - Pros: Simplest, one file to maintain
  - Cons: Installs unused packages, larger environment
  
- **Option B:** requirements-base.txt + requirements-{script}.txt
  - Format: `requirements-base.txt`, `requirements-video.txt`, `requirements-api.txt`
  - Pros: Clean separation, smaller environments
  - Cons: More files, more complex
  
- **Option C:** Document per-script in comments
  - Pros: Flexible, no automation needed
  - Cons: Manual process, easy to miss

**Your Decision:** [ ] Option A  [ ] Option B  [ ] Option C

---

#### Decision 1.3: Unity Dependency Management
**Context:** Unity packages managed differently than Python packages

**Options:**
- **Option A:** Document in markdown file
  - Format: `Unity-Packages.md` with list
  - Pros: Simple, no automation needed
  - Cons: Manual, might get out of sync
  
- **Option B:** Unity package manifest
  - Format: `Packages/manifest.json` (requires Unity project structure)
  - Pros: Automated, standard Unity practice
  - Cons: Requires Unity project in repo
  
- **Option C:** Hybrid approach
  - Format: Markdown for documentation, manifest if available
  - Pros: Flexible, supports both
  - Cons: Two sources of truth

**Your Decision:** [ ] Option A  [ ] Option B  [ ] Option C

---

#### Decision 1.4: Version Pinning Strategy
**Context:** How strictly to pin package versions

**Options:**
- **Option A:** Pin all versions exactly
  - Format: `opencv-python==4.8.0.76`
  - Pros: Fully reproducible, no surprises
  - Cons: Might conflict, harder to update
  
- **Option B:** Pin major versions only
  - Format: `opencv-python>=4.8.0,<5.0.0`
  - Pros: Flexible, gets patches
  - Cons: Might break with minor updates
  
- **Option C:** Pin critical, unpin others
  - Format: Pin OpenCV, unpin requests
  - Pros: Balanced approach
  - Cons: Inconsistent, requires judgment

**Your Decision:** [ ] Option A  [ ] Option B  [ ] Option C

---

### Decision Set 2: Environment Setup (2 decisions)

#### Decision 2.1: Virtual Environment Requirement
**Context:** Should virtual environments be required, recommended, or optional?

**Options:**
- **Option A:** Required for all Python scripts
  - Pros: Clean environments, no conflicts
  - Cons: More complex setup, might discourage use
  
- **Option B:** Recommended but not required
  - Pros: Flexible, simpler for beginners
  - Cons: Might have conflicts, less reproducible
  
- **Option C:** Required for some scripts, optional for others
  - Pros: Pragmatic, balances needs
  - Cons: Inconsistent, requires judgment

**Your Decision:** [ ] Option A  [ ] Option B  [ ] Option C

---

#### Decision 2.2: Unity Validation Approach
**Context:** How to verify Unity version and packages

**Options:**
- **Option A:** Manual check only
  - Format: Document in rules, user checks manually
  - Pros: Simple, always works
  - Cons: Not automated, easy to miss
  
- **Option B:** Automated check via project files
  - Format: Check `ProjectSettings/ProjectVersion.txt`
  - Pros: Automated, catches issues
  - Cons: Requires Unity project in repo
  
- **Option C:** Hybrid approach
  - Format: Try automated, fallback to manual instructions
  - Pros: Best of both worlds
  - Cons: More complex

**Your Decision:** [ ] Option A  [ ] Option B  [ ] Option C

---

### Decision Set 3: Execution Instructions (1 decision)

#### Decision 3.1: Redundancy with README
**Context:** Rules document vs. README files - how to handle overlap?

**Options:**
- **Option A:** Keep in rules, reference README for details
  - Pros: Rules are complete, README has details
  - Cons: Some duplication
  
- **Option B:** Keep minimal in rules, full docs in README
  - Pros: Less duplication, README is source of truth
  - Cons: Rules less complete
  
- **Option C:** Rules point to README, no duplication
  - Pros: No duplication, single source of truth
  - Cons: Rules less actionable

**Your Decision:** [ ] Option A  [ ] Option B  [ ] Option C

---

### Decision Set 4: Configuration Management (3 decisions)

#### Decision 4.1: Existing Hardcoded Values
**Context:** Scripts like `extract_frames.py` have hardcoded paths (e.g., `video_path = "BallCODE_Addy.mov"`)

**Options:**
- **Option A:** Refactor all scripts immediately
  - Pros: Clean, consistent
  - Cons: Time-consuming, might break existing workflows
  
- **Option B:** Document pattern, refactor gradually
  - Pros: Pragmatic, doesn't break existing
  - Cons: Inconsistent during transition
  
- **Option C:** Only apply to new scripts
  - Pros: Simple, no disruption
  - Cons: Leaves technical debt, inconsistent

**Your Decision:** [ ] Option A  [ ] Option B  [ ] Option C

---

#### Decision 4.2: Configuration Complexity Requirement
**Context:** Should all scripts use configuration management, or only some?

**Options:**
- **Option A:** Require for all scripts
  - Pros: Consistent, prevents hardcoded values
  - Cons: Might be overkill for simple scripts
  
- **Option B:** Require for scripts with secrets/paths
  - Pros: Pragmatic, focuses on what matters
  - Cons: Requires judgment, might be inconsistent
  
- **Option C:** Recommend, not require
  - Pros: Flexible, no enforcement
  - Cons: Might be ignored, inconsistent

**Your Decision:** [ ] Option A  [ ] Option B  [ ] Option C

---

#### Decision 4.3: Config File Format
**Context:** What format for configuration files?

**Options:**
- **Option A:** JSON
  - Pros: Standard, easy to parse, no extra dependencies
  - Cons: Less human-readable, no comments
  
- **Option B:** YAML
  - Pros: Human-readable, supports comments
  - Cons: Requires PyYAML library, indentation sensitive
  
- **Option C:** .env file
  - Pros: Simple, standard for environment variables
  - Cons: Limited structure, key-value only

**Your Decision:** [ ] Option A  [ ] Option B  [ ] Option C

---

### Decision Set 5: Execution Verification (1 decision)

#### Decision 5.1: Automation vs Manual
**Context:** How to verify code runs correctly?

**Options:**
- **Option A:** Automated where possible
  - Format: Scripts to verify execution
  - Pros: Efficient, catches issues early
  - Cons: Requires scripts, more complex
  
- **Option B:** Manual checklist only
  - Format: Human checks checklist
  - Pros: Simple, flexible
  - Cons: Time-consuming, easy to miss
  
- **Option C:** Hybrid approach
  - Format: Automated for common checks, manual for complex
  - Pros: Balanced, practical
  - Cons: More complex, requires judgment

**Your Decision:** [ ] Option A  [ ] Option B  [ ] Option C

---

## Implementation Plan

### Phase 1: Immediate (No Decisions Needed)
1. ✅ Add execution instructions section (basic structure)
2. ✅ Add execution verification checklist items
3. ✅ Add cross-platform documentation
4. ✅ Add error message standards
5. ✅ Add entry point documentation

### Phase 2: After Your Decisions
6. ⚠️ Create requirements.txt (after Decision 1.1, 1.2, 1.4)
7. ⚠️ Create verify_setup.py (after Decision 2.1, 2.2)
8. ⚠️ Add dependency management section (after all Decision Set 1)
9. ⚠️ Add environment setup section (after Decision Set 2)
10. ⚠️ Complete execution instructions (after Decision 3.1)
11. ⚠️ Add configuration management section (after Decision Set 4)
12. ⚠️ Add automation to verification (after Decision 5.1)

### Phase 3: Refinement (After Implementation)
13. Refactor existing scripts (based on Decision 4.1)
14. Add automation scripts (based on Decision 5.1)
15. Test and refine

---

## How to Provide Decisions

**Option 1:** Reply with decisions in format:
```
Decision 1.1: Option B
Decision 1.2: Option A
Decision 1.3: Option C
...
```

**Option 2:** Edit this document and mark your choices with [X]

**Option 3:** Discuss each decision set separately

---

## Guardrails Summary

**Principle:** I will NOT implement anything that requires a decision until you provide it.

**What I WILL do:**
- ✅ Implement items marked "Ready to Implement"
- ✅ Ask clarifying questions if needed
- ✅ Provide recommendations based on AIMCODE analysis

**What I WON'T do:**
- ❌ Make assumptions about your preferences
- ❌ Implement solutions with multiple valid paths
- ❌ Proceed without your explicit decisions

---

**Next Steps:**
1. Review decisions needed
2. Provide your choices
3. I'll implement based on your decisions
4. We'll refine as needed

---

**Questions?** If any decision is unclear, I can provide more detail or examples.


