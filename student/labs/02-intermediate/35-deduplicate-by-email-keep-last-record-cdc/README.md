# Lab 35 — Deduplicate by email, keep last record (CDC)

**Level:** moderate  
**Section folder:** `02-intermediate`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** `distinctBy` keeps **first**. For last-wins upsert, reduce into an object keyed by email, then `valuesOf`.

**Input:**

```json
[
  { "email": "a@acme.com", "name": "Old" },
  { "email": "b@acme.com", "name": "Bee" },
  { "email": "a@acme.com", "name": "New" }
]
```

**Expected:** New Asha-row for `a@acme.com`, plus Bee.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
