#!/usr/bin/env python3
"""Draw the bikeIQ "Breathe Every 5 Pedals" video card (visual.png) and thumbnail.jpg.
Usage: python3 scripts/make-bikeiq-card.py video-packages/rasun/bikeiq-breathe-every-5-pedals
Needs Pillow and the Inter fonts (paths below)."""
import math, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
_FONT_DIRS = [
    Path("/usr/share/fonts/opentype/inter"),
    Path("/Library/Fonts"),
    Path("/System/Library/Fonts"),
    Path("/System/Library/Fonts/Supplemental"),
]
_FONT_FALLBACKS = {
    "Inter-Bold.otf": ["Inter-Bold.otf", "Arial Bold.ttf", "Helvetica.ttc", "Arial.ttf"],
    "InterDisplay-Black.otf": ["InterDisplay-Black.otf", "Arial Black.ttf", "Helvetica.ttc", "Arial.ttf"],
    "Inter-Medium.otf": ["Inter-Medium.otf", "Arial.ttf", "Helvetica.ttc"],
}
def font(n, s):
    for base in _FONT_DIRS:
        for cand in _FONT_FALLBACKS.get(n, [n]):
            p = base / cand
            if p.exists():
                return ImageFont.truetype(str(p), s)
    return ImageFont.load_default()
BG=(22,28,40); PANEL=(28,35,49); ORANGE=(232,104,42); BLUE=(43,123,196); WHITE=(236,238,242); GREY=(160,168,182)

def wheel(d, cx, cy, r, scale):
    w=max(2,int(6*scale))
    d.ellipse([cx-r,cy-r,cx+r,cy+r], outline=BLUE, width=w)
    d.ellipse([cx-r*0.86,cy-r*0.86,cx+r*0.86,cy+r*0.86], outline=(36,70,110), width=max(1,w//2))
    for k in range(10):
        a=math.radians(k*36-90)
        d.line([cx,cy,cx+math.cos(a)*r*0.86,cy+math.sin(a)*r*0.86], fill=(36,70,110), width=max(1,w//3))
    # five orange pedal marks on the top half = inhale, five blue on the bottom = exhale
    for k in range(10):
        a=math.radians(-162+k*36)
        px,py=cx+math.cos(a)*r,cy+math.sin(a)*r
        rr=r*0.075
        col = ORANGE if k<5 else WHITE
        d.ellipse([px-rr,py-rr,px+rr,py+rr], fill=col)
    d.ellipse([cx-r*0.12,cy-r*0.12,cx+r*0.12,cy+r*0.12], fill=BLUE)

def card(W,H,thumb):
    s=W/1920
    im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    m=int(100*s)
    d.rectangle([m,int(88*s),W-m,H-int(88*s)], fill=PANEL)
    x=int(200*s)
    if thumb:
        d.text((x,int(170*s)),"1 HOUR GUIDED RIDE",font=font("Inter-Bold.otf",int(58*s)),fill=ORANGE)
        d.text((x,int(270*s)),"BREATHE",font=font("InterDisplay-Black.otf",int(200*s)),fill=WHITE)
        d.text((x,int(490*s)),"EVERY",font=font("InterDisplay-Black.otf",int(200*s)),fill=WHITE)
        d.text((x,int(710*s)),"5 PEDALS",font=font("InterDisplay-Black.otf",int(200*s)),fill=ORANGE)
        wheel(d,int(1560*s),int(560*s),int(230*s),s)
    else:
        d.text((x,int(190*s)),"bikeIQ  ·  1 HOUR GUIDED RIDE",font=font("Inter-Bold.otf",int(46*s)),fill=ORANGE)
        d.text((x,int(270*s)),"BREATHE EVERY",font=font("InterDisplay-Black.otf",int(124*s)),fill=WHITE)
        d.text((x,int(420*s)),"5 PEDALS",font=font("InterDisplay-Black.otf",int(124*s)),fill=ORANGE)
        d.text((x,int(620*s)),"In for 5 pedals. Out for 5 pedals.",font=font("Inter-Medium.otf",int(50*s)),fill=GREY)
        d.text((x,int(705*s)),"Count one each time your right foot",font=font("Inter-Medium.otf",int(50*s)),fill=GREY)
        d.text((x,int(790*s)),"reaches the bottom.",font=font("Inter-Medium.otf",int(50*s)),fill=GREY)
        d.text((x,int(880*s)),"SPORTSTECHWEST",font=font("Inter-Bold.otf",int(44*s)),fill=WHITE)
        tw=d.textlength("SPORTSTECHWEST",font=font("Inter-Bold.otf",int(44*s)))
        d.text((x+tw+int(24*s),int(880*s)),"·  Voice: Rashad West",font=font("Inter-Medium.otf",int(44*s)),fill=GREY)
        wheel(d,int(1530*s),int(560*s),int(210*s),s)
        f=font("Inter-Bold.otf",int(38*s))
        d.text((int(1530*s)-d.textlength("IN 5",font=f)/2,int(280*s)),"IN 5",font=f,fill=ORANGE)
        d.text((int(1530*s)-d.textlength("OUT 5",font=f)/2,int(800*s)),"OUT 5",font=f,fill=WHITE)
    return im
out=sys.argv[1]
card(1920,1080,False).save(out+"/visual.png")
card(1280,720,True).convert("RGB").save(out+"/thumbnail.jpg",quality=90)
