# LAB 15 — Flatten one level of nested arrays

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/15-flatten-one-level-of-nested-arrays/` |
| Solution | `instructor/solutions/01-fundamentals/15-flatten-one-level-of-nested-arrays/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-15-flatten-one-level-of-nested-arrays.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 15. Flatten one level of nested arrays. Flatten one level only: `[[1, 2], [3], [4, 5]]` → `[1, 2, 3, 4, 5]`. Deeper trees are a later lab.

flatten is one level only. Nested arrays need recursion or repeated flatten.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[[1, 2], [3], [4, 5]]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 15 — Flatten one level of nested arrays**
> Folder: `student/labs/01-fundamentals/15-flatten-one-level-of-nested-arrays/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-15-flatten-one-level-of-nested-arrays-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
flatten(payload)
```

**SAY:** That should match Expected:

`[1, 2, 3, 4, 5]`

## Part 4 — Interview phrase and close

**SAY:**

flatten is one level only. Nested arrays need recursion or repeated flatten.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 16 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 15

Flatten one level of nested arrays

## Expected (note)

`[1, 2, 3, 4, 5]`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
