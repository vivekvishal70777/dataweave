# Lab 25 — Merge config overlay (right wins)

**Level:** moderate  
**Section folder:** `02-intermediate`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Shallow-merge `base` with `overlay`. Right-hand keys win. Both objects live on **payload** so this runs in the Playground (no Mule `vars` required).

**Input:**

```json
{
  "base": { "timeout": 30, "retries": 2, "region": "us-east-1" },
  "overlay": { "retries": 5, "region": "ap-south-1" }
}
```

**Expected:**

```json
{ "timeout": 30, "retries": 5, "region": "ap-south-1" }
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
