# LAB 20 — Total amount per customer (groupBy + sum)

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/20-total-amount-per-customer-groupby-sum/` |
| Solution | `instructor/solutions/02-intermediate/20-total-amount-per-customer-groupby-sum/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-20-total-amount-per-customer-groupby-sum.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 20. Total amount per customer (groupBy + sum). Return `{ customerId, orderCount, total }` per customer. Coerce amounts. This is the standard interview follow-up to `groupBy`.

groupBy then pluck. Coerce amounts. Add orderCount. No nested-filter per customer.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "id": "ORD-1", "customerId": "C1", "amount": "10.00" },
  { "id": "ORD-2", "customerId": "C2", "amount": "20" },
  { "id": "ORD-3", "customerId": "C1", "amount": 15 }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 20 — Total amount per customer (groupBy + sum)**
> Folder: `student/labs/02-intermediate/20-total-amount-per-customer-groupby-sum/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-20-total-amount-per-customer-groupby-sum-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload groupBy ((o) -> o.customerId)
  pluck ((orders, customerId) -> {
    customerId: customerId,
    orderCount: sizeOf(orders),
    total: sum(orders.amount map ($ as Number))
  })
```

**SAY:** That should match Expected:

```
[
  { "customerId": "C1", "orderCount": 2, "total": 25.00 },
  { "customerId": "C2", "orderCount": 1, "total": 20 }
]
```

## Part 4 — Interview phrase and close

**SAY:**

groupBy then pluck. Coerce amounts. Add orderCount. No nested-filter per customer.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 21 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 20

Total amount per customer (groupBy + sum)

## Expected

```
[
  { "customerId": "C1", "orderCount": 2, "total": 25.00 },
  { "customerId": "C2", "orderCount": 1, "total": 20 }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
