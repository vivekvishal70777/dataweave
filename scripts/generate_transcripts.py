#!/usr/bin/env python3
"""Build spoken recording transcripts for every concept lecture and every lab."""
from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "instructor" / "transcripts"
MANIFEST = ROOT / "instructor" / "lab-manifest.json"
QA = ROOT / "reference" / "MuleSoft-DataWeave-Interview-Questions.md"
TIPS = ROOT / "scripts" / "lab_talking_points.txt"


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


def load_tips() -> dict[int, str]:
    tips: dict[int, str] = {}
    for line in TIPS.read_text(encoding="utf-8").splitlines():
        if not line.strip() or "|" not in line:
            continue
        n, text = line.split("|", 1)
        tips[int(n)] = text.strip()
    return tips


def md_to_spoken_blocks(body: str) -> str:
    body = re.sub(r"^\*\*Answer:\*\*\s*", "", body.strip(), flags=re.M)
    return body.strip()


def lecture_from_qs(
    questions: dict[int, tuple[str, str]],
    qs: list[int],
    intro: str,
    outro: str,
    demo: str = "",
) -> str:
    chunks = ["## Open", "", "**SAY:**", "", intro.strip(), ""]
    if demo:
        chunks += [demo.strip(), ""]
    for n in qs:
        title, body = questions[n]
        chunks += [
            f"## Interview beat — Q{n}. {title}",
            "",
            "**SAY:**",
            "",
            md_to_spoken_blocks(body),
            "",
            "Type every DataWeave sample on screen. Read the header out loud: percent dw two point oh, output, dash dash dash.",
            "",
        ]
        chunks += ["## Close", "", "**SAY:**", "", outro.strip(), ""]
    return "\n".join(chunks)


def wrap_lecture(
    code: str,
    title: str,
    mins: str,
    filename: str,
    body: str,
    kind: str = "Video",
) -> str:
    return "\n".join(
        [
            f"# {code} — {title}",
            "",
            f"| Field | Value |",
            f"| --- | --- |",
            f"| Udemy type | {kind} |",
            f"| Target length | {mins} |",
            f"| File name | `{filename}` |",
            "",
            "Read the **SAY** lines. Follow **ON CAMERA** and **PAUSE CARD** stage directions. Keep the take under the target length; split rather than ramble.",
            "",
            body.rstrip(),
            "",
        ]
    )


CUSTOM: dict[str, str] = {}

CUSTOM["L01"] = """
## ON CAMERA
Full screen: course title `DataWeave 2.0 for Mule 4: Labs + Interview Prep`. Then switch to the Playground with a nested order JSON.

## SAY

Welcome. I am Vivek, and this course is a gym for DataWeave 2.0 on Mule 4 — not a slide dump.

By the last section you will have written fifty-four transformation scripts and you will be able to answer sixty interview questions out loud, with a short script on a whiteboard.

Here is the promise in one picture. Ugly nested JSON — line items inside orders — becomes a clean invoice: line totals, tax, grand total. That is Lab 54. We will not start there. We start with map and filter.

You do not need Anypoint Studio on day one. The DataWeave Playground in the browser is enough for almost every lab. If you already work in Transform Message, use that. Same language.

What this course is not: it is not official Salesforce training, and it is not a MuleSoft certification dump. It is how you actually map payloads at work and in interviews.

Next video: how each lesson is built — concept, pause card, lab, quiz. Then we tour the student folder and you write Lab 01.

See you in the next lecture.
"""

CUSTOM["L02"] = """
## ON CAMERA
Whiteboard or slide with four boxes: Concept → Pause → Lab → Quiz.

## SAY

Every teaching section uses the same loop. If you remember only this video, remember the loop.

First, a short concept. One idea. Three to seven minutes. I will talk, and I will type a tiny example.

Second, a pause card. That is not a Udemy setting. It is a slide I put on screen for a few seconds that says: pause this video, open the lab folder, try it yourself. You hit pause on Udemy. You work. You come back.

Third, the lab video — and in this course, **every lab has its own video**. I show the failing starter, I read the problem, I show the pause card, then I type the solution. Do not skip the pause. If you watch the solution first, you only learn to copy.

Fourth, a section quiz on Udemy. Those are practice tests, not videos. I will not read every question on camera.

Target length: concept videos six to ten minutes. Lab videos six to ten, hard cap twelve. If Lab 54 runs long, I split it.

File names on my side look like S02-L07-script-structure.mp4. You just press play in order.

Next: the getting-started article, then a tour of the student lab folder.
"""

CUSTOM["L03"] = """
## ON CAMERA
Open `student/00-getting-started.md` and scroll slowly. This lecture can be an **article** on Udemy; use this transcript if you record a voiceover instead.

## SAY

Before Lab 01, set up once.

Option A: open the DataWeave Playground in your browser. That is enough for almost every exercise.

Option B: Anypoint Studio or Anypoint Code Builder, a Mule 4 project, and a Transform Message component.

If you need the update operator, drop, take, divideBy, or leftJoin, use Mule 4.3 or newer.

The lab ritual never changes. Open the lab README. Paste the sample input. Set the MIME type — JSON unless the lab says XML or CSV. Replace the TODO in transform.dwl. Leave the percent dw 2.0 header unless the output type must change. Compare your result to Expected. Only then watch the solution video.

Trap list: plus versus plus-plus. Missing fields use default or the safe selector, not only Java null checks. XML needs one root. Attributes are at-sign. Coerce with as Number. If coercion can fail, use try.

Work the sections in order. Do not jump to recursion until map, filter, and groupBy feel boring.

Next video: I will click through the student folder so you know exactly which file to open.
"""

CUSTOM["L04"] = """
## ON CAMERA
IDE with `instructor/` hidden. Expand `student/labs/01-fundamentals/01-map-salesforce-contact-to-a-shorter-api-shape/`.

## SAY

This is the student pack you download from Udemy. You will live in student, not instructor.

student/labs has four folders: fundamentals, intermediate, advanced, industry. Labs are numbered 01 through 58. Each lab is a folder: README, input, and transform.dwl.

I am opening Lab 01. README states the problem, the input, and the expected JSON. input.json is the payload. transform.dwl is the starter — it should just pass payload through, which is the wrong shape. That is on purpose.

Quizzes live under student/quizzes. No answers there. The cheat sheet and whiteboard list are under student/resources.

Do not hunt for solutions in this zip. Solutions are either on camera after the pause card, or in a solutions pack at the very end of the course.

Your job after this video: open Lab 01 in the Playground, paste the input, and wait for the Lab 01 video — or skip ahead only if you already finished the attempt.

Next section: what DataWeave actually is in Mule 4.
"""

CUSTOM["L55"] = """
## ON CAMERA
Timer on screen, empty Playground, `student/resources/whiteboard.md` on the left. Students should have solutions closed.

## SAY

This is a mock interview, not a new topic. Six problems. Eight minutes each. Say the header out loud before the body: percent dw two point oh, output application json, dash dash dash.

Problem one: Lab 23. One row per line item with orderId and sku. Skill: flatMap.

Pause card: eight minutes. Go.

## PAUSE CARD
Whiteboard 1 of 6 — Lab 23 flatMap — 8:00

## SAY

Time. I paste only the input, then I type the solution. flatMap maps each order to an array of lines and flattens one level. Nested map without flatten leaves arrays inside arrays — that is the usual fail.

Problem two: Lab 20. Total amount per customer. groupBy, then sum.

## PAUSE CARD
Whiteboard 2 of 6 — Lab 20 totals — 8:00

## SAY

groupBy returns an object of arrays. pluck or entriesOf to walk groups. Sum the amounts. Do not nested-filter the whole list for every customer — that is O of n squared.

Problem three: Lab 32. Left join orders to customers without leftJoin.

## PAUSE CARD
Whiteboard 3 of 6 — groupBy lookup — 8:00

## SAY

Index customers with groupBy id once. Then map orders and pick the first customer. Same idea as a hash join. Mention why lookup inside map is an N-plus-one.

Problem four: Lab 39. Mask ssn, password, email at any depth.

## PAUSE CARD
Whiteboard 4 of 6 — PII mask — 8:00

## SAY

Recursion plus match on types. Object: mapObject, if the key is secret output stars, else recurse. Array: map recurse. Else: the leaf.

Problem five: Lab 53. Flat employees to a nested org chart.

## PAUSE CARD
Whiteboard 5 of 6 — org chart — 8:00

## SAY

Index by id. Find roots where managerId is null. Recursive children filter managerId equals this id. Watch infinite loops if the data has cycles.

Problem six: Lab 54. Invoice line totals, tax, grand total.

## PAUSE CARD
Whiteboard 6 of 6 — invoice — 8:00

## SAY

Header vars: lines with lineTotal, subtotal as sum, tax, grandTotal. Body is one object. That is the do-or-var interview pattern.

Next video: I talk through the nested XML to canonical JSON design — interview question 60 — without turning it into a ninety-minute recording.
"""

CUSTOM["L56"] = """
## ON CAMERA
Empty whiteboard, then slowly type the Q60 sketch from the interview bank. Do not rush namespaces.

## SAY

Question 60 is a design talk. Interviewers want to hear the order of operations, not only syntax.

Step one, reader. Incoming XML with namespaces. Declare ns. Repeating line items with the multi-value selector. Attributes with at-sign.

Step two, normalize. sku from attributes becomes a field. Quantities and prices as Number. Dates as DateTime with an explicit format.

Step three, enrich. Line total is qty times price, inside a do block so the map stays readable. Order total is sum of line totals. Format money if they care about two decimals.

Step four, join. Customer comes from vars.customer that a previous connector already fetched. I will say out loud: I am not going to lookup a flow for every line item.

Step five, shape. Canonical names: orderId, customerId, currency, lines as an array. Not XML tag names leaked into JSON.

Step six, writer. application/json, skipNullOn everywhere so nulls do not ship.

Step seven, errors. Bad price: try, push into an errors array, do not crash the whole order unless the business says so.

Step eight, scale. One-pass map on line items. No orderBy unless the API requires sorted lines. No payload as String.

Now I type the sketch: ns, output json, fun money, body with orderId from ns0 hash order at-id, lines from star lineItem, orderTotal from sum.

If they ask follow-ups: default namespace versus prefix, and writer properties for XML on the way back out.

You now have the verbal map. The coding version is Lab 41 and Lab 54 together. Go take the final practice test.
"""

CUSTOM["L58"] = """
## ON CAMERA
Course title, then student/resources/cheat-sheet.md, then optional solutions zip on lecture 58 only.

## SAY

You finished the lab trail and the interview bank.

Revisit the whiteboard six until you can do them cold: flatMap lines, totals per customer, join via groupBy, PII mask, org chart, invoice.

The cheat sheet is in student/resources. The sixty questions are in the interview article and the section lectures.

If I attached a solutions pack on this lecture, use it only after you have attempts. If I did not attach it, you already saw solutions on camera after each pause card.

This course is not an official MuleSoft credential. It is how you map data. Go apply it on the next Transform Message at work, and good luck in the interview.

Thank you for working the labs instead of only watching.
"""

CUSTOM["L09"] = """
## ON CAMERA
Short section bridge — optional if you already publish Lab 03, 05, 08, and 13 as their own videos.

## SAY

Fundamentals concept videos are done. Your practice is four labs, each with its own video in this section’s lab list: Lab 03 sum, Lab 05 default email, Lab 08 tax, Lab 13 grades.

Do not binge the solutions. Open the starter, pause, attempt, then play that lab’s video.

After the four labs, take the Fundamentals practice test on Udemy.
"""

CUSTOM["L13"] = """
## SAY
Arrays concepts are done. Record Lab 01 and Lab 02 as the on-camera demos. Homework labs 09, 10, 14, and 15 each have their own video. Pause, try, then play the matching lab lecture. Then the Arrays quiz.
"""

CUSTOM["L18"] = """
## SAY
Objects and nulls: your lab videos are 04, 05, 16, and 18. Lab 05 you may have seen in fundamentals — treat this as a second look at default. Then the Objects quiz.
"""

CUSTOM["L22"] = """
## SAY
Strings and conditionals: lab videos 06, 07, 08, 13, and 17. Lab 08 and 13 might already be recorded; you can reuse those files. Then the section quiz.
"""

CUSTOM["L27"] = """
## SAY
Format labs: 11 and 12 for XML, 29 and 30 for CSV. Each is its own video. Same payload, different output MIME types. Then the Formats quiz.
"""

CUSTOM["L33"] = """
## SAY
This lecture is only a pointer. The full walkthrough is the Lab 20 video: totals per customer after groupBy. If you already recorded Lab 20, you can skip publishing this duplicate, or keep a three-minute recap of mistakes: forgetting groupBy returns an object, and summing strings instead of numbers.
"""

CUSTOM["L37"] = """
## SAY
Date and match labs: 27, 28, 33, and 52. Lab 27 mixed formats is the interview favorite — give it a full video. Then the section quiz.
"""

CUSTOM["L41"] = """
## SAY
Join labs 31 and 32 should be two videos back to back: leftJoin first, then the same result with groupBy lookup. That pair is the interview story. Labs 34 and 45 are extra. Then the Joins quiz.
"""

CUSTOM["L45"] = """
## SAY
This concept lecture is the production story. The full recursive mask is Lab 39’s video. If Lab 39 is already recorded, keep this clip to three minutes: why we mask before logging, and the match-on-types skeleton. Students then open Lab 39.
"""

CUSTOM["L48"] = """
## SAY
Capstone: Lab 53 org chart and Lab 54 invoice are two separate videos. Do not combine them into one twenty-minute file. Pause cards on both. Then the Advanced quiz.
"""


def q_lecture(
    questions: dict[int, tuple[str, str]],
    intro: str,
    qs: list[int],
    outro: str,
    demo: str = "",
) -> str:
    return lecture_from_qs(questions, qs, intro, outro, demo)


def build_q_lectures(questions: dict[int, tuple[str, str]]) -> dict[str, str]:
    o = "Close by repeating the interview phrase in one sentence. Point to the lab videos for this section. Stop. Do not start a new topic."
    return {
        "L05": q_lecture(
            questions,
            "Open with a Transform Message on screen. Students need a one-sentence definition they can repeat in an interview.",
            [1],
            o,
        ),
        "L06": q_lecture(
            questions,
            "Draw two columns: Mule 3 versus Mule 4. Interviews almost always want DataWeave 2.0.",
            [2],
            o,
        ),
        "L07": q_lecture(
            questions,
            "Live-type the hello-world script. Say each line of the header before the body.",
            [3],
            o,
            demo="**TYPE** the Q3 script from scratch. Run it against `{ \"name\": \"Vivek\" }`.",
        ),
        "L08": q_lecture(
            questions,
            "One video for vars, functions, types, and as. Keep each beat under two minutes.",
            [4, 5, 6, 7],
            o,
        ),
        "L11": q_lecture(
            questions,
            "Show an orders array. Filter PAID, then map to id and total. Then explain dollar and dollar-dollar.",
            [8, 35],
            o,
        ),
        "L12": q_lecture(
            questions,
            "sizeOf versus isEmpty. Prefer isEmpty in interviews when you only check empty.",
            [15],
            o,
        ),
        "L15": q_lecture(
            questions,
            "Whiteboard the selector table. Dot, brackets, star, and descendant dots.",
            [13],
            o,
        ),
        "L16": q_lecture(
            questions,
            "Demo a missing email. default versus the safe selector versus skipNullOn on output.",
            [11, 20],
            o,
        ),
        "L17": q_lecture(
            questions,
            "map is arrays. mapObject is objects. pluck turns an object into an array.",
            [21, 9],
            o,
        ),
        "L20": q_lecture(
            questions,
            "Trap: plus on two strings. Show the error, then fix with plus-plus. Also split, join, case.",
            [10, 16],
            o,
        ),
        "L21": q_lecture(
            questions,
            "If/else is an expression. No ternary. Mention comments so they do not look lost in a header.",
            [12, 19],
            o,
        ),
        "L24": q_lecture(
            questions,
            "Same array, output xml. Stress a single root element.",
            [14],
            o,
        ),
        "L25": q_lecture(
            questions,
            "Attributes versus elements versus repeating children. Write an attribute with at-paren syntax.",
            [33],
            o,
        ),
        "L26": q_lecture(
            questions,
            "CSV in as array of objects. CSV out with header true. Coerce numbers.",
            [31, 32],
            o,
        ),
        "L29": q_lecture(
            questions,
            "groupBy returns an object of arrays. orderBy and distinctBy on the same slide.",
            [22],
            o,
        ),
        "L30": q_lecture(
            questions,
            "reduce for a sum and reduce to build an object. Mention flatten versus flatMap.",
            [23, 24],
            o,
        ),
        "L31": q_lecture(
            questions,
            "Hero idea: one order, many lines. This concept video; the full typing is the Lab 23 video.",
            [25, 43],
            o,
        ),
        "L32": q_lecture(
            questions,
            "Merge plus-plus, update on Mule 4.3, and do blocks for local vars.",
            [26, 27, 36],
            o,
        ),
        "L35": q_lecture(
            questions,
            "now, format, parse, period literals with pipes. Lab 28 is the format drill.",
            [30],
            o,
        ),
        "L36": q_lecture(
            questions,
            "match for statuses. try for errors. default is nulls, try is failures.",
            [28, 29],
            o,
        ),
        "L39": q_lecture(
            questions,
            "Transform Message input graph: payload, vars, attributes, p for properties.",
            [17, 18],
            o,
        ),
        "L40": q_lecture(
            questions,
            "import modules. Transform Message versus hash-bracket expressions.",
            [34, 39],
            o,
        ),
        "L42": q_lecture(
            questions,
            "Java from DataWeave is possible. lookup inside map is the anti-pattern. Name N-plus-one.",
            [38, 40],
            o,
        ),
        "L44": q_lecture(
            questions,
            "Recursion plus match on Array, Object, else. This is the skeleton for labs 37 to 40.",
            [42, 47, 50],
            o,
        ),
        "L46": q_lecture(
            questions,
            "ns prefix, hash names, attributes, writing namespaced XML. Labs 41 and 42 are the typing.",
            [44],
            o,
        ),
        "L47": q_lecture(
            questions,
            "Dynamic keys need parentheses. Diff of two objects. Last-wins dedupe. Pagination take drop.",
            [48, 49, 54, 55],
            o,
        ),
        "L50": q_lecture(
            questions,
            "Streaming works for one-pass map and filter. List what breaks it. Do not only say it streams.",
            [41],
            o,
        ),
        "L51": q_lecture(
            questions,
            "Hash versus HMAC. Binary and Base64. Reader and writer properties for JSON XML CSV.",
            [45, 52, 53],
            o,
        ),
        "L52": q_lecture(
            questions,
            "Reusable dwl module, pure functions, then the performance pitfall list. Close the production section.",
            [46, 58, 59],
            o,
        ),
        "L70": q_lecture(
            questions,
            "Industry Arrays helpers. maxBy returns the item. firstWith is first match. zip pairs columns.",
            [61, 62, 63],
            o,
        ),
        "L71": q_lecture(
            questions,
            "Types, money helpers, timezones. Inject time. Shift with >> Asia/Kolkata.",
            [64, 65, 66, 67],
            o,
        ),
        "L72": q_lecture(
            questions,
            "Strings regex, Transform Message multiple targets, Java MIME, readUrl, log, try vs On Error, HTTP attributes.",
            [68, 69, 70, 71, 72, 73, 74],
            o,
        ),
        "L73": q_lecture(
            questions,
            "Default XML ns, YAML/Excel/flat file, Values mask, boolean precedence, two-field sort, DW vs For Each vs Batch.",
            [75, 76, 77, 78, 79, 80],
            o,
        ),
        "L54a": q_lecture(
            questions,
            "Article voiceover optional. How to drill the eighty-question bank: cover answers, speak out loud, then uncover.",
            [57, 56],
            "Point students at sections-slash-12 lecture markdown and the reference file. Do not read all eighty on camera.",
        ),
    }


LECTURE_META = [
    ("L01", "Welcome and what you will build", "3–4 min", "S01-L01-welcome.mp4", "Video"),
    ("L02", "How this course works (concept, pause, lab, quiz)", "3–4 min", "S01-L02-how-the-course-works.mp4", "Video"),
    ("L03", "Getting started: Playground vs Transform Message", "4–6 min", "S01-L03-getting-started.mp4", "Article or voiceover"),
    ("L04", "Tour of the student lab folder", "3–5 min", "S01-L04-student-folder.mp4", "Video"),
    ("L05", "What is DataWeave in Mule 4?", "4–6 min", "S02-L05-what-is-dataweave.mp4", "Video"),
    ("L06", "DataWeave 1.0 vs 2.0", "5–7 min", "S02-L06-dw1-vs-dw2.mp4", "Video"),
    ("L07", "Script structure: header, output, body", "5–8 min", "S02-L07-script-structure.mp4", "Video"),
    ("L08", "Variables, functions, types, and as", "7–10 min", "S02-L08-var-fun-types.mp4", "Video"),
    ("L09", "Section bridge: fundamentals labs", "1–2 min", "S02-L09-fundamentals-labs-bridge.mp4", "Optional video"),
    ("L11", "map, filter, dollar and dollar-dollar", "7–10 min", "S03-L11-map-filter.mp4", "Video"),
    ("L12", "sizeOf, isEmpty, flatten", "5–7 min", "S03-L12-sizeof-isempty.mp4", "Video"),
    ("L13", "Section bridge: array labs", "1–2 min", "S03-L13-array-labs-bridge.mp4", "Optional video"),
    ("L15", "Selectors: dot, brackets, star, descendant", "6–9 min", "S04-L15-selectors.mp4", "Video"),
    ("L16", "default, safe selector, skipNullOn", "6–9 min", "S04-L16-nulls.mp4", "Video"),
    ("L17", "mapObject and pluck", "6–9 min", "S04-L17-mapobject-pluck.mp4", "Video"),
    ("L18", "Section bridge: object labs", "1–2 min", "S04-L18-object-labs-bridge.mp4", "Optional video"),
    ("L20", "plus-plus vs plus; split, join, case", "6–9 min", "S05-L20-strings.mp4", "Video"),
    ("L21", "if/else expressions (no Java ternary)", "5–8 min", "S05-L21-if-else.mp4", "Video"),
    ("L22", "Section bridge: string labs", "1–2 min", "S05-L22-string-labs-bridge.mp4", "Optional video"),
    ("L24", "JSON to XML (single root)", "6–9 min", "S06-L24-json-to-xml.mp4", "Video"),
    ("L25", "XML attributes and repeating elements", "6–9 min", "S06-L25-xml-attributes.mp4", "Video"),
    ("L26", "CSV to JSON and JSON to CSV", "6–9 min", "S06-L26-csv.mp4", "Video"),
    ("L27", "Section bridge: format labs", "1–2 min", "S06-L27-format-labs-bridge.mp4", "Optional video"),
    ("L29", "groupBy, orderBy, distinctBy", "7–10 min", "S07-L29-groupby.mp4", "Video"),
    ("L30", "reduce and flatten", "7–10 min", "S07-L30-reduce.mp4", "Video"),
    ("L31", "flatMap line items (concept)", "5–8 min", "S07-L31-flatmap-concept.mp4", "Video"),
    ("L32", "Merge, update, and do", "7–10 min", "S07-L32-merge-update-do.mp4", "Video"),
    ("L33", "Homework recap pointer (Lab 20)", "3–5 min", "S07-L33-lab20-recap.mp4", "Optional if Lab 20 exists"),
    ("L35", "Dates, formats, and periods", "6–9 min", "S08-L35-dates.mp4", "Video"),
    ("L36", "match and try / orElse", "7–10 min", "S08-L36-match-try.mp4", "Video"),
    ("L37", "Section bridge: date labs", "1–2 min", "S08-L37-date-labs-bridge.mp4", "Optional video"),
    ("L39", "vars, attributes, and properties", "6–9 min", "S09-L39-mule-context.mp4", "Video"),
    ("L40", "Modules and Transform Message vs hash-bracket", "6–9 min", "S09-L40-modules.mp4", "Video"),
    ("L41", "Section bridge: join labs 31–32", "1–2 min", "S09-L41-join-labs-bridge.mp4", "Optional video"),
    ("L42", "Why not lookup or Java inside every map", "6–9 min", "S09-L42-no-n-plus-one.mp4", "Video"),
    ("L44", "Recursion and match on types", "8–12 min", "S10-L44-recursion.mp4", "Video"),
    ("L45", "Deep PII mask (concept)", "3–6 min", "S10-L45-pii-concept.mp4", "Optional if Lab 39 exists"),
    ("L46", "XML namespaces read and write", "8–12 min", "S10-L46-xml-namespaces.mp4", "Video"),
    ("L47", "Dynamic keys, diffs, last-wins, pagination", "8–12 min", "S10-L47-dynamic-keys.mp4", "Video"),
    ("L48", "Section bridge: capstone labs 53–54", "1–2 min", "S10-L48-capstone-bridge.mp4", "Optional video"),
    ("L50", "Streaming: what breaks it", "6–9 min", "S11-L50-streaming.mp4", "Video"),
    ("L51", "Crypto, binary, reader/writer properties", "8–12 min", "S11-L51-crypto-binary.mp4", "Video"),
    ("L52", "Reusable modules and performance pitfalls", "8–12 min", "S11-L52-modules-perf.mp4", "Video"),
    ("L70", "Arrays helpers: maxBy, firstWith, zip, ranges", "8–12 min", "S13-L70-arrays-helpers.mp4", "Video"),
    ("L71", "Types, money, timezones, Dates module", "8–12 min", "S13-L71-timezones-numbers.mp4", "Video"),
    ("L72", "TM targets, Java MIME, readUrl, log, HTTP attributes", "8–12 min", "S13-L72-message-and-mime.mp4", "Video"),
    ("L73", "XML ns extras, Excel/YAML, DW vs Batch", "8–12 min", "S13-L73-mime-and-architecture.mp4", "Video"),
    ("L54a", "How to run the 80-question bank", "4–6 min", "S12-L54-question-bank.mp4", "Article or voiceover"),
    ("L55", "Whiteboard mock interview (set of 6)", "split into 6×~10 min or one section", "S12-L55-whiteboard.mp4", "Video"),
    ("L56", "Nested XML to canonical JSON (Q60)", "8–12 min", "S12-L56-q60-design.mp4", "Video"),
    ("L58", "Next steps and solutions pack", "2–3 min", "S12-L58-next-steps.mp4", "Video"),
]


def load_programming_labs() -> dict[int, dict]:
    spec = importlib.util.spec_from_file_location(
        "generate_udemy_labs", ROOT / "scripts" / "generate_udemy_labs.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    parsed = mod.parse_labs(mod.SRC.read_text(encoding="utf-8"))
    return {lab["num"]: lab for lab in parsed}


# On-camera payloads when the drill states the sample in the problem text only.
DEMO_PAYLOADS: dict[int, tuple[str, str]] = {
    6: ("text", "Asha,IT,Pune"),
    7: ("json", '["red", "green", "blue"]'),
    12: ("xml", '<order id="O-9"><amount>50</amount></order>'),
    15: ("json", "[[1, 2], [3], [4, 5]]"),
    16: ("json", '{ "a": 1, "b": 2 }'),
    18: ("text", "MULE-12345"),
    20: (
        "json",
        '[\n  { "id": 1, "customerId": "C1", "amount": 10 },\n'
        '  { "id": 2, "customerId": "C2", "amount": 20 },\n'
        '  { "id": 3, "customerId": "C1", "amount": 15 }\n]',
    ),
    22: (
        "json",
        '[{ "id": "p1", "name": "A" }, { "id": "p2", "name": "B" }]',
    ),
    25: (
        "json",
        '{ "a": 1, "b": 2 }\n\n'
        "Also set vars.base to `{ \"b\": 9, \"c\": 3 }` (right-hand object is payload, or swap and say plus-plus).",
    ),
    27: (
        "json",
        '[{ "id": 1, "date": "2026-08-20" }, { "id": 2, "date": "21/08/2026" }, { "id": 3, "date": "bad" }]',
    ),
    28: ("json", '{ "note": "now() ignores payload; empty object is fine" }'),
    29: ("text", "Name,Amount\nAsha,10.5\nBen,3"),
    30: (
        "json",
        '[{ "id": "O1", "name": "Asha" }, { "id": "O2", "name": "Ben" }]',
    ),
    32: (
        "json",
        '{\n  "orders": [{ "id": "O1", "customerId": "C1" }],\n'
        '  "customers": [{ "id": "C1", "name": "Asha" }]\n}',
    ),
    33: ("json", '{ "code": 404 }'),
    34: ("json", "[10, 20, 30, 40, 50]"),
    39: (
        "json",
        '{ "name": "Asha", "email": "a@x.com", "address": { "ssn": "111", "city": "Pune" }, "password": "x" }',
    ),
    41: (
        "xml",
        '<ns0:order xmlns:ns0="http://acme.com/order" id="O-1">\n'
        '  <ns0:line sku="A" qty="2"/>\n'
        '  <ns0:line sku="B" qty="1"/>\n'
        "</ns0:order>",
    ),
    42: (
        "json",
        '{ "orderId": "O-1", "lines": [{ "sku": "A", "qty": 2 }, { "sku": "B", "qty": 1 }] }',
    ),
    43: (
        "json",
        '{ "a": 1, "b": 2, "c": 3 }\n\n'
        "Set vars.old to `{ \"a\": 1, \"b\": 9, \"d\": 4 }` so the script can diff.",
    ),
    44: (
        "json",
        '{ "a": 1, "nested": { "x": 1, "y": 2 } }\n\n'
        "Set vars.old to `{ \"a\": 1, \"nested\": { \"x\": 1, \"y\": 9 } }`.",
    ),
    48: (
        "json",
        '[{ "email": "a@x.com", "age": 20 }, { "email": "bad", "age": 17 }, { "email": "b@x.com", "age": "x" }]',
    ),
    49: (
        "json",
        '{ "left": [{ "id": "1", "a": 1 }], "right": [{ "id": "1", "b": 2 }, { "id": "2", "b": 3 }] }',
    ),
    50: ("json", '{ "a": "hi", "b": 2, "c": ["ok", 3] }'),
    52: (
        "json",
        '[{ "id": 1, "amount": 10, "qty": 2 }, { "id": 2, "amount": 10, "qty": 0 }]',
    ),
}


def format_input(lab_src: dict) -> str:
    n = lab_src.get("num")
    raw = lab_src.get("input_json")
    if raw:
        lang = lab_src.get("input_lang") or (
            "text" if lab_src.get("input_is_raw") else "json"
        )
        fence = {"json": "json", "xml": "xml", "csv": "csv", "text": "text"}.get(lang, "text")
        return f"```{fence}\n{raw}\n```"
    if n in DEMO_PAYLOADS:
        kind, sample = DEMO_PAYLOADS[n]
        if "Set vars" in sample or "Also set" in sample or "now() ignores" in sample:
            if "\n\n" in sample:
                payload, note = sample.split("\n\n", 1)
                lang = "json" if payload.strip().startswith(("{", "[")) else "text"
                return f"```{lang}\n{payload}\n```\n\n**SAY (vars):** {note}"
            return f"**SAY:** {sample}"
        return f"```{kind}\n{sample}\n```"
    body = lab_src.get("problem") or ""
    tick = re.search(r"`(\[[^\]]+\]|\{[^}]+\}|\"[^\"]+\")`", body)
    if tick:
        return f"```json\n{tick.group(1)}\n```"
    return "_Paste the sample from the lab README on screen._"


def format_expected(lab_src: dict) -> str:
    if lab_src.get("expected_block"):
        return f"```\n{lab_src['expected_block']}\n```"
    if lab_src.get("expected_note"):
        return lab_src["expected_note"]
    return "_No expected block in the reference drill; run the solution on camera and show the preview._"


def write_lab(
    lab: dict,
    tips: dict[int, str],
    src: dict,
) -> None:
    n = lab["num"]
    section = lab["section"]
    slug = lab["slug"]
    title = lab["title"]
    readme_path = ROOT / "student" / "labs" / section / f"{n:02d}-{slug}" / "README.md"
    sol_path = ROOT / "instructor" / "solutions" / section / f"{n:02d}-{slug}" / "solution.dwl"
    notes_path = sol_path.parent / "NOTES.md"
    readme = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
    solution = sol_path.read_text(encoding="utf-8") if sol_path.exists() else "// missing solution"
    notes = notes_path.read_text(encoding="utf-8") if notes_path.exists() else ""
    problem = src.get("problem") or ""
    if not problem:
        m = re.search(r"\*\*Problem:\*\*\s*(.+)", readme)
        problem = m.group(1).strip() if m else ""
    input_block = format_input(src)
    exp_block = format_expected(src)
    tip = tips.get(n, "Build the script in two or three saves. Read the header out loud.")
    mins = "8–12 min" if n >= 37 else "6–10 min"
    fname = f"LAB-{n:02d}-{slug}.mp4"
    body = f"""# LAB {n:02d} — {title}

| Field | Value |
| --- | --- |
| Level | {lab['level']} |
| Student folder | `student/labs/{section}/{n:02d}-{slug}/` |
| Solution | `instructor/solutions/{section}/{n:02d}-{slug}/solution.dwl` |
| Target length | {mins} |
| File name | `{fname}` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab {n:02d}. {title}. {problem or 'Read the problem from the README on screen.'}

{tip}

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

{input_block or '_See the lab README for input._'}

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab {n:02d} — {title}**
> Folder: `student/labs/{section}/{n:02d}-{slug}/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `{fname.replace('.mp4', '-solution.mp4')}`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
{solution.rstrip()}
```

**SAY:** That should match Expected:

{exp_block or '_See NOTES or README expected._'}

## Part 4 — Interview phrase and close

**SAY:**

{tip}

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab {n+1:02d} in this file.
"""
    if notes.strip():
        body += f"\n## Instructor notes (do not read verbatim)\n\n{notes.strip()}\n"
    outp = OUT / "labs" / f"{n:02d}-{slug}.md"
    outp.write_text(body, encoding="utf-8")


def write_index(lecture_files: list[tuple[str, str, str, str, str]]) -> None:
    lines = [
        "# Recording transcripts",
        "",
        "Spoken scripts for Vivek. **One video per concept lecture** and **one video per lab (01–58)**.",
        "",
        "How to use: open the markdown, read **SAY**, follow **PAUSE CARD**, type the **TYPE** blocks. Target 6–10 minutes; cap 12. Split Lab 23, 39, 53, 54, and the whiteboard set if needed.",
        "",
        "Quizzes on Udemy are practice tests — no transcript, no video.",
        "",
        "Regenerate after lab or Q&A edits:",
        "",
        "```bash",
        "python3 scripts/generate_transcripts.py",
        "```",
        "",
        "## Suggested recording order",
        "",
        "For each Udemy section: record the concept videos, then every lab video listed in `instructor/CURRICULUM.md` for that section. Optional “section bridge” transcripts (L09, L13, …) are skippable if the lab videos already sit in the curriculum.",
        "",
        "## Concept and section lectures",
        "",
        "| Code | Title | Length | Transcript |",
        "| --- | --- | --- | --- |",
    ]
    for code, title, mins, _fn, _kind in lecture_files:
        slug = {
            "L54a": "L54a-question-bank",
        }.get(code, None)
        path = slug or code
        # actual filenames written below
        lines.append(f"| {code} | {title} | {mins} | [lectures/{code}.md](lectures/{code}.md) |")
    lines += [
        "",
        "## Lab videos (58)",
        "",
        "All files: [`labs/`](labs/).",
        "",
        "| Lab | Transcript |",
        "| --- | --- |",
    ]
    for lab in json.loads(MANIFEST.read_text(encoding="utf-8")):
        n = lab["num"]
        slug = lab["slug"]
        lines.append(
            f"| {n:02d} {lab['title']} | [labs/{n:02d}-{slug}.md](labs/{n:02d}-{slug}.md) |"
        )
    lines += [
        "",
        "## Udemy mapping",
        "",
        "Old bundled lectures such as “Labs 03, 05, 08, 13” are replaced by individual lab videos. Keep the concept videos. Attach the matching `student/labs/...` folder on each lab lecture.",
        "",
    ]
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    questions = parse_questions(QA.read_text(encoding="utf-8"))
    if len(questions) != 80:
        raise SystemExit(f"Expected 80 questions, parsed {len(questions)}")
    tips = load_tips()
    if len(tips) != 58:
        raise SystemExit(f"Expected 58 lab tips, got {len(tips)}")

    lect_dir = OUT / "lectures"
    lab_dir = OUT / "labs"
    lect_dir.mkdir(parents=True, exist_ok=True)
    lab_dir.mkdir(parents=True, exist_ok=True)

    q_bodies = build_q_lectures(questions)
    bodies = dict(CUSTOM)
    bodies.update(q_bodies)

    for code, title, mins, fname, kind in LECTURE_META:
        if code not in bodies:
            raise SystemExit(f"Missing transcript body for {code}")
        text = wrap_lecture(code, title, mins, fname, bodies[code], kind)
        (lect_dir / f"{code}.md").write_text(text, encoding="utf-8")

    labs = json.loads(MANIFEST.read_text(encoding="utf-8"))
    src_by_num = load_programming_labs()
    for lab in labs:
        write_lab(lab, tips, src_by_num[lab["num"]])

    write_index(LECTURE_META)
    print(f"Wrote {len(LECTURE_META)} lecture transcripts and {len(labs)} lab transcripts to {OUT}")


if __name__ == "__main__":
    main()
