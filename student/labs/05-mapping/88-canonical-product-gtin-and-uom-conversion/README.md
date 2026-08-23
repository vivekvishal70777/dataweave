# Lab 88 — Canonical product GTIN and UoM conversion

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** qty in EA. If uom CS, multiply qty by packSize. gtin from first barcode type EAN13. Skip items without GTIN.

**Input:**

```json
{
  "items": [
    { "sku": "S1", "qty": 2, "uom": "CS", "packSize": 10, "barcodes": [{ "type": "UPC", "id": "x" }, { "type": "EAN13", "id": "8901234567890" }] },
    { "sku": "S2", "qty": 3, "uom": "EA", "packSize": 1, "barcodes": [{ "type": "EAN13", "id": "8900000000001" }] },
    { "sku": "S3", "qty": 1, "uom": "EA", "barcodes": [] }
  ]
}
```

**Expected:**

```json
[
  { "sku": "S1", "gtin": "8901234567890", "qtyEa": 20 },
  { "sku": "S2", "gtin": "8900000000001", "qtyEa": 3 }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
