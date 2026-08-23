# Lab 15 — Flatten one level of nested arrays

**Level:** easy  
**Section folder:** `01-fundamentals`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Flatten one level only: `[[1, 2], [3], [4, 5]]` → `[1, 2, 3, 4, 5]`. Deeper trees are a later lab.

**Input:**

```json
[[1, 2], [3], [4, 5]]
```

**Expected:** `[1, 2, 3, 4, 5]`

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
