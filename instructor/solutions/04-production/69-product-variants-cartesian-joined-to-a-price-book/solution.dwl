%dw 2.0
output application/json
var priceBySku = payload.prices groupBy ((p) -> p.sku)
---
payload.products
  filter ((p) -> p.active)
  flatMap ((p) ->
    p.colors flatMap ((c) ->
      p.sizes map (s) -> do {
        var sku = p.id ++ "-" ++ c ++ "-" ++ s
        var price = priceBySku[sku][0].price
        ---
        if (price == null) null
        else { sku: sku, productId: p.id, color: c, size: s, price: price }
      }
    )
  )
  filter $ != null
