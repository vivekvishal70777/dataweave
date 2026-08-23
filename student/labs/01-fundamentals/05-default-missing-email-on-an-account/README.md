# Lab 05 — Default missing email on an Account

**Level:** easy  
**Section folder:** `01-fundamentals`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** If `Email` is null or missing, use `"noreply@acme.invalid"`. Keep `Name`.

**Input:**

```json
{ "Name": "Sam Logistics" }
```

**Expected:**

```json
{ "Name": "Sam Logistics", "Email": "noreply@acme.invalid" }
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
