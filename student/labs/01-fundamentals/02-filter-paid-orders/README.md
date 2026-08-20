# Lab 02 — Filter paid orders

**Level:** easy  
**Section folder:** `01-fundamentals`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Keep only orders with `status == "PAID"`.

**Input:**

```json
[
  { "id": 1, "status": "PAID", "amount": 100 },
  { "id": 2, "status": "NEW", "amount": 50 },
  { "id": 3, "status": "PAID", "amount": 75 }
]
```

**Expected:** orders `1` and `3` only.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
