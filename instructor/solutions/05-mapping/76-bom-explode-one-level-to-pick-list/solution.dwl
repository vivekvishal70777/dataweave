%dw 2.0
output application/json
var byP = payload.bom groupBy $.parent
---
payload.orders
  flatMap ((o) ->
    (byP[o.sku] default []) map (b) -> {
      component: b.component,
      qty: (o.qty as Number) * (b.per as Number)
    }
  )
