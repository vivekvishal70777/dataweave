# Lab 19 — Group orders by customer

**Level:** moderate  
**Section folder:** `02-intermediate`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Group the array by `customerId`.

**Input:**

```json
[
  { "id": 1, "customerId": "C1", "amount": 10 },
  { "id": 2, "customerId": "C2", "amount": 20 },
  { "id": 3, "customerId": "C1", "amount": 15 }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

**Expected keys:** `C1` → orders 1 and 3; `C2` → order 2.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
