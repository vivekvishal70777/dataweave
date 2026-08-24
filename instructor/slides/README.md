# Recording slides

HTML decks for every concept lecture, lab video, section opener, mapping cluster, and easy tutorial.

**For screen share, use the PowerPoint files** in [`pptx/`](pptx/README.md) — open, press F5, share the window.

Browser decks: open [`index.html`](index.html) full screen (**F**). Rebuild:

```bash
python3 scripts/generate_slides.py
python3 scripts/generate_pptx.py
```

## How to present

| Key | Action |
| --- | --- |
| → ← Space Enter | Next / previous slide |
| F | Fullscreen |
| N | Speaker notes (the **SAY** text) |
| Home / End | First / last slide |
| Click | Next (right 78%) or previous (left 22%) |

Pause cards are amber. Do not advance to the solution until students have had a beat.

## Layout

| Folder | Source |
| --- | --- |
| `sections/` | `sections/*/LECTURE.md` — section opener |
| `lectures/` | `instructor/transcripts/lectures/` plus mapping cluster decks |
| `labs/` | `instructor/transcripts/labs/` |
| `tutorials/` | `student/tutorials/` — article walkthroughs |

These files are instructor-only. Do not zip them into the student download.
