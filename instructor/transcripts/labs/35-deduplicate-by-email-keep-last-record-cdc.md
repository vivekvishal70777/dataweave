# LAB 35 — Deduplicate by email, keep last record (CDC)

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/35-deduplicate-by-email-keep-last-record-cdc/` |
| Solution | `instructor/solutions/02-intermediate/35-deduplicate-by-email-keep-last-record-cdc/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-35-deduplicate-by-email-keep-last-record-cdc.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 35. Deduplicate by email, keep last record (CDC). `distinctBy` keeps

distinctBy keeps first. Last-wins CDC: reduce keyed by email, then valuesOf.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "email": "a@acme.com", "name": "Old" },
  { "email": "b@acme.com", "name": "Bee" },
  { "email": "a@acme.com", "name": "New" }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 35 — Deduplicate by email, keep last record (CDC)**
> Folder: `student/labs/02-intermediate/35-deduplicate-by-email-keep-last-record-cdc/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-35-deduplicate-by-email-keep-last-record-cdc-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
valuesOf(
  payload reduce ((item, acc = {}) -> acc ++ { (item.email): item })
)
```

**SAY:** That should match Expected:

New Asha-row for `a@acme.com`, plus Bee.

## Part 4 — Interview phrase and close

**SAY:**

distinctBy keeps first. Last-wins CDC: reduce keyed by email, then valuesOf.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 36 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 35

Deduplicate by email, keep last record (CDC)

## Expected (note)

New Asha-row for `a@acme.com`, plus Bee.

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
