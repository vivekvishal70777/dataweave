# Lab 67 — Multi-currency lines to USD using FX table

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** usd = amount / perUsd. Skip unknown currency. fun money.

**Input:**

```json
{
  "fx": [
    { "ccy": "USD", "perUsd": 1 },
    { "ccy": "INR", "perUsd": 83 },
    { "ccy": "EUR", "perUsd": 0.92 }
  ],
  "lines": [
    { "id": "L1", "amount": "8300", "currency": "INR" },
    { "id": "L2", "amount": "10", "currency": "USD" },
    { "id": "L3", "amount": "9.2", "currency": "EUR" },
    { "id": "L4", "amount": "1", "currency": "JPY" }
  ]
}
```

**Expected:**

```json
{
  "lines": [
    { "id": "L1", "usd": 100.00 },
    { "id": "L2", "usd": 10.00 },
    { "id": "L3", "usd": 10.00 }
  ],
  "totalUsd": 120.00
}
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
