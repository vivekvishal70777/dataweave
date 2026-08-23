%dw 2.0
output application/json
var rate = 0.18
fun money(n: Number) = n as String {format: "0.00"} as Number
---
{
  price: money(payload.price),
  tax: money(payload.price * rate),
  total: money(payload.price * (1 + rate))
}
