# Lab 55 — maxBy and firstWith on a work queue

**Level:** industry  
**Section folder:** `04-industry`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** From a list of orders, return `{ richest, firstPaid }`. `richest` is the item with max `amount` (coerce Number). `firstPaid` is the first item whose status is `PAID` (any case). Import `dw::core::Arrays`.

**Input:**

```json
[
  { "id": "O1", "status": "NEW", "amount": "40" },
  { "id": "O2", "status": "paid", "amount": "15" },
  { "id": "O3", "status": "PAID", "amount": 90 }
]
```

**Expected:**

```json
{
  "richest": { "id": "O3", "status": "PAID", "amount": 90 },
  "firstPaid": { "id": "O2", "status": "paid", "amount": "15" }
}
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
