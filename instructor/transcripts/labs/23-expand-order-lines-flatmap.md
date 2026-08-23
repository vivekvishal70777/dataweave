# LAB 23 — Expand order lines (flatMap)

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/23-expand-order-lines-flatmap/` |
| Solution | `instructor/solutions/02-intermediate/23-expand-order-lines-flatmap/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-23-expand-order-lines-flatmap.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 23. Expand order lines (flatMap). One row per line item with `orderId` and `sku`.

flatMap is map then flatten. One output row per line item, carrying orderId.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  {
    "orderId": "O1",
    "items": [{ "sku": "A" }, { "sku": "B" }]
  }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 23 — Expand order lines (flatMap)**
> Folder: `student/labs/02-intermediate/23-expand-order-lines-flatmap/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-23-expand-order-lines-flatmap-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload flatMap ((order) ->
  order.items map (item) -> {
    orderId: order.orderId,
    sku: item.sku
  }
)
```

**SAY:** That should match Expected:

`[{ "orderId": "O1", "sku": "A" }, { "orderId": "O1", "sku": "B" }]`

## Part 4 — Interview phrase and close

**SAY:**

flatMap is map then flatten. One output row per line item, carrying orderId.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 24 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 23

Expand order lines (flatMap)

## Expected (note)

`[{ "orderId": "O1", "sku": "A" }, { "orderId": "O1", "sku": "B" }]`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
