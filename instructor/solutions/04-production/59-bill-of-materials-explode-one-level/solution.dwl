%dw 2.0
output application/json
var bySku = payload.catalog groupBy ((c) -> c.sku)
var parent = bySku[payload.parentSku][0]
fun part(sku) = do {
  var c = (bySku[sku] default [])[0]
  ---
  {
    sku: sku,
    name: c.name default null,
    unitCost: c.unitCost default null,
    missing: c == null
  }
}
var exploded = (parent.components default []) map part($)
---
{
  sku: parent.sku,
  name: parent.name,
  exploded: exploded,
  bomCost: sum((exploded filter !$.missing).unitCost)
}
