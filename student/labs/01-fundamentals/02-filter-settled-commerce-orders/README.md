# Lab 02 — Filter settled commerce orders

**Level:** easy  
**Section folder:** `01-fundamentals`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Keep orders where status is `PAID` or `SETTLED` (any case) **and** `amount` as Number is greater than 0. Drop cancelled/zero-value noise.

**Input:**

```json
[
  { "id": "ORD-1", "status": "paid", "amount": "100.00" },
  { "id": "ORD-2", "status": "NEW", "amount": "50" },
  { "id": "ORD-3", "status": "SETTLED", "amount": 75 },
  { "id": "ORD-4", "status": "PAID", "amount": 0 }
]
```

**Expected:**

```json
[
  { "id": "ORD-1", "status": "paid", "amount": "100.00" },
  { "id": "ORD-3", "status": "SETTLED", "amount": 75 }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
