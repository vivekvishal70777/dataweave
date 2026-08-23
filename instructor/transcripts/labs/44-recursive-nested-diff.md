# LAB 44 — Recursive nested diff

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/44-recursive-nested-diff/` |
| Solution | `instructor/solutions/03-advanced/44-recursive-nested-diff/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-44-recursive-nested-diff.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 44. Recursive nested diff. Return a nested object of only differences. Unchanged subtrees omitted.

Recursive diff: match types, walk objects and arrays, collect paths.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{ "a": 1, "nested": { "x": 1, "y": 2 } }
```

**SAY (vars):** Set vars.old to `{ "a": 1, "nested": { "x": 1, "y": 9 } }`.

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 44 — Recursive nested diff**
> Folder: `student/labs/03-advanced/44-recursive-nested-diff/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-44-recursive-nested-diff-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json skipNullOn="everywhere"
fun diff(a, b) =
  if (a == b) null
  else (a match {
    case ao is Object if b is Object -> do {
      var keys = (namesOf(ao) ++ namesOf(b)) distinctBy $
      var kids = keys reduce ((k, acc = {}) -> do {
        var d = diff(ao[k], b[k])
        ---
        if (d == null) acc else acc ++ { (k): d }
      })
      ---
      if (isEmpty(kids)) null else kids
    }
    else -> { from: a, to: b }
  })
---
diff(vars.old, payload)
```

**SAY:** That should match Expected:

_No expected block in the reference drill; run the solution on camera and show the preview._

## Part 4 — Interview phrase and close

**SAY:**

Recursive diff: match types, walk objects and arrays, collect paths.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 45 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 44

Recursive nested diff

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
