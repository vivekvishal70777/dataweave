# Lab 22 — Pivot array to object keyed by Id

**Level:** moderate  
**Section folder:** `02-intermediate`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** `[{ "Id": "001xxA", "Name": "Acme" }]` → `{ "001xxA": "Acme" }` for O(1) lookup. Dynamic key **must** use parentheses.

**Input:**

```json
[
  { "Id": "001xxA", "Name": "Acme Corp" },
  { "Id": "001xxB", "Name": "Globex" }
]
```

**Expected:**

```json
{ "001xxA": "Acme Corp", "001xxB": "Globex" }
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
