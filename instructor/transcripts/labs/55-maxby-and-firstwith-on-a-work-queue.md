# LAB 55 — maxBy and firstWith on a work queue

| Field | Value |
| --- | --- |
| Level | industry |
| Student folder | `student/labs/04-industry/55-maxby-and-firstwith-on-a-work-queue/` |
| Solution | `instructor/solutions/04-industry/55-maxby-and-firstwith-on-a-work-queue/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-55-maxby-and-firstwith-on-a-work-queue.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 55. maxBy and firstWith on a work queue. From a list of orders, return `{ richest, firstPaid }`. `richest` is the item with max `amount` (coerce Number). `firstPaid` is the first item whose status is `PAID` (any case). Import `dw::core::Arrays`.

maxBy returns the item. firstWith is the first PAID. Import Arrays. Coerce amount.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "id": "O1", "status": "NEW", "amount": "40" },
  { "id": "O2", "status": "paid", "amount": "15" },
  { "id": "O3", "status": "PAID", "amount": 90 }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 55 — maxBy and firstWith on a work queue**
> Folder: `student/labs/04-industry/55-maxby-and-firstwith-on-a-work-queue/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-55-maxby-and-firstwith-on-a-work-queue-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
import * from dw::core::Arrays
output application/json
---
{
  richest: payload maxBy ((o) -> o.amount as Number),
  firstPaid: payload firstWith ((o) -> lower(o.status as String) == "paid")
}
```

**SAY:** That should match Expected:

```
{
  "richest": { "id": "O3", "status": "PAID", "amount": 90 },
  "firstPaid": { "id": "O2", "status": "paid", "amount": "15" }
}
```

## Part 4 — Interview phrase and close

**SAY:**

maxBy returns the item. firstWith is the first PAID. Import Arrays. Coerce amount.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 56 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 55

maxBy and firstWith on a work queue

## Expected

```
{
  "richest": { "id": "O3", "status": "PAID", "amount": 90 },
  "firstPaid": { "id": "O2", "status": "paid", "amount": "15" }
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
