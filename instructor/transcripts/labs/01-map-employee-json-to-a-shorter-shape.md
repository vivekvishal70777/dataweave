# LAB 01 — Map employee JSON to a shorter shape

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/01-map-employee-json-to-a-shorter-shape/` |
| Solution | `instructor/solutions/01-fundamentals/01-map-employee-json-to-a-shorter-shape/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-01-map-employee-json-to-a-shorter-shape.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 01. Map employee JSON to a shorter shape. From each employee, output `fullName` (first + last) and `dept`.

Dollar is the current employee. Join first and last with plus-plus, then rename department to dept.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "firstName": "Asha", "lastName": "Rao", "department": "IT" },
  { "firstName": "Ben", "lastName": "Cole", "department": "HR" }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 01 — Map employee JSON to a shorter shape**
> Folder: `student/labs/01-fundamentals/01-map-employee-json-to-a-shorter-shape/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-01-map-employee-json-to-a-shorter-shape-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload map {
  fullName: $.firstName ++ " " ++ $.lastName,
  dept: $.department
}
```

**SAY:** That should match Expected:

```
[
  { "fullName": "Asha Rao", "dept": "IT" },
  { "fullName": "Ben Cole", "dept": "HR" }
]
```

## Part 4 — Interview phrase and close

**SAY:**

Dollar is the current employee. Join first and last with plus-plus, then rename department to dept.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 02 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 01

Map employee JSON to a shorter shape

## Expected

```
[
  { "fullName": "Asha Rao", "dept": "IT" },
  { "fullName": "Ben Cole", "dept": "HR" }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
