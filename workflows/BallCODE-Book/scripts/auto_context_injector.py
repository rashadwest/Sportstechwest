#!/usr/bin/env python3
"""
Auto Context Injector - Phase 1.1
Automatically injects shared context into new chat sessions without manual commands.

This script monitors for new chat sessions and automatically injects context.
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

# Import the update script functions
sys.path.insert(0, str(Path(__file__).parent))
from update_shared_context import load_shared_context, get_cross_chat_summary, start_session

PROJECT_ROOT = Path(__file__).parent.parent
CONTEXT_FILE = PROJECT_ROOT / ".shared_chat_context.json"


def generate_context_banner() -> str:
    """Generate a context banner to auto-inject at chat start."""
    context = load_shared_context()
    summary = get_cross_chat_summary()
    
    banner = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔒 PRIVATE MODE - AUTO-CONTEXT INJECTED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{summary}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 This context was automatically loaded. No manual commands needed!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    return banner


def auto_inject_context():
    """Auto-inject context and start session."""
    # Start new session
    session_id = start_session()
    
    # Generate and display context banner
    banner = generate_context_banner()
    print(banner)
    
    # Update metrics
    context = load_shared_context()
    if "performance_metrics" not in context:
        context["performance_metrics"] = {}
    context["performance_metrics"]["auto_updates_count"] = context["performance_metrics"].get("auto_updates_count", 0) + 1
    
    from update_shared_context import save_shared_context
    save_shared_context(context)
    
    return session_id, banner


def get_context_for_ai() -> str:
    """Get formatted context for AI assistant to read."""
    context = load_shared_context()
    today = datetime.now().strftime("%Y-%m-%d")
    
    ai_context = "## Shared Context (Auto-Loaded)\n\n"
    
    # Daily progress
    if context["daily_progress"]["date"] == today:
        progress = context["daily_progress"]
        ai_context += f"### Today's ONE Thing\n"
        ai_context += f"- Task: {progress['one_thing'].get('task', 'Not set')}\n"
        ai_context += f"- Status: {progress['one_thing'].get('status', 'NOT_STARTED')}\n\n"
        
        ai_context += f"### Progress Summary\n"
        ai_context += f"- Completed Tasks: {len(progress['completed_tasks'])}\n"
        ai_context += f"- In Progress: {len(progress['in_progress_tasks'])}\n"
        ai_context += f"- Blockers: {len(progress['blockers'])}\n"
        ai_context += f"- Learnings: {len(progress['learnings'])}\n\n"
    
    # Recent completions
    if context.get("cross_chat_knowledge", {}).get("recent_completions"):
        ai_context += "### Recent Completions\n"
        for completion in context["cross_chat_knowledge"]["recent_completions"][-5:]:
            ai_context += f"- {completion.get('task', 'Unknown')}\n"
        ai_context += "\n"
    
    # Recent decisions
    if context.get("cross_chat_knowledge", {}).get("recent_decisions"):
        ai_context += "### Recent Decisions\n"
        for decision in context["cross_chat_knowledge"]["recent_decisions"][-5:]:
            ai_context += f"- {decision.get('decision', 'Unknown')}\n"
        ai_context += "\n"
    
    return ai_context


if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "inject":
            session_id, banner = auto_inject_context()
            print(f"\n✅ Session started: {session_id}")
        
        elif command == "banner":
            print(generate_context_banner())
        
        elif command == "ai-context":
            print(get_context_for_ai())
        
        else:
            print("Usage:")
            print("  python auto_context_injector.py inject  - Auto-inject context and start session")
            print("  python auto_context_injector.py banner  - Generate context banner")
            print("  python auto_context_injector.py ai-context - Get context formatted for AI")
    else:
        # Default: auto-inject
        session_id, banner = auto_inject_context()




