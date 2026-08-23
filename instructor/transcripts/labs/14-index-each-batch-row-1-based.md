# LAB 14 — Index each batch row (1-based)

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/14-index-each-batch-row-1-based/` |
| Solution | `instructor/solutions/01-fundamentals/14-index-each-batch-row-1-based/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-14-index-each-batch-row-1-based.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 14. Index each batch row (1-based). Add a 1-based `rowNum` for error reports. `$` is value, `$$` is 0-based index.

Dollar-dollar is the 0-based index. Add one for rowNum in error reports.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
["alpha", "beta"]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 14 — Index each batch row (1-based)**
> Folder: `student/labs/01-fundamentals/14-index-each-batch-row-1-based/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-14-index-each-batch-row-1-based-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload map {
  rowNum: $$ + 1,
  value: $
}
```

**SAY:** That should match Expected:

```
[{ "rowNum": 1, "value": "alpha" }, { "rowNum": 2, "value": "beta" }]
```

## Part 4 — Interview phrase and close

**SAY:**

Dollar-dollar is the 0-based index. Add one for rowNum in error reports.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 15 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 14

Index each batch row (1-based)

## Expected

```
[{ "rowNum": 1, "value": "alpha" }, { "rowNum": 2, "value": "beta" }]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
