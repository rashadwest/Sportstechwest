#!/usr/bin/env python3
"""
Update Shared Context - Cross-Chat Knowledge System

This script updates the shared context file that all private mode chats can read.
Run this at the start and end of each chat session to maintain continuity.
Enhanced for Phase 1: Zero-Command Automation
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
import uuid

SHARED_CONTEXT_PATH = Path(__file__).parent.parent / ".shared_chat_context.json"


def load_shared_context() -> Dict[str, Any]:
    """Load the shared context file."""
    if not SHARED_CONTEXT_PATH.exists():
        return {
            "metadata": {
                "description": "Shared context across all private mode chats",
                "version": "2.0",
                "last_updated": None,
                "auto_mode": True
            },
            "daily_progress": {
                "date": None,
                "one_thing": {"task": None, "status": "NOT_STARTED", "progress_notes": []},
                "completed_tasks": [],
                "in_progress_tasks": [],
                "blockers": [],
                "key_decisions": [],
                "learnings": []
            },
            "cross_chat_knowledge": {
                "recent_completions": [],
                "recent_decisions": [],
                "recent_blockers": []
            },
            "performance_metrics": {
                "manual_commands_count": 0,
                "auto_updates_count": 0,
                "context_accuracy": 0.0,
                "last_improvement_date": None
            }
        }
    
    with open(SHARED_CONTEXT_PATH, 'r') as f:
        return json.load(f)


def save_shared_context(context: Dict[str, Any]):
    """Save the shared context file."""
    context["metadata"]["last_updated"] = datetime.now().isoformat()
    # Increment auto_updates_count
    if "performance_metrics" not in context:
        context["performance_metrics"] = {"auto_updates_count": 0}
    context["performance_metrics"]["auto_updates_count"] = context["performance_metrics"].get("auto_updates_count", 0) + 1
    
    with open(SHARED_CONTEXT_PATH, 'w') as f:
        json.dump(context, f, indent=2, default=str)


def update_daily_progress(
    task: Optional[str] = None,
    status: Optional[str] = None,
    completed: bool = False,
    blocker: Optional[str] = None,
    decision: Optional[str] = None,
    learning: Optional[str] = None
):
    """Update daily progress in shared context."""
    context = load_shared_context()
    today = datetime.now().strftime("%Y-%m-%d")
    
    if context["daily_progress"]["date"] != today:
        context["daily_progress"] = {
            "date": today,
            "one_thing": {"task": None, "status": "NOT_STARTED", "progress_notes": []},
            "completed_tasks": [],
            "in_progress_tasks": [],
            "blockers": [],
            "key_decisions": [],
            "learnings": []
        }
    
    if task:
        if completed:
            if task not in [t.get("task") for t in context["daily_progress"]["completed_tasks"]]:
                context["daily_progress"]["completed_tasks"].append({
                    "task": task,
                    "completed_at": datetime.now().isoformat()
                })
            context["daily_progress"]["in_progress_tasks"] = [
                t for t in context["daily_progress"]["in_progress_tasks"]
                if t.get("task") != task
            ]
            # Add to recent completions
            if "cross_chat_knowledge" not in context:
                context["cross_chat_knowledge"] = {"recent_completions": []}
            context["cross_chat_knowledge"]["recent_completions"].append({
                "task": task,
                "completed_at": datetime.now().isoformat()
            })
            # Keep only last 10 completions
            context["cross_chat_knowledge"]["recent_completions"] = context["cross_chat_knowledge"]["recent_completions"][-10:]
        else:
            if not any(t.get("task") == task for t in context["daily_progress"]["in_progress_tasks"]):
                context["daily_progress"]["in_progress_tasks"].append({
                    "task": task,
                    "started_at": datetime.now().isoformat(),
                    "status": status or "IN_PROGRESS"
                })
    
    if blocker:
        context["daily_progress"]["blockers"].append({
            "blocker": blocker,
            "identified_at": datetime.now().isoformat(),
            "resolved": False
        })
        # Add to recent blockers
        if "cross_chat_knowledge" not in context:
            context["cross_chat_knowledge"] = {"recent_blockers": []}
        context["cross_chat_knowledge"]["recent_blockers"].append({
            "blocker": blocker,
            "identified_at": datetime.now().isoformat()
        })
        context["cross_chat_knowledge"]["recent_blockers"] = context["cross_chat_knowledge"]["recent_blockers"][-10:]
    
    if decision:
        context["daily_progress"]["key_decisions"].append({
            "decision": decision,
            "made_at": datetime.now().isoformat()
        })
        # Add to recent decisions
        if "cross_chat_knowledge" not in context:
            context["cross_chat_knowledge"] = {"recent_decisions": []}
        context["cross_chat_knowledge"]["recent_decisions"].append({
            "decision": decision,
            "made_at": datetime.now().isoformat()
        })
        context["cross_chat_knowledge"]["recent_decisions"] = context["cross_chat_knowledge"]["recent_decisions"][-10:]
    
    if learning:
        context["daily_progress"]["learnings"].append({
            "learning": learning,
            "captured_at": datetime.now().isoformat()
        })
    
    save_shared_context(context)
    return context


def get_daily_progress() -> Dict[str, Any]:
    """Get today's progress from shared context."""
    context = load_shared_context()
    today = datetime.now().strftime("%Y-%m-%d")
    
    if context["daily_progress"]["date"] != today:
        return {
            "date": today,
            "one_thing": {"task": None, "status": "NOT_STARTED"},
            "completed_tasks": [],
            "in_progress_tasks": [],
            "blockers": [],
            "key_decisions": [],
            "learnings": []
        }
    
    return context["daily_progress"]


def update_one_thing(task: str, status: str = "IN_PROGRESS", note: Optional[str] = None):
    """Update the ONE thing for today."""
    context = load_shared_context()
    today = datetime.now().strftime("%Y-%m-%d")
    
    if context["daily_progress"]["date"] != today:
        context["daily_progress"]["date"] = today
    
    context["daily_progress"]["one_thing"]["task"] = task
    context["daily_progress"]["one_thing"]["status"] = status
    
    if note:
        context["daily_progress"]["one_thing"]["progress_notes"].append({
            "note": note,
            "timestamp": datetime.now().isoformat()
        })
    
    save_shared_context(context)
    return context


def get_cross_chat_summary() -> str:
    """Get a summary of cross-chat knowledge for new chat sessions."""
    context = load_shared_context()
    today = datetime.now().strftime("%Y-%m-%d")
    
    summary = f"📊 Cross-Chat Summary (Last Updated: {context['metadata'].get('last_updated', 'Never')})\n\n"
    
    if context["daily_progress"]["date"] == today:
        progress = context["daily_progress"]
        summary += f"🎯 ONE Thing: {progress['one_thing'].get('task', 'Not set')} ({progress['one_thing'].get('status', 'NOT_STARTED')})\n"
        summary += f"✅ Completed: {len(progress['completed_tasks'])} tasks\n"
        summary += f"🔄 In Progress: {len(progress['in_progress_tasks'])} tasks\n"
        summary += f"⚠️ Blockers: {len(progress['blockers'])} blockers\n"
        summary += f"💡 Learnings: {len(progress['learnings'])} captured\n\n"
    
    if context.get("cross_chat_knowledge", {}).get("recent_completions"):
        summary += "✅ Recent Completions:\n"
        for completion in context["cross_chat_knowledge"]["recent_completions"][-5:]:
            summary += f"  - {completion.get('task', 'Unknown')}\n"
        summary += "\n"
    
    if context.get("cross_chat_knowledge", {}).get("recent_decisions"):
        summary += "🎯 Recent Decisions:\n"
        for decision in context["cross_chat_knowledge"]["recent_decisions"][-5:]:
            summary += f"  - {decision.get('decision', 'Unknown')}\n"
        summary += "\n"
    
    # Performance metrics
    metrics = context.get("performance_metrics", {})
    if metrics.get("auto_updates_count", 0) > 0:
        summary += f"⚡ Auto-Updates: {metrics.get('auto_updates_count', 0)}\n"
        summary += f"📝 Manual Commands: {metrics.get('manual_commands_count', 0)}\n"
    
    return summary


def start_session(session_id: Optional[str] = None) -> str:
    """Start a new chat session and return session ID."""
    context = load_shared_context()
    if not session_id:
        session_id = str(uuid.uuid4())
    
    context["current_session"]["session_id"] = session_id
    context["current_session"]["date"] = datetime.now().strftime("%Y-%m-%d")
    context["current_session"]["last_activity"] = datetime.now().isoformat()
    
    if session_id not in context["current_session"]["active_chats"]:
        context["current_session"]["active_chats"].append(session_id)
    
    save_shared_context(context)
    return session_id


def end_session(session_id: Optional[str] = None):
    """End a chat session."""
    context = load_shared_context()
    if session_id and session_id in context["current_session"]["active_chats"]:
        context["current_session"]["active_chats"].remove(session_id)
    context["current_session"]["last_activity"] = datetime.now().isoformat()
    save_shared_context(context)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "update":
            task = sys.argv[2] if len(sys.argv) > 2 else None
            completed = "--completed" in sys.argv
            update_daily_progress(task=task, completed=completed)
            print(f"✅ Updated shared context")
        
        elif command == "one-thing":
            task = sys.argv[2] if len(sys.argv) > 2 else None
            status = sys.argv[3] if len(sys.argv) > 3 else "IN_PROGRESS"
            if task:
                update_one_thing(task, status)
                print(f"✅ ONE Thing updated: {task}")
            else:
                print("Usage: python update_shared_context.py one-thing 'Task description' [status]")
        
        elif command == "summary":
            print(get_cross_chat_summary())
        
        elif command == "progress":
            progress = get_daily_progress()
            print(json.dumps(progress, indent=2, default=str))
        
        elif command == "start":
            session_id = start_session()
            print(f"✅ Session started: {session_id}")
        
        elif command == "end":
            session_id = sys.argv[2] if len(sys.argv) > 2 else None
            end_session(session_id)
            print(f"✅ Session ended")
        
        else:
            print("Usage:")
            print("  python update_shared_context.py update [task] [--completed]")
            print("  python update_shared_context.py one-thing 'Task' [status]")
            print("  python update_shared_context.py summary")
            print("  python update_shared_context.py progress")
            print("  python update_shared_context.py start")
            print("  python update_shared_context.py end [session_id]")
    else:
        print(get_cross_chat_summary())



