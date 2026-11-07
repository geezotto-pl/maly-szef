#!/usr/bin/env python3
"""Mały Szef – obrazki produktów i dań.
Źródło ikon: Fluent Emoji 3D (Microsoft, licencja MIT), pakiet npm @lobehub/fluent-emoji-3d.
Produkty bez emoji rysujemy jako opakowania z ikoną na etykiecie albo prostymi kształtami.
Użycie: python3 imagegen.py <katalog_assets_fluent> <katalog_wyjściowy>"""
import os, sys, math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import products

ASSETS = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/emoji/f3d/package/assets"
OUT = sys.argv[2] if len(sys.argv) > 2 else "out/img"
os.makedirs(OUT, exist_ok=True)
N = 640          # płótno robocze (4× supersampling)
SIZE = 160       # rozmiar wynikowy

def cp(e): return "-".join(f"{ord(c):x}" for c in e if ord(c) != 0xFE0F)
def emoji(e, size):
    im = Image.open(os.path.join(ASSETS, cp(e) + ".webp")).convert("RGBA")
    return im.resize((size, size), Image.LANCZOS)

def hexc(h, a=255):
    h = h.lstrip("#"); return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a)
def mix(c, d, t): return tuple(int(c[i] * (1 - t) + d[i] * t) for i in range(3)) + (c[3] if len(c) > 3 else 255,)
WHITE = (255, 255, 255, 255); BLACK = (0, 0, 0, 255)

def tint(im, dh, ds, dv):
    a = np.asarray(im).astype(np.float32) / 255.0
    rgb, al = a[..., :3], a[..., 3:]
    mx, mn = rgb.max(-1), rgb.min(-1); d = mx - mn
    h = np.zeros_like(mx)
    m = d > 1e-6
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    idx = m & (mx == r); h[idx] = ((g - b)[idx] / d[idx]) % 6
    idx = m & (mx == g); h[idx] = ((b - r)[idx] / d[idx]) + 2
    idx = m & (mx == b); h[idx] = ((r - g)[idx] / d[idx]) + 4
    h = (h * 60 + dh) % 360
    s = np.where(mx > 0, d / np.maximum(mx, 1e-6), 0) * ds
    v = mx * dv
    s, v = np.clip(s, 0, 1), np.clip(v, 0, 1)
    c = v * s; x = c * (1 - np.abs((h / 60) % 2 - 1)); mm = v - c
    z = np.zeros_like(h); hi = (h // 60).astype(int)
    rr = np.select([hi == 0, hi == 1, hi == 2, hi == 3, hi == 4, hi == 5], [c, x, z, z, x, c])
    gg = np.select([hi == 0, hi == 1, hi == 2, hi == 3, hi == 4, hi == 5], [x, c, c, x, z, z])
    bb = np.select([hi == 0, hi == 1, hi == 2, hi == 3, hi == 4, hi == 5], [z, z, x, c, c, x])
    out = np.concatenate([np.stack([rr + mm, gg + mm, bb + mm], -1), al], -1)
    return Image.fromarray((out * 255).astype(np.uint8), "RGBA")

def grad_fill(size, mask, top, bottom):
    """Pionowy gradient wypełniający maskę."""
    w, h = size
    g = np.zeros((h, w, 4), np.uint8)
    t = np.linspace(0, 1, h)[:, None]
    for i in range(3): g[..., i] = (top[i] * (1 - t) + bottom[i] * t).astype(np.uint8)
    g[..., 3] = 255
    im = Image.fromarray(g, "RGBA"); im.putalpha(mask); return im

class FillDraw:
    """ImageDraw, który domyślnie wypełnia kształty (fill=255)."""
    def __init__(self, im): self.d = ImageDraw.Draw(im)
    def __getattr__(self, name):
        f = getattr(self.d, name)
        def g(*a, **k):
            if name in ("polygon", "rectangle", "rounded_rectangle", "ellipse", "pieslice", "chord"): k.setdefault("fill", 255)
            return f(*a, **k)
        return g

def shape_layer(draw_fn, col, light=.35, dark=.18):
    m = Image.new("L", (N, N), 0); draw_fn(FillDraw(m))
    return grad_fill((N, N), m, mix(col, WHITE, light), mix(col, BLACK, dark)), m

def shadow(base, box, alpha=70):
    sh = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse(box, fill=(60, 40, 20, alpha))
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))

def highlight(base, box, r=30, alpha=90):
    hl = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    ImageDraw.Draw(hl).rounded_rectangle(box, r, fill=(255, 255, 255, alpha))
    base.alpha_composite(hl.filter(ImageFilter.GaussianBlur(6)))

def label(base, cx, cy, d, e, ring):
    lb = Image.new("RGBA", (N, N), (0, 0, 0, 0)); dr = ImageDraw.Draw(lb)
    dr.ellipse((cx - d // 2 - 10, cy - d // 2 - 10, cx + d // 2 + 10, cy + d // 2 + 10), fill=ring)
    dr.ellipse((cx - d // 2, cy - d // 2, cx + d // 2, cy + d // 2), fill=WHITE)
    base.alpha_composite(lb)
    ic = emoji(e, int(d * .82)); base.alpha_composite(ic, (cx - ic.width // 2, cy - ic.height // 2))

def outline_of(mask, col, width=10):
    """Delikatny kontur, żeby białe opakowania odcinały się od tła."""
    m = mask.filter(ImageFilter.MaxFilter(width * 2 + 1))
    o = Image.new("RGBA", (N, N), col); o.putalpha(m); return o

def package(kind, color, e):
    col = hexc(color); base = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    is_white = sum(col[:3]) > 690
    edge = mix(col, BLACK, .30) if not is_white else (205, 200, 192, 255)
    ring = mix(col, BLACK, .15) if not is_white else (225, 220, 210, 255)
    layers = []
    def add(fn, c, light=.35, dark=.18):
        im, m = shape_layer(fn, c, light, dark); layers.append((im, m))
    if kind == "cup":
        shadow(base, (150, 520, 490, 580))
        add(lambda d: d.polygon([(130, 200), (510, 200), (450, 550), (190, 550)]), col)
        add(lambda d: d.rounded_rectangle((110, 160, 530, 220), 20), (230, 232, 236, 255), .4, .15)
        cx, cy, ld = 320, 370, 200
    elif kind == "tub":
        shadow(base, (90, 470, 550, 540))
        add(lambda d: d.rounded_rectangle((100, 240, 540, 510), 50), col)
        add(lambda d: d.rounded_rectangle((85, 200, 555, 268), 26), mix(col, BLACK, .08) if not is_white else (230, 232, 236, 255), .3, .12)
        cx, cy, ld = 320, 385, 190
    elif kind == "block":
        shadow(base, (90, 480, 560, 550))
        add(lambda d: d.polygon([(150, 210), (530, 210), (480, 290), (100, 290)]), col, .55, .05)
        add(lambda d: d.rounded_rectangle((100, 280, 480, 510), 18), col)
        add(lambda d: d.polygon([(480, 290), (530, 210), (530, 430), (480, 510)]), mix(col, BLACK, .15), .1, .2)
        cx, cy, ld = 290, 395, 190
    elif kind == "box":
        shadow(base, (140, 540, 520, 600))
        add(lambda d: d.polygon([(190, 80), (480, 80), (430, 140), (140, 140)]), col, .55, .05)
        add(lambda d: d.rounded_rectangle((140, 130, 430, 570), 16), col)
        add(lambda d: d.polygon([(430, 140), (480, 80), (480, 510), (430, 570)]), mix(col, BLACK, .2), .1, .2)
        cx, cy, ld = 285, 340, 210
    elif kind in ("bag", "sachet"):
        top, bot, l, r = (90, 570, 140, 500) if kind == "bag" else (120, 540, 170, 470)
        shadow(base, (l - 10, bot - 30, r + 10, bot + 30))
        def bag(d):
            d.rounded_rectangle((l, top + 40, r, bot), 50)
            z = [(l + 5, top + 60)]
            for i in range(9): z.append((l + 5 + (r - l - 10) * (i + .5) / 9, top + (0 if i % 2 == 0 else 30)))
            z.append((r - 5, top + 60)); d.polygon(z)
        add(bag, col)
        add(lambda d: d.rectangle((l + 10, top + 50, r - 10, top + 75)), mix(col, BLACK, .12), .1, .1)
        cx, cy, ld = (l + r) // 2, (top + bot) // 2 + 40, 210 if kind == "bag" else 180
    elif kind == "bottle":
        shadow(base, (190, 560, 450, 610))
        add(lambda d: d.rounded_rectangle((250, 70, 390, 140), 18), mix(col, BLACK, .35), .3, .2)
        add(lambda d: (d.rounded_rectangle((180, 210, 460, 590), 60), d.polygon([(265, 130), (375, 130), (440, 230), (200, 230)])), col)
        cx, cy, ld = 320, 410, 190
    elif kind in ("jar", "spice"):
        if kind == "jar": x0, x1, y0, y1, lid = 150, 490, 210, 570, (170, 140, 470, 225)
        else: x0, x1, y0, y1, lid = 205, 435, 240, 570, (215, 160, 425, 250)
        shadow(base, (x0, y1 - 30, x1, y1 + 30))
        add(lambda d: d.rounded_rectangle((x0, y0, x1, y1), 60), col)
        lc = (226, 69, 69, 255) if kind == "spice" else (mix(col, BLACK, .35) if not is_white else (90, 140, 220, 255))
        add(lambda d: d.rounded_rectangle(lid, 22), lc, .35, .2)
        cx, cy, ld = (x0 + x1) // 2, (y0 + y1) // 2 + 10, min(210, x1 - x0 - 50)
    elif kind == "can":
        shadow(base, (150, 540, 490, 600))
        add(lambda d: d.rounded_rectangle((160, 130, 480, 570), 40), col)
        add(lambda d: d.ellipse((160, 95, 480, 165)), (205, 210, 218, 255), .45, .2)
        add(lambda d: (d.rectangle((160, 150, 480, 175)), d.rectangle((160, 530, 480, 550))), (180, 186, 196, 255), .3, .2)
        cx, cy, ld = 320, 350, 220
    elif kind == "carton":
        shadow(base, (150, 550, 490, 610))
        add(lambda d: d.polygon([(170, 200), (320, 70), (470, 200)]), mix(col, BLACK, .06), .4, .1)
        add(lambda d: d.rounded_rectangle((170, 190, 470, 580), 14), col)
        add(lambda d: d.rectangle((300, 40, 340, 90)), mix(col, BLACK, .2), .2, .2)
        cx, cy, ld = 320, 385, 210
    elif kind == "tray":
        shadow(base, (70, 470, 570, 560))
        add(lambda d: d.polygon([(70, 250), (570, 250), (520, 500), (120, 500)]), (236, 238, 242, 255), .3, .15)
        add(lambda d: d.rounded_rectangle((120, 270, 520, 470), 70), col, .1, .25)
        cx, cy, ld = 320, 365, 190
    else:
        raise ValueError(kind)
    for im, m in layers:
        base.alpha_composite(outline_of(m, edge, 5))
    for im, m in layers: base.alpha_composite(im)
    if kind not in ("tray",):
        highlight(base, (cx - ld // 2 - 70 if kind not in ("bottle",) else 205, 230, cx - ld // 2 - 45 if kind not in ("bottle",) else 228, 470), 12, 80)
    if kind == "tray":  # folia
        f = Image.new("RGBA", (N, N), (0, 0, 0, 0)); ImageDraw.Draw(f).polygon([(110, 270), (300, 270), (200, 480), (140, 480)], fill=(255, 255, 255, 70))
        base.alpha_composite(f.filter(ImageFilter.GaussianBlur(4)))
    label(base, cx, cy, ld, e, ring)
    return base

def drawn(name):
    base = Image.new("RGBA", (N, N), (0, 0, 0, 0)); d = ImageDraw.Draw(base)
    def blob(fn, col, light=.35, dark=.2):
        im, m = shape_layer(fn, col, light, dark); base.alpha_composite(outline_of(m, mix(col, BLACK, .35), 5)); base.alpha_composite(im)
    if name == "kielbasa":
        shadow(base, (90, 480, 560, 560))
        blob(lambda d: (d.arc((90, 110, 550, 570), 160, 380, fill=255, width=120)), (176, 58, 46, 255))
        for x, y in [(170, 260), (250, 180), (360, 175), (450, 240), (480, 340), (140, 360)]:
            d.ellipse((x - 9, y - 9, x + 9, y + 9), fill=(255, 225, 215, 230))
        for x, y in [(105, 380), (535, 380)]:
            d.ellipse((x - 22, y - 10, x + 22, y + 30), fill=(150, 110, 70, 255))
    elif name == "kabanosy":
        shadow(base, (110, 470, 560, 550))
        for i, off in enumerate([-90, 0, 90]):
            blob(lambda dd, o=off: dd.line((150 + o, 520, 470 + o, 110), fill=255, width=58), (150, 62, 40, 255), .3, .25)
        for i, off in enumerate([-90, 0, 90]):
            d.line((175 + off, 470, 440 + off, 140), fill=(255, 255, 255, 60), width=10)
    elif name == "burak":
        shadow(base, (170, 520, 470, 580))
        blob(lambda dd: (dd.ellipse((290, 40, 380, 230)), dd.ellipse((370, 60, 470, 230)), dd.ellipse((200, 70, 300, 230))), (60, 160, 70, 255))
        d.line((320, 230, 330, 120), fill=(140, 30, 70, 255), width=14); d.line((330, 230, 410, 110), fill=(140, 30, 70, 255), width=12)
        blob(lambda dd: (dd.ellipse((170, 210, 470, 500)), dd.polygon([(280, 470), (360, 470), (325, 600)])), (128, 24, 82, 255))
        highlight(base, (220, 280, 250, 400), 12, 90)
    elif name == "rzodkiewka":
        for (x, y, s) in [(200, 330, 1), (400, 300, 1.1), (300, 420, 1.15)]:
            shadow(base, (x - 90 * s, y + 80 * s, x + 90 * s, y + 120 * s), 50)
        for (x, y, s) in [(200, 330, 1), (400, 300, 1.1), (300, 420, 1.15)]:
            blob(lambda dd, x=x, y=y, s=s: (dd.ellipse((x - 25 * s, y - 230 * s, x + 25 * s, y - 70 * s)), dd.ellipse((x - 75 * s, y - 200 * s, x - 15 * s, y - 70 * s)), dd.ellipse((x + 15 * s, y - 200 * s, x + 75 * s, y - 70 * s))), (70, 170, 70, 255))
            blob(lambda dd, x=x, y=y, s=s: dd.ellipse((x - 95 * s, y - 95 * s, x + 95 * s, y + 85 * s)), (222, 40, 70, 255))
            blob(lambda dd, x=x, y=y, s=s: (dd.ellipse((x - 45 * s, y + 25 * s, x + 45 * s, y + 95 * s)), dd.polygon([(x - 12 * s, y + 80 * s), (x + 12 * s, y + 80 * s), (x, y + 140 * s)])), (248, 244, 240, 255), .2, .1)
            highlight(base, (int(x - 60 * s), int(y - 60 * s), int(x - 38 * s), int(y)), 10, 110)
    elif name == "por":
        shadow(base, (130, 520, 520, 580))
        blob(lambda dd: (dd.polygon([(330, 120), (420, 30), (450, 60), (380, 160)]), dd.polygon([(320, 120), (300, 20), (340, 20), (360, 140)]), dd.polygon([(320, 140), (200, 60), (230, 40), (350, 130)])), (50, 140, 60, 255))
        blob(lambda dd: dd.polygon([(290, 130), (370, 130), (390, 300), (270, 300)]), (130, 190, 80, 255))
        blob(lambda dd: dd.rounded_rectangle((268, 290, 392, 560), 50), (240, 240, 225, 255), .3, .12)
        d.line((300, 560, 300, 590), fill=(200, 180, 150, 255), width=5); d.line((330, 560, 335, 595), fill=(200, 180, 150, 255), width=5); d.line((360, 560, 365, 590), fill=(200, 180, 150, 255), width=5)
    elif name == "cynamon":
        shadow(base, (100, 470, 560, 550))
        for off in (-80, 20, 120):
            blob(lambda dd, o=off: dd.line((140, 420 + o * .3 - 40 + o, 500, 260 + o * .3 - 40 + o), fill=255, width=70), (160, 92, 48, 255), .3, .25)
            x, y = 500, 260 + off * .3 - 40 + off
            d.ellipse((x - 38, y - 38, x + 38, y + 38), fill=(125, 66, 30, 255))
            d.arc((x - 26, y - 26, x + 26, y + 26), 0, 300, fill=(200, 140, 90, 255), width=6)
            d.arc((x - 13, y - 13, x + 13, y + 13), 60, 360, fill=(200, 140, 90, 255), width=5)
    elif name == "dynia":
        shadow(base, (110, 500, 530, 580))
        blob(lambda dd: dd.rounded_rectangle((300, 70, 345, 190), 14), (110, 140, 60, 255), .3, .3)
        for x0, x1, t in [(95, 335, .25), (305, 545, .25), (150, 340, .35), (300, 490, .35), (220, 420, .45)]:
            blob(lambda dd, a=x0, b=x1: dd.ellipse((a, 170, b, 540)), (243, 128, 40, 255), t, .22)
        d.arc((215, 175, 425, 540), 75, 105, fill=(200, 95, 25, 255), width=4)
        highlight(base, (170, 250, 200, 400), 14, 90)
        blob(lambda dd: dd.ellipse((330, 100, 430, 150)), (90, 160, 70, 255), .3, .25)
    elif name == "natka":
        shadow(base, (170, 540, 470, 600))
        stems = [(320, 560, x, y) for x, y in [(190, 200), (250, 150), (320, 130), (390, 150), (450, 200), (220, 290), (420, 290)]]
        for x0, y0, x1, y1 in stems:
            d.line((x0, y0 - 120, x1, y1 + 40), fill=(120, 175, 80, 255), width=12)
        d.line((320, 560, 320, 440), fill=(120, 175, 80, 255), width=40)
        for _, _, x, y in stems:
            for ang in (-50, 0, 50, 180):
                r = math.radians(ang - 90); cx, cy = x + 42 * math.cos(r), y + 42 * math.sin(r)
                blob(lambda dd, cx=cx, cy=cy: (dd.ellipse((cx - 38, cy - 30, cx + 38, cy + 30)), dd.polygon([(cx - 38, cy), (cx, cy - 46), (cx + 38, cy), (cx, cy + 40)])), (46, 150, 60, 255), .35, .25)
        blob(lambda dd: dd.rounded_rectangle((282, 455, 358, 495), 12), (220, 60, 60, 255), .3, .2)
    else:
        raise ValueError(name)
    return base

def fit(im):
    bb = im.getbbox(); im = im.crop(bb)
    s = 600 / max(im.size); im = im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.LANCZOS)
    c = Image.new("RGBA", (N, N), (0, 0, 0, 0)); c.alpha_composite(im, ((N - im.width) // 2, (N - im.height) // 2)); return c

def make(spec):
    if spec.startswith("p:"):
        _, kind, col, e = spec.split(":"); im = fit(package(kind, col, e))
    elif spec.startswith("d:"):
        im = fit(drawn(spec[2:]))
    elif spec.startswith("t:"):
        _, e, args = spec.split(":"); h, s, v = map(float, args.split(",")); im = tint(emoji(e, N), h, s, v)
    else:
        im = emoji(spec, N)
    return im.resize((SIZE, SIZE), Image.LANCZOS)

def save(im, name): im.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=88, method=6)

if __name__ == "__main__":
    P = products.parse()
    for k, p in P.items(): save(make(p["img"]), k)
    # dania i ikony interfejsu (emoji)
    extra = "🍕🍦🍓🍎🥤🥧🍪🧁🧇🥞🍲🍝🥟🌭🍔🍟🌯🥪🐟🍗🍳🥣🍚🍖🥬🥔🧑‍🍳🍮🥗🍒🥛🍫🍊⭐🏆🎉👧👦🧊🧺🗄️❄️🥦🔍📒🔒🏠"
    import regex as _re  # grafemy
    for e in _re.findall(r"\X", extra):
        try: save(emoji(e, N).resize((SIZE, SIZE), Image.LANCZOS), "e-" + cp(e))
        except FileNotFoundError: print("brak", e)
    # ikony aplikacji: kucharz 3D na pomarańczowym tle
    root = os.path.dirname(os.path.abspath(OUT))
    chef = emoji("🧑‍🍳", 512)
    for size, sc, name in [(192, .74, "icon-192.png"), (512, .74, "icon-512.png"), (512, .58, "icon-maskable-512.png"), (180, .74, "apple-touch-icon.png")]:
        im = Image.new("RGBA", (size, size), (255, 122, 69, 255)); w = int(size * sc); c = chef.resize((w, w), Image.LANCZOS)
        im.alpha_composite(c, ((size - w) // 2, (size - w) // 2 + int(size * .02))); im.convert("RGB").save(os.path.join(root, name))
    print("OK", len(os.listdir(OUT)), "plików")
