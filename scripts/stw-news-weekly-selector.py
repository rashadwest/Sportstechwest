#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple
from urllib.parse import urlparse


def _slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return re.sub(r"-{2,}", "-", s)[:54] or "story"


def _canonical_url(u: str) -> str:
    u = u.strip()
    if not u:
        return u
    for token in ("?utm_", "&utm_", "?ref=", "&ref=", "?fbclid=", "&fbclid="):
        idx = u.find(token)
        if idx != -1:
            u = u[:idx]
    return u.rstrip("/")


def _load_recent_candidates(out_dir: Path, lookback_days: int) -> List[Dict[str, Any]]:
    today = datetime.now(timezone.utc).date()
    rows: List[Dict[str, Any]] = []
    for i in range(lookback_days):
        d = (today - timedelta(days=i)).isoformat()
        p = out_dir / f"daily-{d}.jsonl"
        if not p.exists():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                obj["url"] = _canonical_url(str(obj.get("url", "")))
                rows.append(obj)
            except Exception:
                continue
    return rows


def _dedupe_rank(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen: set[str] = set()
    ranked: List[Dict[str, Any]] = []
    for row in sorted(rows, key=lambda x: float(x.get("score", 0.0)), reverse=True):
        key = row.get("url") or row.get("title", "")
        if not key or key in seen:
            continue
        seen.add(key)
        ranked.append(row)
    return ranked


def _next_week_slots(today: date) -> List[date]:
    # Monday, Tuesday, Thursday, Friday of upcoming week.
    days_ahead = 7 - today.weekday() if today.weekday() != 0 else 7
    monday = today + timedelta(days=days_ahead)
    return [monday, monday + timedelta(days=1), monday + timedelta(days=3), monday + timedelta(days=4)]


def _write_shortlist(path: Path, ranked: List[Dict[str, Any]], top_n: int) -> None:
    lines = [
        f"# STW News Weekly Shortlist ({datetime.now().date().isoformat()})",
        "",
        "## Recommended Top Stories",
        "",
    ]
    for idx, row in enumerate(ranked[:top_n], start=1):
        slug = _slugify(row.get("title", "story"))
        lines += [
            f"### {idx}. {row.get('title','(untitled)')}",
            f"- Score: {row.get('score', 0)}",
            f"- Slug: `{slug}`",
            f"- Source: {row.get('source','')} ({row.get('domain','')})",
            f"- URL: {row.get('url','')}",
            f"- Reasons: {', '.join(row.get('reasons', [])) or 'n/a'}",
            "",
        ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def _update_queue(queue_path: Path, selected: List[Tuple[date, str]]) -> None:
    existing: Dict[str, str] = {}
    if queue_path.exists():
        reader = csv.DictReader(queue_path.read_text(encoding="utf-8").splitlines())
        for row in reader:
            d = (row.get("date") or "").strip()
            story = (row.get("story") or "").strip()
            if d:
                existing[d] = story
    for d, slug in selected:
        existing[d.isoformat()] = slug
    rows = [{"date": k, "story": v} for k, v in sorted(existing.items())]
    queue_path.parent.mkdir(parents=True, exist_ok=True)
    with queue_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date", "story"])
        w.writeheader()
        w.writerows(rows)


def _stub_story(package_root: Path, slug: str, row: Dict[str, Any]) -> None:
    story_dir = package_root / slug
    story_dir.mkdir(parents=True, exist_ok=True)
    article_url = row.get("url", "")
    domain = row.get("domain", "")
    company_url = f"https://{domain}/" if domain else "https://example.com/"
    title = row.get("title", f"{slug.replace('-', ' ').title()} | Sportstechwest")
    summary = row.get("summary", "Quick sportstech update in about 1 minute.")

    files = {
        "article-url.txt": article_url + "\n",
        "company-url.txt": company_url + "\n",
        "source.txt": f"{row.get('source','news feed')}\n",
        "story-name.txt": title + "\n",
        "script-elevenlabs.txt": (
            f"{title}.\n\n{summary}\n\n"
            "Why this matters: this story shows how sports innovation is moving from hype to practical tools for athletes and teams.\n\n"
            "That's STW News. More next time.\n"
        ),
        "short.md": (
            f"# STW News — {title}\n\n"
            f"> {summary}\n\n"
            "## Spec\n\n"
            "- **series**: STW News\n"
            f"- **story**: {title}\n"
            "- **duration_seconds**: ~60\n"
            "- **format**: Voiceover (ElevenLabs) over article + company scroll\n"
            "- **brand**: STW News opener; Sportstechwest logo corner\n"
        ),
        "youtube-test.txt": (
            f"{title} | Sportstechwest\n\n"
            f"{summary}\n\n"
            "#STWNews #sportstech #innovation #training #sportstechwest\n\n"
            "— Sportstechwest\n\n"
            "TAGS (paste into YouTube Studio → Tags):\n"
            "STW News, sportstech, sports innovation, AI, wearables, training, Sportstechwest\n"
        ),
    }
    for name, content in files.items():
        p = story_dir / name
        if not p.exists():
            p.write_text(content, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description="Sunday STW News selector and queue writer")
    ap.add_argument("--out-dir", default="output/stw-news-scout")
    ap.add_argument("--queue", default="_data/stw_news_queue.csv")
    ap.add_argument("--package-root", default="shorts-packages/stw-news-2026-01")
    ap.add_argument("--lookback-days", type=int, default=7)
    ap.add_argument("--top", type=int, default=4)
    ap.add_argument("--backups", type=int, default=2)
    ap.add_argument("--write-queue", action="store_true")
    ap.add_argument("--create-stubs", action="store_true")
    args = ap.parse_args()

    repo = Path(__file__).resolve().parents[1]
    out_dir = repo / args.out_dir
    rows = _load_recent_candidates(out_dir, args.lookback_days)
    ranked = _dedupe_rank(rows)
    if not ranked:
        raise SystemExit("No scout candidates found. Run stw-news-scout.py first.")

    shortlist_md = out_dir / f"weekly-shortlist-{datetime.now().date().isoformat()}.md"
    _write_shortlist(shortlist_md, ranked, args.top + args.backups)

    slots = _next_week_slots(datetime.now().date())
    selected_rows = ranked[: args.top]
    selected: List[Tuple[date, str]] = []
    for d, row in zip(slots, selected_rows):
        slug = _slugify(row.get("title", "story"))
        selected.append((d, slug))
        if args.create_stubs:
            _stub_story(repo / args.package_root, slug, row)

    if args.write_queue:
        _update_queue(repo / args.queue, selected)

    print(f"Wrote shortlist: {shortlist_md}")
    for d, slug in selected:
        print(f"{d.isoformat()} -> {slug}")


if __name__ == "__main__":
    main()
