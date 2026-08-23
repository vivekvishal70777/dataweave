# Lab 19 — Group orders by customerId

**Level:** moderate  
**Section folder:** `02-intermediate`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Group the commerce array by `customerId`. `groupBy` returns an **object** of arrays — say that in interviews.

**Input:**

```json
[
  { "id": "ORD-1", "customerId": "C1", "amount": 10 },
  { "id": "ORD-2", "customerId": "C2", "amount": 20 },
  { "id": "ORD-3", "customerId": "C1", "amount": 15 }
]
```

**Expected:**

```json
{
  "C1": [
    { "id": "ORD-1", "customerId": "C1", "amount": 10 },
    { "id": "ORD-3", "customerId": "C1", "amount": 15 }
  ],
  "C2": [
    { "id": "ORD-2", "customerId": "C2", "amount": 20 }
  ]
}
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
