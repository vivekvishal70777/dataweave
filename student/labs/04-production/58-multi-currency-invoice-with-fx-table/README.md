# Lab 58 — Multi-currency invoice with FX table

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Convert each line to USD using `rates` (units of USD per 1 unit of `currency`). If a rate is missing, the line is an error and excluded from `totalUsd`.

**Input:**

```json
{
  "rates": { "USD": 1, "EUR": 1.1 },
  "lines": [
    { "sku": "A", "amount": 100, "currency": "EUR" },
    { "sku": "B", "amount": 50, "currency": "USD" },
    { "sku": "C", "amount": 20, "currency": "GBP" }
  ]
}
```

**Expected:**

```json
{
  "lines": [
    { "sku": "A", "amount": 100, "currency": "EUR", "amountUsd": 110 },
    { "sku": "B", "amount": 50, "currency": "USD", "amountUsd": 50 }
  ],
  "totalUsd": 160,
  "errors": [
    { "sku": "C", "reason": "missing FX rate for GBP" }
  ]
}
```

**Interview talking point:** FX belongs in a **table** (Object keyed by currency), not an HTTP `lookup` per line. Pin the rate timestamp in production (not shown here).

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
