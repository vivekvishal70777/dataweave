# Lab 58 — Simulate Transform Message payload + vars

**Level:** industry  
**Section folder:** `04-industry`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** One script returns **two targets** as an object (Playground cannot set Mule vars). `payload` = `{ orderId, amount }` with amount as Number. `vars` = `{ correlationId, recordCount }`. `correlationId` from `payload.headers.xCorrelationId` default `"missing"`.

**Input:**

```json
{
  "headers": { "xCorrelationId": "corr-9" },
  "order": { "id": "O-1", "amount": "42.00" }
}
```

**Expected:**

```json
{
  "payload": { "orderId": "O-1", "amount": 42.00 },
  "vars": { "correlationId": "corr-9", "recordCount": 1 }
}
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
