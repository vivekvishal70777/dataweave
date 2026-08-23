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
