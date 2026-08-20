# Lab 61 — Pagination envelope for a list API

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Page `page` (1-based) of `size` over `items`. Return the window plus `total`, `hasMore`, and `nextPage` (`null` if none).

**Input:**

```json
{
  "page": 2,
  "size": 2,
  "items": [1, 2, 3, 4, 5]
}
```

**Expected:**

```json
{
  "items": [3, 4],
  "page": 2,
  "size": 2,
  "total": 5,
  "hasMore": true,
  "nextPage": 3
}
```

**Interview talking point:** `drop`/`take` **materialize** the array. For huge files, paginate at the **connector** (DB `LIMIT`, S3 list), not in DataWeave.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
