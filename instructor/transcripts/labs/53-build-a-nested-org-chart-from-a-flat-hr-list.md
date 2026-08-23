# LAB 53 — Build a nested org chart from a flat HR list

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/53-build-a-nested-org-chart-from-a-flat-hr-list/` |
| Solution | `instructor/solutions/03-advanced/53-build-a-nested-org-chart-from-a-flat-hr-list/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-53-build-a-nested-org-chart-from-a-flat-hr-list.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 53. Build a nested org chart from a flat HR list. Flat employees + `managerId` → nested `children`. Index by manager. Roots have `managerId: null`.

Index by managerId. Recurse children. Watch cycles if they ask.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "id": "1", "name": "CEO", "managerId": null },
  { "id": "2", "name": "Eng", "managerId": "1" },
  { "id": "3", "name": "Dev", "managerId": "2" }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 53 — Build a nested org chart from a flat HR list**
> Folder: `student/labs/03-advanced/53-build-a-nested-org-chart-from-a-flat-hr-list/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-53-build-a-nested-org-chart-from-a-flat-hr-list-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var byMgr = payload groupBy ((e) -> e.managerId default "ROOT")
fun node(e) = {
  id: e.id,
  name: e.name,
  children: (byMgr[e.id] default []) map node($)
}
---
(byMgr["ROOT"] default []) map node($)
```

**SAY:** That should match Expected:

CEO → children Eng → children Dev.

## Part 4 — Interview phrase and close

**SAY:**

Index by managerId. Recurse children. Watch cycles if they ask.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 54 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 53

Build a nested org chart from a flat HR list

## Expected (note)

CEO → children Eng → children Dev.

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
