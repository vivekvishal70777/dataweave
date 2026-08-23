#!/usr/bin/env python3
"""Write easy-word concept tutorials per section topic."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "reference" / "easy-tutorials-source.md"
QA = ROOT / "reference" / "MuleSoft-DataWeave-Interview-Questions.md"
OUT = ROOT / "student" / "tutorials"

# Keep in sync with generate_udemy_lectures.SECTIONS (ids + qs + title)
SECTIONS = [
    ("01-welcome-and-setup", "Welcome and setup", []),
    ("02-dataweave-fundamentals", "DataWeave 2.0 fundamentals", list(range(1, 8))),
    ("03-arrays-and-core-operators", "Arrays: map, filter, and indexes", [8, 15, 35, 24]),
    ("04-objects-nulls-and-selectors", "Objects, nulls, and selectors", [9, 11, 13, 20, 21]),
    ("05-strings-numbers-conditionals", "Strings, numbers, and conditionals", [10, 12, 16, 19]),
    ("06-json-xml-csv", "JSON, XML, and CSV mappings", [14, 31, 32, 33]),
    ("07-intermediate-transforms", "Group, reduce, merge, and update", [22, 23, 24, 25, 26, 27, 36]),
    ("08-dates-match-and-errors", "Dates, pattern matching, and try", [28, 29, 30]),
    ("09-joins-modules-mule-context", "Joins, modules, and Mule context", [17, 18, 34, 37, 38, 39, 40]),
    ("10-advanced-recursion-and-xml-ns", "Advanced: recursion, namespaces, diffs", [41, 42, 43, 44, 47, 48, 49, 50, 51, 54, 55, 56, 57]),
    ("11-performance-and-production", "Streaming, crypto, modules, and pitfalls", [41, 45, 46, 52, 53, 58]),
    ("13-industry-operators-and-mule-message", "Industry operators, message, and MIME", list(range(61, 81))),
    ("14-dataweave-mapping", "DataWeave Mapping", []),
    ("12-interview-bootcamp", "Interview bootcamp", []),
]


def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:70]


def parse_easy(text: str) -> dict[int, dict]:
    blocks = re.split(r"^%%% (\d+)\s*$", text, flags=re.M)
    out: dict[int, dict] = {}
    i = 1
    while i + 1 < len(blocks):
        num = int(blocks[i])
        body = blocks[i + 1]
        def field(name: str) -> str:
            m = re.search(rf"^{name}:\s*(.+)$", body, re.M)
            return m.group(1).strip() if m else ""
        out[num] = {
            "title": field("TITLE"),
            "one": field("ONE"),
            "life": field("LIFE"),
            "remember": field("REMEMBER"),
        }
        i += 2
    return out


# Tiny scripts when the Q&A has no ```dataweave fence (concepts, tables).
FALLBACK_CODE = {
    1: '%dw 2.0\noutput application/json\n---\n{\n  name: payload.Name,\n  email: payload.Email\n}',
    2: '%dw 2.0\noutput application/json\n---\n// Mule 4 header: version 2.0, then output, then ---\npayload',
    10: '%dw 2.0\noutput application/json\n---\n{\n  hello: "Hi " ++ payload.firstName,\n  ids: [1, 2] ++ [3],\n  sum: 10 + 5\n}',
    13: '%dw 2.0\noutput application/json\n---\n{\n  name: payload.customer.name,\n  first: payload[0],\n  hyphen: payload["first-name"],\n  items: payload.*item,\n  anyId: payload..id\n}',
    18: '%dw 2.0\noutput application/json\n---\n// Transform Message: whole script.\n// Set Payload expression: #[payload.orderId]  (one expression, not a full mapping)',
    40: '%dw 2.0\noutput application/json\nvar customersById = vars.customers groupBy $.id\n---\npayload map (o) -> o ++ {\n  customer: customersById[o.customerId][0]\n}',
    41: '%dw 2.0\noutput application/json\n---\n// Streaming-friendly: map / filter on the array.\n// Streaming-hostile: orderBy, groupBy, sizeOf on the whole file, reduce to one object.\npayload filter $.status == "PAID"',
    58: '%dw 2.0\noutput application/json\n---\n// Pitfalls: lookup/Java inside map, orderBy on a huge file,\n// ++ in a hot loop, nested map+filter that rescans the same array.\npayload map (r) -> r - "internalNotes"',
    59: '%dw 2.0\noutput application/json\nfun twice(n: Number) = n * 2\n---\n[1, 2, 3] map twice($)',
    60: '%dw 2.0\noutput application/json\n---\n{\n  orderId: payload.Envelope.Body.Order.@id,\n  lines: payload.Envelope.Body.Order.*Line map {\n    sku: $.@sku,\n    qty: $.Qty as Number\n  }\n}',
    65: '%dw 2.0\noutput application/json\n---\n{\n  abs: abs(-3),\n  ceil: ceil(1.1),\n  floor: floor(1.9),\n  mod: 10 mod 3,\n  pow: pow(2, 8)\n}',
    69: '%dw 2.0\noutput application/json\n---\n// Target 1 — Payload:\npayload\n// Target 2 — Variable correlationId (separate script):\n// attributes.headers[\'x-correlation-id\'] default uuid()',
    70: '%dw 2.0\noutput application/json\n---\n// After a Java connector, payload is often application/java.\n// You still write: payload.Account.Name\n{\n  name: payload.Name\n}',
    73: '%dw 2.0\noutput application/json\n---\npayload map (row) -> {\n  sku: row.sku,\n  qty: try(() -> row.qty as Number) orElse 0\n}',
    74: '%dw 2.0\noutput application/json\n---\n{\n  method: attributes.method,\n  id: attributes.uriParams.id,\n  page: attributes.queryParams.page,\n  corr: attributes.headers[\'x-correlation-id\']\n}',
    75: '%dw 2.0\nns ord http://acme.com/order\noutput application/xml\n---\n{\n  ord#PurchaseOrder @(id: payload.id): {\n    ord#Note: payload.note\n  }\n}',
    76: '%dw 2.0\noutput application/json\n---\n// YAML: set reader MIME application/yaml, then map like JSON.\n// Excel / EDI: connector or flat-file schema first, then this script.\npayload.rows map {\n  sku: $.sku\n}',
    77: '%dw 2.0\noutput application/json\n---\n// Known path: mask / update.\n// Unknown depth: recursive match (Lab 39).\npayload update {\n  case .ssn -> "****"\n}',
    80: '%dw 2.0\noutput application/json\n---\n// DataWeave = CPU mapping (this script).\n// For Each = connector per item.\n// Batch = huge file + retries.\npayload map {\n  id: $.Id\n}',
}


def first_code(answer: str, q: int) -> str:
    m = re.search(r"```(?:dataweave|dw)\n(.*?)```", answer, re.S)
    code = m.group(1).strip() if m else FALLBACK_CODE.get(q, "")
    if not code:
        return ""
    lines = code.splitlines()
    if len(lines) > 18:
        code = "\n".join(lines[:18]) + "\n// ... see lecture for the rest"
    return code


def parse_answers(text: str) -> dict[int, str]:
    parts = re.split(r"^### (\d+)\. (.+)$", text, flags=re.M)
    out: dict[int, str] = {}
    i = 1
    while i + 2 < len(parts):
        num = int(parts[i])
        body = parts[i + 2]
        nxt = re.search(r"^## ", body, re.M)
        if nxt:
            body = body[: nxt.start()]
        out[num] = body
        i += 3
    return out


def page(q: int, easy: dict, code: str, section_title: str) -> str:
    lines = [
        f"# {easy['title']}",
        "",
        f"*Section: {section_title} · Interview Q{q} · easy words*",
        "",
        "## In one sentence",
        "",
        easy["one"],
        "",
        "## Like this in real life",
        "",
        easy["life"],
        "",
    ]
    if code:
        lines += [
            "## Tiny example",
            "",
            "Read this slowly. Header first, then the body.",
            "",
            "```dataweave",
            code,
            "```",
            "",
        ]
    lines += [
        "## Remember",
        "",
        easy["remember"],
        "",
        f"After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.",
        "",
    ]
    return "\n".join(lines)


WELCOME = [
    (
        "01-how-this-course-works",
        "How this course works",
        """# How this course works

*Section: Welcome and setup · easy words*

## In one sentence

Each idea is a short video, then you pause, try a lab, then watch the solution.

## Like this in real life

A gym class: the trainer shows one move (concept), you try it (lab), then they fix your form (solution). Watching without trying does not build muscle.

## Remember

- Concept video: 6–10 minutes.
- Pause card: you hit pause on Udemy.
- Lab: your own attempt, even if wrong.
- Quiz: practice test, not a video.

Next: set up the Playground, then open Lab 01.
""",
    ),
    (
        "02-playground-vs-transform-message",
        "Playground vs Transform Message",
        """# Playground vs Transform Message

*Section: Welcome and setup · easy words*

## In one sentence

The DataWeave Playground in the browser is enough for almost every lab. Transform Message is the same language inside Mule.

## Like this in real life

Playground is a kitchen at home. Transform Message is the same recipes at the restaurant (your Mule flow). Learn the recipes at home first.

## Remember

- Paste `input.json` / `input.xml` / `input.csv` and set the MIME type to match.
- Mule 4.3+ is needed for `update`, `leftJoin`, `divideBy`, `drop` / `take`.
- Starter `transform.dwl` often just returns `payload` — that is supposed to be wrong.

Open [00-getting-started.md](../../00-getting-started.md) next.
""",
    ),
    (
        "03-folders-you-will-use",
        "Folders you will use",
        """# Folders you will use

*Section: Welcome and setup · easy words*

## In one sentence

You live in `student/`. Solutions hide in `instructor/` until after you try.

## Like this in real life

Exam paper vs answer key. If the key sits on the desk, you copy. Keep it in another room.

## Remember

- `student/labs` — starters, numbered 01–88, five folders (fundamentals, intermediate, advanced, industry, mapping).
- `student/tutorials` — these easy concept pages.
- `student/quizzes` — no answers.
- `instructor/solutions` — after your attempt, or on the solution video.

Do not zip `instructor/` into the Udemy student pack.
""",
    ),
]

BOOTCAMP = [
    (
        "01-how-to-drill-the-question-bank",
        "How to drill the question bank",
        """# How to drill the question bank

*Section: Interview bootcamp · easy words*

## In one sentence

Cover the prompt, say it out loud in 60–90 seconds, then play the model answer on the video. Do not binge-read an answer key.

## Like this in real life

Flashcards. If you only reread the book, you feel fluent and fail the whiteboard.

## Remember

- Eighty **Set B prompts** (no answers) live in `student/resources/bootcamp-prompts.md`. Same skills as the course, new wording.
- Easy tutorials (earlier sections) are for learning. Set B is for speaking under time.
- Timebox: easy 45s, moderate 90s, hard 3 minutes plus a tiny script.
- Model answers are on the mock-interview **video** after you pause — not in the student zip.

Then run the whiteboard set with a timer.
""",
    ),
    (
        "02-whiteboard-method",
        "Whiteboard method",
        """# Whiteboard method

*Section: Interview bootcamp · easy words*

## In one sentence

Say the header out loud, write a tiny example, then the body. Eight minutes per problem.

## Like this in real life

A cooking show: ingredients (header), then the dish (body). Silent typing looks like panic.

## Remember

Problems: Lab 23 flatMap, Lab 20 totals, Lab 32 groupBy join, Lab 39 PII, Lab 41 SOAP, Lab 53 org, Lab 54 invoice.

Header every time: `%dw 2.0`, `output application/json`, `---`.
""",
    ),
    (
        "03-q60-in-easy-words",
        "Q60 in easy words",
        """# Q60 in easy words

*Section: Interview bootcamp · easy words*

## In one sentence

Tell a story in eight beats: read XML, clean types, money, join customer you already have, shape names, write JSON, catch bad rows, keep it one-pass.

## Like this in real life

Unload a SOAP truck, put stickers in *your* shop language, do not phone the warehouse for every box.

## Remember

1. Reader: `ns`, Envelope/Body, `*Line`, `@sku`.
2. Normalize: `as Number`, date formats.
3. Enrich: `fun money`, `do` for line total.
4. Join: `vars.customer` already fetched — not `lookup` per line.
5. Shape: `orderId`, `currency`, `lines`.
6. Writer: `skipNullOn="everywhere"`.
7. Errors: `try` on bad price.
8. Scale: `map` once, no `orderBy` unless the API demands it.

Labs 41 and 54 are the typing version.
""",
    ),
]


MAPPING = [
    (
        "01-canonical-model",
        "What a canonical mapping is",
        """# What a canonical mapping is

*Section: DataWeave Mapping · easy words*

## In one sentence

You copy the vendor’s ugly payload into **your** shop’s JSON names — `orderId`, `lines`, `money` — not SAP `vbeln`.

## Like this in real life

A warehouse relabels every box in the store language. The truck label can stay in German; the shelf cannot.

## Remember

- Header: `%dw 2.0`, `output application/json`, `---`.
- Drop fields you do not own.
- Lookups already on the payload — never `lookup` inside `map`.

Then open Lab 59.
""",
    ),
    (
        "02-join-tables-on-the-payload",
        "Join tables that arrived together",
        """# Join tables that arrived together

*Section: DataWeave Mapping · easy words*

## In one sentence

`groupBy` the small table by id, then `map` the big table. That is a hash join.

## Like this in real life

Index the customer list once. For each order, pick the card from the index. Do not phone HQ per order.

## Tiny example

```dataweave
var byId = payload.customers groupBy $.id
---
payload.orders map (o) -> o ++ { email: (byId[o.customerId][0].email) default "unknown" }
```

## Remember

Missing match → `default`. Outer merge is Lab 84 / Lab 49.

Lab 59, 63, 64.
""",
    ),
    (
        "03-money-qty-tax",
        "Money, zero qty, tax",
        """# Money, zero qty, tax

*Section: DataWeave Mapping · easy words*

## In one sentence

ERP amounts are strings. `as Number`, skip qty 0, `fun money` (`0.00` format), then tax.

## Like this in real life

A cashier does not add `"100.00"` as text. They tap the number keys, skip empty carts, then GST.

## Remember

- Intra-state GST: CGST+SGST. Inter-state: IGST.
- `default` does not catch bad `as Number` — use `try`.

Labs 60, 73, 88.
""",
    ),
    (
        "04-xml-and-cdc",
        "XML namespaces and CDC envelopes",
        """# XML namespaces and CDC envelopes

*Section: DataWeave Mapping · easy words*

## In one sentence

XML: declare `ns`, walk `ns#Element`, attributes `@id`. CDC: `after` for upsert, `before` for delete.

## Like this in real life

SOAP is a sealed envelope. CDC is a form that says create, update, or strike-through.

## Remember

Prefix is yours; URI must match. Do not log PII.

Labs 65, 79.
""",
    ),
    (
        "05-how-to-drill-mapping-labs",
        "How to drill the 30 mapping labs",
        """# How to drill the 30 mapping labs

*Section: DataWeave Mapping · easy words*

## In one sentence

Read input and expected. Pause. Write the header out loud. Map. Then play the solution.

## Like this in real life

Interview whiteboard: eight to twelve minutes per mapping. Silence while typing looks like panic — narrate.

## Remember

Clusters: 59–63 CRM/commerce, 64–70 ops/CDC/FX, 71–80 identity/tax/catalog, 81–88 recon/events.

Solutions stay in `instructor/solutions/05-mapping/`.
""",
    ),
]


def write_topic(dir_: Path, idx: int, filename: str, body: str) -> Path:
    dir_.mkdir(parents=True, exist_ok=True)
    path = dir_ / f"{idx:02d}-{filename}.md"
    path.write_text(body if body.endswith("\n") else body + "\n", encoding="utf-8")
    return path


def main() -> None:
    easy = parse_easy(SRC.read_text(encoding="utf-8"))
    if len(easy) != 80:
        raise SystemExit(f"Expected 80 easy topics, got {len(easy)}")
    answers = parse_answers(QA.read_text(encoding="utf-8"))

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    index = [
        "# Easy concept tutorials",
        "",
        "Plain-language pages — **one topic per file**. Read these before the interview Q&A and before the lab.",
        "",
        "On Udemy you can paste each file as an **Article** lecture, or attach the section folder as a resource.",
        "",
        "| Section | Tutorials |",
        "| --- | --- |",
    ]

    total = 0
    for sid, title, qs in SECTIONS:
        sdir = OUT / sid
        sec_dir = ROOT / "sections" / sid / "tutorials"
        if sec_dir.exists():
            shutil.rmtree(sec_dir)
        sec_dir.mkdir(parents=True, exist_ok=True)
        names: list[tuple[str, str]] = []
        n = 1
        if sid == "01-welcome-and-setup":
            for slug, t, body in WELCOME:
                p = write_topic(sdir, n, slug, body)
                shutil.copy(p, sec_dir / p.name)
                names.append((p.name, t))
                n += 1
                total += 1
        elif sid == "14-dataweave-mapping":
            for slug, t, body in MAPPING:
                p = write_topic(sdir, n, slug, body)
                shutil.copy(p, sec_dir / p.name)
                names.append((p.name, t))
                n += 1
                total += 1
        elif sid == "12-interview-bootcamp":
            for slug, t, body in BOOTCAMP:
                p = write_topic(sdir, n, slug, body)
                shutil.copy(p, sec_dir / p.name)
                names.append((p.name, t))
                n += 1
                total += 1
        else:
            seen: set[int] = set()
            for q in qs:
                if q in seen or q not in easy:
                    continue
                seen.add(q)
                e = easy[q]
                slug = slugify(e["title"])
                body = page(q, e, first_code(answers.get(q, ""), q), title)
                p = write_topic(sdir, n, slug, body)
                shutil.copy(p, sec_dir / p.name)
                names.append((p.name, e["title"]))
                n += 1
                total += 1

        toc = [
            f"# Easy tutorials — {title}",
            "",
            "Read in order. Each page is one topic in simple words, then a tiny example.",
            "",
        ]
        for fname, t in names:
            toc.append(f"- [{t}]({fname})")
        toc.append("")
        (sdir / "README.md").write_text("\n".join(toc), encoding="utf-8")
        (sec_dir / "README.md").write_text("\n".join(toc), encoding="utf-8")
        index.append(f"| {title} | [{sid}/README.md]({sid}/README.md) ({len(names)} topics) |")

    index += [
        "",
        "Regenerate after editing `reference/easy-tutorials-source.md`:",
        "",
        "```bash",
        "python3 scripts/generate_easy_tutorials.py",
        "```",
        "",
    ]
    (OUT / "README.md").write_text("\n".join(index), encoding="utf-8")
    print(f"Wrote {total} topic tutorials under {OUT}")


if __name__ == "__main__":
    main()
