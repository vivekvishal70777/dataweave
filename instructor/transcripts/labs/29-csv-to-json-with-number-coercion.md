# LAB 29 — CSV to JSON with number coercion

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/29-csv-to-json-with-number-coercion/` |
| Solution | `instructor/solutions/02-intermediate/29-csv-to-json-with-number-coercion/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-29-csv-to-json-with-number-coercion.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 29. CSV to JSON with number coercion. Incoming CSV with header. Coerce `Amount` to Number. MIME `application/csv`.

CSV with header becomes an array of objects. Coerce Amount as Number.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```csv
Name,Amount,City
Asha,10.5,Pune
Ben,3,Mumbai
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 29 — CSV to JSON with number coercion**
> Folder: `student/labs/02-intermediate/29-csv-to-json-with-number-coercion/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-29-csv-to-json-with-number-coercion-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload map {
  name: $.Name,
  amount: $.Amount as Number,
  city: $.City
}
```

**SAY:** That should match Expected:

```
[
  { "name": "Asha", "amount": 10.5, "city": "Pune" },
  { "name": "Ben", "amount": 3, "city": "Mumbai" }
]
```

## Part 4 — Interview phrase and close

**SAY:**

CSV with header becomes an array of objects. Coerce Amount as Number.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 30 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 29

CSV to JSON with number coercion

## Expected

```
[
  { "name": "Asha", "amount": 10.5, "city": "Pune" },
  { "name": "Ben", "amount": 3, "city": "Mumbai" }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
