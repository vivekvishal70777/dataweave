# LAB 43 — CDC flat diff (before vs after)

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/43-cdc-flat-diff-before-vs-after/` |
| Solution | `instructor/solutions/03-advanced/43-cdc-flat-diff-before-vs-after/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-43-cdc-flat-diff-before-vs-after.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 43. CDC flat diff (before vs after). Compare `before` and `after` on the same payload. List `{ field, from, to }` for changed or missing keys. Platform event / Salesforce CDC style.

CDC before versus after on payload. List field, from, and to.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "before": { "status": "NEW", "amount": 10, "owner": "Asha" },
  "after": { "status": "PAID", "amount": 10, "paidAt": "2026-08-20" }
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 43 — CDC flat diff (before vs after)**
> Folder: `student/labs/03-advanced/43-cdc-flat-diff-before-vs-after/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-43-cdc-flat-diff-before-vs-after-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var old = payload.before
var newp = payload.after
var allKeys = (namesOf(old) ++ namesOf(newp)) distinctBy $
---
allKeys
  filter ((k) -> old[k] != newp[k])
  map (k) -> { field: k, from: old[k], to: newp[k] }
```

**SAY:** That should match Expected:

`status` and `owner`/`paidAt` appear as diffs; `amount` omitted.

## Part 4 — Interview phrase and close

**SAY:**

CDC before versus after on payload. List field, from, and to.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 44 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 43

CDC flat diff (before vs after)

## Expected (note)

`status` and `owner`/`paidAt` appear as diffs; `amount` omitted.

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
