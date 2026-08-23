# Lab 49 — Outer-join style merge of two lists by `id`

**Level:** hard  
**Section folder:** `03-advanced`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Union by `id`; fields from left and right, **right overwrites** on conflict (master-data merge).

**Input:**

```json
{
  "left": [{ "id": "1", "a": 1, "name": "old" }],
  "right": [{ "id": "1", "b": 2, "name": "new" }, { "id": "2", "b": 3 }]
}
```

**Expected:** id `1` has `a`, `b`, `name=new`; id `2` from right only.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
