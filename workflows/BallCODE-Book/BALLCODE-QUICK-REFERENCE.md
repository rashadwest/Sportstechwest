# BallCODE Development Quick Reference
## Quick & Full Question System

**Date:** December 10, 2025  
**Tool:** `ballcode-question.py`  
**Modes:** `--quick` | `--full`

---

## ⚡ QUICK MODE

**Use for:** Fast decisions, quick answers, initial planning

### Examples:
```bash
# Quick priority check
python3 ballcode-question.py --quick "What's the next priority for game integration?"

# Quick feature question
python3 ballcode-question.py --quick "What feature should we build for Book 1?"

# Quick integration check
python3 ballcode-question.py --quick "How does curriculum connect to game levels?"

# Quick blocker identification
python3 ballcode-question.py --quick "What's blocking level creation automation?"
```

### Quick Questions Cover:
- System identification (which system?)
- Priority assessment (High/Medium/Low)
- Immediate action (what to do first?)
- Blocker identification (what's stopping us?)

---

## 📋 FULL MODE

**Use for:** Comprehensive analysis, detailed planning, complex problems

### Examples:
```bash
# Full system analysis
python3 ballcode-question.py --full "Analyze the complete Book-to-Game integration"

# Full feature planning
python3 ballcode-question.py --full "Plan the Episode 2 level creation system"

# Full problem diagnosis
python3 ballcode-question.py --full "Diagnose why curriculum mapping isn't working"

# Full integration design
python3 ballcode-question.py --full "Design the complete Website-Book-Curriculum-Game integration"
```

### Full Questions Cover:
- System architecture analysis
- Feature/component deep dive
- Integration design
- Implementation plan
- Success metrics
- Future considerations

---

## 🎯 BALLCODE SYSTEMS

**4 Core Systems:**
1. **Website** - Content delivery, book showcase
2. **Book** - Curriculum content, stories, exercises
3. **Curriculum** - Learning paths, lesson plans
4. **Game** - Unity-based interactive learning

**Integration Goal:** Seamless connection between all 4 systems

---

## 📊 QUESTION TEMPLATES

### Quick Templates:
- `priority`: "What's the next priority for {system}?"
- `feature`: "What feature should we build for {system}?"
- `integration`: "How does {system_a} connect to {system_b}?"
- `blocker`: "What's blocking {feature}?"
- `status`: "What's the status of {component}?"
- `test`: "What should we test for {feature}?"

### Full Templates:
- `analysis`: "Analyze the complete {component}..."
- `plan`: "Plan the complete {feature} implementation..."
- `diagnose`: "Diagnose {issue} in {system}..."
- `design`: "Design the complete {system} integration..."

---

## 🚀 WORKFLOW

### Typical Development Flow:
1. **Quick Check:** `--quick "What's the priority?"`
2. **Full Analysis:** `--full "Plan the implementation"`
3. **Build:** Implement based on analysis
4. **Quick Validate:** `--quick "Did it work?"`
5. **Full Review:** `--full "Analyze the results"` (if needed)

---

## 💡 TIPS

### When to Use Quick:
- Need immediate answer
- Simple question
- Initial exploration
- Quick status check
- Blocker identification

### When to Use Full:
- Complex problem
- Major feature planning
- System design
- Integration architecture
- Comprehensive analysis needed

---

**Tool:** `ballcode-question.py`  
**Documentation:** `BALLCODE-DEVELOPMENT-QUESTIONING-SYSTEM.md`  
**Status:** ✅ Ready to use!


