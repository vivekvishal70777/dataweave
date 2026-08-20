# Lab 77 — Keep latest version per id (upsert projection)

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Event log of `{ id, version, payload }`. Keep the row with the **highest** `version` per `id`. If versions tie, keep the last in array order.

**Input:**

```json
[
  { "id": "A", "version": 1, "payload": { "name": "old" } },
  { "id": "B", "version": 1, "payload": { "name": "b" } },
  { "id": "A", "version": 3, "payload": { "name": "new" } },
  { "id": "A", "version": 2, "payload": { "name": "mid" } }
]
```

**Expected:**

```json
[
  { "id": "A", "version": 3, "payload": { "name": "new" } },
  { "id": "B", "version": 1, "payload": { "name": "b" } }
]
```

**Interview talking point:** This is an **in-memory projection**. True source of truth is the event store; DataWeave only shapes the current snapshot for a target API.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
