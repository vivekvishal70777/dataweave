# Lab 04 — Uppercase string fields on an address object

**Level:** easy  
**Section folder:** `01-fundamentals`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Uppercase every **string** value; leave numbers as-is. Production addresses mix `city` and `postalCode`.

**Input:**

```json
{ "city": "pune", "country": "india", "postalCode": 411001 }
```

**Expected:**

```json
{ "city": "PUNE", "country": "INDIA", "postalCode": 411001 }
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
