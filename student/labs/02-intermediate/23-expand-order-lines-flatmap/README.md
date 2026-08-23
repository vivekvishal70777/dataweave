# Lab 23 — Expand order lines (flatMap)

**Level:** moderate  
**Section folder:** `02-intermediate`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** One canonical row per line: `orderId`, `sku`, `qty`. Nested `items` must not remain nested arrays.

**Input:**

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

**Expected:**

```json
[
  { "orderId": "O-1001", "sku": "SKU-A", "qty": 2 },
  { "orderId": "O-1001", "sku": "SKU-B", "qty": 1 }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
