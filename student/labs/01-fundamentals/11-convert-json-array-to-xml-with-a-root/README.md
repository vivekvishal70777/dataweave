# Lab 11 — Convert JSON array to XML with a root

**Level:** easy  
**Section folder:** `01-fundamentals`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Wrap users as XML `users/user`.

**Input:** `[{ "id": 1, "name": "Asha" }, { "id": 2, "name": "Ben" }]`

**Solution:** Hidden until you try it. See `instructor/solutions`.

**Expected (shape):**

```xml
<users>
  <user><id>1</id><name>Asha</name></user>
  <user><id>2</id><name>Ben</name></user>
</users>
```

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
