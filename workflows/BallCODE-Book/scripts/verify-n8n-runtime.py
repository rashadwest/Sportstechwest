#!/usr/bin/env python3
"""Verify Raspberry Pi n8n is running and executing workflows.

This is the "trust but verify" check for launch.

It verifies:
- n8n health endpoint reachable
- (if authenticated) fetch workflow list, find BallCODE/Unity workflow, confirm active
- (if authenticated) fetch recent executions and show last execution timestamp

Auth methods supported:
- N8N_API_KEY (header: X-N8N-API-KEY)
- N8N_BASIC_AUTH (user:pass)

Env:
- N8N_URL (e.g. http://192.168.1.226:5678)
- N8N_API_KEY (optional)
- N8N_BASIC_AUTH (optional)

Exit codes:
- 0: OK
- 2: n8n unreachable
- 3: API unauthorized (need key/auth to verify executions)
- 4: workflow not found
- 5: workflow inactive
- 6: no executions found

Copyright © 2025 Rashad West. All Rights Reserved.
"""

from __future__ import annotations

import os
import sys
from datetime import datetime, timezone, timedelta
from typing import Any, Dict, Optional, Tuple

import requests


def _headers() -> Dict[str, str]:
    headers: Dict[str, str] = {"Content-Type": "application/json"}
    api_key = os.getenv("N8N_API_KEY", "").strip()
    if api_key:
        headers["X-N8N-API-KEY"] = api_key
    return headers


def _auth() -> Optional[Tuple[str, str]]:
    basic = os.getenv("N8N_BASIC_AUTH", "").strip()
    if not basic:
        return None
    if ":" not in basic:
        return None
    user, pwd = basic.split(":", 1)
    return user, pwd


def check_health(n8n_url: str) -> bool:
    try:
        r = requests.get(f"{n8n_url}/healthz", timeout=5)
        return r.status_code == 200
    except Exception:
        return False


def get_workflows(n8n_url: str) -> Tuple[bool, Any, str]:
    try:
        r = requests.get(
            f"{n8n_url}/api/v1/workflows",
            headers=_headers(),
            auth=_auth(),
            timeout=10,
        )
        if r.status_code in (401, 403):
            return False, None, "unauthorized"
        r.raise_for_status()
        return True, r.json(), "ok"
    except Exception as e:
        return False, None, str(e)


def find_workflow_id(workflows_payload: Any) -> Optional[str]:
    if not isinstance(workflows_payload, dict):
        return None
    items = workflows_payload.get("data")
    if not isinstance(items, list):
        return None

    for wf in items:
        if not isinstance(wf, dict):
            continue
        name = str(wf.get("name", "")).lower()
        if "unity" in name or "ballcode" in name:
            return str(wf.get("id", "")).strip() or None

    return None


def get_workflow_detail(n8n_url: str, workflow_id: str) -> Tuple[bool, Any, str]:
    try:
        r = requests.get(
            f"{n8n_url}/api/v1/workflows/{workflow_id}",
            headers=_headers(),
            auth=_auth(),
            timeout=10,
        )
        if r.status_code in (401, 403):
            return False, None, "unauthorized"
        r.raise_for_status()
        return True, r.json(), "ok"
    except Exception as e:
        return False, None, str(e)


def get_executions(n8n_url: str, workflow_id: str, limit: int = 10) -> Tuple[bool, Any, str]:
    try:
        r = requests.get(
            f"{n8n_url}/api/v1/executions",
            params={"workflowId": workflow_id, "limit": limit},
            headers=_headers(),
            auth=_auth(),
            timeout=10,
        )
        if r.status_code in (401, 403):
            return False, None, "unauthorized"
        r.raise_for_status()
        return True, r.json(), "ok"
    except Exception as e:
        return False, None, str(e)


def _parse_iso(dt: str) -> Optional[datetime]:
    if not dt:
        return None
    try:
        return datetime.fromisoformat(dt.replace("Z", "+00:00")).astimezone(timezone.utc)
    except Exception:
        return None


def main() -> int:
    n8n_url = os.getenv("N8N_URL", "http://localhost:5678").strip()

    print("VERIFY N8N RUNTIME")
    print("=" * 70)
    print(f"N8N_URL: {n8n_url}")

    if not check_health(n8n_url):
        print("FAIL: n8n healthz not reachable")
        print("- Check Raspberry Pi is online and n8n service is running")
        return 2

    print("OK: n8n healthz reachable")

    ok, workflows, msg = get_workflows(n8n_url)
    if not ok and msg == "unauthorized":
        print("WARN: n8n API unauthorized (cannot verify executions)")
        print("- Set N8N_API_KEY in .n8n-env (recommended) OR set N8N_BASIC_AUTH=user:pass")
        return 3
    if not ok:
        print(f"FAIL: could not fetch workflows ({msg})")
        return 3

    wf_id = find_workflow_id(workflows)
    if not wf_id:
        print("FAIL: could not find BallCODE/Unity workflow in n8n")
        return 4

    print(f"OK: found workflow id: {wf_id}")

    ok, wf_detail, msg = get_workflow_detail(n8n_url, wf_id)
    if not ok and msg == "unauthorized":
        print("WARN: cannot read workflow details (unauthorized)")
        return 3
    if not ok:
        print(f"FAIL: could not fetch workflow detail ({msg})")
        return 3

    active = bool(wf_detail.get("active")) if isinstance(wf_detail, dict) else None
    name = wf_detail.get("name") if isinstance(wf_detail, dict) else None
    print(f"Workflow: {name} | active={active}")

    if active is False:
        print("FAIL: workflow is not active (toggle ON in n8n UI)")
        return 5

    ok, execs, msg = get_executions(n8n_url, wf_id, limit=10)
    if not ok and msg == "unauthorized":
        print("WARN: cannot fetch executions (unauthorized)")
        return 3
    if not ok:
        print(f"FAIL: could not fetch executions ({msg})")
        return 3

    executions = execs.get("data") if isinstance(execs, dict) else None
    if not isinstance(executions, list) or len(executions) == 0:
        print("FAIL: no executions found for workflow")
        return 6

    latest = executions[0] if isinstance(executions[0], dict) else {}
    started_at = _parse_iso(str(latest.get("startedAt", "")))
    stopped_at = _parse_iso(str(latest.get("stoppedAt", "")))
    finished = bool(latest.get("finished"))

    print("Latest execution:")
    print(f"- startedAt: {latest.get('startedAt')}")
    print(f"- stoppedAt: {latest.get('stoppedAt')}")
    print(f"- finished: {finished}")

    if started_at:
        age = datetime.now(timezone.utc) - started_at
        print(f"- age: {age}")
        # Hourly expectation: give a 2 hour tolerance.
        if age > timedelta(hours=2):
            print("WARN: last execution is older than 2 hours (schedule may not be firing)")

    print("RESULT: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


