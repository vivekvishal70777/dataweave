# Lab 10 — Count line items in a composite payload

**Level:** easy  
**Section folder:** `01-fundamentals`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Return how many records are in `payload.records` (Salesforce Composite / bulk query shape).

**Input:**

```json
{
  "done": true,
  "records": [
    { "Id": "a1" },
    { "Id": "a2" },
    { "Id": "a3" }
  ]
}
```

**Expected:** `3`

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
