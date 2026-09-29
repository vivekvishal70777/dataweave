#!/usr/bin/env python3
"""Render a DataWeave mapObject walkthrough as an animated GIF."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 980, 560
OUT = Path(__file__).resolve().parents[1] / "assets" / "mapObject.gif"

BG = (15, 23, 42)
CARD = (30, 41, 59)
CARD_EDGE = (51, 65, 85)
INK = (248, 250, 252)
MUTED = (148, 163, 184)
DIM = (100, 116, 139)
CYAN = (56, 189, 248)
AMBER = (251, 191, 36)
GREEN = (74, 222, 128)
ACTIVE = (23, 55, 94)
DONE = (20, 55, 42)

FONT = "/usr/share/fonts/truetype/macos/Inter-Regular.ttf"
FONT_MED = "/usr/share/fonts/truetype/macos/Inter-Medium.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/macos/Inter-Bold.ttf"
MONO = "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-Medium.ttf"

ITEMS = [("apple", 2, 4), ("bread", 3, 6), ("milk", 4, 8)]


def font(path, size):
    return ImageFont.truetype(path, size)


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text(draw, xy, content, face, fill):
    draw.text(xy, content, font=face, fill=fill)


def frame(step, phase):
    """step: -1 intro, 0..2 items, 3 returned. phase 0..1 within the step."""
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)

    title = font(FONT_BOLD, 32)
    subtitle = font(FONT, 17)
    label = font(FONT_MED, 15)
    mono = font(MONO, 18)
    row_font = font(MONO, 22)
    small = font(FONT, 16)
    badge = font(FONT_MED, 14)

    text(draw, (40, 24), "mapObject", title, INK)
    text(
        draw,
        (40, 66),
        "DataWeave walks each entry, runs the mapper, and returns an object.",
        subtitle,
        MUTED,
    )

    rounded(draw, (40, 108, 940, 164), 12, CARD, CARD_EDGE, 2)
    text(draw, (56, 124), "cart mapObject (value, key) -> { (key): value * 2 }", mono, CYAN)

    left = (40, 186, 470, 448)
    right = (510, 186, 940, 448)
    rounded(draw, left, 16, CARD, CARD_EDGE, 2)
    rounded(draw, right, 16, CARD, CARD_EDGE, 2)
    text(draw, (60, 200), "cart", label, MUTED)
    text(draw, (530, 200), "result", label, MUTED)

    active_index = step if 0 <= step <= 2 else None
    finished = step >= 3
    if step in (0, 1, 2) and phase < 0.55:
        written = ITEMS[:step]
    elif 0 <= step <= 2:
        written = ITEMS[: step + 1]
    elif finished:
        written = ITEMS
    else:
        written = []

    for index, (key, src, _out) in enumerate(ITEMS):
        y = 238 + index * 64
        box = (60, y, 450, y + 52)
        is_active = index == active_index and not finished
        fill, edge, color = (ACTIVE, AMBER, AMBER) if is_active else ((15, 23, 42), CARD_EDGE, INK)
        rounded(draw, box, 10, fill, edge, 2)
        text(draw, (76, y + 12), f"{key}: {src}", row_font, color)

    result_edge = GREEN if finished else (AMBER if written else CARD_EDGE)
    result_fill = DONE if finished else CARD
    rounded(draw, (530, 238, 920, 430), 10, result_fill, result_edge, 2)
    if not written:
        text(draw, (548, 318), "{ }", row_font, DIM)
    else:
        lines = ["{"] + [f"  {key}: {out}" + ("," if i < len(written) - 1 else "") for i, (key, _src, out) in enumerate(written)] + ["}"]
        for i, line in enumerate(lines):
            line_color = GREEN if finished else (AMBER if i == len(lines) - 2 else INK)
            text(draw, (548, 252 + i * 32), line, row_font, line_color)

    rounded(draw, (40, 468, 940, 528), 12, CARD, CARD_EDGE, 2)
    if step < 0:
        status = "Each mapper call must return an object. Those objects are merged."
        color = MUTED
    elif step < 3:
        key, src, out = ITEMS[step]
        if phase < 0.55:
            status = f"Entry {step}: value = {src}, key = {key}"
            color = AMBER
        else:
            status = f"Mapper returns {{ {key}: {out} }}. Merge it into the result."
            color = GREEN
    else:
        status = "Returns { apple: 4, bread: 6, milk: 8 }. cart is unchanged."
        color = GREEN
    text(draw, (56, 486), status, small, color)

    count = 0 if step < 0 else (3 if finished else step + (1 if phase >= 0.55 else 0))
    pill_color = GREEN if finished else CYAN
    rounded(draw, (844, 26, 940, 64), 12, CARD, pill_color, 2)
    text(draw, (866, 36), f"{count}/3", badge, pill_color)

    return image


def build_frames():
    frames = []
    durations = []

    def add(step, phase, ms, repeats=1):
        img = frame(step, phase)
        for _ in range(repeats):
            frames.append(img)
            durations.append(ms)

    add(-1, 0, 140, 8)
    for step in range(3):
        for phase in (0.0, 0.25, 0.7, 1.0):
            add(step, phase, 160, 3)
        add(step, 1.0, 180, 4)
    add(3, 1, 180, 10)
    return frames, durations


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    frames, durations = build_frames()
    frames[0].save(
        OUT,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        optimize=True,
        disposal=2,
    )
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes, {len(frames)} frames)")


if __name__ == "__main__":
    main()
