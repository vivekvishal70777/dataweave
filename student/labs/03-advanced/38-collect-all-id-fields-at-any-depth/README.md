# Lab 38 — Collect all `id` fields at any depth

**Level:** hard  
**Section folder:** `03-advanced`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Return every `id` in a nested integration payload. Descendant `payload..id` is acceptable; be ready to recurse if the interviewer forbids `..`.

**Input:**

```json
{
  "id": "root",
  "child": { "id": "c1", "items": [{ "id": "i1" }, { "sku": "x" }] }
}
```

**Expected:** `["root", "c1", "i1"]` (walk order may vary)

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
