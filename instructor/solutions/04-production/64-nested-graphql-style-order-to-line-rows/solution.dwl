%dw 2.0
output application/json
---
payload.order.lines
  filter ((l) -> (l.qty as Number) > 0)
  map (l) -> {
    orderId: payload.order.id,
    customer: payload.order.customer,
    sku: l.sku,
    qty: l.qty as Number
  }
