# LAB 46 — Running totals

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/46-running-totals/` |
| Solution | `instructor/solutions/03-advanced/46-running-totals/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-46-running-totals.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 46. Running totals. Running totals

reduce with accumulator carrying total so far. Do not mutate; build a new array.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[10, 20, 30]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 46 — Running totals**
> Folder: `student/labs/03-advanced/46-running-totals/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-46-running-totals-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload reduce ((n, acc = []) -> acc ++ [ (acc[-1] default 0) + n ])
```

**SAY:** That should match Expected:

_No expected block in the reference drill; run the solution on camera and show the preview._

## Part 4 — Interview phrase and close

**SAY:**

reduce with accumulator carrying total so far. Do not mutate; build a new array.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 47 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 46

Running totals

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
