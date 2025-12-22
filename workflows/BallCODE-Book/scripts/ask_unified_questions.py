#!/usr/bin/env python3
"""
Quick command to trigger Unified Prompting Framework questions.

Usage:
    python scripts/ask_unified_questions.py              # Interactive mode
    python scripts/ask_unified_questions.py --quick     # Quick 5 questions
    python scripts/ask_unified_questions.py --full       # Full 23 questions
    python scripts/ask_unified_questions.py --show       # Just show questions
"""

import sys
import os

# Quick 5 questions
QUICK_QUESTIONS = {
    "1. GOAL": "What exactly do I want? (Be specific)",
    "2. FORMAT": "What structure do I need? (List, table, script, document, etc.)",
    "3. CONTEXT": "What background information is relevant?",
    "4. EXAMPLES": "What illustrates what I want?",
    "5. RESULTS": "What does success look like?"
}

# Full 23 questions
FULL_QUESTIONS = {
    "GOAL & CLARITY": [
        "What exactly do I want? (Be specific, not vague)",
        "What does success look like?",
        "What are the constraints?",
        "Who is the audience?"
    ],
    "FORMAT & LOGIC": [
        "What structure do I need? (List, table, script, outline, code, document, etc.)",
        "What's the logical flow or sequence?",
        "How should this be organized?",
        "What steps should be followed?"
    ],
    "GUARDRAILS & ADAPTATION": [
        "What accuracy standards are required?",
        "What tone/style should be used?",
        "What should be avoided?",
        "What constraints or limitations exist?",
        "What flexibility is needed?"
    ],
    "CONTEXT, EXAMPLES & ALPHA EVOLVE": [
        "What background information is relevant?",
        "What are my goals and objectives?",
        "What examples illustrate what I want?",
        "What similar work exists to reference?",
        "What foundational concepts need to be established first? (Alpha Evolve Layer 1)",
        "How should this build systematically? (Alpha Evolve Layers 2, 3, 4...)",
        "What systems thinking is needed?"
    ],
    "RESULTS": [
        "What does 'done' look like?",
        "How will I know it's successful?",
        "What are the success criteria?"
    ]
}

def show_quick_questions():
    """Display quick 5 questions."""
    print("\n" + "="*70)
    print("🎯 UNIFIED PROMPTING FRAMEWORK - QUICK MODE (5 Questions)")
    print("="*70 + "\n")
    
    for key, question in QUICK_QUESTIONS.items():
        print(f"{key}:")
        print(f"  {question}")
        print(f"  Answer: _________________________________\n")
    
    print("="*70)
    print("\n💡 Copy these questions and answer them before your prompt!\n")

def show_full_questions():
    """Display full 23 questions."""
    print("\n" + "="*70)
    print("🎯 UNIFIED PROMPTING FRAMEWORK - FULL MODE (23 Questions)")
    print("="*70 + "\n")
    
    question_num = 1
    for category, questions in FULL_QUESTIONS.items():
        print(f"\n### {category}")
        for question in questions:
            print(f"\n{question_num}. {question}")
            print(f"   Answer: _________________________________")
            question_num += 1
    
    print("\n" + "="*70)
    print("\n💡 Copy these questions and answer them before your prompt!\n")

def interactive_mode():
    """Interactive mode - let user choose."""
    print("\n" + "="*70)
    print("🎯 UNIFIED PROMPTING FRAMEWORK")
    print("="*70)
    print("\nSelect mode:")
    print("  1. Quick mode (5 essential questions) - Recommended for most tasks")
    print("  2. Full framework (23 questions) - For complex tasks")
    print("  3. Just show questions (no interactive)")
    print()
    
    try:
        choice = input("Enter choice (1/2/3): ").strip()
        
        if choice == "1":
            show_quick_questions()
        elif choice == "2":
            show_full_questions()
        elif choice == "3":
            print("\nQuick questions:")
            show_quick_questions()
            print("\n\nFull questions:")
            show_full_questions()
        else:
            print("Invalid choice. Showing quick questions by default.")
            show_quick_questions()
    except (EOFError, KeyboardInterrupt):
        print("\n\nShowing quick questions by default.")
        show_quick_questions()

def main():
    """Main function."""
    if len(sys.argv) > 1:
        flag = sys.argv[1].lower()
        
        if flag == "--quick" or flag == "-q":
            show_quick_questions()
        elif flag == "--full" or flag == "-f":
            show_full_questions()
        elif flag == "--show" or flag == "-s":
            show_quick_questions()
            print("\n" + "="*70 + "\n")
            show_full_questions()
        elif flag == "--help" or flag == "-h":
            print(__doc__)
        else:
            print(f"Unknown flag: {flag}")
            print(__doc__)
            sys.exit(1)
    else:
        interactive_mode()

if __name__ == "__main__":
    main()



