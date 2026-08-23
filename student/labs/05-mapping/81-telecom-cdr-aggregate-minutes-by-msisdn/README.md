# Lab 81 — Telecom CDR aggregate minutes by MSISDN

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Sum durationSec/60 floor per msisdn. Drop failed calls (status != OK).

**Input:**

```json
[
  { "msisdn": "91A", "durationSec": 90, "status": "OK" },
  { "msisdn": "91A", "durationSec": 30, "status": "FAIL" },
  { "msisdn": "91B", "durationSec": 120, "status": "ok" }
]
```

**Expected:**

```json
[
  { "msisdn": "91A", "minutes": 1 },
  { "msisdn": "91B", "minutes": 2 }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
