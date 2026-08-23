#!/usr/bin/env python3
"""Split interview Q&A into Udemy section lecture articles."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from bootcamp_set_b import ITEMS as SET_B

SRC = ROOT / "reference" / "MuleSoft-DataWeave-Interview-Questions.md"

# Udemy section -> inclusive question numbers + student lab numbers
SECTIONS = [
    {
        "id": "01-welcome-and-setup",
        "title": "Welcome and setup",
        "qs": [],
        "labs": [],
        "objectives": [
            "Know how this course is sequenced (concept → demo → lab → quiz).",
            "Set up DataWeave Playground or Anypoint Studio Transform Message.",
            "Use starter labs without opening solutions first.",
        ],
        "talking": [
            "Welcome students; state the outcome: write DataWeave 2.0 for Mule 4 interviews and real mappings.",
            "Show the repo folders: student/labs vs instructor/solutions.",
            "Demo opening Lab 01 starter in the Playground.",
        ],
    },
    {
        "id": "02-dataweave-fundamentals",
        "title": "DataWeave 2.0 fundamentals",
        "qs": list(range(1, 8)),
        "labs": [3, 5, 8, 13],
        "objectives": [
            "Describe DataWeave and the Mule 4 script header.",
            "Declare `var` and `fun`, and coerce types with `as`.",
            "Contrast DataWeave 1.0 and 2.0 at interview level.",
        ],
        "talking": [
            "Record one short video per question cluster: what DW is, 1 vs 2, script shape, vars, functions, types, `as`.",
            "Live-type the hello-world script from Q3.",
        ],
    },
    {
        "id": "03-arrays-and-core-operators",
        "title": "Arrays: map, filter, and indexes",
        "qs": [8, 15, 35],
        "labs": [1, 2, 9, 10, 14, 15],
        "objectives": [
            "Use `map`, `filter`, `$` / `$$`, `sizeOf`, `isEmpty`, and `flatten`.",
            "Explain when named lambda parameters are clearer than `$`.",
        ],
        "talking": [
            "Demo Lab 01 (map shape) and Lab 02 (filter) on camera.",
            "Assign Labs 09–10, 14–15 as homework.",
        ],
    },
    {
        "id": "04-objects-nulls-and-selectors",
        "title": "Objects, nulls, and selectors",
        "qs": [9, 11, 13, 20, 21],
        "labs": [4, 5, 16, 18],
        "objectives": [
            "Choose `.` vs `[]` vs `.*` vs `..`.",
            "Handle missing data with `default` and `?`.",
            "Transform objects with `mapObject` and `pluck`.",
        ],
        "talking": [
            "Whiteboard the selector table from Q13.",
            "Show `skipNullOn` from Q20 as a writer-property demo.",
        ],
    },
    {
        "id": "05-strings-numbers-conditionals",
        "title": "Strings, numbers, and conditionals",
        "qs": [10, 12, 16, 19],
        "labs": [6, 7, 8, 13, 17],
        "objectives": [
            "Concatenate with `++` vs add with `+`.",
            "Split, join, and change case.",
            "Write if/else expressions (no Java ternary).",
        ],
        "talking": [
            "Trap: `+` on strings. Demo the error, then fix with `++`.",
            "Lab 13 HTTP retry class is the if/else pattern. Mention `write`/`read` (Q19) as a production follow-up.",
        ],
    },
    {
        "id": "06-json-xml-csv",
        "title": "JSON, XML, and CSV mappings",
        "qs": [14, 31, 32, 33],
        "labs": [11, 12, 29, 30],
        "objectives": [
            "Change `output` MIME type and produce a single XML root.",
            "Read and write XML attributes.",
            "Round-trip CSV with headers and number coercion.",
        ],
        "talking": [
            "JSON to XML (single root). SOAP/namespaces wait until the advanced section.",
            "Stress: XML needs one root; CSV keys become headers.",
        ],
    },
    {
        "id": "07-intermediate-transforms",
        "title": "Group, reduce, merge, and update",
        "qs": [22, 23, 24, 25, 26, 27, 36],
        "labs": [19, 20, 21, 22, 23, 24, 25, 26, 35, 36],
        "objectives": [
            "Use `groupBy`, `orderBy`, `distinctBy`, `reduce`, and `flatMap`.",
            "Merge objects and update nested fields.",
            "Scope locals with `do`.",
        ],
        "talking": [
            "Hero demo: Lab 20 totals per customer (coerce string amounts), then Lab 23 flatMap lines.",
            "Show `update` and mention Mule 4.3+ (Q26).",
        ],
    },
    {
        "id": "08-dates-match-and-errors",
        "title": "Dates, pattern matching, and try",
        "qs": [28, 29, 30],
        "labs": [27, 28, 33, 52],
        "objectives": [
            "Parse and format dates; use period literals.",
            "Pattern-match with `match`.",
            "Catch coercion errors with `try` / `orElse` (not Mule error handlers).",
        ],
        "talking": [
            "Lab 27 mixed dates is the interview favorite — type it slowly.",
            "Contrast `default` (nulls) vs `try` (errors).",
        ],
    },
    {
        "id": "09-joins-modules-mule-context",
        "title": "Joins, modules, and Mule context",
        "qs": [17, 18, 34, 37, 38, 39, 40],
        "labs": [31, 32, 34, 45],
        "objectives": [
            "Read `vars`, `attributes`, and properties.",
            "Import modules and join arrays (or index with `groupBy`).",
            "Know when not to call Java or `lookup` inside `map`.",
        ],
        "talking": [
            "Lab 32 (join via groupBy) after Lab 31 (leftJoin) — same result, better interview story.",
            "Warn about N+1 `lookup` (Q40).",
        ],
    },
    {
        "id": "10-advanced-recursion-and-xml-ns",
        "title": "Advanced: recursion, namespaces, diffs",
        "qs": [41, 42, 43, 44, 47, 48, 49, 50, 51, 54, 55, 56, 57],
        "labs": [37, 38, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 51, 53, 54],
        "objectives": [
            "Walk trees with `match` + recursion.",
            "Read/write namespaced XML.",
            "Build diffs, org charts, and invoice totals.",
        ],
        "talking": [
            "Split into 4–5 videos: recursion, SOAP ns (Lab 41), dynamic keys, capstone invoice (Lab 54).",
            "Lab 39 PII mask as a production story.",
        ],
    },
    {
        "id": "11-performance-and-production",
        "title": "Streaming, crypto, modules, and pitfalls",
        "qs": [41, 45, 46, 52, 53, 58],
        "labs": [45],
        "objectives": [
            "Name what breaks DataWeave streaming.",
            "Hash vs HMAC; binary/Base64 care.",
            "Extract a reusable `.dwl` module.",
        ],
        "talking": [
            "Whiteboard the performance list from Q58 — this is a closing-section video.",
            "Optional: show a tiny Pricing.dwl module (Q46).",
        ],
    },
    {
        "id": "13-industry-operators-and-mule-message",
        "title": "Industry operators, message, and MIME",
        "qs": list(range(61, 81)),
        "labs": [55, 56, 57, 58],
        "objectives": [
            "Use Arrays helpers: maxBy, firstWith, zip, ranges.",
            "Shift timezones; replace/find; Transform Message multiple targets.",
            "Distinguish try vs Mule On Error, Java MIME, and DW vs Batch vs For Each.",
        ],
        "talking": [
            "These are the production topics the first 60 questions only hinted at.",
            "Demo Lab 55 (maxBy) and Lab 56 (IST). Assign zip and TM dual-target as homework.",
        ],
    },
    {
        "id": "12-interview-bootcamp",
        "title": "Interview bootcamp",
        "qs": list(range(1, 81)),
        "labs": [20, 23, 32, 39, 41, 53, 54],
        "objectives": [
            "Answer the 80-question bank out loud.",
            "Whiteboard the six signature programs.",
            "Talk through the nested XML → JSON design (Q60).",
        ],
        "talking": [
            "Do not re-teach Q1–80. Those answers were already taught in sections 2–12.",
            "Record timed drills: verbal flashcards, then whiteboard labs, then Q60 as a design talk.",
        ],
        "qa_mode": "drill",
    },
]


def parse_questions(text: str) -> dict[int, tuple[str, str]]:
    parts = re.split(r"^### (\d+)\. (.+)$", text, flags=re.M)
    out: dict[int, tuple[str, str]] = {}
    i = 1
    while i + 2 < len(parts):
        num = int(parts[i])
        title = parts[i + 1].strip()
        body = parts[i + 2]
        nxt = re.search(r"^## ", body, re.M)
        if nxt:
            body = body[: nxt.start()]
        out[num] = (title, body.strip().strip("-").strip())
        i += 3
    return out


def write_section(sec: dict, questions: dict[int, tuple[str, str]]) -> None:
    d = ROOT / "sections" / sec["id"]
    d.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# Section — {sec['title']}",
        "",
        "Use this file as the **article lecture** and recording outline on Udemy.",
        "",
        f"**Easy-word tutorials (one page per topic):** [`../../student/tutorials/{sec['id']}/README.md`](../../student/tutorials/{sec['id']}/README.md) (copies also in `tutorials/` next to this file).",
        "",
        "## Learning objectives",
        "",
    ]
    for o in sec["objectives"]:
        lines.append(f"- {o}")
    lines += ["", "## Suggested video breakdown", ""]
    for t in sec["talking"]:
        lines.append(f"- {t}")
    if sec["labs"]:
        lines += [
            "",
            "## Labs in this section",
            "",
            "Student starters live under `student/labs/`.",
            "",
        ]
        for n in sec["labs"]:
            lines.append(f"- Lab {n:02d}")
    qa_mode = sec.get("qa_mode", "full" if sec["qs"] else "none")
    if qa_mode == "drill":
        lines += [
            "",
            "## This is not a second teaching pass",
            "",
            "Q1–80 already appear in **topic sections** (easy tutorial → concept video → demo → lab → quiz).",
            "Do **not** record another 80 videos here. Students drill from **prompts only** (no answer key in the zip).",
            "",
            "Students drill **Set B**: `student/resources/bootcamp-prompts.md` (questions only).",
            "Your answers while recording: `instructor/bootcamp/BOOTCAMP-QA.md`. Never zip that file.",
            "",
            "The course bank (`reference/MuleSoft-DataWeave-Interview-Questions.md`) was already taught in sections 2–12.",
            "",
            "### What to publish in this section",
            "",
            "1. **Article** — how to drill. Attach **`student/resources/bootcamp-prompts.md` only** (Set B, no answers).",
            "2. **Video: verbal mock** — you ask 8 mixed questions (easy + hard). Pause card after each prompt. Then you give a model 60-second answer. Do not open Studio.",
            "3. **Video: whiteboard** — timebox 8 minutes each on Labs 23, 20, 32, 39, 41, 53/54 (pick 3 on camera; assign the rest).",
            "4. **Video: Q60 design talk** — eight beats only (reader, types, money, join, shape, writer, try, scale). They already coded Lab 41 + 54.",
            "5. **Practice test** — final quiz, not a lecture.",
            "",
            "### Set B checklist (titles only — answers in instructor/bootcamp/BOOTCAMP-QA.md)",
            "",
        ]
        for n, title, _ans in SET_B:
            lines.append(f"- B{n}. {title}")
        lines.append("")
    elif sec["qs"]:
        lines += [
            "",
            "## Interview talking points for this section",
            "",
            "Teach the **concept**, then demo, then lab. Use these Q&A as the phrases to say on camera —",
            "not as a second lecture series. One 20–40s “if they ask this in an interview…” close per video is enough.",
            "",
        ]
        seen = set()
        for n in sec["qs"]:
            if n in seen or n not in questions:
                continue
            seen.add(n)
            title, body = questions[n]
            lines += [f"### Q{n}. {title}", "", body, "", "---", ""]
    else:
        lines += [
            "",
            "## Content for this section",
            "",
            "No theory dump here — walk the repo, playground, and Lab 01 starter.",
            "Point students to `student/00-getting-started.md`.",
            "",
        ]
    (d / "LECTURE.md").write_text("\n".join(lines), encoding="utf-8")


def write_student_prompts(questions: dict[int, tuple[str, str]]) -> None:
    """Questions only — safe to zip into the Udemy student pack."""
    bands: list[tuple[str, range]] = [
        ("Easy (Q1–20)", range(1, 21)),
        ("Moderate (Q21–40)", range(21, 41)),
        ("Hard (Q41–60)", range(41, 61)),
        ("Industry / Mule message (Q61–80)", range(61, 81)),
    ]
    lines = [
        "# Interview prompts (no answers)",
        "",
        "These are the **same 80 questions** you already learned in the course. This file is a **prompt list only**.",
        "",
        "**Answers are not here.** Speak first, then resume the mock-interview video for a model answer.",
        "",
        "How to drill:",
        "",
        "1. Read one prompt.",
        "2. Pause the video (or close this file and look away).",
        "3. Speak for 45–90 seconds (hard questions: up to 3 minutes, plus a tiny script).",
        "4. Resume the video or replay the original concept lecture.",
        "",
        "If you download an “answer key” pack, that is only for **after** you attempt — same rule as lab solutions.",
        "",
    ]
    for heading, nums in bands:
        lines += [f"## {heading}", ""]
        for n in nums:
            if n not in questions:
                continue
            title, _body = questions[n]
            lines += [f"### {n}. {title}", "", "_Speak, then check the video._", ""]
    path = ROOT / "student" / "resources" / "interview-prompts.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)} ({len(questions)} prompts, no answers)")


def write_curriculum(questions: dict[int, tuple[str, str]]) -> None:
    lines = [
        "# Udemy curriculum (record in this order)",
        "",
        "Each **section** is a Udemy curriculum section. Each **lecture** is one video or article.",
        "Keep coding videos under ~12 minutes; split if a demo runs longer.",
        "",
        "| # | Udemy section | Lecture files | Student labs |",
        "| --- | --- | --- | --- |",
    ]
    for i, sec in enumerate(SECTIONS, 1):
        labs = ", ".join(f"{n:02d}" for n in sec["labs"]) or "—"
        lines.append(
            f"| {i:02d} | {sec['title']} | [sections/{sec['id']}/LECTURE.md](../sections/{sec['id']}/LECTURE.md) | {labs} |"
        )
    lines += [
        "",
        "## Lecture count (suggested)",
        "",
        "| Section | Videos | Articles | Practice tests |",
        "| --- | --- | --- | --- |",
        "| Welcome | 3 | 1 | 0 |",
        "| Fundamentals | 5 | 1 | 1 |",
        "| Arrays | 3 | 1 | 1 |",
        "| Objects | 3 | 1 | 1 |",
        "| Strings / conditionals | 3 | 1 | 1 |",
        "| JSON / XML / CSV | 4 | 1 | 1 |",
        "| Intermediate | 5 | 1 | 1 |",
        "| Dates / match / try | 3 | 1 | 1 |",
        "| Joins / Mule | 4 | 1 | 1 |",
        "| Advanced | 6 | 1 | 1 |",
        "| Production | 3 | 1 | 1 |",
        "| Industry operators / MIME | 4 | 1 | 1 |",
        "| Interview bootcamp | 4 | 1 | 1 (practice test) |",
        "",
        "Target: **~50 published lectures** plus **58 downloadable labs** and **section quizzes**.",
        "",
        "Plain-language concept pages (one file per topic): [`student/tutorials/README.md`](../student/tutorials/README.md). Same files are copied under `sections/<id>/tutorials/`.",
        "",
        "## Interview Q&A is not a second course",
        "",
        "Each topic section **teaches** its questions (concept + demo + lab + quiz).",
        "The last section is **practice only**: timed verbal answers and whiteboard labs.",
        "Attach `student/resources/bootcamp-prompts.md` (Set B, questions only). Instructor answers: `instructor/bootcamp/BOOTCAMP-QA.md`.",
        "",
        "## After each section",
        "",
        "1. Students complete the listed labs (starters only).",
        "2. They take `student/quizzes/` for that section.",
        "3. Next video: 3–5 minute homework recap of the trickiest lab.",
        "",
    ]
    (ROOT / "instructor" / "CURRICULUM.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    questions = parse_questions(text)
    if len(questions) != 80:
        raise SystemExit(f"Expected 80 questions, parsed {len(questions)}")
    for sec in SECTIONS:
        write_section(sec, questions)
    write_curriculum(questions)
    write_student_prompts(questions)
    print(f"Wrote {len(SECTIONS)} section lectures from {len(questions)} questions")


if __name__ == "__main__":
    main()
