# LAB 30 — JSON to CSV

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/30-json-to-csv/` |
| Solution | `instructor/solutions/02-intermediate/30-json-to-csv/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-30-json-to-csv.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 30. JSON to CSV. Write `id,name` CSV with header.

output application/csv header true. Object keys become column names.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[{ "id": "O1", "name": "Asha" }, { "id": "O2", "name": "Ben" }]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 30 — JSON to CSV**
> Folder: `student/labs/02-intermediate/30-json-to-csv/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-30-json-to-csv-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/csv header=true
---
payload map {
  id: $.id,
  name: $.name
}
```

**SAY:** That should match Expected:

_No expected block in the reference drill; run the solution on camera and show the preview._

## Part 4 — Interview phrase and close

**SAY:**

output application/csv header true. Object keys become column names.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 31 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 30

JSON to CSV

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
