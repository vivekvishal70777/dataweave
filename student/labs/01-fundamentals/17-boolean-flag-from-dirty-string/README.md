# Lab 17 — Boolean flag from dirty string

**Level:** easy  
**Section folder:** `01-fundamentals`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** `"Y"` / `"yes"` / `"true"` / `"1"` (any case) → `true`, else `false`. Common in SAP/legacy flags.

**Input:**

```json
{ "active": "Yes" }
```

**Expected:**

```json
{ "active": true }
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
