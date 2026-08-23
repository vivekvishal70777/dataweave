# Lab 75 — Appointment slots to IST display with duration

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Parse start/end ISO. Shift both to Asia/Kolkata. durationMinutes from period. Inject times — no now().

**Input:**

```json
{
  "id": "APT-1",
  "start": "2026-08-20T03:30:00Z",
  "end": "2026-08-20T04:00:00Z"
}
```

**Expected:**

```json
{
  "id": "APT-1",
  "startIst": "20-Aug-2026 09:00",
  "endIst": "20-Aug-2026 09:30",
  "durationMinutes": 30
}
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
