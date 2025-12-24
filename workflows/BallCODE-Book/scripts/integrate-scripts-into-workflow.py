#!/usr/bin/env python3
"""
Integrate all Full Integration scripts into n8n workflow JSON.
This script adds Execute Command nodes after AI generation nodes.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
WORKFLOW_FILE = PROJECT_ROOT / "n8n-ballcode-full-integration-workflow.json"
OUTPUT_FILE = PROJECT_ROOT / "n8n-ballcode-full-integration-workflow-INTEGRATED.json"

def add_execute_nodes(workflow):
    """Add Execute Command nodes after AI generation nodes."""
    
    # Get workflow path from environment
    workflow_path = "$env.WORKFLOW_PATH || '/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book'"
    
    # Node positions (x, y) - increment x by 200 for each new node
    base_x = 1650
    next_y = 100
    
    # New nodes to add
    new_nodes = []
    new_connections = {}
    
    # 1. After "Generate Game Updates (AI)" - Execute Game Script
    execute_game = {
        "id": "execute-game-script",
        "name": "Execute: Apply Game Updates",
        "type": "n8n-nodes-base.executeCommand",
        "typeVersion": 1,
        "position": [base_x, next_y],
        "parameters": {
            "command": "python3",
            "arguments": f"{workflow_path}/scripts/full-integration-apply-game.py",
            "options": {}
        }
    }
    new_nodes.append(execute_game)
    
    # Parse Game Output
    parse_game = {
        "id": "parse-game-output",
        "name": "Parse Game Script Output",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [base_x + 200, next_y],
        "parameters": {
            "jsCode": """// Parse game script output
const output = $input.item.json.stdout || $input.item.json;
let result;
try {
  result = typeof output === 'string' ? JSON.parse(output) : output;
} catch (e) {
  result = { status: 'error', error: 'Failed to parse output', raw: output };
}
return { json: { ...$('Generate Game Updates (AI)').item.json, gameResult: result } };"""
        }
    }
    new_nodes.append(parse_game)
    next_y += 100
    
    # 2. After "Generate Curriculum Updates (AI)" - Execute Curriculum Script
    execute_curriculum = {
        "id": "execute-curriculum-script",
        "name": "Execute: Apply Curriculum Updates",
        "type": "n8n-nodes-base.executeCommand",
        "typeVersion": 1,
        "position": [base_x, next_y],
        "parameters": {
            "command": "python3",
            "arguments": f"{workflow_path}/scripts/full-integration-apply-curriculum.py",
            "options": {}
        }
    }
    new_nodes.append(execute_curriculum)
    
    parse_curriculum = {
        "id": "parse-curriculum-output",
        "name": "Parse Curriculum Script Output",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [base_x + 200, next_y],
        "parameters": {
            "jsCode": """// Parse curriculum script output
const output = $input.item.json.stdout || $input.item.json;
let result;
try {
  result = typeof output === 'string' ? JSON.parse(output) : output;
} catch (e) {
  result = { status: 'error', error: 'Failed to parse output', raw: output };
}
return { json: { ...$('Generate Curriculum Updates (AI)').item.json, curriculumResult: result } };"""
        }
    }
    new_nodes.append(parse_curriculum)
    next_y += 100
    
    # 3. After "Generate Book Updates (AI)" - Execute Book Script
    execute_book = {
        "id": "execute-book-script",
        "name": "Execute: Apply Book Updates",
        "type": "n8n-nodes-base.executeCommand",
        "typeVersion": 1,
        "position": [base_x, next_y],
        "parameters": {
            "command": "python3",
            "arguments": f"{workflow_path}/scripts/full-integration-apply-book.py",
            "options": {}
        }
    }
    new_nodes.append(execute_book)
    
    parse_book = {
        "id": "parse-book-output",
        "name": "Parse Book Script Output",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [base_x + 200, next_y],
        "parameters": {
            "jsCode": """// Parse book script output
const output = $input.item.json.stdout || $input.item.json;
let result;
try {
  result = typeof output === 'string' ? JSON.parse(output) : output;
} catch (e) {
  result = { status: 'error', error: 'Failed to parse output', raw: output };
}
return { json: { ...$('Generate Book Updates (AI)').item.json, bookResult: result } };"""
        }
    }
    new_nodes.append(parse_book)
    next_y += 100
    
    # 4. After "Generate Website Updates (AI)" - Execute Website Script
    execute_website = {
        "id": "execute-website-script",
        "name": "Execute: Apply Website Updates",
        "type": "n8n-nodes-base.executeCommand",
        "typeVersion": 1,
        "position": [base_x, next_y],
        "parameters": {
            "command": "python3",
            "arguments": f"{workflow_path}/scripts/full-integration-apply-website.py",
            "options": {}
        }
    }
    new_nodes.append(execute_website)
    
    parse_website = {
        "id": "parse-website-output",
        "name": "Parse Website Script Output",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [base_x + 200, next_y],
        "parameters": {
            "jsCode": """// Parse website script output
const output = $input.item.json.stdout || $input.item.json;
let result;
try {
  result = typeof output === 'string' ? JSON.parse(output) : output;
} catch (e) {
  result = { status: 'error', error: 'Failed to parse output', raw: output };
}
return { json: { ...$('Generate Website Updates (AI)').item.json, websiteResult: result } };"""
        }
    }
    new_nodes.append(parse_website)
    
    # Update connections
    # Game: Generate -> Execute -> Parse -> Merge
    new_connections["Generate Game Updates (AI)"] = {
        "main": [[
            {"node": "Execute: Apply Game Updates", "type": "main", "index": 0}
        ]]
    }
    new_connections["Execute: Apply Game Updates"] = {
        "main": [[
            {"node": "Parse Game Script Output", "type": "main", "index": 0}
        ]]
    }
    new_connections["Parse Game Script Output"] = {
        "main": [[
            {"node": "Merge All System Updates", "type": "main", "index": 0}
        ]]
    }
    
    # Curriculum: Generate -> Execute -> Parse -> Merge
    new_connections["Generate Curriculum Updates (AI)"] = {
        "main": [[
            {"node": "Execute: Apply Curriculum Updates", "type": "main", "index": 0}
        ]]
    }
    new_connections["Execute: Apply Curriculum Updates"] = {
        "main": [[
            {"node": "Parse Curriculum Script Output", "type": "main", "index": 0}
        ]]
    }
    new_connections["Parse Curriculum Script Output"] = {
        "main": [[
            {"node": "Merge All System Updates", "type": "main", "index": 0}
        ]]
    }
    
    # Book: Generate -> Execute -> Parse -> Merge
    new_connections["Generate Book Updates (AI)"] = {
        "main": [[
            {"node": "Execute: Apply Book Updates", "type": "main", "index": 0}
        ]]
    }
    new_connections["Execute: Apply Book Updates"] = {
        "main": [[
            {"node": "Parse Book Script Output", "type": "main", "index": 0}
        ]]
    }
    new_connections["Parse Book Script Output"] = {
        "main": [[
            {"node": "Merge All System Updates", "type": "main", "index": 0}
        ]]
    }
    
    # Website: Generate -> Execute -> Parse -> Merge
    new_connections["Generate Website Updates (AI)"] = {
        "main": [[
            {"node": "Execute: Apply Website Updates", "type": "main", "index": 0}
        ]]
    }
    new_connections["Execute: Apply Website Updates"] = {
        "main": [[
            {"node": "Parse Website Script Output", "type": "main", "index": 0}
        ]]
    }
    new_connections["Parse Website Script Output"] = {
        "main": [[
            {"node": "Merge All System Updates", "type": "main", "index": 0}
        ]]
    }
    
    return new_nodes, new_connections

def integrate_workflow():
    """Integrate scripts into workflow."""
    # Load existing workflow
    with open(WORKFLOW_FILE, 'r', encoding='utf-8') as f:
        workflow = json.load(f)
    
    # Add new nodes
    new_nodes, new_connections = add_execute_nodes(workflow)
    workflow["nodes"].extend(new_nodes)
    
    # Update connections
    for node_name, connection in new_connections.items():
        if node_name in workflow["connections"]:
            # Merge connections
            if "main" in workflow["connections"][node_name]:
                workflow["connections"][node_name]["main"][0].extend(connection["main"][0])
            else:
                workflow["connections"][node_name] = connection
        else:
            workflow["connections"][node_name] = connection
    
    # Update workflow name
    workflow["name"] = "BallCODE Full Integration - AI Development Workflow (INTEGRATED)"
    
    # Save updated workflow
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(workflow, f, indent=2)
    
    print(f"✅ Integrated workflow saved to: {OUTPUT_FILE}")
    print(f"📊 Added {len(new_nodes)} new nodes")
    print(f"🔗 Updated {len(new_connections)} connections")
    
    return OUTPUT_FILE

if __name__ == "__main__":
    try:
        output_file = integrate_workflow()
        print(f"\n✅ Integration complete!")
        print(f"📁 Output file: {output_file}")
        print(f"\n📋 Next steps:")
        print(f"1. Review the integrated workflow JSON")
        print(f"2. Import to n8n via UI or API")
        print(f"3. Test end-to-end execution")
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)

