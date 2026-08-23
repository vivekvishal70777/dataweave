# Lab 77 — RMA restock vs refund split

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** reason DAMAGED → refund only (restock false). Else restock true. Amount = qty * unit. fun money.

**Input:**

```json
[
  { "rma": "R1", "reason": "DAMAGED", "qty": "2", "unit": "10.00" },
  { "rma": "R2", "reason": "SIZE", "qty": 1, "unit": "15.5" }
]
```

**Expected:**

```json
[
  { "rma": "R1", "restock": false, "refund": 20.00 },
  { "rma": "R2", "restock": true, "refund": 15.50 }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
