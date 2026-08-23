# LAB 27 — Parse mixed date formats

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/27-parse-mixed-date-formats/` |
| Solution | `instructor/solutions/02-intermediate/27-parse-mixed-date-formats/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-27-parse-mixed-date-formats.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 27. Parse mixed date formats. Accept `yyyy-MM-dd` or `dd/MM/yyyy`. Invalid → `null`.

try the first date format, orElseTry the next. default will not save a bad as-Date.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[{ "id": 1, "date": "2026-08-20" }, { "id": 2, "date": "21/08/2026" }, { "id": 3, "date": "bad" }]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 27 — Parse mixed date formats**
> Folder: `student/labs/02-intermediate/27-parse-mixed-date-formats/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-27-parse-mixed-date-formats-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
import try, orElseTry, orElse from dw::Runtime
output application/json
fun parseDate(s) =
  try(() -> s as Date {format: "yyyy-MM-dd"})
    orElseTry (() -> s as Date {format: "dd/MM/yyyy"})
    orElse null
---
payload map { id: $.id, date: parseDate($.date as String) }
```

**SAY:** That should match Expected:

_No expected block in the reference drill; run the solution on camera and show the preview._

## Part 4 — Interview phrase and close

**SAY:**

try the first date format, orElseTry the next. default will not save a bad as-Date.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 28 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 27

Parse mixed date formats

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
