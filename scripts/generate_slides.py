#!/usr/bin/env python3
"""Build HTML recording slide decks from transcripts, tutorials, and section lectures."""
from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "instructor" / "slides"
TRANSCRIPTS = ROOT / "instructor" / "transcripts"
TUTORIALS = ROOT / "student" / "tutorials"
SECTIONS = ROOT / "sections"

SKIP_SNIPPETS = (
    "type every dataweave sample on screen",
    "read the header out loud: percent dw two point oh",
    "read the **say** lines",
    "follow **on camera**",
    "keep the take under the target length",
    "do not show `solution.dwl` until after the pause card",
    "_end recording part 1",
)

GENERIC_CLOSE = (
    "close by repeating the interview phrase in one sentence",
    "point to the lab videos for this section",
    "stop. do not start a new topic",
)

SECTION_FOLDERS = [
    ("01-welcome-and-setup", "Welcome and setup"),
    ("02-dataweave-fundamentals", "DataWeave 2.0 fundamentals"),
    ("03-arrays-and-core-operators", "Arrays: map, filter, and indexes"),
    ("04-objects-nulls-and-selectors", "Objects, nulls, and selectors"),
    ("05-strings-numbers-conditionals", "Strings, numbers, and conditionals"),
    ("06-json-xml-csv", "JSON, XML, and CSV mappings"),
    ("07-intermediate-transforms", "Group, reduce, merge, and update"),
    ("08-dates-match-and-errors", "Dates, pattern matching, and try"),
    ("09-joins-modules-mule-context", "Joins, modules, and Mule context"),
    ("10-advanced-recursion-and-xml-ns", "Advanced: recursion, namespaces, diffs"),
    ("11-performance-and-production", "Streaming, crypto, modules, and pitfalls"),
    ("13-industry-operators-and-mule-message", "Industry operators, message, and MIME"),
    ("14-dataweave-mapping", "DataWeave Mapping"),
    ("12-interview-bootcamp", "Interview bootcamp"),
]


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def inline_md(text: str) -> str:
    text = esc(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def highlight(code: str, lang: str) -> str:
    raw = esc(code.rstrip()) + "\n"
    lang = (lang or "").lower()
    if lang in {"dataweave", "dw", "dwl"}:
        raw = re.sub(r"(//[^\n]*)", r'<span class="cm">\1</span>', raw)
        raw = re.sub(
            r"\b(%dw|output|input|var|fun|ns|import|type|if|else|case|match|default|do|using|is|as|true|false|null)\b",
            r'<span class="kw">\1</span>',
            raw,
        )
        raw = re.sub(r"(&quot;.*?&quot;)", r'<span class="str">\1</span>', raw)
        raw = re.sub(r"\b(\d+(?:\.\d+)?)\b", r'<span class="num">\1</span>', raw)
    elif lang in {"json", "javascript"}:
        raw = re.sub(r"(&quot;.*?&quot;)", r'<span class="str">\1</span>', raw)
        raw = re.sub(r"\b(\d+(?:\.\d+)?)\b", r'<span class="num">\1</span>', raw)
    elif lang in {"xml", "html"}:
        raw = re.sub(r"(&lt;/?[\w:#-]+)", r'<span class="kw">\1</span>', raw)
        raw = re.sub(r"(&quot;.*?&quot;)", r'<span class="str">\1</span>', raw)
    return raw


def skip_text(text: str) -> bool:
    s = re.sub(r"\s+", " ", text).strip().lower()
    if not s:
        return True
    return any(tok in s for tok in SKIP_SNIPPETS)


def is_generic_close(text: str) -> bool:
    return any(tok in text.lower() for tok in GENERIC_CLOSE)


def split_sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9“\"])", text)
    out: list[str] = []
    buf = ""
    for part in parts:
        if buf and len(buf) + len(part) > 160:
            out.append(buf)
            buf = part
        else:
            buf = (buf + " " + part).strip()
    if buf:
        out.append(buf)
    return out


def parse_meta(md: str) -> dict[str, str]:
    meta: dict[str, str] = {}
    heading = re.search(r"^# (.+)$", md, flags=re.M)
    meta["heading"] = heading.group(1).strip() if heading else "Untitled"
    for key, val in re.findall(r"^\| ([^|]+) \| ([^|]+) \|", md, flags=re.M):
        key, val = key.strip(), val.strip().strip("`")
        if key.lower() in {"field", "---"}:
            continue
        meta[key] = val
    return meta


def extract_blocks(md: str) -> list[tuple[str, str]]:
    md = md.replace("\r\n", "\n")
    cut = re.search(r"^## Instructor notes\b", md, flags=re.M)
    if cut:
        md = md[: cut.start()]
    parts = re.split(r"^## (.+)$", md, flags=re.M)
    blocks: list[tuple[str, str]] = []
    if parts[0].strip():
        blocks.append(("", parts[0]))
    i = 1
    while i + 1 < len(parts):
        blocks.append((parts[i].strip(), parts[i + 1]))
        i += 2
    return blocks


def take_fences(body: str) -> list[tuple[str, str]]:
    return [
        (lang or "text", code.rstrip())
        for lang, code in re.findall(r"```(\w+)?\n(.*?)```", body, flags=re.S)
    ]


def take_list(body: str) -> list[str]:
    items = re.findall(r"^[-*] (.+)$", body, flags=re.M)
    return [re.sub(r"\s+", " ", x).strip() for x in items if not skip_text(x)]


def take_say(body: str) -> str:
    chunks: list[str] = []
    for m in re.finditer(
        r"\*\*SAY:\*\*\s*\n+(.*?)(?=\n\*\*[A-Z][A-Z /()]+:\*\*|\Z)",
        body,
        flags=re.S,
    ):
        chunk = re.sub(r"```.*?```", "", m.group(1), flags=re.S).strip()
        if chunk:
            chunks.append(chunk)
    return "\n\n".join(chunks)


def strip_directives(body: str) -> str:
    body = re.sub(r"\*\*ON CAMERA:\*\*.*", "", body)
    body = re.sub(r"\*\*ON SCREEN:\*\*.*", "", body)
    body = re.sub(r"\*\*TYPE:\*\*\s*", "", body)
    say = take_say(body)
    if say:
        return say
    return body.strip()


def bullets_from_prose(text: str) -> list[str]:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    listed = take_list(text)
    if listed:
        return listed
    bits: list[str] = []
    for para in re.split(r"\n\s*\n", text):
        para = re.sub(r"^\*\*[A-Z /()]+:\*\*\s*", "", para.strip())
        para = para.strip()
        if skip_text(para) or is_generic_close(para):
            continue
        if para.startswith(">") or para.startswith("|") or para.startswith("#") or para.startswith("```"):
            continue
        bits.extend(split_sentences(para))
    return [b for b in bits if not skip_text(b)][:12]


class Deck:
    def __init__(self, kicker: str, title: str, assets: str):
        self.kicker = kicker
        self.title = title
        self.assets = assets
        self.slides: list[str] = []
        self.items: list[dict] = []

    def add(
        self,
        kind: str,
        heading: str,
        body_html: str = "",
        notes: str = "",
        kicker: str | None = None,
        bullets: list[str] | None = None,
        code: str | None = None,
        lang: str = "",
        subtitle: str = "",
        chips: list[str] | None = None,
    ) -> None:
        cls = "slide" + ((" " + kind) if kind else "")
        kick = kicker if kicker is not None else self.kicker
        note = re.sub(r"\s+", " ", notes)[:800]
        self.items.append(
            {
                "kind": kind or "content",
                "heading": heading,
                "kicker": kick,
                "notes": note,
                "bullets": bullets or [],
                "code": code or "",
                "lang": lang,
                "subtitle": subtitle,
                "chips": [c for c in (chips or []) if c],
            }
        )
        self.slides.append(
            f'<section class="{cls}" data-notes="{esc(note)}">'
            f'<div class="kicker">{esc(kick)}</div>'
            f"<h1>{inline_md(heading)}</h1>"
            f"{body_html}"
            "</section>"
        )

    def add_title(self, subtitle: str, chips: list[str] | None = None) -> None:
        chips_html = ""
        if chips:
            chips_html = '<div class="chips">' + "".join(
                f'<span class="chip">{esc(c)}</span>' for c in chips if c
            ) + "</div>"
        self.add(
            "title",
            self.title,
            f'<p class="sub">{inline_md(subtitle)}</p>{chips_html}',
            notes="Open PowerPoint Slide Show (F5). Share this window. Switch to Playground on code slides.",
            subtitle=subtitle,
            chips=chips,
        )

    def add_bullets(
        self,
        heading: str,
        bullets: list[str],
        notes: str = "",
        kicker: str | None = None,
    ) -> None:
        clean = [b.strip() for b in bullets if b.strip() and not skip_text(b)]
        if not clean:
            return
        for i in range(0, len(clean), 4):
            chunk = clean[i : i + 4]
            ul = "<ul>" + "".join(f"<li>{inline_md(b)}</li>" for b in chunk) + "</ul>"
            label = heading if i == 0 else f"{heading} (cont.)"
            self.add("content", label, ul, notes=notes, kicker=kicker, bullets=chunk)

    def add_code(self, heading: str, lang: str, code: str, notes: str = "") -> None:
        if not code.strip():
            return
        self.add(
            "code",
            heading,
            f"<pre><code>{highlight(code, lang)}</code></pre>",
            notes=notes
            or "Type this. Read the header: percent dw two point oh, output, dash dash dash.",
            code=code,
            lang=lang,
        )

    def add_pause(self, heading: str, bullets: list[str], notes: str = "") -> None:
        ul = "<ul>" + "".join(f"<li>{inline_md(b)}</li>" for b in bullets) + "</ul>"
        self.add(
            "pause",
            heading,
            ul,
            notes=notes or "Hold 3–5 seconds. Do not show the solution yet.",
            kicker="Pause card",
            bullets=bullets,
        )

    def render(self) -> str:
        n = max(len(self.slides), 1)
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>{esc(self.title)}</title>
  <link rel="stylesheet" href="{self.assets}/deck.css"/>
</head>
<body class="deck">
{chr(10).join(self.slides)}
<div class="chrome"><span>{esc(self.kicker)}</span><span>← → space · F fullscreen · N notes</span><span id="counter">1 / {n}</span></div>
<div class="progress" id="progress"></div>
<aside class="notes" id="notes"><h3>Speaker notes</h3><p></p></aside>
<script src="{self.assets}/deck.js"></script>
</body>
</html>
"""


def lecture_deck(path: Path) -> Deck:
    md = path.read_text(encoding="utf-8")
    meta = parse_meta(md)
    heading = meta["heading"]
    code, _, title = heading.partition(" — ")
    code, title = code.strip(), (title.strip() or heading)
    deck = Deck(code, title, "../assets")
    deck.add_title(
        "Record from this deck. Switch to the Playground when a code slide appears.",
        [meta.get("Target length", ""), meta.get("File name", ""), meta.get("Udemy type", "")],
    )
    saw_close = False
    for h, body in extract_blocks(md):
        if not h:
            continue
        hl = h.lower()
        notes = take_say(body) or re.sub(r"\s+", " ", body)[:500]
        fences = take_fences(body)
        listed = take_list(body)
        bullets = bullets_from_prose(strip_directives(body))

        if "pause" in hl:
            quoted = [re.sub(r"^>\s?", "", ln).strip() for ln in body.splitlines() if ln.strip().startswith(">")]
            quoted = [q for q in quoted if q]
            deck.add_pause(
                "Pause the video",
                quoted or listed or bullets or ["Pause. Try it. Resume with an attempt."],
                notes=take_say(body),
            )
            continue
        if hl.startswith("on camera"):
            cam = body.strip()
            deck.add_bullets("On camera", split_sentences(cam) or [cam], notes=cam)
            continue
        if hl == "say":
            deck.add_bullets(title if len(bullets) <= 4 else "Talking points", bullets, notes=notes)
            for lang, code_block in fences:
                deck.add_code("Example", lang, code_block, notes=notes)
            continue
        if "interview beat" in hl:
            qtitle = re.sub(r"^Interview beat —\s*", "", h)
            deck.add_bullets(qtitle, bullets or listed or [qtitle], notes=notes)
            for lang, code_block in fences:
                deck.add_code("Type this", lang, code_block, notes=notes)
            continue
        if hl.startswith("close"):
            unique = [b for b in bullets if not is_generic_close(b)]
            if unique and not saw_close:
                deck.add_bullets("Close", unique[:4], notes=notes)
                saw_close = True
            continue
        label = re.sub(r"^Part \d+ —\s*", "", h)
        if bullets:
            deck.add_bullets(label, bullets, notes=notes)
        elif listed:
            deck.add_bullets(label, listed, notes=notes)
        for lang, code_block in fences:
            deck.add_code("Example" if bullets else label, lang, code_block, notes=notes)
    if not saw_close:
        deck.add_bullets("Next", ["Stop. Do not start a new topic."])
    return deck


def lab_deck(path: Path) -> Deck:
    md = path.read_text(encoding="utf-8")
    meta = parse_meta(md)
    heading = meta["heading"]
    _, _, title = heading.partition(" — ")
    title = title.strip() or heading
    num_m = re.search(r"LAB\s+(\d+)", heading, flags=re.I)
    num = num_m.group(1) if num_m else path.stem[:2]
    folder = meta.get("Student folder", "")
    deck = Deck(f"Lab {num}", title, "../assets")
    deck.add_title(
        "Show the failing starter first. Hold the pause card before any solution.",
        [meta.get("Level", ""), meta.get("Target length", ""), meta.get("File name", "")],
    )
    for h, body in extract_blocks(md):
        if not h:
            continue
        hl = h.lower()
        notes = take_say(body)
        fences = take_fences(body)
        bullets = bullets_from_prose(strip_directives(body))
        if "pause" in hl:
            deck.add_pause(
                f"Pause — try Lab {num}",
                [
                    "Pause the video",
                    f"Open {folder or 'the student lab folder'}",
                    "Finish transform.dwl — wrong is fine",
                    "Resume when you have an attempt",
                ],
                notes=notes,
            )
            continue
        if "hook" in hl:
            deck.add_bullets("The job", bullets, notes=notes)
            continue
        if "input" in hl:
            deck.add_bullets("Paste the payload", ["Set the MIME type to match the sample."], notes=notes)
            for lang, code_block in fences:
                deck.add_code("Input", lang, code_block)
            extra = re.findall(r"\*\*SAY \(vars\):\*\*\s*(.+)", body)
            if extra:
                deck.add_bullets("Also set vars", extra)
            continue
        if "solution" in hl:
            deck.add_bullets(
                "Welcome back",
                bullets[:3]
                or [
                    "Header first: percent dw two point oh, output, dash dash dash.",
                    "Type with me. Do not paste blindly.",
                ],
                notes=notes,
            )
            for lang, code_block in fences:
                label = "Solution" if "%dw" in code_block or "payload" in code_block[:80] else "Expected"
                deck.add_code(label, lang, code_block, notes=notes)
            continue
        if "interview" in hl or hl.startswith("part 4"):
            deck.add_bullets("Interview phrase", bullets[:5], notes=notes)
            continue
        if "expected" in hl:
            for lang, code_block in fences:
                deck.add_code("Expected", lang, code_block)
            continue
        if bullets:
            deck.add_bullets(re.sub(r"^Part \d+ —\s*", "", h), bullets, notes=notes)
        for lang, code_block in fences:
            deck.add_code("Example", lang, code_block, notes=notes)
    return deck


def tutorial_deck(path: Path, section_title: str) -> Deck:
    md = path.read_text(encoding="utf-8")
    title_m = re.search(r"^# (.+)$", md, flags=re.M)
    title = title_m.group(1).strip() if title_m else path.stem
    deck = Deck(section_title, title, "../../assets")
    deck.add_title("Plain-language walkthrough. Then jump to the matching concept or lab video.")
    for h, body in extract_blocks(md):
        if not h:
            continue
        fences = take_fences(body)
        listed = take_list(body)
        prose = re.sub(r"```.*?```", "", body, flags=re.S).strip()
        prose = re.sub(r"^\*(.+)\*$", "", prose, flags=re.M).strip()
        bullets = listed or bullets_from_prose(prose)
        if bullets:
            deck.add_bullets(h, bullets)
        for lang, code_block in fences:
            deck.add_code("Tiny example" if "example" in h.lower() else h, lang, code_block)
    return deck


def section_overview_deck(path: Path) -> Deck:
    md = path.read_text(encoding="utf-8")
    title_m = re.search(r"^# (.+)$", md, flags=re.M)
    title = (title_m.group(1).strip() if title_m else path.parent.name).replace("Section — ", "")
    sid = path.parent.name
    deck = Deck(sid, title, "../assets")
    deck.add_title("Section opener. Then jump into the concept videos and labs.")

    def grab(header: str) -> str:
        m = re.search(rf"^## {re.escape(header)}\n+(.*?)(?=\n## |\Z)", md, flags=re.S | re.I)
        return m.group(1).strip() if m else ""

    for header, slide_title in [
        ("Learning objectives", "You will be able to"),
        ("Suggested video breakdown", "On camera this section"),
        ("Labs in this section", "Labs"),
        ("How to record", "How to record"),
        ("Interview talking points for this section", "Interview phrases"),
    ]:
        body = grab(header)
        items = take_list(body) or bullets_from_prose(body)
        if items:
            deck.add_bullets(slide_title, items)
    extra = grab("This section is 30 mapping labs")
    if extra:
        deck.add_bullets("Mapping labs, not new syntax", take_list(extra) or bullets_from_prose(extra))
    # Fallback: any remaining ## with lists
    if len(deck.slides) < 3:
        for h, body in extract_blocks(md):
            if not h or h.lower().startswith("section"):
                continue
            items = take_list(body) or bullets_from_prose(body)
            fences = take_fences(body)
            if items:
                deck.add_bullets(h, items[:8])
            for lang, code_block in fences[:1]:
                deck.add_code(h, lang, code_block)
    deck.add(
        "",
        "The loop",
        """<div class="grid-4">
        <div class="box"><strong>Concept</strong><span>One idea. Three to seven minutes.</span></div>
        <div class="box"><strong>Pause</strong><span>Hold the card. Students try.</span></div>
        <div class="box"><strong>Lab</strong><span>Type from the starter, not the solution.</span></div>
        <div class="box"><strong>Quiz</strong><span>Udemy practice test. No video.</span></div>
        </div>""",
        notes="Hit this slide on section openers so students remember the gym loop.",
    )
    return deck


def mapping_cluster_decks() -> list[tuple[Path, Deck]]:
    clusters = [
        (
            "S14-A-crm-commerce-payments",
            "Mapping cluster A — CRM, commerce, payments",
            "Labs 59–63",
            [
                "This section is mapping, not new syntax.",
                "Canonical names: orderId, lines, money — not vendor fields.",
                "Lookups already on the payload. Never lookup inside map.",
            ],
            [
                "59 Salesforce Account composite",
                "60 SAP-style GST invoice",
                "61 Workday workers",
                "62 Shopify to ERP",
                "63 Stripe + customer",
            ],
        ),
        (
            "S14-B-itsm-cdc-fx",
            "Mapping cluster B — ITSM, CDC, FX, EDI",
            "Labs 64–70",
            [
                "Join tables that arrived together.",
                "CDC envelopes flatten to upsert rows.",
                "Money: coerce, skip zero qty, convert FX last.",
            ],
            [
                "64 ServiceNow + CMDB",
                "65 Debezium CDC",
                "66 Color × size SKUs",
                "67 Multi-currency to USD",
                "68 IN vs US address",
                "69 EDI-like PO",
                "70 Bank ledger",
            ],
        ),
        (
            "S14-C-iam-gst-claims",
            "Mapping cluster C — IAM, stock, GST, claims",
            "Labs 71–80",
            [
                "GST: CGST/SGST vs IGST by ship-from vs ship-to state.",
                "XML namespaces stay until you map them off.",
                "Partition restock vs refund, good vs bad rows.",
            ],
            [
                "71 IdP roles",
                "72 FIFO stock",
                "73 India GST split",
                "74 Loyalty points",
                "75 IST slots",
                "76 BOM pick list",
                "77 RMA split",
                "78 Locale fallback",
                "79 Catalog XML",
                "80 ICD claims",
            ],
        ),
        (
            "S14-D-telco-recon-events",
            "Mapping cluster D — telco, recon, events",
            "Labs 81–88",
            [
                "Aggregate, then map. Do not nested-scan.",
                "SCIM patch is merge, not replace-all.",
                "Event-sourced balance is reduce in time order.",
            ],
            [
                "81 CDR minutes",
                "82 Listings + geo",
                "83 SCIM patch",
                "84 Bank UTR recon",
                "85 Routing duration",
                "86 Event balance",
                "87 Tenant overlay",
                "88 GTIN + UoM",
            ],
        ),
    ]
    out: list[tuple[Path, Deck]] = []
    for slug, title, span, ideas, labs in clusters:
        deck = Deck("DataWeave Mapping", title, "../assets")
        deck.add_title(
            "Record one cluster video, or one lab video each. Pause before every solution.",
            [span],
        )
        deck.add_bullets("Remember", ideas)
        deck.add_bullets("Labs in this cluster", labs)
        deck.add_pause(
            "After each lab hook",
            ["Show the starter fail", "Read the problem", "Hold this card", "Then type the solution"],
        )
        deck.add_bullets(
            "Close the cluster",
            ["Point at remaining homework labs.", "Quiz lives in student/quizzes."],
        )
        out.append((OUT / "lectures" / f"{slug}.html", deck))
    return out


def lecture_group(filename: str) -> str:
    names = {
        "01": "Welcome and setup",
        "02": "DataWeave 2.0 fundamentals",
        "03": "Arrays: map, filter, and indexes",
        "04": "Objects, nulls, and selectors",
        "05": "Strings, numbers, and conditionals",
        "06": "JSON, XML, and CSV mappings",
        "07": "Group, reduce, merge, and update",
        "08": "Dates, pattern matching, and try",
        "09": "Joins, modules, and Mule context",
        "10": "Advanced: recursion, namespaces, diffs",
        "11": "Streaming, crypto, modules, and pitfalls",
        "12": "Interview bootcamp",
        "13": "Industry operators, message, and MIME",
        "14": "DataWeave Mapping",
    }
    m = re.search(r"S(\d+)", filename)
    if m:
        return names.get(m.group(1), "Concept lectures")
    return "Concept lectures"


def write_deck(path: Path, deck: Deck) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(deck.render(), encoding="utf-8")


def index_html(rows: list[tuple[str, str, str, str]]) -> str:
    groups: dict[str, list[tuple[str, str, str]]] = {}
    for group, kind, title, href in rows:
        groups.setdefault(group, []).append((kind, title, href))
    parts = [
        """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Recording slides — DataWeave 2.0</title>
  <link rel="stylesheet" href="assets/deck.css"/>
  <style>
    body { overflow: auto; padding: 4vh 6vw 8vh; }
    a { color: var(--accent); text-decoration: none; }
    a:hover { text-decoration: underline; }
    h1 { max-width: none; }
    table { width: 100%; border-collapse: collapse; margin: 1.5rem 0 3rem; font-size: 16px; }
    th, td { text-align: left; padding: 0.55rem 0.4rem; border-bottom: 1px solid var(--line); vertical-align: top; }
    th { color: var(--muted); font-weight: 600; }
    .kind { color: var(--warn); font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; }
  </style>
</head>
<body>
  <div class="kicker">Instructor</div>
  <h1>Recording slides</h1>
  <p class="sub">Open a deck full screen. Arrow keys or click to advance. Press F for fullscreen, N for speaker notes. Rebuild with <code>python3 scripts/generate_slides.py</code>.</p>
"""
    ]
    for group, items in groups.items():
        parts.append(f"<h2>{esc(group)}</h2><table><tr><th>Type</th><th>Deck</th></tr>")
        for kind, title, href in items:
            parts.append(
                f'<tr><td class="kind">{esc(kind)}</td><td><a href="{esc(href)}">{esc(title)}</a></td></tr>'
            )
        parts.append("</table>")
    parts.append("</body></html>")
    return "\n".join(parts)


def main() -> None:
    rows: list[tuple[str, str, str, str]] = []

    for sid, title in SECTION_FOLDERS:
        lec = SECTIONS / sid / "LECTURE.md"
        if lec.exists():
            dest = OUT / "sections" / f"{sid}.html"
            write_deck(dest, section_overview_deck(lec))
            rows.append((title, "Section opener", title, dest.relative_to(OUT).as_posix()))

    for path in sorted((TRANSCRIPTS / "lectures").glob("L*.md")):
        meta = parse_meta(path.read_text(encoding="utf-8"))
        deck = lecture_deck(path)
        dest = OUT / "lectures" / f"{path.stem}.html"
        write_deck(dest, deck)
        group = lecture_group(meta.get("File name", ""))
        rows.append((group, "Concept video", f"{path.stem} — {deck.title}", dest.relative_to(OUT).as_posix()))

    for dest, deck in mapping_cluster_decks():
        write_deck(dest, deck)
        rows.append(("DataWeave Mapping", "Cluster video", deck.title, dest.relative_to(OUT).as_posix()))

    for path in sorted((TRANSCRIPTS / "labs").glob("*.md")):
        deck = lab_deck(path)
        dest = OUT / "labs" / f"{path.stem}.html"
        write_deck(dest, deck)
        rows.append(("Labs 01–88", "Lab video", f"{deck.kicker} — {deck.title}", dest.relative_to(OUT).as_posix()))

    for sid, title in SECTION_FOLDERS:
        tdir = TUTORIALS / sid
        if not tdir.is_dir():
            continue
        for path in sorted(tdir.glob("*.md")):
            if path.name.lower() == "readme.md":
                continue
            deck = tutorial_deck(path, title)
            dest = OUT / "tutorials" / sid / f"{path.stem}.html"
            write_deck(dest, deck)
            rows.append((f"Tutorials — {title}", "Article walkthrough", deck.title, dest.relative_to(OUT).as_posix()))

    (OUT / "index.html").write_text(index_html(rows), encoding="utf-8")
    html_files = list(OUT.rglob("*.html"))
    print(f"Wrote {len(html_files)} HTML files under {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
