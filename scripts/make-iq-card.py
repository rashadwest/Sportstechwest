#!/usr/bin/env python3
"""
Draw an IQ session's video card (visual.png, 1920x1080) and thumbnail (thumbnail.jpg, 1280x720)
from the "card" block in its package.json, so every episode gets its own look.

  python3 scripts/make-iq-card.py video-packages/rasun/<slug>

package.json "card":
  {
    "theme":   "forest" | "dusk" | "teal" | "night" | "sunrise" | "ember",
    "motif":   "contours" | "switchback" | "senses" | "streetlights" | "sunrise" | "rings",
    "kicker":  "hikingIQ · 1 HOUR GUIDED HIKE",
    "line1":   "HEEL-TOE",
    "line2":   "GROUNDING",
    "sub":     ["In for 3 steps. Out for 4 steps.", "Heel first, then roll to the toe."],
    "thumb":   ["HEEL", "TOE", "3 IN · 4 OUT"]      # last line is drawn in the accent color
  }

Needs Pillow and the Inter fonts (FONT_DIR).
"""

from __future__ import annotations

import json
import math
import random
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

# Prefer Inter (Linux CI / Debian). Fall back to common Mac system fonts.
_FONT_CANDIDATES = [
    Path("/usr/share/fonts/opentype/inter"),
    Path("/Library/Fonts"),
    Path.home() / "Library/Fonts",
]
_FONT_MAP = {
    "InterDisplay-Black.otf": ["InterDisplay-Black.otf", "Arial Black.ttf", "Arial Black", "Helvetica.ttc"],
    "Inter-Bold.otf": ["Inter-Bold.otf", "Arial Bold.ttf", "Arial.ttf", "Helvetica.ttc"],
    "Inter-Medium.otf": ["Inter-Medium.otf", "Arial.ttf", "Helvetica.ttc"],
}


def _resolve_font_file(name: str) -> str:
    for base in _FONT_CANDIDATES:
        if not base.exists():
            continue
        for cand in _FONT_MAP.get(name, [name]):
            p = base / cand
            if p.exists():
                return str(p)
            # Mac sometimes stores fonts without extension in the path listing
            matches = list(base.glob(cand + "*")) if not Path(cand).suffix else []
            if matches:
                return str(matches[0])
    raise FileNotFoundError(f"No font for {name}; install Inter or Arial")


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(_resolve_font_file(name), size)


THEMES = {
    #           background      panel           accent          secondary       text            muted
    "forest":  ((14, 32, 26),   (20, 44, 36),   (236, 168, 72), (88, 160, 112), (238, 240, 234), (164, 186, 172)),
    "dusk":    ((30, 20, 44),   (42, 28, 60),   (240, 128, 82), (150, 112, 210), (240, 236, 244), (184, 170, 200)),
    "teal":    ((10, 36, 42),   (14, 50, 58),   (250, 196, 84), (64, 190, 186), (236, 244, 244), (160, 192, 194)),
    "night":   ((12, 16, 34),   (18, 24, 48),   (255, 206, 102), (92, 132, 230), (236, 238, 248), (158, 166, 196)),
    "sunrise": ((44, 24, 22),   (60, 32, 28),   (255, 176, 64), (240, 104, 72), (250, 240, 232), (210, 178, 164)),
    "ember":   ((38, 14, 18),   (54, 20, 26),   (255, 122, 92), (240, 186, 96), (248, 236, 234), (206, 164, 164)),
}


def mix(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


# ---------------------------------------------------------------- motifs (drawn in a box)

def motif_contours(d, box, T, s):
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2 + 30 * s
    rng = random.Random(7)
    for k in range(9, 0, -1):
        r = k * (x1 - x0) / 17
        pts = []
        for a in range(0, 361, 6):
            ang = math.radians(a)
            wob = 1 + 0.08 * math.sin(3 * ang + k) + 0.05 * math.sin(5 * ang + k * 2)
            pts.append((cx + math.cos(ang) * r * wob, cy + math.sin(ang) * r * wob * 0.72))
        col = T[2] if k == 1 else mix(T[1], T[3], 0.35 + k * 0.05)
        d.line(pts, fill=col, width=max(2, int(4 * s)))
    # trail: dashed path climbing to the summit
    for i in range(14):
        t = i / 14
        px = x0 + (cx - x0) * t + math.sin(t * 9) * 30 * s
        py = y1 - (y1 - cy) * t
        if i % 2 == 0:
            d.ellipse([px - 6 * s, py - 6 * s, px + 6 * s, py + 6 * s], fill=T[2])
    d.polygon([(cx, cy - 34 * s), (cx - 22 * s, cy + 6 * s), (cx + 22 * s, cy + 6 * s)], fill=T[2])


def motif_switchback(d, box, T, s):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    d.polygon([(x0, y1), (x0 + w * 0.48, y0 + h * 0.08), (x1, y1)], fill=mix(T[1], T[3], 0.35))
    d.polygon([(x0 + w * 0.3, y1), (x0 + w * 0.72, y0 + h * 0.3), (x1 + w * 0.1, y1)], fill=mix(T[1], T[3], 0.55))
    pts = []
    for i in range(7):
        y = y1 - 20 * s - i * (h * 0.78) / 6
        half = (y - (y0 + h * 0.08)) / (h * 0.92) * w * 0.4
        pts.append((x0 + w * 0.48 + (half if i % 2 else -half), y))
    d.line(pts, fill=T[2], width=int(8 * s), joint="curve")
    px, py = x0 + w * 0.48, y0 + h * 0.08
    d.line([(px, py), (px, py - 70 * s)], fill=T[4], width=int(5 * s))
    d.polygon([(px, py - 70 * s), (px + 46 * s, py - 56 * s), (px, py - 42 * s)], fill=T[2])


def motif_senses(d, box, T, s):
    x0, y0, x1, y1 = box
    rows = [5, 4, 3, 2, 1]
    labels = ["SEE", "TOUCH", "HEAR", "SMELL", "TASTE"]
    rh = (y1 - y0) / 5
    f = font("Inter-Bold.otf", int(30 * s))
    for i, n in enumerate(rows):
        y = y0 + i * rh + rh / 2
        d.text((x0, y - 22 * s), str(n), font=font("InterDisplay-Black.otf", int(44 * s)), fill=T[2])
        for j in range(n):
            cx = x0 + 80 * s + j * 62 * s
            r = 20 * s
            d.ellipse([cx - r, y - r, cx + r, y + r], fill=mix(T[3], T[2], i / 5))
        d.text((x0 + 80 * s + 5 * 62 * s, y - 18 * s), labels[i], font=f, fill=T[5])


def motif_streetlights(d, box, T, s):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    vx, vy = x0 + w * 0.5, y0 + h * 0.18  # vanishing point
    d.polygon([(x0 + w * 0.1, y1), (vx - 8 * s, vy), (vx + 8 * s, vy), (x1 - w * 0.1, y1)], fill=mix(T[1], T[0], 0.4))
    for i in range(5):
        t = 1 - i / 5
        px = vx - (vx - (x0 + w * 0.06)) * t
        base = vy + (y1 - vy) * t
        top = base - 230 * s * t - 20 * s
        d.line([(px, base), (px, top)], fill=T[5], width=max(2, int(7 * s * t)))
        r = max(6, 30 * s * t)
        glow = Image.new("RGBA", (int(r * 8), int(r * 8)), (0, 0, 0, 0))
        ImageDraw.Draw(glow).ellipse([r * 2, r * 2, r * 6, r * 6], fill=T[2] + (120,))
        d._image.paste(glow.filter(ImageFilter.GaussianBlur(r)), (int(px - r * 4), int(top - r * 4)), glow.filter(ImageFilter.GaussianBlur(r)))
        d.ellipse([px - r * 0.6, top - r * 0.6, px + r * 0.6, top + r * 0.6], fill=T[2])
    for i in range(6):
        t = (i + 0.5) / 6
        yy = vy + (y1 - vy) * t
        d.line([(vx, yy), (vx, yy + 26 * s * t)], fill=T[2], width=max(2, int(6 * s * t)))


def motif_sunrise(d, box, T, s):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    cx, hy = x0 + w * 0.5, y0 + h * 0.62
    for k in range(6, 0, -1):
        r = k * w * 0.075
        d.ellipse([cx - r, hy - r, cx + r, hy + r], fill=mix(T[1], T[2], 1 - k / 7))
    d.rectangle([x0 - 10, hy, x1 + 10, y1 + 10], fill=T[1])
    for i in range(12):
        a = math.radians(180 + i * 15 + 7.5)
        d.line([(cx + math.cos(a) * w * 0.5, hy + math.sin(a) * w * 0.5),
                (cx + math.cos(a) * w * 0.56, hy + math.sin(a) * w * 0.56)], fill=T[3], width=int(5 * s))
    d.polygon([(cx - 12 * s, hy), (cx + 12 * s, hy), (cx + w * 0.32, y1), (cx - w * 0.32, y1)], fill=mix(T[1], T[3], 0.5))
    for i in range(5):
        t = (i + 0.5) / 5
        yy = hy + (y1 - hy) * t
        d.line([(cx, yy), (cx, yy + 18 * s * t)], fill=T[4], width=max(2, int(6 * s * t)))


def motif_rings(d, box, T, s):
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    R = (x1 - x0) / 2
    for k in range(7, 3, -1):
        r = R * k / 7
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=mix(T[3], T[2], k / 7), width=max(2, int(5 * s)))
    rc = R * 0.5
    d.ellipse([cx - rc, cy - rc, cx + rc, cy + rc], fill=T[1])
    f = font("InterDisplay-Black.otf", int(40 * s))
    word = "YOUR WORD"
    tw = d.textlength(word, font=f)
    d.text((cx - tw / 2, cy - 26 * s), word, font=f, fill=T[4])
    for i in range(8):
        a = math.radians(i * 45 + 22.5)
        px, py = cx + math.cos(a) * R * 0.86, cy + math.sin(a) * R * 0.86
        d.ellipse([px - 9 * s, py - 9 * s, px + 9 * s, py + 9 * s], fill=T[2])


MOTIFS = {
    "contours": motif_contours, "switchback": motif_switchback, "senses": motif_senses,
    "streetlights": motif_streetlights, "sunrise": motif_sunrise, "rings": motif_rings,
}


# ---------------------------------------------------------------- layout

def fit(d, text, name, size, max_w):
    while size > 20 and d.textlength(text, font=font(name, size)) > max_w:
        size -= 4
    return font(name, size)


def draw(card: dict, W: int, H: int, thumb: bool) -> Image.Image:
    T = THEMES[card["theme"]]
    s = W / 1920
    im = Image.new("RGB", (W, H), T[0])
    d = ImageDraw.Draw(im)
    m = int(100 * s)
    d.rectangle([m, int(88 * s), W - m, H - int(88 * s)], fill=T[1])
    x = int(190 * s)
    text_w = int(1030 * s)
    motif_box = (int(1290 * s), int(220 * s), int(1740 * s), int(860 * s))
    MOTIFS[card["motif"]](d, motif_box, T, s)
    # Optional athlete silhouette (cyclist/hiker/walker/runner) — see add-iq-athlete-silhouette.py
    sil = (card.get("silhouette") or "").strip().lower()
    if sil in {"cyclist", "hiker", "walker", "runner"}:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "sil", Path(__file__).with_name("add-iq-athlete-silhouette.py")
        )
        mod = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(mod)
        mod.DRAWERS[sil](d, motif_box, T[2], s)

    if thumb:
        lines = card.get("thumb") or [card["line1"], card["line2"]]
        d.text((x, int(170 * s)), card["kicker"].split("·")[-1].strip(), font=font("Inter-Bold.otf", int(58 * s)), fill=T[2])
        y = int(270 * s)
        for i, line in enumerate(lines):
            f = fit(d, line, "InterDisplay-Black.otf", int(200 * s), text_w)
            d.text((x, y), line, font=f, fill=T[2] if i == len(lines) - 1 else T[4])
            y += int(220 * s)
    else:
        d.text((x, int(190 * s)), card["kicker"], font=font("Inter-Bold.otf", int(46 * s)), fill=T[2])
        f1 = fit(d, card["line1"], "InterDisplay-Black.otf", int(130 * s), text_w)
        f2 = fit(d, card["line2"], "InterDisplay-Black.otf", int(130 * s), text_w)
        fs = min(f1.size, f2.size)
        d.text((x, int(270 * s)), card["line1"], font=font("InterDisplay-Black.otf", fs), fill=T[4])
        d.text((x, int(270 * s) + int(fs * 1.12)), card["line2"], font=font("InterDisplay-Black.otf", fs), fill=T[2])
        y = int(620 * s)
        for line in card.get("sub", []):
            d.text((x, y), line, font=fit(d, line, "Inter-Medium.otf", int(48 * s), text_w), fill=T[5])
            y += int(70 * s)
        fb = font("Inter-Bold.otf", int(44 * s))
        d.text((x, int(880 * s)), "SPORTSTECHWEST", font=fb, fill=T[4])
        tw = d.textlength("SPORTSTECHWEST", font=fb)
        d.text((x + tw + int(24 * s), int(880 * s)), "·  Voice: Rashad West", font=font("Inter-Medium.otf", int(44 * s)), fill=T[5])
    return im


def main() -> None:
    pkg_dir = Path(sys.argv[1])
    card = json.loads((pkg_dir / "package.json").read_text(encoding="utf-8"))["card"]
    draw(card, 1920, 1080, False).save(pkg_dir / "visual.png")
    draw(card, 1280, 720, True).save(pkg_dir / "thumbnail.jpg", quality=90)
    print(f"wrote {pkg_dir / 'visual.png'} and {pkg_dir / 'thumbnail.jpg'}")


if __name__ == "__main__":
    main()
