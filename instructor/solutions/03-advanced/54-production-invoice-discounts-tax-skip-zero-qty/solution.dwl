%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var lines = payload.lines
  filter ((l) -> (l.qty as Number) > 0)
  map (l) -> do {
    var qty = l.qty as Number
    var price = l.price as Number
    var disc = (l.discountPct default 0) as Number
    ---
    l ++ { lineTotal: money(qty * price * (1 - disc)) }
  }
var subtotal = money(sum(lines.lineTotal))
var tax = money(subtotal * payload.taxRate)
---
{
  currency: payload.currency,
  lines: lines,
  subtotal: subtotal,
  tax: tax,
  grandTotal: money(subtotal + tax)
}
