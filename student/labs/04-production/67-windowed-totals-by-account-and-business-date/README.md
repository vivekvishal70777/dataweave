# Lab 67 — Windowed totals by account and business date

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Group payments by `accountId` and calendar date of `ts` (`yyyy-MM-dd` prefix). Sum `amount`. Sort output by account then date.

**Input:**

```json
{
  "payments": [
    { "accountId": "A1", "ts": "2026-08-20T10:00:00Z", "amount": 10 },
    { "accountId": "A1", "ts": "2026-08-20T18:00:00Z", "amount": 5 },
    { "accountId": "A2", "ts": "2026-08-21T01:00:00Z", "amount": 7 },
    { "accountId": "A1", "ts": "2026-08-21T00:00:00Z", "amount": 1 }
  ]
}
```

**Expected:**

```json
[
  { "accountId": "A1", "date": "2026-08-20", "total": 15 },
  { "accountId": "A1", "date": "2026-08-21", "total": 1 },
  { "accountId": "A2", "date": "2026-08-21", "total": 7 }
]
```

**Interview talking point:** “Business date” is a **timezone policy**, not `now()`. Here we take the UTC date prefix; production often converts to a store timezone first (see Lab 72).

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
