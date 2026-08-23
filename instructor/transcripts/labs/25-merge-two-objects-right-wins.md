# LAB 25 — Merge two objects (right wins)

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/25-merge-two-objects-right-wins/` |
| Solution | `instructor/solutions/02-intermediate/25-merge-two-objects-right-wins/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-25-merge-two-objects-right-wins.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 25. Merge two objects (right wins). Merge `vars.base` with `payload`.

plus-plus on objects is a shallow merge. Right-hand key wins.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{ "a": 1, "b": 2 }
```

**SAY (vars):** Also set vars.base to `{ "b": 9, "c": 3 }` (right-hand object is payload, or swap and say plus-plus).

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 25 — Merge two objects (right wins)**
> Folder: `student/labs/02-intermediate/25-merge-two-objects-right-wins/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-25-merge-two-objects-right-wins-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
vars.base ++ payload
```

**SAY:** That should match Expected:

`{ "a": 1, "b": 9, "c": 3 }`

## Part 4 — Interview phrase and close

**SAY:**

plus-plus on objects is a shallow merge. Right-hand key wins.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 26 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 25

Merge two objects (right wins)

## Expected (note)

`{ "a": 1, "b": 9, "c": 3 }`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
