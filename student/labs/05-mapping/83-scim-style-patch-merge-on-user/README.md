# Lab 83 — SCIM-style patch merge on user

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Apply replace email and add phone. Reduce over ops starting from user.

**Input:**

```json
{
  "user": { "id": "U1", "email": "old@x.com", "phones": ["111"] },
  "ops": [
    { "op": "replace", "path": "email", "value": "new@x.com" },
    { "op": "add", "path": "phones", "value": "222" }
  ]
}
```

**Expected:**

```json
{
  "id": "U1",
  "email": "new@x.com",
  "phones": ["111", "222"]
}
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
