#!/usr/bin/env python3
"""Emit reference/DataWeave-Mapping-Questions.md (labs 59–88)."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mapping_set import LABS

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    if len(LABS) != 30:
        raise SystemExit(f"Expected 30 mapping labs, got {len(LABS)}")
    nums = [x["num"] for x in LABS]
    if nums != list(range(59, 89)):
        raise SystemExit(f"Labs must be 59–88, got {nums[:3]}...{nums[-1]}")

    lines = [
        "# DataWeave Mapping — 30 complex industry sets",
        "",
        "Interview-hard **end-to-end mappings** (labs **59–88**). Each payload is a realistic integration shape:",
        "Salesforce composite, SAP/GST, Shopify, Stripe, ServiceNow, CDC, SOAP, FX, inventory, claims.",
        "Playground-friendly: lookup tables sit **on the payload** (no required Mule `vars`).",
        "",
        "Try the script before opening `instructor/solutions`.",
        "",
        "---",
        "",
        "## Complex industry mappings (59–88)",
        "",
    ]
    for lab in LABS:
        lang = lab.get("input_lang", "json")
        exp_lang = lab.get("expected_lang", "json")
        lines += [
            f"### {lab['num']}. {lab['title']}",
            "",
            f"**Problem:** {lab['problem']}",
            "",
            "**Input:**",
            "",
            f"```{lang}",
            lab["input"].strip(),
            "```",
            "",
            "**Expected:**",
            "",
            f"```{exp_lang}",
            lab["expected"].strip(),
            "```",
            "",
            "**Solution:**",
            "",
            "```dataweave",
            lab["solution"].strip(),
            "```",
            "",
            "---",
            "",
        ]
    path = ROOT / "reference" / "DataWeave-Mapping-Questions.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
