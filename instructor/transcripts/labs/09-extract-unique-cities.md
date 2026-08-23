# LAB 09 — Extract unique cities

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/09-extract-unique-cities/` |
| Solution | `instructor/solutions/01-fundamentals/09-extract-unique-cities/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-09-extract-unique-cities.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 09. Extract unique cities. Unique `city` values, sorted.

distinctBy email or city keeps the first unique key. Mention last-wins as a later lab.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "city": "Pune" },
  { "city": "Mumbai" },
  { "city": "Pune" }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 09 — Extract unique cities**
> Folder: `student/labs/01-fundamentals/09-extract-unique-cities/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-09-extract-unique-cities-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload.city distinctBy $ orderBy $
```

**SAY:** That should match Expected:

`["Mumbai", "Pune"]`

## Part 4 — Interview phrase and close

**SAY:**

distinctBy email or city keeps the first unique key. Mention last-wins as a later lab.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 10 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 09

Extract unique cities

## Expected (note)

`["Mumbai", "Pune"]`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
