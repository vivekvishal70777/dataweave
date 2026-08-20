# Lab 54 — Invoice: compute line totals, tax, and grand total

**Level:** hard  
**Section folder:** `03-advanced`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Input:**

```json
{
  "taxRate": 0.18,
  "lines": [
    { "sku": "A", "qty": 2, "price": 50 },
    { "sku": "B", "qty": 1, "price": 100 }
  ]
}
```

**Expected:** each line has `lineTotal`; document has `subtotal` `200`, `tax` `36`, `grandTotal` `236`.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
