# LAB 19 — Group orders by customer

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/19-group-orders-by-customer/` |
| Solution | `instructor/solutions/02-intermediate/19-group-orders-by-customer/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-19-group-orders-by-customer.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 19. Group orders by customer. Group the array by `customerId`.

groupBy returns an object whose keys are group names and values are arrays.

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
> Try **Lab 19 — Group orders by customer**
> Folder: `student/labs/02-intermediate/19-group-orders-by-customer/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-19-group-orders-by-customer-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload groupBy ((o) -> o.customerId)
```

**SAY:** That should match Expected:

`C1` → orders 1 and 3; `C2` → order 2.

## Part 4 — Interview phrase and close

**SAY:**

groupBy returns an object whose keys are group names and values are arrays.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 20 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 19

Group orders by customer

## Expected (note)

`C1` → orders 1 and 3; `C2` → order 2.

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
