#!/usr/bin/env python3
"""Build simple 16:9 PowerPoint decks for screen-share recording."""
from __future__ import annotations

import re
import sys
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import generate_slides as gs  # noqa: E402

OUT = ROOT / "instructor" / "slides" / "pptx"

NAVY = RGBColor(0x0F, 0x27, 0x44)
NAVY_DEEP = RGBColor(0x0A, 0x1B, 0x30)
AMBER_BG = RGBColor(0x3D, 0x29, 0x10)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
MUTED = RGBColor(0xB7, 0xCB, 0xDE)
ACCENT = RGBColor(0x3E, 0xC6, 0xFF)
AMBER = RGBColor(0xFF, 0xB0, 0x20)
CODE_BG = RGBColor(0x06, 0x12, 0x1C)
CODE_FG = RGBColor(0xD7, 0xE8, 0xF5)

W = Inches(13.333)
H = Inches(7.5)


def strip_md(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def set_run(run, size: int, color: RGBColor, bold: bool = False, font: str = "Calibri") -> None:
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.name = font


def fill_shape(shape, color: RGBColor) -> None:
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()


def add_notes(slide, notes: str) -> None:
    if not notes:
        return
    tf = slide.notes_slide.notes_text_frame
    tf.text = notes


def new_slide(prs: Presentation, bg: RGBColor):
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
    fill_shape(slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, H), bg)
    return slide


def kicker_box(slide, text: str, color: RGBColor) -> None:
    box = slide.shapes.add_textbox(Inches(0.7), Inches(0.28), Inches(12), Inches(0.4))
    p = box.text_frame.paragraphs[0]
    p.text = text.upper()
    set_run(p.runs[0], 14, color, bold=True)
    p.runs[0].font.name = "Calibri"


def title_box(slide, text: str, top: float, size: int = 36) -> None:
    box = slide.shapes.add_textbox(Inches(0.7), Inches(top), Inches(12), Inches(1.6))
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = strip_md(text)
    set_run(p.runs[0], size, WHITE, bold=True)


def bullets_box(slide, bullets: list[str], top: float, color: RGBColor = WHITE) -> None:
    box = slide.shapes.add_textbox(Inches(0.85), Inches(top), Inches(11.6), Inches(5.2))
    tf = box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = "•  " + strip_md(item)
        p.space_after = Pt(14)
        set_run(p.runs[0], 24, color)


def code_box(slide, code: str) -> None:
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(2.05), Inches(11.9), Inches(4.7)
    )
    fill_shape(shape, CODE_BG)
    tf = shape.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.28)
    tf.margin_top = Inches(0.18)
    lines = code.rstrip().splitlines() or [""]
    # Keep on one screen: drop extra lines rather than shrink to unreadability.
    if len(lines) > 16:
        lines = lines[:15] + ["…"]
    size = 16 if len(lines) <= 10 else 13 if len(lines) <= 14 else 12
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line if line else " "
        p.space_after = Pt(2)
        set_run(p.runs[0], size, CODE_FG, font="Consolas")


def title_slide(prs: Presentation, item: dict) -> None:
    slide = new_slide(prs, NAVY)
    kicker_box(slide, item["kicker"], ACCENT)
    title_box(slide, item["heading"], 2.1, 44)
    if item.get("subtitle"):
        box = slide.shapes.add_textbox(Inches(0.7), Inches(4.0), Inches(11.8), Inches(1.2))
        tf = box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = strip_md(item["subtitle"])
        set_run(p.runs[0], 20, MUTED)
    chips = item.get("chips") or []
    if chips:
        box = slide.shapes.add_textbox(Inches(0.7), Inches(5.5), Inches(12), Inches(0.5))
        p = box.text_frame.paragraphs[0]
        p.text = "   ·   ".join(strip_md(c) for c in chips)
        set_run(p.runs[0], 16, ACCENT)
    add_notes(slide, item.get("notes", ""))


def content_slide(prs: Presentation, item: dict) -> None:
    pause = item["kind"] == "pause"
    slide = new_slide(prs, AMBER_BG if pause else NAVY)
    kicker_box(slide, item["kicker"], AMBER if pause else ACCENT)
    title_box(slide, item["heading"], 0.75, 32)
    if item["kind"] == "code" and item.get("code"):
        code_box(slide, item["code"])
    elif item.get("heading") == "The loop":
        bullets_box(
            slide,
            [
                "Concept — one idea, 3–7 minutes",
                "Pause — hold the card, students try",
                "Lab — type from the starter, not the solution",
                "Quiz — Udemy practice test, no video",
            ],
            2.5,
        )
    elif item.get("bullets"):
        bullets_box(slide, item["bullets"], 2.5, AMBER if pause else WHITE)
    add_notes(slide, item.get("notes", ""))


def write_pptx(path: Path, deck: gs.Deck) -> None:
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H
    items = deck.items or [
        {
            "kind": "title",
            "heading": deck.title,
            "kicker": deck.kicker,
            "subtitle": "",
            "chips": [],
            "notes": "",
            "bullets": [],
            "code": "",
        }
    ]
    for item in items:
        if item["kind"] == "title":
            title_slide(prs, item)
        else:
            content_slide(prs, item)
    path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(path))


def main() -> None:
    n = 0
    for sid, title in gs.SECTION_FOLDERS:
        lec = gs.SECTIONS / sid / "LECTURE.md"
        if lec.exists():
            write_pptx(OUT / "sections" / f"{sid}.pptx", gs.section_overview_deck(lec))
            n += 1

    for path in sorted((gs.TRANSCRIPTS / "lectures").glob("L*.md")):
        write_pptx(OUT / "lectures" / f"{path.stem}.pptx", gs.lecture_deck(path))
        n += 1

    for dest, deck in gs.mapping_cluster_decks():
        write_pptx(OUT / "lectures" / f"{dest.stem}.pptx", deck)
        n += 1

    for path in sorted((gs.TRANSCRIPTS / "labs").glob("*.md")):
        write_pptx(OUT / "labs" / f"{path.stem}.pptx", gs.lab_deck(path))
        n += 1

    for sid, title in gs.SECTION_FOLDERS:
        tdir = gs.TUTORIALS / sid
        if not tdir.is_dir():
            continue
        for path in sorted(tdir.glob("*.md")):
            if path.name.lower() == "readme.md":
                continue
            write_pptx(
                OUT / "tutorials" / sid / f"{path.stem}.pptx",
                gs.tutorial_deck(path, title),
            )
            n += 1

    print(f"Wrote {n} PowerPoint files under {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
