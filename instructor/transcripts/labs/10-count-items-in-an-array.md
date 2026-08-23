# LAB 10 — Count items in an array

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/10-count-items-in-an-array/` |
| Solution | `instructor/solutions/01-fundamentals/10-count-items-in-an-array/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-10-count-items-in-an-array.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 10. Count items in an array. Return how many products are in `payload`.

sizeOf is length. Prefer isEmpty when you only care about empty versus not.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[{ "sku": "A" }, { "sku": "B" }, { "sku": "C" }]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 10 — Count items in an array**
> Folder: `student/labs/01-fundamentals/10-count-items-in-an-array/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-10-count-items-in-an-array-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
sizeOf(payload)
```

**SAY:** That should match Expected:

`3`

## Part 4 — Interview phrase and close

**SAY:**

sizeOf is length. Prefer isEmpty when you only care about empty versus not.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 11 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 10

Count items in an array

## Expected (note)

`3`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
