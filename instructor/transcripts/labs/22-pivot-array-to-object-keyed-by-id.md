# LAB 22 — Pivot array to object keyed by id

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/22-pivot-array-to-object-keyed-by-id/` |
| Solution | `instructor/solutions/02-intermediate/22-pivot-array-to-object-keyed-by-id/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-22-pivot-array-to-object-keyed-by-id.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 22. Pivot array to object keyed by id. `[{ "id": "u1", "name": "Asha" }]` → `{ "u1": "Asha" }`

reduce into an object keyed by id. Dynamic key needs parentheses around the expression.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[{ "id": "p1", "name": "A" }, { "id": "p2", "name": "B" }]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 22 — Pivot array to object keyed by id**
> Folder: `student/labs/02-intermediate/22-pivot-array-to-object-keyed-by-id/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-22-pivot-array-to-object-keyed-by-id-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload reduce ((item, acc = {}) -> acc ++ { (item.id): item.name })
```

**SAY:** That should match Expected:

_No expected block in the reference drill; run the solution on camera and show the preview._

## Part 4 — Interview phrase and close

**SAY:**

reduce into an object keyed by id. Dynamic key needs parentheses around the expression.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 23 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 22

Pivot array to object keyed by id

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
