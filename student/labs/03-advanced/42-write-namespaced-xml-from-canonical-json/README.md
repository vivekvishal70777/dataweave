# Lab 42 — Write namespaced XML from canonical JSON

**Level:** hard  
**Section folder:** `03-advanced`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Inverse of 41: JSON → `ord:PurchaseOrder` with line attributes. One root. MIME `application/xml`.

**Input:**

```json
{
  "orderId": "PO-1001",
  "currency": "INR",
  "lines": [
    { "sku": "SKU-A", "qty": 2, "unitPrice": 50.00 },
    { "sku": "SKU-B", "qty": 1, "unitPrice": 100.00 }
  ]
}
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
