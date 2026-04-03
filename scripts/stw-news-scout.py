#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List
from urllib.parse import urlparse
from urllib.request import urlopen
import xml.etree.ElementTree as ET


def _now_utc() -> datetime:
    return datetime.now(timezone.utc)


def _safe_text(node: ET.Element | None) -> str:
    if node is None or node.text is None:
        return ""
    return node.text.strip()


def _parse_pub_date(item: ET.Element) -> datetime | None:
    for tag in ("pubDate", "updated", "published"):
        n = item.find(tag)
        if n is not None and n.text:
            txt = n.text.strip()
            for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ"):
                try:
                    dt = datetime.strptime(txt, fmt)
                    return dt.astimezone(timezone.utc)
                except Exception:
                    continue
    return None


def _hours_ago(dt: datetime | None, now: datetime) -> float:
    if dt is None:
        return 240.0
    return max(0.0, (now - dt).total_seconds() / 3600.0)


def _clean_text(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def _score_story(
    title: str,
    summary: str,
    source_authority: float,
    hours_old: float,
    weights: Dict[str, float],
    keyword_boosts: Dict[str, float],
    brand_boosts: Dict[str, float],
) -> Dict[str, Any]:
    text = f"{title} {summary}".lower()
    recency = max(0.0, 10.0 - min(hours_old / 12.0, 10.0))
    brand = 0.0
    for k, v in brand_boosts.items():
        if k in text:
            brand += float(v)
    brand = min(10.0, brand / 2.0)
    athlete = 2.0
    for token in ("athlete", "team", "coach", "training", "performance", "player", "sport"):
        if token in text:
            athlete += 1.3
    athlete = min(10.0, athlete)
    clarity = 9.0 if len(title) <= 95 else 6.0
    kw = 0.0
    reasons: List[str] = []
    for k, v in keyword_boosts.items():
        if k in text:
            kw += float(v)
            reasons.append(f"keyword:{k}")
    authority = max(0.0, min(10.0, source_authority))
    score = (
        authority * weights.get("sourceAuthority", 0.26)
        + recency * weights.get("recency", 0.24)
        + brand * weights.get("brandStrength", 0.2)
        + athlete * weights.get("athleteRelevance", 0.2)
        + clarity * weights.get("headlineClarity", 0.1)
    ) * 10.0
    score += min(12.0, kw / 3.0)
    return {"score": round(score, 2), "reasons": reasons}


def _fetch_source(source: Dict[str, Any], cfg: Dict[str, Any], now: datetime) -> List[Dict[str, Any]]:
    url = source["url"]
    out: List[Dict[str, Any]] = []
    with urlopen(url, timeout=20) as resp:
        raw = resp.read()
    root = ET.fromstring(raw)
    items = root.findall(".//item")
    if not items:
        items = root.findall(".//entry")

    for item in items[:30]:
        title = _safe_text(item.find("title"))
        link = _safe_text(item.find("link"))
        if not link:
            link_node = item.find("link")
            if link_node is not None and "href" in link_node.attrib:
                link = link_node.attrib["href"].strip()
        summary = _safe_text(item.find("description")) or _safe_text(item.find("summary"))
        if not title or not link:
            continue
        published_at = _parse_pub_date(item)
        hours_old = _hours_ago(published_at, now)
        scored = _score_story(
            title=title,
            summary=summary,
            source_authority=float(source.get("sourceAuthority", 6)),
            hours_old=hours_old,
            weights=cfg.get("weights", {}),
            keyword_boosts=cfg.get("keywordBoosts", {}),
            brand_boosts=cfg.get("brandBoosts", {}),
        )
        domain = urlparse(link).netloc.lower()
        out.append(
            {
                "fetched_at": now.isoformat(),
                "source": source.get("name", ""),
                "source_url": url,
                "domain": domain,
                "title": _clean_text(title),
                "url": link.strip(),
                "summary": _clean_text(summary)[:420],
                "published_at": published_at.isoformat() if published_at else "",
                "hours_old": round(hours_old, 2),
                "score": scored["score"],
                "reasons": scored["reasons"],
            }
        )
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Daily STW News story scout")
    ap.add_argument("--config", default="config/stw-news-scout-sources.json")
    ap.add_argument("--out-dir", default="output/stw-news-scout")
    ap.add_argument("--top", type=int, default=20)
    args = ap.parse_args()

    repo = Path(__file__).resolve().parents[1]
    cfg = json.loads((repo / args.config).read_text(encoding="utf-8"))
    out_dir = repo / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    now = _now_utc()
    rows: List[Dict[str, Any]] = []
    errors: List[str] = []
    for source in cfg.get("sources", []):
        try:
            rows.extend(_fetch_source(source, cfg, now))
        except Exception as e:
            errors.append(f"{source.get('name','unknown')}: {e}")

    rows.sort(key=lambda x: x.get("score", 0.0), reverse=True)
    day = now.date().isoformat()
    daily_path = out_dir / f"daily-{day}.jsonl"
    with daily_path.open("a", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=True) + "\n")

    top_path = out_dir / "latest-top.json"
    top_payload = {"generated_at": now.isoformat(), "count": len(rows), "errors": errors, "top": rows[: args.top]}
    top_path.write_text(json.dumps(top_payload, indent=2), encoding="utf-8")
    print(f"Wrote {len(rows)} items to {daily_path}")
    if errors:
        print("Source errors:")
        for err in errors:
            print(f"- {err}")


if __name__ == "__main__":
    main()
