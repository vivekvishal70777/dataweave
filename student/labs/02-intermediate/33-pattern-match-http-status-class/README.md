# Lab 33 — Pattern match HTTP status class

**Level:** moderate  
**Section folder:** `02-intermediate`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Map `code`: 2xx → `ok`, 4xx → `client`, 5xx → `server`, else `other`. Prefer `match` over a pile of ifs in interviews.

**Input:**

```json
{ "code": 404 }
```

**Expected:** `"client"`

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
