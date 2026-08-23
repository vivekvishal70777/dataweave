# Lab 66 — Product variants color times size SKUs

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Cartesian colors x sizes. Skip discontinued colors. SKU base-color-size.

**Input:**

```json
{
  "base": "TEE",
  "colors": [
    { "code": "BLK", "discontinued": false },
    { "code": "RED", "discontinued": true },
    { "code": "WHT", "discontinued": false }
  ],
  "sizes": ["S", "M"]
}
```

**Expected:**

```json
[
  { "sku": "TEE-BLK-S" },
  { "sku": "TEE-BLK-M" },
  { "sku": "TEE-WHT-S" },
  { "sku": "TEE-WHT-M" }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
