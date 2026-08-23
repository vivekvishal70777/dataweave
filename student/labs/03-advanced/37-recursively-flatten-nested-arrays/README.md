# Lab 37 — Recursively flatten nested arrays

**Level:** hard  
**Section folder:** `03-advanced`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Deep-flatten mixed arrays to a single list of leaves. One `flatten` is **not** enough.

**Input:**

```json
[1, [2, [3, 4], 5], 6]
```

**Expected:** `[1, 2, 3, 4, 5, 6]`

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
