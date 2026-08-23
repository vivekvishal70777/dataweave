%dw 2.0
output application/json
---
payload flatMap ((order) ->
  (order.items default []) map (item) -> {
    orderId: order.orderId,
    sku: item.sku,
    qty: item.qty as Number
  }
)
