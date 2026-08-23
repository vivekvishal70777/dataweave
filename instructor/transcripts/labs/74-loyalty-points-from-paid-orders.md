# LAB 74 — Loyalty points from paid orders

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/74-loyalty-points-from-paid-orders/` |
| Solution | `instructor/solutions/05-mapping/74-loyalty-points-from-paid-orders/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-74-loyalty-points-from-paid-orders.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 74. Loyalty points from paid orders. 1 point per whole INR of paid amount. status PAID/SETTLED any case. Sum points per customerId.

Paid or settled only. floor of sum is loyalty points. groupBy customer.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "customerId": "C1", "status": "paid", "amount": "199.9" },
  { "customerId": "C1", "status": "NEW", "amount": "50" },
  { "customerId": "C2", "status": "SETTLED", "amount": "10.1" }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 74 — Loyalty points from paid orders**
> Folder: `student/labs/05-mapping/74-loyalty-points-from-paid-orders/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-74-loyalty-points-from-paid-orders-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload
  filter ((o) -> ["paid", "settled"] contains lower(o.status))
  groupBy $.customerId
  pluck ((rows, cid) -> {
    customerId: cid,
    points: floor(sum(rows.amount map ($ as Number)))
  })
```

**SAY:** That should match Expected:

```
[
  { "customerId": "C1", "points": 199 },
  { "customerId": "C2", "points": 10 }
]
```

## Part 4 — Interview phrase and close

**SAY:**

Paid or settled only. floor of sum is loyalty points. groupBy customer.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 75 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 74

Loyalty points from paid orders

## Expected

```
[
  { "customerId": "C1", "points": 199 },
  { "customerId": "C2", "points": 10 }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
