%dw 2.0
import try from dw::Runtime
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
fun lineOk(l) =
  try(() -> (l.qty as Number) >= 0 and (l.price as Number) >= 0).success default false
var parsed = payload.lines map (l) -> {
  sku: l.sku,
  ok: lineOk(l),
  qty: try(() -> l.qty as Number).result,
  price: try(() -> l.price as Number).result
}
var good = parsed filter $.ok map (l) -> {
  sku: l.sku,
  qty: l.qty,
  price: l.price,
  lineTotal: money(l.qty * l.price)
}
var subtotal = money(sum(good.lineTotal default []))
var tax = money(subtotal * payload.taxRate)
---
{
  correlationId: payload.correlationId,
  customerId: payload.customerId default null,
  lines: good,
  subtotal: subtotal,
  tax: tax,
  grandTotal: money(subtotal + tax),
  errors: parsed filter !$.ok map {
    sku: $.sku,
    reason: "qty or price is not numeric"
  }
}
