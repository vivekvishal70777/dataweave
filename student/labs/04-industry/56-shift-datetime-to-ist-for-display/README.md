# Lab 56 — Shift DateTime to IST for display

**Level:** industry  
**Section folder:** `04-industry`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Canonical APIs store UTC. Output `occurredAtIst` as `dd-MMM-yyyy HH:mm` in `Asia/Kolkata`. Do not use `now()`.

**Input:**

```json
{ "occurredAt": "2026-08-20T14:05:00Z" }
```

**Expected:** IST is UTC+5:30 → `20-Aug-2026 19:35`

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
