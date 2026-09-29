#!/usr/bin/env python3
"""Render a DataWeave filterObject walkthrough as an animated GIF."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 980, 560
OUT = Path(__file__).resolve().parents[1] / "assets" / "filterObject.gif"

BG = (15, 23, 42)
CARD = (30, 41, 59)
CARD_EDGE = (51, 65, 85)
INK = (248, 250, 252)
MUTED = (148, 163, 184)
DIM = (100, 116, 139)
CYAN = (56, 189, 248)
AMBER = (251, 191, 36)
GREEN = (74, 222, 128)
RED = (248, 113, 113)
ACTIVE = (23, 55, 94)
DONE = (20, 55, 42)
DROP = (55, 28, 36)

FONT = "/usr/share/fonts/truetype/macos/Inter-Regular.ttf"
FONT_MED = "/usr/share/fonts/truetype/macos/Inter-Medium.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/macos/Inter-Bold.ttf"
MONO = "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-Medium.ttf"

# key, value, kept
ITEMS = [("apple", 2, False), ("bread", 3, True), ("milk", 4, True)]


def font(path, size):
    return ImageFont.truetype(path, size)


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text(draw, xy, content, face, fill):
    draw.text(xy, content, font=face, fill=fill)


def kept_through(step, phase):
    """Entries already accepted into the result."""
    if step < 0:
        return []
    limit = 3 if step >= 3 else step + (1 if phase >= 0.55 else 0)
    return [item for item in ITEMS[:limit] if item[2]]


def frame(step, phase):
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)

    title = font(FONT_BOLD, 32)
    subtitle = font(FONT, 17)
    label = font(FONT_MED, 15)
    mono = font(MONO, 17)
    row_font = font(MONO, 22)
    small = font(FONT, 16)
    badge = font(FONT_MED, 14)

    text(draw, (40, 24), "filterObject", title, INK)
    text(
        draw,
        (40, 66),
        "DataWeave keeps entries whose test is true and returns an object.",
        subtitle,
        MUTED,
    )

    rounded(draw, (40, 108, 940, 164), 12, CARD, CARD_EDGE, 2)
    text(draw, (56, 126), "cart filterObject (value, key) -> value > 2", mono, CYAN)

    rounded(draw, (40, 186, 470, 448), 16, CARD, CARD_EDGE, 2)
    rounded(draw, (510, 186, 940, 448), 16, CARD, CARD_EDGE, 2)
    text(draw, (60, 200), "cart", label, MUTED)
    text(draw, (530, 200), "result", label, MUTED)

    finished = step >= 3
    kept = kept_through(step, phase)

    for index, (key, value, keep) in enumerate(ITEMS):
        y = 238 + index * 64
        box = (60, y, 450, y + 52)
        decided = finished or index < step or (index == step and phase >= 0.55)
        active = index == step and not finished and phase < 0.55
        if active:
            fill, edge, color = ACTIVE, AMBER, AMBER
        elif decided and keep:
            fill, edge, color = DONE, GREEN, GREEN
        elif decided and not keep:
            fill, edge, color = DROP, RED, RED
        else:
            fill, edge, color = (15, 23, 42), CARD_EDGE, INK
        rounded(draw, box, 10, fill, edge, 2)
        text(draw, (76, y + 12), f"{key}: {value}", row_font, color)

    if finished:
        result_fill, result_edge = DONE, GREEN
    elif kept:
        result_fill, result_edge = CARD, AMBER
    else:
        result_fill, result_edge = CARD, CARD_EDGE
    rounded(draw, (530, 238, 920, 430), 10, result_fill, result_edge, 2)

    if not kept:
        text(draw, (548, 318), "{ }", row_font, DIM)
    else:
        lines = ["{"]
        for i, (key, value, _keep) in enumerate(kept):
            comma = "," if i < len(kept) - 1 else ""
            lines.append(f"  {key}: {value}{comma}")
        lines.append("}")
        for i, line in enumerate(lines):
            newest = i == len(lines) - 2 and not finished
            line_color = GREEN if finished else (AMBER if newest else INK)
            text(draw, (548, 268 + i * 32), line, row_font, line_color)

    rounded(draw, (40, 468, 940, 528), 12, CARD, CARD_EDGE, 2)
    if step < 0:
        status = "The test receives each value. Only passing entries are copied."
        color = MUTED
    elif step < 3:
        key, value, keep = ITEMS[step]
        if phase < 0.55:
            status = f"Test {key}: {value} > 2"
            color = AMBER
        elif keep:
            status = f"{value} > 2 is true. Keep {{ {key}: {value} }}."
            color = GREEN
        else:
            status = f"{value} > 2 is false. Drop {key}."
            color = RED
    else:
        status = "Returns { bread: 3, milk: 4 }. cart is unchanged."
        color = GREEN
    text(draw, (56, 486), status, small, color)

    pill = f"{len(kept)} kept"
    pill_color = GREEN if finished else CYAN
    rounded(draw, (812, 26, 940, 64), 12, CARD, pill_color, 2)
    text(draw, (834, 36), pill, badge, pill_color)

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
