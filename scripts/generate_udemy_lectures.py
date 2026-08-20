#!/usr/bin/env python3
"""Split interview Q&A into Udemy section lecture articles."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "reference" / "MuleSoft-DataWeave-Interview-Questions.md"
PROD_SRC = ROOT / "reference" / "DataWeave-Production-Interview-Questions.md"

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
            "Lab 13 grades as the if/else pattern students will reuse.",
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
            "Same payload, three outputs: JSON, XML, CSV — three short clips.",
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
            "Hero demo: Lab 20 totals per customer, then Lab 23 flatMap lines.",
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
            "Split into 4–5 videos: recursion, XML ns, dynamic keys, capstone invoice (Lab 54).",
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
        "id": "13-production-hard-transforms",
        "title": "Production-level hard transformations",
        "qs": list(range(61, 81)),
        "labs": [55, 56, 63, 70, 73, 75, 82],
        "objectives": [
            "Ship partial-success canonical APIs with `errors[]`.",
            "Merge golden records, CDC, FX, overlays, and merge-patch with explicit rules.",
            "Wrap ops concerns: scatter-gather, DLQ, redaction, injected clocks.",
        ],
        "talking": [
            "Open with Lab 55 (canonical order + bad line) — this is the production default.",
            "Whiteboard Lab 56 precedence vs `++`, then Lab 73 cycle guard.",
            "Close with scatter-gather (75) and payment `match` (82).",
        ],
    },
    {
        "id": "12-interview-bootcamp",
        "title": "Interview bootcamp",
        "qs": list(range(1, 61)),
        "labs": [20, 23, 32, 39, 53, 54],
        "objectives": [
            "Answer the 60-question bank out loud.",
            "Whiteboard the six signature programs.",
            "Talk through the nested XML → JSON design (Q60).",
        ],
        "talking": [
            "Do not re-teach; run timed drills. Students close solutions.",
            "Record 2–3 mock interviews using the whiteboard set.",
        ],
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
    if sec["qs"]:
        lines += ["", "## Teach these interview questions", ""]
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
        "| Streaming / pitfalls | 3 | 1 | 1 |",
        "| Production hard transforms | 6 | 1 | 1 |",
        "| Interview bootcamp | 4 | 1 | 1 (practice test) |",
        "",
        "Target: **~55 published lectures** plus **82 downloadable labs** and **section quizzes**.",
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
    questions = parse_questions(SRC.read_text(encoding="utf-8"))
    questions.update(parse_questions(PROD_SRC.read_text(encoding="utf-8")))
    if len(questions) != 80:
        raise SystemExit(f"Expected 80 questions, parsed {len(questions)}")
    for sec in SECTIONS:
        write_section(sec, questions)
    write_curriculum(questions)
    print(f"Wrote {len(SECTIONS)} section lectures from {len(questions)} questions")


if __name__ == "__main__":
    main()
