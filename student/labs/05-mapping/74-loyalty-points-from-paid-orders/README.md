# Lab 74 — Loyalty points from paid orders

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** 1 point per whole INR of paid amount. status PAID/SETTLED any case. Sum points per customerId.

**Input:**

```json
[
  { "customerId": "C1", "status": "paid", "amount": "199.9" },
  { "customerId": "C1", "status": "NEW", "amount": "50" },
  { "customerId": "C2", "status": "SETTLED", "amount": "10.1" }
]
```

**Expected:**

```json
[
  { "customerId": "C1", "points": 199 },
  { "customerId": "C2", "points": 10 }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
