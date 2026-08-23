# Lab 65 — Debezium CDC envelope to flat upsert rows

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** c/u → UPSERT from after; d → DELETE from before. Include tsMs.

**Input:**

```json
{
  "changes": [
    { "op": "c", "ts_ms": 100, "before": null, "after": { "id": "A1", "status": "NEW" } },
    { "op": "u", "ts_ms": 101, "before": { "id": "A1", "status": "NEW" }, "after": { "id": "A1", "status": "PAID" } },
    { "op": "d", "ts_ms": 102, "before": { "id": "B9", "status": "X" }, "after": null }
  ]
}
```

**Expected:**

```json
[
  { "action": "UPSERT", "id": "A1", "status": "NEW", "tsMs": 100 },
  { "action": "UPSERT", "id": "A1", "status": "PAID", "tsMs": 101 },
  { "action": "DELETE", "id": "B9", "status": "X", "tsMs": 102 }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
