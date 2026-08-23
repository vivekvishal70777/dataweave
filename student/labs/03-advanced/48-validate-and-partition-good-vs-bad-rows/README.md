# Lab 48 — Validate and partition good vs bad rows

**Level:** hard  
**Section folder:** `03-advanced`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Valid if `email` contains `"@"` and `age` as Number `>= 18`. Return `{ valid, invalid }`. Coercion failures are invalid (`try`).

**Input:**

```json
[
  { "email": "a@acme.com", "age": 20 },
  { "email": "bad", "age": 17 },
  { "email": "b@acme.com", "age": "x" }
]
```

**Expected:** one valid, two invalid.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
