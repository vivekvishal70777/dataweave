# LAB 03 — Sum array of numbers

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/03-sum-array-of-numbers/` |
| Solution | `instructor/solutions/01-fundamentals/03-sum-array-of-numbers/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-03-sum-array-of-numbers.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 03. Sum array of numbers. Return the total of `payload`.

Sum walks the array of numbers. Say sum of payload, not a Java for-loop.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[10, 20, 30, 40]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 03 — Sum array of numbers**
> Folder: `student/labs/01-fundamentals/03-sum-array-of-numbers/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-03-sum-array-of-numbers-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
sum(payload)
```

**SAY:** That should match Expected:

`100`

## Part 4 — Interview phrase and close

**SAY:**

Sum walks the array of numbers. Say sum of payload, not a Java for-loop.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 04 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 03

Sum array of numbers

## Expected (note)

`100`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
