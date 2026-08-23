# LAB 43 — Diff two flat objects (changed keys)

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/43-diff-two-flat-objects-changed-keys/` |
| Solution | `instructor/solutions/03-advanced/43-diff-two-flat-objects-changed-keys/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-43-diff-two-flat-objects-changed-keys.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 43. Diff two flat objects (changed keys). `vars.old` vs `payload`. List `{ field, from, to }` for keys whose values changed (and keys only in one side).

Compare namesOf old and new. Output field, from, and to.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{ "a": 1, "b": 2, "c": 3 }
```

**SAY (vars):** Set vars.old to `{ "a": 1, "b": 9, "d": 4 }` so the script can diff.

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 43 — Diff two flat objects (changed keys)**
> Folder: `student/labs/03-advanced/43-diff-two-flat-objects-changed-keys/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-43-diff-two-flat-objects-changed-keys-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var old = vars.old
var newp = payload
var allKeys = (namesOf(old) ++ namesOf(newp)) distinctBy $
---
allKeys
  filter ((k) -> old[k] != newp[k])
  map (k) -> { field: k, from: old[k], to: newp[k] }
```

**SAY:** That should match Expected:

_No expected block in the reference drill; run the solution on camera and show the preview._

## Part 4 — Interview phrase and close

**SAY:**

Compare namesOf old and new. Output field, from, and to.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 44 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 43

Diff two flat objects (changed keys)

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
