# Lab 62 — Idempotency key from a natural key

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Build `idempotencyKey` = `customerId` + `|` + `externalOrderId` + `|` + sorted unique line `sku`s joined by `,`. Production APIs send this as `Idempotency-Key` or store it for upserts.

**Input:**

```json
{
  "customerId": "C1",
  "externalOrderId": "EXT-9",
  "lines": [
    { "sku": "B" },
    { "sku": "A" },
    { "sku": "B" }
  ]
}
```

**Expected:** `"C1|EXT-9|A,B"`

**Interview talking point:** Keys must be **stable** if the client retries with the same business document (sort, distinct). Do not include `now()` or random UUIDs in the key.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
