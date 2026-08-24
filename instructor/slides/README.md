# Recording slides

HTML decks for every concept lecture, lab video, section opener, mapping cluster, and easy tutorial.

Open [`index.html`](index.html) in a browser, go full screen (**F**), and walk the deck while you record. Rebuild after transcript or tutorial edits:

```bash
python3 scripts/generate_slides.py
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
