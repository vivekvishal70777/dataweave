# Lab 16 — Object keys to array of `{ key, value }`

**Level:** easy  
**Section folder:** `01-fundamentals`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Convert a config object `{ "timeout": 30, "retries": 3 }` to entries for logging or CSV.

**Input:**

```json
{ "timeout": 30, "retries": 3 }
```

**Expected:**

```json
[{ "key": "timeout", "value": 30 }, { "key": "retries", "value": 3 }]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
