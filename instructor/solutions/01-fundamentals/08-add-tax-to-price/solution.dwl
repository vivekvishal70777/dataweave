%dw 2.0
output application/json
var rate = 0.18
---
{
  price: payload.price,
  tax: payload.price * rate,
  total: payload.price * (1 + rate)
}
