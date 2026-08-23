#!/usr/bin/env python3
"""Split programming drills into student labs and instructor solutions."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "reference" / "DataWeave-Programming-Questions.md"

LAB_MAP = {
    range(1, 19): ("01-fundamentals", "easy"),
    range(19, 37): ("02-intermediate", "moderate"),
    range(37, 55): ("03-advanced", "hard"),
}


def section_for(num: int) -> tuple[str, str]:
    for rng, meta in LAB_MAP.items():
        if num in rng:
            return meta
    raise KeyError(num)


def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60]


def parse_labs(text: str) -> list[dict]:
    parts = re.split(r"^### (\d+)\. (.+)$", text, flags=re.M)
    labs = []
    # parts[0] is preamble; then triples of (num, title, body)
    i = 1
    while i + 2 < len(parts):
        num = int(parts[i])
        title = parts[i + 1].strip()
        body = parts[i + 2]
        next_sec = re.search(r"^## ", body, re.M)
        if next_sec:
            body = body[: next_sec.start()]
        body = body.strip().strip("-").strip()
        sol = re.search(r"\*\*Solution:\*\*\s*```dataweave\n(.*?)```", body, re.S)
        solution = sol.group(1).strip() if sol else ""
        inp = re.search(r"\*\*Input:\*\*\s*```(json|xml|csv|text)\n(.*?)```", body, re.S)
        input_lang = "json"
        if inp:
            input_lang = inp.group(1)
            input_json = inp.group(2).strip()
            input_is_raw = input_lang in ("csv", "text", "xml")
        else:
            inp = re.search(r"\*\*Input:\*\*\s*`([^`]+)`", body)
            input_json = inp.group(1).strip() if inp else None
            input_is_raw = bool(inp) and not str(input_json).startswith("{") and not str(input_json).startswith("[")
            if input_json and str(input_json).startswith("<"):
                input_lang = "xml"
                input_is_raw = True
        exp = re.search(r"\*\*Expected[^*]*:\*\*\s*```(?:json|xml)\n(.*?)```", body, re.S)
        if not exp:
            exp_line = re.search(r"\*\*Expected[^*]*:\*\*\s*(.+)", body)
            expected_note = exp_line.group(1).strip() if exp_line else ""
            expected_block = ""
        else:
            expected_block = exp.group(1).strip()
            expected_note = ""
        problem = re.search(r"\*\*Problem:\*\*\s*(.+?)(?:\n\n|\*\*)", body, re.S)
        problem_text = problem.group(1).strip() if problem else title
        student_body = re.sub(
            r"\*\*Solution:\*\*\s*```dataweave\n.*?```",
            "**Solution:** Hidden until you try it. See `instructor/solutions`.",
            body,
            count=1,
            flags=re.S,
        )
        labs.append(
            {
                "num": num,
                "title": title,
                "slug": slugify(title),
                "body": body,
                "student_body": student_body,
                "solution": solution,
                "input_json": input_json,
                "input_is_raw": input_is_raw,
                "input_lang": input_lang,
                "expected_block": expected_block,
                "expected_note": expected_note,
                "problem": problem_text,
            }
        )
        i += 3
    return labs


def mime_from_solution(sol: str) -> str:
    m = re.search(r"output\s+(\S+)", sol)
    return m.group(1) if m else "application/json"


def starter_script(sol: str) -> str:
    mime = mime_from_solution(sol)
    header = []
    for line in sol.splitlines():
        if line.startswith("%dw") or line.startswith("output") or line.startswith("import") or line.startswith("ns "):
            header.append(line)
        elif line.strip() == "---":
            break
        elif line.startswith("var ") or line.startswith("fun "):
            continue
    if not header:
        header = ["%dw 2.0", f"output {mime}"]
    if not any(l.startswith("output") for l in header):
        header.append(f"output {mime}")
    return "\n".join(header) + "\n---\n// TODO: write the transformation\npayload\n"


def write_lab(lab: dict, student_root: Path, instructor_root: Path) -> None:
    folder, level = section_for(lab["num"])
    name = f"{lab['num']:02d}-{lab['slug']}"
    sdir = student_root / folder / name
    idir = instructor_root / folder / name
    sdir.mkdir(parents=True, exist_ok=True)
    idir.mkdir(parents=True, exist_ok=True)

    readme = [
        f"# Lab {lab['num']:02d} — {lab['title']}",
        "",
        f"**Level:** {level}  ",
        f"**Section folder:** `{folder}`",
        "",
        "## Try this first",
        "",
        "1. Open DataWeave Playground or Transform Message.",
        "2. Set the input MIME type to match the sample (JSON unless stated otherwise).",
        "3. Paste `input` into the payload.",
        "4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.",
        "",
        "## Problem",
        "",
        lab["student_body"],
        "",
        "## Files",
        "",
        "| File | Role |",
        "| --- | --- |",
        "| `transform.dwl` | Your script (starter) |",
        "| `input.json` / `input.txt` | Sample payload |",
        "| Instructor `solution.dwl` | Reference after you try |",
        "",
    ]
    (sdir / "README.md").write_text("\n".join(readme), encoding="utf-8")
    (sdir / "transform.dwl").write_text(starter_script(lab["solution"]) + "\n", encoding="utf-8")

    if lab["input_json"]:
        lang = lab.get("input_lang") or ("text" if lab["input_is_raw"] else "json")
        name = {"json": "input.json", "xml": "input.xml", "csv": "input.csv", "text": "input.txt"}.get(
            lang, "input.txt" if lab["input_is_raw"] else "input.json"
        )
        (sdir / name).write_text(lab["input_json"] + "\n", encoding="utf-8")

    (idir / "solution.dwl").write_text(lab["solution"] + "\n", encoding="utf-8")
    notes = [f"# Instructor solution — Lab {lab['num']:02d}", "", lab["title"], ""]
    if lab["expected_block"]:
        notes += ["## Expected", "", "```", lab["expected_block"], "```", ""]
    if lab["expected_note"]:
        notes += ["## Expected (note)", "", lab["expected_note"], ""]
    notes += [
        "## Teaching tip",
        "",
        "Demo the failing starter (`payload` passthrough) first, then build the script live.",
        "Pause the recording and ask students to pause and try before showing `solution.dwl`.",
        "",
    ]
    (idir / "NOTES.md").write_text("\n".join(notes), encoding="utf-8")
    if lab["input_json"]:
        lang = lab.get("input_lang") or ("text" if lab["input_is_raw"] else "json")
        name = {"json": "input.json", "xml": "input.xml", "csv": "input.csv", "text": "input.txt"}.get(
            lang, "input.txt" if lab["input_is_raw"] else "input.json"
        )
        (idir / name).write_text(lab["input_json"] + "\n", encoding="utf-8")


def write_index(labs: list[dict], path: Path) -> None:
    lines = [
        "# Student lab index",
        "",
        "Work **in order**. Each lab is one Udemy practice lecture or homework item.",
        "",
        "| # | Level | Section | Lab |",
        "| --- | --- | --- | --- |",
    ]
    for lab in labs:
        folder, level = section_for(lab["num"])
        name = f"{lab['num']:02d}-{lab['slug']}"
        rel = f"{folder}/{name}/README.md"
        lines.append(f"| {lab['num']:02d} | {level} | `{folder}` | [{lab['title']}]({rel}) |")
    lines += [
        "",
        "## How labs map to videos",
        "",
        "- **In-lecture demo:** instructor types the solution live; students use the starter file.",
        "- **Homework:** assign 2–3 labs after each section; review one in the next video.",
        "- **Solutions:** `../../instructor/solutions/`.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    labs = parse_labs(text)
    if len(labs) != 54:
        raise SystemExit(f"Expected 54 labs, parsed {len(labs)}")
    student = ROOT / "student" / "labs"
    instructor = ROOT / "instructor" / "solutions"
    if student.exists():
        import shutil

        shutil.rmtree(student)
    if instructor.exists():
        import shutil

        shutil.rmtree(instructor)
    for lab in labs:
        write_lab(lab, student, instructor)
    write_index(labs, student / "README.md")
    manifest = [
        {
            "num": l["num"],
            "title": l["title"],
            "slug": l["slug"],
            "section": section_for(l["num"])[0],
            "level": section_for(l["num"])[1],
        }
        for l in labs
    ]
    (ROOT / "instructor" / "lab-manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {len(labs)} labs")


if __name__ == "__main__":
    main()
