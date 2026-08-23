# Teaching guide (instructor)

## Pedagogy (keep every section to this loop)

1. **Hook (30–60s)** — a before/after payload (ugly input → clean API JSON).
2. **Concept (3–7 min)** — one idea; use the easy tutorial in `student/tutorials/<section>/` then the Q&A in `sections/*/LECTURE.md`.
3. **Live demo (5–10 min)** — start from the **student starter**, not the finished script.
4. **Pause card** — “Pause and try Lab NN. Resume when you have an attempt.”
5. **Solution recap (3–6 min)** — open `instructor/solutions`, compare 1–2 student pitfalls.
6. **Quiz** — Udemy practice test from `instructor/quizzes/ANSWER-KEY.md` (student copy has no answers).

Do not paste full solutions on screen before the pause. Udemy students binge; the pause card is the course.

Before you hit publish: you do **not** need a license from MuleSoft or a book author for **your** DataWeave labs and Q&A. You **must not** upload anyone else’s book or PDF. Details: [`PUBLISHING-RIGHTS.md`](PUBLISHING-RIGHTS.md).

## What to upload on Udemy

| Udemy field | File |
| --- | --- |
| Curriculum sections / lectures | `instructor/CURRICULUM.md` |
| Landing page copy | `instructor/UDEMY-LISTING.md` |
| Resources per section | Zip of `student/labs/<that-section>/` + `student/quizzes/` |
| Article lectures | Easy tutorials: `student/tutorials/<section>/` (one page per topic). Longer Q&A: `sections/*/LECTURE.md` |
| Captions / slides | Optional; cheat sheet `student/resources/cheat-sheet.md` |

**Never** attach `instructor/solutions` or `ANSWER-KEY.md` as early-section resources. Options:

- End-of-section lecture: “Solutions pack” download, **or**
- Only show solutions on camera.

## Recording setup

- Editor font ≥ 16px; hide `instructor/` in the file tree while recording student view.
- Dual monitor: Playground on the right, `LECTURE.md` talking points on the left.
- Name videos: `S02-L03-script-structure.mp4` matching curriculum order.
- Coding videos: aim **under 12 minutes**. Split Lab 54 / Q60 if needed.
- Read the spoken script from [`transcripts/README.md`](transcripts/README.md) — one file per concept lecture and one file per lab.

## Per-lab on-camera pattern

1. Run starter (`payload` passthrough) — show it is wrong.
2. Write the header out loud (`%dw 2.0`, `output`, `---`).
3. Build the body in 2–3 saves (filter, then map, then fields).
4. Call out the interview phrase (`$` vs named args, `default` vs `try`, streaming).

## Homework load

After each teaching section, assign **2 or 3 labs** not fully demoed. Next video: 5-minute recap of the one with most mistakes (`flatMap`, `groupBy`+`sum`, recursive mask).

## Interview bootcamp section

Students close the IDE solutions. You pick 5 from the whiteboard table in `student/resources/whiteboard.md`. Timebox 8 minutes per problem. Then walk the reference solution.

## Regenerating content

Edit `reference/*.md`, then:

```bash
python3 scripts/generate_udemy_labs.py
python3 scripts/generate_udemy_lectures.py
```

Re-zip student resources after regenerate. Section quizzes in `student/quizzes/` are hand-written — update those if you change a concept.
