# Lab 80 — SLA overdue flags (injected clock)

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** For each open ticket, if `dueAt` < `now` then `OVERDUE`, else `ON_TRACK`. Closed tickets stay `CLOSED`. Use `payload.now` (do not call `now()`).

**Input:**

```json
{
  "now": "2026-08-20T12:00:00Z",
  "tickets": [
    { "id": "T1", "status": "OPEN", "dueAt": "2026-08-20T11:00:00Z" },
    { "id": "T2", "status": "OPEN", "dueAt": "2026-08-20T13:00:00Z" },
    { "id": "T3", "status": "CLOSED", "dueAt": "2026-08-19T00:00:00Z" }
  ]
}
```

**Expected:**

```json
[
  { "id": "T1", "sla": "OVERDUE" },
  { "id": "T2", "sla": "ON_TRACK" },
  { "id": "T3", "sla": "CLOSED" }
]
```

**Interview talking point:** Clocks are **inputs** so MUnit stays deterministic. Compare `DateTime`, not strings, if formats vary.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
