%dw 2.0
output application/json
var bySku = payload.catalog groupBy ((c) -> c.sku)
fun explode(sku, visited) =
  if (visited contains sku)
    { sku: sku, cycle: true, missing: false, name: null, children: [] }
  else do {
    var c = (bySku[sku] default [])[0]
    ---
    if (c == null)
      { sku: sku, cycle: false, missing: true, name: null, children: [] }
    else {
      sku: sku,
      name: c.name,
      cycle: false,
      missing: false,
      children: (c.components default []) map explode($, visited ++ [sku])
    }
  }
---
explode(payload.parentSku, [])
