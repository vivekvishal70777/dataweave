# Lab 45 — Chunk array into batches of N (Salesforce Composite / bulk)

**Level:** hard  
**Section folder:** `03-advanced`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Split work into batches of 2 for a bulk API that caps records per call.

**Input:**

```json
[1, 2, 3, 4, 5]
```

**Expected:** `[[1, 2], [3, 4], [5]]`

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
