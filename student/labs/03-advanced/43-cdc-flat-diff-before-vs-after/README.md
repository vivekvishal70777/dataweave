# Lab 43 — CDC flat diff (before vs after)

**Level:** hard  
**Section folder:** `03-advanced`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Compare `before` and `after` on the same payload. List `{ field, from, to }` for changed or missing keys. Platform event / Salesforce CDC style.

**Input:**

```json
{
  "before": { "status": "NEW", "amount": 10, "owner": "Asha" },
  "after": { "status": "PAID", "amount": 10, "paidAt": "2026-08-20" }
}
```

**Expected:** `status` and `owner`/`paidAt` appear as diffs; `amount` omitted.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
