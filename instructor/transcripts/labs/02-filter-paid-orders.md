# LAB 02 — Filter paid orders

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/02-filter-paid-orders/` |
| Solution | `instructor/solutions/01-fundamentals/02-filter-paid-orders/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-02-filter-paid-orders.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 02. Filter paid orders. Keep only orders with `status == "PAID"`.

Filter keeps rows where the predicate is true. Compare status to the string PAID, then keep only what you need.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "id": 1, "status": "PAID", "amount": 100 },
  { "id": 2, "status": "NEW", "amount": 50 },
  { "id": 3, "status": "PAID", "amount": 75 }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 02 — Filter paid orders**
> Folder: `student/labs/01-fundamentals/02-filter-paid-orders/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-02-filter-paid-orders-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload filter ((o) -> o.status == "PAID")
```

**SAY:** That should match Expected:

orders `1` and `3` only.

## Part 4 — Interview phrase and close

**SAY:**

Filter keeps rows where the predicate is true. Compare status to the string PAID, then keep only what you need.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 03 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 02

Filter paid orders

## Expected (note)

orders `1` and `3` only.

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
