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

This is Lab 23. Expand order lines (flatMap). One canonical row per line: `orderId`, `sku`, `qty`. Nested `items` must not remain nested arrays.

flatMap expands 1-to-many. Default empty items so missing arrays do not fail.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  {
    "orderId": "O-1001",
    "items": [
      { "sku": "SKU-A", "qty": 2 },
      { "sku": "SKU-B", "qty": 1 }
    ]
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
  (order.items default []) map (item) -> {
    orderId: order.orderId,
    sku: item.sku,
    qty: item.qty as Number
  }
)
```

**SAY:** That should match Expected:

```
[
  { "orderId": "O-1001", "sku": "SKU-A", "qty": 2 },
  { "orderId": "O-1001", "sku": "SKU-B", "qty": 1 }
]
```

## Part 4 — Interview phrase and close

**SAY:**

flatMap expands 1-to-many. Default empty items so missing arrays do not fail.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 24 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 23

Expand order lines (flatMap)

## Expected

```
[
  { "orderId": "O-1001", "sku": "SKU-A", "qty": 2 },
  { "orderId": "O-1001", "sku": "SKU-B", "qty": 1 }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
