# Lab 36 — Dynamic object keys from header pairs

**Level:** moderate  
**Section folder:** `02-intermediate`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** HTTP/query pairs `[{ "k": "X-Request-Id", "v": "abc" }]` → object. Parentheses around the key expression.

**Input:**

```json
[
  { "k": "X-Request-Id", "v": "abc-123" },
  { "k": "X-Correlation-Id", "v": "corr-9" }
]
```

**Expected:**

```json
{ "X-Request-Id": "abc-123", "X-Correlation-Id": "corr-9" }
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
