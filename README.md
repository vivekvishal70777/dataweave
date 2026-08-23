# DataWeave 2.0 — Udemy course materials

Teach **Mule 4 / DataWeave 2.x** as a linear online course: concept videos, then a lab, then a quiz. This repo is the **curriculum + student resources + instructor solutions**, not a Mule application.

## How the course is organized

| Folder | Who uses it | What it is |
| --- | --- | --- |
| `student/` | Learners (Udemy downloadable resources) | Starter labs, quizzes (no answers), getting-started guide |
| `instructor/` | You, while recording | Solutions, quiz keys, curriculum, recording notes |
| `sections/` | You + optional article lectures | One `LECTURE.md` per Udemy section (objectives, talking points, full Q&A to teach) |
| `reference/` | Archive | Original 80 interview Q&A, 58 programming drills |

**Do not zip `instructor/` into the student resource pack on Udemy.** Publish `student/` (and optionally `sections/` as reading). Keep solutions for after-try videos or a separate “solutions” lecture at the end of each section.

## Suggested Udemy path

1. **Welcome** — playground setup, how labs work.
2. **Fundamentals → arrays → objects → strings** — Easy labs 01–18.
3. **JSON / XML / CSV** — format switch demos.
4. **Intermediate transforms** — `groupBy`, `reduce`, `flatMap`, `update`.
5. **Dates, `match`, `try`**.
6. **Joins and Mule context** (`vars`, modules, no N+1 `lookup`).
7. **Advanced recursion, namespaces, capstone invoice**.
8. **Production / streaming / performance**.
9. **Interview bootcamp** — 60 questions out loud + 6 whiteboard programs.

Full recording order: [`instructor/CURRICULUM.md`](instructor/CURRICULUM.md).

Marketplace title, outcomes, and section list for the Udemy form: [`instructor/UDEMY-LISTING.md`](instructor/UDEMY-LISTING.md).

How to record, pause for practice, and package resources: [`instructor/TEACHING-GUIDE.md`](instructor/TEACHING-GUIDE.md).

Spoken scripts for every concept lecture and every lab video: [`instructor/transcripts/README.md`](instructor/transcripts/README.md).

Easy-word tutorials (one file per topic, per section): [`student/tutorials/README.md`](student/tutorials/README.md).

Copyright / Udemy rights (original labs vs third-party books): [`instructor/PUBLISHING-RIGHTS.md`](instructor/PUBLISHING-RIGHTS.md).

## Student quick start

1. Read [`student/00-getting-started.md`](student/00-getting-started.md).
2. Open [`student/tutorials/README.md`](student/tutorials/README.md) and read the easy concept pages for that section.
3. Open [`student/labs/README.md`](student/labs/README.md).
4. For each lab: paste `input.json` (or `input.txt`) into [DataWeave Playground](https://dataweave.mulesoft.com/learn/) or Transform Message, then complete `transform.dwl`.
5. Take the section quiz under [`student/quizzes/`](student/quizzes/).

## Regenerating labs and lectures

If you edit the files in `reference/`, rebuild:

```bash
python3 scripts/generate_udemy_labs.py
python3 scripts/generate_udemy_lectures.py
python3 scripts/generate_easy_tutorials.py
```

## Source material

- 80 theory questions: `reference/MuleSoft-DataWeave-Interview-Questions.md`
- 58 coding drills: `reference/DataWeave-Programming-Questions.md`

Aligned with **DataWeave 2.x / Mule 4** production interviews (`update`, `leftJoin`, `divideBy` need **Mule 4.3+**). Labs use Salesforce-shaped JSON, SOAP/XML, dirty CSV, and CDC diffs — not toy `{ "a": 1 }` examples.
