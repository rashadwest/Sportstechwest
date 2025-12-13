#!/usr/bin/env python3
"""BallCODE Release Validation (Pre-flight Gates)

Runs the validation gates defined in:
- documents/VALIDATION-GATES-AND-ESCALATION.md

This script is designed to be called by humans or automation (n8n).

Copyright © 2025 Rashad West. All Rights Reserved.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests

PROJECT_ROOT = Path(__file__).parent.parent
DEFAULT_PACKET = PROJECT_ROOT / "documents" / "BOOK-PACKET-TEMPLATE.json"
CURRICULUM_SCHEMA = PROJECT_ROOT / "curriculum-schema.json"
LEVELS_DIR = PROJECT_ROOT / "Unity-Scripts" / "Levels"
WEBSITE_INDEX = PROJECT_ROOT / "BallCode" / "index.html"

SUCCESS_NETLIFY_STATES = {"ready", "published"}


@dataclass
class CheckResult:
    name: str
    ok: bool
    severity: str  # PASS | WARN | FAIL
    message: str


def _load_json_file(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _get_nested(d: Dict[str, Any], path: List[str]) -> Any:
    cur: Any = d
    for key in path:
        if not isinstance(cur, dict) or key not in cur:
            return None
        cur = cur[key]
    return cur


def check_book_packet(packet_path: Path) -> Tuple[Optional[Dict[str, Any]], List[CheckResult]]:
    results: List[CheckResult] = []

    if not packet_path.exists():
        results.append(
            CheckResult(
                name="BookPacket",
                ok=False,
                severity="FAIL",
                message=f"Book packet not found: {packet_path}",
            )
        )
        return None, results

    try:
        packet = _load_json_file(packet_path)
    except Exception as e:
        results.append(
            CheckResult(
                name="BookPacket",
                ok=False,
                severity="FAIL",
                message=f"Book packet invalid JSON: {e}",
            )
        )
        return None, results

    if not isinstance(packet, dict):
        results.append(
            CheckResult(
                name="BookPacket",
                ok=False,
                severity="FAIL",
                message="Book packet JSON must be an object",
            )
        )
        return None, results

    required_paths = [
        ["packet_version"],
        ["book", "book_number"],
        ["book", "title"],
        ["book", "description"],
        ["book", "grade_bands"],
        ["commerce", "channel_priority"],
    ]

    missing: List[str] = []
    for p in required_paths:
        v = _get_nested(packet, p)
        if v is None or (isinstance(v, str) and not v.strip()):
            missing.append(".".join(p))

    if missing:
        results.append(
            CheckResult(
                name="BookPacket",
                ok=False,
                severity="FAIL",
                message=f"Missing required fields: {', '.join(missing)}",
            )
        )
        return packet, results

    results.append(
        CheckResult(
            name="BookPacket",
            ok=True,
            severity="PASS",
            message=f"Book packet OK: {packet_path.name}",
        )
    )
    return packet, results


def check_assets(packet: Dict[str, Any], packet_path: Path) -> List[CheckResult]:
    results: List[CheckResult] = []

    assets = packet.get("assets") if isinstance(packet.get("assets"), dict) else {}
    if not assets:
        results.append(
            CheckResult(
                name="Assets",
                ok=True,
                severity="WARN",
                message="No assets section provided (will rely on fallbacks).",
            )
        )
        return results

    base_dir = packet_path.parent
    for key in ["thumbnail_path", "video_path"]:
        val = assets.get(key)
        if not val:
            continue

        p = Path(val)
        if not p.is_absolute():
            p = (base_dir / p).resolve()

        if not p.exists():
            results.append(
                CheckResult(
                    name="Assets",
                    ok=False,
                    severity="FAIL",
                    message=f"Missing asset for {key}: {p}",
                )
            )
            return results

    results.append(
        CheckResult(
            name="Assets",
            ok=True,
            severity="PASS",
            message="Assets OK (all referenced paths exist).",
        )
    )
    return results


def check_curriculum_schema() -> List[CheckResult]:
    if not CURRICULUM_SCHEMA.exists():
        return [
            CheckResult(
                name="CurriculumSchema",
                ok=False,
                severity="FAIL",
                message=f"Missing curriculum schema: {CURRICULUM_SCHEMA}",
            )
        ]

    try:
        _load_json_file(CURRICULUM_SCHEMA)
    except Exception as e:
        return [
            CheckResult(
                name="CurriculumSchema",
                ok=False,
                severity="FAIL",
                message=f"Curriculum schema invalid JSON: {e}",
            )
        ]

    return [
        CheckResult(
            name="CurriculumSchema",
            ok=True,
            severity="PASS",
            message="Curriculum schema exists and is valid JSON.",
        )
    ]


def _find_level_file(level_id: str) -> Optional[Path]:
    if not LEVELS_DIR.exists():
        return None
    matches = list(LEVELS_DIR.rglob(f"{level_id}.json"))
    return matches[0] if matches else None


def check_game_levels(packet: Dict[str, Any]) -> List[CheckResult]:
    game = packet.get("game") if isinstance(packet.get("game"), dict) else {}
    levels = game.get("levels") if isinstance(game.get("levels"), list) else []

    if not levels:
        return [
            CheckResult(
                name="GameLevels",
                ok=True,
                severity="WARN",
                message="No game.levels provided in packet (book can publish, but deep links may be incomplete).",
            )
        ]

    missing: List[str] = []
    for lvl in levels:
        if not isinstance(lvl, dict):
            continue
        level_id = str(lvl.get("level_id", "")).strip()
        if not level_id:
            continue
        if _find_level_file(level_id) is None:
            missing.append(level_id)

    if missing:
        return [
            CheckResult(
                name="GameLevels",
                ok=False,
                severity="FAIL",
                message=f"Missing level JSON for level_id(s): {', '.join(missing)}",
            )
        ]

    return [
        CheckResult(
            name="GameLevels",
            ok=True,
            severity="PASS",
            message="All referenced level_id JSON files found.",
        )
    ]


def check_website_files() -> List[CheckResult]:
    if not WEBSITE_INDEX.exists():
        return [
            CheckResult(
                name="Website",
                ok=False,
                severity="FAIL",
                message=f"Missing website index: {WEBSITE_INDEX}",
            )
        ]

    return [
        CheckResult(
            name="Website",
            ok=True,
            severity="PASS",
            message="Website index exists.",
        )
    ]


def _check_github_latest_run() -> Tuple[bool, str]:
    token = os.getenv("GITHUB_TOKEN", "")
    owner = os.getenv("GITHUB_REPO_OWNER", "")
    repo = os.getenv("GITHUB_REPO_NAME", "")
    workflow = os.getenv("GITHUB_WORKFLOW_FILE", "")

    if not all([token, owner, repo, workflow]):
        return False, "Missing GitHub env vars (GITHUB_TOKEN, GITHUB_REPO_OWNER, GITHUB_REPO_NAME, GITHUB_WORKFLOW_FILE)"

    url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow}/runs"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    r = requests.get(url, headers=headers, params={"per_page": 1}, timeout=10)
    r.raise_for_status()
    data = r.json()
    runs = data.get("workflow_runs", [])
    if not runs:
        return False, "No workflow runs found"

    latest = runs[0]
    status = latest.get("status")
    conclusion = latest.get("conclusion")
    html_url = latest.get("html_url", "")

    if status == "completed" and conclusion == "success":
        return True, f"GitHub OK (latest run success): {html_url}"

    return False, f"GitHub not healthy (status={status}, conclusion={conclusion}): {html_url}"


def _check_netlify_latest_deploy() -> Tuple[bool, str]:
    token = os.getenv("NETLIFY_AUTH_TOKEN", "")
    site_id = os.getenv("NETLIFY_SITE_ID", "")

    if not all([token, site_id]):
        return False, "Missing Netlify env vars (NETLIFY_AUTH_TOKEN, NETLIFY_SITE_ID)"

    url = f"https://api.netlify.com/api/v1/sites/{site_id}/deploys"
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(url, headers=headers, params={"per_page": 1}, timeout=10)
    r.raise_for_status()
    deploys = r.json()
    if not deploys:
        return False, "No Netlify deploys found"

    latest = deploys[0]
    state = latest.get("state", "unknown")
    deploy_url = latest.get("deploy_url", "")

    if state in SUCCESS_NETLIFY_STATES:
        return True, f"Netlify OK (latest deploy {state}): {deploy_url}"

    return False, f"Netlify not healthy (state={state}): {deploy_url}"


def check_build_deploy_health() -> List[CheckResult]:
    # If we cannot check due to missing credentials, WARN (do not block automation by default).
    try:
        gh_ok, gh_msg = _check_github_latest_run()
    except Exception as e:
        return [
            CheckResult(
                name="BuildDeploy",
                ok=True,
                severity="WARN",
                message=f"GitHub check unavailable: {e}",
            )
        ]

    try:
        nf_ok, nf_msg = _check_netlify_latest_deploy()
    except Exception as e:
        return [
            CheckResult(
                name="BuildDeploy",
                ok=True,
                severity="WARN",
                message=f"Netlify check unavailable: {e}",
            )
        ]

    if gh_ok and nf_ok:
        return [
            CheckResult(
                name="BuildDeploy",
                ok=True,
                severity="PASS",
                message=f"{gh_msg} | {nf_msg}",
            )
        ]

    return [
        CheckResult(
            name="BuildDeploy",
            ok=False,
            severity="FAIL",
            message=f"{gh_msg} | {nf_msg}",
        )
    ]


def check_telemetry_backend(require_telemetry: bool) -> List[CheckResult]:
    # Minimal gate for now: allow automation to proceed unless telemetry is required.
    ready_flag = os.getenv("SUPABASE_SCHEMA_READY", "")

    if ready_flag == "1":
        return [
            CheckResult(
                name="TelemetryBackend",
                ok=True,
                severity="PASS",
                message="Telemetry backend marked ready (SUPABASE_SCHEMA_READY=1).",
            )
        ]

    if require_telemetry:
        return [
            CheckResult(
                name="TelemetryBackend",
                ok=False,
                severity="FAIL",
                message="Telemetry required but backend not marked ready (set SUPABASE_SCHEMA_READY=1 after applying DB schema fix).",
            )
        ]

    return [
        CheckResult(
            name="TelemetryBackend",
            ok=True,
            severity="WARN",
            message="Telemetry backend not confirmed ready (set SUPABASE_SCHEMA_READY=1 when Supabase schema is fixed).",
        )
    ]


def run_checks(packet_path: Path, require_telemetry: bool) -> Tuple[bool, List[CheckResult]]:
    all_results: List[CheckResult] = []

    packet, res = check_book_packet(packet_path)
    all_results.extend(res)
    if packet is None or any(r.severity == "FAIL" for r in res):
        return False, all_results

    all_results.extend(check_assets(packet, packet_path))
    all_results.extend(check_curriculum_schema())
    all_results.extend(check_game_levels(packet))
    all_results.extend(check_website_files())
    all_results.extend(check_build_deploy_health())
    all_results.extend(check_telemetry_backend(require_telemetry))

    ok = all(r.severity != "FAIL" for r in all_results)
    return ok, all_results


def main() -> int:
    parser = argparse.ArgumentParser(description="BallCODE release validation (pre-flight gates)")
    parser.add_argument(
        "--packet",
        default=str(DEFAULT_PACKET),
        help=f"Path to book packet JSON (default: {DEFAULT_PACKET})",
    )
    parser.add_argument(
        "--require-telemetry",
        action="store_true",
        help="Fail if telemetry backend is not confirmed ready.",
    )

    args = parser.parse_args()
    packet_path = Path(args.packet)

    ok, results = run_checks(packet_path, require_telemetry=args.require_telemetry)

    print("=" * 70)
    print("BALLCODE RELEASE VALIDATION")
    print("=" * 70)

    for r in results:
        status = "PASS" if r.severity == "PASS" else ("WARN" if r.severity == "WARN" else "FAIL")
        print(f"{status:<4} | {r.name:<16} | {r.message}")

    print("=" * 70)

    if ok:
        print("RESULT: PASS (no FAIL gates)")
        return 0

    print("RESULT: FAIL (one or more FAIL gates)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
