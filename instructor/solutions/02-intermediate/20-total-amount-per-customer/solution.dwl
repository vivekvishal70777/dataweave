%dw 2.0
output application/json
---
payload groupBy ((o) -> o.customerId)
  pluck ((orders, customerId) -> {
    customerId: customerId,
    total: sum(orders.amount)
  })
