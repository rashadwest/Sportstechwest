"""Shrink rendered PNG graphics by quantizing to a 256-colour palette.
Usage: python3 _graphics/shrink_png.py path/to/image.png [...]"""
import sys
from PIL import Image
for p in sys.argv[1:]:
    im = Image.open(p).convert('RGB')
    im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG).save(p, optimize=True)
    print(p)
