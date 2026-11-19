#!/usr/bin/env python3
"""
Composite a simple athlete silhouette onto an IQ session visual.png / thumbnail.jpg
so the card matches the movement theme (bike / hike / walk / run).

  python3 scripts/add-iq-athlete-silhouette.py video-packages/rasun/<slug>
  python3 scripts/add-iq-athlete-silhouette.py --all

Reads package.json "card.silhouette" if set, else infers from slug:
  bikeIQ → cyclist, hikingIQ → hiker, walkingIQ → walker, runningIQ → runner

Does not change spoken scripts. Overwrites visual.png and thumbnail.jpg in place
(after writing *.pre-silhouette backups once).
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

REPO = Path(__file__).resolve().parents[1]
PKG_ROOT = REPO / "video-packages" / "rasun"


def infer_athlete(slug: str, card: dict) -> str:
    explicit = (card.get("silhouette") or "").strip().lower()
    if explicit in {"cyclist", "hiker", "walker", "runner"}:
        return explicit
    s = slug.lower()
    if "bike" in s:
        return "cyclist"
    if "hik" in s:
        return "hiker"
    if "run" in s:
        return "runner"
    if "walk" in s:
        return "walker"
    return "walker"


def _poly(draw: ImageDraw.ImageDraw, pts, fill):
    draw.polygon(pts, fill=fill)


def draw_cyclist(d: ImageDraw.ImageDraw, box, fill, s: float) -> None:
    x0, y0, x1, y1 = box
    cx = (x0 + x1) / 2
    cy = (y0 + y1) / 2 + 40 * s
    r = min(x1 - x0, y1 - y0) * 0.16
    # wheels
    for wx in (cx - 95 * s, cx + 95 * s):
        d.ellipse([wx - r, cy - r, wx + r, cy + r], outline=fill, width=max(3, int(5 * s)))
        d.ellipse([wx - r * 0.2, cy - r * 0.2, wx + r * 0.2, cy + r * 0.2], fill=fill)
    # frame
    d.line([(cx - 95 * s, cy), (cx - 10 * s, cy - 70 * s), (cx + 70 * s, cy - 55 * s), (cx + 95 * s, cy)], fill=fill, width=max(3, int(6 * s)))
    d.line([(cx - 10 * s, cy - 70 * s), (cx + 20 * s, cy), (cx + 95 * s, cy)], fill=fill, width=max(3, int(5 * s)))
    # rider
    head = (cx + 5 * s, cy - 130 * s)
    hr = 22 * s
    d.ellipse([head[0] - hr, head[1] - hr, head[0] + hr, head[1] + hr], fill=fill)
    _poly(d, [
        (cx - 25 * s, cy - 100 * s), (cx + 40 * s, cy - 105 * s),
        (cx + 55 * s, cy - 40 * s), (cx + 10 * s, cy - 20 * s),
        (cx - 40 * s, cy - 35 * s),
    ], fill)
    d.line([(cx + 10 * s, cy - 20 * s), (cx + 5 * s, cy + 5 * s)], fill=fill, width=max(4, int(8 * s)))  # leg
    d.line([(cx - 20 * s, cy - 40 * s), (cx - 50 * s, cy + 10 * s)], fill=fill, width=max(4, int(8 * s)))
    d.line([(cx + 40 * s, cy - 105 * s), (cx + 85 * s, cy - 70 * s)], fill=fill, width=max(3, int(6 * s)))  # arms to bars


def draw_hiker(d: ImageDraw.ImageDraw, box, fill, s: float) -> None:
    x0, y0, x1, y1 = box
    cx = (x0 + x1) / 2 + 20 * s
    base = y1 - 40 * s
    hr = 24 * s
    head_y = base - 280 * s
    d.ellipse([cx - hr, head_y - hr, cx + hr, head_y + hr], fill=fill)
    # torso + backpack
    _poly(d, [
        (cx - 28 * s, head_y + hr), (cx + 28 * s, head_y + hr),
        (cx + 36 * s, base - 140 * s), (cx - 36 * s, base - 140 * s),
    ], fill)
    _poly(d, [
        (cx + 28 * s, head_y + 20 * s), (cx + 70 * s, head_y + 30 * s),
        (cx + 65 * s, base - 150 * s), (cx + 30 * s, base - 145 * s),
    ], fill)
    # legs mid-stride
    d.line([(cx - 10 * s, base - 140 * s), (cx - 55 * s, base)], fill=fill, width=max(6, int(14 * s)))
    d.line([(cx + 10 * s, base - 140 * s), (cx + 50 * s, base - 10 * s)], fill=fill, width=max(6, int(14 * s)))
    # poles
    d.line([(cx - 70 * s, head_y + 40 * s), (cx - 90 * s, base)], fill=fill, width=max(2, int(4 * s)))
    d.line([(cx + 40 * s, head_y + 50 * s), (cx + 95 * s, base - 20 * s)], fill=fill, width=max(2, int(4 * s)))


def draw_walker(d: ImageDraw.ImageDraw, box, fill, s: float) -> None:
    x0, y0, x1, y1 = box
    cx = (x0 + x1) / 2
    base = y1 - 35 * s
    hr = 22 * s
    head_y = base - 270 * s
    d.ellipse([cx - hr, head_y - hr, cx + hr, head_y + hr], fill=fill)
    _poly(d, [
        (cx - 26 * s, head_y + hr), (cx + 26 * s, head_y + hr),
        (cx + 30 * s, base - 130 * s), (cx - 30 * s, base - 130 * s),
    ], fill)
    # walking legs
    d.line([(cx - 8 * s, base - 130 * s), (cx - 45 * s, base)], fill=fill, width=max(6, int(13 * s)))
    d.line([(cx + 8 * s, base - 130 * s), (cx + 55 * s, base - 5 * s)], fill=fill, width=max(6, int(13 * s)))
    # swinging arms
    d.line([(cx - 20 * s, head_y + 50 * s), (cx - 70 * s, base - 160 * s)], fill=fill, width=max(4, int(9 * s)))
    d.line([(cx + 20 * s, head_y + 50 * s), (cx + 65 * s, base - 150 * s)], fill=fill, width=max(4, int(9 * s)))


def draw_runner(d: ImageDraw.ImageDraw, box, fill, s: float) -> None:
    x0, y0, x1, y1 = box
    cx = (x0 + x1) / 2
    base = y1 - 30 * s
    hr = 20 * s
    head_y = base - 250 * s
    d.ellipse([cx - hr + 15 * s, head_y - hr, cx + hr + 15 * s, head_y + hr], fill=fill)
    # forward lean torso
    _poly(d, [
        (cx - 5 * s, head_y + hr), (cx + 45 * s, head_y + hr + 10 * s),
        (cx + 20 * s, base - 120 * s), (cx - 35 * s, base - 130 * s),
    ], fill)
    # stride
    d.line([(cx - 15 * s, base - 125 * s), (cx - 80 * s, base - 20 * s)], fill=fill, width=max(5, int(12 * s)))
    d.line([(cx + 5 * s, base - 120 * s), (cx + 90 * s, base)], fill=fill, width=max(5, int(12 * s)))
    d.line([(cx + 30 * s, head_y + 40 * s), (cx + 100 * s, base - 180 * s)], fill=fill, width=max(4, int(9 * s)))
    d.line([(cx - 10 * s, head_y + 45 * s), (cx - 70 * s, base - 170 * s)], fill=fill, width=max(4, int(9 * s)))


DRAWERS = {
    "cyclist": draw_cyclist,
    "hiker": draw_hiker,
    "walker": draw_walker,
    "runner": draw_runner,
}


def composite(path: Path, athlete: str, accent_rgb: tuple[int, int, int]) -> None:
    im = Image.open(path).convert("RGBA")
    W, H = im.size
    s = W / 1920
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    # Right-side motif box (matches make-iq-card layout)
    box = (int(1290 * s), int(220 * s), int(1740 * s), int(860 * s))
    if W <= 1400:  # thumbnail 1280x720 — tighter box
        box = (int(820 * s * (1920 / 1280)), int(160 * (H / 720)), int(1180 * (W / 1280)), int(600 * (H / 720)))
        box = (int(W * 0.62), int(H * 0.18), int(W * 0.95), int(H * 0.88))
    fill = (*accent_rgb, 210)
    DRAWERS[athlete](d, box, fill, s if W > 1400 else max(0.55, s))
    # Soft shadow under silhouette
    shadow = overlay.filter(ImageFilter.GaussianBlur(radius=max(2, int(4 * s))))
    out = Image.alpha_composite(im, shadow)
    out = Image.alpha_composite(out, overlay)
    if path.suffix.lower() in {".jpg", ".jpeg"}:
        out.convert("RGB").save(path, quality=92)
    else:
        out.convert("RGB").save(path)
    print(f"  + {athlete} → {path.relative_to(REPO)}")


def theme_accent(theme: str) -> tuple[int, int, int]:
    # Keep in sync with make-iq-card THEMES accent column
    accents = {
        "forest": (236, 168, 72),
        "dusk": (240, 128, 82),
        "teal": (250, 196, 84),
        "night": (255, 206, 102),
        "sunrise": (255, 176, 64),
        "ember": (255, 122, 92),
        "navy": (232, 104, 42),
    }
    return accents.get(theme, (236, 180, 90))


def process_slug(slug: str) -> int:
    d = PKG_ROOT / slug
    pkg_path = d / "package.json"
    if not pkg_path.exists():
        print(f"skip {slug}: no package.json", file=sys.stderr)
        return 1
    pkg = json.loads(pkg_path.read_text(encoding="utf-8"))
    card = pkg.get("card") or {}
    athlete = infer_athlete(slug, card)
    theme = card.get("theme") or ("navy" if "bike" in slug else "teal")
    accent = theme_accent(theme)
    # Persist silhouette choice for regenerations
    if "card" not in pkg or pkg["card"] is None:
        if "bike" in slug:
            pkg["card"] = {
                "theme": "navy",
                "motif": "wheel",
                "silhouette": "cyclist",
                "kicker": "bikeIQ  ·  1 HOUR GUIDED RIDE",
                "line1": "BREATHE EVERY",
                "line2": "5 PEDALS",
                "sub": ["In for 5 pedals. Out for 5 pedals."],
                "thumb": ["BREATHE", "EVERY", "5 PEDALS"],
            }
        else:
            pkg["card"] = card
    else:
        pkg["card"]["silhouette"] = athlete
    pkg_path.write_text(json.dumps(pkg, indent=2) + "\n", encoding="utf-8")

    for name in ("visual.png", "thumbnail.jpg"):
        path = d / name
        if not path.exists():
            print(f"  missing {path}", file=sys.stderr)
            continue
        bak = path.with_suffix(path.suffix + ".pre-silhouette")
        if not bak.exists():
            bak.write_bytes(path.read_bytes())
        composite(path, athlete, accent)
    print(f"{slug}: {athlete}")
    return 0


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print("Usage: add-iq-athlete-silhouette.py <slug>|--all", file=sys.stderr)
        return 2
    if args == ["--all"]:
        slugs = sorted(
            p.name for p in PKG_ROOT.iterdir()
            if p.is_dir() and (p / "package.json").exists() and (p / "visual.png").exists()
            and "beasley" not in p.name
        )
    else:
        slugs = args
    rc = 0
    for slug in slugs:
        rc = process_slug(slug) or rc
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
