# LAB 61 — Workday workers to HR API (active only)

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/61-workday-workers-to-hr-api-active-only/` |
| Solution | `instructor/solutions/05-mapping/61-workday-workers-to-hr-api-active-only/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-61-workday-workers-to-hr-api-active-only.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 61. Workday workers to HR API (active only). Keep Active workers (any case). `fullName` from legal names. `managerId` from `manager.wid` (null-safe). Coerce `fte`.

Filter Active any case. manager.wid default null. FTE as Number.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "Report_Entry": [
    { "wid": "W1", "Legal_First": "Ira", "Legal_Last": "Shah", "Status": "Active", "FTE": "1.0", "manager": { "wid": "W9" } },
    { "wid": "W2", "Legal_First": "Jon", "Legal_Last": "Lee", "Status": "Terminated", "FTE": "1", "manager": {} },
    { "wid": "W3", "Legal_First": "Mia", "Legal_Last": "Das", "Status": "active", "FTE": 0.5 }
  ]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 61 — Workday workers to HR API (active only)**
> Folder: `student/labs/05-mapping/61-workday-workers-to-hr-api-active-only/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-61-workday-workers-to-hr-api-active-only-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload.Report_Entry
  filter ((w) -> lower(w.Status) == "active")
  map {
    id: $.wid,
    fullName: ($.Legal_First default "") ++ " " ++ ($.Legal_Last default ""),
    fte: $.FTE as Number,
    managerId: $.manager.wid default null
  }
```

**SAY:** That should match Expected:

```
[
  { "id": "W1", "fullName": "Ira Shah", "fte": 1.0, "managerId": "W9" },
  { "id": "W3", "fullName": "Mia Das", "fte": 0.5, "managerId": null }
]
```

## Part 4 — Interview phrase and close

**SAY:**

Filter Active any case. manager.wid default null. FTE as Number.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 62 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 61

Workday workers to HR API (active only)

## Expected

```
[
  { "id": "W1", "fullName": "Ira Shah", "fte": 1.0, "managerId": "W9" },
  { "id": "W3", "fullName": "Mia Das", "fte": 0.5, "managerId": null }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
