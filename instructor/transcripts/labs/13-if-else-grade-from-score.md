# LAB 13 — If/else grade from score

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/13-if-else-grade-from-score/` |
| Solution | `instructor/solutions/01-fundamentals/13-if-else-grade-from-score/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-13-if-else-grade-from-score.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 13. If/else grade from score. `>=90` A, `>=75` B, `>=50` C, else F.

If/else is an expression. There is no Java question-mark colon ternary.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{ "score": 76 }
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 13 — If/else grade from score**
> Folder: `student/labs/01-fundamentals/13-if-else-grade-from-score/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-13-if-else-grade-from-score-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
if (payload.score >= 90) "A"
else if (payload.score >= 75) "B"
else if (payload.score >= 50) "C"
else "F"
```

**SAY:** That should match Expected:

_No expected block in the reference drill; run the solution on camera and show the preview._

## Part 4 — Interview phrase and close

**SAY:**

If/else is an expression. There is no Java question-mark colon ternary.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 14 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 13

If/else grade from score

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
