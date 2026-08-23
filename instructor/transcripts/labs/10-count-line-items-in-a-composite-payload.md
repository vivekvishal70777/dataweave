# LAB 10 — Count line items in a composite payload

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/10-count-line-items-in-a-composite-payload/` |
| Solution | `instructor/solutions/01-fundamentals/10-count-line-items-in-a-composite-payload/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-10-count-line-items-in-a-composite-payload.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 10. Count line items in a composite payload. Return how many records are in `payload.records` (Salesforce Composite / bulk query shape).

sizeOf on payload.records, not the wrapper object.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "done": true,
  "records": [
    { "Id": "a1" },
    { "Id": "a2" },
    { "Id": "a3" }
  ]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 10 — Count line items in a composite payload**
> Folder: `student/labs/01-fundamentals/10-count-line-items-in-a-composite-payload/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-10-count-line-items-in-a-composite-payload-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
sizeOf(payload.records)
```

**SAY:** That should match Expected:

`3`

## Part 4 — Interview phrase and close

**SAY:**

sizeOf on payload.records, not the wrapper object.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 11 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 10

Count line items in a composite payload

## Expected (note)

`3`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
