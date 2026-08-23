# LAB 01 — Map Salesforce Contact to a shorter API shape

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/01-map-salesforce-contact-to-a-shorter-api-shape/` |
| Solution | `instructor/solutions/01-fundamentals/01-map-salesforce-contact-to-a-shorter-api-shape/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-01-map-salesforce-contact-to-a-shorter-api-shape.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 01. Map Salesforce Contact to a shorter API shape. From each Contact, output `fullName` (FirstName + LastName, single space) and `dept` from `Department`. Skip building Java-style loops.

Named lambdas preferred. Coerce missing FirstName with default empty string before plus-plus.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "Id": "003xx000001", "FirstName": "Asha", "LastName": "Rao", "Department": "IT", "Email": "asha@acme.com" },
  { "Id": "003xx000002", "FirstName": "Ben", "LastName": "Cole", "Department": "Finance", "Email": "ben@acme.com" }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 01 — Map Salesforce Contact to a shorter API shape**
> Folder: `student/labs/01-fundamentals/01-map-salesforce-contact-to-a-shorter-api-shape/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-01-map-salesforce-contact-to-a-shorter-api-shape-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload map {
  fullName: ($.FirstName default "") ++ " " ++ ($.LastName default ""),
  dept: $.Department
}
```

**SAY:** That should match Expected:

```
[
  { "fullName": "Asha Rao", "dept": "IT" },
  { "fullName": "Ben Cole", "dept": "Finance" }
]
```

## Part 4 — Interview phrase and close

**SAY:**

Named lambdas preferred. Coerce missing FirstName with default empty string before plus-plus.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 02 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 01

Map Salesforce Contact to a shorter API shape

## Expected

```
[
  { "fullName": "Asha Rao", "dept": "IT" },
  { "fullName": "Ben Cole", "dept": "Finance" }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
