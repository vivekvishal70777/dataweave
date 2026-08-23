# Lab 76 — BOM explode one level to pick list

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Each finished SKU has components. Explode order lines to component qty = parent qty * per. Skip unknown BOM.

**Input:**

```json
{
  "bom": [
    { "parent": "BIKE", "component": "FRAME", "per": 1 },
    { "parent": "BIKE", "component": "WHEEL", "per": 2 }
  ],
  "orders": [
    { "sku": "BIKE", "qty": 3 },
    { "sku": "UNK", "qty": 1 }
  ]
}
```

**Expected:**

```json
[
  { "component": "FRAME", "qty": 3 },
  { "component": "WHEEL", "qty": 6 }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
