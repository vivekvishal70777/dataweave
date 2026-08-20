# Lab 79 — Log-safe HTTP headers (redact secrets)

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Copy headers for logging. Keys `authorization`, `cookie`, `x-api-key` (any case) become `"****"`. Keep `x-correlation-id` as-is.

**Input:**

```json
{
  "headers": {
    "Authorization": "Bearer secret",
    "X-Correlation-Id": "corr-9",
    "Cookie": "sid=abc",
    "Accept": "application/json"
  }
}
```

**Expected:**

```json
{
  "Authorization": "****",
  "X-Correlation-Id": "corr-9",
  "Cookie": "****",
  "Accept": "application/json"
}
```

**Interview talking point:** Never log inbound HTTP before this map. Pair with Lab 39 (body PII). Correlation id is the one header you **must** keep.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
