"""
Gera o icone do app (1024x1024 PNG) do Radar de Posts: fundacao escura, arcos de
radar e barras ascendentes de engajamento.

Uso: python scripts/gerar-icone.py
"""
from PIL import Image, ImageDraw
import math
import os

S = 1024
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "radar-de-posts-site", "icone-1024.png")

BG_TOP = (13, 22, 48)
BG_BOTTOM = (28, 79, 216)
ACCENT = (94, 196, 255)
BAR = (255, 255, 255)
WARM = (255, 198, 92)


def vertical_gradient(size, top, bottom):
    img = Image.new("RGB", (1, size))
    px = img.load()
    for y in range(size):
        t = y / (size - 1)
        px[0, y] = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
    return img.resize((size, size), Image.BICUBIC)


def main():
    base = vertical_gradient(S, BG_TOP, BG_BOTTOM).convert("RGBA")
    d = ImageDraw.Draw(base, "RGBA")

    cx, cy = S * 0.22, S * 0.82
    max_r = S * 0.52
    for i, r in enumerate([0.30, 0.58, 0.86, 1.14]):
        rr = max_r * r
        alpha = 220 - i * 40
        d.arc([cx - rr, cy - rr, cx + rr, cy + rr], start=270, end=350,
              fill=ACCENT + (alpha,), width=int(S * 0.012))
    d.ellipse([cx - S * 0.028, cy - S * 0.028, cx + S * 0.028, cy + S * 0.028],
              fill=ACCENT + (255,))

    # barras de engajamento (comentarios / curtidas / views)
    base_x, base_y = S * 0.42, S * 0.80
    bw = S * 0.125
    gap = S * 0.035
    heights = [S * 0.22, S * 0.34, S * 0.48]
    colors = [ACCENT, BAR, WARM]
    for i, (h, c) in enumerate(zip(heights, colors)):
        x0 = base_x + i * (bw + gap)
        d.rounded_rectangle([x0, base_y - h, x0 + bw, base_y], radius=int(S * 0.022),
                            fill=c + (255,))

    d.rounded_rectangle([base_x - S * 0.02, base_y, base_x + 3 * bw + 2 * gap + S * 0.02,
                         base_y + S * 0.028], radius=int(S * 0.014),
                        fill=(255, 255, 255, 90))

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    base.convert("RGB").save(OUT, "PNG", optimize=True)
    print(f"icone gerado em {OUT}")


if __name__ == "__main__":
    main()
