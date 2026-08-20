# Lab 82 — Heterogeneous payments to a canonical charge

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** `method` is `card`, `upi`, or `netbanking`. Map to `{ method, instrument, ref }`. Unknown method → `{ method: "other", instrument: null, ref: null }` (do not fail the batch).

**Input:**

```json
{
  "payments": [
    { "method": "card", "last4": "4242", "authCode": "A1" },
    { "method": "upi", "vpa": "asha@upi", "txnId": "U9" },
    { "method": "netbanking", "bank": "HDFC", "refNo": "N3" },
    { "method": "wallet", "id": "w1" }
  ]
}
```

**Expected:**

```json
[
  { "method": "card", "instrument": "4242", "ref": "A1" },
  { "method": "upi", "instrument": "asha@upi", "ref": "U9" },
  { "method": "netbanking", "instrument": "HDFC", "ref": "N3" },
  { "method": "other", "instrument": null, "ref": null }
]
```

**Interview talking point:** PSP webhooks are **union types**. `match` on `method` (or `type`) is the production pattern — not a pile of `if` with missing `else`.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
