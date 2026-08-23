# LAB 07 — Join SKUs into a comma-separated string

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/07-join-skus-into-a-comma-separated-string/` |
| Solution | `instructor/solutions/01-fundamentals/07-join-skus-into-a-comma-separated-string/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-07-join-skus-into-a-comma-separated-string.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 07. Join SKUs into a comma-separated string. Join `["SKU-A", "SKU-B", "SKU-C"]` with `","` for a query parameter or header.

joinBy builds a query string of SKUs. Arrays use plus-plus; joinBy builds one string.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
["SKU-A", "SKU-B", "SKU-C"]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 07 — Join SKUs into a comma-separated string**
> Folder: `student/labs/01-fundamentals/07-join-skus-into-a-comma-separated-string/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-07-join-skus-into-a-comma-separated-string-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload joinBy ","
```

**SAY:** That should match Expected:

`"SKU-A,SKU-B,SKU-C"`

## Part 4 — Interview phrase and close

**SAY:**

joinBy builds a query string of SKUs. Arrays use plus-plus; joinBy builds one string.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 08 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 07

Join SKUs into a comma-separated string

## Expected (note)

`"SKU-A,SKU-B,SKU-C"`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
