# Lab 72 — Allocate warehouse stock to order lines FIFO

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** For each order line, allocated = min(qty, stock for sku). leftover stock is not required. Unmatched sku allocated 0.

**Input:**

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

**Expected:**

```json
[
  { "sku": "A", "requested": 3, "allocated": 3 },
  { "sku": "A", "requested": 4, "allocated": 2 },
  { "sku": "C", "requested": 2, "allocated": 0 }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
