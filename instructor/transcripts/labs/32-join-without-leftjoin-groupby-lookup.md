# LAB 32 — Join without `leftJoin` (groupBy lookup)

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/32-join-without-leftjoin-groupby-lookup/` |
| Solution | `instructor/solutions/02-intermediate/32-join-without-leftjoin-groupby-lookup/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-32-join-without-leftjoin-groupby-lookup.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 32. Join without `leftJoin` (groupBy lookup). Join without `leftJoin` (groupBy lookup)

groupBy customers by id, then map orders with a lookup. Same result, no N-plus-one.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "orders": [{ "id": "O1", "customerId": "C1" }],
  "customers": [{ "id": "C1", "name": "Asha" }]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 32 — Join without `leftJoin` (groupBy lookup)**
> Folder: `student/labs/02-intermediate/32-join-without-leftjoin-groupby-lookup/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-32-join-without-leftjoin-groupby-lookup-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var byId = payload.customers groupBy ((c) -> c.id)
---
payload.orders map (o) -> {
  orderId: o.id,
  customerName: (byId[o.customerId][0].name) default null
}
```

**SAY:** That should match Expected:

_No expected block in the reference drill; run the solution on camera and show the preview._

## Part 4 — Interview phrase and close

**SAY:**

groupBy customers by id, then map orders with a lookup. Same result, no N-plus-one.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 33 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 32

Join without `leftJoin` (groupBy lookup)

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
