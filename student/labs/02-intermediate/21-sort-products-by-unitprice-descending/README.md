# Lab 21 — Sort products by unitPrice descending

**Level:** moderate  
**Section folder:** `02-intermediate`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Highest price first (catalog / pricing API).

**Input:**

```json
[
  { "sku": "SKU-A", "unitPrice": 30 },
  { "sku": "SKU-B", "unitPrice": 90 },
  { "sku": "SKU-C", "unitPrice": 90 }
]
```

**Expected:** SKU-B and SKU-C before SKU-A (equal prices keep relative order).

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
