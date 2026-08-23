# Lab 03 — Sum invoice line amounts (string money)

**Level:** easy  
**Section folder:** `01-fundamentals`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Return the numeric total of `amount` on each line. Incoming amounts are **strings** (typical ERP/CSV). Coerce, then `sum`.

**Input:**

```json
[
  { "sku": "SKU-A", "amount": "10.50" },
  { "sku": "SKU-B", "amount": "20" },
  { "sku": "SKU-C", "amount": "30.25" }
]
```

**Expected:** `60.75`

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
