# Critical Decisions Only: Rules Implementation
**Date:** December 2025  
**Principle:** Only ask about decisions that could negatively impact the build

---

## Re-Evaluation: Critical vs. Non-Critical

### ✅ Non-Critical (Making Reasonable Defaults)

These are implementation details with minimal negative impact. I'll use reasonable defaults:

1. **Optional Dependencies** → **Default: Document in comments + one requirements.txt**
   - Impact: Minimal - just documentation
   - Default: Include all optional deps in requirements.txt with comments

2. **Multiple Dependency Sets** → **Default: One requirements.txt with all dependencies**
   - Impact: Minimal - just installs a few extra packages
   - Default: Single file, simplest approach

3. **Unity Dependency Management** → **Default: Simple markdown documentation**
   - Impact: Minimal - just documentation
   - Default: Unity-Packages.md file

4. **Virtual Environment** → **Default: Recommended, not required**
   - Impact: Minimal - flexible approach
   - Default: Recommend in rules, don't enforce

5. **Unity Validation** → **Default: Manual check with clear instructions**
   - Impact: Minimal - just documentation
   - Default: Document in rules, user checks manually

6. **README Redundancy** → **Default: Minimal in rules, full in README**
   - Impact: Minimal - just organization
   - Default: Rules have essentials, README has details

7. **Config File Format** → **Default: JSON (standard, no extra deps)**
   - Impact: Minimal - just format choice
   - Default: JSON format

8. **Automation vs Manual** → **Default: Start with manual, add automation later**
   - Impact: Minimal - can add automation later
   - Default: Manual checklist now, automation optional

---

## ⚠️ Critical Decisions (Could Negatively Impact Build)

These decisions could break things or cause significant problems:

### Decision 1: Version Pinning Strategy
**Why Critical:** Wrong choice could cause dependency conflicts or break builds

**Options:**
- **Option A:** Pin all versions exactly (`opencv-python==4.8.0.76`)
  - Risk: High - might conflict with other projects, harder to update
  - Impact: Could prevent installation if conflicts exist
  
- **Option B:** Pin major versions only (`opencv-python>=4.8.0,<5.0.0`)
  - Risk: Medium - might break with minor updates, but gets patches
  - Impact: Could break if minor version has breaking changes
  
- **Option C:** Pin critical packages only, unpin others
  - Risk: Low - balanced approach
  - Impact: Minimal - only critical packages pinned

**Recommendation:** Option C (pin critical like OpenCV, unpin others like requests)

**Your Decision:** [ ] Option A  [ ] Option B  [ ] Option C

---

### Decision 2: Existing Hardcoded Values Refactoring
**Why Critical:** Could break existing workflows that depend on current behavior

**Options:**
- **Option A:** Refactor all scripts immediately
  - Risk: High - could break existing workflows, time-consuming
  - Impact: Could break scripts that are currently working
  
- **Option B:** Document pattern, refactor gradually
  - Risk: Low - doesn't break existing, allows gradual migration
  - Impact: Minimal - existing scripts keep working
  
- **Option C:** Only apply to new scripts
  - Risk: Low - no disruption
  - Impact: Minimal - leaves technical debt but no breakage

**Recommendation:** Option B (document pattern, refactor gradually)

**Your Decision:** [ ] Option A  [ ] Option B  [ ] Option C

---

### Decision 3: Configuration Complexity Requirement
**Why Critical:** Could add unnecessary complexity or allow problems to persist

**Options:**
- **Option A:** Require for all scripts
  - Risk: Medium - might be overkill for simple scripts, adds overhead
  - Impact: Could slow down development, add unnecessary complexity
  
- **Option B:** Require for scripts with secrets/paths
  - Risk: Low - pragmatic, focuses on what matters
  - Impact: Minimal - only applies where needed
  
- **Option C:** Recommend, not require
  - Risk: Medium - might be ignored, problems persist
  - Impact: Could allow hardcoded values to continue

**Recommendation:** Option B (require for secrets/paths, recommend for others)

**Your Decision:** [ ] Option A  [ ] Option B  [ ] Option C

---

## Implementation Plan with Defaults

### Phase 1: Immediate Implementation (Using Defaults)
1. ✅ Add execution instructions section
2. ✅ Add execution verification checklist items
3. ✅ Add cross-platform documentation
4. ✅ Add error message standards
5. ✅ Add entry point documentation
6. ✅ Create requirements.txt (one file, all deps, optional in comments)
7. ✅ Add dependency management section (using defaults)
8. ✅ Add environment setup section (recommend venv, manual Unity check)
9. ✅ Add configuration management section (JSON format, require for secrets/paths)
10. ✅ Create verify_setup.py (basic checks, clear errors)

### Phase 2: After Critical Decisions
11. ⚠️ Update requirements.txt with version pinning (after Decision 1)
12. ⚠️ Refactor existing scripts (after Decision 2)
13. ⚠️ Update configuration requirements (after Decision 3)

---

## Summary

**Making Defaults For (8 items):**
- Optional dependencies → One requirements.txt with comments
- Multiple dependency sets → One requirements.txt
- Unity dependencies → Markdown file
- Virtual environment → Recommended, not required
- Unity validation → Manual check
- README redundancy → Minimal in rules, full in README
- Config format → JSON
- Automation → Manual checklist, automation optional

**Need Your Decision (3 items):**
1. Version pinning strategy (could cause conflicts)
2. Existing hardcoded values refactoring (could break workflows)
3. Configuration complexity requirement (could add complexity or allow problems)

---

**Next Steps:**
1. I'll implement everything with defaults
2. You provide 3 critical decisions
3. I'll update implementation based on your decisions


