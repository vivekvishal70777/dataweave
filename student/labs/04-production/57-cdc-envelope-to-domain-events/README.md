# Lab 57 — CDC envelope to domain events

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Each change-data-capture row has `op` (`c` create, `u` update, `d` delete), `before`, `after`, and `ts`. Emit domain events. Deletes use `before` as `record`. Unknown `op` → skip (do not fail the batch).

**Input:**

```json
{
  "changes": [
    { "op": "c", "before": null, "after": { "id": "1", "name": "Asha" }, "ts": "2026-08-20T10:00:00Z" },
    { "op": "u", "before": { "id": "1", "name": "Asha" }, "after": { "id": "1", "name": "Asha R" }, "ts": "2026-08-20T11:00:00Z" },
    { "op": "d", "before": { "id": "2" }, "after": null, "ts": "2026-08-20T12:00:00Z" },
    { "op": "x", "before": null, "after": { "id": "9" }, "ts": "2026-08-20T13:00:00Z" }
  ]
}
```

**Expected:**

```json
[
  { "type": "created", "id": "1", "record": { "id": "1", "name": "Asha" }, "ts": "2026-08-20T10:00:00Z" },
  { "type": "updated", "id": "1", "record": { "id": "1", "name": "Asha R" }, "ts": "2026-08-20T11:00:00Z" },
  { "type": "deleted", "id": "2", "record": { "id": "2" }, "ts": "2026-08-20T12:00:00Z" }
]
```

**Interview talking point:** CDC mappings must be **idempotent** downstream (same event twice = same business result). Tombstones (`op=d`) still need a stable `id`.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
