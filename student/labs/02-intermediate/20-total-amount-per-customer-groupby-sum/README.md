# Lab 20 — Total amount per customer (groupBy + sum)

**Level:** moderate  
**Section folder:** `02-intermediate`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Return `{ customerId, orderCount, total }` per customer. Coerce amounts. This is the standard interview follow-up to `groupBy`.

**Input:**

```json
[
  { "id": "ORD-1", "customerId": "C1", "amount": "10.00" },
  { "id": "ORD-2", "customerId": "C2", "amount": "20" },
  { "id": "ORD-3", "customerId": "C1", "amount": 15 }
]
```

**Expected:**

```json
[
  { "customerId": "C1", "orderCount": 2, "total": 25.00 },
  { "customerId": "C2", "orderCount": 1, "total": 20 }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
