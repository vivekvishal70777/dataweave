# LAB 06 — Split a CSV line into fields

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/06-split-a-csv-line-into-fields/` |
| Solution | `instructor/solutions/01-fundamentals/06-split-a-csv-line-into-fields/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-06-split-a-csv-line-into-fields.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 06. Split a CSV line into fields. Split a single inbound line `"Asha,IT,Pune"` on comma (no quoted commas). Output an array of fields.

splitBy comma turns a CSV line into an array of fields.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```text
Asha,IT,Pune
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 06 — Split a CSV line into fields**
> Folder: `student/labs/01-fundamentals/06-split-a-csv-line-into-fields/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-06-split-a-csv-line-into-fields-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload splitBy ","
```

**SAY:** That should match Expected:

`["Asha", "IT", "Pune"]`

## Part 4 — Interview phrase and close

**SAY:**

splitBy comma turns a CSV line into an array of fields.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 07 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 06

Split a CSV line into fields

## Expected (note)

`["Asha", "IT", "Pune"]`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
