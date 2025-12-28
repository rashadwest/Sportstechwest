#!/usr/bin/env python3
"""
Code Quality Audit Tool
Scans all Python scripts for bugs, incomplete code, and quality issues

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import ast
import re
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict

PROJECT_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"

class CodeQualityAuditor:
    """Audits Python code for quality issues"""
    
    def __init__(self):
        self.issues = defaultdict(list)
        self.scripts = []
    
    def find_python_scripts(self) -> List[Path]:
        """Find all Python scripts"""
        scripts = []
        if SCRIPTS_DIR.exists():
            scripts.extend(SCRIPTS_DIR.glob("*.py"))
        return scripts
    
    def check_bare_except(self, file_path: Path, content: str) -> List[Tuple[int, str]]:
        """Check for bare except clauses"""
        issues = []
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            # Check for bare except (not except Exception or specific exception)
            if re.search(r'^\s*except\s*:\s*$', line):
                issues.append((i, "Bare except clause - should specify exception type"))
        return issues
    
    def check_missing_docstrings(self, file_path: Path, content: str) -> List[Tuple[int, str]]:
        """Check for missing docstrings"""
        issues = []
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                    if not ast.get_docstring(node):
                        issues.append((node.lineno, f"Missing docstring for {node.name}"))
        except SyntaxError:
            # Skip files with syntax errors (will be caught elsewhere)
            pass
        return issues
    
    def check_todo_comments(self, file_path: Path, content: str) -> List[Tuple[int, str]]:
        """Check for TODO/FIXME comments"""
        issues = []
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            if re.search(r'#\s*(TODO|FIXME|XXX|HACK|BUG)', line, re.IGNORECASE):
                issues.append((i, f"TODO/FIXME found: {line.strip()}"))
        return issues
    
    def check_undefined_variables(self, file_path: Path, content: str) -> List[Tuple[int, str]]:
        """Check for potentially undefined variables"""
        issues = []
        lines = content.split('\n')
        
        # Common patterns that might indicate undefined variables
        for i, line in enumerate(lines, 1):
            # Check for variables used before assignment in conditional blocks
            if re.search(r'if\s+.*:\s*$', line):
                # Check next few lines for variable usage
                for j in range(i, min(i + 10, len(lines))):
                    next_line = lines[j]
                    # Look for variables that might not be defined
                    if re.search(r'\b(logged_count|result|data|response)\s*=', next_line):
                        # Check if it's used before being defined
                        if j > i + 1:
                            # Variable might be used before assignment
                            var_match = re.search(r'(\w+)\s*=', next_line)
                            if var_match:
                                var_name = var_match.group(1)
                                # Check if used before this assignment
                                for k in range(i, j):
                                    if var_name in lines[k] and '=' not in lines[k]:
                                        issues.append((k + 1, f"Variable '{var_name}' might be used before assignment"))
                                        break
        
        return issues
    
    def check_error_handling(self, file_path: Path, content: str) -> List[Tuple[int, str]]:
        """Check for poor error handling"""
        issues = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Check for print statements in except blocks (should use logging)
            if 'except' in line.lower() and i < len(lines):
                # Check next few lines for print statements
                for j in range(i, min(i + 5, len(lines))):
                    if 'print(' in lines[j] and 'error' in lines[j].lower():
                        # Should use proper logging
                        issues.append((j + 1, "Error handling uses print() - consider using logging module"))
        
        return issues
    
    def check_missing_type_hints(self, file_path: Path, content: str) -> List[Tuple[int, str]]:
        """Check for missing type hints in function signatures"""
        issues = []
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Check if function has type hints
                    if not node.returns and len(node.args.args) > 0:
                        # Check if any args have type hints
                        has_type_hints = any(arg.annotation for arg in node.args.args)
                        if not has_type_hints and node.name not in ['__init__', 'main']:
                            issues.append((node.lineno, f"Function '{node.name}' missing type hints"))
        except SyntaxError:
            pass
        return issues
    
    def audit_file(self, file_path: Path) -> Dict:
        """Audit a single file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return {"error": str(e)}
        
        file_issues = {
            "bare_except": self.check_bare_except(file_path, content),
            "missing_docstrings": self.check_missing_docstrings(file_path, content),
            "todo_comments": self.check_todo_comments(file_path, content),
            "undefined_variables": self.check_undefined_variables(file_path, content),
            "error_handling": self.check_error_handling(file_path, content),
            "missing_type_hints": self.check_missing_type_hints(file_path, content)
        }
        
        return file_issues
    
    def audit_all(self) -> Dict:
        """Audit all Python scripts"""
        scripts = self.find_python_scripts()
        results = {}
        
        for script in scripts:
            if script.name == "code-quality-audit.py":
                continue  # Skip self
            
            print(f"🔍 Auditing: {script.name}...")
            results[script.name] = self.audit_file(script)
        
        return results
    
    def print_report(self, results: Dict):
        """Print audit report"""
        print("\n" + "=" * 70)
        print("📊 Code Quality Audit Report")
        print("=" * 70)
        
        total_issues = 0
        critical_files = []
        
        for filename, issues in results.items():
            if "error" in issues:
                print(f"\n❌ {filename}: Error reading file - {issues['error']}")
                continue
            
            file_issues = sum(len(v) for v in issues.values())
            total_issues += file_issues
            
            if file_issues > 0:
                critical_files.append((filename, file_issues, issues))
        
        if total_issues == 0:
            print("\n✅ No issues found! All code is clean.")
            return
        
        print(f"\n⚠️  Found {total_issues} issues across {len(critical_files)} files\n")
        
        # Sort by issue count
        critical_files.sort(key=lambda x: x[1], reverse=True)
        
        for filename, count, issues in critical_files:
            print(f"\n📄 {filename} ({count} issues):")
            print("-" * 70)
            
            for issue_type, issue_list in issues.items():
                if issue_list:
                    print(f"\n  {issue_type.replace('_', ' ').title()}:")
                    for line_num, message in issue_list[:5]:  # Show first 5
                        print(f"    Line {line_num}: {message}")
                    if len(issue_list) > 5:
                        print(f"    ... and {len(issue_list) - 5} more")
        
        print("\n" + "=" * 70)
        print(f"📊 Summary: {total_issues} total issues found")
        print("=" * 70)


def main():
    """Main function"""
    auditor = CodeQualityAuditor()
    results = auditor.audit_all()
    auditor.print_report(results)


if __name__ == "__main__":
    main()


