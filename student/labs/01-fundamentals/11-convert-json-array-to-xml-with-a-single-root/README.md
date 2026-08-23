# Lab 11 — Convert JSON array to XML with a single root

**Level:** easy  
**Section folder:** `01-fundamentals`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Wrap users as XML `users/user`. XML **must** have one root. Set MIME `application/xml`.

**Input:**

```json
[{ "id": "U-1", "name": "Asha Rao" }, { "id": "U-2", "name": "Ben Cole" }]
```

**Expected:**

```xml
<users>
  <user>
    <id>U-1</id>
    <name>Asha Rao</name>
  </user>
  <user>
    <id>U-2</id>
    <name>Ben Cole</name>
  </user>
</users>
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
