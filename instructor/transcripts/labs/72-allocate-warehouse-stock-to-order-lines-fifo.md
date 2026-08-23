# LAB 72 — Allocate warehouse stock to order lines FIFO

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/72-allocate-warehouse-stock-to-order-lines-fifo/` |
| Solution | `instructor/solutions/05-mapping/72-allocate-warehouse-stock-to-order-lines-fifo/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-72-allocate-warehouse-stock-to-order-lines-fifo.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 72. Allocate warehouse stock to order lines FIFO. For each order line, allocated = min(qty, stock for sku). leftover stock is not required. Unmatched sku allocated 0.

Allocate min of remaining stock and qty. Reduce the on-hand map.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "stock": [
    { "sku": "A", "onHand": 5 },
    { "sku": "B", "onHand": 1 }
  ],
  "order": [
    { "sku": "A", "qty": 3 },
    { "sku": "A", "qty": 4 },
    { "sku": "C", "qty": 2 }
  ]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 72 — Allocate warehouse stock to order lines FIFO**
> Folder: `student/labs/05-mapping/72-allocate-warehouse-stock-to-order-lines-fifo/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-72-allocate-warehouse-stock-to-order-lines-fifo-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload.order reduce ((line, acc = { stock: payload.stock groupBy $.sku, out: [] }) -> do {
  var have = (acc.stock[line.sku][0].onHand default 0) as Number
  var give = min([line.qty as Number, have])
  var rest = have - give
  ---
  {
    stock: acc.stock mapObject ((v, k) ->
      if ((k as String) == line.sku) { (k): [{ sku: line.sku, onHand: rest }] }
      else { (k): v }
    ),
    out: acc.out ++ [{ sku: line.sku, requested: line.qty as Number, allocated: give }]
  }
}).out
```

**SAY:** That should match Expected:

```
[
  { "sku": "A", "requested": 3, "allocated": 3 },
  { "sku": "A", "requested": 4, "allocated": 2 },
  { "sku": "C", "requested": 2, "allocated": 0 }
]
```

## Part 4 — Interview phrase and close

**SAY:**

Allocate min of remaining stock and qty. Reduce the on-hand map.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 73 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 72

Allocate warehouse stock to order lines FIFO

## Expected

```
[
  { "sku": "A", "requested": 3, "allocated": 3 },
  { "sku": "A", "requested": 4, "allocated": 2 },
  { "sku": "C", "requested": 2, "allocated": 0 }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
