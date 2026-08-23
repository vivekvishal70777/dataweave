# Lab 27 — Parse mixed date formats (ISO or dd/MM/yyyy)

**Level:** moderate  
**Section folder:** `02-intermediate`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Accept `yyyy-MM-dd` or `dd/MM/yyyy`. Invalid → `null`. Do **not** use `default` for failed `as Date` (that is `try`).

**Input:**

```json
[
  { "id": "E-1", "date": "2026-08-20" },
  { "id": "E-2", "date": "21/08/2026" },
  { "id": "E-3", "date": "not-a-date" }
]
```

**Expected:** first two parse to dates; third `date` is `null`.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
