# Lab 63 — Stripe charges enriched with customer

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Join charges to customers. Amount cents/100. Missing email unknown.

**Input:**

```json
{
  "customers": [
    { "id": "cus_1", "email": "a@x.com" }
  ],
  "charges": {
    "data": [
      { "id": "ch_1", "customer": "cus_1", "amount": 1999, "paid": true },
      { "id": "ch_2", "customer": "cus_missing", "amount": 500, "paid": false }
    ]
  }
}
```

**Expected:**

```json
[
  { "chargeId": "ch_1", "email": "a@x.com", "amount": 19.99, "paid": true },
  { "chargeId": "ch_2", "email": "unknown", "amount": 5.00, "paid": false }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
