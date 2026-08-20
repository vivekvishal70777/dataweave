# Lab 81 — Dead-letter / replay envelope

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Wrap a failed record for a DLQ or object store: `replayKey` (stable), `failedAt` from injected `now`, `errorType`, and `original` (the record only).

**Input:**

```json
{
  "now": "2026-08-20T08:00:00Z",
  "errorType": "HTTP:CONNECTIVITY",
  "record": { "orderId": "O-1", "customerId": "C1" }
}
```

**Expected:**

```json
{
  "replayKey": "C1|O-1",
  "failedAt": "2026-08-20T08:00:00Z",
  "errorType": "HTTP:CONNECTIVITY",
  "original": { "orderId": "O-1", "customerId": "C1" }
}
```

**Interview talking point:** Replay keys must match Lab 62 (idempotency). Store the **canonical** original, not the raw connector error HTML.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
