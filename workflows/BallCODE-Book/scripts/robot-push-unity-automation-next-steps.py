#!/usr/bin/env python3
"""
Robot: Push Unity Automation Next Steps
Automates the next steps for Unity UI/UX automation implementation.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DOCS_DIR = PROJECT_ROOT / "documents"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
NC = '\033[0m'

def print_header(text):
    print(f"\n{BLUE}{'='*70}{NC}")
    print(f"{BLUE}{text:^70}{NC}")
    print(f"{BLUE}{'='*70}{NC}\n")

def print_success(text):
    print(f"{GREEN}✅ {text}{NC}")

def print_error(text):
    print(f"{RED}❌ {text}{NC}")

def print_warning(text):
    print(f"{YELLOW}⚠️  {text}{NC}")

def print_info(text):
    print(f"{BLUE}ℹ️  {text}{NC}")

def check_unity_project() -> Dict:
    """Check Unity project status."""
    unity_project = Path("/Users/rashadwest/BTEBallCODE")
    
    status = {
        "exists": unity_project.exists(),
        "has_assets": (unity_project / "Assets").exists(),
        "has_scripts": (unity_project / "Assets/Scripts").exists(),
        "has_editor": (unity_project / "Assets/Editor").exists(),
        "uiux_helper_exists": (unity_project / "Assets/Editor/UIUXButtonSetupHelper.cs").exists(),
        "improved_button_exists": (unity_project / "Assets/Scripts/ImprovedButton.cs").exists()
    }
    
    return status

def check_unity_editor() -> Dict:
    """Check Unity Editor availability."""
    unity_path = Path("/Applications/Unity/Hub/Editor/2021.3.10f1/Unity.app/Contents/MacOS/Unity")
    
    return {
        "exists": unity_path.exists(),
        "path": str(unity_path) if unity_path.exists() else None
    }

def check_package_issue() -> Dict:
    """Check for Unity package dependency issues."""
    manifest_path = Path("/Users/rashadwest/BTEBallCODE/Packages/manifest.json")
    
    if not manifest_path.exists():
        return {
            "has_issue": True,
            "error": "manifest.json not found"
        }
    
    try:
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        
        dependencies = manifest.get("dependencies", {})
        universal_pipeline = dependencies.get("com.unity.render-pipelines.universal")
        
        return {
            "has_issue": universal_pipeline is not None,
            "package": universal_pipeline,
            "manifest": manifest
        }
    except Exception as e:
        return {
            "has_issue": True,
            "error": str(e)
        }

def create_next_steps_guide(project_status: Dict, editor_status: Dict, package_status: Dict) -> str:
    """Create comprehensive next steps guide."""
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    project_exists = '✅ Found' if project_status['exists'] else '❌ Not Found'
    assets_ok = '✅' if project_status['has_assets'] else '❌'
    scripts_ok = '✅' if project_status['has_scripts'] else '❌'
    editor_ok = '✅' if project_status['has_editor'] else '❌'
    helper_ok = '✅' if project_status['uiux_helper_exists'] else '❌'
    button_ok = '✅' if project_status['improved_button_exists'] else '❌'
    editor_available = '✅ Available' if editor_status['exists'] else '❌ Not Found'
    editor_path = editor_status.get('path', 'N/A')
    package_issue = '⚠️ Issue Detected' if package_status.get('has_issue') else '✅ OK'
    package_error = package_status.get('error', 'Package dependency may need resolution')
    package_needs_fix = '⚠️ Needs Manual Fix' if package_status.get('has_issue') else '✅ OK'
    
    guide = """# 🤖 Robot: Unity Automation Next Steps

**Generated:** """ + timestamp + """  
**Status:** Automation Ready - Package Fix Needed

---

## 📊 CURRENT STATUS

### Unity Project: """ + project_exists + """
- Location: `/Users/rashadwest/BTEBallCODE`
- Assets folder: """ + assets_ok + """
- Scripts folder: """ + scripts_ok + """
- Editor folder: """ + editor_ok + """
- UIUX Helper: """ + helper_ok + """
- ImprovedButton: """ + button_ok + """

### Unity Editor: """ + editor_available + """
- Path: """ + editor_path + """

### Package Status: """ + package_issue + """
- Issue: """ + package_error + """

---

## 🚀 NEXT STEPS (Automated & Manual)

### **Step 1: Fix Unity Package Dependency** ⏳

**Status:** """ + package_needs_fix + """

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Status:** Automation Ready - Package Fix Needed

---

## 📊 CURRENT STATUS

### Unity Project: {'✅ Found' if project_status['exists'] else '❌ Not Found'}
- Location: `/Users/rashadwest/BTEBallCODE`
- Assets folder: {'✅' if project_status['has_assets'] else '❌'}
- Scripts folder: {'✅' if project_status['has_scripts'] else '❌'}
- Editor folder: {'✅' if project_status['has_editor'] else '❌'}
- UIUX Helper: {'✅' if project_status['uiux_helper_exists'] else '❌'}
- ImprovedButton: {'✅' if project_status['improved_button_exists'] else '❌'}

### Unity Editor: {'✅ Available' if editor_status['exists'] else '❌ Not Found'}
- Path: {editor_status.get('path', 'N/A')}

### Package Status: {'⚠️ Issue Detected' if package_status.get('has_issue') else '✅ OK'}
- Issue: {package_status.get('error', 'Package dependency may need resolution')}

---

## 🚀 NEXT STEPS (Automated & Manual)

### **Step 1: Fix Unity Package Dependency** ⏳

**Status:** {'⚠️ Needs Manual Fix' if package_status.get('has_issue') else '✅ OK'}

**Automated Check:**
```bash
# Robot verified package issue exists
# Manual fix required in Unity Editor
```

**Manual Fix (5-10 minutes):**
1. Open Unity project:
   ```bash
   open /Users/rashadwest/BTEBallCODE
   ```
   Or open Unity Hub and select the project

2. Wait for Unity to resolve packages:
   - Unity will automatically detect missing packages
   - Package Manager will download required packages
   - Wait for "Resolving packages..." to complete

3. Verify packages resolved:
   - Check Console for errors
   - Should see "Packages resolved successfully"
   - No red errors about missing packages

**Alternative (If packages don't auto-resolve):**
1. Open Unity Editor
2. Window → Package Manager
3. Check for any package errors
4. Click "Resolve" or "Update" if needed

---

### **Step 2: Test Automation Script** ⏳

**Status:** Ready to test (after Step 1)

**Automated Command:**
```bash
# Set environment variable
export UNITY_PROJECT_PATH=/Users/rashadwest/BTEBallCODE

# Run automation
python3 scripts/garvis-apply-unity-components.py
```

**Expected Result:**
- ✅ Unity Editor opens in headless mode
- ✅ Components applied to buttons
- ✅ Scene files updated
- ✅ No errors in log

**If Errors:**
- Check `unity-apply-components.log` for details
- Verify Unity project opens without errors
- Ensure all scripts are in place

---

### **Step 3: Verify Components Applied** ⏳

**Status:** After Step 2

**Manual Verification:**
1. Open Unity project in Unity Editor
2. Check Hierarchy for button GameObjects
3. Select a button (e.g., "Coding")
4. Check Inspector for new components:
   - Should see `GameModeButton` component
   - Should see `ImprovedButton` component
   - Component properties should be configured

**Automated Check:**
```bash
# Check if scene files were modified
cd /Users/rashadwest/BTEBallCODE
git status Assets/
```

**Expected:**
- Modified `.unity` scene files
- New component references in scene files

---

### **Step 4: Commit and Push Changes** ⏳

**Status:** After Step 3

**Automated Commands:**
```bash
cd /Users/rashadwest/BTEBallCODE

# Check what changed
git status

# Add changes
git add Assets/

# Commit
git commit -m "Apply UI/UX improvements to buttons via automation"

# Push
git push origin main
```

**Expected:**
- Scene files committed
- Scripts already in repository (from previous push)
- Changes pushed to GitHub

---

### **Step 5: Trigger Unity Build** ⏳

**Status:** After Step 4

**Automated Command:**
```bash
# Trigger Unity Build Orchestrator
curl -X POST http://192.168.1.226:5678/webhook/unity-build \\
  -H "Content-Type: application/json" \\
  -d '{"request": "Build Unity game with UI/UX improvements", "branch": "main"}'
```

**Or via Garvis:**
```bash
python3 scripts/garvis-push.py --game
```

**Expected:**
- GitHub Actions triggered
- Unity build starts
- Build completes in 10-15 minutes
- Netlify deployment triggered automatically

---

## 📋 QUICK REFERENCE

### **All-in-One Command (After Package Fix):**
```bash
# 1. Fix packages (manual - open Unity Editor)
open /Users/rashadwest/BTEBallCODE

# 2. After packages resolved, run automation
export UNITY_PROJECT_PATH=/Users/rashadwest/BTEBallCODE
python3 scripts/garvis-apply-unity-components.py

# 3. Verify and commit
cd /Users/rashadwest/BTEBallCODE
git add Assets/ && git commit -m "Apply UI/UX improvements" && git push

# 4. Trigger build
python3 scripts/garvis-push.py --game
```

---

## 🎯 SUCCESS CRITERIA

### **Automation Working When:**
- ✅ Unity Editor opens project in batch mode without errors
- ✅ Script executes `UIUXButtonSetupHelper.ApplyUIUXImprovements`
- ✅ Components applied to buttons automatically
- ✅ Scene files updated
- ✅ Changes committed and pushed
- ✅ Unity build triggered
- ✅ Game deployed with UI/UX improvements

---

## 📝 NOTES

- **Package Fix:** Must be done manually in Unity Editor (GUI mode)
- **Automation:** Works automatically after package fix
- **Fallback:** Manual application available if automation fails
- **Long-term:** JSON-driven UI system planned for next week

---

**Generated by:** Robot Unity Automation Next Steps  
**Status:** Ready for execution after package fix
"""
    
    return guide

def generate_action_plan(project_status: Dict, editor_status: Dict, package_status: Dict) -> Dict:
    """Generate automated action plan."""
    
    actions = []
    
    # Check if everything is ready
    if not project_status['exists']:
        actions.append({
            "action": "Clone Unity project",
            "status": "pending",
            "command": "git clone https://github.com/rashadwest/BTEBallCODE.git /Users/rashadwest/BTEBallCODE",
            "automated": True
        })
    
    if not project_status['uiux_helper_exists']:
        actions.append({
            "action": "Copy UIUXButtonSetupHelper.cs",
            "status": "pending",
            "command": f"cp {PROJECT_ROOT}/Unity-Scripts/Editor/UIUXButtonSetupHelper.cs /Users/rashadwest/BTEBallCODE/Assets/Editor/",
            "automated": True
        })
    
    if package_status.get('has_issue'):
        actions.append({
            "action": "Fix Unity package dependencies",
            "status": "pending",
            "command": "open /Users/rashadwest/BTEBallCODE (then wait for Unity to resolve packages)",
            "automated": False,
            "manual": True,
            "time": "5-10 minutes"
        })
    
    actions.append({
        "action": "Test automation script",
        "status": "pending",
        "command": "python3 scripts/garvis-apply-unity-components.py",
        "automated": True,
        "depends_on": "Fix Unity package dependencies"
    })
    
    actions.append({
        "action": "Commit and push changes",
        "status": "pending",
        "command": "cd /Users/rashadwest/BTEBallCODE && git add Assets/ && git commit -m 'Apply UI/UX improvements' && git push",
        "automated": True,
        "depends_on": "Test automation script"
    })
    
    actions.append({
        "action": "Trigger Unity build",
        "status": "pending",
        "command": "python3 scripts/garvis-push.py --game",
        "automated": True,
        "depends_on": "Commit and push changes"
    })
    
    return {
        "actions": actions,
        "ready": all([
            project_status['exists'],
            project_status['uiux_helper_exists'],
            editor_status['exists']
        ]),
        "blocked": package_status.get('has_issue', False)
    }

def main():
    """Main robot function."""
    print_header("Robot: Push Unity Automation Next Steps")
    
    # Check current status
    print_info("Checking Unity project status...")
    project_status = check_unity_project()
    
    print_info("Checking Unity Editor...")
    editor_status = check_unity_editor()
    
    print_info("Checking package dependencies...")
    package_status = check_package_issue()
    
    # Generate guide
    print_info("Generating next steps guide...")
    guide = create_next_steps_guide(project_status, editor_status, package_status)
    
    # Save guide
    guide_file = DOCS_DIR / "ROBOT-UNITY-AUTOMATION-NEXT-STEPS.md"
    with open(guide_file, 'w', encoding='utf-8') as f:
        f.write(guide)
    
    print_success(f"Next steps guide saved: {guide_file}")
    
    # Generate action plan
    print_info("Generating action plan...")
    action_plan = generate_action_plan(project_status, editor_status, package_status)
    
    # Print summary
    print_header("Status Summary")
    
    print(f"Unity Project: {'✅' if project_status['exists'] else '❌'}")
    print(f"Unity Editor: {'✅' if editor_status['exists'] else '❌'}")
    print(f"UIUX Helper: {'✅' if project_status['uiux_helper_exists'] else '❌'}")
    print(f"Package Issue: {'⚠️' if package_status.get('has_issue') else '✅'}")
    
    print_header("Action Plan")
    
    for i, action in enumerate(action_plan['actions'], 1):
        status_emoji = "⏳" if action['status'] == 'pending' else "✅"
        auto_emoji = "🤖" if action.get('automated') else "👤"
        print(f"{status_emoji} {i}. {auto_emoji} {action['action']}")
        if action.get('depends_on'):
            print(f"   └─ Depends on: {action['depends_on']}")
        if action.get('manual'):
            print(f"   └─ Manual step: {action.get('time', 'N/A')}")
    
    if action_plan['blocked']:
        print_warning("\n⚠️  BLOCKED: Unity package dependency issue must be fixed first")
        print_info("   Open Unity project in Unity Editor to resolve packages")
        print_info("   Then run: python3 scripts/garvis-apply-unity-components.py")
    elif action_plan['ready']:
        print_success("\n✅ Ready to proceed with automation!")
        print_info("   Run: python3 scripts/garvis-apply-unity-components.py")
    else:
        print_warning("\n⚠️  Some setup steps needed before automation")
    
    print(f"\n📄 Full guide: {guide_file}")
    print("✅ Robot next steps complete!")

if __name__ == "__main__":
    main()

