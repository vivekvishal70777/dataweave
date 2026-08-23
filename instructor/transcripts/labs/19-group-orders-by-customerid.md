# LAB 19 — Group orders by customerId

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/19-group-orders-by-customerid/` |
| Solution | `instructor/solutions/02-intermediate/19-group-orders-by-customerid/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-19-group-orders-by-customerid.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 19. Group orders by customerId. Group the commerce array by `customerId`. `groupBy` returns an

groupBy returns an object of arrays. Say that out loud in interviews.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "id": "ORD-1", "customerId": "C1", "amount": 10 },
  { "id": "ORD-2", "customerId": "C2", "amount": 20 },
  { "id": "ORD-3", "customerId": "C1", "amount": 15 }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 19 — Group orders by customerId**
> Folder: `student/labs/02-intermediate/19-group-orders-by-customerid/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-19-group-orders-by-customerid-solution.mp4`._

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

```
{
  "C1": [
    { "id": "ORD-1", "customerId": "C1", "amount": 10 },
    { "id": "ORD-3", "customerId": "C1", "amount": 15 }
  ],
  "C2": [
    { "id": "ORD-2", "customerId": "C2", "amount": 20 }
  ]
}
```

## Part 4 — Interview phrase and close

**SAY:**

groupBy returns an object of arrays. Say that out loud in interviews.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 20 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 19

Group orders by customerId

## Expected

```
{
  "C1": [
    { "id": "ORD-1", "customerId": "C1", "amount": 10 },
    { "id": "ORD-3", "customerId": "C1", "amount": 15 }
  ],
  "C2": [
    { "id": "ORD-2", "customerId": "C2", "amount": 20 }
  ]
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
