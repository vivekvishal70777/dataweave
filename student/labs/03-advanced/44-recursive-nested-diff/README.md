# Lab 44 — Recursive nested diff

**Level:** hard  
**Section folder:** `03-advanced`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Return a nested object of **only** differences. Unchanged subtrees omitted. Use `payload.before` / `payload.after`.

**Input:**

```json
{
  "before": { "a": 1, "nested": { "x": 1, "y": 2 } },
  "after": { "a": 1, "nested": { "x": 1, "y": 9 } }
}
```

**Expected:** `{ "nested": { "y": { "from": 2, "to": 9 } } }` (shape may wrap `from`/`to`).

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
