# LAB 50 — Tree map: apply `f` to every leaf string

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/50-tree-map-apply-f-to-every-leaf-string/` |
| Solution | `instructor/solutions/03-advanced/50-tree-map-apply-f-to-every-leaf-string/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-50-tree-map-apply-f-to-every-leaf-string.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 50. Tree map: apply `f` to every leaf string. Uppercase every string leaf; leave numbers as-is.

Tree map: same recursion as mask, but apply f to every string leaf.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{ "a": "hi", "b": 2, "c": ["ok", 3] }
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 50 — Tree map: apply `f` to every leaf string**
> Folder: `student/labs/03-advanced/50-tree-map-apply-f-to-every-leaf-string/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-50-tree-map-apply-f-to-every-leaf-string-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
fun mapLeaves(x) =
  x match {
    case s is String -> upper(s)
    case a is Array -> a map mapLeaves($)
    case o is Object -> o mapObject ((v, k) -> { (k): mapLeaves(v) })
    else -> x
  }
---
mapLeaves(payload)
```

**SAY:** That should match Expected:

_No expected block in the reference drill; run the solution on camera and show the preview._

## Part 4 — Interview phrase and close

**SAY:**

Tree map: same recursion as mask, but apply f to every string leaf.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 51 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 50

Tree map: apply `f` to every leaf string

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
