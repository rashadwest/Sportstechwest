#!/usr/bin/env python3
"""Create human-readable report from blind analysis results"""

import json
from pathlib import Path

# Load analysis results
with open('ballcode_blind_analysis.json', 'r') as f:
    results = json.load(f)

# Create report
report = []
report.append("# BallCODE Screenshots - Blind Analysis Report")
report.append("")
report.append("**Copyright © 2025 Rashad West. All Rights Reserved.**")
report.append("")
report.append("**Analysis Method:** AIMCODE Blind Image Analysis (no vision APIs, no human assistance)")
report.append("**Total Images Analyzed:** " + str(len(results)))
report.append("")
report.append("---")
report.append("")

# Summary statistics
total_text = 0
total_ui_elements = 0
layout_types = {}
visual_themes = {}
game_states = {}

for result in results:
    if "layers" in result:
        layers = result["layers"]
        
        # Text extraction
        if "text" in layers and "word_count" in layers["text"]:
            total_text += layers["text"]["word_count"]
        
        # UI elements
        if "patterns" in layers and "ui_elements_detected" in layers["patterns"]:
            total_ui_elements += layers["patterns"]["ui_elements_detected"]
        
        # Layout types
        if "patterns" in layers and "layout_type" in layers["patterns"]:
            layout = layers["patterns"]["layout_type"]
            layout_types[layout] = layout_types.get(layout, 0) + 1
        
        # Visual themes
        if "understanding" in layers and "visual_theme" in layers["understanding"]:
            theme = layers["understanding"]["visual_theme"]
            visual_themes[theme] = visual_themes.get(theme, 0) + 1
        
        # Game states
        if "understanding" in layers and "game_state" in layers["understanding"]:
            state = layers["understanding"]["game_state"]
            game_states[state] = game_states.get(state, 0) + 1

report.append("## 📊 Summary Statistics")
report.append("")
report.append(f"- **Total Text Words Extracted:** {total_text}")
report.append(f"- **Total UI Elements Detected:** {total_ui_elements}")
report.append(f"- **Average UI Elements per Image:** {total_ui_elements / len(results):.1f}")
report.append("")
report.append("### Layout Types Found:")
for layout, count in sorted(layout_types.items(), key=lambda x: x[1], reverse=True):
    report.append(f"- **{layout}:** {count} images")
report.append("")
report.append("### Visual Themes:")
for theme, count in sorted(visual_themes.items(), key=lambda x: x[1], reverse=True):
    report.append(f"- **{theme}:** {count} images")
report.append("")
report.append("### Game States Detected:")
for state, count in sorted(game_states.items(), key=lambda x: x[1], reverse=True):
    report.append(f"- **{state}:** {count} images")
report.append("")
report.append("---")
report.append("")

# Detailed analysis for each image
report.append("## 🔍 Detailed Image Analysis")
report.append("")

for i, result in enumerate(results, 1):
    if "error" in result:
        continue
    
    filename = result.get("filename", "unknown")
    report.append(f"### Image {i}: {filename}")
    report.append("")
    
    if "layers" in result:
        layers = result["layers"]
        
        # Basic info
        if "basic" in layers:
            basic = layers["basic"]
            report.append(f"**Dimensions:** {basic.get('dimensions', {}).get('width', '?')}x{basic.get('dimensions', {}).get('height', '?')}")
            report.append(f"**File Size:** {basic.get('file_size_mb', '?')}MB")
            report.append("")
        
        # Text content
        if "text" in layers:
            text_layer = layers["text"]
            if "full_text" in text_layer and text_layer["full_text"]:
                report.append(f"**Text Found:** {text_layer['full_text'][:200]}...")
                report.append(f"**Word Count:** {text_layer.get('word_count', 0)}")
            elif "text_blocks" in text_layer and text_layer["text_blocks"]:
                texts = [t["text"] for t in text_layer["text_blocks"][:5]]
                report.append(f"**Text Blocks:** {', '.join(texts)}")
            else:
                report.append("**Text:** No text detected (OCR not available)")
            report.append("")
        
        # Structure
        if "structure" in layers:
            struct = layers["structure"]
            report.append(f"**Structure:** {struct.get('significant_regions', 0)} significant regions detected")
            report.append(f"**Edge Density:** {struct.get('edge_density', 0):.4f}")
            report.append("")
        
        # Colors
        if "colors" in layers:
            colors = layers["colors"]
            if "dominant_colors" in colors:
                dom_colors = colors["dominant_colors"]
                color_str = ", ".join([f"RGB{tuple(c['rgb'])} ({c['percentage']}%)" for c in dom_colors])
                report.append(f"**Dominant Colors:** {color_str}")
            report.append(f"**Brightness:** {colors.get('brightness', '?')} ({colors.get('visual_theme', 'unknown')} theme)")
            report.append("")
        
        # Patterns
        if "patterns" in layers:
            patterns = layers["patterns"]
            report.append(f"**Layout Type:** {patterns.get('layout_type', 'unknown')}")
            report.append(f"**UI Elements Detected:** {patterns.get('ui_elements_detected', 0)}")
            if "ui_element_positions" in patterns and patterns["ui_element_positions"]:
                report.append(f"**UI Element Positions:** {len(patterns['ui_element_positions'])} elements with coordinates")
            report.append("")
        
        # Understanding
        if "understanding" in layers:
            understanding = layers["understanding"]
            if "description" in understanding:
                report.append(f"**Analysis:** {understanding['description']}")
            report.append(f"**Inferred State:** {understanding.get('game_state', 'unknown')}")
            report.append("")
    
    report.append("---")
    report.append("")

# Write report
with open('BALLCODE-BLIND-ANALYSIS-REPORT.md', 'w') as f:
    f.write('\n'.join(report))

print("✅ Report created: BALLCODE-BLIND-ANALYSIS-REPORT.md")


