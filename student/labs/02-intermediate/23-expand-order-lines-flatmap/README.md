# Lab 23 — Expand order lines (flatMap)

**Level:** moderate  
**Section folder:** `02-intermediate`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** One row per line item with `orderId` and `sku`.

**Input:**

```json
[
  {
    "orderId": "O1",
    "items": [{ "sku": "A" }, { "sku": "B" }]
  }
]
```

**Expected:** `[{ "orderId": "O1", "sku": "A" }, { "orderId": "O1", "sku": "B" }]`

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
