#!/usr/bin/env python3
"""
Cursor Extension Audit - Phase 0.1.3
Analyze extension impact on performance and identify resource-heavy extensions

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
import subprocess
from pathlib import Path
from datetime import datetime
import os

# Cursor extension locations
CURSOR_EXTENSION_PATHS = {
    'macos': Path.home() / 'Library/Application Support/Cursor/User/extensions',
    'linux': Path.home() / '.config/Cursor/User/extensions',
    'windows': Path(os.environ.get('APPDATA', '')) / 'Cursor/User/extensions'
}

def detect_platform():
    """Detect the current platform."""
    if sys.platform == 'darwin':
        return 'macos'
    elif sys.platform.startswith('linux'):
        return 'linux'
    elif sys.platform == 'win32':
        return 'windows'
    return 'unknown'

def get_extension_path():
    """Get the Cursor extensions path for current platform."""
    platform = detect_platform()
    if platform == 'unknown':
        print("❌ Unknown platform. Please specify path manually.")
        return None
    return CURSOR_EXTENSION_PATHS[platform]

def list_installed_extensions(extension_path):
    """List all installed Cursor extensions."""
    if not extension_path or not extension_path.exists():
        print(f"❌ Extensions directory not found: {extension_path}")
        return []
    
    extensions = []
    
    # Cursor stores extensions in versioned directories
    # Format: publisher.extension-name-version
    for item in extension_path.iterdir():
        if item.is_dir():
            # Parse extension name from directory name
            # Example: "ms-python.python-2024.1.1"
            parts = item.name.rsplit('-', 1)
            if len(parts) == 2:
                extension_id = parts[0]
                version = parts[1]
                
                # Try to read package.json for extension info
                package_json = item / 'package.json'
                extension_info = {
                    'id': extension_id,
                    'version': version,
                    'path': str(item),
                    'name': extension_id,
                    'publisher': '',
                    'displayName': extension_id,
                    'description': '',
                    'enabled': True,  # Assume enabled if installed
                    'size': get_directory_size(item)
                }
                
                if package_json.exists():
                    try:
                        with open(package_json, 'r', encoding='utf-8') as f:
                            pkg_data = json.load(f)
                            extension_info.update({
                                'name': pkg_data.get('name', extension_id),
                                'publisher': pkg_data.get('publisher', ''),
                                'displayName': pkg_data.get('displayName', extension_id),
                                'description': pkg_data.get('description', ''),
                                'version': pkg_data.get('version', version),
                            })
                    except Exception as e:
                        print(f"⚠️  Could not read package.json for {extension_id}: {e}")
                
                extensions.append(extension_info)
    
    return extensions

def get_directory_size(path):
    """Calculate total size of directory in bytes."""
    total = 0
    try:
        for entry in path.rglob('*'):
            if entry.is_file():
                try:
                    total += entry.stat().st_size
                except (OSError, PermissionError):
                    pass
    except (OSError, PermissionError):
        pass
    return total

def check_cursor_processes():
    """Check Cursor processes and their resource usage."""
    try:
        # Use psutil if available, otherwise use basic ps
        import psutil
        
        cursor_processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'memory_percent']):
            try:
                if 'cursor' in proc.info['name'].lower():
                    cursor_processes.append({
                        'pid': proc.info['pid'],
                        'name': proc.info['name'],
                        'cpu_percent': proc.info['cpu_percent'],
                        'memory_mb': proc.info['memory_info'].rss / 1024 / 1024,
                        'memory_percent': proc.info['memory_percent']
                    })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        return cursor_processes
    except ImportError:
        print("⚠️  psutil not available. Install with: pip install psutil")
        return []

def identify_resource_heavy_extensions(extensions):
    """Identify potentially resource-heavy extensions."""
    # Known resource-intensive extension patterns
    resource_heavy_patterns = [
        'language-server',
        'lsp',
        'debugger',
        'test',
        'lint',
        'format',
        'git',
        'docker',
        'kubernetes',
        'typescript',
        'python',
        'java',
        'go',
        'rust'
    ]
    
    # Extensions that are typically heavy
    known_heavy = [
        'ms-python.python',
        'ms-vscode.vscode-typescript-next',
        'golang.go',
        'rust-lang.rust-analyzer',
        'redhat.java',
        'ms-vscode.cpptools'
    ]
    
    heavy_extensions = []
    
    for ext in extensions:
        score = 0
        reasons = []
        
        # Check size (extensions >50MB are potentially heavy)
        if ext['size'] > 50 * 1024 * 1024:
            score += 2
            reasons.append(f"Large size ({ext['size'] / 1024 / 1024:.1f} MB)")
        
        # Check for resource-heavy patterns
        ext_id_lower = ext['id'].lower()
        for pattern in resource_heavy_patterns:
            if pattern in ext_id_lower:
                score += 1
                reasons.append(f"Contains '{pattern}' pattern")
        
        # Check if known heavy extension
        if any(known in ext['id'] for known in known_heavy):
            score += 2
            reasons.append("Known resource-intensive extension")
        
        if score > 0:
            ext['resource_score'] = score
            ext['resource_reasons'] = reasons
            heavy_extensions.append(ext)
    
    # Sort by resource score
    heavy_extensions.sort(key=lambda x: x.get('resource_score', 0), reverse=True)
    
    return heavy_extensions

def generate_recommendations(extensions, heavy_extensions):
    """Generate recommendations for extension management."""
    recommendations = {
        'disable': [],
        'update': [],
        'keep': [],
        'monitor': []
    }
    
    # Recommend disabling very heavy extensions if not essential
    for ext in heavy_extensions[:5]:  # Top 5 heaviest
        if ext.get('resource_score', 0) >= 3:
            recommendations['disable'].append({
                'id': ext['id'],
                'name': ext.get('displayName', ext['id']),
                'reason': '; '.join(ext.get('resource_reasons', [])),
                'size_mb': ext['size'] / 1024 / 1024
            })
    
    # Recommend updating all extensions
    recommendations['update'] = [
        {
            'id': ext['id'],
            'name': ext.get('displayName', ext['id']),
            'current_version': ext.get('version', 'unknown')
        }
        for ext in extensions
    ]
    
    # Keep essential/lightweight extensions
    recommendations['keep'] = [
        {
            'id': ext['id'],
            'name': ext.get('displayName', ext['id']),
            'reason': 'Lightweight or essential'
        }
        for ext in extensions
        if ext not in heavy_extensions or ext.get('resource_score', 0) < 2
    ]
    
    # Monitor medium-weight extensions
    recommendations['monitor'] = [
        {
            'id': ext['id'],
            'name': ext.get('displayName', ext['id']),
            'size_mb': ext['size'] / 1024 / 1024,
            'resource_score': ext.get('resource_score', 0)
        }
        for ext in heavy_extensions
        if 1 <= ext.get('resource_score', 0) < 3
    ]
    
    return recommendations

def save_audit_report(extensions, heavy_extensions, recommendations, output_path):
    """Save audit report to JSON file."""
    report = {
        'timestamp': datetime.now().isoformat(),
        'total_extensions': len(extensions),
        'heavy_extensions_count': len(heavy_extensions),
        'extensions': extensions,
        'heavy_extensions': heavy_extensions,
        'recommendations': recommendations,
        'summary': {
            'total_size_mb': sum(ext['size'] for ext in extensions) / 1024 / 1024,
            'heavy_extensions_size_mb': sum(ext['size'] for ext in heavy_extensions) / 1024 / 1024,
            'average_size_mb': (sum(ext['size'] for ext in extensions) / len(extensions) / 1024 / 1024) if extensions else 0
        }
    }
    
    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    return report

def main():
    """Main execution."""
    print("=" * 60)
    print("Cursor Extension Audit - Phase 0.1.3")
    print("Identify resource-heavy extensions affecting performance")
    print("=" * 60)
    print()
    
    extension_path = get_extension_path()
    
    if not extension_path:
        print("❌ Could not locate Cursor extensions directory.")
        return 1
    
    print(f"📍 Scanning extensions at: {extension_path}")
    print()
    
    # List installed extensions
    print("🔍 Discovering installed extensions...")
    extensions = list_installed_extensions(extension_path)
    
    if not extensions:
        print("⚠️  No extensions found or could not read extension directory.")
        return 1
    
    print(f"✅ Found {len(extensions)} installed extensions")
    print()
    
    # Identify resource-heavy extensions
    print("📊 Analyzing extension resource usage...")
    heavy_extensions = identify_resource_heavy_extensions(extensions)
    
    print(f"⚠️  Found {len(heavy_extensions)} potentially resource-heavy extensions")
    print()
    
    # Generate recommendations
    print("💡 Generating recommendations...")
    recommendations = generate_recommendations(extensions, heavy_extensions)
    
    # Save report
    output_path = Path('data/extension_audit.json')
    print(f"💾 Saving audit report to: {output_path}")
    report = save_audit_report(extensions, heavy_extensions, recommendations, output_path)
    
    # Display summary
    print()
    print("=" * 60)
    print("EXTENSION AUDIT SUMMARY")
    print("=" * 60)
    print(f"Total Extensions: {len(extensions)}")
    print(f"Total Size: {report['summary']['total_size_mb']:.1f} MB")
    print(f"Heavy Extensions: {len(heavy_extensions)} ({report['summary']['heavy_extensions_size_mb']:.1f} MB)")
    print(f"Average Size: {report['summary']['average_size_mb']:.1f} MB")
    print()
    
    if recommendations['disable']:
        print("🚫 RECOMMEND DISABLING (if not essential):")
        for ext in recommendations['disable']:
            print(f"   - {ext['name']} ({ext['size_mb']:.1f} MB)")
            print(f"     Reason: {ext['reason']}")
        print()
    
    if recommendations['monitor']:
        print("👀 MONITOR (may impact performance):")
        for ext in recommendations['monitor'][:5]:  # Top 5
            print(f"   - {ext['name']} (Score: {ext['resource_score']}, {ext['size_mb']:.1f} MB)")
        print()
    
    print("✅ All extensions should be updated to latest versions")
    print()
    print("📝 Next steps:")
    print("   1. Review recommendations in data/extension_audit.json")
    print("   2. Disable non-essential heavy extensions in Cursor")
    print("   3. Update all extensions to latest versions")
    print("   4. Restart Cursor and test performance")
    print("   5. Continue to Phase 0.2 (Performance Monitoring)")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())

