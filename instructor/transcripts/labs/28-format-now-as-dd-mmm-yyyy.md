# LAB 28 — Format `now()` as `dd-MMM-yyyy`

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/28-format-now-as-dd-mmm-yyyy/` |
| Solution | `instructor/solutions/02-intermediate/28-format-now-as-dd-mmm-yyyy/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-28-format-now-as-dd-mmm-yyyy.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 28. Format `now()` as `dd-MMM-yyyy`. Format `now()` as `dd-MMM-yyyy`

now as String with format dd-MMM-yyyy. Periods use pipe literals like P7D.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

**SAY:** { "note": "now() ignores payload; empty object is fine" }

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 28 — Format `now()` as `dd-MMM-yyyy`**
> Folder: `student/labs/02-intermediate/28-format-now-as-dd-mmm-yyyy/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-28-format-now-as-dd-mmm-yyyy-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
now() as String {format: "dd-MMM-yyyy"}
```

**SAY:** That should match Expected:

_No expected block in the reference drill; run the solution on camera and show the preview._

## Part 4 — Interview phrase and close

**SAY:**

now as String with format dd-MMM-yyyy. Periods use pipe literals like P7D.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 29 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 28

Format `now()` as `dd-MMM-yyyy`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
