%dw 2.0
output application/json
var lines = payload.lines map (l) -> l ++ { lineTotal: l.qty * l.price }
var subtotal = sum(lines.lineTotal)
var tax = subtotal * payload.taxRate
---
{
  lines: lines,
  subtotal: subtotal,
  tax: tax,
  grandTotal: subtotal + tax
}
