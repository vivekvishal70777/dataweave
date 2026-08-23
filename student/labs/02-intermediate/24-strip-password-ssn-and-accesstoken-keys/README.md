# Lab 24 — Strip password, ssn, and accessToken keys

**Level:** moderate  
**Section folder:** `02-intermediate`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Drop secret keys from a flat object before logging. Keys compared as strings.

**Input:**

```json
{
  "name": "Asha Rao",
  "password": "s3cret",
  "ssn": "AAAAA1234A",
  "accessToken": "00Dxx...",
  "city": "Pune"
}
```

**Expected:**

```json
{ "name": "Asha Rao", "city": "Pune" }
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
