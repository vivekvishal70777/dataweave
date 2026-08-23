# Lab 54 — Production invoice: discounts, tax, skip zero qty

**Level:** hard  
**Section folder:** `03-advanced`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Drop lines with `qty` ≤ 0. `lineTotal = qty * price * (1 - discountPct)` rounded to 2 decimals. `subtotal` = sum of line totals. `tax` = subtotal × `taxRate`. `grandTotal` = subtotal + tax. Header `var` / `fun money`.

**Input:**

```json
{
  "taxRate": 0.18,
  "currency": "INR",
  "lines": [
    { "sku": "SKU-A", "qty": 2, "price": 50, "discountPct": 0.10 },
    { "sku": "SKU-B", "qty": 1, "price": 100, "discountPct": 0 },
    { "sku": "SKU-Z", "qty": 0, "price": 999, "discountPct": 0 }
  ]
}
```

**Expected:** SKU-Z omitted; SKU-A `lineTotal` 90.00; SKU-B 100.00; `subtotal` 190.00; `tax` 34.20; `grandTotal` 224.20.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
