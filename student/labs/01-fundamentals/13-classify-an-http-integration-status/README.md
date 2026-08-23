# Lab 13 — Classify an HTTP/integration status

**Level:** easy  
**Section folder:** `01-fundamentals`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** From `{ "httpStatus": 503 }`, return `"retry"` for 408/429/5xx, `"client"` for 4xx, `"ok"` for 2xx, else `"other"`. No Java ternary.

**Input:**

```json
{ "httpStatus": 503 }
```

**Expected:** `"retry"`

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
