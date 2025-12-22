#!/usr/bin/env python3
"""
Daily Morning Questions - BallCODE Daily Workflow System

Usage:
    python scripts/daily-morning-questions.py              # Interactive mode
    python scripts/daily-morning-questions.py --morning    # Show morning questions
    python scripts/daily-morning-questions.py -m            # Short form
    python scripts/daily-morning-questions.py --with-n8n   # Include n8n status
"""

import sys
import os
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

# Get workflow directory
WORKFLOW_DIR = Path(__file__).parent.parent

# Daily workflow questions
DAILY_QUESTIONS = {
    "1️⃣ Orchestrate — Don't Multitask": "What is the ONE system/process you're orchestrating today? (Not juggling multiple things)",
    "2️⃣ Protect Deep Work Windows": "When is your 2–3 hour Deep Work window today? (No meetings, no texts, no tabs)",
    "3️⃣ Batch Similar Contexts": "What similar tasks can you batch together today? (Group by context: finance, creative, coding, meetings, etc.)",
    "4️⃣ Delegate with Context": """What are you delegating today (to AI or humans)? For each delegation, answer:

What's the goal?

How will success be measured?

When should it escalate back to you?""",
    "5️⃣ Use If–Then Rules": "What if–then rules are you activating today?",
    "6️⃣ Track Your Metrics Daily": """What metrics are you tracking today?

Focus Time: _ hours (target: 2–3 hours)

Delegations Created: _ (target: 3–5)

Context Switches: _ (target: < 5)

Energy Level (1–10): _ (target: 7+)

One Domino Status: _""",
    "7️⃣ Automate for Clarity, Not Complexity": "What repetitive/reactive work can you automate or delegate to AI today?",
    "8️⃣ Move One Domino a Day": "What's the ONE task today that makes everything else easier or unnecessary?",
    "9️⃣ Audit Systems Weekly": "Is today your weekly audit day? (If yes, complete the weekly audit checklist)",
    "🔟 Protect Energy Like a KPI": "What's your energy level right now? (1–10 scale)"
}

def get_current_date():
    """Get current date from DATE-TIME-TRACKER.md or use system date."""
    date_file = WORKFLOW_DIR / "DATE-TIME-TRACKER.md"
    if date_file.exists():
        try:
            with open(date_file, 'r') as f:
                content = f.read()
                # Try to extract date from file
                for line in content.split('\n'):
                    if 'date' in line.lower() or 'today' in line.lower():
                        # Simple extraction - can be improved
                        pass
        except:
            pass
    
    # Fallback to system date
    return datetime.now()

def get_yesterday_date(today):
    """Calculate yesterday's date."""
    return today - timedelta(days=1)

def get_yesterday_summary(today):
    """Try to get yesterday's summary from daily workflow file."""
    yesterday = get_yesterday_date(today)
    date_str = yesterday.strftime("%Y-%m-%d")
    
    # Try different date formats
    possible_files = [
        WORKFLOW_DIR / f"DAILY-WORKFLOW-{date_str}.md",
        WORKFLOW_DIR / f"documents/DAILY-WORKFLOW-{date_str}.md",
        WORKFLOW_DIR / f"DAILY-WORKFLOW-{yesterday.strftime('%B-%d-%Y')}.md",
        WORKFLOW_DIR / f"DAILY-WORKFLOW-{yesterday.strftime('%B-%d-%Y').lower()}.md",
    ]
    
    for file_path in possible_files:
        if file_path.exists():
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    # Extract summary section if exists
                    if "summary" in content.lower() or "completed" in content.lower():
                        return f"[Found yesterday's workflow file: {file_path.name}]"
            except:
                pass
    
    return "[No yesterday's workflow file found - you can provide summary manually]"

def get_n8n_status():
    """Get n8n workflow status by running daily-n8n-report.sh."""
    report_script = WORKFLOW_DIR / "scripts" / "daily-n8n-report.sh"
    
    if report_script.exists():
        try:
            result = subprocess.run(
                ["bash", str(report_script)],
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0:
                return result.stdout
            else:
                return "[n8n status check failed - check manually]"
        except subprocess.TimeoutExpired:
            return "[n8n status check timed out]"
        except Exception as e:
            return f"[n8n status check error: {str(e)}]"
    else:
        return "[n8n status script not found]"

def show_morning_questions(include_n8n=False):
    """Display daily morning questions with context."""
    today = get_current_date()
    yesterday = get_yesterday_date(today)
    
    today_str = today.strftime("%Y-%m-%d")
    yesterday_str = yesterday.strftime("%Y-%m-%d")
    
    print("\n" + "="*70)
    print("🌅 DAILY WORKFLOW — " + today_str)
    print("="*70 + "\n")
    
    # Yesterday's summary
    print("Yesterday's summary (" + yesterday_str + ")")
    print("-" * 70)
    yesterday_summary = get_yesterday_summary(today)
    print(yesterday_summary)
    print()
    
    # n8n Status (if requested)
    if include_n8n:
        print("📊 BALLCODE N8N WORKFLOW STATUS")
        print("-" * 70)
        n8n_status = get_n8n_status()
        print(n8n_status)
        print()
    
    # Daily questions
    print("10 daily workflow questions")
    print("-" * 70)
    print()
    
    for emoji_question, question_text in DAILY_QUESTIONS.items():
        print(emoji_question)
        print()
        if "\n" in question_text:
            # Multi-line question
            for line in question_text.split('\n'):
                print(line)
        else:
            print(question_text)
        print()
        print("Answer: _________________________________")
        print()
    
    print("="*70)
    print("\n💡 Copy these questions and answer them in your chat!")
    print("   Then tell me your ONE thing focus for today.\n")

def show_help():
    """Show help message."""
    print(__doc__)
    print("\nExamples:")
    print("  python scripts/daily-morning-questions.py --morning")
    print("  python scripts/daily-morning-questions.py -m")
    print("  python scripts/daily-morning-questions.py --with-n8n")
    print("  python scripts/daily-morning-questions.py  # Interactive mode")

def interactive_mode():
    """Interactive mode - let user choose."""
    print("\n" + "="*70)
    print("🌅 DAILY MORNING QUESTIONS")
    print("="*70)
    print("\nSelect option:")
    print("  1. Show morning questions (standard)")
    print("  2. Show morning questions with n8n status")
    print("  3. Show help")
    print()
    
    try:
        choice = input("Enter choice (1/2/3): ").strip()
        
        if choice == "1":
            show_morning_questions(include_n8n=False)
        elif choice == "2":
            show_morning_questions(include_n8n=True)
        elif choice == "3":
            show_help()
        else:
            print("Invalid choice. Showing morning questions by default.")
            show_morning_questions(include_n8n=False)
    except (EOFError, KeyboardInterrupt):
        print("\n\nShowing morning questions by default.")
        show_morning_questions(include_n8n=False)

def main():
    """Main function."""
    if len(sys.argv) > 1:
        flag = sys.argv[1].lower()
        
        if flag == "--morning" or flag == "-m":
            show_morning_questions(include_n8n=False)
        elif flag == "--with-n8n" or flag == "--n8n":
            show_morning_questions(include_n8n=True)
        elif flag == "--help" or flag == "-h":
            show_help()
        else:
            print(f"Unknown flag: {flag}")
            print(__doc__)
            sys.exit(1)
    else:
        interactive_mode()

if __name__ == "__main__":
    main()

