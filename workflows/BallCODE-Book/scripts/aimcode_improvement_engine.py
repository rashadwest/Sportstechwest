#!/usr/bin/env python3
"""
AIMCODE Improvement Engine
Integrates AIMCODE Build-Measure-Learn methodology into continuous improvement process.

This engine applies AIMCODE methodology to every improvement:
- CLEAR Framework for planning
- BUILD phase for implementation
- MEASURE phase for data collection
- LEARN phase for refinement
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, Optional, List
import uuid

SHARED_CONTEXT_PATH = Path(__file__).parent.parent / ".shared_chat_context.json"
IMPROVEMENTS_LOG_PATH = Path(__file__).parent.parent / "data" / "aimcode_improvements.json"
LEARNINGS_LOG_PATH = Path(__file__).parent.parent / "data" / "aimcode_learnings.json"


class AIMCODEImprovementEngine:
    """AIMCODE-based improvement engine for continuous system enhancement."""
    
    def __init__(self):
        self.improvements_path = IMPROVEMENTS_LOG_PATH
        self.learnings_path = LEARNINGS_LOG_PATH
        self.ensure_data_directory()
    
    def ensure_data_directory(self):
        """Ensure data directory exists."""
        self.improvements_path.parent.mkdir(parents=True, exist_ok=True)
        self.learnings_path.parent.mkdir(parents=True, exist_ok=True)
    
    def apply_clear_framework(self, improvement: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply CLEAR framework to improvement planning.
        
        C - Clarity: Clear objectives
        L - Logic: Systematic approach
        E - Examples: Reference successful improvements
        A - Adaptation: Flexible implementation
        R - Results: Success metrics
        """
        clear_analysis = {
            "clarity": {
                "objectives": improvement.get("objectives", []),
                "requirements": improvement.get("requirements", []),
                "expectations": improvement.get("expectations", [])
            },
            "logic": {
                "systematic_approach": improvement.get("systematic_approach", ""),
                "dependencies": improvement.get("dependencies", []),
                "progression": improvement.get("progression", [])
            },
            "examples": {
                "reference_improvements": improvement.get("reference_improvements", []),
                "similar_features": improvement.get("similar_features", []),
                "best_practices": improvement.get("best_practices", [])
            },
            "adaptation": {
                "constraints": improvement.get("constraints", []),
                "flexibility_needed": improvement.get("flexibility_needed", []),
                "contingency_plans": improvement.get("contingency_plans", [])
            },
            "results": {
                "success_metrics": improvement.get("success_metrics", []),
                "measurement_methods": improvement.get("measurement_methods", []),
                "success_criteria": improvement.get("success_criteria", [])
            }
        }
        return clear_analysis
    
    def start_build_phase(self, improvement_id: str, clear_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Start BUILD phase of improvement."""
        build_record = {
            "improvement_id": improvement_id,
            "phase": "BUILD",
            "started_at": datetime.now().isoformat(),
            "clear_analysis": clear_analysis,
            "status": "IN_PROGRESS",
            "implementation_steps": [],
            "alpha_evolve_layers": []
        }
        self.save_improvement(build_record)
        return build_record
    
    def complete_build_phase(self, improvement_id: str, implementation_details: Dict[str, Any]):
        """Complete BUILD phase and transition to MEASURE."""
        improvement = self.load_improvement(improvement_id)
        if improvement:
            improvement["build_completed_at"] = datetime.now().isoformat()
            improvement["implementation_details"] = implementation_details
            improvement["status"] = "MEASURING"
            self.save_improvement(improvement)
    
    def start_measure_phase(self, improvement_id: str) -> Dict[str, Any]:
        """Start MEASURE phase - collect metrics."""
        improvement = self.load_improvement(improvement_id)
        if not improvement:
            return None
        
        measure_record = {
            "improvement_id": improvement_id,
            "phase": "MEASURE",
            "started_at": datetime.now().isoformat(),
            "metrics": {
                "performance": {},
                "accuracy": {},
                "user_satisfaction": {},
                "cloud_parity": {}
            },
            "data_collected": []
        }
        
        improvement["measure_phase"] = measure_record
        improvement["status"] = "MEASURING"
        self.save_improvement(improvement)
        return measure_record
    
    def record_metric(self, improvement_id: str, metric_name: str, value: Any, category: str = "performance"):
        """Record a metric during MEASURE phase."""
        improvement = self.load_improvement(improvement_id)
        if improvement and "measure_phase" in improvement:
            if category not in improvement["measure_phase"]["metrics"]:
                improvement["measure_phase"]["metrics"][category] = {}
            improvement["measure_phase"]["metrics"][category][metric_name] = {
                "value": value,
                "recorded_at": datetime.now().isoformat()
            }
            self.save_improvement(improvement)
    
    def start_learn_phase(self, improvement_id: str) -> Dict[str, Any]:
        """Start LEARN phase - analyze results and generate learnings."""
        improvement = self.load_improvement(improvement_id)
        if not improvement:
            return None
        
        learn_record = {
            "improvement_id": improvement_id,
            "phase": "LEARN",
            "started_at": datetime.now().isoformat(),
            "analysis": {
                "what_worked": [],
                "what_didnt": [],
                "root_causes": [],
                "patterns": []
            },
            "learnings": [],
            "refinements": [],
            "next_cycle_adjustments": []
        }
        
        improvement["learn_phase"] = learn_record
        improvement["status"] = "LEARNING"
        self.save_improvement(improvement)
        return learn_record
    
    def record_learning(self, improvement_id: str, learning: str, category: str = "general"):
        """Record a learning from LEARN phase."""
        improvement = self.load_improvement(improvement_id)
        if improvement and "learn_phase" in improvement:
            learning_entry = {
                "learning": learning,
                "category": category,
                "recorded_at": datetime.now().isoformat()
            }
            improvement["learn_phase"]["learnings"].append(learning_entry)
            self.save_improvement(improvement)
            self.save_learning_to_log(learning_entry, improvement_id)
    
    def complete_cycle(self, improvement_id: str) -> Dict[str, Any]:
        """Complete full BML cycle."""
        improvement = self.load_improvement(improvement_id)
        if improvement:
            improvement["cycle_completed_at"] = datetime.now().isoformat()
            improvement["status"] = "COMPLETED"
            improvement["next_improvements"] = improvement.get("learn_phase", {}).get("next_cycle_adjustments", [])
            self.save_improvement(improvement)
        return improvement
    
    def load_improvement(self, improvement_id: str) -> Optional[Dict[str, Any]]:
        """Load improvement record."""
        if not self.improvements_path.exists():
            return None
        with open(self.improvements_path, 'r') as f:
            improvements = json.load(f)
        return improvements.get(improvement_id)
    
    def save_improvement(self, improvement: Dict[str, Any]):
        """Save improvement record."""
        if self.improvements_path.exists():
            with open(self.improvements_path, 'r') as f:
                improvements = json.load(f)
        else:
            improvements = {}
        
        improvements[improvement["improvement_id"]] = improvement
        
        with open(self.improvements_path, 'w') as f:
            json.dump(improvements, f, indent=2, default=str)
    
    def save_learning_to_log(self, learning_entry: Dict[str, Any], improvement_id: str):
        """Save learning to learnings log."""
        if self.learnings_path.exists():
            with open(self.learnings_path, 'r') as f:
                learnings = json.load(f)
        else:
            learnings = {"weekly_learnings": [], "monthly_synthesis": []}
        
        learning_entry["improvement_id"] = improvement_id
        learnings["weekly_learnings"].append(learning_entry)
        
        # Keep only last 100 learnings
        learnings["weekly_learnings"] = learnings["weekly_learnings"][-100:]
        
        with open(self.learnings_path, 'w') as f:
            json.dump(learnings, f, indent=2, default=str)
    
    def get_weekly_bml_summary(self) -> str:
        """Get summary of current week's BML cycle."""
        if not self.improvements_path.exists():
            return "No improvements tracked yet."
        
        with open(self.improvements_path, 'r') as f:
            improvements = json.load(f)
        
        this_week = datetime.now() - timedelta(days=7)
        recent_improvements = [
            imp for imp in improvements.values()
            if datetime.fromisoformat(imp.get("started_at", "2000-01-01")) >= this_week
        ]
        
        summary = f"📊 AIMCODE BML Cycle Summary (Last 7 Days)\n\n"
        summary += f"Total Improvements: {len(recent_improvements)}\n\n"
        
        by_phase = {"BUILD": 0, "MEASURE": 0, "LEARN": 0, "COMPLETED": 0}
        for imp in recent_improvements:
            phase = imp.get("status", "UNKNOWN")
            if phase in by_phase:
                by_phase[phase] += 1
        
        summary += "By Phase:\n"
        for phase, count in by_phase.items():
            summary += f"  {phase}: {count}\n"
        
        return summary


if __name__ == "__main__":
    import sys
    
    engine = AIMCODEImprovementEngine()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "summary":
            print(engine.get_weekly_bml_summary())
        else:
            print("Usage: python aimcode_improvement_engine.py summary")
    else:
        print(engine.get_weekly_bml_summary())



