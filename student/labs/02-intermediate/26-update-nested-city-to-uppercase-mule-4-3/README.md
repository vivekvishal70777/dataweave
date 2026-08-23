# Lab 26 — Update nested city to uppercase (Mule 4.3+)

**Level:** moderate  
**Section folder:** `02-intermediate`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Uppercase `customer.address.city` without rebuilding the whole tree by hand.

**Input:**

```json
{ "customer": { "id": "C-9", "address": { "city": "pune", "postalCode": "411001" } } }
```

**Expected:** city `"PUNE"`, other fields unchanged.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
