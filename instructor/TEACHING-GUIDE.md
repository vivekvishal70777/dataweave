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
| Resources per section | Zip of `student/labs/<that-section>/` + `student/quizzes/` (no answers) |
| Interview bootcamp resource | **`student/resources/bootcamp-prompts.md` only** (Set B, 80 questions, no answers) |
| Article lectures | Easy tutorials: `student/tutorials/<section>/`. Do **not** attach `sections/*/LECTURE.md` or `reference/*Interview-Questions*` — those contain full answers. |
| Captions / slides | Optional; cheat sheet `student/resources/cheat-sheet.md` |

**Never** attach `instructor/`, `reference/MuleSoft-DataWeave-Interview-Questions.md`, or quiz `ANSWER-KEY.md` as early-section resources.

Answers for the 80 questions: **your voice after the pause card**, or an optional last lecture “answer key pack” (same idea as lab solutions).

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

## Interview Q&A appears twice — record it once

The same 80 questions show up in **topic `LECTURE.md` files** and again as the **full bank** in `reference/MuleSoft-DataWeave-Interview-Questions.md`. That is a **study aid**, not two courses.

| Place | Student job | You record |
| --- | --- | --- |
| Sections 2–12 (and industry) | Learn the idea, then code a lab | Concept → demo → pause → lab solution → quiz. Mention the interview phrasing in 20–40 seconds (“If they ask how `map` differs from `filter`…”). |
| Easy tutorials | Read before the video | Optional Udemy **Articles**. Not a second video. |
| Section quizzes | Check memory | Udemy practice tests. |
| Interview bootcamp (last section) | Speak **Set B** prompts under time | Do not attach course Q&A. Model answers after pause from `instructor/bootcamp/BOOTCAMP-QA.md`. |

If you filmed every Q as its own bootcamp lecture you would duplicate ~80 videos and students would skip the real labs.

### Topic-section close (say this, then stop)

“That is also interview question N. In an interview, say: …” — one sentence from the Q&A — then the pause card for the lab.

### Bootcamp recording order

1. Article: how to drill. Attach `student/resources/bootcamp-prompts.md` (**Set B, no answers**). Never attach `BOOTCAMP-QA.md` or the course Q&A file.
2. Video: you ask ~8 mixed questions; pause; model 60-second answers. No Playground.
3. Video: 3 timed whiteboard labs (from `student/resources/whiteboard.md`). Pause before each solution.
4. Video: Q60 as an 8-beat **design** talk (they already built Labs 41 and 54).
5. Final practice test.

Students close solutions. You are the interviewer, not a second teacher.

## Regenerating content

Edit `reference/*.md`, then:

```bash
python3 scripts/generate_udemy_labs.py
python3 scripts/generate_udemy_lectures.py
python3 scripts/generate_easy_tutorials.py
python3 scripts/generate_bootcamp_set_b.py
```

Re-zip student resources after regenerate. Section quizzes in `student/quizzes/` are hand-written — update those if you change a concept.
