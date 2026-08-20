# Lab 66 — Tenant config overlay (defaults < tenant < request)

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Deep-merge objects with precedence **request > tenant > defaults**. For `featureFlags` (array of strings), **replace** the whole array from the highest source that provided it (do not concatenate). Scalars: first non-null from request, then tenant, then defaults.

**Input:**

```json
{
  "defaults": {
    "timeoutMs": 3000,
    "region": "us",
    "featureFlags": ["a"],
    "retry": { "max": 2, "backoffMs": 100 }
  },
  "tenant": {
    "region": "in",
    "featureFlags": ["b", "c"],
    "retry": { "max": 4 }
  },
  "request": {
    "timeoutMs": 9000,
    "retry": { "backoffMs": 250 }
  }
}
```

**Expected:**

```json
{
  "timeoutMs": 9000,
  "region": "in",
  "featureFlags": ["b", "c"],
  "retry": { "max": 4, "backoffMs": 250 }
}
```

**Interview talking point:** Config overlays need a **documented merge algebra**. Blind `++` is shallow; array concat silently duplicates flags.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
