# LAB 88 — Canonical product GTIN and UoM conversion

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/88-canonical-product-gtin-and-uom-conversion/` |
| Solution | `instructor/solutions/05-mapping/88-canonical-product-gtin-and-uom-conversion/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-88-canonical-product-gtin-and-uom-conversion.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 88. Canonical product GTIN and UoM conversion. qty in EA. If uom CS, multiply qty by packSize. gtin from first barcode type EAN13. Skip items without GTIN.

EAN13 barcode is GTIN. Case pack CS times packSize. Drop missing GTIN.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "items": [
    { "sku": "S1", "qty": 2, "uom": "CS", "packSize": 10, "barcodes": [{ "type": "UPC", "id": "x" }, { "type": "EAN13", "id": "8901234567890" }] },
    { "sku": "S2", "qty": 3, "uom": "EA", "packSize": 1, "barcodes": [{ "type": "EAN13", "id": "8900000000001" }] },
    { "sku": "S3", "qty": 1, "uom": "EA", "barcodes": [] }
  ]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 88 — Canonical product GTIN and UoM conversion**
> Folder: `student/labs/05-mapping/88-canonical-product-gtin-and-uom-conversion/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-88-canonical-product-gtin-and-uom-conversion-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload.items
  map (i) -> {
    sku: i.sku,
    gtin: (i.barcodes filter ((b) -> b.type == "EAN13"))[0].id,
    qtyEa: if (upper(i.uom default "EA") == "CS") (i.qty as Number) * (i.packSize default 1)
           else (i.qty as Number)
  }
  filter ((r) -> r.gtin != null)
```

**SAY:** That should match Expected:

```
[
  { "sku": "S1", "gtin": "8901234567890", "qtyEa": 20 },
  { "sku": "S2", "gtin": "8900000000001", "qtyEa": 3 }
]
```

## Part 4 — Interview phrase and close

**SAY:**

EAN13 barcode is GTIN. Case pack CS times packSize. Drop missing GTIN.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 89 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 88

Canonical product GTIN and UoM conversion

## Expected

```
[
  { "sku": "S1", "gtin": "8901234567890", "qtyEa": 20 },
  { "sku": "S2", "gtin": "8900000000001", "qtyEa": 3 }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
