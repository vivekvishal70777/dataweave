# LAB 49 — Outer-join style merge of two lists by `id`

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/49-outer-join-style-merge-of-two-lists-by-id/` |
| Solution | `instructor/solutions/03-advanced/49-outer-join-style-merge-of-two-lists-by-id/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-49-outer-join-style-merge-of-two-lists-by-id.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 49. Outer-join style merge of two lists by `id`. Union by `id`; fields from left and right,

Outer merge by id. Right overwrites. Union of keys.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "left": [{ "id": "1", "a": 1, "name": "old" }],
  "right": [{ "id": "1", "b": 2, "name": "new" }, { "id": "2", "b": 3 }]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 49 — Outer-join style merge of two lists by `id`**
> Folder: `student/labs/03-advanced/49-outer-join-style-merge-of-two-lists-by-id/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-49-outer-join-style-merge-of-two-lists-by-id-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var left = payload.left groupBy ((x) -> x.id)
var right = payload.right groupBy ((x) -> x.id)
var ids = (namesOf(left) ++ namesOf(right)) distinctBy $
---
ids map (id) -> (left[id][0] default {}) ++ (right[id][0] default {})
```

**SAY:** That should match Expected:

id `1` has `a`, `b`, `name=new`; id `2` from right only.

## Part 4 — Interview phrase and close

**SAY:**

Outer merge by id. Right overwrites. Union of keys.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 50 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 49

Outer-join style merge of two lists by `id`

## Expected (note)

id `1` has `a`, `b`, `name=new`; id `2` from right only.

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
