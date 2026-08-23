# Lab 62 — Shopify order to ERP sales order

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Map line_items; skip SKU GIFT. Money strings. soldTo = last then first. channel WEB.

**Input:**

```json
{
  "id": 991,
  "currency": "USD",
  "shipping_address": { "first_name": "Sam", "last_name": "Patel" },
  "line_items": [
    { "sku": "TEE-M", "quantity": 2, "price": "19.99" },
    { "sku": "GIFT", "quantity": 1, "price": "25.00" },
    { "sku": "HAT", "quantity": 1, "price": "12.5" }
  ]
}
```

**Expected:**

```json
{
  "erpOrderId": "991",
  "currency": "USD",
  "channel": "WEB",
  "soldTo": "Patel Sam",
  "lines": [
    { "sku": "TEE-M", "qty": 2, "unitPrice": 19.99 },
    { "sku": "HAT", "qty": 1, "unitPrice": 12.50 }
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
