# Ready-to-share PowerPoint

Simple **16:9** `.pptx` files for screen share. Open the matching file, press **F5** (Slide Show), and share that window.

Rebuild:

```bash
python3 scripts/generate_pptx.py
```

Needs `python-pptx` (`pip install python-pptx`).

## What to open while you record

| You are recording | Open |
| --- | --- |
| Section intro | `pptx/sections/` |
| Concept video | `pptx/lectures/Lxx.pptx` |
| Mapping cluster A–D | `pptx/lectures/S14-*.pptx` |
| Lab 01–88 | `pptx/labs/` |
| Article voiceover | `pptx/tutorials/` |

Pause cards are amber and show a pause illustration. Title and concept slides carry a topic picture on the right. Code slides stay text-only so the script stays readable.

HTML versions (browser) live in the parent `slides/` folder.
