# Lab 64 — Nested GraphQL-style order to line rows

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Flatten `order.lines` into reporting rows: `orderId`, `customer`, `sku`, `qty`. Drop lines with `qty <= 0`.

**Input:**

```json
{
  "order": {
    "id": "O-1",
    "customer": "Asha",
    "lines": [
      { "sku": "A", "qty": 2 },
      { "sku": "B", "qty": 0 },
      { "sku": "C", "qty": 5 }
    ]
  }
}
```

**Expected:**

```json
[
  { "orderId": "O-1", "customer": "Asha", "sku": "A", "qty": 2 },
  { "orderId": "O-1", "customer": "Asha", "sku": "C", "qty": 5 }
]
```

**Interview talking point:** Same pattern as exploding SOAP/XML line items: **`flatMap` / `map` + filter**. Analytics feeds want a **grain** (one row = one line), not nested documents.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
