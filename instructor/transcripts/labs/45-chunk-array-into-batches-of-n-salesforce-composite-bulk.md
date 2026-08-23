# LAB 45 — Chunk array into batches of N (Salesforce Composite / bulk)

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/45-chunk-array-into-batches-of-n-salesforce-composite-bulk/` |
| Solution | `instructor/solutions/03-advanced/45-chunk-array-into-batches-of-n-salesforce-composite-bulk/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-45-chunk-array-into-batches-of-n-salesforce-composite-bulk.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 45. Chunk array into batches of N (Salesforce Composite / bulk). Split work into batches of 2 for a bulk API that caps records per call.

divideBy n for Salesforce Composite batch caps.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[1, 2, 3, 4, 5]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 45 — Chunk array into batches of N (Salesforce Composite / bulk)**
> Folder: `student/labs/03-advanced/45-chunk-array-into-batches-of-n-salesforce-composite-bulk/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-45-chunk-array-into-batches-of-n-salesforce-composite-bulk-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
import divideBy from dw::core::Arrays
output application/json
---
payload divideBy 2
```

**SAY:** That should match Expected:

`[[1, 2], [3, 4], [5]]`

## Part 4 — Interview phrase and close

**SAY:**

divideBy n for Salesforce Composite batch caps.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 46 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 45

Chunk array into batches of N (Salesforce Composite / bulk)

## Expected (note)

`[[1, 2], [3, 4], [5]]`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
