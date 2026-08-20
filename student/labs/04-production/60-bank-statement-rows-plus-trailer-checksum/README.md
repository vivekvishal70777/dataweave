# Lab 60 — Bank statement rows plus trailer checksum

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** `rows` are transactions; the last object with `type == "TRAILER"` holds `total`. Sum `amount` of non-trailer rows. Return `{ total, expected, balanced, items }`.

**Input:**

```json
{
  "rows": [
    { "type": "TXN", "id": "1", "amount": 10.5 },
    { "type": "TXN", "id": "2", "amount": 4.5 },
    { "type": "TRAILER", "total": 15 }
  ]
}
```

**Expected:**

```json
{
  "items": [
    { "id": "1", "amount": 10.5 },
    { "id": "2", "amount": 4.5 }
  ],
  "total": 15,
  "expected": 15,
  "balanced": true
}
```

**Interview talking point:** File-based banking/EDI often has **control totals**. Fail the flow (or route to ops) when `balanced` is false; do not post partial ledgers.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
