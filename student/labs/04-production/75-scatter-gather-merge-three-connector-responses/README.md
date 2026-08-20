# Lab 75 — Scatter-gather: merge three connector responses

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** `responses` is what a Scatter-Gather (or parallel HTTP) returns. Status `200–299` → put `body` under `ok[name]`. Anything else → `errors[]`. Do not drop successes because one leg failed.

**Input:**

```json
{
  "responses": [
    { "name": "crm", "status": 200, "body": { "id": "C1" } },
    { "name": "erp", "status": 500, "body": { "error": "down" } },
    { "name": "mdm", "status": 200, "body": { "id": "M1" } }
  ]
}
```

**Expected:**

```json
{
  "ok": {
    "crm": { "id": "C1" },
    "mdm": { "id": "M1" }
  },
  "errors": [
    { "name": "erp", "status": 500, "body": { "error": "down" } }
  ]
}
```

**Interview talking point:** HTTP 207 / partial aggregation is the integration default. Map **per leg**, then decide in Choice whether the flow can continue.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
