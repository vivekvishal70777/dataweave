# LAB 37 — Recursively flatten nested arrays

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/37-recursively-flatten-nested-arrays/` |
| Solution | `instructor/solutions/03-advanced/37-recursively-flatten-nested-arrays/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-37-recursively-flatten-nested-arrays.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 37. Recursively flatten nested arrays. Deep-flatten mixed arrays to a single list of leaves. One `flatten` is

Recurse with match: array flatMaps, else wrap the leaf.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[1, [2, [3, 4], 5], 6]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 37 — Recursively flatten nested arrays**
> Folder: `student/labs/03-advanced/37-recursively-flatten-nested-arrays/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-37-recursively-flatten-nested-arrays-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
fun deepFlatten(x) =
  x match {
    case a is Array -> a flatMap deepFlatten($)
    else -> [x]
  }
---
deepFlatten(payload)
```

**SAY:** That should match Expected:

`[1, 2, 3, 4, 5, 6]`

## Part 4 — Interview phrase and close

**SAY:**

Recurse with match: array flatMaps, else wrap the leaf.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 38 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 37

Recursively flatten nested arrays

## Expected (note)

`[1, 2, 3, 4, 5, 6]`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
