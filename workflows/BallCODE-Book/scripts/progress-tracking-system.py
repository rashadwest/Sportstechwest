#!/usr/bin/env python3
"""
BallCODE Progress Tracking System
Tracks student progress through books, games, and curriculum

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import os
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from collections import defaultdict

PROJECT_ROOT = Path(__file__).parent.parent
PROGRESS_DATA_FILE = PROJECT_ROOT / "progress-data.json"
ANALYTICS_DATA_FILE = PROJECT_ROOT / "analytics-data.json"

# Progress tracking structure
PROGRESS_SCHEMA = {
    "students": {},  # student_id -> progress data
    "books": {},     # book_id -> completion stats
    "games": {},     # level_id -> completion stats
    "curriculum": {}, # concept_id -> mastery stats
    "last_updated": None
}

def load_progress_data() -> Dict:
    """Load progress tracking data."""
    if PROGRESS_DATA_FILE.exists():
        with open(PROGRESS_DATA_FILE, 'r') as f:
            return json.load(f)
    return PROGRESS_SCHEMA.copy()

def save_progress_data(data: Dict):
    """Save progress tracking data."""
    data["last_updated"] = datetime.now().isoformat()
    with open(PROGRESS_DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def track_book_completion(student_id: str, book_id: str, completed: bool = True):
    """Track book completion for a student."""
    data = load_progress_data()
    
    # Initialize student if needed
    if student_id not in data["students"]:
        data["students"][student_id] = {
            "books_completed": [],
            "games_completed": [],
            "curriculum_mastered": [],
            "total_time_spent": 0,
            "first_seen": datetime.now().isoformat(),
            "last_active": datetime.now().isoformat()
        }
    
    student = data["students"][student_id]
    student["last_active"] = datetime.now().isoformat()
    
    # Track book completion
    if completed and book_id not in student["books_completed"]:
        student["books_completed"].append({
            "book_id": book_id,
            "completed_at": datetime.now().isoformat()
        })
    
    # Update book stats
    if book_id not in data["books"]:
        data["books"][book_id] = {
            "total_completions": 0,
            "unique_students": set(),
            "avg_completion_time": 0,
            "completion_rate": 0.0
        }
    
    book_stats = data["books"][book_id]
    if completed:
        book_stats["total_completions"] += 1
        book_stats["unique_students"].add(student_id)
        # Convert set to list for JSON serialization
        book_stats["unique_students"] = list(book_stats["unique_students"])
    
    save_progress_data(data)
    return True

def track_game_completion(student_id: str, level_id: str, score: float = 0.0, attempts: int = 1):
    """Track game level completion."""
    data = load_progress_data()
    
    # Initialize student if needed
    if student_id not in data["students"]:
        data["students"][student_id] = {
            "books_completed": [],
            "games_completed": [],
            "curriculum_mastered": [],
            "total_time_spent": 0,
            "first_seen": datetime.now().isoformat(),
            "last_active": datetime.now().isoformat()
        }
    
    student = data["students"][student_id]
    student["last_active"] = datetime.now().isoformat()
    
    # Track game completion
    game_completion = {
        "level_id": level_id,
        "completed_at": datetime.now().isoformat(),
        "score": score,
        "attempts": attempts
    }
    
    # Check if already completed (update if better score)
    existing = next((g for g in student["games_completed"] if g["level_id"] == level_id), None)
    if existing:
        if score > existing.get("score", 0):
            student["games_completed"].remove(existing)
            student["games_completed"].append(game_completion)
    else:
        student["games_completed"].append(game_completion)
    
    # Update game stats
    if level_id not in data["games"]:
        data["games"][level_id] = {
            "total_completions": 0,
            "unique_students": set(),
            "avg_score": 0.0,
            "avg_attempts": 0.0,
            "completion_rate": 0.0
        }
    
    game_stats = data["games"][level_id]
    game_stats["total_completions"] += 1
    game_stats["unique_students"].add(student_id)
    game_stats["unique_students"] = list(game_stats["unique_students"])
    
    # Update averages
    all_scores = [g.get("score", 0) for s in data["students"].values() 
                  for g in s.get("games_completed", []) if g["level_id"] == level_id]
    all_attempts = [g.get("attempts", 1) for s in data["students"].values() 
                    for g in s.get("games_completed", []) if g["level_id"] == level_id]
    
    if all_scores:
        game_stats["avg_score"] = sum(all_scores) / len(all_scores)
    if all_attempts:
        game_stats["avg_attempts"] = sum(all_attempts) / len(all_attempts)
    
    save_progress_data(data)
    return True

def track_curriculum_mastery(student_id: str, concept_id: str, mastery_level: float = 1.0):
    """Track curriculum concept mastery."""
    data = load_progress_data()
    
    # Initialize student if needed
    if student_id not in data["students"]:
        data["students"][student_id] = {
            "books_completed": [],
            "games_completed": [],
            "curriculum_mastered": [],
            "total_time_spent": 0,
            "first_seen": datetime.now().isoformat(),
            "last_active": datetime.now().isoformat()
        }
    
    student = data["students"][student_id]
    student["last_active"] = datetime.now().isoformat()
    
    # Track curriculum mastery
    mastery = {
        "concept_id": concept_id,
        "mastery_level": mastery_level,
        "mastered_at": datetime.now().isoformat()
    }
    
    # Update if already exists
    existing = next((m for m in student["curriculum_mastered"] if m["concept_id"] == concept_id), None)
    if existing:
        if mastery_level > existing.get("mastery_level", 0):
            student["curriculum_mastered"].remove(existing)
            student["curriculum_mastered"].append(mastery)
    else:
        student["curriculum_mastered"].append(mastery)
    
    # Update curriculum stats
    if concept_id not in data["curriculum"]:
        data["curriculum"][concept_id] = {
            "total_mastered": 0,
            "unique_students": set(),
            "avg_mastery_level": 0.0,
            "mastery_rate": 0.0
        }
    
    curriculum_stats = data["curriculum"][concept_id]
    if mastery_level >= 0.8:  # Consider "mastered" at 80%+
        curriculum_stats["total_mastered"] += 1
        curriculum_stats["unique_students"].add(student_id)
        curriculum_stats["unique_students"] = list(curriculum_stats["unique_students"])
    
    # Update average mastery
    all_mastery = [m.get("mastery_level", 0) for s in data["students"].values() 
                   for m in s.get("curriculum_mastered", []) if m["concept_id"] == concept_id]
    if all_mastery:
        curriculum_stats["avg_mastery_level"] = sum(all_mastery) / len(all_mastery)
    
    save_progress_data(data)
    return True

def get_student_progress(student_id: str) -> Dict:
    """Get progress for a specific student."""
    data = load_progress_data()
    return data["students"].get(student_id, {})

def get_overall_stats() -> Dict:
    """Get overall progress statistics."""
    data = load_progress_data()
    
    total_students = len(data["students"])
    total_books_completed = sum(len(s.get("books_completed", [])) for s in data["students"].values())
    total_games_completed = sum(len(s.get("games_completed", [])) for s in data["students"].values())
    total_concepts_mastered = sum(len(s.get("curriculum_mastered", [])) for s in data["students"].values())
    
    active_students = sum(1 for s in data["students"].values() 
                         if datetime.fromisoformat(s.get("last_active", "2000-01-01")) > datetime.now() - timedelta(days=7))
    
    return {
        "total_students": total_students,
        "active_students_7d": active_students,
        "total_books_completed": total_books_completed,
        "total_games_completed": total_games_completed,
        "total_concepts_mastered": total_concepts_mastered,
        "avg_books_per_student": total_books_completed / total_students if total_students > 0 else 0,
        "avg_games_per_student": total_games_completed / total_students if total_students > 0 else 0,
        "avg_concepts_per_student": total_concepts_mastered / total_students if total_students > 0 else 0
    }

def generate_progress_report() -> str:
    """Generate a progress tracking report."""
    stats = get_overall_stats()
    data = load_progress_data()
    
    report = f"""
# 📊 BallCODE Progress Tracking Report

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overall Statistics

- **Total Students:** {stats['total_students']}
- **Active Students (7 days):** {stats['active_students_7d']}
- **Total Books Completed:** {stats['total_books_completed']}
- **Total Games Completed:** {stats['total_games_completed']}
- **Total Concepts Mastered:** {stats['total_concepts_mastered']}
- **Avg Books/Student:** {stats['avg_books_per_student']:.2f}
- **Avg Games/Student:** {stats['avg_games_per_student']:.2f}
- **Avg Concepts/Student:** {stats['avg_concepts_per_student']:.2f}

## Book Completion Stats

"""
    
    for book_id, book_stats in data.get("books", {}).items():
        report += f"- **{book_id}**: {book_stats.get('total_completions', 0)} completions, {len(book_stats.get('unique_students', []))} unique students\n"
    
    report += "\n## Game Completion Stats\n\n"
    
    for level_id, game_stats in data.get("games", {}).items():
        report += f"- **{level_id}**: {game_stats.get('total_completions', 0)} completions, "
        report += f"Avg Score: {game_stats.get('avg_score', 0):.2f}, "
        report += f"Avg Attempts: {game_stats.get('avg_attempts', 0):.2f}\n"
    
    report += "\n## Curriculum Mastery Stats\n\n"
    
    for concept_id, curriculum_stats in data.get("curriculum", {}).items():
        report += f"- **{concept_id}**: {curriculum_stats.get('total_mastered', 0)} mastered, "
        report += f"Avg Mastery: {curriculum_stats.get('avg_mastery_level', 0):.2%}\n"
    
    return report

def main():
    """Main function for CLI usage."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python progress-tracking-system.py report          # Generate report")
        print("  python progress-tracking-system.py stats         # Show overall stats")
        print("  python progress-tracking-system.py test          # Run test tracking")
        return
    
    command = sys.argv[1]
    
    if command == "report":
        report = generate_progress_report()
        print(report)
        
        # Save report
        report_file = PROJECT_ROOT / "PROGRESS-REPORT.md"
        with open(report_file, 'w') as f:
            f.write(report)
        print(f"\n✅ Report saved to: {report_file}")
    
    elif command == "stats":
        stats = get_overall_stats()
        print("\n📊 Overall Progress Statistics:")
        print(json.dumps(stats, indent=2))
    
    elif command == "test":
        print("🧪 Running test tracking...")
        
        # Test book completion
        track_book_completion("test_student_1", "book1", True)
        print("✅ Tracked book completion")
        
        # Test game completion
        track_game_completion("test_student_1", "level_math_1", score=85.0, attempts=2)
        print("✅ Tracked game completion")
        
        # Test curriculum mastery
        track_curriculum_mastery("test_student_1", "concept_variables", mastery_level=0.9)
        print("✅ Tracked curriculum mastery")
        
        print("\n✅ Test tracking complete!")
        print("Run 'python progress-tracking-system.py report' to see results")
    
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()


