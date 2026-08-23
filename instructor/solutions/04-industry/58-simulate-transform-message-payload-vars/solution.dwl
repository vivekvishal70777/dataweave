%dw 2.0
output application/json
var canonical = {
  orderId: payload.order.id,
  amount: payload.order.amount as Number
}
---
{
  payload: canonical,
  vars: {
    correlationId: payload.headers.xCorrelationId default "missing",
    recordCount: 1
  }
}
