#!/usr/bin/env python3
"""Renders DPGlance's icons, social image and Play Store graphics.

Needs: fonttools (pip install fonttools), rsvg-convert and ImageMagick (magick).
Run:   python3 tools/graphics.py path/to/spacegrotesk.ttf
Text is converted to vector outlines so no font has to be installed.
"""
import pathlib
import subprocess
import sys
import tempfile

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMG = ROOT / "docs" / "assets" / "img"
PLAY = ROOT / "play-store" / "graphics"
TTF = sys.argv[1]

BG, AMBER, CORAL = "#0C0C0D", "#FFC53D", "#FF6B4A"
AMBER_DEEP, CORAL_DEEP, INK = "#7A5410", "#8F2F1B", "#F4F4F5"

# Mark: amber avatar disc with a dark person silhouette and a coral sparkle (the "glance").
# Everything sits inside a 33-unit radius of the centre so Android's circular launcher mask never clips it.
EYE = ('<defs><clipPath id="av"><circle cx="54" cy="54" r="29.7"/></clipPath></defs>'
       f'<circle cx="54" cy="54" r="29" fill="{AMBER}"/>'
       f'<g clip-path="url(#av)"><circle cx="54" cy="47" r="9" fill="{BG}"/><ellipse cx="54" cy="82" rx="22" ry="18" fill="{BG}"/></g>'
       f'<path d="M72,28 L74.2,33.8 L80,36 L74.2,38.2 L72,44 L69.8,38.2 L64,36 L69.8,33.8 Z" fill="{CORAL}"/>')


def make_font(weight):
    f = TTFont(TTF)
    return instantiateVariableFont(f, {"wght": weight})


FONTS = {w: make_font(w) for w in (500, 700)}


def text(s, size, x, y, weight=700, fill=INK, anchor="start", opacity=1.0):
    f = FONTS[weight]
    gs, cmap, upm = f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm
    k = size / upm
    width = sum(gs[cmap[ord(c)]].width for c in s) * k
    cur = x - (width / 2 if anchor == "middle" else 0)
    d = []
    for ch in s:
        g = gs[cmap[ord(ch)]]
        pen = SVGPathPen(gs)
        g.draw(TransformPen(pen, (k, 0, 0, -k, cur, y)))
        d.append(pen.getCommands())
        cur += g.width * k
    return f'<path d="{" ".join(d)}" fill="{fill}" fill-opacity="{opacity}"/>'


def logo_tile(x, y, size, rounded=True):
    s = size / 108
    rx = 24 if rounded else 0
    return (f'<g transform="translate({x},{y}) scale({s})"><rect width="108" height="108" rx="{rx}" fill="{BG}"/>{EYE}</g>')


def scene(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<defs><filter id="b" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="90"/></filter></defs>'
            f'<rect width="{w}" height="{h}" fill="{BG}"/>{body}</svg>')


def orbs(w, h):
    return (f'<circle cx="{w*0.1}" cy="{h*0.05}" r="{h*0.55}" fill="{AMBER_DEEP}" opacity=".8" filter="url(#b)"/>'
            f'<circle cx="{w*0.92}" cy="{h*0.95}" r="{h*0.5}" fill="{CORAL_DEEP}" opacity=".75" filter="url(#b)"/>')


def render(svg, out, w=None, h=None):
    with tempfile.NamedTemporaryFile("w", suffix=".svg", delete=False) as t:
        t.write(svg)
        src = t.name
    cmd = ["rsvg-convert", src, "-o", str(out)]
    if w:
        cmd += ["-w", str(w)]
    if h:
        cmd += ["-h", str(h)]
    subprocess.run(cmd, check=True)
    pathlib.Path(src).unlink()


def square_svg(size):
    return scene(size, size, f'<g transform="scale({size/108})">{EYE}</g>')


def main():
    IMG.mkdir(parents=True, exist_ok=True)
    PLAY.mkdir(parents=True, exist_ok=True)

    # vector icons
    logo = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 108 108"><rect width="108" height="108" rx="24" fill="{BG}"/>{EYE}</svg>')
    (IMG / "favicon.svg").write_text(logo + "\n")
    (IMG / "logo.svg").write_text(logo.replace(
        'viewBox="0 0 108 108">', 'viewBox="0 0 108 108" role="img" aria-label="DPGlance logo: an amber profile avatar with a coral sparkle">') + "\n")

    # raster icons (full-bleed square; platforms apply their own mask)
    render(square_svg(512), IMG / "icon-512.png")
    render(square_svg(192), IMG / "icon-192.png")
    render(square_svg(180), IMG / "apple-touch-icon.png")
    render(square_svg(512), PLAY / "app-icon-512.png")
    subprocess.run(["magick", str(PLAY / "app-icon-512.png"), "-alpha", "on", "PNG32:" + str(PLAY / "app-icon-512.png")], check=True)
    for n in (16, 32, 48):
        render(square_svg(n), pathlib.Path(tempfile.gettempdir()) / f"dpglance-{n}.png")
    t = pathlib.Path(tempfile.gettempdir())
    subprocess.run(["magick", str(t / "dpglance-16.png"), str(t / "dpglance-32.png"), str(t / "dpglance-48.png"),
                    str(ROOT / "docs" / "favicon.ico")], check=True)

    # social share image 1200x630
    w, h = 1200, 630
    body = orbs(w, h)
    body += ('<rect x="70" y="80" width="1060" height="470" rx="56" fill="#ffffff" fill-opacity=".07" '
             'stroke="#ffffff" stroke-opacity=".2" stroke-width="2"/>')
    body += logo_tile(130, 195, 240)
    body += text("DPGlance", 128, 420, 322)
    body += text("Glance at any public profile.", 46, 424, 392, 500)
    body += text("Free Android app. No account needed.", 30, 424, 448, 500, INK, opacity=.72)
    body += text("Independent app. Not affiliated with Snap Inc.", 24, 424, 506, 500, INK, opacity=.55)
    render(scene(w, h, body), IMG / "og-image.png")

    # Google Play feature graphic 1024x500
    w, h = 1024, 500
    body = orbs(w, h)
    body += logo_tile(96, 130, 240)
    body += text("DPGlance", 112, 380, 270)
    body += text("Glance at any public profile.", 40, 384, 338, 500, INK, opacity=.85)
    render(scene(w, h, body), PLAY / "feature-graphic-1024x500.png")

    print("graphics written")


if __name__ == "__main__":
    main()
