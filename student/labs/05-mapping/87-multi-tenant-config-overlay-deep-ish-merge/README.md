# Lab 87 — Multi-tenant config overlay (deep-ish merge)

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Start from base. Overlay tenant object with ++ (right wins). Concat arrays for `plugins` only if both are arrays — interview: document ++ is shallow. Here: merge plugins with distinctBy.

**Input:**

```json
{
  "base": { "timeout": 30, "plugins": ["auth"], "theme": "light" },
  "tenant": { "timeout": 10, "plugins": ["audit"], "region": "IN" }
}
```

**Expected:**

```json
{
  "timeout": 10,
  "plugins": ["auth", "audit"],
  "theme": "light",
  "region": "IN"
}
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
