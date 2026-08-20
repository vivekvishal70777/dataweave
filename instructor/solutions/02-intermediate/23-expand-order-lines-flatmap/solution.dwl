%dw 2.0
output application/json
---
payload flatMap ((order) ->
  order.items map (item) -> {
    orderId: order.orderId,
    sku: item.sku
  }
)
