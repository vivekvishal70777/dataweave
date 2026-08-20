%dw 2.0
import leftJoin from dw::core::Arrays
output application/json
---
leftJoin(payload.orders, payload.customers, (o) -> o.customerId, (c) -> c.id)
  map {
    orderId: $.l.id,
    customerName: $.r.name default null
  }
