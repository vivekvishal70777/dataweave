#!/usr/bin/env python3
"""Write bootcamp Set B Q&A (instructor) and prompts-only (student)."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bootcamp_set_b import ITEMS

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    if len(ITEMS) != 80:
        raise SystemExit(f"Expected 80 Set B items, got {len(ITEMS)}")
    nums = [n for n, _, _ in ITEMS]
    if nums != list(range(1, 81)):
        raise SystemExit(f"Set B numbers must be 1–80 in order, got {nums[:5]}...")

    ans_lines = [
        "# Interview bootcamp — Set B (answers)",
        "",
        "Use this **only while recording** the last Udemy section. Same 80 skills as the course bank,",
        "new wording so students cannot recite the Section 2–12 questions from memory.",
        "",
        "**Do not zip this file into the student pack.** Students get `student/resources/bootcamp-prompts.md`.",
        "",
        "Course twins: each answer ends with `Course twin: Qn` (the teaching-bank number).",
        "",
        "---",
        "",
        "## Easy (B1–B20)",
        "",
    ]
    prompt_lines = [
        "# Interview bootcamp prompts — Set B (no answers)",
        "",
        "These 80 questions test the **same skills** as the course, with **new wording**.",
        "They are not a copy of the articles you already read.",
        "",
        "**Answers are not in this file.** Speak 45–90 seconds, then resume the mock-interview video.",
        "",
        "1. Read one prompt.",
        "2. Pause.",
        "3. Speak (hard questions: up to 3 minutes + a tiny script).",
        "4. Play the model answer on the video, or replay the matching *concept* lecture from earlier sections.",
        "",
        "---",
        "",
        "## Easy (B1–B20)",
        "",
    ]

    def band_header(n: int) -> str | None:
        return {
            21: "## Moderate (B21–B40)",
            41: "## Hard (B41–B60)",
            61: "## Industry / Mule message (B61–B80)",
        }.get(n)

    for n, title, answer in ITEMS:
        h = band_header(n)
        if h:
            ans_lines += ["", "---", "", h, ""]
            prompt_lines += ["", "---", "", h, ""]
        ans_lines += [f"### B{n}. {title}", "", answer.strip(), ""]
        prompt_lines += [f"### B{n}. {title}", "", "_Speak, then check the video._", ""]

    ans_path = ROOT / "instructor" / "bootcamp" / "BOOTCAMP-QA.md"
    ans_path.parent.mkdir(parents=True, exist_ok=True)
    ans_path.write_text("\n".join(ans_lines) + "\n", encoding="utf-8")

    pr_path = ROOT / "student" / "resources" / "bootcamp-prompts.md"
    pr_path.write_text("\n".join(prompt_lines) + "\n", encoding="utf-8")
    print(f"Wrote {ans_path.relative_to(ROOT)}")
    print(f"Wrote {pr_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
