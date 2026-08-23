# Lab 69 — EDI-like PO JSON to procurement canonical

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Header po/vendor. Skip qty 0. needBy from yyyyMMdd to yyyy-MM-dd.

**Input:**

```json
{
  "BEG": { "po": "PO-77", "vendor": "V-9" },
  "PO1": [
    { "sku": "BOLT", "qty": "10", "aaa": "20260820" },
    { "sku": "NUT", "qty": "0", "aaa": "20260821" }
  ]
}
```

**Expected:**

```json
{
  "poNum": "PO-77",
  "vendor": "V-9",
  "lines": [
    { "sku": "BOLT", "qty": 10, "needBy": "2026-08-20" }
  ]
}
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
