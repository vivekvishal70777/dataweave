# Lab 72 — Store-local business date from UTC plus offset hours

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Convert each UTC timestamp to a **business date** using a fixed offset (`offsetHours`, e.g. IST = 5.5 → use `5` here for integer hours, or pass `offsetHours`: 5). Add `offsetHours * 3600` seconds, then take `yyyy-MM-dd`. Do not call `now()`.

**Input:**

```json
{
  "offsetHours": 5,
  "events": [
    { "id": "1", "utc": "2026-08-20T20:00:00Z" },
    { "id": "2", "utc": "2026-08-20T18:00:00Z" }
  ]
}
```

**Expected:**

```json
[
  { "id": "1", "utc": "2026-08-20T20:00:00Z", "businessDate": "2026-08-21" },
  { "id": "2", "utc": "2026-08-20T18:00:00Z", "businessDate": "2026-08-20" }
]
```

**Interview talking point:** Offsets are a teaching stand-in. Production uses IANA zones and DST (`dw::core::Dates` / Java time). Never mix store-local “business date” with UTC `createdAt` without a written rule.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
