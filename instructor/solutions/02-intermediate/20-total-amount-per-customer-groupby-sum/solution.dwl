%dw 2.0
output application/json
---
payload groupBy ((o) -> o.customerId)
  pluck ((orders, customerId) -> {
    customerId: customerId,
    orderCount: sizeOf(orders),
    total: sum(orders.amount map ($ as Number))
  })
