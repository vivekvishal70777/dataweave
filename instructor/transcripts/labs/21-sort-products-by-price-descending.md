# LAB 21 — Sort products by price descending

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/21-sort-products-by-price-descending/` |
| Solution | `instructor/solutions/02-intermediate/21-sort-products-by-price-descending/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-21-sort-products-by-price-descending.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 21. Sort products by price descending. Sort products by price descending

orderBy minus price or orderBy descending. Show the minus trick and the named lambda.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[{ "name": "A", "price": 30 }, { "name": "B", "price": 90 }]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 21 — Sort products by price descending**
> Folder: `student/labs/02-intermediate/21-sort-products-by-price-descending/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-21-sort-products-by-price-descending-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload orderBy ((p) -> -p.price)
```

**SAY:** That should match Expected:

_No expected block in the reference drill; run the solution on camera and show the preview._

## Part 4 — Interview phrase and close

**SAY:**

orderBy minus price or orderBy descending. Show the minus trick and the named lambda.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 22 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 21

Sort products by price descending

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
