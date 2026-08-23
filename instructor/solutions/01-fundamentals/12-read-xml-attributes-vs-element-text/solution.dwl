%dw 2.0
output application/json
---
{
  id: payload.order.@id,
  amount: payload.order.amount as Number
}
