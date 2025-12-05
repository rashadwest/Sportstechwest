#!/usr/bin/env python3
"""
Unity Project Assessment Script
Purpose: Analyze Unity project structure and generate assessment report
Usage: python assess-unity-project.py <unity-project-path>
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, List, Set

# Colors for terminal output
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    NC = '\033[0m'  # No Color

def find_csharp_files(directory: Path) -> List[Path]:
    """Find all C# files in directory."""
    csharp_files = []
    for root, dirs, files in os.walk(directory):
        # Skip common Unity folders that don't contain user scripts
        dirs[:] = [d for d in dirs if d not in ['Library', 'Temp', 'obj', 'Logs']]
        for file in files:
            if file.endswith('.cs'):
                csharp_files.append(Path(root) / file)
    return csharp_files

def find_scenes(directory: Path) -> List[Path]:
    """Find all Unity scene files."""
    scenes = []
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in ['Library', 'Temp', 'obj', 'Logs']]
        for file in files:
            if file.endswith('.unity'):
                scenes.append(Path(root) / file)
    return scenes

def analyze_script(script_path: Path) -> Dict:
    """Analyze a C# script to extract class names and patterns."""
    analysis = {
        'path': str(script_path),
        'classes': [],
        'managers': [],
        'interfaces': [],
        'has_monobehaviour': False,
        'has_serialize_field': False
    }
    
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Find class definitions
            import re
            class_pattern = r'class\s+(\w+)'
            classes = re.findall(class_pattern, content)
            analysis['classes'] = classes
            
            # Check for manager patterns
            manager_pattern = r'class\s+(\w*Manager\w*)'
            managers = re.findall(manager_pattern, content)
            analysis['managers'] = managers
            
            # Check for interfaces
            interface_pattern = r'interface\s+(\w+)'
            interfaces = re.findall(interface_pattern, content)
            analysis['interfaces'] = interfaces
            
            # Check for MonoBehaviour
            if 'MonoBehaviour' in content:
                analysis['has_monobehaviour'] = True
            
            # Check for SerializeField
            if '[SerializeField]' in content or 'SerializeField' in content:
                analysis['has_serialize_field'] = True
                
    except Exception as e:
        analysis['error'] = str(e)
    
    return analysis

def assess_unity_project(project_path: Path) -> Dict:
    """Assess Unity project structure."""
    assessment = {
        'project_path': str(project_path),
        'unity_version': None,
        'scripts': [],
        'scenes': [],
        'game_mode_managers': [],
        'story_mode_scripts': [],
        'assets_structure': {},
        'recommendations': []
    }
    
    # Check for ProjectVersion.txt (Unity version)
    version_file = project_path / 'ProjectSettings' / 'ProjectVersion.txt'
    if version_file.exists():
        try:
            with open(version_file, 'r') as f:
                for line in f:
                    if 'm_EditorVersion:' in line:
                        assessment['unity_version'] = line.split(':')[1].strip()
                        break
        except:
            pass
    
    # Find all C# scripts
    scripts_dir = project_path / 'Assets' / 'Scripts'
    if scripts_dir.exists():
        scripts = find_csharp_files(scripts_dir)
        assessment['scripts'] = [str(s.relative_to(project_path)) for s in scripts]
        
        # Analyze scripts
        for script_path in scripts:
            analysis = analyze_script(script_path)
            
            # Check for game mode managers
            if any('Manager' in cls for cls in analysis['classes']):
                if 'StoryMode' not in str(script_path):
                    assessment['game_mode_managers'].append({
                        'file': str(script_path.relative_to(project_path)),
                        'classes': analysis['classes'],
                        'managers': analysis['managers']
                    })
            
            # Check for Story Mode scripts
            if 'StoryMode' in str(script_path):
                assessment['story_mode_scripts'].append({
                    'file': str(script_path.relative_to(project_path)),
                    'classes': analysis['classes']
                })
    
    # Find scenes
    scenes_dir = project_path / 'Assets' / 'Scenes'
    if scenes_dir.exists():
        scenes = find_scenes(scenes_dir)
        assessment['scenes'] = [str(s.relative_to(project_path)) for s in scenes]
    
    # Check Assets structure
    assets_dir = project_path / 'Assets'
    if assets_dir.exists():
        for item in assets_dir.iterdir():
            if item.is_dir() and item.name not in ['Scripts', 'Scenes', 'Resources']:
                assessment['assets_structure'][item.name] = [
                    str(p.relative_to(project_path)) 
                    for p in item.rglob('*') 
                    if p.is_file()
                ][:10]  # Limit to 10 files per directory
    
    # Generate recommendations
    if not assessment['story_mode_scripts']:
        assessment['recommendations'].append(
            "Story Mode scripts not found. Run automate-unity-setup.sh to copy scripts."
        )
    
    if not assessment['game_mode_managers']:
        assessment['recommendations'].append(
            "No game mode managers found. Check if managers exist with different naming."
        )
    
    if not assessment['scenes']:
        assessment['recommendations'].append(
            "No scenes found in Assets/Scenes. Check scene location."
        )
    
    return assessment

def print_report(assessment: Dict):
    """Print formatted assessment report."""
    print(f"\n{Colors.BLUE}{'='*60}{Colors.NC}")
    print(f"{Colors.BLUE}Unity Project Assessment Report{Colors.NC}")
    print(f"{Colors.BLUE}{'='*60}{Colors.NC}\n")
    
    print(f"{Colors.GREEN}Project Path:{Colors.NC} {assessment['project_path']}")
    
    if assessment['unity_version']:
        print(f"{Colors.GREEN}Unity Version:{Colors.NC} {assessment['unity_version']}")
    else:
        print(f"{Colors.YELLOW}Unity Version:{Colors.NC} Not detected")
    
    print(f"\n{Colors.BLUE}Scripts Found:{Colors.NC} {len(assessment['scripts'])}")
    if assessment['scripts']:
        print("  Sample scripts:")
        for script in assessment['scripts'][:5]:
            print(f"    - {script}")
        if len(assessment['scripts']) > 5:
            print(f"    ... and {len(assessment['scripts']) - 5} more")
    
    print(f"\n{Colors.BLUE}Scenes Found:{Colors.NC} {len(assessment['scenes'])}")
    for scene in assessment['scenes']:
        print(f"    - {scene}")
    
    print(f"\n{Colors.BLUE}Game Mode Managers:{Colors.NC} {len(assessment['game_mode_managers'])}")
    for manager in assessment['game_mode_managers']:
        print(f"    - {manager['file']}")
        print(f"      Classes: {', '.join(manager['classes'])}")
    
    print(f"\n{Colors.BLUE}Story Mode Scripts:{Colors.NC} {len(assessment['story_mode_scripts'])}")
    if assessment['story_mode_scripts']:
        for script in assessment['story_mode_scripts']:
            print(f"    {Colors.GREEN}✓{Colors.NC} {script['file']}")
    else:
        print(f"    {Colors.YELLOW}⚠{Colors.NC} No Story Mode scripts found")
    
    print(f"\n{Colors.BLUE}Assets Structure:{Colors.NC}")
    for folder, files in assessment['assets_structure'].items():
        print(f"    {folder}/ ({len(files)} files shown)")
    
    if assessment['recommendations']:
        print(f"\n{Colors.YELLOW}Recommendations:{Colors.NC}")
        for i, rec in enumerate(assessment['recommendations'], 1):
            print(f"    {i}. {rec}")
    
    print(f"\n{Colors.BLUE}{'='*60}{Colors.NC}\n")

def main():
    if len(sys.argv) < 2:
        print(f"{Colors.RED}Error: Unity project path not provided{Colors.NC}")
        print("Usage: python assess-unity-project.py <unity-project-path>")
        print("Example: python assess-unity-project.py ~/Projects/BTEBallCODE")
        sys.exit(1)
    
    project_path = Path(sys.argv[1])
    
    if not project_path.exists():
        print(f"{Colors.RED}Error: Project path does not exist: {project_path}{Colors.NC}")
        sys.exit(1)
    
    if not (project_path / 'Assets').exists():
        print(f"{Colors.RED}Error: Not a valid Unity project (Assets folder not found){Colors.NC}")
        sys.exit(1)
    
    print(f"{Colors.GREEN}Assessing Unity project...{Colors.NC}")
    assessment = assess_unity_project(project_path)
    
    print_report(assessment)
    
    # Save JSON report
    report_file = project_path / 'unity-project-assessment.json'
    with open(report_file, 'w') as f:
        json.dump(assessment, f, indent=2)
    
    print(f"{Colors.GREEN}JSON report saved to: {report_file}{Colors.NC}")

if __name__ == '__main__':
    main()


