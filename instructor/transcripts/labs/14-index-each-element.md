# LAB 14 — Index each element

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/14-index-each-element/` |
| Solution | `instructor/solutions/01-fundamentals/14-index-each-element/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-14-index-each-element.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 14. Index each element. Add a 1-based `index` field.

Dollar-dollar is the index. Map to index and value so interviews hear both names.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
["a", "b"]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 14 — Index each element**
> Folder: `student/labs/01-fundamentals/14-index-each-element/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-14-index-each-element-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload map {
  index: $$ + 1,
  value: $
}
```

**SAY:** That should match Expected:

`[{ "index": 1, "value": "a" }, { "index": 2, "value": "b" }]`

## Part 4 — Interview phrase and close

**SAY:**

Dollar-dollar is the index. Map to index and value so interviews hear both names.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 15 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 14

Index each element

## Expected (note)

`[{ "index": 1, "value": "a" }, { "index": 2, "value": "b" }]`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
