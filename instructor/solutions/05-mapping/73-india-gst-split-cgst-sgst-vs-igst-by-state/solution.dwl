%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var t = payload.taxable as Number
var intra = payload.fromState == payload.toState
---
{
  taxable: money(t),
  cgst: if (intra) money(t * 0.09) else 0.00,
  sgst: if (intra) money(t * 0.09) else 0.00,
  igst: if (intra) 0.00 else money(t * 0.18)
}
