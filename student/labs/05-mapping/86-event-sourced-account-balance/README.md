# Lab 86 — Event-sourced account balance

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Apply events in order: credit add, debit subtract, hold subtract. Start 0. fun money. Final balance only plus last event id.

**Input:**

```json
{
  "events": [
    { "id": "e1", "type": "credit", "amt": "100" },
    { "id": "e2", "type": "debit", "amt": "30" },
    { "id": "e3", "type": "hold", "amt": "10.5" }
  ]
}
```

**Expected:**

```json
{
  "lastEvent": "e3",
  "balance": 59.50
}
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
