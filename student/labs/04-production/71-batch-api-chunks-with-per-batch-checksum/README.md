# Lab 71 — Batch API chunks with per-batch checksum

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Split `records` into batches of `size`. Each batch: `batchId` (`B1`, `B2`, …), `count`, `ids`, `checksum` = sum of numeric `id`s.

**Input:**

```json
{
  "size": 2,
  "records": [
    { "id": 1 },
    { "id": 2 },
    { "id": 3 },
    { "id": 4 },
    { "id": 5 }
  ]
}
```

**Expected:**

```json
[
  { "batchId": "B1", "count": 2, "ids": [1, 2], "checksum": 3 },
  { "batchId": "B2", "count": 2, "ids": [3, 4], "checksum": 7 },
  { "batchId": "B3", "count": 1, "ids": [5], "checksum": 5 }
]
```

**Interview talking point:** Bulk HTTP/SFTP jobs need **stable batch ids** and a control total. `divideBy` is the Array helper; it materializes the list (streaming tradeoff).

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
