#!/usr/bin/env python3
"""
Garvis Escalation System
BallCODE Fully Integrated System

Purpose: Handle escalations when Garvis needs clarification or encounters blockers.
Garvis only escalates when truly unclear or blocking.
"""

import sys
import json
import sqlite3
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional

WORKFLOW_DIR = Path(__file__).parent.parent
GARVIS_DB = WORKFLOW_DIR / "garvis_jobs.db"
ESCALATION_FILE = WORKFLOW_DIR / "GARVIS-ESCALATIONS.md"

def create_escalation(job_id: str, reason: str, context: Optional[Dict] = None) -> Dict:
    """Create escalation ticket for human intervention"""
    escalation = {
        'job_id': job_id,
        'reason': reason,
        'context': context or {},
        'created_at': datetime.now().isoformat(),
        'status': 'pending',
        'question': _generate_question(reason, context)
    }
    
    # Save to file for visibility
    _save_escalation_to_file(escalation)
    
    # Update job in database
    if GARVIS_DB.exists():
        conn = sqlite3.connect(GARVIS_DB)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE garvis_jobs
            SET escalation_needed = 1, escalation_reason = ?, status = 'escalated'
            WHERE job_id = ?
        """, (reason, job_id))
        conn.commit()
        conn.close()
    
    return escalation

def _generate_question(reason: str, context: Optional[Dict]) -> str:
    """Generate clear question for user"""
    if 'unclear' in reason.lower() or 'ambiguous' in reason.lower():
        return f"I need clarification: {reason}. Can you provide more details?"
    elif 'blocked' in reason.lower() or 'error' in reason.lower():
        return f"I encountered a blocker: {reason}. How should I proceed?"
    elif 'missing' in reason.lower():
        return f"I'm missing something: {reason}. Can you provide it?"
    else:
        return f"I need your input: {reason}"

def _save_escalation_to_file(escalation: Dict):
    """Save escalation to markdown file for visibility"""
    if not ESCALATION_FILE.exists():
        ESCALATION_FILE.write_text("# Garvis Escalations\n\n")
    
    content = ESCALATION_FILE.read_text()
    
    escalation_text = f"""
## Escalation: {escalation['job_id']}

**Created:** {escalation['created_at']}  
**Status:** {escalation['status']}  
**Reason:** {escalation['reason']}

**Question for You:**
{escalation['question']}

**Context:**
```json
{json.dumps(escalation['context'], indent=2)}
```

---

"""
    
    # Prepend to file
    ESCALATION_FILE.write_text(escalation_text + content)

def get_pending_escalations() -> List[Dict]:
    """Get all pending escalations"""
    if not GARVIS_DB.exists():
        return []
    
    conn = sqlite3.connect(GARVIS_DB)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT job_id, one_thing, escalation_reason, created_at
        FROM garvis_jobs
        WHERE escalation_needed = 1 AND status = 'escalated'
        ORDER BY created_at DESC
    """)
    
    escalations = [dict(row) for row in cursor.fetchall()]
    conn.close()
    
    return escalations

def resolve_escalation(job_id: str, answer: str):
    """Resolve escalation with user's answer"""
    if not GARVIS_DB.exists():
        return
    
    conn = sqlite3.connect(GARVIS_DB)
    cursor = conn.cursor()
    
    # Update job - remove escalation flag, resume
    cursor.execute("""
        UPDATE garvis_jobs
        SET escalation_needed = 0, escalation_reason = NULL, status = 'in_progress'
        WHERE job_id = ?
    """, (job_id,))
    
    # Log resolution
    cursor.execute("""
        INSERT INTO garvis_execution_log (job_id, step, action, result)
        VALUES (?, 'escalation_resolved', 'User provided answer', ?)
    """, (job_id, answer))
    
    conn.commit()
    conn.close()

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python scripts/garvis-escalation.py --create <job_id> <reason>")
        print("  python scripts/garvis-escalation.py --list")
        print("  python scripts/garvis-escalation.py --resolve <job_id> <answer>")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == '--create':
        if len(sys.argv) < 4:
            print("Usage: python scripts/garvis-escalation.py --create <job_id> <reason>")
            sys.exit(1)
        job_id = sys.argv[2]
        reason = sys.argv[3]
        escalation = create_escalation(job_id, reason)
        print(json.dumps(escalation, indent=2))
    
    elif command == '--list':
        escalations = get_pending_escalations()
        if not escalations:
            print("No pending escalations. Garvis is handling everything!")
        else:
            print(f"\n⚠️  {len(escalations)} PENDING ESCALATIONS\n")
            for esc in escalations:
                print(f"Job: {esc['job_id']}")
                print(f"ONE Thing: {esc['one_thing']}")
                print(f"Reason: {esc['escalation_reason']}")
                print(f"Created: {esc['created_at']}")
                print("-" * 70)
    
    elif command == '--resolve':
        if len(sys.argv) < 4:
            print("Usage: python scripts/garvis-escalation.py --resolve <job_id> <answer>")
            sys.exit(1)
        job_id = sys.argv[2]
        answer = ' '.join(sys.argv[3:])
        resolve_escalation(job_id, answer)
        print(f"Escalation resolved for {job_id}. Garvis will resume execution.")
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()


