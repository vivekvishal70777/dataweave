# Lab 39 — Deep mask PII keys (`ssn`, `password`, `email`, `accessToken`)

**Level:** hard  
**Section folder:** `03-advanced`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Replace those keys with `"****"` at **any** nesting level before logging. Production follow-up: do not log the pre-mask payload.

**Input:**

```json
{
  "name": "Asha Rao",
  "email": "asha@acme.com",
  "address": { "ssn": "AAAAA1234A", "city": "Pune" },
  "auth": { "accessToken": "00Dxx...", "password": "x" }
}
```

**Expected:** secret fields `"****"`, `name` and `city` unchanged.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
