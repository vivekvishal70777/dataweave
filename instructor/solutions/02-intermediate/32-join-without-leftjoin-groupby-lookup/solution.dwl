%dw 2.0
output application/json
var byId = payload.customers groupBy ((c) -> c.id)
---
payload.orders map (o) -> {
  orderId: o.id,
  customerName: (byId[o.customerId][0].name) default null
}
