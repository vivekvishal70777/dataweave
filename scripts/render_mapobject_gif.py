#!/usr/bin/env python3
"""Render an animation of mapObject walking an object and returning a new one."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 960, 540
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

    title = font(FONT_BOLD, 34)
    subtitle = font(FONT, 18)
    label = font(FONT_MED, 15)
    mono = font(MONO, 20)
    row_font = font(MONO, 22)
    small = font(FONT, 16)
    badge = font(FONT_MED, 14)

    text(draw, (48, 28), "mapObject", title, INK)
    text(
        draw,
        (48, 74),
        "Walk each entry, run an operation, return a new object.",
        subtitle,
        MUTED,
    )

    rounded(draw, (48, 118, 912, 176), 12, CARD, CARD_EDGE, 2)
    text(draw, (68, 134), "mapObject(cart, (price) => price * 2)", mono, CYAN)

    # Columns
    left = (48, 200, 468, 430)
    right = (492, 200, 912, 430)
    rounded(draw, left, 16, CARD, CARD_EDGE, 2)
    rounded(draw, right, 16, CARD, CARD_EDGE, 2)
    text(draw, (72, 214), "cart", label, MUTED)
    text(draw, (516, 214), "result", label, MUTED)

    active_index = step if 0 <= step <= 2 else None
    finished = step >= 3
    written = ITEMS[: step + 1] if 0 <= step <= 2 else (ITEMS if finished else [])
    # During the approach phase, the result row is not written yet.
    if step in (0, 1, 2) and phase < 0.55:
        written = ITEMS[:step]

    def draw_rows(origin_x, values, side):
        for index, (key, src, out) in enumerate(ITEMS):
            y = 252 + index * 52
            box = (origin_x, y, origin_x + 372, y + 44)
            is_active = side == "in" and index == active_index and not finished
            is_written = side == "out" and any(item[0] == key for item in written)
            is_focus_out = side == "out" and index == active_index and phase >= 0.55 and not finished
            if finished and side == "out":
                fill, edge, color = DONE, GREEN, GREEN
            elif is_active or is_focus_out:
                fill, edge, color = ACTIVE, AMBER, AMBER
            elif is_written:
                fill, edge, color = DONE, GREEN, GREEN
            else:
                fill, edge, color = (15, 23, 42), CARD_EDGE, DIM if side == "out" else INK
            rounded(draw, box, 10, fill, edge, 2)
            shown = out if side == "out" and (is_written or is_focus_out or finished) else src
            if side == "out" and not (is_written or is_focus_out or finished):
                label_text = "·"
                color = DIM
            else:
                label_text = f"{key}: {shown}"
            text(draw, (origin_x + 16, y + 9), label_text, row_font, color)

    draw_rows(72, ITEMS, "in")
    draw_rows(516, ITEMS, "out")

    # Footer status
    rounded(draw, (48, 452, 912, 508), 12, CARD, CARD_EDGE, 2)
    if step < 0:
        status = "Input stays unchanged. Result starts empty."
        color = MUTED
    elif step < 3:
        key, src, out = ITEMS[step]
        if phase < 0.55:
            status = f"Visit {key}. operation({src}) is next."
            color = AMBER
        else:
            status = f"operation({src}) → {out}. Store {key}: {out}."
            color = GREEN
    else:
        status = "Returns { apple: 4, bread: 6, milk: 8 }."
        color = GREEN
    text(draw, (68, 468), status, small, color)

    count = 0 if step < 0 else (3 if finished else step + (1 if phase >= 0.55 else 0))
    pill = f"{count}/3"
    rounded(draw, (820, 32, 912, 70), 12, CARD, CYAN if not finished else GREEN, 2)
    text(draw, (842, 42), pill, badge, CYAN if not finished else GREEN)

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
