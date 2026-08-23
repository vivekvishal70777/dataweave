# LAB 20 — Total amount per customer

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/20-total-amount-per-customer/` |
| Solution | `instructor/solutions/02-intermediate/20-total-amount-per-customer/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-20-total-amount-per-customer.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 20. Total amount per customer. Return `{ customerId, total }` for each customer.

After groupBy, map the entries and sum amounts. This is the homework recap pattern.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "id": 1, "customerId": "C1", "amount": 10 },
  { "id": 2, "customerId": "C2", "amount": 20 },
  { "id": 3, "customerId": "C1", "amount": 15 }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 20 — Total amount per customer**
> Folder: `student/labs/02-intermediate/20-total-amount-per-customer/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-20-total-amount-per-customer-solution.mp4`._

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
    total: sum(orders.amount)
  })
```

**SAY:** That should match Expected:

_No expected block in the reference drill; run the solution on camera and show the preview._

## Part 4 — Interview phrase and close

**SAY:**

After groupBy, map the entries and sum amounts. This is the homework recap pattern.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 21 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 20

Total amount per customer

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
