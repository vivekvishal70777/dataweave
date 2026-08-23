# Lab 30 — JSON to CSV for finance export

**Level:** moderate  
**Section folder:** `02-intermediate`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Write `orderId,customerId,amount` CSV with header. MIME `application/csv`.

**Input:**

```json
[
  { "orderId": "O-1", "customerId": "C1", "amount": 100.5 },
  { "orderId": "O-2", "customerId": "C2", "amount": 40 }
]
```

**Expected:** CSV with header row `orderId,customerId,amount`.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
