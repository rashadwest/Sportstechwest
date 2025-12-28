#!/usr/bin/env python3
"""
Automate Launch Checklist
Creates comprehensive launch readiness checklist

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent
LAUNCH_DIR = PROJECT_ROOT / "documents" / "launch-prep"

# Ensure directory exists
LAUNCH_DIR.mkdir(parents=True, exist_ok=True)

def create_launch_readiness_checklist():
    """Create comprehensive launch readiness checklist."""
    checklist = {
        "launch_date": "January 14, 2026",
        "days_until_launch": 29,
        "current_status": "90% Complete",
        "target_status": "95% Complete",
        "checklists": {
            "system_readiness": {
                "title": "System Readiness (95% Target)",
                "items": [
                    {"task": "Website complete with visuals", "status": "pending", "priority": "critical"},
                    {"task": "Book 1 complete and functional", "status": "complete", "priority": "critical"},
                    {"task": "Curriculum integrated", "status": "complete", "priority": "critical"},
                    {"task": "Game integration working", "status": "complete", "priority": "critical"},
                    {"task": "Measurement system operational", "status": "complete", "priority": "high"},
                    {"task": "Testing complete", "status": "complete", "priority": "critical"},
                    {"task": "Mobile responsive", "status": "complete", "priority": "high"},
                    {"task": "Teacher resources ready", "status": "complete", "priority": "high"}
                ]
            },
            "content_readiness": {
                "title": "Content Readiness",
                "items": [
                    {"task": "Visual assets generated", "status": "pending", "priority": "critical"},
                    {"task": "Launch materials reviewed", "status": "pending", "priority": "high"},
                    {"task": "Demo script ready", "status": "complete", "priority": "high"},
                    {"task": "One-pager ready", "status": "complete", "priority": "high"},
                    {"task": "Launch announcements ready", "status": "complete", "priority": "high"}
                ]
            },
            "promotion_readiness": {
                "title": "Promotion Readiness (Dec 31 - Jan 13)",
                "items": [
                    {"task": "Coming soon page created", "status": "complete", "priority": "high"},
                    {"task": "Daily content templates ready", "status": "complete", "priority": "high"},
                    {"task": "Email templates ready", "status": "complete", "priority": "high"},
                    {"task": "Social media templates ready", "status": "complete", "priority": "high"},
                    {"task": "Content calendar created", "status": "complete", "priority": "high"},
                    {"task": "School outreach structure ready", "status": "complete", "priority": "medium"}
                ]
            },
            "technical_readiness": {
                "title": "Technical Readiness",
                "items": [
                    {"task": "Website deployed and live", "status": "pending", "priority": "critical"},
                    {"task": "All links working", "status": "complete", "priority": "critical"},
                    {"task": "Integration flow tested", "status": "complete", "priority": "critical"},
                    {"task": "Mobile testing complete", "status": "pending", "priority": "high"},
                    {"task": "Performance optimized", "status": "complete", "priority": "medium"},
                    {"task": "Analytics tracking active", "status": "complete", "priority": "high"}
                ]
            },
            "launch_day": {
                "title": "Launch Day (Jan 14, 2026)",
                "items": [
                    {"task": "Official launch announcement", "status": "pending", "priority": "critical"},
                    {"task": "Press release sent", "status": "pending", "priority": "high"},
                    {"task": "Social media blitz", "status": "pending", "priority": "high"},
                    {"task": "Email to all contacts", "status": "pending", "priority": "high"},
                    {"task": "School signup open", "status": "pending", "priority": "critical"},
                    {"task": "System monitoring active", "status": "pending", "priority": "high"}
                ]
            }
        }
    }
    
    checklist_file = LAUNCH_DIR / "launch-readiness-checklist.json"
    with open(checklist_file, 'w') as f:
        json.dump(checklist, f, indent=2)
    
    # Create markdown version
    md_content = f"""# 🚀 Launch Readiness Checklist

**Launch Date:** January 14, 2026  
**Days Until Launch:** 29  
**Current Status:** 90% Complete  
**Target Status:** 95% Complete

---

## ✅ System Readiness (95% Target)

- [x] Book 1 complete and functional
- [x] Curriculum integrated
- [x] Game integration working
- [x] Measurement system operational
- [x] Testing complete
- [x] Mobile responsive
- [x] Teacher resources ready
- [ ] **Visual assets generated** ⚠️ CRITICAL

---

## 📚 Content Readiness

- [x] Demo script ready
- [x] One-pager ready
- [x] Launch announcements ready
- [ ] **Visual assets generated** ⚠️ CRITICAL
- [ ] **Launch materials reviewed** ⚠️ HIGH

---

## 📢 Promotion Readiness (Dec 31 - Jan 13)

- [x] Coming soon page created
- [x] Daily content templates ready
- [x] Email templates ready
- [x] Social media templates ready
- [x] Content calendar created
- [x] School outreach structure ready

---

## 🔧 Technical Readiness

- [x] All links working
- [x] Integration flow tested
- [x] Performance optimized
- [x] Analytics tracking active
- [ ] **Website deployed and live** ⚠️ CRITICAL
- [ ] **Mobile testing complete** ⚠️ HIGH

---

## 🎯 Launch Day (Jan 14, 2026)

- [ ] Official launch announcement
- [ ] Press release sent
- [ ] Social media blitz
- [ ] Email to all contacts
- [ ] School signup open
- [ ] System monitoring active

---

## 📊 Progress Summary

**Completed:** {sum(1 for section in checklist['checklists'].values() for item in section['items'] if item['status'] == 'complete')} items  
**Pending:** {sum(1 for section in checklist['checklists'].values() for item in section['items'] if item['status'] == 'pending')} items  
**Critical Pending:** {sum(1 for section in checklist['checklists'].values() for item in section['items'] if item['status'] == 'pending' and item['priority'] == 'critical')} items

---

**Next Critical Actions:**
1. Generate visual assets (2-3 hours)
2. Review launch materials (30 min)
3. Deploy website (1 hour)
4. Complete mobile testing (1 hour)

---

*Generated: {datetime.now().strftime('%B %d, %Y')}*
"""
    
    md_file = LAUNCH_DIR / "launch-readiness-checklist.md"
    with open(md_file, 'w') as f:
        f.write(md_content)
    
    print(f"✅ Created: {checklist_file}")
    print(f"✅ Created: {md_file}")
    return checklist_file, md_file

def main():
    """Main function."""
    print("=" * 60)
    print("✅ Launch Checklist Automation")
    print("=" * 60)
    print()
    
    create_launch_readiness_checklist()
    
    print()
    print("=" * 60)
    print("✅ Launch Checklist Complete!")
    print("=" * 60)
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)


