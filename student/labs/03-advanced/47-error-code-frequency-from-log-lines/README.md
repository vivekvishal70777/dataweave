# Lab 47 — Error-code frequency from log lines

**Level:** hard  
**Section folder:** `03-advanced`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Count case-insensitive tokens in an ops log string (same skill as word frequency). Ignore empty pieces.

**Input:**

```text
TIMEOUT timeout 429 TIMEOUT mule
```

**Expected:** `{ "timeout": 3, "429": 1, "mule": 1 }` (key order may vary)

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
