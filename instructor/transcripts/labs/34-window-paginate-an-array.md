# LAB 34 — Window / paginate an array

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/34-window-paginate-an-array/` |
| Solution | `instructor/solutions/02-intermediate/34-window-paginate-an-array/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-34-window-paginate-an-array.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 34. Window / paginate an array. Page 2, size 2 of `[1,2,3,4,5]` → `[3,4]`

drop then take, or slice. Page size from vars if you have them.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[10, 20, 30, 40, 50]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 34 — Window / paginate an array**
> Folder: `student/labs/02-intermediate/34-window-paginate-an-array/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-34-window-paginate-an-array-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
import * from dw::core::Arrays
output application/json
var page = 2
var size = 2
---
payload drop ((page - 1) * size) take size
```

**SAY:** That should match Expected:

_No expected block in the reference drill; run the solution on camera and show the preview._

## Part 4 — Interview phrase and close

**SAY:**

drop then take, or slice. Page size from vars if you have them.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 35 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 34

Window / paginate an array

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
