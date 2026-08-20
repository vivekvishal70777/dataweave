# Lab 68 — SOAP-like envelope: success vs fault

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** If `Envelope.Body.Fault` exists, return `{ ok: false, code, message }`. Else unwrap `Envelope.Body` as `{ ok: true, data }` (the body without `Fault`).

**Input:**

```json
{
  "Envelope": {
    "Body": {
      "Fault": {
        "faultcode": "soap:Server",
        "faultstring": "credit check failed"
      }
    }
  }
}
```

**Expected:**

```json
{
  "ok": false,
  "code": "soap:Server",
  "message": "credit check failed"
}
```

**Interview talking point:** Always branch on **fault vs body** before mapping the happy path. In Mule, that often becomes a Choice router after a small DW expression — keep the script obvious.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
