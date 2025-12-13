#!/usr/bin/env python3
"""Update n8n workflow scheduleTrigger to hourly.

This repo uses scheduleTrigger nodes configured via cronExpression.
We standardize to: "0 * * * *" (hourly).

Usage:
  python3 scripts/update-n8n-schedule.py \
    --workflow /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/n8n-unity-automation-workflow-FINAL-WORKING.json

Copyright © 2025 Rashad West. All Rights Reserved.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List


def load_json(path: Path) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("Workflow JSON must be an object")
    return data


def save_json(path: Path, data: Dict[str, Any]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def update_schedule_to_hourly(workflow: Dict[str, Any]) -> int:
    nodes = workflow.get("nodes", [])
    if not isinstance(nodes, list):
        raise ValueError("Workflow JSON missing 'nodes' list")

    updated = 0
    for node in nodes:
        if not isinstance(node, dict):
            continue
        if node.get("type") != "n8n-nodes-base.scheduleTrigger":
            continue

        params = node.setdefault("parameters", {})
        if not isinstance(params, dict):
            continue
        rule = params.setdefault("rule", {})
        if not isinstance(rule, dict):
            continue

        # Standardize to cronExpression hourly.
        rule.pop("interval", None)
        if rule.get("cronExpression") != "0 * * * *":
            rule["cronExpression"] = "0 * * * *"
            updated += 1

        # Update display name if present
        if isinstance(node.get("name"), str) and "Hourly" not in node.get("name"):
            node["name"] = "Scheduled Trigger (Hourly)"

    return updated


def main() -> int:
    parser = argparse.ArgumentParser(description="Set n8n scheduleTrigger to hourly")
    parser.add_argument(
        "--workflow",
        required=True,
        help="Path to n8n workflow JSON file",
    )

    args = parser.parse_args()
    workflow_path = Path(args.workflow)
    if not workflow_path.exists():
        raise FileNotFoundError(f"Workflow not found: {workflow_path}")

    wf = load_json(workflow_path)
    updated = update_schedule_to_hourly(wf)
    save_json(workflow_path, wf)

    print(f"Updated scheduleTrigger nodes: {updated}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
